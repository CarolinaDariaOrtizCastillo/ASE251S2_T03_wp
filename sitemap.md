# Mapa del Sitio (Planificación del Proyecto)

Este documento describe la estructura de páginas y la arquitectura de la información del sitio web `programatransitabilidadVG.com`.

## 1. Páginas Públicas (Marketing y Contenido)

Estas son las páginas principales visibles para cualquier visitante y para Google.

* `/` (Homepage)
    * **Propósito:** Bienvenida principal. Resumen del programa, accesos directos a videos y presentación.
    * **Prioridad SEO:** 1.0 (Máxima)

* `/presentacion`
    * **Propósito:** Página informativa que detalla en qué consiste el programa, sus objetivos y beneficios.
    * **Prioridad SEO:** 0.9

* `/videos`
    * **Propósito:** Galería o sección con videos introductorios, testimonios o material explicativo.
    * **Prioridad SEO:** 0.8

* `/contacto`
    * **Propósito:** Muestra un formulario de contacto, teléfonos, dirección y/o mapa de ubicación.
    * **Prioridad SEO:** 0.6

* `/redes`
    * **Propósito:** Página que enlaza a los perfiles de redes sociales oficiales del programa (Facebook, LinkedIn, etc.).
    * **Prioridad SEO:** 0.5

* `/enlaces`
    * **Propósito:** Lista de enlaces de interés o sitios relacionados con el programa (instituciones, gobierno, etc.).
    * **Prioridad SEO:** 0.4

## 2. Páginas de Aplicación (Acceso y Registro)

Estas páginas son funcionales y no deben ser indexadas por Google.

* `/login`
    * **Propósito:** Formulario de inicio de sesión para usuarios registrados (estudiantes, instituciones).

* `/registro-estudiante`
    * **Propósito:** Formulario de registro para nuevos estudiantes.

* `/registro-institucion`
    * **Propósito:** Formulario de registro para nuevas instituciones.

* `/recuperar-password`
    * **Propósito:** Flujo para que los usuarios puedan restablecer su contraseña olvidada.

## 3. Páginas Privadas (Post-Login)

Estas páginas solo son accesibles para usuarios que han iniciado sesión.

* `/dashboard` (o `/panel-estudiante`)
    * **Propósito:** Panel principal del usuario después de iniciar sesión. Muestra cursos, progreso, etc.

* `/perfil`
    * **Propósito:** Página para que el usuario pueda ver y editar su información personal.

* `/mis-cursos`
    * **Propósito:** Lista de los cursos en los que el estudiante está inscrito.