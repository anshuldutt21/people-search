import django_filters

from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend

from kernel.models import ResidentialInformation

from people_search.models.profile import Profile


class StudentFilter(django_filters.FilterSet):
    residence = django_filters.CharFilter(field_name='residence__code', method = 'custom_filter')
    branch = django_filters.CharFilter(field_name = 'student__branch__name')
    current_year = django_filters.CharFilter(field_name = 'student__current_year')
    
    class Meta:
        model = Profile
        fields = [
                'branch', 'current_year', 'residence'
                ]

    def custom_filter(self, queryset, name, value):
        bhawans = ResidentialInformation.objects.filter(residence__code = value)
        updated_queryset = Profile.objects.none()
        
        for bhawan in bhawans:
            student_id = bhawan.person.student
            _ = Profile.objects.get(student = student_id)
            if(_ in queryset):
                updated_queryset |= Profile.objects.filter(student = student_id)
            
        return updated_queryset

