import swapper

from django.db.models import Q

from rest_framework import status
from rest_framework import viewsets

from people_search.serializers.student_detail_serializer import StudentDetailSerializer
from people_search.models.profile import Profile

class StudentDetailSearch(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = StudentDetailSerializer
    lookup_field = 'student__enrolment_number'
