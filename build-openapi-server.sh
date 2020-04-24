


docker run --rm -u "$(id -u):$(id -g)" \
    -v ${PWD}:/local openapitools/openapi-generator-cli generate \
    -i https://raw.githubusercontent.com/pjakovits/datapipelineserver/master/datapipeline-openapi.yaml \
    -g python-flask \
    -o /local/datapipeline-server/
