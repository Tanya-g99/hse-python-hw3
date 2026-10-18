# Домашняя работа №3

Приложение на FastAPI принимает числа и задержки, асинхронно считает квадрат каждого числа и возвращает время выполнения.

## Установка

Создайте виртуальное окружение и установите зависимости из `requirements.txt`:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Запуск

```bash
uv run fastapi dev
```

Сервер будет доступен на http://127.0.0.1:8000.  

## Проверка

```bash
curl -X POST http://127.0.0.1:8000/calculate/ \
  -H "Content-Type: application/json" \
  -d '{"numbers": [5, 3, 10], "delays": [1, 2, 0.5]}'
```
