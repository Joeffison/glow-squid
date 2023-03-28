from django.db.models import deletion
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from projects.models import Project
from projects.serializers import ProjectSerializer


@api_view(['GET', 'POST'])
def project_list(request):
    if request.method == 'GET':
        projects = Project.objects.all()

        serializer = ProjectSerializer(projects, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def project_detail(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialier = ProjectSerializer(project)
        return Response(serialier.data)

    elif request.method == 'PUT':
        serialier = ProjectSerializer(project, data=request.data)

        if serialier.is_valid():
            serialier.save()
            return Response(serialier.data)

        return Response(serialier.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            project.delete()
        except deletion.ProtectedError:
            # this was a business decision. An alternative is to use cascade deletion
            error = 'Cannot delete project with associated WTGs. Delete the WTGs first.'
            return Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
