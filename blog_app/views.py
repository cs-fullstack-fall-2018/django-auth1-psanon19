from django.shortcuts import render
from .models import BlogModel
from django.contrib.auth.decorators import login_required


def index(request):
    form_list = BlogModel.objects.all()
    context = {'form_list': form_list}
    return render(request, 'blog_app/index.html', context)


def userindex(request):
    form_list = BlogModel.objects.filter(username=request.user)
    context = {'form_list': form_list}
    return render(request, 'blog_app/index.html', context)