from django.urls import path
from .views import signupFunc, loginFunc, listFunc, logoutFunc, detailFunc, goodFunc

urlpatterns = [
    path('signup/', signupFunc, name='signup'),
    path('login/', loginFunc, name='login'),
    path('list/', listFunc, name='list'),
    path('logout/', logoutFunc, name='logout'),
    path('detail/<int:pk>', detailFunc, name='detail'),
    path('good/<int:pk>', goodFunc, name='good'),
]
