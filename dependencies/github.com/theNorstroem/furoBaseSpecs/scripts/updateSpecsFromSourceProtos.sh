#!/usr/bin/env bash

# enable recursion for /**/*.xxx
shopt -s globstar dotglob

cd sourceProtos

protoc -I. --furo-specs_out=:../Specs **/*.proto