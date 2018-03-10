import pytest
import subprocess

from hr import users

# encrypted version of 'password'
password = '$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/'

user_dict = {
    'name': 'kevin',
    'groups': ['wheel', 'dev'],
    'password': password
}

def test_users_add(mocker):
    """
    Given a user dictionary. `users.add(...)` should
    utilize `useradd` to create a user with the password
    and groups.
    """
    mocker.patch('subprocess.call')
    users.add(user_dict)
    subprocess.call.assert_called_with([
        'useradd',
        '-p',
        password,
        '-G',
        'wheel,dev',
        'kevin'
    ])

def test_users_remove(mocker):
    """
    Given a user dictionary, `users.remove(...)` should
    utilize `userdel` to delete the user.
    """
    mocker.patch('subprocess.call')
    users.remove(user_dict)
    subprocess.call.assert_called_with([
        'userdel',
        '-r',
        'kevin'
    ])

def test_users_update(mocker):
    """
    Given a user dictionary, `users.test_user_update(...)` should
    utilize `usermod` to update the user.
    """
    mocker.patch('subprocess.call')
    users.update(user_dict)
    subprocess.call.assert_called_with([
        'usermod',
        '-p',
        password,
        '-G',
        'wheel,dev',
        'kevin'
    ])

def test_users_sync(mocker):
    """
    Given a list of user dictionaries, `users.sync(...)` should
    create missing users, remove extra non-system users, and update
    existing users. A list of existing usernames can be passed in
    or default users will be used.
    """
    existing_user_name = ['kevin', 'bob']
    user_info = [
        user_dict,
        {
            'name': 'jose',
            'groups': ['wheel'],
            'password': password
        }
    ]
    mocker.patch('subprocess.call')

    users.sync(user_info, existing_user_name)
    subprocess.call.assert_has_calls([
        mocker.call([
            'usermod',
            '-p',
            password,
            '-G',
            'wheel,dev',
            'kevin',
        ]),
        mocker.call([
            'useradd',
            '-p',
            password,
            '-G',
            'wheel',
            'jose',
        ]),
         mocker.call([
            'userdel',
            '-r',
            'bob',
        ]),
    ])





