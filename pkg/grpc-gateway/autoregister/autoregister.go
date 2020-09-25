package autoregister

import (
	"context"
	"github.com/grpc-ecosystem/grpc-gateway/v2/runtime"
	//Services.sampleservice.Sample
	sampleservicepb "github.com/theNorstroem/template-furo-spec-project/dist/pb/Services/sampleservice"

	"google.golang.org/grpc"
)

func RegisterAllEndpoints(grpcBackendAddr string, ctx context.Context, mux *runtime.ServeMux, opts []grpc.DialOption) error {
	var err error
	// Services.sampleservice.Sample
	err = sampleservicepb.RegisterSampleHandlerFromEndpoint(ctx, mux, grpcBackendAddr, opts)
	if err != nil {
		return err
	}

	return err
}
