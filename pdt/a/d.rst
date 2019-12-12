#####
PDT A
#####

****
Do
****

.. _`da0`:
:da0: data text (|pa0|)

There are several text serialization formats:
https://en.wikipedia.org/wiki/Comparison_of_data-serialization_formats

All of them need conversion to be usable in python or buffered in an SQL database.

Since the programming language here is Python,
also data shall be represented in Python.
A language is a good tool to describe also data.
One can use its inherent lookup for identifiers.

Data files are recognized by ``*.db.py``.

.. _`da4`:
:da4: conversion

Text data (``*.db.py``) files are converted to a local database for buffering,
either by a separate command or automatically on an event
(checkout, loading in python, start of a (local) http server).

Data can be edited

- directly in the original ``.db.py`` files
- optionally via the database (via direct SQL or via an HTTP server)

A database buffering might not be needed at all for smaller data sets.

If editing via the database is possible,
there must be a conversion
from the database to the text files (``.db.py``) before checking in.

.. _`da1`:
:da1: data ID (|pa1|)

- The ID of a data record is NOT sequentially generated from the database.
- The ID is also a valid python identifier usable in code.
- The ID is unique throughout the repo.
  This is achieved via a name prefix per class/table.

.. _`da2`:
:da2: history (|pa2|)

Text data is checked into git to track changes over time.
The git history text is a journal entry
that describes the changes in the ``.db.py`` files.

``.db.py`` file changes are checked in *per posting*.

Python code

- does the posting between the data files
- makes a git commit with a marker for these posting commits
- followed by *ledger-cli* posting command

This can be done

- via command line
- from Python
- by an HTTP POST




