#!/bin/bash

for file in $(find . -type f | grep [^X].gv$ | sort); do
  basename="${file##*/}"
  basename="${basename%.gv}"
  echo [+] $basename
  dot -Tpng $basename.gv -o $basename.png
done

