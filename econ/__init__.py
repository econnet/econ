"""
The econ Python module automates activities around an econ repo.

A technical proposal on the layout of an econ repos is developed along.

.. _`e0`:
:e0: data text

Data is stored as **text**, because text is the most accessible format.

There are several text serializaton formats:
https://en.wikipedia.org/wiki/Comparison_of_data-serialization_formats

All of them need conversion to be usable in python or buffered in an SQL database.

Since the programming language here is Python,
also data shall be represented in Python.
A language is a good tool to describe also data, especially if interpreted.
One can use its inherent lookup for identifiers.

Data files are recognized by ``*.db.py``.

Text data is checked into git to track changes over time.

.. _`e3`:
:e3: data language

A data query language like SQL is more cumbersome for retrieval, than e.g. Python.
SQL though

- is able to selectively retrieve and edit data not fitting into memory
- is a data domain specific language usable by all general languages

.. `e4`:
:e4: conversion

Text data (``*.db.py``) files are converted to a local database for buffering,
either by a separate command or automatically on an event
(checkout, loading in python, start of a (local) http server).

Data can be edited

- directly in the original ``.db.py`` files
- optionally via the database (via direct SQL or via an HTTP server)

A database buffering might not be needed at all for smaller data sets.

If editing via the database is possible,
there must be a conversion from the database to the text files before checking in.

.. _`e1`:
:e1: data ID

| The ID of data records are NOT sequentially generated from a database buffering.
| The ID is also a valid python identifier usable in code.
| The ID is unique throughout the repo.

"""

from rstdoc.dcx import mkdir, mktree, cwd, new_cwd, up_dir
from git import Repo
import os
import sys

import logging
import click

from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.ext.declarative.api import declared_attr

from sqlalchemy import *
C = Column

__version__ = '0.0.1.dev0'

@as_declarative()
class Model(object):
    """Use as base class for models:

    Define models in one file:

    >>> class User(Model):
    >>>     name = C(String)

    Have a separate files with the data:

    >>> def user(ID, name):
    >>>     #if ID in globals():
    >>>     #    raise ValueError("'%s' is duplicate"%ID)
    >>>     globals()[ID] = User(ID=ID,name=name)
    >>> user('user1',"user one")
    >>> user('user2',"user two")
    >>> del user

    Use the data:

    >>> user1.name
    'user one'
    >>> user2.name
    'user two'
    >>> User.metadata.tables['user'].columns
    ['user.ID', 'user.name']

    """

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    @declared_attr
    def __table_args__(cls):
        return {'extend_existing':True}
    ID = C(String,primary_key=True,autoincrement=False)

