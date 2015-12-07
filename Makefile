DIR?=src
APP?=wsgi:app

run: env
	. env/bin/activate; gunicorn -c gunicorn.conf --chdir $(DIR) $(APP)

debug: env
	. env/bin/activate; cd src; python debug.py

env:
	virtualenv env
	. env/bin/activate; pip install --upgrade pip
	. env/bin/activate; pip install -r requirements.txt

clean:
	rm -rf env/
