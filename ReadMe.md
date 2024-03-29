
# House Price Prediction API

## Описание проекта
Этот проект представляет собой API для прогнозирования цен на жилье. Модель была обучена с использованием Lasso регрессии на данных из соревнования Kaggle House Prices Prediction. API разработано с использованием FastAPI и позволяет клиентам отправлять данные о недвижимости и получать предсказанные цены.

## Установка и запуск

### Требования
Для работы с проектом вам понадобятся следующие инструменты:
- Python 3.6+
- pip (Python package installer)

### Установка зависимостей
Перед запуском API убедитесь, что все необходимые библиотеки установлены. Вы можете установить их, используя команду:
```bash
pip install -r requirements.txt
```

### Запуск API
Для запуска сервера выполните следующую команду:
```bash
uvicorn main:app --reload
```
API будет доступно по адресу `http://127.0.0.1:8000`.

## Использование API

### Отправка запроса на прогноз
Чтобы получить прогноз цены на жилье, отправьте POST-запрос на `/predict` с JSON, содержащим характеристики дома. Пример запроса:

```json
{
    "area": 2000,
    "bedrooms": 4,
    "bathrooms": 2,
    "stories": 2,
    "mainroad": 1,
    "guestroom": 0,
    "basement": 1,
    "hotwaterheating": 0,
    "airconditioning": 1,
    "parking": 2,
    "prefarea": 1,
    "furnished": 1,
    "semi_furnished": 0,
    "unfurnished": 0
}
```

Ответ будет содержать предсказанную цену.

## Структура проекта

- `main.py`: Главный файл, содержащий определения FastAPI и конечные точки.
- `model/`: Папка, содержащая сериализованную модель Lasso регрессии.

## Лицензия
Укажите информацию о лицензии здесь (если применимо).
