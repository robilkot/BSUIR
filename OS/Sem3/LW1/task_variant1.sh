#! /bin/bash

find $3 -size +$1 -size -$2 | tee task_variant1_output.txt