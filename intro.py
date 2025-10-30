# Django — это фреймворк на Python для веб-разработки.
# Он помогает быстро создавать сайты и веб-приложения.
# Основан на принципе MTV (Model–Template–View) — 
#                          это похоже на MVC (Model–View–Controller).

# Model — это работа с данными (как таблица в базе данных).
# Template — это внешний вид (HTML-страницы).
# View — это логика (код, который обрабатывает запросы).



# Библиотека — это как набор инструментов (молоток, отвертка, линейка). 
# Ты сам решаешь, как их использовать.

# Фреймворк — это уже половина построенного дома, в который ты вставляешь 
# свои окна и двери. Он задаёт структуру проекта.


# venv
# Представь, у тебя есть кухня. В каждой семье разные продукты.
# Чтобы не перепутать продукты между семьями, каждому проекту делают свою кухню → это и есть venv.

# venv — это папка, в которой хранятся библиотеки только для одного проекта.
# Так ты избежишь конфликтов версий (например, в одном проекте Django 5, в другом Django 4).





# MTV
# Model (Модель) → отвечает за работу с базой данных. (Таблицы → Классы Python)
# Template (Шаблон) → отвечает за внешний вид, HTML-страницы.
# View (Представление) → связывает модель и шаблон, управляет логикой.




# Поток работы MTV

# Пользователь отправляет запрос (HTTP)
# Например, открывает страницу /students/.

# URLConf (urls.py)
# Django ищет, какое View обрабатывать этот путь.

# View
# View берёт нужные данные (часто через Model) и решает, какой шаблон вернуть.

# Model
# Если нужны данные из базы, View обращается к модели.

# Template
# View передаёт данные в шаблон → шаблон формирует HTML → возвращается пользователю.






# Models (Модели) в Django
# 1. Что такое модель?

# Модель — это Python-класс, который описывает таблицу в базе данных.
# Каждое поле класса = колонка в таблице.
# Каждый объект модели = строка в таблице.


# 2. Зачем нужны модели

# Абстракция: программист работает с Python-классами, а не с SQL-запросами.
# Безопасность: Django защищает от SQL-инъекций. SQL-инъекция (или внедрение SQL-кода) — это метод взлома
# Удобство: можно создавать, изменять, удалять данные одной строкой кода.

from django.db import models

class Student:
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()


# Создать студента
Student.objects.create(name="Ali", age=20, email="ali@gmail.com")

# Получить всех студентов
students = Student.objects.all()

# Найти по имени
ali = Student.objects.get(name="Ali")

# Фильтрация
young = Student.objects.filter(age__lt=25) # less then



# 3. ORM (Object-Relational Mapping)

# ORM = мост между Python-кодом и базой данных.
# Ты пишешь Student.objects.all() → Django делает SELECT * FROM student.
# Ты пишешь Student.objects.create() → Django делает INSERT INTO student....
# То есть, ORM переводит Python → SQL.





# Views (Представления)

# View — это функция или класс в Django, который принимает запрос (request) и возвращает ответ (response) пользователю.
# Проще говоря, view решает:
# что показать пользователю,
# какие данные взять из базы,
# какой HTML-шаблон отдать.


# Виды Views:

# 1. Функциональные (Function-Based Views, FBV)
# Простая функция, которая принимает request и возвращает HttpResponse.

# 2. Классовые (Class-Based Views, CBV)
# Позволяют писать более структурированный код.

from django.views import View
from django.http import HttpResponse

class HelloView(View):
    def get(self, request):
        return HttpResponse("Привет от CBV!")



# Templates (Шаблоны)

# Template — это HTML-файл с динамическими данными.
# Django использует шаблонизатор, чтобы вставлять Python-переменные в HTML.


# Связь между View и Template

# Пользователь заходит на URL.
# Django вызывает View (функцию/класс).
# View может взять данные из базы.
# View рендерит Template, подставляя данные.
# Пользователь видит HTML-страницу.





