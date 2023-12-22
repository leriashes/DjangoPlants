from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Rastenie
from .forms import RastenieForm


# Create your views here.

def rastenie_index(request):
    rastenies = Rastenie.objects.filter(opublikovano=True).order_by('data_izmen')[:6]
    return render(request, 'plants/index.html', {'rastenies' : rastenies})

def rastenie_all(request):
    rastenies = Rastenie.objects.filter(opublikovano=True).order_by('nazvanie')
    return render(request, 'plants/all.html', {'rastenies' : rastenies})

def rastenie_show(request, pk):
    rastenie = get_object_or_404(Rastenie, pk=pk)
    return render(request, 'plants/show.html', {'rastenie' : rastenie})

def rastenie_adm_all(request):
    rastenies = Rastenie.objects.all().order_by('-data_izmen')
    return render(request, 'plants/adm_all.html', {'rastenies' : rastenies})

def rastenie_new(request):
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

def rastenie_edit(request, pk):
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

def rastenie_delete(request, pk):
    rastenie = get_object_or_404(Rastenie, pk=pk)
    rastenie.delete()
    return redirect('adm_all')
   