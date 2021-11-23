from django.urls import path
from .views import signupFunc, loginFunc, listFunc

urlpatterns = [
    path('signup/', signupFunc, name='signup'),
    path('login/', loginFunc, name='login'),
    path('list/', listFunc, name='list'),
]
