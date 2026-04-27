from setuptools import setup, find_packages

setup(
    name="rosen-claw",
    version="0.1.0",
    description="A CLI AI agent tool",
    author="NOKIAO",
    license="MIT",
    python_requires=">=3.10",
    packages=find_packages(),
    install_requires=[
        "openai>=2.32.0",
        "typer>=0.24.2",
        "prompt-toolkit>=3.0.52",
        "rich>=15.0.0",
        "loguru>=0.7.3",
        "pydantic-settings>=2.14.0",
        "asyncer>=0.0.17"
    ],
)