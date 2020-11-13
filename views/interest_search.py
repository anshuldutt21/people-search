import swapper
from itertools import chain

from django.db.models import Q

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

from student_biodata.models.miscellaneous.interest import Interest

from people_search.serializers.student_serializer import StudentSerializer
from people_search.models.profile import Profile

Student = swapper.load_model('kernel', 'Student')


class InterestSearch(viewsets.ModelViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):

        query = self.request.query_params.get('query', None)
        if(query is not None):
            result_matches = []
            interest_results = Interest.objects.filter(
                Q(topic__icontains=query))

            for interest in interest_results:
                student_id = interest.student
                _ = Profile.objects.get(student=student_id)
                result_matches.append(_)
                return result_matches
        else:
            return []
