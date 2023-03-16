#!/usr/bin/env python3
import re
import sys
import yaml

from plumbum import cli
from pathlib import Path


class Y2P(cli.Application):
    DESCRIPTION = "convert yaml to dot notation"

    show_params = cli.Flag(["--show-params"], default=False,
                           help="Show parameters given to y2p and exit.")

    def main(self):
        if self.show_params:
            print(sys.argv)

        if not self.nested_command:
            print("No command given")
            return 1  # error exit code


@Y2P.subcommand("file")
class Y2PFile(cli.Application):

    def main(self, *files):
        for file in files:
            with open(file, 'r') as f:
                yaml_content = yaml.safe_load(f)
                visit(yaml_content)


@Y2P.subcommand("string")
class Y2PString(cli.Application):
    stdin = cli.Flag(["-s", "--stdin"], default=False,
                     help="Use stdin as source")

    def main(self, *yaml_strs):

        if self.stdin:
            yaml_strs = [sys.stdin.read()]

        for yaml_str in yaml_strs:
            yaml_content = yaml.safe_load(yaml_str)
            visit(yaml_content)


def visit(node, parent=None):
    if isinstance(node, str):
        print(f"{parent}={node}")
        return

    for key, value in node.items():
        if isinstance(value, dict):
            visit(value, f"{parent}.{key}") if parent else visit(value, f"{key}")
        elif isinstance(value, list):
            for n, item in enumerate(value):
                visit(item, f"{parent}.{key}[{n}]")
        else:
            print(f"{parent}.{key}={value}")


if __name__ == "__main__":
    try:
        Y2P.run()
    except (Exception, RuntimeError) as e:
        raise Exception(f"There is an error in your command parameters. Please verify them: '{sys.argv}'. "
                        f"Upper exception:{e}")
