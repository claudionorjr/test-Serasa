installvirtualenv:
	sudo apt install virtualenv

ambvir:
	virtualenv .ambvir --python=python3.7

start:
	source .ambvir/bin/activate

install:
	pip install -r requirements/base.txt

run:
	python app.py

test:
	pytest -v

help:
	@printf "_______________________________________________________________________________________\n\n"
	@printf "'installvirtualenv' serve para instalar o virtualenv. \n"
	@printf "'ambvir' serve para criar um ambiente virtual. \n"
	@printf "'start' serve para iniciar seu ambiente virtual. \n"
	@printf "'install' serve para instalar todas as dependências necessárias. \n"
	@printf "'run' executa o arquivo principal.\n"
	@printf "'test' executa os testes unitários.\n"
	@printf "_______________________________________________________________________________________\n\n"