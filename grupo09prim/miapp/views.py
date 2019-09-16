from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'home.html')

def ingresar(request):
	return render(request, 'ingresar.html')

def contacto(request):
	return render(request, 'contacto.html')

def registro(request):
	return render(request, 'registro.html')

def solicitar(request):
	return render(request, 'solicitar.html')

def clientes(request):
	return render(request, 'clientes.html')

def servicios(request):
	return render(request, 'servicios.html')

def empresa(request):
	return render(request, 'empresa.html')

def recuperar(request):
	nombre=request.POST["nombre"]
	usuario=request.POST["usuario"]
	correo=request.POST["correo"]
	diccionario={}
	diccionario["comentario"]=nombre
	diccionario["comentario2"]=usuario
	diccionario["comentario3"]=correo
	return render(request, "devreg.html", diccionario)

def recuperar1(request):
	tipo=request.POST["tipo"]
	com=request.POST["com"]
	direc=request.POST["direc"]
	fecha=request.POST["fecha"]
	fono=request.POST["fono"]
	mail=request.POST["mail"]
	des=request.POST["des"]
	sol={}
	sol["tipo"]=tipo
	sol["com"]=com
	sol["mail"]=mail
	sol["direc"]=direc
	sol["fecha"]=fecha
	sol["fono"]=fono
	sol["des"]=des
	return render(request, "resol.html", sol)

def recuperar2(request):
	user=request.POST["user"]
	ing={}
	ing["user"]=user
	return render(request, "ingreso.html", ing)