import swapper
from itertools import chain

from django.db.models import Q

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND

from people_search.serializers.faculty_serializer import FacultySerializer

FacultyMember = swapper.load_model('kernel', 'FacultyMember')

class FacultySearch(viewsets.ModelViewSet):
    serializer_class = FacultySerializer
    lookup_field = 'employee_id'
    
    def get_queryset(self):

        query = self.request.query_params.get('query', None)
        if(query!=None):
            results = FacultyMember.objects.filter(Q(person__full_name__icontains=query))
            return results
        else:
            return FacultyMember.objects.all()
