from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import BoardModel, CommentModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.


def signupFunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            User.objects.create_user(username, '', password)
            return render(request, 'signup.html', {'some': 100})
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーは登録されています'})
    return render(request, 'signup.html', {'some': 100})


def loginFunc(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = User.objects.get(email=email.lower()).username
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html', {'error': 'メールアドレスまたはパスワードが異なります'})
    return render(request, 'login.html', {})


def logoutFunc(request):
    logout(request)
    return redirect('login')


@login_required
def listFunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list': object_list})


@login_required
def detailFunc(request, pk):
    boardDetail = get_object_or_404(BoardModel, pk=pk)
    files = boardDetail.file
    commentsQuerySet = CommentModel.objects.filter(board=boardDetail)
    comments = commentsQuerySet.values()
    return render(request, 'detail.html', {'boardDetail': boardDetail, 'comments': comments, 'file': files})

@login_required
def newCommentFunc(request, pk):
    print('11111')
    if request.method == 'POST':
        comment = request.POST['comment']
        board = get_object_or_404(BoardModel, pk=pk)
        print('asdf')
        CommentModel.objects.create(comment=comment, board=board)
    return redirect('detail', pk=pk)

@login_required
def goodFunc(request, pk):
    object = get_object_or_404(BoardModel, pk=pk)
    object.good = object.good + 1
    object.save()
    return redirect('list')


@login_required
def readFunc(request, pk):
    object = get_object_or_404(BoardModel, pk=pk)
    username = request.user.get_username()
    if username in object.readText:
        return redirect('list')
    else:
        object.read = object.read + 1
        object.readText = object.readText + ' ' + username
        object.save()
        return redirect('list')


class BoardCreate(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ('title', 'content', 'author', 'file')
    success_url = reverse_lazy('list')
