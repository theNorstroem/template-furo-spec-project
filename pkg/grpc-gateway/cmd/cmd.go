package main

import (
	"fmt"
	grpc_gateway "github.com/theNorstroem/template-furo-spec-project/pkg/grpc-gateway"
)

func main() {
	backendAddr := ":7777" // The grpc server addr
	exposedArr := ":8888"  // The addr of the exposed api
	fmt.Println("TRANSCODER connects to grpc backend:" + backendAddr)
	fmt.Println("TRANSCODER started on: " + exposedArr)
	grpc_gateway.Run(backendAddr, exposedArr)
}
