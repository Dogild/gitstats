Gitstats
========

Introduction
------------

This library can be used to retrieve public activities of the last year of a github account. The datas retrieved per account are the number of contributions and number of commits/issues per days. Statistics only used public activity of the account.

Installation
------------

Create a virtualenv and then

`pip install -r requirements.txt`

You need to define the environment variable `GITSTATS_TOKEN` to used the library. Go to the webpage github to generate a token.

Getting start
-------------

Open the file example.py, change the account name to yours and then launch `python example.py` et voilà

Licence
-------
This library is free software; you can redistribute it and/or modify it under
the terms of the GNU Lesser General Public License as published by the Free
Software Foundation; either version 2.1 of the License, or (at your option)
any later version.

This library is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
details.

You should have received a copy of the GNU Lesser General Public License along
with this library; if not, write to the Free Software Foundation, Inc., 51
Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA