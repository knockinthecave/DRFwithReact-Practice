from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import WorkerList, WorkerDetail

urlpatterns = [
    path('worker/', WorkerList.as_view()),
    path('worker/<int:wid>/', WorkerDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
