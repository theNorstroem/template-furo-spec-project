# your spec project

Description of your spec project goes here.
## Prequisits
If you have Go installed, if not follow [the instructions to install GO](https://golang.org/doc/install).

`simple-generator` has to be installed. Quick installation: `go get github.com/theNorstroem/simple-generator` .




- `go get -u google.golang.org/grpc`  

### GRPC Gateway Installation
More about  [grpc-gateway](https://grpc-ecosystem.github.io/grpc-gateway/docs/usage.html), gRPC to JSON proxy generator 
following the gRPC HTTP spec.


First you need to install ProtocolBuffers 3.0.0-beta-3 or later.
```shell script

mkdir tmp
cd tmp
git clone https://github.com/google/protobuf
cd protobuf
./autogen.sh
./configure
make
make check
sudo make install
```

Then, go get -u as usual the following packages:
````shell script
go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway
go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger
go get -u github.com/golang/protobuf/protoc-gen-go

````

## Quickstart
Use the template repository from https://github.com/theNorstroem/template-furo-spec-project to create a spec project for your specs.
More about using [template repositorys can be found here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template).

run `npm install` to install the tools.
 
Install your additional spec types and register them in the furo.spec.conf.json.

To edit the specs, you can use a json editor or you can use [the api designer](http://api.designer.furo.pro/). 


## Usage of spec builder

To quickly add types and services for a package, just add them in the packages section of the conf. 

Then run 
```shell script
npm init
```
to generate a initial structure for a spec. 
This consists of the *minimal type*, a *minimal service definition*, a *default entity spec*
and a *default collection spec*    

To build the furo data_environment.js, the swagger docs, the golang files for the grpc-gateway and the java interfaces run.

```shell script
npm build
```
