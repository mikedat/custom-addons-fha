## Incidencias en Compras 

### Resumen
Este módulo añade funcionalidades para informar de incidencias en compras

### Instalación
Antes de instalar el módulo debemos tener instalados los siguientes modulos:
  - purchase
  - contacts
  - base_tier_validation

Una vez instalados, solamente tendremos que ir a la sección de aplicaciones, seleccionar el módulo e instalarlo.

### Configuración
En el caso que queramos que el usuario esté dentro del nuevo grupo "Administradores de compras" tendremos que hacer lo siguiente:
  1. Activar el modo desarrollador (Control + K > tecleamos "debug" y seleccionamos.)
  2. Ir a Ajustes > Usuarios y Compañías > Usuarios.
  3. Clicamos sobre el usuario que queremos que esté dentro del nuevo grupo.
  4. Bajamos hasta que veamos la sección de "Purchase".
  5. Una vez estemos en la sección de "Purchase", dejamos seleccionada la opción "Administradores de compras".

#### ¿Qué tiene de especial estar asignar el grupo administrador de compras a un usuario?
  - Añadirá campos extra para el formulario de compra/solicitud de presupuesto
  - Campos extra:
    1.  Incidencias Administrativas
       - Factura errónea
       - No recepción de factura
    2.  Incidencias Internas
       - Solicitud mal hecha
       - Solicitud mal aprobada
       - No se ha enviado la factura al departamento de administración
