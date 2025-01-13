#!/bin/bash

fil=$1

filn=$(echo $fil | sed 's/á/a/g')
filn=$(echo $filn | sed 's/é/e/g')
filn=$(echo $filn | sed 's/í/i/g')
filn=$(echo $filn | sed 's/ó/o/g')
filn=$(echo $filn | sed 's/ú/u/g')
filn=$(echo $filn | sed 's/_-/-/g')
filn=$(echo $filn | sed 's/_/-/g')

echo $filn

mv $fil $filn


