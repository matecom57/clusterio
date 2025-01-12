#!/bin/bash

fil=$1

filn=$(echo $fil | sed 's/_-/-/g')

filn=$(echo $filn | sed 's/_/-/g')

filn=$(echo $filn | sed 's/ó/o/g')

echo $filn

mv $fil $filn


