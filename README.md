# OpenAPIGenerator migration to Requests library

## About

This repo is an example of tests that are writen two ways: with OpenAPIGenerator and with Requests library.

## Set Up

### OpenAPI Generator
Install OpenAPIGenerator with `brew install openapi-generator`

You will need to run `generate` script in Makefile to regenerate tests with OpenAPIGenerator. 
It will create clients, docs and samples of unit tests in corresponding folders.
