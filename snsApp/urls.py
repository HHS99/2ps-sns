from django.urls import path
from .views import signupFunc, loginFunc

urlpatterns = [
    path('signup/', signupFunc),
    path('login/', loginFunc),
]
