BASE_CONFIGURATION = """[apm.project.definition]
name = "{app_name}"
description = ""

[apm.templates.code]
lambda_template = "utils/templates/lambda.txt"
lambda_cfn_template = "utils/templates/lambda.json"
swagger_template = "utils/templates/api_verbs.json"

[apm.templates.deploy]
project_template = "templates/projectTemplate.json"
api_swagger_template = "src/api.json"

[apm.project.folders]
lambdas = "src/lambdas"
layers = "src/layers"
"""