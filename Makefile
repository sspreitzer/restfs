DIR?=src
APP?=wsgi:app

run: env bower_components
	. env/bin/activate; gunicorn -c gunicorn.conf --chdir $(DIR) $(APP)

debug: env bower_components
	. env/bin/activate; cd src; python debug.py

env:
	virtualenv env
	. env/bin/activate; pip install --upgrade pip
	. env/bin/activate; pip install -r requirements.txt

bower_components:
	bower install

clean:
	rm -rf env/ bower_components/
