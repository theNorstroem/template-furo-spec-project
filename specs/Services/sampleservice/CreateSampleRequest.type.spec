name: CreateSampleRequest
type: CreateSampleRequest
description: request message for CreateSample
__proto:
    package: Services.sampleservice
    targetfile: reqmsgs.proto
    imports:
        - sample/sample.proto
    options:
        go_package: github.com/theNorstroem/template-furo-spec-project/dist/pb/Services/sampleservice;sampleservicepb
        java_multiple_files: "true"
        java_outer_classname: ReqmsgsProto
        java_package: com.Services.sampleservice
fields:
    body:
        type: .sample.Sample
        description: Body with sample.Sample
        __proto:
            number: 1
            oneof: ""
        __ui: null
        meta:
            default: ""
            hint: ""
            label: label.Services.sampleservice.CreateSampleRequest.body
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
