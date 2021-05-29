from django.urls import path
from .views import WatsonList
from .views import WatsonCreate
from .views import WatsonDetail

urlpatterns = [
    path("", WatsonList.as_view(), name="list"),
    path("detail/<int:pk>", WatsonDetail.as_view(), name="detail"),
    path("create/", WatsonCreate.as_view()),
]
