#!/usr/bin/env bash
# exit when any command fails
set -e

DOMAINTYPESPATH=github.com/theNorstroem/template-furo-spec-project/dist/pb
TARGETDIR="../pb"
# enable recursion for /**/*.xxx
shopt -s globstar dotglob
WD=`pwd`

cd ./dist/proto/


TMPDIR=$TARGETDIR"_tmp"
rm -rf $TMPDIR
mkdir $TMPDIR

FILES=./**/*.proto

protoc --proto_path=./ \
-I./ \
-I../../dependencies/github.com/theNorstroem/furoBaseSpecs/dist/proto/Messages \
-I$GOPATH/src/github.com/googleapis/googleapis \
-I/usr/local/include \
-I$GOPATH/src \
-I$GOPATH/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
--go_out=\
:$TMPDIR \
--go-patch_out=\
:$TMPDIR \
--go-grpc_out=\
:$TMPDIR \
$FILES

cd $TMPDIR/github.com/theNorstroem/template-furo-spec-project

FILES=**/*.go


for f in $FILES
do
dir=$(dirname -- "$WD/$f")
echo $f
mkdir -p $dir
file=$WD/$f
[ -f $file ] && rm $file
mv $f $WD/$f
done

cd $WD/./dist/proto/
pwd
rm -rf $TMPDIR

