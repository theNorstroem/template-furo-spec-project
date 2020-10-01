## type and service specs

there is a sample type spec below. **the text after '#' are only for explaining the meaning of the fields.
do not use them in you specs**.  

```yaml
name: Sample
type: Sample
description: Sample with auto Collection and Entity (ce)
__proto: # this part hat additional information about google protobufs  
    package: sample # package name of protos
    targetfile: sample.proto
    imports: # dependencies must be listed here
        - google/protobuf/field_mask.proto
        - google/type/money.proto
        - google/protobuf/wrappers.proto
    options:
        go_package: github.com/theNorstroem/template-furo-spec-project/dist/pb/sample;samplepb
        java_multiple_files: "true" # Causes top-level messages, enums, and services to be defined at the package level, rather than inside an outer class named after the .proto file.
        java_outer_classname: SampleProto
        java_package: com.sample
fields:
    id: # subfield name of the sample type
        type: string # the type of field id. see the type list below
        description: A * before the type means required # this description will be use as the comment for the 'id' field for sample message int the sample.proto
        __proto:
            number: 1 # this number means that the field 'id' in sample message proto has a unique field number 1 
            oneof: "" # if this 'id' field is one of an enum type
        __ui: null # ui component can be defined here for display this 'id' field. e.g. furo-ui5-data-number-input
        meta: # meata information of this 'id' field
            default: "" # default value. this default value can be used to initiate the sample object
            hint: "" # will be used as hint for the input field like furo-data-textarea-input
            label: label.sample.Sample.id # label can be used as the placeholder of the input field like furo-ui5-data-number-input
            options:
                flags: [] # Attribute flags e.g. important, negative, positive. can be used for example for menu 
                list:  # use furo.optionitem as the type of items in the list in order to display them in the data-collection-dropdown component
                - id: xxx1
                  display_name: bike
                  selected: false 
                  "@type": type.furo.pro/furo.Optionitem
                - id: xxx2
                  display_name: car
                  selected: true # mark whether selected in dropdown as default
                  "@type": type.furo.pro/furo.Optionitem
            readonly: false # for ui this means this field is disabled
            repeated: false # field is an array by true
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
