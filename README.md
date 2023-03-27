# OpenAPIGenerator migration to Requests library

## About

This repo is an example of tests that are writen two ways: with OpenAPIGenerator and with Requests library.

## Set Up

Install dependencies with `pip install -r requirements.txt`

### OpenAPI Generator

If you want to regenerate data, which is used in tests:
1. Install OpenAPIGenerator with `brew install openapi-generator`
2. You will need to run `generate` script in Makefile to regenerate tests with OpenAPIGenerator. 
It will download openapi-generator-cli.jar, which is used to create clients, 
docs and samples of unit tests in corresponding folders.

## Project Structure

In folder `tests` you can find tests that are written with OpenAPIGenerator and with Requests library. 
Tests are situated in `tests/generator_tests` and `tests/requeststs_tests` folders correspondingly.

In folder `utils` you can find supporting functions for tests.
In `http_requests.py` there is a declaration of a client for forking with Requests lib.

Client for OpenApiGenerator is situated in `clients/petstore_service/__init__.py` and was added manually.

## Run Tests

All tests can be run with __pytest__.
