import pytest

from hr import cli

@pytest.fixture()
def parser():
    return cli.create_parser()

def test_parser_without_argument(parser):
    """
    An error is raised if no arguments are passed to the parser
    """
    with pytest.raises(SystemExit):
        parser.parse_args([])

def test_parser_with_argument(parser):
    """
    No error is raised if a path is given as an argument
    """
    args = parser.parse_args(['/some/path/test.json'])
    assert args.path == '/some/path/test.json'

def test_parser_export_flag(parser):
    """
    The export value is set to True if the --export flag is given
    or False if not presented.
    """
    args = parser.parse_args(['some/path/test.json', '--export'])
    assert args.export == True

    args = parser.parse_args(['some/path/test.json'])
    assert args.export == False
