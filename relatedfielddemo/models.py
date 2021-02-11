from django.db import models

# Create your models here.


class QuestionSet(models.Model):
    pass


class Question(models.Model):
    question_set = models.ForeignKey(
        QuestionSet, related_name="questions", on_delete=models.CASCADE)
    is_archived = models.BooleanField(default=False)
