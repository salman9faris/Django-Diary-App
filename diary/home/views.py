from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from .form import NewUserForm, Diaryform
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .models import Diaryy

@login_required(login_url='/signin')
def home(request):
    obj = Diaryy.objects.filter(user_name=request.user)
    context = {
        "obj": obj
    }
    template = "index.html"
    return render(request, template, context)


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your profile is updated successfully!')
            return redirect("home")
        else:
            form = NewUserForm(request.POST)
            context = {"form": form}
            messages.success(request, 'invalid password!')
            templates = "register.html"
            return render(request, templates, context)
    form = NewUserForm
    context = {"form": form}
    templates = "register.html"
    return render(request, templates, context)


def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "inavlid username or password")
        else:
            messages.error(request, "invalid credential")
    form = AuthenticationForm()
    context = {"form": form}
    templates = "login.html"
    return render(request, templates, context)


def logout_request(request):
    logout(request)
    messages.error(request, "Logout successfully")
    return redirect("signin")

@login_required(login_url='/signin')
def diary(request):
    form = Diaryform()
    if request.method == "POST":
        form = Diaryform(request.POST or None)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.user_name = request.user
            forms.save()
            return redirect("home")
    context = {
        "form": form
    }
    return render(request, "diary.html", context)

@login_required(login_url='/signin')
def delete_conform(request, id):
    obj = Diaryy.objects.get(id=id)
    context = {"obj": obj}
    return render(request, 'conform.html', context)

@login_required(login_url='/signin')
def delete_diary(request, id):
    obj = Diaryy.objects.get(id=id)
    obj.delete()
    return redirect("home")

@login_required(login_url='/signin')
def edit(request, id):
    obj = Diaryy.objects.get(id=id)
    form = Diaryform(request.POST or None, instance=obj)
    if form.is_valid():
        forms = form.save(commit=False)
        forms.user_name = request.user
        forms.save()
        return redirect("home")
    context = {
        "form": form
    }
    return render(request, "diary.html", context)
@login_required(login_url='/signin')
def search(request):
    query=request.GET.get("search",None)
    obj = Diaryy.objects.filter(user_name=request.user)
    if query is not None:
        obj=obj.filter(Q(diary__icontains=query)|Q(date__icontains=query))
        if len(obj) != 0:
            messages.error(request, "Your search result")
            context = {
                "obj": obj
            }
        else:

            messages.error(request, "Sorry no result found ,if you are searching with date it should be in YYYY-MM-DD format")
    context = {
        "obj": obj
    }
    return render(request, "index.html", context)
