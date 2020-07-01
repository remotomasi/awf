#!/bin/bash

wget "https://www.ilmeteo.it/portale/archivio-meteo/Lecce/2020/Giugno?format=csv"  2>/dev/null -O - > data.csv
cat data.csv | cut -d';' -f3,6,7,9 | tail -n 30 | tr ';' ',' | sed 's/"//g' > data_fin.csv
