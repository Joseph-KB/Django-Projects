virtualenv venv
source venv/bin/activate    linux
venv/bin/activate   windows
pip install -r requiremtns.txt

django-adim startproject freelance_arch
python manage.py runserver localhost:8000
python manage.py startapp home
python manage.py startapp customer
python manage.py startapp staff


create urls.py
include app/urls.py in main project folder urls.py file

create a view function in app/view.py

create a template folder

postgresql
    .my_pgpass
        localhost:5432:freelancerdb:josephpg:kalipikali
    .pg_service.conf
    [my_service]
        host=localhost
        user=josephpg
        dbname=freelancerdb
        port=5432

secret key django-insecure-n34uag5y)nqt5f7q!f154of&=@!29x!trstlznduq5hqp@yqzy
