import typer
from typing import Annotated

app = typer.Typer()


def version_callback(value: bool):
    if value:
        typer.echo("Rosen Claw v1.0.0")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        False,
        "--version",
        "-V",
        help="显示版本",
        callback=version_callback,
        is_eager=True,
    ),
):
    pass


@app.command()
def run(
    type_: Annotated[str, typer.Option("--type", "-t", help="启动类型")] = "command",
):
    if type_ == "command":
        from rosen_claw.channel.channels.command import CommandChannel
        from asyncer import runnify

        channel = CommandChannel()
        runnify(channel.run)()
    else:
        typer.echo(f"未知的启动类型: {type_}")


if __name__ == "__main__":
    app()
