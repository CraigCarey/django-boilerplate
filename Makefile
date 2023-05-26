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
	poetry run python -m core.manage runserver

.PHONY: send-email
send-email:
	poetry run python -m core.manage shell < scripts/send_email.py

.PHONY: test
test:
	poetry run python -m core.manage test

.PHONY: superuser
superuser:
	DJANGO_SUPERUSER_PASSWORD=admin \
	poetry run python -m core.manage \
	createsuperuser --username admin --email craigc@oosto.com --noinput

.PHONY: update
update: install migrate install-pre-commit;

.PHONY: reset
reset: clean-migrations migrations migrate superuser run-server
