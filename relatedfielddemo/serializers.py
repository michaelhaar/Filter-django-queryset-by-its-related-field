from rest_framework import serializers
from .models import Question, QuestionSet


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'is_archived', 'question_set']


class QuestionSetSerializer(serializers.ModelSerializer):
    inactive_questions = serializers.SerializerMethodField()

    class Meta:
        model = QuestionSet
        fields = ['id', 'inactive_questions']

    def get_inactive_questions(self, obj):
        active_questions = obj.questions.filter(is_archived=True)
        return QuestionSerializer(active_questions, many=True, read_only=True).data