# Что такое Static files?

# Static files — это файлы, которые не меняются динамически (в отличие от шаблонов).
# Примеры:
# CSS (стили),
# JavaScript (скрипты),
# изображения (jpg, png, svg).


# Где хранить static файлы?

# Обычно Django ищет статику в двух местах:
# В папке каждого приложения → app_name/static/app_name/
# В общей папке static/ в корне проекта.


# Настройки в settings.py

# # Где Django будет искать статику
# STATIC_URL = '/static/'

# # Папка для общей статики (создаём вручную)
# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]

# # Папка для собранных файлов (для деплоя)
# STATIC_ROOT = BASE_DIR / "staticfiles"


# python manage.py collectstatic — собирает все статические файлы из приложений в одну папку (STATIC_ROOT), 
# чтобы потом использовать на сервере.






# PIP
# Что такое pip?

# pip (Python Installer Package) — это инструмент для установки, обновления и удаления библиотек (пакетов) в Python.
# Пример: Django, Requests, Numpy и т.д.

# Пакеты скачиваются из PyPI (Python Package Index) — это как "Play Market/App Store", только для Python.


# Основные команды pip

# Проверка версии pip
# pip --version

# Установка пакета
# pip install package_name

# Установка конкретной версии
# pip install django==4.2

# Обновление пакета
# pip install --upgrade package_name

# Удаление пакета
# pip uninstall package_name

# Список установленных пакетов
# pip list 

# Информация о пакете
# pip show package_name

# Заморозка зависимостей (для сохранения всех пакетов в проекте)
# pip freeze > requirements.txt
# Файл requirements.txt содержит список всех библиотек и их версий.

# Установка пакетов из requirements.txt
# pip install -r requirements.txt







# Что такое админ-панель Django?

# Это встроенный интерфейс для управления данными в базе (CRUD — Create, Read, Update, Delete).
# Автоматически генерируется для моделей.
# Очень удобно для админов, тестов, менеджеров.
# Чтобы включить её, в settings.py уже есть:

# INSTALLED_APPS = [
#     ...
#     'django.contrib.admin',
#     ...
# ]

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


# 1. list_display
# Показывает колонки в списке объектов.

# 2. search_fields
# Добавляет строку поиска.
# Можно искать даже по ForeignKey (search_fields = ('category__name',)).

# 3. list_filter
# Фильтрация справа по указанным полям.

# 4. ordering
# Сортировка по умолчанию.

# 5. list_editable
# Позволяет редактировать поля прямо в списке.

# 6. list_per_page
# Сколько записей отображать на одной странице.

# 7. readonly_fields
# Поля только для чтения (например, даты).

# 8. fieldsets
# Группировка полей в админке.

# 9. prepopulated_fields
# Автогенерация значений. Например, last_name из name:
prepopulated_fields = {'last_name': ('name',)}

# 10. date_hierarchy
# Навигация по датам сверху.
date_hierarchy = 'created_at'

# 11. fields
# Определяет порядок и набор отображаемых полей в форме.

# 12. exclude
# Исключает поля из формы редактирования.

# 13. actions
# Создаёт кастомные действия для списка объектов.

# @admin.action(description="Активировать пользователей")
# def make_active(modeladmin, request, queryset):
#     queryset.update(is_active=True)

# actions = [make_active]


# 14. list_display_links
# Делает поля из list_display кликабельными для перехода в детали объекта.

# 15. save_on_top
# Кнопки "Сохранить" появляются сверху формы.








# Основные HTTP методы

# 1. GET

# Используется для получения данных с сервера.
# Безопасный метод: ничего не изменяет в БД.
# Данные можно передавать через query params (например: ?id=5).
# Пример: открыть страницу студента. 
# GET /students/5


# 2. POST

# Используется для создания новых данных (например, новый студент).
# Данные передаются в теле запроса (формы или JSON).
# Не отображаются в адресной строке.
# Может изменять базу данных. 
# POST /students/create


