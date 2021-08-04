#sudo apt install postgresql postgresql-contrib
sudo -u postgres createdb Cargamos_Inventory
sudo -u postgres psql -c "\c Cargamos_Inventory"
sudo -u postgres psql -c "CREATE TABLE shops(id serial primary key,
    name varchar(30) NOT NULL,
    address varchar(60)NOT NULL,
    city varchar(30) NOT NULL,
    country varchar(30) NOT NULL,
    state varchar(30) NOT NULL,
    phone varchar(30) NOT NULL,
    schedule varchar(30) NOT NULL,
    warehouse varchar(30) NOT NULL
);"

sudo -u postgres psql -c "INSERT INTO shops (id, name, address, city, country, state, phone, schedule, warehouse)
VALUES ('1', 'test', 'test', 'test', 'test', 'test', 'test', 'test', 'test');"

sudo -u postgres psql -c "CREATE TABLE products_el(id serial primary key,
    type varchar(30) NOT NULL,
    model varchar(30)NOT NULL,
    brand varchar(30) NOT NULL,
    status boolean NOT NULL,
    color varchar(30) NOT NULL,
    sku varchar(30) NOT NULL,
    class varchar(30) NOT NULL,
    warehouse varchar(20) NOT NULL,
    extra varchar(40) NOT NULL,
    shop varchar(30) NOT NULL,
    idTime varchar NOT NULL,
    UNIQUE (idTime)
);"

sudo -u postgres psql -c "INSERT INTO products_el (id, type, model, brand, status, color, sku, class, warehouse, extra, shop, idTime)
VALUES (1, 'test', 'test', 'test', 'true', 'test', 'test', 'test', 'test', 'test','test','test');"


