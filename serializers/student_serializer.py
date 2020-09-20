import swapper

from rest_framework import serializers

from omniport.utils import switcher
from formula_one.models import ContactInformation

from people_search.models.profile import Profile

Student = swapper.load_model('kernel', 'Student')
BaseSerializer = switcher.load_serializer('kernel', 'Student')

class StudentSerializer(serializers.ModelSerializer):
    """
    Serializer that serializes Student objects
    """

    full_name = serializers.CharField(
        source='person.full_name',
        read_only=True,
    )
    
    branch_name = serializers.CharField(
    source='person.student.branch.name',
    read_only=True
    )

    current_year = serializers.CharField(
        source='person.student.current_year',
        read_only=True
    )
    
    enrolment_number = serializers.IntegerField(
        source='person.student.enrolment_number',
        read_only=True
    )
        
    email_address = serializers.SerializerMethodField()
    
    def get_email_address(self, instance):        
        try:
            return instance.person.contact_information.get().email_address
        
        except (ContactInformation.DoesNotExist, TypeError) as error:
            return None
        
        
    class Meta:
        model = Profile

        fields = [
            'id',
            'person',
            'full_name',
            'email_address',
            'branch_name',
            'current_year',
            'enrolment_number',
        ]
