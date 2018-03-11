import tempfile

from hr import inventory


def test_inventory_load():
    """
    `inventory.load` takes a path to a file and parses it as JSON
    """
    inv_file = tempfile.NamedTemporaryFile(delete=False)
    inv_file.write("""
    [
        {
            "name": "kevin",
            "groups": ["wheel", "dev"],
            "password": "password_one"
        },
        {
            "name": "lisa",
            "groups": ["wheel"],
            "password": "password_two"
        },
        {
            "name": "jim",
            "groups": [],
            "password": "password_three"
        }
    ]
    """)
    inv_file.close()
    user_list = inventory.load(inv_file.name)
    assert user_list[0] == {
        'name': 'kevin',
        'groups': ['wheel', 'dev'],
        'password': 'password_one'
    }
    assert user_list[1] == {
        'name': 'lisa',
        'groups': ['wheel'],
        'password': 'password_two'
    }
    assert user_list[2] == {
        'name': 'jim',
        'groups': [],
        'password': 'password_three'
    }

def test_inventory_dump(mocker):
    """
    `inventory.dump` takes a destination path and optional list of users
    to export then exports the existing user information.
    """
    dest_file = tempfile.NamedTemporaryFile(delete=False)
    dest_file.close()

    # spwd.getspnam can't be used by non-root user normally.
    # Mock the implemntation so that we can test.
    mocker.patch('spwd.getspnam', return_value=mocker.Mock(sp_pwd='password'))

    # grp.getgrall will return the values from the test machine.
    # To get consistent results we need to mock this.
    mocker.patch('grp.getgrall', return_value=[
        mocker.Mock(gr_name='super', gr_mem=['bob']),
        mocker.Mock(gr_name='other', gr_mem=[]),
        mocker.Mock(gr_name='wheel', gr_mem=['bob','kevin']),
    ])

    inventory.dump(dest_file.name, ['kevin', 'bob'])

    with open(dest_file.name) as f:
       assert f.read() == """[{"password": "password", "name": "kevin", "groups": ["wheel"]}, {"password": "password", "name": "bob", "groups": ["super", "wheel"]}]"""
















