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
	rm -f core/**/migrations/0*.py
	rm -f db.sqlite3

.PHONY: update-db
update-db: clean-migrations migrations migrate

.PHONY: run-server
run-server:
	poetry run python -m core.manage runserver

.PHONY: superuser
superuser:
	DJANGO_SUPERUSER_PASSWORD=admin \
	poetry run python -m core.manage \
	createsuperuser --username admin --email admin@test.com --noinput

.PHONY: update
update: install migrate install-pre-commit;
