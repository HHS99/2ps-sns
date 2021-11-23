from django.urls import path
from .views import signupFunc, loginFunc, listFunc, logoutFunc

urlpatterns = [
    path('signup/', signupFunc, name='signup'),
    path('login/', loginFunc, name='login'),
    path('list/', listFunc, name='list'),
    path('logout/', logoutFunc, name='logout'),
]
