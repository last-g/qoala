#!/bin/bash


FILE=${BASH_SOURCE[0]}
CURRENT=`dirname -- "${FILE}"`
PROJECT=`readlink -fn -- "${CURRENT}/../"`
