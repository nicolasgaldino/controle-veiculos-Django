from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from veiculos.forms import CarrosForm
from veiculos.models import Carros

def home(request):

  context = {}
  context["form"] = Carros.objects.all()

  tudo = Carros.objects.all()
  paginator = Paginator(tudo, 5)
  pages = request.GET.get("page")
  context["form"] = paginator.get_page(pages)

  return render(request, "index.html", context)

def form(request):

  context = { "form": CarrosForm() }

  return render(request, "form.html", context)

def create(request):

  form = CarrosForm(request.POST or None)

  if form.is_valid():
    form.save()
    return redirect("home")

  context = { "form": form }

  return render(request, "create.html", context)

def view(request, id):

  context = { "data": Carros.objects.get(id=id) }

  return render(request, "view.html", context)

def edit(request, id):

  context = {}
  context["db"] = Carros.objects.get(id=id)
  context["form"] = CarrosForm(instance=context["db"])

  return render(request, "form.html", context)

def update(request, id):

  context = {}
  context["db"] = Carros.objects.get(id=id)
  form = CarrosForm(request.POST or None, instance=context["db"])

  if form.is_valid():
    form.save()
    return redirect("home")

def delete(request, id):

  db = Carros.objects.get(id=id)
  db.delete()
  return redirect("home")
