name: SampleEntity
type: SampleEntity
description: Entitycontainer which holds a sample.Sample
__proto:
    package: sample
    targetfile: sample.proto
    imports:
        - furo/furo.proto
        - furo/furo.proto
    options:
        go_package: github.com/theNorstroem/template-furo-spec-project/dist/pb/sample;samplepb
        java_multiple_files: "true"
        java_outer_classname: SampleProto
        java_package: com.sample
fields:
    data:
        type: sample.Sample
        description: the data contains a sample.Sample
        __proto:
            number: 1
            oneof: ""
        __ui: null
        meta:
            default: ""
            hint: ""
            label: label.sample.SampleEntity.data
            options: null
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
    links:
        type: furo.Link
        description: the Hateoas links
        __proto:
            number: 2
            oneof: ""
        __ui: null
        meta:
            default: ""
            hint: ""
            label: label.sample.SampleEntity.links
            options: null
            readonly: false
            repeated: true
            typespecific: null
        constraints: {}
    meta:
        type: furo.Meta
        description: Meta for the response
        __proto:
            number: 3
            oneof: ""
        __ui: null
        meta:
            default: ""
            hint: ""
            label: label.sample.SampleEntity.meta
            options: null
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
