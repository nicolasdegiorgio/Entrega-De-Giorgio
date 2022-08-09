# All Cars Detailing - Project by Nicolás De Giorgio
Proyecto ACD (All Cars Detailing) para el proyecto final del curso de Python

Bienvenido a mi primer entrega del proyecto final!

Te cuento un poco de que se trata:
Este en una preentrega de mi segunda aplicación creada con python y django, las cuales estoy aprendiendo actualmente.
Para este proyecto, plantee un ecommerce donde se pueden encontrar productos de detailing de vehiculos y distintos servicios que brindara la "empresa cliente".

La app web, cuenta a su vez con 3 "django-apps" las cuales administran los 3 punteros del servicio:

Usuarios o clientes
Productos que se pueden comprar
Servicios (turnos) que se brindan

En la página de inicio, se entrará de lleno al listado de productos, lo cual considero como vista proncipal de la app (directamente al abrir la web desde la terminal).

En la parte superior se podrán ver los tres punteros para navegar a través de la página.
El boton Productos vuelve siempre a la url principal, la cual es un template con herencia desde base.html (por ahora todas lo son, falta embellecer el sitio), y lo que verdaderamente se carga es index.html

Siguiendo con los productos, se puede realizar la carga de nuevos productos desde el menu desplegable de la barra superior, o desde http://127.0.0.1:8000/cargarproducto/

En el boton de Buscar o en http://127.0.0.1:8000/busqueda/ , se puede acceder a la busqueda simple de productos, el cual renderiza en primer lugar formulario_busqueda.html y luego renderiza resultado_busqueda.html

Por el lado de los usuarios o clientes, se puede acceder desde el menu desplegable o desde http://127.0.0.1:8000/clientes/clientes/. En la parte inferior se puede acceder al formulario de carga de los mismos, o bien desde http://127.0.0.1:8000/clientes/crear/

Por ultimo, los servicios van a funcionar de la misma manera que los clientes, pero con sus correspondientes apartados. Por ahora solo es una lista de los turnos creados.
