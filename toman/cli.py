import click


@click.command()
@click.option('--name', '-n')
@click.option('--age', '-a')
def cli(name, age):
    if name:
        click.echo(f'Hello {name}!')
    if age:
        click.echo(f'Aint you {age} years old!')
    if not name and not age:
        click.echo('Hello Guest!! Welcome to toman cli interface')