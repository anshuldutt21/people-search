import swapper

from rest_framework import serializers

from omniport.utils import switcher
from formula_one.models import ContactInformation
from kernel.models import ResidentialInformation
from student_biodata.models.miscellaneous.interest import Interest

from people_search.models.profile import Profile
from people_search.permissions.has_email_permission import has_email_permission
from people_search.permissions.has_mobile_no_permissions import has_mobile_no_permission
from people_search.permissions.has_room_no_permissions import has_room_no_permission
from people_search.permissions.has_bhawan_permissions import has_bhawan_permission

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

    display_picture = serializers.ImageField(
        source='student.person.display_picture',
        read_only=True
    )

    def get_email_address(self, instance):
        try:
            if(has_email_permission(self.context['request'], instance)):
                return instance.student.person.contact_information.get().email_address

        except (ContactInformation.DoesNotExist, TypeError) as error:
            return None

    interests = serializers.SerializerMethodField()

    def get_interests(self, instance):
        try:
            return list(
                Interest.objects.filter(
                    student=instance.student).values_list(
                    'topic', flat=True))

        except (Interest.DoesNotExist, TypeError) as error:
            return None

    mobile_number = serializers.SerializerMethodField()

    def get_mobile_number(self, instance):
        try:
            if(has_mobile_no_permission(self.context['request'], instance)):
                return instance.student.person.contact_information.get().primary_phone_number

        except (ContactInformation.DoesNotExist, TypeError) as error:
            return None

    room_no_information = serializers.SerializerMethodField()

    def get_room_no_information(self, instance):
        try:
            if(has_room_no_permission(self.context['request'], instance)) and (has_bhawan_permission(self.context['request'], instance)):
                return ResidentialInformation.objects.get(
                    person=instance.student.person).room_number

        except (ResidentialInformation.DoesNotExist, TypeError) as error:
            return None

    bhawan_information = serializers.SerializerMethodField()

    def get_bhawan_information(self, instance):
        try:
            if(has_bhawan_permission(self.context['request'], instance)):
                return ResidentialInformation.objects.get(
                    person=instance.student.person).residence.name

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
            'interests',
            'mobile_number',
            'room_no_information',
            'bhawan_information',
            'display_picture',
            'primary_email_id',
            'primary_mobile_no',
            'room_no',
            'bhawan'
        ]
