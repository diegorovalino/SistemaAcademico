PROYECTO DE APLICACIONES

Instrucciones:
1-relizar el fork de este repositorio 
2-clonar localmente con $ git clone "URL", la URL se encuentra en la parte inferios derecha donde dice https despues de hacer fork
3-configurar la conexión a la bdd SistemaAcademico/wsgi/openshift/settings.py 
 la configuración que ya esta hecha es de la bdd de postgres de openshift, si ya tienen los datos de la bdd de la fica puede configurar ahí.
 
 la configuración debe hacerse en "else" porque no vamos a trabajar con bdd openshift.
*********************************************************************************************************************

23 if ON_OPENSHIFT:
 24     # os.environ['OPENSHIFT_MYSQL_DB_*'] variables can be used with databases created
 25     # with rhc cartridge add (see /README in this git repo)
 26     DATABASES = {
 27         'default': {
 28             'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'postgresql'    , 'mysql', 'sqlite3' or 'oracle'.
 29             'NAME':  'pythonok', # Or path to database file if using sqlite3.
 30             'USER': 'adminctdikkl',                      # Not used with sqlite3.
 31             'PASSWORD': 'BlGXW2nCVTvj',                  # Not used with sqlite3.
 32             'HOST': '127.2.119.2',                      # Set to empty string for localhost. Not used with     sqlite3.
 33             'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
 34         }
 35     }
 36 else:                         ***AQUÍ***
 37     DATABASES = {
 38         'default': {
 39             'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'postgresql'    , 'mysql', 'sqlite3' or 'oracle'.
 40             'NAME': 'pythonok',
 41             'USER': 'adminctdikkl',                      # Not used with sqlite3.
 42             'PASSWORD': 'BlGXW2nCVTvj',                  # Not used with sqlite3.
 43             'HOST': '127.2.119.2',                      # Set to empty string for localhost. Not used with     sqlite3.
 44             'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
 45         }
 46     }
********************************************************************************************************************

4. crear la app de su módulo con : python manage startapp "modulo"
5. hacer el seguimiento y commit git con : git commit -am 'creación de mi modulo' 
6. hacer el push de los datos a la cuenta github: git push
7. enviar el pull request desde la cuenta de github para subir a openshift
8. 
