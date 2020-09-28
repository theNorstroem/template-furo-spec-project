# your spec project

Description of your spec project goes here.
## Prequisits
If you have Go installed, if not follow [the instructions to install GO](https://golang.org/doc/install).

`simple-generator` has to be installed. Quick installation: `go get github.com/theNorstroem/simple-generator` .

- `go get -u google.golang.org/grpc`  

you also need to install the [furo spectools](https://github.com/theNorstroem/spectools). 

- `brew install spectools`  

Install dependencies

	go get github.com/veith/protoc-gen-go-patch
	go get google.golang.org/grpc/cmd/protoc-gen-go-grpc
	go get google.golang.org/protobuf/cmd/protoc-gen-go"
	
## Quickstart
Use the template repository from https://github.com/theNorstroem/template-furo-spec-project to create a spec project for your specs.
More about using [template repositorys can be found here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template).

.spectools is the config file for spectools. you need first to run
 ```
spectools install
 ```

to install your additional dependencies like the base specs which are defined in '.spectool'.

if you want to generate specs from the tiny mu specs ([readme](muspecs/readme.md)). you can write the mu spec and put them into 'muspec' folder. 

then run
 ```
spectools muSpec2Spec
 ```
to generate the normal service and type specs. you can find these specs in 'specs' folder. 
if you have defined these command in flows in .spectools. you can run
 ```
spectools 
 ```
to execute all commands sequentially which are defined in flows. 

To edit the specs ([readme](specs/readme.md)), you can use a json editor or you can use [the api designer](http://api.designer.furo.pro/). 

run 
```
 spectools checkImports 
```
to check whether all needed types are imported. 

## build the furo data_environment.js

 run 
```spectools genEsModule
```
to build the furo data_environment.js

## more usages

 run 
```spectools -h
```
to find more usages like generate protos and docus, build grpc gateway etc. 