# 3. PUT

# Используется для полного обновления объекта.
# Обычно в API: заменить весь объект новыми данными.
# Редко используется в HTML-формах, чаще в REST API.
# PUT /students/5


# 4. PATCH

# Используется для частичного обновления объекта (обновить только одно поле).
# Более гибкий, чем PUT.
# PATCH /students/5


# 5. DELETE

# Используется для удаления данных с сервера.
# Опасный метод: удаляет объект навсегда (если не реализовать "soft delete").
# DELETE /students/5


# Additional Methods ------

# 6. HEAD

# Как GET, но возвращает только заголовки, без тела.
# Используется для проверки доступности ресурса.


# 7. OPTIONS

# Запросить у сервера список доступных методов для ресурса.
# Пример: сервер может ответить, что поддерживает GET, POST, PUT, DELETE.


# GET → читать данные
# POST → создавать новые
# PUT → полностью обновить
# PATCH → частично обновить
# DELETE → удалить
# HEAD, OPTIONS → служебные





# Что такое CSRF?

# CSRF (Cross-Site Request Forgery) — это атака, (Подделка межсайтовых запросов)
# при которой злоумышленник заставляет пользователя выполнить нежелательный запрос на сайт, где он уже авторизован.

# Ты залогинен в интернет-банке.
# Заходишь на другой сайт с картинками.
# Там скрыта форма:

# <form action="https://bank.com/transfer" method="POST">
#     <input type="hidden" name="to" value="hacker_account">
#     <input type="hidden" name="amount" value="1000">
# </form>

# <script>document.forms[0].submit()</script>

# zапрос отправляется от твоего имени → деньги украдены


# Как работает CSRF-защита в Django?

# Django добавляет уникальный токен (строку) в каждую HTML-форму.
# Этот токен сверяется на сервере при каждом POST-запросе.
# Если токен отсутствует или неправильный → запрос блокируется.


# На сервере Django проверяет:

# Есть ли токен в форме.
# Совпадает ли он с токеном из сессии пользователя.
# Если да → запрос проходит.
# Если нет → ошибка 403 Forbidden (CSRF verification failed).


# Important Points

# CSRF нужен только для POST, PUT, PATCH, DELETE (т.е. методов, которые изменяют данные).
# Для GET → не обязателен.
# Django автоматически подключает CSRF через django.middleware.csrf.CsrfViewMiddleware.
# Если работаешь с AJAX / fetch / axios, нужно передавать токен вручную.

# fetch("/submit/", {
#   method: "POST",
#   headers: {
#     "X-CSRFToken": "{{ csrf_token }}"
#   },
#   body: JSON.stringify({name: "Hoji"})
# })







# Что такое фильтры в Django?

# Фильтры — это способ отбирать (фильтровать) данные из базы данных по определённым условиям.
# Обычно мы используем фильтры вместе с QuerySet, то есть когда мы запрашиваем данные из модели.

# Django-filter (библиотека)

# Есть также отдельная библиотека django-filter, которая помогает фильтровать 
# данные прямо в API или на странице без написания кучи кода.










# Что такое Git?

# Git — это система контроля версий (Version Control System).
# Она помогает программистам сохранять историю изменений в коде и работать в команде, не теряя данные.


# Простыми словами:
# Git — это как «машина времени» для твоего кода.
# Можно увидеть, кто что изменил, откатиться назад, объединить код и т.д.


# Что такое GitHub?

# GitHub — это онлайн-платформа, где хранятся ваши проекты Git.
# Это как «облако» для кода.
# Можно загружать туда свой репозиторий и делиться с другими.

# Аналогичные сайты:

# GitLab
# Bitbucket
# Gitea



# Основные команды Git

