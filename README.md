# Аттестационное задание "Онлайн платформа-торговой сети электроники"
## Задание
Создайте веб-приложение с API-интерфейсом и админ-панелью.
Создайте базу данных, используя миграции Django.
## Требования к реализации:

Необходимо реализовать модель сети по продаже электроники.
Сеть должна представлять собой иерархическую структуру из трех уровней:

завод;
розничная сеть;
индивидуальный предприниматель.
Каждое звено сети ссылается только на одного поставщика оборудования (не обязательно предыдущего по иерархии). Важно отметить, что уровень иерархии определяется не названием звена, а отношением к остальным элементам сети, т. е. завод всегда находится на уровне 0, а если розничная сеть относится напрямую к заводу, минуя остальные звенья, ее уровень — 1.

## Каждое звено сети должно обладать следующими элементами:
Название.
Контакты:
email,
страна,
город,
улица,
номер дома.
Продукты:
название,
модель,
дата выхода продукта на рынок.
Поставщик (предыдущий по иерархии объект сети).
Задолженность перед поставщиком в денежном выражении с точностью до копеек.
Время создания (заполняется автоматически при создании).
## Сделать вывод в админ-панели созданных объектов.
На странице объекта сети добавить:

ссылку на «Поставщика»;
фильтр по названию города;
admin action, очищающий задолженность перед поставщиком у выбранных объектов.
## Используя DRF, создать набор представлений:
CRUD для модели поставщика (запретить обновление через API поля «Задолженность перед поставщиком»).

Добавить возможность фильтрации объектов по определенной стране.

## Настроить права доступа к API так, чтобы только активные сотрудники имели доступ к API.

## Инструкция по запуска проекта:
В файле .env.example обязательно следует указать SECRET_KEY, а также предоставить значения для других переменных окружения, которые могут быть установлены по умолчанию. Важно помнить, что эти значения следует изменить перед запуском проекта, чтобы обеспечить безопасность.

Для установки всех необходимых зависимостей необходимо активировать виртуальное окружение, выполнив команду env\Scripts\activate, а затем установить пакеты, перечисленные в файле requirements.txt, с помощью команды pip install -r requirements.txt.

Прежде чем начать использовать приложение, необходимо создать базу данных. Для этого следует подключиться к серверу PostgreSQL с помощью команды psql -U <ваш логин>, ввести пароль, а затем выполнить команду create database <название базы данных>;. После подтверждения создания базы данных можно выйти из интерфейса PostgreSQL, набрав команду \q.

Затем следует применить миграции к базе данных, используя команду python manage.py migrate, чтобы создать необходимые таблицы и структуру данных. После этого можно запустить сервер, выполнив команду python manage.py runserver.

Для доступа к административной панели приложения необходимо создать суперпользователя. Для этого можно воспользоваться командой python manage.py csu. По умолчанию будут использованы логин 'admin@sky.pro' и пароль '12345', но рекомендуется изменить их на более безопасные значения.
