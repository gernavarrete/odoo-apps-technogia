Cajero
======

El módulo **Cajero** ofrece una aplicación estilo PdV que centraliza la gestión
operativa de las cajas de cobro. Al instalarlo aparece como una aplicación más
en el *dashboard* principal de Odoo y permite:

* Crear sesiones de cajero ligadas a empleados y registrar montos de apertura/cierre.
* Visualizar, desde un panel, las órdenes pendientes de facturar y las ya
  procesadas.
* Lanzar un asistente para generar la factura correspondiente, registrar el
  pago con el diario autorizado y abrir automáticamente el documento impreso.
* Configurar, desde Ajustes, los diarios, impuestos, permisos y métodos de pago
  que cada compañía puede utilizar en el cajero, incluyendo diarios separados
  para moneda local y extranjera.
* Registrar pagos rápidos que aprovechan funcionalidades existentes de Ventas,
  Facturación y Punto de Venta.

Requisitos
----------

El módulo depende de ``sale_management``, ``account``, ``hr`` y
``point_of_sale`` porque reutiliza empleados, órdenes de venta y diarios
contables para reflejar los cobros realizados por caja.

Compatibilidad
--------------

La versión incluida en este repositorio está probada para **Odoo 18.0**.
