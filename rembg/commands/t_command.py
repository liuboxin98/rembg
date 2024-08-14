# test for learning how to use the rembg library
import click


@click.command(
    name="t",
    help="for example, a cat has an age of 3 years old and she is swimming in the pool.",
)
@click.option(
    "-o",
    "--obj",
    default="cat",
    type=str,
    required=True,
    help="the object that is being described.",
)
@click.option(
    "-a",
    "--age",
    default=3,
    type=int,
    required=True,
    help="the age of the object.",
)
@click.option(
    "-d",
    "--desc",
    default="swimming in the pool",
    type=str,
    required=True,
    help="the description of the object.",
)
def t_command(obj:str, age:int, desc:str) -> None:
    """for testing the rembg library."""
    print(f"a {obj} has an age of {age} years old and she is {desc}.")