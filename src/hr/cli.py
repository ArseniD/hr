import argparse

from setuptools import setup, find_packages

def create_parser():
    parser = argparse.ArgumentParser(description="""
    Manage users premised on json file.
    """)
    parser.add_argument('path', help='PATH to json inventory file')
    parser.add_argument('--export', action='store_true', help='export current settings to inventory file')
    return parser


def main():
    from hr import users, inventory

    args = create_parser().parse_args()

    if args.export:
        inventory.dump(args.path)
    else:
        users_info = inventory.load(args.path)
        users.sync(user_info)
