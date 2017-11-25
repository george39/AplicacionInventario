from django import forms
from compra.models import Compra

class CompraForm(forms.ModelForm):

	class Meta:   #para indicar de que modelo se va a crear el formulario
		model = Compra

		fields = [
           'codigo_compra',
           'id_producto',
           'nit_proveedor',
           'cantidad',
           'valor_compra',
		]
		labels = {
	        'codigo_compra' : 'Codigo compra',
            'id_producto' : 'Producto',
            'nit_proveedor' : 'Proveedor',
            'cantidad' : 'Cantidad',
            'valor_compra' : 'Valor',

	        
		}
		widgets = {
		'codigo_compra': forms.TextInput(attrs={'class':'form-control'}),
		'id_producto': forms.Select(attrs={'class':'form-control'}),
		'nit_proveedor': forms.Select(attrs={'class':'form-control'}),
		'cantidad': forms.TextInput(attrs={'class':'form-control'}),
        'valor_compra': forms.TextInput(attrs={'class':'form-control'}),
        
        
        #'nombre_distribuidor': forms.Select(attrs={'class':'form-control'}),

		}