import swapper
from itertools import chain

from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND

from people_search.serializers.faculty_serializer import FacultySerializer
from people_search.utils.faculty_filters import FacultyFilter

FacultyMember = swapper.load_model('kernel', 'FacultyMember')

class FacultySearch(viewsets.ModelViewSet):
    serializer_class = FacultySerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = FacultyFilter
    lookup_field = 'employee_id'
    
    def get_queryset(self):

        query = self.request.query_params.get('query', None)
        if(query!=None):
            results = FacultyMember.objects.filter(Q(person__full_name__icontains=query))
            return results
        else:
            return FacultyMember.objects.all()
