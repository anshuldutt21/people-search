import swapper

from rest_framework import filters
from itertools import chain

from django.db.models import Q

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND

from kernel.models.roles.student import Student
from people_search.serializers.student_serializer import StudentSerializer
from people_search.serializers.faculty_serializer import FacultySerializer
#from people_search.serializers.student_search_serializer import StudentSearchSerializer
from people_search.models.profile import Profile

Student = swapper.load_model('kernel','Student')
FacultyMember = swapper.load_model('kernel', 'FacultyMember')

class StudentProfile(viewsets.ModelViewSet):
    serializer_class = FacultySerializer
    queryset = Profile.objects.all()
    def get_queryset(self):

        enrol = self.request.query_params.get('query',None)
        print(enrol)
        if enrol is not None:
            result = FacultyMember.objects.get(employee_id=enrol)
            return result
        else:
            return FacultyMember.objects.all()
