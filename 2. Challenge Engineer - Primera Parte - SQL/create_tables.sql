-- Tabla Customer
CREATE TABLE Customer (
    id INT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    sexo CHAR(1),
    direccion TEXT,
    fecha_nacimiento DATE,
    telefono VARCHAR(20)
);

-- Tabla Item
CREATE TABLE Item (
    id INT PRIMARY KEY,
    nombre VARCHAR(255),
    precio DECIMAL(10, 2),
    estado VARCHAR(50),
    fecha_baja DATE,
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES Category(id)
);

-- Tabla Category
CREATE TABLE Category (
    id INT PRIMARY KEY,
    nombre VARCHAR(255),
    path VARCHAR(255) -- ejemplo: Tecnología > Celulares y Teléfonos > Celulares y Smartphones
);


-- Tabla Order
CREATE TABLE Order (
    id INT PRIMARY KEY,
    customer_id INT,
    item_id INT,
    cantidad INT,
    fecha TIMESTAMP,
    monto_total DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES Customer(id),
    FOREIGN KEY (item_id) REFERENCES Item(id)
);
