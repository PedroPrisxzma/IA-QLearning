#!/bin/bash
INPUT=$1
ALPHA=$2
EPSILON=$3
LAMBDA=$4
N=$5

python3 main.py ${INPUT} ${ALPHA} ${EPSILON} ${LAMBDA} ${N} > pi.txt
