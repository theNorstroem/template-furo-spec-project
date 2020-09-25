## List of types
{{range $t, $type:= .types}}
### <a name="{{$t}}"></a>{{$t}}
> {{$type.description | replace "\n" "\n> " | noescape}}

{{range $fieldname, $field:= $type.fields}}
**{{$fieldname}}**
<small>[{{$field.type}}](#{{$field.type}})</small>
<br>{{$field.description | replace "\n" "<br> " | noescape}}
{{end}}
{{end}}