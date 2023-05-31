.PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	# this ensures they run in the same shell
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: migrations
migrations:
	poetry run python -m core.manage makemigrations

.PHONY: migrate
migrate:
	poetry run python -m core.manage migrate

.PHONY: clean-migrations
clean-migrations:
	rm -f core/apps/**/migrations/0*.py
	rm -f db.sqlite3

.PHONY: update-db
update-db: clean-migrations migrations migrate

.PHONY: run-server
run-server:
	poetry run python -m core.manage runserver 0.0.0.0:8000

.PHONY: send-email
send-email:
	poetry run python -m core.manage shell < scripts/send_email.py

.PHONY: superuser
superuser:
	DJANGO_SUPERUSER_PASSWORD=admin \
	poetry run python -m core.manage \
	createsuperuser --username admin --email craigc@oosto.com --noinput

.PHONY: dev-docker-compose-up
dev-docker-compose-up:
	test -f .env || touch .env
	docker compose -f docker-compose.dev.yml up --force-recreate db

.PHONY: dev-docker-compose-down
dev-docker-compose-down:
	docker compose -f docker-compose.dev.yml down

.PHONY: prod-docker-compose-up
prod-docker-compose-up:
	test -f .env || touch .env
	docker compose -f docker-compose.yml up

.PHONY: prod-docker-compose-down
prod-docker-compose-down:
	docker compose -f docker-compose.yml down
	docker rmi -f django-boilerplate-app

.PHONY: shell
shell:
	poetry run python -m core.manage shell

.PHONY: update
update: install migrate install-pre-commit;

.PHONY: reset
reset: clean-migrations migrations migrate superuser run-server

.PHONY: test
test:
	PYTHONPATH=. poetry run pytest -v -rs -n auto --show-capture=no

.PHONY: test-verbose
test-verbose:
	PYTHONPATH=. poetry run pytest -v -s -n auto
