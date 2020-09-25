name: ListSampleRequest
type: ListSampleRequest
description: request message for ListSample
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
            label: label.Services.sampleservice.ListSampleRequest.body
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
    q:
        type: string
        description: query string.
        __proto:
            number: 2
            oneof: ""
        __ui: null
        meta:
            default: ""
            hint: ""
            label: label.Services.sampleservice.ListSampleRequest.q
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
    page:
        type: string
        description: Use this field to specify page to display.
        __proto:
            number: 5
            oneof: ""
        __ui: null
        meta:
            default: ""
            hint: ""
            label: label.Services.sampleservice.ListSampleRequest.page
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
    filter:
        type: string
        description: Use this field to specify page to display.
        __proto:
            number: 3
            oneof: ""
        __ui: null
        meta:
            default: ""
            hint: ""
            label: label.Services.sampleservice.ListSampleRequest.filter
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
    order_by:
        type: string
        description: Use this field to specify page to display.
        __proto:
            number: 4
            oneof: ""
        __ui: null
        meta:
            default: ""
            hint: ""
            label: label.Services.sampleservice.ListSampleRequest.order_by
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
