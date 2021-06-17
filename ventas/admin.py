from django.contrib import admin

# Register your models here.

from ventas.models import Categorias, Clientes, Compras, Detallecompras, Detalleventas, EstadoProducto, PlataformaVenta, Productos, Proveedores, Ventas


class CategoriasAdmin(admin.ModelAdmin):
    list_display_links = ('nombrecategoria',)
    list_display = ('idcategorias','nombrecategoria',)
    list_filter = ('nombrecategoria',)
    search_fields = ('nombrecategoria',)
    
admin.site.register(Categorias, CategoriasAdmin)


class ClientesAdmin(admin.ModelAdmin):
    list_display_links = ('documentocliente',)
    list_display = ('documentocliente',)
    list_filter = ('documentocliente',)
    search_fields = ('documentocliente',)
    
admin.site.register(Clientes, ClientesAdmin)


class ComprasAdmin(admin.ModelAdmin):
    list_display_links = ('numerocompra',)
    list_display = ('numerocompra',)
    list_filter = ('numerocompra',)
    search_fields = ('numerocompra',)
    
admin.site.register(Compras, ComprasAdmin)

class DetallecomprasAdmin(admin.ModelAdmin):
    list_display_links = ('cantidadproductos',)
    list_display = ('cantidadproductos',)
    list_filter = ('cantidadproductos',)
    search_fields = ('cantidadproductos',)
    
admin.site.register(Detallecompras, DetallecomprasAdmin)

class DetalleventasAdmin(admin.ModelAdmin):
    list_display_links = ('precioproducto',)
    list_display = ('precioproducto',)
    list_filter = ('precioproducto',)
    search_fields = ('precioproducto',)
    
admin.site.register(Detalleventas, DetalleventasAdmin)

class EstadoProductoAdmin(admin.ModelAdmin):
    list_display_links = ('estado',)
    list_display = ('estado',)
    list_filter = ('estado',)
    search_fields = ('estado',)
    
admin.site.register(EstadoProducto, EstadoProductoAdmin)

class PlataformaVentaAdmin(admin.ModelAdmin):
    list_display_links = ('nom_plataforma',)
    list_display = ('nom_plataforma',)
    list_filter = ('nom_plataforma',)
    search_fields = ('nom_plataforma',)
    
admin.site.register(PlataformaVenta, PlataformaVentaAdmin)

class ProductosAdmin(admin.ModelAdmin):
    list_display_links = ('nombreproducto',)
    list_display = ('nombreproducto','estado_producto_idestado_producto',)
    list_filter = ('nombreproducto','estado_producto_idestado_producto',)
    search_fields = ('nombreproducto',)
    
admin.site.register(Productos, ProductosAdmin)

class ProveedoresAdmin(admin.ModelAdmin):
    list_display_links = ('docproveedor',)
    list_display = ('docproveedor',)
    list_filter = ('docproveedor',)
    search_fields = ('docproveedor',)
    
admin.site.register(Proveedores, ProveedoresAdmin)

class VentasAdmin(admin.ModelAdmin):
    list_display_links = ('numeroventa',)
    list_display = ('numeroventa',)
    list_filter = ('numeroventa',)
    search_fields = ('numeroventa',)
    
admin.site.register(Ventas, VentasAdmin)