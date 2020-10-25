#!/bin/bash
ALGORITHM=$1
INPUT=$2

if [ "$ALGORITHM" = "-bfs" ] || [ "$ALGORITHM" = "-dfs" ] || 
    [ "$ALGORITHM" = "-ids" ] || [ "$ALGORITHM" = "-astar" ] 
then
    #echo python3 main.py "${ALGORITHM//-}" "${INPUT//-}"
    python3 main.py "${ALGORITHM#?}" "${INPUT#?}"
else
    echo Command must be ./busca.sh -algoritmo -entrada
    echo Possible -algoritmo are -bfs, -dfs, -ids or -astar
    echo -entrada must be a .txt indicating a maze, as specified
fi