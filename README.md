# Flask REST API - cargamosShop 
API Creada con Flask para simular un sistema de inventario (API)


# Guía de instalación
### Clonar repositorio

```
git clone https://github.com/ABISUKI/cargamosShop.git
```
### Instalar dependencias

  ### linux(ubuntu environment)
  Si se tiene un ambiente linux(ubuntu) basta con ejecutar el siguiente comando 
  dentro de la carpeta cargamosShop
  ```
  source ./install
```

  ### Otro entorno de trabajo
  Si se esta trabajando con otro entorno se deberá installar todos lo requerimientos:
  
  1- Seguir todos los pasos manualmente del archivo
  ```
  environment.sh
  ```
  2- Seguir todos los pasos manualmente del archivo
  ```
  dbstart.sh
  ```

### Variables de entorno
 Por el moento las variables secretas se deberan de agregar en el entorno virtual
 ve al siguiente archivos y añade las variables de entorno requeridas
 ```
  dbstart.sh
  ```
  ```
  export POSTGRES_USER=youser
export POSTGRES_PWD=cargShop
export FLASK_HOST=0.0.0.0
export FLASK_PORT=8080

  ```
 
