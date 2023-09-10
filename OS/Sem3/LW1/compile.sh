#! /bin/bash

if gcc $1 -o $2; then
    echo "Compiled, running"
    ./$2
else
    echo "Compile error"
fi