#TODO: move to separate file
sample_repo_tree = '''
  org
    ├ le
    │  └ le.data.yaml
           legal_name: ...
           founder: ...
           mail address: ...
           bank_account: ...
    ├ process
    │  └ SOP
    │      └ purchase.rest
    │             .. _`sop_purchase`:
    │
    │             :sop_purchase:
    │
    │             A contributor places a link under the purchase folder.
    │
    │
    │             .. include:: /_links_sphinx.rst
    ├ discussion
    │  └ topic1.rest
    │     .. _`topic_merge_delay`:
    │
    │     :topic_merge_delay:
    │
    │     Can someone take over review of |000|, as I'm busy with ...
    │
    │     .. include:: /_links_sphinx.rst
    ├ mediation
    │  └ conflict1.rest
    │     .. _`conflict_000`:
    │
    │     :conflict_000:
    │
    │     Conflicting view on |000| between ...
    │
    │     .. include:: /_links_sphinx.rst
    ├ account
    │  ├ purchase
    │  │   └ /dev/cots/ATmega328
    │  ├ model
    │  │   └ MX1
    │  │       ├ tributes.db.py
                   from econ import T
                   T(c1,212)
    │          └ bom.db.py
    │              from dev.cots.cots.db import cots
    │              from econ import bom
    │              bom(cots[0],21,1)
    │  └ 2019_ledger.db.py
    ├ market
    │  ├ ads
           └ ad1/
    │  └ orders
    │      └ orders_2019.db.py
    ├ prod
    │  └ SNxyz
    │     ├ DMR/
    │     └ tests/
    ├ tribute
    │  ├ contributor
    │      └ c1
    │         ├ assigned
    │         │   └ /pdt/000
    │         ├ log
    │         │   └ 2019.rest
    │                .. _`c1_20191101`
    │
    │                |issue1|
    │
    │                .. _`c1_20191102`
    │
    │                |issue1|
    │                It was necessary to refactor ...
    │
    │                .. include:: /_links_sphinx.rst
    │         └ responsibility
    │             └ /dev/sw/fw
  doc
    ├ index.rest
    │    .. toc::
    │
    │       tutorial.rest
    │
    │    .. include:: /_links_sphinx.rst
    └ tutorial.rest
          Example API usage
    │
    │     .. include:: /_links_sphinx.rst
  pdt
    └ 000
        ├ info.rest
        │   .. _`000`:
        │
        │   Feature
        │   =======
        │
        │   .. _`i000a`:
        │
        │   :i000a: test
        │
        │   .. include:: /_links_sphinx.rst
        ├ plan.rest
        │   .. _`p000a`:
        │
        │   :p000a: test
        │
        │   .. include:: /_links_sphinx.rst
        ├ do.rest
        │   .. _`d000a`:
        │
        │   :d000a: test
        │
        │   .. include:: /_links_sphinx.rst
        └ test.rest
        │   .. _`t000a`:
        │
        │   :t000a: test
        │
        │   .. include:: /_links_sphinx.rst
  dev
    ├ cots
    │   └ supplier.db.py
    │       import econ
            sup = econ.supplier
            sup('supXYZ','url')
    │   └ cots.db.py
    │       import econ
    │       from dev.cots.supplier.db import sup
            cots=econ.cots
    │       cots('ATmega328','/dev/cots/ATmega328',sup[0],'72328')
    │   └ ATmega328
    │       └ ATmega328.data.py
    ├ issues
    │  └ issue1.rest
    │      .. _`issue1`:
    │
    │      :issue1:
    │
    │      SW does not link to device, if ...
    │
    │      .. include:: /_links_sphinx.rst
    │  └ issue2.rest
    │      .. _`issue2`:
    │
    │      :issue2:
    │
    │      Test xyz fails.
    │
    │      .. include:: /_links_sphinx.rst
    ├ hw
    │  ├ casing
    │  │   ├ plan.rest
    │          .. _`case001`:
    │
    │          :case001:
    │
    │          According |d000a| ...
    │
    │          .. include:: /_links_sphinx.rst
    │  │   ├ scad/
    │  │   └ test
    │  │       └ stability.rest
    │              .. _`fall_test`:
    │
    │              :fall_test:
    │
    │              The casing is pushed from a table.
    │
    │              .. include:: /_links_sphinx.rst
    │  ├ pcb1
    │  │   ├ plan.rest
    │          .. _`pcb1_000`:
    │
    │          :pcb1_000:
    │
               Overview of functional units of pcb1.
    │
    │          .. include:: /_links_sphinx.rst
    │  │   ├ pcb1.sch
    │  │   └ test/
    │  └ test/
    ├ sw
    │  ├ fw
    │  │   ├ plan.rest
    │          .. _`fw_000`:
    │
    │          :fw_000:
    │
    │          To satisfy |000| these steps need to be taken.
    │
    │          .. include:: /_links_sphinx.rst
    │  │   ├ controller1/
    │  │       └ C
    │  │         └ init.c
                    // just an example
    │  │   ├ test/
    │  ├ android/
    │  │   ├ plan.rest
    │          .. _`appplan`:
    │
    │          :appplan:
    │
    │          Implementation plan satisfying |000|.
    │
    │          .. include:: /_links_sphinx.rst
    │  │   ├ app/
    │  │   ├ testapp/
    │  └ test/
    └ test/
  LICENSE-econ-1.0.txt << https://raw.githubusercontent.com/rpuntaie/econ/master/econ-1.0.rst
  contribution.rest
     .. _`how_to_contribute`:

     :how_to_contribute:

     - |general_goal|
     - pdt about plans

     .. _`micro_contribution`:

     :micro_contribution:

     An occational bug report or fix is considered as micro-contribution.
     Contributors that intend to or did spend more than a day's work on the repo should register for profit distribution.

     .. _`unassigned_issues`:

     :unassigned_issues:

     These issues are still unassigned and need new contributors.

     |issue2|

     .. include:: /_links_sphinx.rst
  /readme.rest <- readme.rst
  readme.rest
     .. _`general_goal`:

     :general_goal:

     Overview of goal and links to further information.

     .. include:: /_links_sphinx.rst
  wscript
     #vim: ft=python
     from waflib import Logs
     Logs.colors_lst['BLUE']='\x1b[01;36m'
     top='.'
     out='../build'
     def options(opt):
         opt.load('rstdoc.dcx')
     def configure(cfg):
         cfg.load('rstdoc.dcx')
     def build(bld):
         bld.load('rstdoc.dcx')
         bld.build_docs()
  index.rest
     .. toctree::

     .. vim: ft=rst

     #######
     example
     #######

     .. toctree::

           readme.rest
           contribution.rest
           org/discussion/topic1.rest
           org/mediation/conflict1.rest
           org/process/SOP/purchase.rest
           org/tribute/contributor/c1/log/2019.rest
           pdt/000/info.rest
           pdt/000/do.rest
           pdt/000/plan.rest
           pdt/000/test.rest
           doc/tutorial.rest
           dev/hw/casing/plan.rest
           dev/hw/casing/test/stability.rest
           dev/hw/pcb1/plan.rest
           dev/sw/android/plan.rest
           dev/sw/fw/plan.rest
           dev/issues/issue1.rest
           dev/issues/issue2.rest

     .. include:: /_links_sphinx.rst
  repo.py
     import click
     import sys
     import os.path
     import econ

     here = os.path.dirname(__file__)
     sys.path.add(here)

     econ.set_repo_path(here)

     if __name__ == '__main__':
        econ.cli()

'''

