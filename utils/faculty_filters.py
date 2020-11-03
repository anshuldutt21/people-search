import swapper
import django_filters

from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend

from kernel.models import ResidentialInformation

from people_search.models.profile import Profile

FacultyMember = swapper.load_model('kernel', 'FacultyMember')
Centre = swapper.load_model('shell', 'Centre')
Department = swapper.load_model('shell', 'Department')

class FacultyFilter(django_filters.FilterSet):
    department = django_filters.CharFilter(field_name='department', method = 'custom_filter')
    designation = django_filters.CharFilter(field_name = 'designation')
    
    class Meta:
        model = FacultyMember
        fields = [
                'department', 'designation'
                ]

    def custom_filter(self, queryset, name, value):
        faculties = FacultyMember.objects.all()
        updated_queryset = FacultyMember.objects.none()

        for faculty in faculties:
            if faculty.entity_content_type.name == 'centre':
                try:
                    centre_id = Centre.objects.get(code = value).id
                    if(centre_id == faculty.entity_object_id):
                        updated_queryset |= FacultyMember.objects.filter(id=faculty.id)
                
                except:
                    continue
                    
            elif faculty.entity_content_type.name == 'department':
                try:
                    dept_id = Department.objects.get(code = value).id
                    if(dept_id == faculty.entity_object_id):
                        updated_queryset |= FacultyMember.objects.filter(id=faculty.id)
                
                except:
                    continue
        
        return updated_queryset
