name: Valueonly
type: Valueonly
description: Test
__proto:
    package: sample
    targetfile: sample.proto
    imports:
        - google/protobuf/wrappers.proto
    options:
        go_package: github.com/theNorstroem/template-furo-spec-project/dist/pb/sample;samplepb
        java_multiple_files: "true"
        java_outer_classname: SampleProto
        java_package: com.sample
fields:
    value:
        type: int32
        description: A * before the type means required
        __proto:
            number: 1
            oneof: ""
        __ui: null
        meta:
            default: ""
            hint: ""
            label: label.sample.Valueonly.value
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
    goint:
        type: google.protobuf.UInt32Value
        description: test wrapper type
        __proto:
            number: 2
            oneof: ""
        __ui: null
        meta:
            default: ""
            hint: ""
            label: label.sample.Valueonly.goint
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
