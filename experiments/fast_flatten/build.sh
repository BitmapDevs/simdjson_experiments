#!/bin/bash
SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
cd $SCRIPTPATH/../../library/simdjson
make -k parse
mv parse fastparse
make -k parse EXTRAFLAGS=-DSIMDJSON_NAIVE_FLATTEN
mv parse slowparse
