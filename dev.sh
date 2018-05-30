#!/bin/bash
build_app() {
  docker-compose run web django-admin.py startproject app .
}

migrate_app() {
  python manage.py migrate
}
