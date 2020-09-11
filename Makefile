fun:
	@. ./venv/bin/activate && \
		python ./main.py

prepare:
	virtualenv -p python3 venv
