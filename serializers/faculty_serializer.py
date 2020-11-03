import swapper
from rest_framework import serializers

from omniport.utils import switcher

FacultyMember = swapper.load_model('kernel', 'FacultyMember')
BaseSerializer = switcher.load_serializer('kernel', 'FacultyMember')


class FacultySerializer(BaseSerializer):
    """
    Serializer that serializes FacultyMember objects
    """

    name = serializers.CharField(
        source='person.full_name',
        read_only=True,
    )

    display_picture = serializers.ImageField(
        source='person.display_picture',
        read_only=True
    )

    class Meta:
        model = FacultyMember

        fields = [
            'employee_id',
            'name',
            'department',
            'designation',
            'entity_content_type',
            'entity_object_id',
            'display_picture'
        ]
