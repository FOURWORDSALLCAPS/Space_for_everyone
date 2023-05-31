# Telegram-бот для публикации фотографий

Данный код представляет собой Telegram-бота, который регулярно публикует фотографии в указанный чат. 

## Установка зависимостей

Запускаем CMD (можно через Win+R, дальше вводим cmd) и вписываем команду cd /D <путь к папке со скриптами>


```pip install -r requirements.txt```

## Подготовка к запуску
Для запуска бота необходимо:
1. Создать файл .env в корневом каталоге со скриптами
2. Получить токен Telegram-бота, создать бота через BotFather в Telegram, получить токен и указать его в качестве переменной окружения `TELEGRAM_TOKEN`. Например: `TELEGRAM_TOKEN=3253423236:SSDDSfghhft54gdf`
3. Подготовить директорию с фотографиями для публикации.
4. Получить идентификатор чата, куда необходимо опубликовывать фотографии, и указать его в качестве переменной окружения `TG_CHAT_ID`. Например: `TG_CHAT_ID=@My_chat`
5. Получить токен от Api Nasa, и указать его в качестве переменной окружения `NASA_TOKEN`. Например: `NASA_TOKEN=Lafsdfrgg1241125d`

## Запуск бота
Запуск бота осуществляется командой:

```python space_for_everyone_bot.py --dir <директория>```

где `<директория>` - путь к директории с фотографиями для публикации.

По умолчанию бот будет публиковать случайную фотографию из указанной директории каждый час. 

Дополнительные параметры запуска:
- `--interval` - интервал в секундах между публикацией фотографий (по умолчанию 3600 секунд, т.е. час).
- `--photo` - путь к конкретной фотографии для публикации. Если указан этот параметр, то будет опубликована только указанная фотография, игнорируя другие параметры.

```python space_for_everyone_bot.py --dir <директория> --interval 1800 --photo <путь_к_фото>```

## Сценарий скачивания фото
Для использования скриптов нужно, чтобы был получен API-ключ для работы с NASA API, и написать его в `.env` файле, используя ключевое слово `API_KEY`. Например: `API_KEY=Lsdrgvbd1252`
    
1. fetch_astronomy_picture_day.py - для скачивания астрономических картинок дня
2. fetch_earth_polychromatic_imaging.py - для скачивания полихроматического изображения Земли
3. fetch_spacex_images.py - для скачивания фотографий запуска SapceX
4. Примеры аргументов:
   - `python fetch_astronomy_picture_day.py -c <количество картинок>`
   - - По умолчанию используется количество картинок `2`.
   - `python fetch_earth_polychromatic_imaging.py -d <дату формата YYYY/MM/DD>'` 
   - - По умолчанию используется дата `2023/05/29`.
   - `python fetch_spacex_images.py -i <id запуска>` 
   - - По умолчанию используется id `5eb87d47ffd86e000604b38a`.
5. При первом запуске будет создан каталог images и туда помещены счаченный картинки.

## Остановка бота
Чтобы остановить работу бота, нужно просто прервать выполнение скрипта (нажать `Ctrl+C`)

## Версия Python: 
Я использовал Python `3.8.3`, но он должен работать на любой более новой версии.

## Цель проекта:
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

## Автор
(2023) Zaitsev Vladimir