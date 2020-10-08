import swapper
from itertools import chain

from django.db.models import Q

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND

from kernel.models.roles.student import Student
from kernel.models import ResidentialInformation

from people_search.serializers.student_serializer import StudentSerializer
from people_search.models.profile import Profile

Student = swapper.load_model('kernel','Student')

class StudentSearch(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Profile.objects.all()
    
    def get_queryset(self):
        
        query = self.request.query_params.get('query',None)
        if(query!=None):
            results = Profile.objects.filter(Q(student__person__full_name__icontains=query) | 
                                             Q(student__enrolment_number__icontains = query) | 
                                             Q(student__current_year__icontains = query) |
                                             Q(student__branch__name__icontains = query) | 
                                             Q(student__person__contact_information__email_address__icontains = query)
                                             )
            return results
        else:
            return Profile.objects.all()
