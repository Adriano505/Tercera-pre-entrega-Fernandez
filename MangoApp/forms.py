from django import forms
from .models import Inversor, Emprendedor, Comprador

class InversorFrom(forms.ModelForm):
    class Meta:
        model = Inversor
        fields = ['nombre_empresa', 'rubro_empresa', 'capital_inicial']

class EmprendedorForm(forms.ModelForm):
    class Meta:
        model = Emprendedor
        fields = ['nombre', 'emprendimiento', 'dinero_requerido']


class CompradorForm(forms.ModelForm):
    class Meta:
        model = Comprador
        fields = ['nombre', 'apellido', 'email']

class BuscarComprador(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100, required=False)
    apellido = forms.CharField(label='Apellido', max_length=100, required=False)

class BuscarEmprendedor(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100, required=False)
    emprendimiento = forms.CharField(label='Emprendimiento', max_length=100, required=False)

class BuscarInversor(forms.Form):
    nombre_empresa = forms.CharField(label='Nombre de la Empresa', max_length=100, required=False)
    rubro_empresa = forms.CharField(label='Rubro de la Empresa', max_length=100, required=False)
