from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signupFunc, name='signup'),
    path('login/', views.loginFunc, name='login'),
    path('list/', views.listFunc, name='list'),
    path('logout/', views.logoutFunc, name='logout'),
    path('detail/<int:pk>', views.detailFunc, name='detail'),
    path('new_comment/<int:pk>', views.newCommentFunc, name='newComment'),
    path('create/', views.BoardCreate.as_view(), name='create'),
    path('remove/<int:pk>', views.removeFunc, name='remove'),
]
