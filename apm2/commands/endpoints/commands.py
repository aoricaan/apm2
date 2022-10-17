import typer

from apm2.commands.endpoints.actions import CreatePath
from apm2.utils.data_types import endpoint_name_validation, Verbs
from apm2.utils.providers import BasicProvider

swagger_app = typer.Typer()
provider = BasicProvider()


@swagger_app.command('new')
def new_path(lambda_name: str = typer.Option(..., help='Lambda name where is the endpoint.',
                                             prompt='Ingress the lambda name'),
             handler: str = typer.Option('lambda_function.lambda_handler',
                                         help='name of the function file and function name.'),
             endpoint: str = typer.Option(..., help='Name for the endpoint',
                                          callback=endpoint_name_validation,
                                          prompt='Ingress the endpoint name'),
             verb: Verbs = typer.Option(..., help='Name of the verb for the endpoint',
                                        prompt='Ingress the verb fot this endpoint'),
             cors: bool = typer.Option(False, help='Enable the cors for the endpoint', prompt='Enable cors?')):
    """
    Add a new lambda with the swagger configuration to create an endpoint.

    """
    payload = dict(lambda_name=lambda_name, handler=handler, endpoint=endpoint, verb=verb, cors=cors)
    provider.set_command(CreatePath(payload))
    provider.execute_command()
