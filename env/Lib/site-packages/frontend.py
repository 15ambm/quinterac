import click

logged = False

def log():
     click.echo(logged)

@click.command()
def hello():
     click.echo("Hello World")
     log()
