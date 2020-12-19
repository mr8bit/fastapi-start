## Стартовый пример с авторизацией на FastAPI

### Запуск
- Создать виртуальное окружение
```shell
  virtualenv venv && soruce venv/bin/activate
 ```
- Установить зависимости
```shell
pip install -r requirements.txt
```
- При необходимости поменять файл `.env.dev`
- Эскопртировать переменные 
```shell
export $(cat .env.dev | xargs)
```
- Запустить БД
```shell
docker-compose -f docker-compose.posrgres.yml up -d
```
- Инициализировать БД
```shell
aerich init-db
```
- Запустить приложение
```shell
uvicorn main:app --reload
```

### Авторизация и пользователи
Для авторизации используется [fastapi-users](https://frankie567.github.io/fastapi-users/)

Путь с авторизацией - `src->app->users`

### База данных

Запуск базы данных PostgreQL
```shell 
docker-compose -f docker-compose.posrgres.yml up -d 
```

В качестве ORM используется Черепаха. Почему, можно прочитать тут - https://github.com/tortoise/orm-benchmarks

### Скрипты для базы данных
1. Инициализация базы данных
```shell
aerich init-db  
```
2.  Создание файла миграций 
```shell
aerich migrate --name название_миграции 
```
3. Приминение миграций
```shell
 aerich upgrade  
```