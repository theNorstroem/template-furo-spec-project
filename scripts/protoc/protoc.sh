#!/bin/bash

TARGETDIR=scripts
mkdir -p $TARGETDIR

go build -i -o bin/protoc-gen-go-grpc google.golang.org/grpc/cmd/protoc-gen-go-grpc/.

# the gateway
spectools exportAsYaml -f | simple-generator -t scripts/protoc/proto2DomainServices.tpl > $TARGETDIR/proto2DomainServices.sh

spectools exportAsYaml -f | simple-generator -t scripts/protoc/proto2DomainTypes.tpl > $TARGETDIR/proto2DomainTypes.sh
chmod 755 $TARGETDIR/proto2DomainServices.sh

chmod 755 $TARGETDIR/proto2DomainTypes.sh
