from rest_framework.response import Response
from rest_framework.decorators import api_view

from projects.models import Project
from projects.serializers import ProjectSerializer


@api_view(['GET'])
def get_projects(request):
    projects = Project.objects.all()

    serializer = ProjectSerializer(projects, context={'request': request}, many=True)

    return Response(serializer.data)
