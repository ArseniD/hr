hr
========

CLI for managing users on a server based on an “inventory” JSON file.

Preparing for Development
--------------------------------

1. Ensure ``pip`` and ``pipenv`` are installed.
2. Clone repository: ``git clone git@github.com:example/pgbackup``
3. Fetch development dependencies: ``make install``

Usage
-------

Takes a path, and produces an inventory file based on the current state of the system.

Export Example w/ bucket name:

::

        $ hr --export /home/user/current_user.json

Read a given inventory file, parse the JSON, and add, remove or update systems users info based on file.

Path Example w/ local path:

::

        $ hr /home/user/users_info.json

Example inventory JSON file:

::

        [
          {
            "name": "kevin",
            "groups": ["wheel", "dev"],
            "password": "$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/"
          },
          {
            "name": "lisa",
            "groups": ["wheel"],
            "password": "$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/"
          },
          {
            "name": "jim",
            "groups": [],
            "password": "$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/"
          }
        ]

Running Tests
-----------------

Run tests locally using ``make`` if virtualenv is active:

::

        $ make

If virtualenv isn't active then use:

::

        $ pipenv run make

