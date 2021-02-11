from rest_framework import viewsets, permissions
from .models import Question, QuestionSet
from .serializers import QuestionSerializer, QuestionSetSerializer

# Create your views here.


class QuestionSetViewSet(viewsets.ModelViewSet):
    queryset = QuestionSet.objects.all()
    serializer_class = QuestionSetSerializer
    permission_classes = [permissions.AllowAny]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.AllowAny]
