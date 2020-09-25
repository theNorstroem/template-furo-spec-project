name: DeleteAllSampleRequest
type: DeleteAllSampleRequest
description: request message for DeleteAllSample
__proto:
    package: Services.sampleservice
    targetfile: reqmsgs.proto
    imports:
        - google/protobuf/empty.proto
    options:
        go_package: github.com/theNorstroem/template-furo-spec-project/dist/pb/Services/sampleservice;sampleservicepb
        java_multiple_files: "true"
        java_outer_classname: ReqmsgsProto
        java_package: com.Services.sampleservice
fields:
    body:
        type: .google.protobuf.Empty
        description: Body with google.protobuf.Empty
        __proto:
            number: 1
            oneof: ""
        __ui: null
        meta:
            default: ""
            hint: ""
            label: label.Services.sampleservice.DeleteAllSampleRequest.body
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
