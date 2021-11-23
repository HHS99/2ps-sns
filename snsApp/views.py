from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def signupFunc(request):
  object_list = User.objects.all()
  if request.method == "POST":
    print('this is post')
  else:
    print('this is not post')
  return render(request, 'signup.html', {'some': 100})