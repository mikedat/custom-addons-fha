# Validaciones para ausencias de empleados

Extiende el módulo `base_tier_validation` para gestionar aprobaciones en ausencias (`hr.leave`).

### Dependencias
- `base_tier_validation`
- `hr_holidays`

### Instalación
1. Ves a la sección de aplicaciones de tu Odoo y busca "fha_leaves_tier_validation".


### Configuración
1. Activa el modo desarrollador en tu Odoo (Control+k y busca "debug").
2. Una vez activado el modo desarrollador, ves a Ajustes > Técnico > Validación de Nivel > Definición de Nivel.
3. Ya solo quedaría crear una nueva validación de nivel.

### Uso
1. Cuando estés dentro de esa sección y crees una nueva definición de nivel, podrás elegir el modelo "Ausencias".
2. Se debe elegir quién será el revisor de esas validaciones (Un usuario específico, cualquier persona de un grupo específico (Por ejemplo cualquier persona que esté dentro del grupo de RRHH) y campo en el registro relacionado)
3. Como herramienta adicional, debajo del formulario puedes añadir un dominio para filtrar por las ausencias que necesites.
   
#### Ejemplo de dominio
`[('numero_de_dias', '>', 3)]` 
con este dominio filtrariamos por el número de días de las ausencias entrantes.  
