name: Sample
version: ""
description: Add xxxsome text here.
lifecycle: null
__proto:
    package: Services.sampleservice
    targetfile: sample.proto
    imports:
        - google/api/annotations.proto
        - Services/sampleservice/reqmsgs.proto
        - google/protobuf/empty.proto
        - sample/sample.proto
    options:
        go_package: github.com/theNorstroem/template-furo-spec-project/dist/pb/Services/sampleservice;sampleservicepb
        java_multiple_files: "true"
        java_outer_classname: SampleProto
        java_package: com.Services.sampleservice
services:
    List:
        description: List samples with pagination.
        data:
            request: google.protobuf.Empty
            response: sample.SampleCollection
            bodyfield: body
        deeplink:
            description: 'List: GET /samples google.protobuf.Empty , sample.SampleCollection #List samples with pagination.'
            href: /samples
            method: GET
            rel: list
        query:
            q:
                constraints: {}
                description: query string.
                meta: null
                type: string
            page:
                constraints: {}
                description: Use this field to specify page to display.
                meta: null
                type: string
            filter:
                constraints: {}
                description: Use this field to specify page to display.
                meta: null
                type: string
            order_by:
                constraints: {}
                description: Use this field to specify page to display.
                meta: null
                type: string
        rpcname: ListSample
    Get:
        description: Returns a single sample.
        data:
            request: google.protobuf.Empty
            response: sample.SampleEntity
            bodyfield: body
        deeplink:
            description: 'Get: GET /samples/{xxx} google.protobuf.Empty , sample.SampleEntity #Returns a single sample.'
            href: /samples/{xxx}
            method: GET
            rel: get
        query:
            xxx:
                constraints: {}
                description: The query param xxx stands for XXX id.
                meta: null
                type: string
            ddd:
                constraints: {}
                description: The query param ddd stands for XXX id.
                meta: null
                type: string
        rpcname: GetSample
    Create:
        description: Use this to create new samples.
        data:
            request: sample.Sample
            response: sample.SampleEntity
            bodyfield: body
        deeplink:
            description: 'Create: POST /samples sample.Sample , sample.SampleEntity #Use this to create new samples.'
            href: /samples
            method: POST
            rel: create
        query: {}
        rpcname: CreateSample
    Update:
        description: Use this to update existing samples.
        data:
            request: sample.Sample
            response: sample.SampleEntity
            bodyfield: body
        deeplink:
            description: 'Update: PATCH /samples/{xxx} sample.Sample , sample.SampleEntity #Use this to update existing samples.'
            href: /samples/{xxx}
            method: PATCH
            rel: update
        query:
            xxx:
                constraints: {}
                description: xxx string.
                meta: null
                type: string
        rpcname: UpdateSample
    Delete:
        description: Use this to delete existing samples.
        data:
            request: google.protobuf.Empty
            response: google.protobuf.Empty
            bodyfield: body
        deeplink:
            description: 'Delete: DELETE /samples/{xxx} google.protobuf.Empty , google.protobuf.Empty #Use this to delete existing samples.'
            href: /samples/{xxx}
            method: DELETE
            rel: delete
        query:
            xxx:
                constraints: {}
                description: xxx string.
                meta: null
                type: string
        rpcname: DeleteSample
    DeleteAll:
        description: Use this to delete ALL samples.
        data:
            request: google.protobuf.Empty
            response: google.protobuf.Empty
            bodyfield: body
        deeplink:
            description: 'DeleteAll: DELETE /samples google.protobuf.Empty , google.protobuf.Empty #Use this to delete ALL samples.'
            href: /samples
            method: DELETE
            rel: deleteall
        query: {}
        rpcname: DeleteAllSample
    Custom:
        description: Custom methods are always POST.
        data:
            request: google.protobuf.Empty
            response: google.protobuf.Empty
            bodyfield: body
        deeplink:
            description: 'Custom: POST /samples/{xxx}:custom google.protobuf.Empty , google.protobuf.Empty #Custom methods are always POST.'
            href: /samples/{xxx}:custom
            method: POST
            rel: custom
        query:
            xxx:
                constraints: {}
                description: xxx string.
                meta: null
                type: string
        rpcname: CustomSample
