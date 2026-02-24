from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import StudyGroup
from .serializers import StudyGroupSerializer

class StudyGroupViewSet(ModelViewSet):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone

    @action(detail=True, methods=['post'])
    def join(self, request, pk=None):
        group = self.get_object()

        if group.scheduled_date < timezone.now():
            return Response({"error": "Cannot join past group"}, status=400)

        if group.participants.count() >= group.max_participants:
            return Response({"error": "Group is full"}, status=400)

        if request.user in group.participants.all():
            return Response({"error": "Already joined"}, status=400)

        group.participants.add(request.user)
        return Response({"message": "Joined group successfully"})


    @action(detail=True, methods=['post'])
    def leave(self, request, pk=None):
        group = self.get_object()
        group.participants.remove(request.user)
        return Response({"message": "Left group"})