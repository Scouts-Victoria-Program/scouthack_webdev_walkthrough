#!/usr/bin/env bash

blocks=(header content footer)
file=index.html

for block in "${blocks[@]}"
do
    for end in block endblock
    do
        grep -E "(<!--x|{%)[[:space:]]*${end}[[:space:]]+${block}[[:space:]]*(x-->|%})" "$file" -q ||
            echo "$file: Missing $end $block"
    done
done
