name: int64
type: Int64
description: Furo annotated type wrapper message for `int64`. The range constraints are set to Number.MIN_SAFE_INTEGER - Number.MAX_SAFE_INTEGER because of browser limitations
__proto:
    package: furo.fat
    targetfile: fat.proto
    imports: []
    options:
        cc_enable_arenas: "true"
        csharp_namespace: Furo.Fat
        go_package: github.com/theNorstroem/FuroBaseSpecs/dist/pb/furo/fat;fatpb
        java_multiple_files: "true"
        java_outer_classname: FatProto
        java_package: pro.furo.fat
        objc_class_prefix: FPB
fields:
    value:
        type: int64
        description: The JSON representation for `Int64Value` is JSON number, range is set to Number.MIN_SAFE_INTEGER - Number.MAX_SAFE_INTEGER
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
            label: ""
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints:
            max:
                is: "9007199254740991"
                message: out of range
            min:
                is: "-9007199254740991"
                message: out of range
    labels:
        type: string
        description: Labels / flags for the value, something like unspecified, empty, confidential, absent,... Can be used for AI, UI, Business Logic,...
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
            label: ""
            options:
                flags: []
                list: []
            readonly: false
            repeated: true
            typespecific: null
        constraints: {}
    attributes:
        type: map<string,string>
        description: 'Attributes for a value, something like confidential-msg: you are not allowed to see this value '
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
            label: ""
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
