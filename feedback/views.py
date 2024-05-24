from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import Feedback
from .serializers import FeedbackSerializer


class FeedbackViewset(GenericViewSet, CreateModelMixin):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
