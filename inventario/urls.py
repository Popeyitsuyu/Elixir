from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    path('', views.home, name='index'),             # raíz -> home
    path('home/', views.home, name='home'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('checkout/', views.checkout, name='checkout'),
]
