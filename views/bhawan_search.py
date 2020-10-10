import swapper
from itertools import chain

from django.db.models import Q

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

from kernel.models import ResidentialInformation

from people_search.serializers.student_serializer import StudentSerializer
from people_search.models.profile import Profile

Student = swapper.load_model('kernel','Student')

class BhawanSearch(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    
    def get_queryset(self):
        
        query = self.request.query_params.get('query',None)
        if(query!=None):
            result_matches = []
            interest_results = Interest.objects.filter(Q(topic__icontains = query))
            
            for bhawan_result in bhawan_results:
                student_id = bhawan_result.person.student
                _ = Profile.objects.get(student = student_id)
                if((_ not in result_matches) and (has_bhawan_permission(self.request, _))):
                    result_matches.append(_)
            return result_matches
        else:
            return []
