from django.db import models
from django.contrib.auth.models import User

# User model ya creado.
#=== VISTAS ESTRUCTURA (VALOR - LO Q SE MUESTRA) ====

#========= VISTA SEXO =========
MASCULINO = 'M'
FEMENINO = 'F'
SEXO = (
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
    )
#========= FIN SEXO =============

# Create your views here.
class Trabajador(models.Model):
    idTrabajador = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150,blank=True, null=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=8,blank=True, null=True)
    
    sexo = models.CharField(max_length=1, choices=SEXO, default=MASCULINO)

    activo = models.BooleanField(default= True)
    eliminado = models.BooleanField(default= False)

    usuarioRegistro = models.CharField(max_length=300)
    fechaRegistro = models.DateField()
    usuarioModificacion = models.CharField(max_length=300,blank=True, null=True)
    fechaModificacion = models.DateField(blank=True, null=True)
    usuarioEliminacion = models.CharField(max_length=300,blank=True, null=True)
    fechaEliminacion = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombres

# Create your views here.
class TipoCliente(models.Model):
    idTipoCliente = models.AutoField(primary_key=True)

    descripcion = models.CharField(max_length=50)
    
    activo = models.BooleanField(default= True)
    eliminado = models.BooleanField(default= False)

    usuarioRegistro = models.CharField(max_length=300)
    fechaRegistro = models.DateField()
    usuarioModificacion = models.CharField(max_length=300,blank=True, null=True)
    fechaModificacion = models.DateField(blank=True, null=True)
    usuarioEliminacion = models.CharField(max_length=300,blank=True, null=True)
    fechaEliminacion = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.descripcion


#========= VISTA TIPO DOCUMENTO =========
DNI = 'DNI'
RUC = 'RUC'
PASAPORTE = 'PASAPORTE'
OTRO = 'OTRO'
TIPODOCUMENTOIDENTIDAD  = (
        (DNI, 'Documento de Identidad'),        
        (RUC, 'Documento Nacional de Identidad'),
        (RUC, 'Registro Único de Contribuyentes'),
        (PASAPORTE, 'Pasaporte'),
        (OTRO, 'Otro'),
    )
#========= FIN TIPO DOCUMENTO =============

# Create your views here.
class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    tipoCliente = models.ForeignKey(TipoCliente, on_delete = models.CASCADE)

    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)
    email = models.EmailField()
    telefono = models.CharField(max_length=8)
    
    tipoDocumentoIdentidad = models.CharField(max_length=50, choices= TIPODOCUMENTOIDENTIDAD, default= DNI)
    documentoIdentidad = models.CharField(max_length=50)

    activo = models.BooleanField(default= True)
    eliminado = models.BooleanField(default= False)
    usuarioRegistro = models.CharField(max_length=300)
    fechaRegistro = models.DateField()
    usuarioModificacion = models.CharField(max_length=300,blank=True, null=True)
    fechaModificacion = models.DateField(blank=True, null=True)
    usuarioEliminacion = models.CharField(max_length=300,blank=True, null=True)
    fechaEliminacion = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombres

#========= VISTA FRECUENCIA =========
BIMENSUAL = 'BIMENSUAL'
TRIMESTRAL = 'TRIMESTRAL'
ANUAL = 'ANUAL'
FRECUENCIA = (
        (BIMENSUAL,'Bimensual'),
        (TRIMESTRAL,'Trimestral'),
        (ANUAL ,'Anual'),
    )
#========= FIN FRECUENCIA =============

class FormaPago(models.Model):
    idFormaPago = models.AutoField(primary_key=True)
    
    descripcion = models.CharField(max_length=100)
    nroCuotas = models.IntegerField()
    frecuencia = models.CharField(max_length=50,choices=FRECUENCIA, default=BIMENSUAL)
    interes = models.DecimalField(max_digits=3,decimal_places=3)

    activo = models.BooleanField(default= True)
    eliminado = models.BooleanField(default= False)
    usuarioRegistro = models.CharField(max_length=300)
    fechaRegistro = models.DateField()
    usuarioModificacion = models.CharField(max_length=300,blank=True, null=True)
    fechaModificacion = models.DateField(blank=True, null=True)
    usuarioEliminacion = models.CharField(max_length=300,blank=True, null=True)
    fechaEliminacion = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.descripcion

