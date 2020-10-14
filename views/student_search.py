import swapper
from itertools import chain

from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

from kernel.models.roles.student import Student
from kernel.models import ResidentialInformation
from student_biodata.models.miscellaneous.interest import Interest

from people_search.serializers.student_serializer import StudentSerializer
from people_search.models.profile import Profile
from people_search.utils.student_filters import StudentFilter
from people_search.permissions.has_room_no_permissions import has_room_no_permission
from people_search.permissions.has_bhawan_permissions import has_bhawan_permission

Student = swapper.load_model('kernel','Student')                
        
class StudentSearch(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = StudentFilter
    
    def get_queryset(self):
        
        query = self.request.query_params.get('query',None)

        if((query!=None)):
            
            result_matches = Profile.objects.filter(Q(student__person__full_name__icontains=query) |
                                                    Q(student__enrolment_number__icontains = query) |
                                                    Q(student__current_year__icontains = query) |
                                                    Q(student__branch__name__icontains = query) | 
                                                    Q(student__person__contact_information__email_address__icontains = query)
                                                    )

            interest_results = Interest.objects.filter(Q(topic__icontains=query))
            
            for interest in interest_results:
                student_id = interest.student
                _ = Profile.objects.get(student = student_id)
                if(_ not in result_matches):
                    result_matches |= Profile.objects.get(student = student_id)
                                
            room_number_results = ResidentialInformation.objects.filter(Q(room_number__icontains = query))
            
            for room_number_result in room_number_results:
                student_id = room_number_result.person.student
                _ = Profile.objects.get(student = student_id)
                if((_ not in result_matches) and (has_room_no_permission(self.request, _))):
                    result_matches |= Profile.objects.filter(student = student_id)
                    
            bhawan_results = ResidentialInformation.objects.filter(Q(residence__code__icontains = query))
            
            for bhawan_result in bhawan_results:
                student_id = bhawan_result.person.student
                _ = Profile.objects.get(student = student_id)
                if((_ not in result_matches) and (has_bhawan_permission(self.request, _))):
                    result_matches |= Profile.objects.filter(student = student_id)
                    
            # print(result_matches)
            return result_matches
        else:
            return Profile.objects.all()
