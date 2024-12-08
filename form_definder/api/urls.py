from django.urls import path
from .views import FormMatchView


urlpatterns = [
    path("get_form/", FormMatchView.as_view(), name="get_form"),
]