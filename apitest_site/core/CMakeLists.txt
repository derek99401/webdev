cmake_minimum_required(VERSION 2.8)

PY_LIBRARY(
  NAME    core
  SOURCES admin.py
          models.py
          tests.py
          urls.py
          views.py
)
