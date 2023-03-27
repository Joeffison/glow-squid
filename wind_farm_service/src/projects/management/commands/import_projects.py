import argparse

import numpy as np
import pandas as pd

from django.core.management.base import BaseCommand
import django.db.utils

from projects.models import Project


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        projects = self._get_projects_from_file(options['file'])

        self._save_projects(projects)

    def _get_projects_from_file(self, file):
        df = self._read_input_file(file)
        yield from df.apply(self._serialize, axis=1)

    def _read_input_file(self, file):
        df = pd.read_csv(file, parse_dates=['acquisition_date'], dayfirst=True)
        df.replace([np.nan], [None], inplace=True)

        return df

    def _serialize(self, project_specs):
        return Project(
            id=project_specs['id'],
            name=project_specs['project_name'],
            number=project_specs['project_number'],
            acquisition_date=project_specs['acquisition_date'],
            number_3l_code=project_specs['number_3l_code'],
            deal_type_id=project_specs['project_deal_type_id'],
            group_id=project_specs['project_group_id'],
            status_id=project_specs['project_status_id'],
            company_id=project_specs['company_id'],
        )

    def _save_projects(self, projects):
        for project in projects:
            try:
                project.save()
            except django.db.utils.IntegrityError as err:
                self.stderr.write(f'Project {project.name} could not be imported due to: {err!r}')
            else:
                self.stdout.write(f'Project {project.name} imported successfully')
