-- Respuestas del negocio

--1.Listar los usuarios que cumplan años el dia de hoy cuya cantidad de ventas realizadas en enero 2020 sea superior a 1500.

SELECT c.nombre, c.apellido, COUNT(o.id) AS cantidad_ventas
FROM Customer c
JOIN Order o ON c.id = o.customer_id
WHERE EXTRACT(MONTH FROM c.fecha_nacimiento) = EXTRACT(MONTH FROM CURRENT_DATE)
AND EXTRACT(DAY FROM c.fecha_nacimiento) = EXTRACT(DAY FROM CURRENT_DATE)  --Tambien se podria usar c.fecha_nacimiento = CURDATE() pero dependiendo el formato de la fecha puede fallar
AND o.fecha >= '2020-01-01' 
AND o.fecha <= '2020-01-31'  --Tambien podriamos usar o.fecha BETWEEN '2020-01-01' AND '2020-01-31'
GROUP BY c.id
HAVING COUNT(o.id) > 1500;


--2.Por cada mes del 2020, se solicita el top 5 de usuarios que mas vendieron($) en la categoría Celulares.

SELECT 
    EXTRACT(MONTH FROM o.fecha) AS mes,
    EXTRACT(YEAR FROM o.fecha) AS año,
    c.nombre, 
    c.apellido, 
    COUNT(o.id) AS cantidad_ventas, 
    SUM(o.cantidad) AS cantidad_productos_vendidos, 
    SUM(o.monto_total) AS monto_total
FROM Customer c
JOIN Order o ON c.id = o.customer_id
JOIN Item i ON o.item_id = i.id
JOIN Category cat ON i.category_id = cat.id
WHERE cat.path = 'Tecnología > Celulares y Teléfonos > Celulares y Smartphones' --No uso LIKE porque puede ser costoso y ademas no suelen usar indices, si es que los hay, de forma eficiente
AND EXTRACT(YEAR FROM o.fecha) = 2020
GROUP BY mes, año, c.nombre, c.apellido
ORDER BY monto_total DESC
LIMIT 5; --Para que solo traiga los 5 primeros, que serian los que mas vendieron porque esta en orden descendiente el monto_total


--3.Poblar una nueva tabla con el precio y estado de los items a fin del dia.

-- Creación de la tabla (la comento porque en realidad la tendria que haber puesto en el script DDL create_tables.sql
--CREATE TABLE Item_History (
--    item_id INT,
--    precio DECIMAL(10, 2),
--    estado VARCHAR(50),
--    fecha DATE,
--    PRIMARY KEY (item_id, fecha)
--);

-- Poblar la tabla a fin del dia (este ejemplo habria que asegurarse de ejecutarlo diariamente para mantener el historico, pero a continuacion dejo el codigo de como hacerlo con un stored procedure)
--INSERT INTO Item_History (item_id, precio, estado, fecha)
--SELECT id, precio, estado, CURRENT_DATE
--FROM Item;

--Aca dejo el codigo de como hacerlo con un stored procedure


CREATE PROCEDURE snapshot_items()
BEGIN
    --Inserto en la tabla Item_History el estado de los items a fin del dia
    INSERT INTO Item_History (item_id, precio, estado, fecha)
    SELECT id, precio, estado, CURDATE()
    FROM Item;
END;