class Categoria(models.Model):
    idCategoria=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=100)

    activo = models.BooleanField(default= True)
    eliminado = models.BooleanField(default= False)
    usuarioRegistro = models.CharField(max_length=300)
    fechaRegistro = models.DateField()
    usuarioModificacion = models.CharField(max_length=300,blank=True, null=True)
    fechaModificacion = models.DateField(blank=True, null=True)
    usuarioEliminacion = models.CharField(max_length=300,blank=True, null=True)
    fechaEliminacion = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.descripcion

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=10)

    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    stock = models.IntegerField()

    precioUnitario = models.DecimalField(max_digits=3,decimal_places=3)

    urlImagen = models.CharField(max_length=1000)
    nombreImagen = models.CharField(max_length=1000)
    fechaCargaImagen = models.DateField()

    activo = models.BooleanField(default= True)
    eliminado = models.BooleanField(default= False)
    usuarioRegistro = models.CharField(max_length=300)
    fechaRegistro = models.DateField()
    usuarioModificacion = models.CharField(max_length=300,blank=True, null=True)
    fechaModificacion = models.DateField(blank=True, null=True)
    usuarioEliminacion = models.CharField(max_length=300,blank=True, null=True)
    fechaEliminacion = models.DateField(blank=True, null=True)

    def __str__(self):
        return self

#========= VISTA TIPOMONEDA =========
SOLES = 'SOLES'
DOLARES = 'DOLARES'
EUROS = 'EUROS'
TIPOMONEDA  = (
    (SOLES ,'Soles'),
    (DOLARES ,'Dolares'),
    (EUROS ,'Euros'),
)
#========= FIN TIPOMONEDA  =============
#========= VISTA ESTADO =========
ABIERTA = 1
CERRADA = 2
LIBERADA = 3
ANULADA = 4
ESTADO  = (
    (ABIERTA ,'Abierta'),
    (CERRADA ,'Cerrada'),
    (LIBERADA ,'Liberada'),
    (ANULADA ,'Anulada'),
)
#========= FIN ESTADO  =============

