from rest_framework import serializers

from projects.models import Project, WTG


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'name', 'number', 'acquisition_date', 'number_3l_code', 'deal_type_id',
                  'group_id', 'status_id', 'company_id', 'wtg_numbers', 'total_kw',
                  'months_acquired')
