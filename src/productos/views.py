from django.shortcuts import render
from django.http import HttpResponse

#Generic views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

#Forms 
from productos.forms import CargaProducto, FormularioBusqueda

#Decorators
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin




#Models
from productos.models import ProductosDetailing
from clientes.models import Avatar


#Vista de inicio
def index (request):
    
    listado_productos=ProductosDetailing.objects.all()
    context = {
        'productos': listado_productos
    }
    
    if not request.user.is_anonymous:
        avatar = Avatar.objects.filter(usuario = request.user ).last()
        context.update({"avatar": avatar})
    
    return render (request, 'productos/index.html', context)

#Vista de carga de producto
@login_required
def cargar_producto(request):
    #El primer paso para crear el formulario de carga
    if request.method == "GET":
        formulario = CargaProducto()
        return render(request, "productos/carga_productos.html", {"formulario": formulario})

    #se envia el formulario a través de POST
    else:

        formulario = CargaProducto(request.POST)

        if formulario.is_valid():
            
            data = formulario.cleaned_data
                  
            nombre = data.get("nombre")
            marca = data.get("marca")
            precio = data.get('precio')
            tipo = data.get('tipo')
            stock = data.get('stock')
            producto = ProductosDetailing(nombre = nombre, marca = marca, precio = precio, tipo = tipo, stock = stock)

            producto.save()

            return render(request, "productos/index.html")

        else:
            return HttpResponse("Formulario no valido")
        

#Formulario de busqueda, se utilizan los templates formulario_busqueda y resultado_busqueda
def formulario_busqueda(request):
    return render(request, "productos/formulario_busqueda.html")

def buscar(request):

    producto_nombre = request.GET.get("producto", None)
    

    if not producto_nombre:
        return HttpResponse("No indicaste ningun nombre")

    producto_lista = ProductosDetailing.objects.filter(nombre__icontains=producto_nombre)

        
    return render(request, "productos/resultado_busqueda.html", {"productos": producto_lista})



class ProductosList (ListView):
    model = ProductosDetailing
    template_name = 'productos/productos_lista.html'
    
    def get_context_data(self, **kwargs):
        context = super(ProductosList,self).get_context_data(**kwargs)
        context ['productos'] = ProductosDetailing.objects.all()
        return context
    
class ProductosDetalle (DetailView):
    model = ProductosDetailing
    template_name = 'productos/productos_detalle.html'
    

class ProductosCrear (LoginRequiredMixin, CreateView):
    model = ProductosDetailing
    success_url = '/productos/'
    fields = ['nombre','marca','precio','tipo','stock']
    template_name = 'productos/productos_crear.html'
    
    
class ProductosModificar (LoginRequiredMixin, UpdateView):
    model = ProductosDetailing
    success_url = '/'
    fields = ['nombre','marca','precio','tipo','stock']
    template_name = 'productos/productos_crear.html'
    
    
class ProductosDelete (LoginRequiredMixin, DeleteView):
    model = ProductosDetailing
    success_url = '/productos/'
    template_name = 'productos/confirmacion_borrado.html'