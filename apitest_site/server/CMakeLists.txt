cmake_minimum_required(VERSION 2.8)

PY_BINARY(
  NAME    server
  SOURCES settings.py
          urls.py
          wsgi.py
          __init__.py
)
