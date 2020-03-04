{
  "name": "example_collection",
  "type": "ExampleCollection",
  "description": "ExampleCollection with repeated ExampleEntity",
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
    "meta": {
      "description": "Meta for the response",
      "type": "furo.Meta",
      "__proto": {
        "number": 2
      }
    },
    "links": {
      "description": "Hateoas links",
      "type": "furo.Link",
      "meta": {
        "repeated": true
      },
      "__proto": {
        "number": 3
      }
    },
    "entities": {
      "description": "Contains a example.ExampleEntity repeated",
      "type": "example.ExampleEntity",
      "meta": {
        "repeated": true
      },
      "__proto": {
        "number": 4
      }
    }
  }
}
