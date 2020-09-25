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
        go_package: github.com/theNorstroem/template-furo-spec-project/dist/pb/sample;samplepb
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
        __ui:
            component: ""
            flags: []
            noinit: false
            noskip: false
        meta:
            default: ""
            hint: ""
            label: label.Sample.id
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
    display_name:
        type: string
        description: A * berore the type means readonly
        __proto:
            number: 2
            oneof: ""
        __ui:
            component: ""
            flags: []
            noinit: false
            noskip: false
        meta:
            default: ""
            hint: ""
            label: label.Sample.display_name
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
    tags:
        type: string
        description: A [] means repeated, repeated can also be required *[]type or readonly -[]type
        __proto:
            number: 3
            oneof: ""
        __ui:
            component: ""
            flags: []
            noinit: false
            noskip: false
        meta:
            default: ""
            hint: ""
            label: label.Sample.tags
            options:
                flags: []
                list: []
            readonly: false
            repeated: true
            typespecific: null
        constraints: {}
    update_mask:
        type: .google.protobuf.FieldMask
        description: Needed if you want to patch a record
        __proto:
            number: 4
            oneof: ""
        __ui:
            component: ""
            flags: []
            noinit: false
            noskip: false
        meta:
            default: ""
            hint: ""
            label: label.Sample.update_mask
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
    cost:
        type: .google.type.Money
        description: Needed if you want to patch a record
        __proto:
            number: 5
            oneof: ""
        __ui:
            component: ""
            flags: []
            noinit: false
            noskip: false
        meta:
            default: ""
            hint: ""
            label: label.Sample.cost
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
    wint:
        type: Valueonly
        description: test wrapper type
        __proto:
            number: 6
            oneof: ""
        __ui: null
        meta:
            default: ""
            hint: ""
            label: label.sample.Sample.wint
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
    goint:
        type: google.protobuf.Int32Value
        description: test wrapper type
        __proto:
            number: 7
            oneof: ""
        __ui: null
        meta:
            default: ""
            hint: ""
            label: label.sample.Sample.goint
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
