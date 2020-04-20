{
  "name": "ExampleService",
  "description": "service specs for the example api",
  "version": "0.0.1",
  "lifecycle": {
    "deprecated": false,
    "info": "This version is still valid"
  },
  "__proto": {
    "package": "exampleservice",
    "imports": [
      "example/example.proto",
      "google/protobuf/empty.proto"
    ],
    "targetfile": "exampleservice.proto",
    "options": {
      "go_package": "/exampleservice"
    }
  },
  "services": {
    "List": {
      "description": "The List method takes zero or more parameters as input, and returns a ExampleCollection of ExampleEntity that match the input parameters.",
      "rpc_name": "ListExamples",
      "data": {
        "request": null,
        "response": "example.ExampleCollection"
      },
      "query": {
        "q": {
          "description": "Query term to search a example",
          "type": "string",
          "meta": {
            "label": "Search",
            "hint": ""
          },
          "__proto": {
            "type": "string"
          }
        }
      },
      "deeplink": {
        "description": "Describe_the_query_params_if_you_have",
        "rel": "list",
        "href": "/api/examples",
        "method": "GET"
      }
    },
    "Create": {
      "description": "Creates a new Example",
      "rpc_name": "CreateExample",
      "data": {
        "request": "example.Example",
        "response": "example.ExampleEntity"
      },
      "query": {
      },
      "deeplink": {
        "rel": "create",
        "href": "/api/examples",
        "method": "POST"
      }
    },
    "Get": {
      "description": "The Get method takes zero or more parameters, and returns a ExampleEntity which contains a Example",
      "rpc_name": "GetExample",
      "data": {
        "request": null,
        "response": "example.ExampleEntity"
      },
      "query": {
      },
      "deeplink": {
        "rel": "self",
        "href": "/api/examples/{ex}",
        "method": "GET"
      }
    },
    "Update": {
      "description": "Updates a Example, partial updates are supported",
      "rpc_name": "UpdateExample",
      "data": {
        "request": "example.Example",
        "response": "example.ExampleEntity"
      },
      "query": {},
      "deeplink": {
        "rel": "update",
        "href": "/api/examples/{ex}",
        "method": "PATCH"
      }
    },
    "Delete": {
      "description": "Delete a Example",
      "rpc_name": "DeleteExample",
      "data": {
        "request": "google.protobuf.Empty",
        "response": "google.protobuf.Empty"
      },
      "query": {},
      "deeplink": {
        "rel": "delete",
        "href": "/api/examples/{ex}",
        "method": "DELETE"
      }
    }
  }
}
