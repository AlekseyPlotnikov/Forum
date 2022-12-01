from django.shortcuts import render, redirect
from .models import *
from .forms import *


def home(request):
    forums = Forum.objects.all()
    count = forums.count()
    discussions = []
    for i in forums:
        discussions.append((i.discussion_set.all()))
    context = {
        'forums': forums,
        'count': count,
        'discussions': discussions
    }
    return render(request, 'home.html', context)


def addForum(request):
    form = CreateForum()
    if request.method == 'POST':
        form = CreateForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'addForum.html', context)


def addDiscussion(request):
    form = CreateDiscussion()
    if request.method == 'POST':
        form = CreateDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'addDiscussion.html', context)
