#!/usr/bin/env bash
# exit when any command fails
set -e

DOMAINTYPESPATH=github.com/theNorstroem/template-furo-spec-project/dist/pb
TARGETDIR="../../spec_out"
# enable recursion for /**/*.xxx
shopt -s globstar dotglob
WD=`pwd`

cd ./dist/proto/Messages


TMPDIR=$TARGETDIR"_tmp"
rm -rf $TMPDIR
mkdir $TMPDIR

FILES=./**/*.proto

protoc --proto_path=./ \
-I. \
-I/usr/local/include \
-I../../../dependencies/github.com/theNorstroem/furoBaseSpecs/dist/proto/Messages \
-I$GOPATH/src \
-I$GOPATH/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
--furo-specs_out=\
Mauth/auth.proto=$DOMAINTYPESPATH/auth,\
Msample/sample.proto=$DOMAINTYPESPATH/sample,\
:$TMPDIR \
$FILES

cd $WD/dist/proto/Services

FILES=./**/*.proto
protoc --proto_path=./ \
-I. \
-I../Messages \
-I/usr/local/include \
-I../../../dependencies/github.com/theNorstroem/furoBaseSpecs/dist/proto/Messages \
-I$GOPATH/src \
-I$GOPATH/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
--furo-specs_out=\
Mauth/auth.proto=$DOMAINTYPESPATH/auth,\
Msample/sample.proto=$DOMAINTYPESPATH/sample,\
:$TMPDIR \
$FILES

