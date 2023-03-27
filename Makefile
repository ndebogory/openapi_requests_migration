OPENAPI_SPEC_URL = https://raw.githubusercontent.com/openapitools/openapi-generator/master/modules/openapi-generator/src/test/resources/3_0/
SWAGGER_YAML_PATH = petstore.yaml
CLIENTS_BASE_FOLDER=clients/_generated
CLIENTS_PACKAGE_NAME_PREFIX=$(subst /,.,${CLIENTS_BASE_FOLDER})
OPENAPI_GENERATOR_IGNORE_PATH = .openapi-generator-ignore

.gen-deps:
	@if ! (test -f bin/openapi-generator-cli.jar) ; then\
		wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/4.3.1/openapi-generator-cli-4.3.1.jar -O bin/openapi-generator-cli.jar;\
	fi

PETSTORE_CLIENT_PATH=${CLIENTS_BASE_FOLDER}/petstore/
generate-client:
	mkdir -p ${PETSTORE_CLIENT_PATH}
	cp ${OPENAPI_GENERATOR_IGNORE_PATH} ${PETSTORE_CLIENT_PATH}.openapi-generator-ignore
	java -Dclient -DmodelDocs=false\
		-jar bin/openapi-generator-cli.jar generate \
		-i ${OPENAPI_SPEC_URL}/${SWAGGER_YAML_PATH} \
		--enable-post-process-file \
		-g python \
		-o . \
		--additional-properties=generateSourceCodeOnly,packageName=${CLIENTS_PACKAGE_NAME_PREFIX}.petstore,withXml=False

generate: .gen-deps generate-client