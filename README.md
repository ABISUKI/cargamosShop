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
### Ejecutar app (recuerda tener abierto tu entorno virtual)
```
  python run.py
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
 Para agregar un nuevo porducto , el tipo de producto  y marca deberá estar registrado en el archivo de configuracion 
 de otra manera la respuesta sería:
 
 ```
 {
  "Response": "product type not exists"
}

  ```
https://github.com/ABISUKI/cargamosShop/blob/main/etc/settings.yaml
Esto con el fin de tener un control de SKU acorde con el ERP - WMS
```
 definition_type:
  product_class:
    - EL  #ELECTRONIc
    - SP  #SPORTS
    - FT  #FOOTWEAR
  product_tags: {"PHONE":"PHN", "TV":"TV", "HEADPHONES":"HDPS", "SNIKERS":"SNK", "BOOTS":"BTS"}
  brand_tags: {"SAMMSUNG": "SMS", "HUAWEI":"HWI", "ASUS":"AS", "NIKE":"NK", "ADIDAS": "ADS", "CATERPILLAR":"CTPLL"}

  ```


#### SKU Model
![SKU model](https://github.com/ABISUKI/cargamosShop/blob/main/diagrams/producto-sku.jpg)

#### Shop Model
![Shop model](https://github.com/ABISUKI/cargamosShop/blob/main/diagrams/shopModel.jpg)

#### Product Model
![Porduct model](https://github.com/ABISUKI/cargamosShop/blob/main/diagrams/productModel.jpg)

#### Endpoints
![endpoints](https://github.com/ABISUKI/cargamosShop/blob/main/diagrams/endpoints.jpg)
