name: SampleCollection
type: SampleCollection
description: Collectioncontainer which holds a sample.Sample
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
    entities:
        type: sample.SampleEntity
        description: the data contains a sample.Sample
        __proto:
            number: 1
            oneof: ""
        __ui: null
        meta:
            default: ""
            hint: ""
            label: label.sample.SampleCollection.entities
            options: null
            readonly: false
            repeated: true
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
            label: label.sample.SampleCollection.links
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
            label: label.sample.SampleCollection.meta
            options: null
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
