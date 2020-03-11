===
LOG
===

.. _`20191212`:
:20191212:

pdt/a/p.rst
pdt/a/d.rst
pdt/a/t.rst

Check ``rstdoc`` on repo.

.. _`20200311`:
:20200311:

- Rename ``ipdt`` files to ``0123``.
- pdt/b
  about logging.

Getting up to speed again.

A crucial point in econ is to
do product related bookkeeping in the same repo.
Also financial data is important for the product,
because it keeps it running.
It should therefore be in the same repo.

How to store data in the same repo?

- text to make it traceable by git
- orthogonal
- convertible to db to allow queries

Option 1: sqlite dump

``Sqlite3`` has ``.dump`` and ``.read``.
The dump fulfills these requirements.
The dump

- is checked in
- a temporary .sqlite files is generated
  for other purposes.

There is `automap`_ to do without ORM code.

.. _`automap`: https://docs.sqlalchemy.org/en/13/orm/extensions/automap.html

Option 2: leger-cli

There is no need to convert to db for query here.
There is also a html interface.
So this should works do *without further effort*.

https://github.com/ledger/ledger
https://www.ledger-cli.org/3.0/doc/ledger3.html

https://github.com/lipidity/ledgible

There would be other options:
https://plaintextaccounting.org/
