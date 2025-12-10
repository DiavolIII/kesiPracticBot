# Чат-бот поддержки  
**Итоговый проект по производственной практике**  
Студент: [Бангерт Данил Сергеевич]  

## Общее описание  
Веб-приложение «Чат-бот поддержки» реализует:
- Регистрацию и авторизацию пользователей
- Создание сессий чата
- Отправку сообщений и автоматические ответы бота
- Хранение истории диалога в базе данных
- Защиту эндпоинтов через JWT-токены

## Технологии  
- **Бэкенд**: Python 3.12, FastAPI, SQLAlchemy, Pydantic, JWT
- **База данных**: SQLite (через aiosqlite)
- **Фронтенд**: HTML5, CSS3, JavaScript (ES6+)
- **Инструменты**: uvicorn, virtualenv

## Установка и запуск

### 1. Подготовка окружения
Убедитесь, что установлен **Python 3.8+**.  
Откройте терминал в корне проекта и перейдите в папку `backend`:
```bash
cd backend
```

## Установка и запуск

### 1. Подготовка окружения
Убедитесь, что установлен **Python 3.8+**.  
Откройте терминал в корне проекта и перейдите в папку `backend`:
```bash
cd backend
```

2. Создание виртуального окружения
# Винда
python -m venv venv
venv\Scripts\activate

# Линух / МакОС
python3 -m venv venv
source venv/bin/activate

3. Установка зависимостей
```bash
pip install -r requirements.txt
```

Сервер запустится на:
→ http://localhost:8000
Док API (Swagger ui): 
→ http://localhost:8000/docs
# Опционально, но можете поменять хосты, они иногда бывают заняты, юзайте например 8001 и 8081
# далее создаться файл test.db 

5. (Опционально) Запуск фронтенда
в новом терминале
```bash
cd frontend
python -m http.server 8080
```

Демонстрация работы (для защиты)
# Шаг 1: Регистрация
Эндпоинт: POST /auth/register
Тело запроса:
```json
{
  "email": "test@example.com",
  "password": "shortpass123"
}
```
/ Ожидаемый ответ: 200 OK

# Шаг 2: Авторизация
Эндпоинт: POST /auth/login
Тело запроса: те же данные
Ожидаемый ответ:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

Файлы конфигурации

```env
DATABASE_URL=sqlite+aiosqlite:///./test.db
SECRET_KEY=09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```
