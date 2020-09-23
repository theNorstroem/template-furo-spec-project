## type and service specs

sample type spec

```yaml
name: Sample
type: Sample
description: Sample with auto Collection and Entity (ce)
__proto:
    package: sample
    targetfile: sample.proto
    imports:
        - google/protobuf/field_mask.proto
        - google/type/money.proto
        - google/protobuf/wrappers.proto
    options:
        go_package: github.com/veith/spectest/dist/pb/sample;samplepb
        java_multiple_files: "true"
        java_outer_classname: SampleProto
        java_package: com.sample
fields:
    id:
        type: string
        description: A * before the type means required
        __proto:
            number: 1
            oneof: ""
        __ui: null
        meta:
            default: ""
            hint: ""
            label: label.sample.Sample.id
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}

```

sample service spec

```yaml
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
        go_package: github.com/veith/spectest/dist/pb/Services/sampleservice;sampleservicepb
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
            page:
                constraints: {}
                description: Use this field to specify page to display.
                meta: null
                type: string
        rpcname: ListSample

```
