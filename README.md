# ya_disk_list

Просто тулза позволяет выгрузить список картинок из яндекс диска.
И да получить доступ к файлам типа Архив, фото - не получится.
Если найдете способ получить доступ - напишите мне .

## Авторизация

Для того чтоб войти в яндекс надо зарегистрировать тут свое приложение
https://oauth.yandex.com/client/new и client_id от него записать в
YANDEX_CLIENT_ID которая находится в .env

## Состав
* list.py - загрузчик списка картинок из яндекс диска в файл
* download.py - выгрузка картинок на локальный диск из яндекс диска
* explore.py - Получить метаинформацию яндекс диск

## list.py
Настраивается через переменные среды. См. пункт "настройка"

## download.py
Параметры
* filename - файл со списком картинок в яндекс диске
* offset - смешение относительно начала файла
* limit - сколько выгружать
* to_dir - директория для сохранения

Пример использования:
```
 ./download.py --filename=1.csv --offset=0 --limit=100 --to_dir=0_100
```

## Настройка

Настройка производиться через файл ```.env```. В качестве примера смотри .env-example

### Параметра настройки

* YANDEX_CLIENT_ID - client_id полученный от яндекса см. пункт Авторизация
* DEVICE_ID - Uuid, id устройства. Может быть любым
* DEVICE_NAME - Название устройства. Может быть любым
* ITEMS_LIMIT - Сколько элементов получать за раз. 100 по умолчанию
* OUTPUT_CSV_FILENAME - Куда сохранять данные в виде csv. 1.csv по умолчанию
* YA_DISK_ROOT - В какой папке искать картинки ."disk:/" по умолчанию.

## Формат результирующего csv

Кодировка utf-8 , разделитель ";" , перенос строки "\n"
Столбцы

* path - путь в яндекс диске
* name - имя
* size - размер в байтах
* sha256 - контрольная сумма в sha256
