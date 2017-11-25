from django import forms
from distribuidor.models import Distribuidor

class DistriForm(forms.ModelForm):

	class Meta:   #para indicar de que modelo se va a crear el formulario
		model = Distribuidor

		fields = [
           'nit_distribuidor',
           'nombre_distribuidor',
           'direccion',
           'telefono',
           'email',
           
		]
		labels = {
	        'nit_distribuidor' : 'Nit',
            'nombre_distribuidor' : 'Nombre',
            'direccion' : 'Direccion',
            'telefono' : 'Telefono',
            'email' : 'Email'
	        
		}
		widgets = {
		'nit_distribuidor': forms.TextInput(attrs={'class':'form-control'}),
		'nombre_distribuidor': forms.TextInput(attrs={'class':'form-control'}),
        'direccion': forms.TextInput(attrs={'class':'form-control'}),
        'telefono': forms.TextInput(attrs={'class':'form-control'}),
        'email': forms.TextInput(attrs={'class':'form-control'}),
        
        #'nombre_distribuidor': forms.Select(attrs={'class':'form-control'}),

		}