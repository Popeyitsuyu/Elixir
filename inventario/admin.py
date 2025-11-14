from django.contrib import admin
from django.utils.html import format_html
from .models import Categoria, Proveedor, Producto, ProductoImagen

# Desregistrar Producto si ya está registrado
try:
    admin.site.unregister(Producto)
except admin.sites.NotRegistered:
    pass

class ProductoImagenInline(admin.TabularInline):
    model = ProductoImagen
    extra = 1

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    inlines = [ProductoImagenInline]
    list_display = [
        'nombre', 'sku', 'categoria',
        'precio_formateado', 'stock_display',
        'margen_display', 'activo'
    ]
    list_filter = ['categoria', 'proveedor', 'activo']
    search_fields = ['nombre', 'sku']
    ordering = ['nombre']

    def precio_formateado(self, obj):
        # Convertir a float antes de formatear
        valor = float(obj.precio or 0)
        return f"${valor:,.0f}"
    precio_formateado.short_description = "Precio"

    def stock_display(self, obj):
        if obj.stock_bajo:
            return format_html(
                '<span style="color: red; font-weight: bold;">{} ⚠️</span>',
                obj.stock
            )
        return obj.stock
    stock_display.short_description = "Stock"

    def margen_display(self, obj):
        # Convertir a float y luego formatear el texto
        margen = float(obj.margen_ganancia or 0)
        texto = f"{margen:.1f}%"
        color = "green" if margen > 20 else "orange" if margen > 10 else "red"
        return format_html(
            '<span style="color: {};">{}</span>',
            color, texto
        )
    margen_display.short_description = "Margen"


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'activa', 'fecha_creacion']
    list_filter = ['activa']
    search_fields = ['nombre']
    ordering = ['nombre']


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'rut', 'email', 'telefono', 'activo']
    list_filter = ['activo']
    search_fields = ['nombre', 'rut']
    ordering = ['nombre']
