import argparse

def create_parser():
    parser = argparse.ArgumentParser(description="""
    Manage users premised on json file.
    """)
    parser.add_argument('path', help='PATH to json inventory file')
    parser.add_argument('--export', action='store_true', help='export current settings to inventory file')
    return parser
