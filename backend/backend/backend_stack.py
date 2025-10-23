from aws_cdk import (
    Stack,
    aws_apigateway as apigw,
    aws_lambda as _lambda,
    aws_lambda_python_alpha as python
)
from constructs import Construct

class BackendStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        fn = python.PythonFunction(
            self,
            "MyPythonLambda",
            entry="./lib",  # Path to the directory containing lambda_handler.py
            index="lambda_handler.py",  # The file containing the handler
            handler="handler",  # The name of the handler function within lambda_handler.py
            runtime=_lambda.Runtime.PYTHON_3_13,  # Specify the Python runtime
            function_name="MyExamplePythonLambda", # Optional: custom function name
            environment={
                "MY_ENV_VAR": "some_value" # Optional: environment variables
            }
        )

        endpoint = apigw.LambdaRestApi(
            self,
            "ApiGwEndpoint",
            handler=fn,
            rest_api_name="HelloApi"
        )