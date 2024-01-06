# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-08-19 21:33
"""
import click


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='THe person to greet')
def hello(count, name):
    """simple program that greets NAME for a total of COUNT times"""
    for x in range(count):
        click.echo(f"Hello {name}")


if __name__ == '__main__':
    hello()
