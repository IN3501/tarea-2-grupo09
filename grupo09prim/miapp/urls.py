from django.urls import path
from .views import * 

urlpatterns = [
	path('', index, name ='index'),
	path('ingresar/', ingresar, name='ingresar'),
	path('contacto/', contacto, name='contacto'),
	path('registro/', registro, name='registro'),
	path('solicitar/', solicitar, name='solicitar'),
	path('clientes/', clientes, name='clientes'),
	path('servicios/', servicios, name='servicios'),
	path('empresa/', empresa, name='empresa'),
	path("devreg", recuperar, name='devreg'),
	path("resol", recuperar1, name='resol'),
	path("ingreso", recuperar2, name='ingreso'),

	
]