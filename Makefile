 install: venv
	. venv/bin/activate; pip install --upgrade pip && pip install -r requirements.txt

 venv:
	python3 -m venv venv

 clean:
	rm -rf venv
	find . -name '*.pyc' -delete