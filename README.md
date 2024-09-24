# Diploma project: 
### Development of software for automatic document generation and electronic document management


## Description

An in-depth paragraph about your project and overview of use.

## Getting Started

### Description

Данное программное обеспечение востребована организациям и людям, у которых есть потребность быстро и легко сформировать документ, и с помощью интеграции систем отправить документ на согласование двум и более сторонам.

При ручном процессе формировании документов требует в среднем от 10 минут до 30 минут в зависимости от пакета материалов. Бумаг для заполнения данных в организации может быть много, вероятность устаревших экземпляров, требующие рефакторинга, очень высокая.  Также документы требуют регулярной проверки на соответствие законам, так как они могут изменяться и добавляться. К документам могут добавляться новые формулировки при изменениях бизнес-процессах в организации.

Таким образом, в силу своей актуальности, цeлью выпускной квалификационной работы былa разработка системы формирования документа и электронного документооборота. Приложение способно с помощью загрузки шаблонов и генерации документов перевести эти операции на электронный вид с целью автоматизации процесса создания, редактирования, хранения, пoиска, удаления и рассылки документов.

Для разработки базы данных была выбрана **СУБД PostgreSQL**. Для разработки серверной части будет выбран фреймворк **Django**, а для клиентской части выбран язык гипертекстовой разметки **HTML**. Для того, чтобы приложение осуществляло задуманные функциональные возможности, понадобится использовать библиотеки **DocxTpl** и **Aspose-words** для взаимодействия с документами и данными, **Numtostr-rus** для преобразования числа в текст, библиотеку **Petrovich** для изменения склонений ФИО пользователей и **DaData** для подсказок адреса и ФИО.




### Dependencies

* Langauge: Python
* Framework: Django
* Database: PostgreSQL
* Additional: Docker, Grafana, Prometheus
* Libraries: 
    * anyio 4.3.0
    * appscript 1.2.5
    * asgiref 3.7.2
    * aspose-words 24.5.0
    * async-timeout 4.0.3
    * Babel 2.14.0
    * beartype 0.18.5
    * certifi 2024.2.2
    * chardet 5.2.0
    * charset-normalizer 3.3.2
    * dadata 21.10.1
    * datetime-truncate 1.1.1
    * Django 5.0.3
    * django-admin-charts 1.3.1
    * django-admin-tools 0.9.3
    * django-bower 5.2.0
    * django-debug-toolbar 4.3.0
    * django-jsonfield 1.4.1
    * django-memoize 2.3.1
    * django-multiselectfield 0.1.12
    * django-nvd3 0.10.1
    * django-prometheus 2.3.1
    * django-qsstats-magic 1.1.0
    * django-redis 5.4.0
    * django-widget-tweaks 1.5.0
    * djcacheutils 3.0.0
    * docx2pdf 0.1.8
    * docxcompose 1.4.0
    * docxtpl 0.17.0
    * h11 0.14.0
    * httpcore 1.0.5
    * httpx 0.27.0
    * idna 3.7
    * Jinja2 3.1.3
    * lxml 5.2.1
    * markdown-it-py 3.0.0
    * MarkupSafe 2.1.5
    * mdurl 0.1.2
    * numtostr-rus 1.0.1
    * pillow 10.3.0
    * pip 24.0
    * plum-dispatch 2.3.6
    * prometheus_client 0.20.0
    * psycopg2 2.9.9
    * PyDocX 0.9.10
    * Pygments 2.18.0
    * pymemcache 4.0.0
    * python-dateutil 2.9.0.post0
    * python-docx 1.1.2
    * python-dotenv 1.0.1
    * python-memcached 1.62
    * python-nvd3 0.16.0
    * python-slugify 8.0.4
    * redis 5.0.4
    * reportlab 4.2.0
    * requests 2.31.0
    * rich 13.7.1
    * setuptools 65.5.1
    * six 1.16.0
    * sniffio 1.3.1
    * sqlparse 0.4.4
    *  text-unidecode 1.3
    *  tqdm 4.66.2
    *  typing_extensions 4.11.0
    *  urllib3 2.2.1
    *  wheel 0.38.4
* macOS Monterey

### Installing

* git clone project
```
git clone https://github.com/morebeautifulthandoriangray/diploma.git
```
* open project in Pycharm
* install all libraries to your project

### Executing program

There are two steps to run the program:

* Press Run buttin in IDE
* Run the next command
```
python manage.py runserver 8000
```


Also you have to run docker-compose.yml for charts:
```
docker compose up -d
```


## Authors

Contributors names and contact info

student: [Ezhova Kate](https://t.me/Alastuer)  
diploma supervisor: [Akutin Artem]()

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the [YURI GAGARIN SSTU](https://www.sstu.ru/) License
