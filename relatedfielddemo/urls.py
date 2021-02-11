from django.urls import path, include
from rest_framework import routers
from .views import QuestionSetViewSet, QuestionViewSet

app_name = 'relatedfielddemo'

router = routers.DefaultRouter(trailing_slash=False)
router.register('questionsets', QuestionSetViewSet)
router.register('questions', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
