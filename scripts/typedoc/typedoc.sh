#!/bin/bash

spectools exportAsYaml | simple-generator -t scripts/typedoc/typedoc.tpl > dist/typedoc.md

echo "Doc written to  dist/typedoc.md"