class PedidoVenta(models.Model):
    idPedidoVenta = models.AutoField(primary_key=True)

    trabajador = models.ForeignKey(Trabajador, on_delete = models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    formaPago = models.ForeignKey(FormaPago, on_delete = models.CASCADE)
    codigo = models.CharField(max_length=10)

    fechaEmision = models.DateField()
    fechaEntrega = models.DateField()

    tipoMoneda= models.CharField(max_length=50,choices=TIPOMONEDA, default=SOLES)
    tasaCambio = models.DecimalField(max_digits=3,decimal_places=3)

    subtotal = models.DecimalField(max_digits=3,decimal_places=3)

    tasaIgv = models.DecimalField(max_digits=3,decimal_places=3)
    descuento = models.DecimalField(max_digits=3,decimal_places=3)
    
    total = models.DecimalField(max_digits=3,decimal_places=3) 

    estado = models.IntegerField(choices=ESTADO, default=ABIERTA)

    eliminado = models.BooleanField(default= False)
    usuarioRegistro = models.CharField(max_length=300)
    fechaRegistro = models.DateField()
    usuarioModificacion = models.CharField(max_length=300,blank=True, null=True)
    fechaModificacion = models.DateField(blank=True, null=True)
    usuarioEliminacion = models.CharField(max_length=300,blank=True, null=True)
    fechaEliminacion = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.codigo



class DetallePedidoVenta(models.Model):
    idDetallePedidoVenta = models.AutoField(primary_key=True)
    pedidoVenta = models.ForeignKey(PedidoVenta, on_delete = models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    cantidad = models.IntegerField()
    precioUnitario = models.DecimalField(max_digits=3,decimal_places=3)
    descuentoUnitario = models.DecimalField(max_digits=3,decimal_places=3)
    precio = models.DecimalField(max_digits=3,decimal_places=3)

    eliminado = models.BooleanField(default= False)
    usuarioRegistro = models.CharField(max_length=300)
    fechaRegistro = models.DateField()
    usuarioModificacion = models.CharField(max_length=300,blank=True, null=True)
    fechaModificacion = models.DateField(blank=True, null=True)
    usuarioEliminacion = models.CharField(max_length=300,blank=True, null=True)
    fechaEliminacion = models.DateField(blank=True, null=True)

    def __str__(self):
        return self

class Proveedor(models.Model):
    idProveedor = models.AutoField(primary_key=True)

    ruc = models.CharField(max_length=11)

    razonSocial = models.CharField(max_length=50)
    nombreComercial = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)
    email = models.EmailField()
    telefono = models.CharField(max_length=8)

    activo = models.BooleanField(default= True)

    eliminado = models.BooleanField(default= False)

    usuarioRegistro = models.CharField(max_length=300)
    fechaRegistro = models.DateField()
    usuarioModificacion = models.CharField(max_length=300,blank=True, null=True)
    fechaModificacion = models.DateField(blank=True, null=True)
    usuarioEliminacion = models.CharField(max_length=300,blank=True, null=True)
    fechaEliminacion = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombreComercial


class OrdenCompra(models.Model):
    idOrdenCompra = models.AutoField(primary_key=True)
    trabajador = models.ForeignKey(Trabajador, on_delete = models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete = models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    formaPago = models.ForeignKey(FormaPago, on_delete = models.CASCADE)
    codigo = models.CharField(max_length=10)

    fechaEmision = models.DateField()
    fechaEntrega = models.DateField()

    tipoMoneda= models.CharField(max_length=50,choices=TIPOMONEDA, default=SOLES)
    tasaCambio = models.DecimalField(max_digits=3,decimal_places=3)

    subtotal = models.DecimalField(max_digits=3,decimal_places=3)

    tasaIgv = models.DecimalField(max_digits=3,decimal_places=3)
    descuento = models.DecimalField(max_digits=3,decimal_places=3)
    
    total = models.DecimalField(max_digits=3,decimal_places=3) 

    estado = models.IntegerField(choices=ESTADO, default=ABIERTA)

    eliminado = models.BooleanField(default= False)
    usuarioRegistro = models.CharField(max_length=300)
    fechaRegistro = models.DateField()
    usuarioModificacion = models.CharField(max_length=300,blank=True, null=True)
    fechaModificacion = models.DateField(blank=True, null=True)
    usuarioEliminacion = models.CharField(max_length=300,blank=True, null=True)
    fechaEliminacion = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.codigo

class DetalleOrdenCompra(models.Model):
    idDetalleOrdenCompra = models.AutoField(primary_key=True)
    ordenCompra = models.ForeignKey(OrdenCompra, on_delete = models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE)

    cantidad = models.IntegerField()
    precioUnitario = models.DecimalField(max_digits=3,decimal_places=3)
    descuentoUnitario = models.DecimalField(max_digits=3,decimal_places=3)
    precio = models.DecimalField(max_digits=3,decimal_places=3)

    eliminado = models.BooleanField(default= False)
    usuarioRegistro = models.CharField(max_length=300)
    fechaRegistro = models.DateField()
    usuarioModificacion = models.CharField(max_length=300,blank=True, null=True)
    fechaModificacion = models.DateField(blank=True, null=True)
    usuarioEliminacion = models.CharField(max_length=300,blank=True, null=True)
    fechaEliminacion = models.DateField(blank=True, null=True)

    def __str__(self):
        return self

#========= VISTA TIPO OPERACION =========
ENTRADA = 'ENTRADA'
SALIDA = 'SALIDA'
TIPOOPERACION  = (
    (ENTRADA ,'Entrada'),
    (SALIDA ,'Salida'),
)
#========= FIN TIPO OPERACION  =============


class NotaAlmacen(models.Model):
    idNotaAlmacen = models.AutoField(primary_key=True)    
    trabajador = models.ForeignKey(Trabajador, on_delete = models.CASCADE)
    pedidoVenta = models.ForeignKey(PedidoVenta, on_delete = models.CASCADE)
    ordenCompra = models.ForeignKey(OrdenCompra, on_delete = models.CASCADE)
    codigo = models.CharField(max_length=10)

    fechaEmision = models.DateField()
    fechaEntrega = models.DateField()

    tipoOperacion = models.CharField(max_length=10,choices=TIPOOPERACION, default=ENTRADA)
    serie = models.CharField(max_length=20) 
    numero = models.CharField(max_length=20)

    estado = models.IntegerField(choices=ESTADO, default=ABIERTA)

    eliminado = models.BooleanField(default= False)
    usuarioRegistro = models.CharField(max_length=300)
    fechaRegistro = models.DateField()
    usuarioModificacion = models.CharField(max_length=300,blank=True, null=True)
    fechaModificacion = models.DateField(blank=True, null=True)
    usuarioEliminacion = models.CharField(max_length=300,blank=True, null=True)
    fechaEliminacion = models.DateField(blank=True, null=True)

    def __str__(self):
        return self

class DetalleNotaAlmacen(models.Model):
    idDetalleNotaAlmacen = models.AutoField(primary_key=True)    
    notaAlmacen = models.ForeignKey(NotaAlmacen, on_delete = models.CASCADE)

    producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    cantidad = models.IntegerField()
    precioUnitario = models.DecimalField(max_digits=3,decimal_places=3)
    descuentoUnitario = models.DecimalField(max_digits=3,decimal_places=3)
    precio = models.DecimalField(max_digits=3,decimal_places=3)

    cantidadTotal = models.IntegerField()
    cantidadUsada = models.IntegerField()
    cantidadSaldo = models.IntegerField()

    eliminado = models.BooleanField(default= False)
    usuarioRegistro = models.CharField(max_length=300)
    fechaRegistro = models.DateField()
    usuarioModificacion = models.CharField(max_length=300,blank=True, null=True)
    fechaModificacion = models.DateField(blank=True, null=True)
    usuarioEliminacion = models.CharField(max_length=300,blank=True, null=True)
    fechaEliminacion = models.DateField(blank=True, null=True)

    def __str__(self):
        return self


#========= VISTA TIPODOCUMENTO =========
BOLETA = 'BOLETA'
FACTURA = 'FACTURA'
TIPODOCUMENTO  = (
    (BOLETA ,'Boleta'),
    (FACTURA ,'Factura'),
)
#========= FIN TIPODOCUMENTO  =============

class DocumentoVenta(models.Model):
    idDocumentoVenta = models.AutoField(primary_key=True)    
    trabajador = models.ForeignKey(Trabajador, on_delete = models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    pedidoVenta = models.ForeignKey(PedidoVenta, on_delete = models.CASCADE)
    codigo = models.CharField(max_length=10)

    fechaEmision = models.DateField()
    fechaEntrega = models.DateField()

    serie = models.CharField(max_length=20) 
    numero = models.CharField(max_length=20)

    tipoDocumento = models.CharField(max_length=20,choices=TIPODOCUMENTO, default=BOLETA)

    eliminado = models.BooleanField(default= False)
    usuarioRegistro = models.CharField(max_length=300)
    fechaRegistro = models.DateField()
    usuarioModificacion = models.CharField(max_length=300,blank=True, null=True)
    fechaModificacion = models.DateField(blank=True, null=True)
    usuarioEliminacion = models.CharField(max_length=300,blank=True, null=True)
    fechaEliminacion = models.DateField(blank=True, null=True)

    def __str__(self):
        return self

class DetalleDocumentoVenta(models.Model):
    idDetalleDocumentoVenta = models.AutoField(primary_key=True)    
    documentoVenta = models.ForeignKey(DocumentoVenta, on_delete = models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE)

    cantidad = models.IntegerField()
    precioUnitario = models.DecimalField(max_digits=3,decimal_places=3)
    descuentoUnitario = models.DecimalField(max_digits=3,decimal_places=3)
    precio = models.DecimalField(max_digits=3,decimal_places=3)

    eliminado = models.BooleanField(default= False)
    usuarioRegistro = models.CharField(max_length=300)
    fechaRegistro = models.DateField()
    usuarioModificacion = models.CharField(max_length=300,blank=True, null=True)
    fechaModificacion = models.DateField(blank=True, null=True)
    usuarioEliminacion = models.CharField(max_length=300,blank=True, null=True)
    fechaEliminacion = models.DateField(blank=True, null=True)

    def __str__(self):
        return self


class DocumentoCompra(models.Model):
    idDocumentoCompra = models.AutoField(primary_key=True)    
    trabajador = models.ForeignKey(Trabajador, on_delete = models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete = models.CASCADE)
    ordenCompra = models.ForeignKey(OrdenCompra, on_delete = models.CASCADE)

    fechaEmision = models.DateField()
    fechaEntrega = models.DateField()

    serie = models.CharField(max_length=20) 
    numero = models.CharField(max_length=20)
    
    tipoDocumento = models.CharField(max_length=20,choices=TIPODOCUMENTO, default=FACTURA)

    eliminado = models.BooleanField(default= False)
    usuarioRegistro = models.CharField(max_length=300)
    fechaRegistro = models.DateField()
    usuarioModificacion = models.CharField(max_length=300,blank=True, null=True)
    fechaModificacion = models.DateField(blank=True, null=True)
    usuarioEliminacion = models.CharField(max_length=300,blank=True, null=True)
    fechaEliminacion = models.DateField(blank=True, null=True)

    def __str__(self):
        return self

class DetalleDocumentoCompra(models.Model):
    idDetalleDocumentoCompra = models.AutoField(primary_key=True)    
    documentoCompra = models.ForeignKey(DocumentoCompra, on_delete = models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE)

    cantidad = models.IntegerField()
    precioUnitario = models.DecimalField(max_digits=3,decimal_places=3)
    descuentoUnitario = models.DecimalField(max_digits=3,decimal_places=3)
    precio = models.DecimalField(max_digits=3,decimal_places=3)

    eliminado = models.BooleanField(default= False)
    usuarioRegistro = models.CharField(max_length=300)
    fechaRegistro = models.DateField()
    usuarioModificacion = models.CharField(max_length=300,blank=True, null=True)
    fechaModificacion = models.DateField(blank=True, null=True)
    usuarioEliminacion = models.CharField(max_length=300,blank=True, null=True)
    fechaEliminacion = models.DateField(blank=True, null=True)

    def __str__(self):
        return self
