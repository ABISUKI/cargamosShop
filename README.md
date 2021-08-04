# Flask REST API - cargamosShop 
API Creada con Flask para simular un sistema de inventario (API)

DB : postgresql

NOTA: procesamiento asyncrono aun no iplementado :(.

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
 Por el moento las variables secretas se deberan de agregar en el entorno virtual.
 Añade las variables de entorno requeridas en el siguiente archivo

 ```
  env-shop/bin/activate
  ```
  ```
  export POSTGRES_USER=postgres
export POSTGRES_PWD=
export FLASK_HOST=0.0.0.0
export FLASK_PORT=8080

  ```
### cambiar contraseña
login
sudo -u postgres psql

cambiando contraseña:
\password

### Test (Pytest)
 Dentro de la carpeta cargamosShop se ejcuta el siguiente comand.
 ```
  pytest -v
  ```
### Problemas comunes
```
   raise KeyError(key) from None
KeyError: 'POSTGRES_USER'

  ```
  Las variables de entorno son temporales , exportalas manualmente
  o ve al archivo env-shop/bin/activate e añadelas permanetemente
  así cada vez que se active el entorno se crearán automaticamente.


### Simple Iformación

#### SKU Model
![SKU model](https://github.com/ABISUKI/cargamosShop/blob/main/diagrams/producto-sku.jpg)

#### Shop Model
![Shop model](https://github.com/ABISUKI/cargamosShop/blob/main/diagrams/shopModel.jpg)

#### Product Model
![Porduct model](https://github.com/ABISUKI/cargamosShop/blob/main/diagrams/productModel.jpg)

#### Endpoints
![endpoints](https://github.com/ABISUKI/cargamosShop/blob/main/diagrams/endpoints.jpg)
