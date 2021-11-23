from django.urls import path
from .views import signupFunc

urlpatterns = [
    path('signup/', signupFunc),
]
