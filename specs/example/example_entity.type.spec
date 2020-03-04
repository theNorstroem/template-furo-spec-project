{
  "name": "example_entity",
  "type": "ExampleEntity",
  "description": "ExampleEntity with Example",
  "__proto": {
    "package": "example",
    "options": {},
    "imports": [
      "furo/meta.proto",
      "furo/link.proto"
    ],
    "targetfile": "example.proto"
  },
  "fields": {
    "data": {
      "description": "contains a example.Example",
      "type": "example.Example",
      "__proto": {
        "number": 1
      }
    },
    "links": {
      "description": "Hateoas links",
      "type": "furo.Link",
      "meta": {"repeated": true},
      "__proto": {
        "number": 2
      }
    },
    "meta": {
      "description": "Meta for the response",
      "type": "furo.Meta",
      "__proto": {
        "number": 3
      }
    }
  }
}
