cmake_minimum_required(VERSION 2.8)
FIND_PACKAGE(cmakesnap)

add_subdirectory(core)
add_subdirectory(server)
add_subdirectory(snap)

PY_BINARY(
  NAME    manage
  SOURCES manage.py
)
