#!/usr/bin/env bash
# exit when any command fails
set -e

DOMAINTYPESPATH={{.config.module}}/dist/pb
TARGETDIR="../pb"
# enable recursion for /**/*.xxx
shopt -s globstar dotglob
WD=`pwd`

cd {{.config.build.proto.targetdir}}


TMPDIR=$TARGETDIR"_tmp"
rm -rf $TMPDIR
mkdir $TMPDIR

FILES=./**/*.proto

protoc --proto_path=./ \
-I./ \
-I$WD/dependencies/github.com/theNorstroem/furoBaseSpecs/dist/proto \
-I/usr/local/include \
-I$GOPATH/src/github.com/googleapis/googleapis \
-I$GOPATH/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
--go_out=\
{{$myDict := dict}}
{{- range $typename, $type := .types}}
{{- $k := print "M" $type.path "/" $type.typespec.__proto.targetfile}}
{{- $v := print "$DOMAINTYPESPATH/" $type.path ",\\"}}
{{- $_ := set $myDict $k $v}}
{{- end}}
{{- range $k,$v := $myDict}}
{{- $k}}={{$v}}
{{end -}}
:$TMPDIR \
--go-patch_out=\
{{$myDict := dict}}
{{- range $typename, $type := .types}}
{{- $k := print "M" $type.path "/" $type.typespec.__proto.targetfile}}
{{- $v := print "$DOMAINTYPESPATH/" $type.path ",\\"}}
{{- $_ := set $myDict $k $v}}
{{- end}}
{{- range $k,$v := $myDict}}
{{- $k}}={{$v}}
{{end -}}
:$TMPDIR \
--go-grpc_out=\
{{$myDict := dict}}
{{- range $typename, $type := .types}}
{{- $k := print "M" $type.path "/" $type.typespec.__proto.targetfile}}
{{- $v := print "$DOMAINTYPESPATH/" $type.path ",\\"}}
{{- $_ := set $myDict $k $v}}
{{- end}}
{{- range $k,$v := $myDict}}
{{- $k}}={{$v}}
{{end -}}
:$TMPDIR $FILES

cd $TMPDIR/{{.config.module}}

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

cd $WD/{{.config.build.proto.targetdir}}
pwd
rm -rf $TMPDIR

