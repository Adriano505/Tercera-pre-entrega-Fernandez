from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Emprendedor, Comprador, Inversor
from .forms import InversorFrom, EmprendedorForm, CompradorForm, BuscarComprador, BuscarEmprendedor, BuscarInversor

# Create your views here.

def inicio(req):

    return render(req, "inicio.html", {})

def comprador(req):

    return render(req, "comprador.html", {})

def emprendedor(req):

    return render(req, "emprendedor.html", {})

def inversor(req):
    
    return render(req, "inversor.html", {})

def inversor_nuevo(req):
    if req.method == 'POST':
        form = InversorFrom(req.POST)
        if form.is_valid():
            form.save()
            return redirect('inversor_exito')
        
    else:
        form = InversorFrom()
    return render(req, 'inversor_formulario.html', {'form': form})

def inversor_exito(req):
    return render(req, 'inversor_exito.html')


def emprendedor_nuevo(req):
    if req.method == 'POST':
        form = EmprendedorForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('emprendedor_exito')
        
    else:
        form = EmprendedorForm()
    return render(req, 'emprendedor_formulario.html', {'form': form})

def emprendedor_exito(req):
    return render(req, 'emprendedor_exito.html')

def comprador_nuevo(req):
    if req.method == 'POST':
        form = CompradorForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('comprador_exito')
        
    else: 
        form = CompradorForm()

        return render(req, 'comprador_formulario.html', {'form': form})
    
def comprador_exito(req):
    return render(req, 'comprador_exito.html')


def comprador_buscar(req):
    form = BuscarComprador(req.GET or None)
    results = Comprador.objects.none()

    if form.is_valid():
        nombre = form.cleaned_data.get('nombre', '')
        apellido = form.cleaned_data.get('apellido', '')

        if nombre or apellido:
            query = Q()
            if nombre:
                query &= Q(nombre__icontains=nombre)
            if apellido:
                query &= Q(apellido__icontains=apellido)
            results = Comprador.objects.filter(query)

    return render(req, 'comprador_buscar.html', {'form': form, 'results': results})

def emprendedor_buscar(req):
    form = BuscarEmprendedor(req.GET or None)
    results = Emprendedor.objects.none()

    if form.is_valid():
        nombre = form.cleaned_data.get('nombre', '')
        emprendimiento = form.cleaned_data.get('emprendimiento', '')

        if nombre or emprendimiento:
            query = Q()
            if nombre:
                query &= Q(nombre__icontains=nombre)
            if emprendimiento:
                query &= Q(emprendimiento__icontains=emprendimiento)
            results = Emprendedor.objects.filter(query)

    return render(req, 'emprendedor_buscar.html', {'form': form, 'results': results})

def inversor_buscar(request):
    form = BuscarInversor(request.GET or None)
    results = Inversor.objects.none()

    if form.is_valid():
        nombre_empresa = form.cleaned_data.get('nombre_empresa', '')
        rubro_empresa = form.cleaned_data.get('rubro_empresa', '')

        if nombre_empresa or rubro_empresa:
            query = Q()
            if nombre_empresa:
                query &= Q(nombre_empresa__icontains=nombre_empresa)
            if rubro_empresa:
                query &= Q(rubro_empresa__icontains=rubro_empresa)
            results = Inversor.objects.filter(query)

    return render(request, 'inversor_buscar.html', {'form': form, 'results': results})