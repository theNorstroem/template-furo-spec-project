#!/usr/bin/env bash
TARGETDIR="../pb/"

# enable recursion for /**/*.xxx
shopt -s globstar dotglob

cd dist/proto


# clear
rm -rf $TARGETDIR
mkdir $TARGETDIR


FILES=./**/*.proto

protoc --proto_path=./ \
-I. \
-I/usr/local/include \
-I$GOPATH/src \
-I$GOPATH/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
--go_out=\
:$TARGETDIR $FILES

# move the files
cd $TARGETDIR
mv github.com/theNorstroem/FuroBaseSpecs/dist/pb/furo furo
rm -rf github.com
rm -rf google.golang.org