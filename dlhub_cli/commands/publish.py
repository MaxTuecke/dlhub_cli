import json
import click

from dlhub_cli.printing import format_output
# from dlhub_cli.config import get_dlhub_client
from dlhub_cli.parsing import dlhub_cmd, index_argument


@dlhub_cmd('publish', help='Publish a servable to DLHub.')
@click.option('--servable',
              default=None, show_default=True,
              help='The servable to publish.')
def publish_cmd(servable):
    """
    Publish a model to DLHub.

    :param servable: A particular servable to publish
    :return:
    """
    format_output("Publishing {}".format(servable))
    pass