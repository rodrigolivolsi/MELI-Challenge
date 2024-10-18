## Punto adicional que considero útil


Un aspecto adicional que agregaría sería la optimización de índices. Esto es debido al volumen de datos que se puede llegar a manejar (particularmente en ítems y órdenes), entonces crear índices en algunas tablas sobre campos que frecuentemente son consultados va a mejorar el rendimiento de las consultas considerablemente.


### Índices recomendados


Si tuviéramos que crear índices en base a los ejercicios propuestos, podríamos crear los siguientes para optimizar las consultas:


#### Primer ejercicio


En el primer ejercicio sería adecuado crear los índices de `fecha_nacimiento` en la tabla `Customer` y también crear el índice de `fecha` en la tabla `Order` con las siguientes sentencias:


```sql
CREATE INDEX indice_order_fecha ON Order(Fecha);
CREATE INDEX indice_customer_fecha_nacimiento ON Customer(Fecha_nacimiento);
```


Con el índice `indice_order_fecha` se va a optimizar la búsqueda de órdenes en el rango de fechas especificado (en el ejercicio sería del 1/1/2020 a 31/1/2020).
Lo mismo sucedería con el índice `indice_customer_fecha_nacimiento`, que optimizaría la búsqueda de la fecha de nacimiento del `Customer` para compararla con el día actual.
Además, si hubiera un índice sobre `Customer_id` en la tabla `Order`, la base de datos también podría utilizarlo para acelerar la operación de `JOIN` entre las tablas `Customer` y `Order`:


```sql
CREATE INDEX indice_order_customer_id ON Order(Customer_id);
```


#### Segundo ejercicio


El índice `indice_order_fecha` también sería útil ya que busca las fechas del año 2020. Adicionalmente, serían útiles los índices de `category_id` en la tabla `Item` y el índice de `id` en la tabla `Customer` para optimizar los `JOIN`:


```sql
CREATE INDEX indice_item_category_id ON Item(Category_id);
CREATE INDEX indice_customer_id ON Customer(id);
```


Adicionalmente, si se suelen hacer muchas consultas al `path` de la categoría, se podría considerar crear un índice sobre `category.path` o tener un campo de categoría padre (el más arriba en el árbol) que esté indexado.


#### Tercer ejercicio


En el tercer ejercicio también se podrían crear índices sobre la tabla `Item_History` sobre las columnas más consultadas, que podrían ser `item_id` y `fecha`:


```sql
CREATE INDEX indice_item_history_item_id ON Item_History(item_id);
CREATE INDEX indice_item_history_fecha ON Item_History(fecha);
```
