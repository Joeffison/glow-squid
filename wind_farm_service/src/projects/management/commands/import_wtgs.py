import argparse

import numpy as np
import pandas as pd

from django.core.management.base import BaseCommand
import django.db.utils

from projects.models import WTG


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        projects = self._get_wtgs_from_file(options['file'])

        self._save_wtgs(projects)

    def _get_wtgs_from_file(self, file):
        df = self._read_input_file(file)
        yield from df.apply(self._serialize, axis=1)

    def _read_input_file(self, file):
        df = pd.read_csv(file, parse_dates=['COD'], dayfirst=True)
        df.replace([np.nan], [None], inplace=True)

        return df

    def _serialize(self, specs):
        return WTG(
            wtg_number=specs['WTG_number'],
            project_id=specs['project_id'],
            type_id=specs['WTG_Type_id'],
            region_id=specs['Region_id'],
            kw=specs['kW'],
            hub=specs['hub'],
            rotor=specs['rotor'],
            altitude=specs['altitude'],
            cod=specs['COD'],
            zip_code=specs['zip_code'],
            wgs_84_north=specs['WGS_84_north'],
            wgs_84_east=specs['WGS_84_east'],
            gauss_krueger_zone=specs['gauss_krueger_zone'],
            gauss_krueger_north=specs['gauss_krueger_north'],
            gauss_krueger_east=specs['gauss_krueger_east'],
            town_id=specs['town_id'],
        )

    def _save_wtgs(self, wtgs):
        for wtg in wtgs:
            try:
                wtg.save()
            except django.db.utils.IntegrityError as err:
                self.stderr.write(f'WTG {wtg.wtg_number} could not be imported due to: {err!r}')
            else:
                self.stdout.write(f'WTG {wtg.wtg_number} imported successfully')
