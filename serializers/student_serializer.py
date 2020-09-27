import swapper

from rest_framework import serializers

from omniport.utils import switcher
from formula_one.models import ContactInformation
from kernel.models import ResidentialInformation

from people_search.models.profile import Profile

Student = swapper.load_model('kernel', 'Student')
BaseSerializer = switcher.load_serializer('kernel', 'Student')

class StudentSerializer(serializers.ModelSerializer):
    """
    Serializer that serializes Student objects
    """

    full_name = serializers.CharField(
        source='student.person.full_name',
        read_only=True,
    )
    
    branch_name = serializers.CharField(
    source='student.branch.name',
    read_only=True
    )

    current_year = serializers.CharField(
        source='student.current_year',
        read_only=True
    )
    
    enrolment_number = serializers.IntegerField(
        source='student.enrolment_number',
        read_only=True
    )
        
    email_address = serializers.SerializerMethodField()
    
    def get_email_address(self, instance):        
        try:
            return instance.student.person.contact_information.get().email_address
        
        except (ContactInformation.DoesNotExist, TypeError) as error:
            return None
    
    mobile_number = serializers.SerializerMethodField()
            
    def get_mobile_number(self, instance):
        try:
            return instance.student.person.contact_information.get().primary_phone_number

        except (ContactInformation.DoesNotExist, TypeError) as error:
            return None
        
    residential_information = serializers.SerializerMethodField()
    
    def get_residential_information(self, instance):
        try:
            return {
                'residence' : ResidentialInformation.objects.get(person = instance.student.person).residence.name,
                'room_number' : ResidentialInformation.objects.get(person = instance.student.person).room_number
            }

        except (ResidentialInformation.DoesNotExist, TypeError) as error:
            return None
        


    class Meta:
        model = Profile

        fields = [
            'id',
            'student',
            'full_name',
            'email_address',
            'branch_name',
            'current_year',
            'enrolment_number',
            'mobile_number',
            'residential_information'
        ]
