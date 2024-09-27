use testdb;

-- 1.1. Получить полную информацию обо всех преподавателях.
-- select * from Lecturers;

-- 1.2. Получить полную информацию обо всех студенческих группах на специальности ЭВМ.
-- select * from StudentGroups where speciality = 'ЭВМ';

-- 1.3. Получить личный номер преподавателя и номера аудиторий, в которых они преподают предмет с кодовым номером 18П.
-- select LecturerId, Auditory from LSG where SubjectId = 18;

-- 1.4. Получить номера предметов и названия предметов, которые ведет преподаватель Костин.
-- select id, name from Subjects where id in
-- (select SubjectId from LSG where LecturerId = (select id from Lecturers where lastName = 'Костин'));

-- 1.5. Получить номер группы, в которой ведутся предметы преподавателем Фроловым.
-- select GroupId from LSG where LecturerId = (select id from Lecturers where lastName = 'Фролов');

-- 1.6. Получить информацию о предметах, которые ведутся на специальности АСОИ.
-- select * from Subjects where Speciality = "АСОИ";

-- 1.7. Получить информацию о преподавателях, которые ведут предметы на специальности АСОИ.
-- select * from Lecturers where Speciality like "%АСОИ%";

-- 1.8. Получить фамилии преподавателей, которые ведут предметы в 210 аудитории.
-- select lastName from Lecturers where id in (select LecturerId from LSG where Auditory = 210)

-- 1.9. Получить названия предметов и названия групп, которые ведут занятия в аудиториях с 100 по 200.
-- select subjects.Name, StudentGroups.Id from LSG
-- join subjects on LSG.SubjectId = subjects.Id
-- join StudentGroups on LSG.GroupId = StudentGroups.Id 
-- where LSG.auditory between 100 and 200;

-- 1.10. Получить пары номеров групп с одной специальности.
-- select g1.name, g2.name from StudentGroups g1, StudentGroups g2 where g1.speciality = g2.speciality and g1.name <> g2.name;

-- 1.11. Получить общее количество студентов, обучающихся на специальности ЭВМ.
-- select sum(students) from StudentGroups where speciality = 'ЭВМ'

-- 1.12. Получить номера преподавателей, обучающих студентов по специальности ЭВМ
-- select id from lecturers where speciality like "%ЭВМ%";

-- 1.13. Получить номера предметов, изучаемых всеми студенческими группами
-- select distinct subjectid from LSG;

-- 1.14. Получить фамилии преподавателей, преподающих те же предметы, что и преподавательпреподающий предмет с номером 14П
-- select l.lastName from lecturers l
-- inner join lsg m on m.lecturerid = l.id
-- where m.subjectid = 14
-- group by l.lastName;

-- 1.15. Получить информацию о предметах, которые не ведет преподаватель с личным номером 221П.
-- select s.id, s.name, s.hours, s.speciality, s.semester from subjects s
-- join LSG m on m.SubjectId = s.Id
-- where m.LecturerId <> 221;

-- 1.16. Получить информацию о предметах, которые не изучаются в группе М-6
-- select s.id, s.name, s.hours, s.speciality, s.semester from subjects s
-- join LSG m on m.SubjectId = s.Id
-- join StudentGroups g on g.Id = m.GroupId
-- where g.Name <> "М-6";

-- 1.17. Получить информацию о доцентах, преподающих в группах 3Г и 8Г
-- select distinct l.id, l.lastname from lecturers l
-- join LSG m on m.LecturerId = l.Id
-- where m.GroupId IN (3, 8) AND l.position = "Доцент";

-- 1.18. Получить номера предметов, номера преподавателей, номера групп, в которых ведут занятияпреподаватели с кафедры ЭВМ, имеющих специальность АСОИ.
-- select m.SubjectId, m.LecturerId, m.GroupId from LSG m
-- join lecturers l on m.LecturerId = l.Id
-- where l.department = "ЭВМ" and l.speciality like "%АСОИ%";

-- 1.19. Получить номера групп с такой же специальностью, что и специальность преподавателей
-- select distinct g.Id from StudentGroups g
-- join lecturers l on g.Speciality = l.Speciality;

-- 1.20. Получить номера преподавателей с кафедры ЭВМ, преподающих предметы по специальности, совпадающей со специальностью студенческой группы
-- select t.Id from Lecturers t
-- inner join LSG m on m.LecturerId = t.Id
-- inner join StudentGroups s on s.Id = m.GroupId
-- inner join subjects sj on sj.Id = m.SubjectId
-- where t.Department = "ЭВМ" and s.Speciality = sj.Speciality
-- group by t.Id;

-- 1.21. Получить специальности студенческой группы, на которых работают преподаватели кафедры АСУ
-- select distinct s.speciality from StudentGroups s
-- join LSG m on s.Id = m.GroupId
-- join Lecturers t on m.LecturerId = t.Id
-- where department = "АСУ";

-- 1.22. Получить номера предметов, изучаемых группой АС-8.
-- select m.SubjectId from LSG m
-- join StudentGroups s on m.GroupId = s.Id
-- where s.Name = "АС-8";

-- 1.23. Получить номера студенческих групп, которые изучают те же предметы, что и студенческая группа АС-8
-- select distinct GroupId from LSG
-- where SubjectId in (
--  select SubjectId from LSG 
--  join StudentGroups
--  on LSG.GroupId = StudentGroups.Id
--  where StudentGroups.Name = 'АС-8'
-- );

-- 1.24. Получить номера студенческих групп, которые не изучают предметы, преподаваемых в студенческой группе АС-8.
-- select distinct GroupId from LSG
-- where SubjectId not in (
--  select SubjectId from LSG 
--  join StudentGroups
--  on LSG.GroupId = StudentGroups.Id
--  where StudentGroups.Name = 'АС-8'
-- );

-- 1.25. Получить номера студенческих групп, которые не изучают предметы, преподаваемых преподавателем 430Л
-- select distinct GroupId from LSG 
-- where LecturerId not in (
--	select LecturerId from LSG
-- 	where LSG.LecturerId = 430
-- );

-- 1.26. Получить номера преподавателей, работающих с группой Э-15, но не преподающих предмет 12П
-- select m.LecturerId from LSG m
-- join StudentGroups s on s.Id = m.GroupId
-- where s.Name = "Э-15" AND m.SubjectId != 12;

