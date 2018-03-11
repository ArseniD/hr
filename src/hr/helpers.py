import pwd

def user_names():
    """
    Helper returns a list of all existing system users with home dir.
    """
    return [user.pw_name for user in pwd.getpwall()
            if user.pw_uid >= 1000 and 'home' in user.pw_dir]


