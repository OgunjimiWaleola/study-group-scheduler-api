from rest_framework import serializers
from .models import StudyGroup

class StudyGroupSerializer(serializers.ModelSerializer):
    participants_count = serializers.SerializerMethodField()

    class Meta:
        model = StudyGroup
        fields = "__all__"
        read_only_fields = ("created_by",)

    def get_participants_count(self, obj):
        return obj.participants.count()
