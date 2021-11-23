from django.urls import path
from .views import signupFunc, loginFunc, listFunc

urlpatterns = [
    path('signup/', signupFunc),
    path('login/', loginFunc),
    path('list/', listFunc),
]
