"""Commands."""
import click
import ujson
import utils

from repositories import configuration


@click.group(name='cli')
def cli():
    pass


@cli.command()
@click.argument('config', type=click.Path(exists=True))
def validate(config: click.Path):
    """Clone the repositories specified in the configuration file."""
    config_path = click.format_filename(config)
    if '.yml' in config_path or '.yaml' in config_path:
        cfg = utils.load_yaml(config_path)
    elif '.json' in config_path:
        cfg = utils.load_json(config_path)
    else:
        raise click.Abort('File not supported!')

    ok, err = configuration.validate(cfg)
    if not ok:
        click.echo(ujson.dumps(err))
        raise click.Abort('Validation failed...')
    click.echo('Configuration is ok')