# | Команда                      | Что делает                                                |
# | ---------------------------- | --------------------------------------------------------- |
# | `git init`                   | Создаёт новый Git-репозиторий в папке                     |
# | `git status`                 | Показывает состояние проекта (изменения, новые файлы)     |
# | `git add .`                  | Добавляет все изменения в «индекс» (подготовка к коммиту) |
# | `git commit -m "текст"`      | Сохраняет изменения с комментарием                        |
# | `git log`                    | Показывает историю коммитов                               |
# | `git diff`                   | Показывает разницу между версиями файлов                  |
# | `git restore <file>`         | Отменяет изменения файла                                  |
# | `git rm <file>`              | Удаляет файл из репозитория                               |
# | `git branch`                 | Показывает список веток                                   |
# | `git checkout -b new_branch` | Создаёт и переключается на новую ветку                    |
# | `git merge branch_name`      | Объединяет другую ветку с текущей                         |
# | `git clone <url>`            | Копирует чужой репозиторий                                |
# | `git pull`                   | Забирает последние изменения с GitHub                     |
# | `git push`                   | Отправляет свои изменения на GitHub                       |








# Class-Based Views — это представления (views), написанные на основе классов, а не функций.

# Разница:

# FBV — это простая функция
# CBV — это класс, где каждый HTTP-метод (GET, POST, PUT, DELETE) — это метод класса


from django.views import View

# class StudentCreateView(View):
#     def get(self, request):
#         return render(request, 'create_student.html')
    
#     def post(self, request):
#         name = request.POST.get('name')
#         Student.objects.create(name=name)
#         return render(request, 'success.html')



# Преимущества CBV

# Код становится структурированным и переиспользуемым
# Легко расширять (через наследование)

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
# Django уже даёт готовые классы, например ListView, DetailView, CreateView, UpdateView, DeleteView



# class StudentListView(ListView):
#     model = Student
#     template_name = 'students.html'
#     context_object_name = 'students'


# class StudentDetailView(DetailView):
#     model = Student
#     template_name = 'student_detail.html'
#     context_object_name = 'student'



# «Class-Based Views — это объектно-ориентированный способ писать представления.
# Вместо одной функции для всех действий, мы используем методы класса: get, post, put, delete.
# Django уже даёт много готовых классов, чтобы писать меньше кода и работать быстрее.»






# TemplateView — это класс-представление, которое просто отображает HTML-шаблон без сложной логики.




# class HomeView(TemplateView):
#     template_name = 'index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Главная страница'
#         context['students'] = 
#         return context

 

# Зачем нужен TemplateView

# Когда нужно просто отобразить страницу (о нас, контакты, главная и т.д.)
# Не нужно писать ручную функцию
# Более чистый и структурированный код





# In Class-Based Views

# Paginations
# paginate_by = 10


# Forms
# form_class = StudentForm


# Filters
# from django_filters.views import FilterView

# class StudentFilterView(FilterView):
#     model = Student
#     template_name = 'students.html'
#     context_object_name = 'students'
#     filterset_class = StudentFilter
#     paginate_by = 10






# Сигналы (Signals) — это способ сообщать другим частям программы, что произошло какое-то событие.
# Например:

# пользователь зарегистрировался → отправляем приветственное письмо
# студент удалён → удаляем его аватар из папки
# создана группа → создаём запись в статистике

# Проще говоря:
# Сигнал = событие, на которое можно “подписаться” и реагировать кодом.


# Как работают сигналы

# Есть две стороны:

# | Роль                      | Описание                                                                  |
# | ------------------------- | ------------------------------------------------------------------------- |
# | **Отправитель (Sender)**  | Модель или объект, который “посылает сигнал” (например, `Student.save()`) |
# | **Получатель (Receiver)** | Функция, которая “слушает сигнал” и выполняет действия                    |



# Основные встроенные сигналы Django
# Сигнал	Когда срабатывает
# pre_save	Перед сохранением объекта
# post_save	После сохранения объекта
# pre_delete	Перед удалением объекта
# post_delete	После удаления объекта
# m2m_changed	При изменении связи ManyToMany
# request_started	Перед обработкой HTTP-запроса
# request_finished	После завершения запроса
# user_logged_in / user_logged_out	При входе/выходе пользователя









