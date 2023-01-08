# Финальный проект спринта: асинхронный парсер PEP


## Запуск проекта

* клонировать проект на компьютер `git clone https://github.com/foxygen-d/scrapy_parser_pep.git`
* создание виртуального окружения `python3 -m venv venv`
* запуск виртуального окружения `source venv/bin/activate`
* запуск команды на старт проекта `scrapy startproject pep_parse .`
* создание паука `scrapy genspider pep peps.python.org`
* запуск паука `scrapy crawl pep`
* запуск тестов `pytest`


## Задача

### Парсер должен выводить собранную информацию в два файла .csv:
1. В первый файл нужно вывести список всех PEP: номер, название и статус.
2. Второй файл должен содержать сводку по статусам PEP — сколько найдено документов в каждом статусе (статус, количество). В последней строке этого файла в колонке «Статус» должно стоять слово Total, а в колонке «Количество» — общее количество всех документов.


### Требования к парсеру:
1. В качестве стартовой ссылки установите https://peps.python.org/. Метод паука `parse()` должен собирать ссылки на документы PEP. Метод `parse_pep()` должен парсить страницы с документами и формировать Items.
2. При парсинге применяйте CSS- или XPath-селекторы.
3. В парсере должны применяться объекты Items. Для создания Items опишите класс `PepParseItem(scrapy.Item)`, у него должно быть три атрибута: 
    * number (номер PEP),
    * name (название PEP),
    * status (статус, указанный на странице PEP)
4. Парсер должен сохранять данные в файлы .csv в директорию results/, она должна находиться в корне проекта, на одном уровне с pep_parse/ и tests/.
    * **Файлы со списком PEP** должны быть именованы по маске `pep_ДатаВремя.csv`, например — `pep_2029-01-31T23-55-00.csv`. В файле должно быть три столбца: «Номер», «Название» и «Статус». Сохранение должно выполняться посредством Feeds, настройки опишите в settings.py.
    * **Файлы со сводкой по статусам** должны быть именованы по маске `status_summary_ДатаВремя.csv`, например — `status_summary_2029-01-31_23-55-00.csv`. Этот файл не удастся сформировать через Feeds, ведь такие данные нельзя получить из отдельных Items. Создавать этот файл нужно через Pipeline.
    
    В файле должно быть два столбца: «Статус» и «Количество». Для создания этого файла опишите pipeline, который суммирует количество документов PEP в разных статусах и по окончании парсинга формирует файл .csv.
    
    Дополнительно в pipeline посчитайте общее количество документов PEP, в последней строке со сводкой в столбце «Статус» напишите “Total”, а в столбце «Количество» выведите общее количество полученных документов PEP.
    
    Вывод данных можно сделать либо через метод стандартной библиотеки `csv.writer()` — в этом поможет документация, либо через класс `csv.DictWriter()` (вот документация), либо через запись строк в файл — сначала заголовок, потом статусы и их количество, потом Total и количество:

    ```
    with open(filename, mode='w', encoding='utf-8') as f:
        # Записываем строки в csv-файл. Колонки разделяются запятой, без пробелов.
        f.write('Статус,Количество\n')
        # Здесь цикл с записью данных в файл.
        f.write(f'Total,{total}\n')
    ```


## Автор
Домнина Анастасия

Студент факультета Бэкенд, Когорта №10+
