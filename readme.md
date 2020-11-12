# your spec project

Description of your spec project goes here.

## Specification

The aim of the specification is to provide minimal behavior that the consumer can rely on. 
The specs can be regarded as the contracts between client and server for the [REST](https://de.wikipedia.org/wiki/Representational_State_Transfer) API. 
You can visite [furo.pro](furo.pro) to get more information about the specs.
## Prequisits
If you have Go installed, if not follow [the instructions to install GO](https://golang.org/doc/install).

`simple-generator` has to be installed. Quick installation: `go get github.com/theNorstroem/simple-generator` .

[gRPC](https://grpc.io/docs/languages/go/basics/) is also needed to be installed.
- `go get -u google.golang.org/grpc`  

you also need to install the [furo spectools](https://github.com/theNorstroem/spectools). 

- `brew tap theNorstroem/tap`  
- `brew install spectools`  

Install dependencies

	go get github.com/veith/protoc-gen-go-patch
	go get google.golang.org/grpc/cmd/protoc-gen-go-grpc
	go get google.golang.org/protobuf/cmd/protoc-gen-go"
	
## Quickstart
Use the template repository from https://github.com/theNorstroem/template-furo-spec-project to create a spec project for your specs.
More about using [template repositorys can be found here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template).

#### configure spectools
`.spectools` is the config file for spectools. you can configure parameters and initial settings of you spec project.
just like your module name. here in template it is 'github.com/theNorstroem/template-furo-spec-project'. 

#### write you specs
write you spec in you spec folder which is defined in spectools config.
there are some sample [specs](samples/specs/readme.md) under 'samples/specs'.
you can use the json/yml editor or  [the api designer](http://api.designer.furo.pro/) to edit your specs. 

#### install dependencies
run `
spectools install` to install your additional dependencies like the furo base specs which are defined in `.spectool`.

#### imports check
run `
 spectools checkImports `
to check whether all needed types are imported. 

#### build the furo data_environment.js

 run `spectools genEsModule`
to build the furo data environment js file. this env.js file can be used in client as 
the contract that the server also follows. 

#### generate proto files

 run 
 
 ```
 spectools genMessageProtos 
 spectools genServiceProtos 
```
to build the protobuf files which can be used to generate swagger Docus and gRPC gateway. 

#### generate gRPC gateway

The [gRPC-gateway](https://github.com/grpc-ecosystem/grpc-gateway) is a plugin of the Google protocol buffers compiler protoc. It reads protobuf service definitions and generates a reverse-proxy server which translates a RESTful HTTP API into gRPC. This server is generated according to the google.api.http annotations in your service definitions.
 
 use 
 
 ```
 spectools gen_transcoder 
```
to build the [gRPC-gateway](https://github.com/grpc-ecosystem/grpc-gateway). 

you can run the generated grpc-gateway by using `go run dist/grpc-gateway/cmd/cmd.go`

#### spectools flows
if you have defined the spectools command-flows in spectools config. you can run
`spectools`
to execute all commands sequentially which are defined in the flows. 

#### more usages of spectools

 run 
 
```
spectools -h
```

to find more usages. 

## read more and useful links
- [API designer](http://api.designer.furo.pro/)
- [furo.pro](furo.pro) 
- [google protobuf 3](https://developers.google.com/protocol-buffers/docs/proto3)
- [gRPC](https://grpc.io/docs/languages/go/basics/)
- [gRPC-gateway](https://github.com/grpc-ecosystem/grpc-gateway)
- [REST](https://de.wikipedia.org/wiki/Representational_State_Transfer)