# Template Tags и Template Filters

# Когда мы пишем HTML в Django, мы можем вставлять переменные, условия, циклы и встроенные функции прямо в шаблон.
# Это делается с помощью тегов и фильтров.


# 1. Template Tags (теги шаблонов)

# Теги — это специальные команды Django, которые добавляют логику в шаблон:
# условия, циклы, подключение других файлов и т.д.

# Теги всегда пишутся в фигурных скобках и с процентами:







# 2. Template Filters (фильтры шаблонов)

# Фильтры — это функции, которые изменяют вывод переменной.
# Они пишутся через вертикальную черту |.


# {{ student.name|upper }}



# Популярные фильтры Django:

# upper	Преобразует в верхний регистр	`{{ name|
# lower	Преобразует в нижний регистр	`{{ name
# title	Делает каждое слово с заглавной буквы	`{{ name
# length	Возвращает длину строки или списка	`{{ students
# default:"-"	Возвращает дефолтное значение, если пусто	`{{ student.age
# date:"d.m.Y"	Форматирует дату	`{{ student.join_date
# truncatechars:10	Обрезает строку после 10 символов	`{{ text
# add:10	Прибавляет число	`{{ student.age
# join:", "	Объединяет список через запятую	`{{ list
# slice:":3"	Берёт первые 3 элемента	`{{ students
# yesno:"Да,Нет"	Выводит "Да"/"Нет" для True/False	`{{ student.is_active







# 3. Пользовательские фильтры и теги

# Можно создавать свои фильтры и теги, если стандартных недостаточно.

# Пример — создадим фильтр, который делает текст с восклицанием:

# from django import template

# register = template.Library()

# @register.filter
# def excited(value):
#     return f"{value}!!!"






from django.contrib.sessions.models import Session




# Cookie (куки)

# Cookie — это небольшой файл, который сервер отправляет браузеру пользователя.
# Браузер сохраняет его и отправляет обратно при каждом запросе на этот же сайт.

# Используются для:

# Запоминания авторизации
# Корзины покупок
# Настроек пользователя (язык, тема и т.д.)


# Пример работы cookie в Django


def set_cookie_view(request):
    response = HttpResponse("Кука установлена!")
    response.set_cookie('username', 'Hojiakbar', max_age=3600) 
    return response


# set_cookie(name, value, max_age) — добавляет cookie в ответ сервера.





# Прочитать cookie


# def get_cookie_view(request):
#     username = request.COOKIES.get('username', 'Гость')
#     return HttpResponse(f"Привет, {username}!")


# request.COOKIES — словарь со всеми куками пользователя.



# Удалить cookie

# def delete_cookie_view(request):
#     response = HttpResponse("Кука удалена!")
#     response.delete_cookie('username')
#     return response




# Session (сессия)

# Session — это способ хранить данные на сервере,
# а в браузере хранится только идентификатор (sessionid).



# Используется для:

# Авторизации пользователей
# Хранения данных между запросами
# Безопасной передачи состояния



# Как Django хранит сессии

# Пользователь заходит → Django создаёт уникальный sessionid
# Этот sessionid отправляется браузеру в cookie
# Все данные (user_id, корзина и т.д.) сохраняются на сервере (в базе данных)


# Установить данные в сессию

def set_session_view(request):
    request.session['username'] = 'Hojiakbar'
    request.session['age'] = 22
    return HttpResponse("Сессия установлена!")


# Прочитать данные из сессии

# def get_session_view(request):
#     username = request.session.get('username', 'Гость')
#     return HttpResponse(f"Привет, {username}!")



# Удалить конкретное значение
# def delete_session_key(request):
#     if 'username' in request.session:
#         del request.session['username']
#     return HttpResponse("Поле username удалено из сессии")


# Очистить всю сессию

# def clear_session(request):
#     request.session.flush()
#     return HttpResponse("Сессия полностью очищена!")
