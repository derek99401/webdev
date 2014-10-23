#!/bin/bash

if [ $# -ne 1 ]; then
  echo "usage: $0 rolename"
fi
rolename=$1
roledir=roles/$rolename
mkdir -p $roledir
mkdir -p $roledir/files/
mkdir -p $roledir/templates/
mkdir -p $roledir/tasks/
mkdir -p $roledir/handlers/
mkdir -p $roledir/vars/
mkdir -p $roledir/defaults/
mkdir -p $roledir/meta/