def init_repo(repopath):
    """
    Initialize a product repo.

        >>> repopath = 'example_repo'
        >>> init_repo(repopath)

    """
    mkdir(repopath)
    with new_cwd(repopath):
        mktree(sample_repo_tree.splitlines())
        r = Repo.init(cwd())
        r.git.add('.')
        r.git.commit('-m', 'initial commit')


def calc_tributes(repo):
    raise NotImplementedError("TODO")

repo_path = None
def set_repo_path(pth):
    global repo_path
    repo_path = pth


#https://github.com/pallets/click/master/examples/repo/repo.py
import os
import sys
import posixpath
import click
class Repo(object):

    def __init__(self, home):
        self.home = home
        self.config = {}
        self.verbose = False

    def set_config(self, key, value):
        self.config[key] = value
        if self.verbose:
            click.echo('  config[%s] = %s' % (key, value), file=sys.stderr)

    def __repr__(self):
        return '<Repo %r>' % self.home


pass_repo = click.make_pass_decorator(Repo)


@click.group()
@click.option('--repo-home', envvar='REPO_HOME', default='.repo',
              metavar='PATH', help='Changes the repository folder location.')
@click.option('--config', nargs=2, multiple=True,
              metavar='KEY VALUE', help='Overrides a config key/value pair.')
@click.option('--verbose', '-v', is_flag=True,
              help='Enables verbose mode.')
@click.version_option('1.0')
@click.pass_context
def cli(ctx, repo_home, config, verbose):
    """Repo is a command line tool that showcases how to build complex
    command line interfaces with Click.

    This tool is supposed to look like a distributed version control
    system to show how something like this can be structured.
    """
    # Create a repo object and remember it as as the context object.  From
    # this point onwards other commands can refer to it by using the
    # @pass_repo decorator.
    ctx.obj = Repo(os.path.abspath(repo_home))
    ctx.obj.verbose = verbose
    for key, value in config:
        ctx.obj.set_config(key, value)


@cli.command()
@click.argument('src')
@click.argument('dest', required=False)
@click.option('--shallow/--deep', default=False,
              help='Makes a checkout shallow or deep.  Deep by default.')
@click.option('--rev', '-r', default='HEAD',
              help='Clone a specific revision instead of HEAD.')
@pass_repo
def clone(repo, src, dest, shallow, rev):
    """Clones a repository.

    This will clone the repository at SRC into the folder DEST.  If DEST
    is not provided this will automatically use the last path component
    of SRC and create that folder.
    """
    if dest is None:
        dest = posixpath.split(src)[-1] or '.'
    click.echo('Cloning repo %s to %s' % (src, os.path.abspath(dest)))
    repo.home = dest
    if shallow:
        click.echo('Making shallow checkout')
    click.echo('Checking out revision %s' % rev)


@cli.command()
@click.confirmation_option()
@pass_repo
def delete(repo):
    """Deletes a repository.

    This will throw away the current repository.
    """
    click.echo('Destroying repo %s' % repo.home)
    click.echo('Deleted!')


@cli.command()
@click.option('--username', prompt=True,
              help='The developer\'s shown username.')
@click.option('--email', prompt='E-Mail',
              help='The developer\'s email address')
@click.password_option(help='The login password.')
@pass_repo
def setuser(repo, username, email, password):
    """Sets the user credentials.

    This will override the current user config.
    """
    repo.set_config('username', username)
    repo.set_config('email', email)
    repo.set_config('password', '*' * len(password))
    click.echo('Changed credentials.')


@cli.command()
@click.option('--message', '-m', multiple=True,
              help='The commit message.  If provided multiple times each '
              'argument gets converted into a new line.')
@click.argument('files', nargs=-1, type=click.Path())
@pass_repo
def commit(repo, files, message):
    """Commits outstanding changes.

    Commit changes to the given files into the repository.  You will need to
    "repo push" to push up your changes to other repositories.

    If a list of files is omitted, all changes reported by "repo status"
    will be committed.
    """
    if not message:
        marker = '# Files to be committed:'
        hint = ['', '', marker, '#']
        for file in files:
            hint.append('#   U %s' % file)
        message = click.edit('\n'.join(hint))
        if message is None:
            click.echo('Aborted!')
            return
        msg = message.split(marker)[0].rstrip()
        if not msg:
            click.echo('Aborted! Empty commit message')
            return
    else:
        msg = '\n'.join(message)
    click.echo('Files to be committed: %s' % (files,))
    click.echo('Commit message:\n' + msg)


@cli.command(short_help='Copies files.')
@click.option('--force', is_flag=True,
              help='forcibly copy over an existing managed file')
@click.argument('src', nargs=-1, type=click.Path())
@click.argument('dst', type=click.Path())
@pass_repo
def copy(repo, src, dst, force):
    """Copies one or multiple files to a new location.  This copies all
    files from SRC to DST.
    """
    for fn in src:
        click.echo('Copy from %s -> %s' % (fn, dst))
