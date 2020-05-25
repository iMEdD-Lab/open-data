#!/bin/bash

echo $USER

echo $SECONDS

cp $1 $2

rm $1

ls $2

dire="~/Desktop"
echo $dire
echo
ls $dire/mathesis
echo
myvar=$( ls /etc | wc -l )

export myvar
export dire
# chmod 755 ./Desktop/test1.sh
./Desktop/test1.sh

./dead.py

