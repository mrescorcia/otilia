# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categorias(models.Model):
    idcategorias = models.AutoField(primary_key=True)
    nombrecategoria = models.CharField(db_column='nombreCategoria', max_length=45)  # Field name made lowercase.
    desccategoria = models.CharField(db_column='descCategoria', max_length=45, blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return str(self.idcategorias) + '-' + self.nombrecategoria

    class Meta:
        managed = False
        db_table = 'categorias'
        verbose_name_plural = 'categorias'


class Clientes(models.Model):
    idclientes = models.AutoField(primary_key=True)
    documentocliente = models.CharField(db_column='documentoCliente', max_length=45)  # Field name made lowercase.
    tipodoccliente = models.CharField(db_column='tipoDocCliente', max_length=45, blank=True, null=True)  # Field name made lowercase.
    nombrescliente = models.CharField(db_column='nombresCliente', max_length=45, blank=True, null=True)  # Field name made lowercase.
    apellidoscliente = models.CharField(db_column='apellidosCliente', max_length=45, blank=True, null=True)  # Field name made lowercase.
    direccioncliente = models.CharField(db_column='direccionCliente', max_length=45, blank=True, null=True)  # Field name made lowercase.
    telefonocliente = models.CharField(db_column='telefonoCliente', max_length=45, blank=True, null=True)  # Field name made lowercase.
    correocliente = models.CharField(db_column='correoCliente', max_length=45, blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.documentocliente + '-' + self.nombrescliente + ' ' + self.apellidoscliente

    class Meta:
        managed = False
        db_table = 'clientes'
        verbose_name_plural = 'clientes'


class Compras(models.Model):
    idcompras = models.AutoField(primary_key=True)
    numerocompra = models.IntegerField(db_column='numeroCompra')  # Field name made lowercase.
    proveedores_idproveedores = models.ForeignKey('Proveedores', models.DO_NOTHING, db_column='proveedores_idproveedores')
    fechacompra = models.DateField(db_column='fechaCompra', blank=True, null=True)  # Field name made lowercase.
    totalcompra = models.FloatField(db_column='totalCompra', blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compras'
        verbose_name_plural = 'compras'


class Detallecompras(models.Model):
    iddetallecompras = models.AutoField(db_column='iddetalleCompras', primary_key=True)  # Field name made lowercase.
    compras_idcompras = models.ForeignKey(Compras, models.DO_NOTHING, db_column='compras_idcompras')
    productos_idproductos = models.ForeignKey('Productos', models.DO_NOTHING, db_column='productos_idproductos')
    cantidadproductos = models.FloatField(db_column='cantidadProductos')  # Field name made lowercase.
    ivaproducto = models.FloatField(db_column='ivaProducto', blank=True, null=True)  # Field name made lowercase.
    subtotalcompra = models.FloatField(db_column='subtotalCompra', blank=True, null=True)  # Field name made lowercase.
    observacionescompra = models.CharField(db_column='observacionesCompra', max_length=45, blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detallecompras'
        verbose_name_plural = 'detallecompras'


class Detalleventas(models.Model):
    iddetalleventas = models.AutoField(db_column='idDetalleVentas', primary_key=True)  # Field name made lowercase.
    ventas_idventas = models.ForeignKey('Ventas', models.DO_NOTHING, db_column='ventas_idventas')
    productos_idproductos = models.ForeignKey('Productos', models.DO_NOTHING, db_column='productos_idproductos')
    plataforma_venta_idplataforma_venta = models.ForeignKey('PlataformaVenta', models.DO_NOTHING, db_column='plataforma_venta_idplataforma_venta')
    precioproducto = models.FloatField(db_column='precioProducto')  # Field name made lowercase.
    cantproducto = models.FloatField(db_column='cantProducto')  # Field name made lowercase.
    subtotalventa = models.FloatField(db_column='subtotalVenta', blank=True, null=True)  # Field name made lowercase.
    dctoproducto = models.FloatField(db_column='dctoProducto', blank=True, null=True)  # Field name made lowercase.
    otrosimpuestos = models.FloatField(db_column='otrosImpuestos', blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalleventas'
        verbose_name_plural = 'detalleventas'


class EstadoProducto(models.Model):
    idestado_producto = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return str(self.idestado_producto) + '-' + self.estado

    class Meta:
        managed = False
        db_table = 'estado_producto'
        verbose_name_plural = 'estado_producto'


class PlataformaVenta(models.Model):
    idplataforma_venta = models.AutoField(primary_key=True)
    nom_plataforma = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plataforma_venta'
        verbose_name_plural = 'plataforma_venta'


class Productos(models.Model):
    idproductos = models.AutoField(primary_key=True)
    categorias_idcategorias = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='categorias_idcategorias')
    estado_producto_idestado_producto = models.ForeignKey(EstadoProducto, models.DO_NOTHING, db_column='estado_producto_idestado_producto')
    nombreproducto = models.TextField(db_column='nombreProducto', max_length=70)  # Field name made lowercase.
    imagenproducto = models.TextField(db_column='imagenProducto', max_length=200)  # Field name made lowercase.
    codigoproducto = models.CharField(db_column='codigoProducto', max_length=45, blank=True, null=True)  # Field name made lowercase.
    sku = models.CharField(max_length=45, blank=True, null=True)
    costoproducto = models.FloatField(db_column='costoProducto', blank=True, null=True)  # Field name made lowercase.
    precioproducto = models.FloatField(db_column='precioProducto', blank=True, null=True)  # Field name made lowercase.
    marcaproducto = models.CharField(db_column='marcaProducto', max_length=45, blank=True, null=True)  # Field name made lowercase.
    modeloproducto = models.CharField(db_column='modeloProducto', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cantidadproducto = models.FloatField(db_column='cantidadProducto', blank=True, null=True)  # Field name made lowercase.
    ivaproducto = models.FloatField(db_column='ivaProducto', blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    detalles = models.TextField(db_column='detalles', max_length=2000)  # Field name made lowercase.
    def __str__(self):
        return str(self.idproductos) + '-' + self.nombreproducto

    class Meta:
        managed = False
        db_table = 'productos'
        verbose_name_plural = 'productos'


class Proveedores(models.Model):
    idproveedores = models.AutoField(primary_key=True)
    docproveedor = models.CharField(db_column='docProveedor', max_length=45)  # Field name made lowercase.
    nombresproveedor = models.CharField(db_column='nombresProveedor', max_length=45, blank=True, null=True)  # Field name made lowercase.
    apellidosproveedor = models.CharField(db_column='apellidosProveedor', max_length=45, blank=True, null=True)  # Field name made lowercase.
    direccionproveedor = models.CharField(db_column='direccionProveedor', max_length=45, blank=True, null=True)  # Field name made lowercase.
    telefonoproveedor = models.CharField(db_column='telefonoProveedor', max_length=45, blank=True, null=True)  # Field name made lowercase.
    celularproveedor = models.CharField(db_column='celularProveedor', max_length=45, blank=True, null=True)  # Field name made lowercase.
    correoproveedor = models.CharField(db_column='correoProveedor', max_length=45, blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedores'
        verbose_name_plural = 'proveedores'


class Ventas(models.Model):
    idventas = models.AutoField(primary_key=True)
    numeroventa = models.IntegerField(db_column='numeroVenta')  # Field name made lowercase.
    clientes_idclientes = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='clientes_idclientes')
    fechaventa = models.DateField(db_column='fechaVenta', blank=True, null=True)  # Field name made lowercase.
    dctoventa = models.FloatField(db_column='dctoVenta', blank=True, null=True)  # Field name made lowercase.
    ivaventa = models.FloatField(db_column='ivaVenta', blank=True, null=True)  # Field name made lowercase.
    totalventa = models.FloatField(db_column='totalVenta', blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ventas'
        verbose_name_plural = 'ventas'
