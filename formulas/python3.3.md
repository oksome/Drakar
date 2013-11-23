Tips for installing Python 3.3 from scratch on Debian.

Run configure with your installation prefix:

`./configure --prefix=/path/to/install`

Create a virtualenv:

`$PYTHON33/bin/pyvenv-3.3 myvenv`

Install easy_install to install pip:

`curl -O http://python-distribute.org/distribute_setup.py`
`easy_install pip`
