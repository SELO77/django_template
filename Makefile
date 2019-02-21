ci_setuptest:
		. ./citest__drop_databases.sh

ci: ci_setuptest tests-delete-migrations tests-makemigrations
		. ./citest__run.sh

collectstatic:
		python manage.py collectstatic --clear --noinput

docker-build:
		docker build -t cgex-admin:0.1 .

docker-run:
		docker run \
		--rm \
		-it \
		-p 80:80 \
		cgex-admin:0.1

docker-run-local:
		docker run \
		--rm \
		-p 8000:80 \
		--env-file ./.env \
		cgex-admin:0.1


docker-rmi:
		docker rmi cgex-admin:0.1 -f
