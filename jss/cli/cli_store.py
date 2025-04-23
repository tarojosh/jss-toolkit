import click

# jss store <website> <password> [username]
# jss update <website> <new_password> [new_username]

# jss get <website>  # returns the password
# jss get --all  # Returns all stored information

# Maybe combine it all?
# jss pm --store -s <website> <password>
# jss pm --update -u <website> <new_password>
# jss pm --get -g <website>

@click.command()
@click.option('--text', '-t', help='wip')
def cli(text):
    click.echo("Store command WIP")


if __name__ == '__main__':
    cli()
