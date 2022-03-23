#!/bin/bash

RUNPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"


python3 $PWD/scripts/resize.py $RUNPATH dim=5000,3000