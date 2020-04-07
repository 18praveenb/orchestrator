#!/usr/bin/env python3
import click

@click.group()
def main():
    pass

@main.command()
def run():
    pass

if __name__ == '__main__':
    main()
