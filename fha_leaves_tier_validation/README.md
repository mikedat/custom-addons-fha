# Validaciones para ausencias de empleados

Extiende el módulo `base_tier_validation` para gestionar aprobaciones en ausencias (`hr.leave`).

### Dependencias
- `base_tier_validation`
- `hr_holidays`

### Instalación
1. Ves a la sección de aplicaciones de tu Odoo y busca "fha_leaves_tier_validation".


### Configuración
1. Activa el modo desarrollador en tu Odoo (Control+k y busca "Depuración").
2. Una vez activado el modo desarrollador, ves a Ajustes > Técnico > Validación de Nivel > Definición de Nivel.
3. Ya solo quedaría crear una nueva validación de nivel.
4. Si has podido entrar a las validaciones de nivel ya has completado todo tipo de configuración necesaria para el uso del módulo.

### Uso
1. Cuando estés dentro de esa sección, hazle clic al botón de Nuevo.
2. Una vez estemos dentro del formulario, tendremos que tener en cuenta ciertos campos importantes a la hora de crear la validación de nivel.
    - Módelo referenciado, campo "many2one" para seleccionar sobre qué modelo queremos aplicar los avisos, en este caso sería Ausencias.
    - Validado por, campo "review_type" para seleccionar un tipo de validación (Usuario específico, Cualquier usuario de un grupo específico y Campo en el registro relacionado).
    - Dependiendo de lo que hayamos seleccionado el siguiente campo cambiará a uno de estos tres:
       - Revisor, campo "many2one" para poder seleccionar al usuario que queramos que sea el revisor.
       - Grupo Revisor, campo  "reviewer_group_id" para poder seleccionar al grupo específico que queramos que revise las validaciones.
       - Campo revisor, campo "reviewer_field_id" para poder seleccionar el campo de registro relacionado que queramos utilizar para las validaciones de nivel.
    - Compañía    
4. Como herramienta adicional, debajo del formulario puedes añadir un dominio para filtrar por las ausencias que necesites.
   
#### Ejemplo de dominio
`[('numero_de_dias', '>', 3)]`
 - con este dominio filtrariamos por el número de días de las ausencias entrantes.
 - Veriamos una ausencia de mas de 3 días pero no una de 3 días o menos.
