from django import forms 
from.models import Venta


class VentaForm(forms.ModelForm):

	class Meta:   #para indicar de que modelo se va a crear el formulario
		model = Venta

		fields = [
           'codigo_venta',
           'id_producto',
           'fecha_venta',
           'cantidad',
           'valor_venta',
           
		]
		labels = {
	        'codig_venta' : 'Codigo',
	        'id_producto': 'Producto',
	        'fecha_venta' : 'Fecha venta',
	        'cantidad' : 'Cantidad',
	        'valor_venta' : 'Valor',
	        
		}
		widgets = {
		'codigo_venta': forms.TextInput(attrs={'class':'form-control'}),
        'id_producto': forms.Select(attrs={'class':'form-control'}),
        'fecha_venta': forms.TextInput(attrs={'class':'form-control'}),
        'cantidad': forms.TextInput(attrs={'class':'form-control'}),
        'valor_venta': forms.TextInput(attrs={'class':'form-control'}),

		}