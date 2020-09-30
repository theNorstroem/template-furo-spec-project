## mu specs
mu spec is the most compact form to describe the type and the service. mu specs can be used as
the basic to generate service and type specs. 

## Notation in mu specs


mu type spec example:
```yaml

- type: 'sample.Valueonly #Test '
  fields:
    value: 'int32:1 #A * before the type means required'
    goint: 'google.protobuf.UInt32Value:2 #test wrapper type'
  target: sample.proto
```
in the example the strings 'int32:1 #A * before the type means required' after field value has following meanings:
- 'int32' is the type of the field. 
- '1' means that the field 'value' in message proto has a unique field number 1 
- '#...' the description of the field can be put after the '#' character


