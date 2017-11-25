from django import forms
from producto.models import Producto


class ProductoForm(forms.ModelForm):

	class Meta:   #para indicar de que modelo se va a crear el formulario
		model = Producto

		fields = [
           'id_producto',
           'nombre_producto',
           'precio_producto',
                      
		]
		labels = {
	        'id_producto' : 'Codigo',
	        'nombre_producto': 'Nombre',
	        'precio_producto' : 'Precio',
	        
	        
		}
		widgets = {
		'id_producto': forms.TextInput(attrs={'class':'form-control'}),
        'nombre_producto': forms.TextInput(attrs={'class':'form-control'}),
        'precio_producto': forms.TextInput(attrs={'class':'form-control'}),
        
		}