from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .models import Rastenie
from .forms import RastenieForm
from .forms import LoginForm
from .forms import RegistrationForm


# Create your views here.

def Login(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('adm_all')
    else:
        messages.info(request, "Для перехода на данную страницу выполните вход.")
    return redirect('index')

def LoginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user != None:
            login(request, user)
        else:
            messages.error(request, "Неверный логин или пароль!")
        return redirect('index')

def LogoutUser(request):
    logout(request)
    request.user = None
    return redirect('index')

def Register(request):
    RegisterUser(request)
    return redirect('index')

def RegisterUser(request):
    if request.method == "POST":
        regForm = RegistrationForm(request.POST)
        if regForm.is_valid():
            user = regForm.save(commit=False)
            user.set_password(regForm.cleaned_data['password'])
            user.is_active = False
            user.save()
            return redirect('index')
    else:
        regForm = RegistrationForm()
    return regForm

def rastenie_index(request):
    form = RegisterUser(request)
    rastenies = Rastenie.objects.filter(opublikovano=True).order_by('data_izmen')[:6]
    return render(request, 'plants/index.html', {'rastenies' : rastenies, "form" : form})

def rastenie_all(request):
    rastenies = Rastenie.objects.filter(opublikovano=True).order_by('nazvanie')
    return render(request, 'plants/all.html', {'rastenies' : rastenies})

@login_required(login_url="/login")
def rastenie_fav(request):
    rastenies = Rastenie.objects.filter(opublikovano=True).order_by('nazvanie')
    return render(request, 'plants/fav.html', {'rastenies' : rastenies})

def rastenie_show(request, pk):
    rastenie = get_object_or_404(Rastenie, pk=pk)
    return render(request, 'plants/show.html', {'rastenie' : rastenie})

@login_required(login_url="/login")
def rastenie_adm_all(request):
    if not request.user.is_superuser:
        messages.info(request, "Для перехода на данную страницу требуются права администратора.")
        return redirect('index')

    rastenies = Rastenie.objects.all().order_by('-data_izmen')
    return render(request, 'plants/adm_all.html', {'rastenies' : rastenies})

@login_required(login_url="/login")
def rastenie_new(request):
    if not request.user.is_superuser:
        messages.info(request, "Для перехода на данную страницу требуются права администратора.")
        return redirect('index')

    if request.method == "POST":
        form = RastenieForm(request.POST, request.FILES)
        if form.is_valid():
            rastenie = form.save(commit=False)
            rastenie.data_izmen = timezone.now()
            if request.FILES:
                with open(f"plants/uploads/{request.FILES['izobrazhenie'].name}", "wb+") as destination:
                    for chunk in request.FILES['izobrazhenie'].chunks():
                        destination.write(chunk)
            rastenie.save()
            form.save_m2m()
            return redirect('adm_all')
    else:
        form = RastenieForm()
    return render(request, 'plants/edit.html', {'form' : form})

@login_required(login_url="/login")
def rastenie_edit(request, pk):
    if not request.user.is_superuser:
        messages.info(request, "Для перехода на данную страницу требуются права администратора.")
        return redirect('index')

    rastenie = get_object_or_404(Rastenie, pk=pk)
    izobr = rastenie.izobrazhenie
    if request.method == "POST":
        form = RastenieForm(request.POST, request.FILES, instance=rastenie)
        if form.is_valid():
            rastenie = form.save(commit=False)
            rastenie.data_izmen = timezone.now()
            if request.FILES:
                with open(f"plants/uploads/{request.FILES['izobrazhenie'].name}", "wb+") as destination:
                    for chunk in request.FILES['izobrazhenie'].chunks():
                        destination.write(chunk)
            else:
                rastenie.izobrazhenie = izobr
            rastenie.save()
            form.save_m2m()
            return redirect('adm_all')
    else:
        form = RastenieForm(instance=rastenie)
    return render(request, 'plants/edit.html', {'form' : form})

@login_required(login_url="/login")
def rastenie_delete(request, pk):
    if not request.user.is_superuser:
        messages.info(request, "Для перехода на данную страницу требуются права администратора.")
        return redirect('index')

    rastenie = get_object_or_404(Rastenie, pk=pk)
    rastenie.delete()
    return redirect('adm_all')
   