
-- 15. Получить общее число проектов, обеспечиваемых поставщиком П1
-- select count(*) from SPP where SupplierId = 1;

-- 28. Получить номера проектов, для которых не поставляются красные детали поставщиками из Лондона
-- select distinct ProjectId from SPP
-- where not (select color, city from Parts where id = SPP.PartId) = ("Красный", "Лондон") 

-- 36. Получить все пары номеров поставщиков, скажем, Пx и Пy, такие, что оба эти поставщика поставляют в точности одно и то же множество деталей.
select s1.SupplierId as Supplier1, s2.SupplierId as Supplier2
from (
    select SupplierId, GROUP_CONCAT(DISTINCT PartId ORDER BY PartId) AS PartsSet from SPP
    group by SupplierId
) s1
inner join (
    select SupplierId, GROUP_CONCAT(DISTINCT PartId ORDER BY PartId) AS PartsSet from SPP
    group by SupplierId
) s2 
on s1.PartsSet = s2.PartsSet and s1.SupplierId < s2.SupplierId;

-- 2. Получить полную информацию обо всех проектах в Лондоне
-- select * from Projects where city = "Лондон";

-- 7. Получить все такие тройки "номера поставщиков-номера деталей-номера проектов", для которых выводимые поставщик, деталь и проект не размещены в одном городе
-- select SupplierId, PartId, ProjectId from SPP
-- where not 
-- (select city from Parts where id = PartId) =
-- (select city from Suppliers where id = SupplierId) =
-- (select city from Projects where id = ProjectId);

-- 18. Получить номера деталей, поставляемых для некоторого проекта со средним количеством больше 320.
-- select PartId from SPP 
-- where (select avg(quantity)) > 320
-- group by PartId 

-- 22. Получить номера проектов, использующих по крайней мере одну деталь, имеющуюся у поставщика П1.
-- select distinct ProjectId from SPP where SupplierId = 1;

-- 26. Получить номера проектов, для которых среднее количество поставляемых деталей Д1 больше, чем наибольшее количество любых деталей, поставляемых для проекта ПР1
-- select distinct ProjectId from SPP where 
-- (select avg(quantity) from SPP where PartId = 1) >
-- (select max(quantity) from SPP where ProjectId = 1)

-- 3. Получить номера поставщиков, которые обеспечивают проект ПР1
-- select distinct SupplierId from SPP where ProjectId = 1;

-- 24. Получить номера поставщиков со статусом, меньшим чем у поставщика П1.
-- select id from Suppliers where status < (select status from Suppliers where id = 1);


