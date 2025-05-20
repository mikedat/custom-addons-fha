## Módulo para añadir nuevas funcionalidades en Compras

### ¿Qué funciones implementa este módulo?
 - Permisos para que los jefes de departamento y jefes de área puedan ver las compras de su departamentos.
 - Nuevos campos para la administración de incidencias de compras.
 - Añadir nuevo grupo "Seguidores de compras", nuevo submenú para poder ver las compras seguidas y permisos para este grupo, con los cuales no podrán editar compras seguidas.

### Instalación
 - Para poder instalar el módulo primero tendremos que tener instalados los siguientes módulo.
   - `base` (Viene incluido con odoo)
   - `contacts` (Viene incluido con odoo)
   - `purchase` (Viene incluido con odoo)
   - `hr` (Viene incluido con odoo)
   - `base_tier_validation`
  
 - Una vez tengamos todos los módulos requeridos, simplemente tendremos que ir a la sección de Aplicaciones de Odoo.
 - Buscamos el módulo `fha_purchases_update` y lo instalamos.


### Funciones más en profundidad
#### Permisos para jefes de departamento y de área 
- Se añaden 2 grupos nuevos "Jefes de Departamento" y "Jefe de Área" que permitirán que puedan ver las compras de su departamentos u áreas.
  #### Configuración
  - Para poder utilizar lo primero de todo necesitamos estar en modo desarrollador (Control + K > Buscar "depuración").
  - Ir a Ajustes > Usuarios y Compañías > Usuario.
  - Seleccionamos el usuario que queremos que tenga los permisos de Jefe de departamento o de área.
  - Bajamos hasta que veamos la sección de "PURCHASE".
  - Seleccionaremos "Jefe de Departamento" o "Jefe de Área" dependiendo de tus necesidades.
 

#### Administración de incidencias
- Se añaden nuevos campos en el formulario de compras, nuevos filtros y un nuevo grupo "Administadores de compras" para la gestión de incidencias.
  #### Configuración
  - Habrán dos casos de uso distintos, para los usuarios normales y para los usuarios los cuales serán "Administradores de compras", cabe decir que para los usuarios que no sean "Administradores de Compra" no necesitaremos hacer ninguna configuración previa, empezemos primero con los usuarios del nuevo grupo.
    -  Lo primero que deberemos de hacer es estar en modo desarrollador (Control + K > Buscar "depuración").
    -  Ir a Ajustes > Usuarios y Compañías > Usuario.
    -  Seleccionamos el usuario que queremos que esté en el grupo de "Administradores de compra".
    -  Bajamos hasta la sección de "PURCHASE".
    -  Seleccionamos "Administradores de Compras".
  - Una vez hayamos acabado cualquier tipo de configuración previa, si vamos al módulo de compra, a la hora de crear un nuevo registro se verá una nueva pestaña "Incidencias", dependiendo de si estás o no en el grupo "Administradores de compra" verás mas o menos campos
    - ¿Qué campos podré ver sin estar en grupo "Administradores de Compras"?
      -  Calificación, un campo tipo "selection" que sirve para calificar la compra.
      -  Retraso en la entrega, un campo tipo "boolean" que sirve para identificar si la compra se ha entregado fuera de plazo.
      -  Material defectuoso, un campo tipo "boolean" que sirve para identificar si el material de la compra está defectuoso.
      -  Material incompleto, un campo tipo "boolean" que sirve para identificar si el material de la compra está incompleto.
      -  Descrición adicional, un campo tipo "text" que sirve para poder añadir si es necesario una descripción adicional del pedido de compra.
    - ¿Qué campos podré ver si estoy dentro del grupo "Administradores de compras"?.
      -  Se incluyen los campos anteriormente mencionados
      -  Factura errónea, un campo tipo "boolean" que sirve para identificar si la factura de la compra es errónea.
      -  No recepción de fáctura, un campo tipo "boolean" que sirve para identificar si la factura de la compra no se ha recibido.
      -  Solicitud mal hecha, un campo tipo "boolean" que sirve para identificar si la factura de la compra se ha hecho mal.
      -  Solicitud mal aprobada, un campo tipo "boolean" que sirve para identificar si la solicitud de la compra se ha aprobado mal.
      -  No se ha enviado la factura al departamento de administración, un campo tipo "boolean" que sirve para identificar si la factura no se ha enviado al departamento de administración.
  - Filtros para Incidencias.
    - Dentro de las vistas, tenemos los filtros, tendremos 3 filtros
      - Retraso en la entrega, filtro para que nos salgan las compras que han llegado fuera de plazo de entrega.
      - Material defectuoso, filtro para que nos salgan las compras con material defectuoso.
      - Material Incompleto, filtro para que nos salgan las compras con material incompleto.
     
    
#### Seguidores de compras
- Se añade un nuevo grupo llamado "Seguidores de compras" y nuevo submenú para poder ver las compras que siguen
  #### Configuración
  - Para poder utilizar lo primero de todo necesitamos estar en modo desarrollador (Control + K > Buscar "depuración").
  - Ir a Ajustes > Usuarios y Compañías > Usuario.
  - Seleccionamos el usuario que queremos que sea un seguidor de compras.
  - Bajamos hasta que veamos la sección de "PURCHASE".
  - Seleccionaremos "Seguidores de compras".


   
