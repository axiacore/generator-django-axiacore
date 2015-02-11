Despliegue de la aplicación
===========================

1. Configuración inicial
------------------------

Para desplegar correctamente la aplicación es necesario tener como base
un sistema compatible con los modulos y tecnologias utilizadas en el
proyecto.

.. note:: Todos estos comandos son ejecutados en un sistema Ubuntu Linux


Paquetes básicos
^^^^^^^^^^^^^^^^

Algunas librerias del sistema son necesarias para compilar algunos
componentes necesarios del proyecto, estos paquetes ya pueden estar
instalados en el sistema operativo donde se hace el despliegue, sin
embargo es bueno confirmar antes de continuar.

.. code-block:: bash

    $ sudo apt-get install git-core
    $ sudo apt-get install build-essential
    $ sudo apt-get install python2.7-dev
    $ sudo apt-get install libxslt1-dev
    $ sudo apt-get install libxml2-dev
    $ sudo apt-get install python-dev
    $ sudo apt-get install libpq-dev
    $ sudo apt-get install postgresql-server-dev-9.1
    $ sudo apt-get install libjpeg62-dev zlib1g-dev libfreetype6-dev
    $ # Follow this: https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager#ubuntu-mint
    $ sudo npm install yuglify jshint uglify-js -g

.. note:: Si es un sistema diferente a Ubuntu los nombres de los paquetes
    pueden variar.



PIP
^^^

PIP es una utilidad que permite instalar paquetes de python de una
manera mas sencilla y compatible con multiples sistemas y requerimientos
de paquetes, es una mejora al sistema anterior llamado *easy_install*.

.. code-block:: bash

    $ sudo apt-get install python-setuptools
    $ sudo easy_install pip


Virtualenv
^^^^^^^^^^

*Virtualenv* es utilidad que permite crear entornos virtuales para la
ejecucion controlada de proyectos escritos en *Python*.

.. code-block:: bash

    $ sudo pip install virtualenv

Luego de tener instalada y configurada la herramienta para el manejo
de los entornos virtuales, procedemos a crear uno para alojar el proyecto.

.. code-block:: bash

    $ virtualenv {{ project_name }}_app

Luego de creado el entorno virtual lo cargamos.

.. code-block:: bash

    $ cd {{ project_name }}_app
    $ source bin/activate

El 'prompt' de la consola debe cambiar a algo similiar a:

.. code-block:: bash

    ({{ project_name }}_app)$

Ahora tenemos creado el entorno virtual que nos permite configurar un
ambiente único de ejecución para nuestro proyecto.


Creación de la base de datos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Es necesario realizar la creación de la base de datos para el proyecto.
Esto lo realizamos siguiendo los siguientes comandos:

.. code-block:: bash

    $ sudo -i
    $ su - postgres
    $ psql
    => CREATE ROLE {{ db_user }} LOGIN ENCRYPTED PASSWORD '{{ db_password }}' NOINHERIT VALID UNTIL 'infinity';
    => CREATE DATABASE {{ db_name }} WITH ENCODING='UTF8' OWNER={{ db_user }} TEMPLATE=template0;

Probamos conectarnos con el usuario de la aplicación:

.. code-block:: bash

    $ psql -d {{ db_name }} -U {{ db_user }}

Con estos pasos comprobados ya podemos vincular la aplicación a esta base
de datos.


Despliegue de código fuente
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ahora que tenemos configurada nuestra base de ejecución vamos a desplegar
el código fuente del proyecto, bien sea por GIT o desde un archivo empaquetado.

.. code-block:: bash

    ({{ project_name }}_app)$ pip install -r requirements.txt

Con lo cual se comienza el proceso de instalación de las librerias necesarias
por el proyecto, esto puede demorar varios minutos.


2. Configuración avanzada
-------------------------

A continuación se deben establecer los parámetros para que la aplicación
funcione de forma local en el fichero **local_settings.py** que debe ser
creado dentro de la carpeta app del proyecto. Los parametros a configurar son:


.. include:: base_files/local_settings.py
   :literal:


Se deben configurar los datos según los parametros del servidor de
producción. *Contacte a su administrador de plataforma si tiene dudas*.


3. Base de datos
----------------

Una vez configurado el proyecto, es necesario crear una base de datos de
acuerdo con la especificación hecha en el fichero **local_settings.py**.
Cuando esta base de datos exista, debe ser poblada con las tablas
necesarias por la aplicación.

.. code-block:: bash

    ({{ project_name }}_app)$ ./manage.py syncdb --all --noinput
    ({{ project_name }}_app)$ ./manage.py migrate --fake

.. note:: Tenga en cuenta que debe tener el entorno virtual activo

La ejecución de estos comandos le creará la base de datos con todas
las tablas y la información base utilizada para el desarrollo de la
aplicación, tenga en cuenta que estos comandos deben ser ejecutados
solamente cuando se despliegue el proyecto por primera vez.


4. Integración continua
-----------------------

Los pasos para la integración continua con jenkins son:

.. include:: base_files/jenkins.sh
   :literal:

