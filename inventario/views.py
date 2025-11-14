from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Producto, Categoria



def home(request):
    # Mostrar solo las categorías deseadas, activas y en mayúscula la primera letra
    categorias = Categoria.objects.filter(
        nombre__in=["Pisco", "Ron", "Cerveza", "Vino"],
        activa=True
    )
    productos_destacados = Producto.objects.filter(activo=True)[:8]
    productos_prueba = Producto.objects.filter(nombre__icontains="Prueba", activo=True)

    context = {
        'categorias': categorias,
        'productos_destacados': productos_destacados,
        'productos_prueba': productos_prueba,
    }
    return render(request, 'home.html', context)



def catalogo(request):
    productos = Producto.objects.filter(activo=True)
    categorias = Categoria.objects.filter(activa=True)
    categoria_id = request.GET.get('categoria')
    busqueda = request.GET.get('q')

    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    if busqueda:
        productos = productos.filter(
            Q(nombre__icontains=busqueda) |
            Q(descripcion__icontains=busqueda)
        )
    context = {
        'productos': productos,
        'categorias': categorias,
        'filtros_activos': {
            'categoria': categoria_id,
            'busqueda': busqueda,
        }
    }
    return render(request, 'catalogo.html', context)


def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id, activo=True)
    productos_relacionados = Producto.objects.filter(
        categoria=producto.categoria,
        activo=True
    ).exclude(id=producto_id)[:4]

    context = {
        'producto': producto,
        'productos_relacionados': productos_relacionados,
    }
    return render(request, 'detalle_producto.html', context)


def checkout(request):
    return render(request, 'checkout.html')
