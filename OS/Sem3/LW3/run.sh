#!/bin/bash

# Проверка количества аргументов
if [ "$#" -ne 2 ]; then
    echo "Использование: $0 <время работы в секундах> <количество экземпляров>"
    exit 1
fi

# Получение аргументов
sleepTime=$1
numInstances=$2

# Запуск указанного количества экземпляров программы
for ((i=1; i<=numInstances; i++))
do
    ./program $sleepTime &
done