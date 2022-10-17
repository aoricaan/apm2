import typer

from apm2.commands.lambdas.actions import CreateLambda
from apm2.utils.providers import BasicProvider

lambda_app = typer.Typer()
provider = BasicProvider()


@lambda_app.command('new')
def new_lambda(name: str = typer.Option(..., help='Name for the new lambda.', prompt=True),
               handler: str = typer.Option('lambda_function.lambda_handler',
                                           help='name of the function file and function name.')):
    """
    Add a new aws lambda structure in the project.
    """
    payload = dict(name=name, handler=handler)
    provider.set_command(CreateLambda(payload))
    provider.execute_command()
