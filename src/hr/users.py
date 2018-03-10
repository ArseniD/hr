import sys
import subprocess
import string


def add(user_info):
    print("Adding user '%s'" % user_info['name'])
    try:
        subprocess.call([
            'useradd',
            '-p',
            user_info['password'],
            '-G',
            _groups_str(user_info),
            user_info['name'],
        ])
    except:
        print("Failed to add user '%s'" % user_info['name'])
        sys.exit(1)

def remove(user_info):
    print("Removing user '%s'" % user_info['name'])
    try:
        subprocess.call([
            'userdel',
            '-r',
            user_info['name']
        ])
    except:
        print("Failed to remove user '%s'" % user_info['name'])
        sys.exit(1)

def update(user_info):
    print("Updating user '%s'" % user_info['name'])
    try:
        subprocess.call([
            'usermod',
            '-p',
            user_info['password'],
            '-G',
            _groups_str(user_info),
            user_info['name']
        ])
    except:
        print("Failed to update user '%s'" % user_info['name'])
        sys.exit(1)

def sync(users, existing_user_names=None):
    existing_user_names = (existing_user_names or _user_names())
    user_names = [user['name'] for user in users]
    for user in users:
        if user['name'] not in existing_user_names:
            add(user)
        elif user['name'] in existing_user_names:
            update(user)
    for user_name in existing_user_names:
        if not user_name in user_names:
            remove({'name': user_name})

def _groups_str(user_info):
    """
    Helper returns a string of all groups from users dict,
    separated by `,`.
    """
    return string.join(user_info['groups'] or [], ',')

def _user_names():
    """
    Helper returns a list of all existing system users with home dir.
    """
    return [user.pw_name for user in pwd.getpwall()
            if user.pw_uid >= 1000 and 'home' in user.pw_dir]





