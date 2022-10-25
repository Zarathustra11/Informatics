# Informatics Чепкасов 041


Чисто таблиц: SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'


Выбрать число(*) из информационной схемы, где тип таблицы = 'основная таблица'


Названия таблиц: table_name FROM information_schema.tables


Имя таблицы из информационной схемы


Список пользователей: SELECT * FROM users;


выбрать всё из пользователей


Узнать все оценки: SELECT * FROM grades;


выбрать всё из оценок
  
  
Вывысти пользователей с оценками: SELECT * FROM users,grades WHERE users.user_id=grades.user_id;


Выбрать всё из пересечения таблиц users и grades


SELECT * FROM users WHERE fam='Чепкасов';


Выбрать всё из пересечения таблиц users, где фамилия = 'Чепкасов'
