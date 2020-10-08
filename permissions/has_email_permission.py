from rest_framework import permissions

from kernel.models import ResidentialInformation
from kernel.managers.get_role import get_role
from formula_one.mixins.period_mixin import ActiveStatus

from people_search.permissions.is_student import get_is_student
from people_search.permissions.is_faculty import get_is_faculty_member

def has_email_permission(request, obj):
    if(obj.primary_email_id=='all'):
        return True
    
    elif(obj.primary_email_id=='students'):
        return get_is_student(request.person)
    
    elif(obj.primary_email_id=='faculty'):
        return get_is_faculty_member(request.person)
    
    elif(obj.primary_email_id=='bhawan'):
        try:
            bhawan_people_search_user = ResidentialInformation.objects.get(person = obj.student.person).residence.name
            bhawan_loggged_in_user = ResidentialInformation.objects.get(person = request.person).residence.name
            return str(bhawan_loggged_in_user)==str(bhawan_people_search_user)
        except:
            return False
        
    elif(obj.primary_email_id=='branch'):
        try:
            return str(obj.student.branch.name)==str(request.person.student.branch.name)
        except:
            return False
        
