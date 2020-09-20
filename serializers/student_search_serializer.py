import swapper

from rest_framework import serializers

from people_search.serializers.student_serializer import StudentSerializer
from people_search.models.profile import Profile

Student = swapper.load_model('kernel','Student')

class StudentSearchSerializer(serializers.ModelSerializer):
    """
    Serializer that serializes the Student search query.
    """

    class Meta:
        model = Profile
        fields = '__all__'

    def to_representation(self, obj):
        if isinstance(obj, Profile):
            serializer = StudentSerializer(obj)
        else:
            raise Exception("No match found.")
        return serializer.data
