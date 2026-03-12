# Todo App API

Backend API для TODO-приложения.
API предназначено для обучения фронтенда на **React** и реализовано на **FastAPI**.

Проект поддерживает базовые операции с задачами:

* создание задачи
* просмотр списка задач
* обновление задачи
* удаление задачи

База данных — SQLite через **SQLAlchemy** (async).

---

# Технологии

* Python 3.10+
* FastAPI
* SQLAlchemy (async)
* SQLite
* aiosqlite

---

# Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone <repo_url>
cd todo-backend
```

### 2. Установить зависимости

```bash
pip install -r requirements.txt
```

### 3. Создать базу данных

Запустить эндпоинт:

```
POST /setup_database
```

Он создаст таблицы в базе `todoapp.db`.

---

### 4. Запустить сервер

```bash
uvicorn main:app --reload
```

API будет доступно по адресу:

```
http://localhost:8000
```

Документация API:

```
http://localhost:8000/docs
```

---

# Структура проекта

```
project
│
├── main.py
├── models
│   ├── base.py
│   └── task.py
│
├── schemas
│   └── task.py
```

---

# Модель задачи

```
Task
```

| поле | тип    | описание      |
| ---- | ------ | ------------- |
| id   | int    | идентификатор |
| text | string | текст задачи  |

---

# API эндпоинты

## Получить список задач

```
GET /
```

Ответ:

```json
[
  {
    "id": 1,
    "text": "Learn React"
  }
]
```

---

## Создать задачу

```
POST /tasks
```

Body:

```json
{
  "text": "Learn React"
}
```

Ответ:

```json
{
  "success": true,
  "message": "Книга успешно добавлена"
}
```

---

## Обновить задачу

```
PUT /tasks
```

Параметры:

```
task_id (query)
```

Body:

```json
{
  "text": "Learn React better"
}
```

---

## Удалить задачу

```
DELETE /{task_id}
```

Ответ:

```json
{
  "success": true
}
```

---

# Назначение проекта

Проект используется как тренировочный backend для фронтенд-разработки:

* работа с REST API
* CRUD операции
* взаимодействие React с сервером
* практика full-stack разработки
