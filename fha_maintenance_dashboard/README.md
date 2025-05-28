## Panel de Tareas para el Módulo de Mantenimiento
- Este módulo sirve para poder gestionar de manera más sencilla y ordeanada las tareas de mantenimiento

## Instalación
1. Primero, deberemos tener instalado el siguiente módulo: `maintenance`
2. Una vez instalado el módulo de mantenimiento, simplemente tendremos que buscar nuestro módulo e instalarlo

## Configuración
- Este módulo no requiere de una configuración previa para su uso.

## Uso del módulo
- Una vez tengamos ya todo instalado, para poder ver por primera vez nuestro panel de tareas simplemente tendremos que ir a Mantenimiento > Dashboard.

  ### ¿Qué información podrás encontrar en tu panel de tareas de mantenimiento?
  - Tendremos 4 subpaneles dentro de nuestro panel principal:
      1. Tareas caducadas:
         - En este subpanel tendremos listadas las tareas caducadas, estas serán las tareas las cuales están sin ejecutar y están fuera de plazo.
         - Tiene un botón "Más Tareas" para poder ver de manera mas detallada las tareas caducadas, al pulsar el botón te llevará a otra vista.
      2. Tareas pendientes:
         - En este subpanel tendremos listadas las tareas pendientes de ejecutar pero que todavía no están fuera de plazo.
         - Tiene un botón "Más Tareas" para poder ver de manera mas detallada las tareas pendientes de ejecutar, al pulsar el botón te llevará a otra vista.
      3. Tareas ejecutadas en Plazo:
         - En este subpanel podremos ver las tareas realizadas dentro del plazo establacido de la tarea.
      5. Tareas ejecutadas fuera de Plazo:
         - En este subpanel podremos ver las taeras realizadas fuera del plazo establecido de la tarea.
        

## Aspectos a tener en cuenta
- Las tareas que verás en el panel de mantenimiento dependerán de tu ROL dentro de Odoo, explico los casos:
    1. Eres Administrador de Odoo, podrás ver todas las tareas de todo el mundo, acceso completo.
    2. Eres Jefe del equipo de mantenimiento, podrás ver las tareas, tanto las tuyas propias como las de tu equipo.
    3. Eres un usuario normal, puedes ver tus propias tareas de mantenimiento.

- En las vistas asociadas a los botones de los subpaneles de "Tareas caducadas" y "Tareas pendientes", se le aplican unos filtros, estos filtros son los siguientes:
    1. Pendientes para el día, con este filtro mostramos las tareas pendientes para ese mismo día, este filtro está aplicado por defecto al entrar a la vista de las tareas pendientes.
    2. Pendientes para la semana, con este filtro mostramos las tareas pendientes para esta semana.
    3. Pendientes para el mes, con este filtro mostramos las tareas pendientes para ese mes.
    4. Pendientes para los próximos 6 meses, con este filtro mostramos las tareas pendientes para los próximos 6 meses.
    5. Pendientes para el próximo año, con este filtro mostramos las tareas pendientes para el próximo año.
 
- En las vistas asociadas a los botones de los subpaneles de "Tareas caducadas" y "Tareas pendientes", la vista por defecto es la tree, pero en caso de cambiarlo a vista kanban las tareas estarán agrupadas por equipo de mantenimiento.
