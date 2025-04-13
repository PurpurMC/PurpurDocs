#!/bin/bash

if [[ -z $1 ]]
then
    read -p 'Press enter to skip selecting commits, otherwise type "(c)ommit": ' first
    if [[ $first = 'c' ]]
    then
        while [[ -z $firstCommit ]]
        do
            read -p 'Enter the first commit: ' firstCommit
        done
        read -p 'Enter the second commit or leave blank to compare against latest commit: ' secondCommit

        python3 base.py $firstCommit $secondCommit
    else
        python3 base.py
    fi
else
    if [[ $1 = '--no-commits' ]] || [[ $1 = '-nc' ]]
    then
        python3 base.py
    else
        python3 base.py $1 $2
    fi
fi