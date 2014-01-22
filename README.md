Novena-EZMac
============

Mac/Serial pairing tracker/generator for the factory line of the Novena open Laptop project.

Built on Django 1.6, though there's nothing fancy in it. Should work with older versions.

Instructions
------------

- Add a local_settings.py file to EzMAC folder declaring a SECRET_KEY for inclusion in settings.py .
- Configure custom DB server settings if desired (defaults to SQLite3) (can be done via env vars w/ dj-database-url).
- './manage.py syncdb' and create an admin un/pw.
- Create an initial dataset through admin console or via './manage.py loaddata macs.json' (after making a source json).
- Run via ./manage.py runserver
