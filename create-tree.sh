#!/bin/bash

cd web

for dir in public uploads etc
  do
  mkdir $dir
  if [ $dir = public ]; then
    cd public
    for subdir in img css js
      do
      mkdir $subdir
      done
    cd ..
  fi
done
