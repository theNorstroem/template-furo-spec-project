name: SecondSample
type: SecondSample
description: Sample with auto Collection and Entity (ce)
__proto:
    package: sample.second
    targetfile: second.proto
    imports:
        - sample/sample.proto
        - google/protobuf/field_mask.proto
        - google/type/money.proto
    options:
        go_package: github.com/theNorstroem/template-furo-spec-project/dist/pb/sample/second;secondpb
        java_multiple_files: "true"
        java_outer_classname: SecondProto
        java_package: com.sample.second
fields:
    first:
        type: sample.Sample
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
        constraints:
            required:
                is: "true"
                message: first is required
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
        type: google.protobuf.FieldMask
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
        type: google.type.Money
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
