"""
Automates activities around an econ repo.

The repo layout is developed along,
starting from the initial idea.

Product version branch::


  repo
   ├ tribute
   │  ├ todo_unassigned
   │  │   └ symlinked content
   │  ├ contributor
   │  │   └ contributor1
   │  │       ├ todo
   │  │       │   └ symlinked content
   │  │       ├ discussions
   │  │       │   └ symlinked content
   │  │       ├ logs
   │  │       │   └ 2019.rest
   │  │       └ contributions
   │  │           └ symlinked content
   │  └ kind
   │      └ kind1
   │          └ symlinked content
   ├ doc
   │  ├ index.rest
   │  └ tutorial.rest
   ├ pdt
   │  └ 000
   │      ├ info.rest
   │      ├ plan.rest
   │      ├ do.rest
   │      └ test.rest
   ├ dev
   │  ├ bugs
   │  │  └ issue1.rest
   │  ├ hw
   │  │  ├ part1
   │  │  │   ├ plan.rest
   │  │  │   ├ bom.txt
   │  │  │   ├ model.scad
   │  │  │   └ test/
   │  │  ├ pcb1
   │  │  │   ├ plan.rest
   │  │  │   ├ pcb1.sch
   │  │  │   └ test/
   │  │  └ test/
   │  ├ sw
   │  │  ├ fw
   │  │  │   ├ plan.rest
   │  │  │   ├ controller1/
   │  │  │   ├ test/
   │  │  ├ android/
   │  │  │   ├ plan.rest
   │  │  │   ├ app/
   │  │  │   ├ testapp/
   │  │  └ test/
   │  └ test/
   ├ LICENSE-econ-1.0.txt
   └ readme.rst

LE branch::

  repo
   ├ le
   │  └ data.yaml
   ├ tribute
   │  └ calc_tributes.py
   ├ process
   │  └ SOP
   │     └ procurement.rest
   ├ contributor
   │  └ contributor1
   │     └ orders
   │         └ cots_item
   ├ mediation
   │  └ issue1.rest
   ├ account
   │  ├ internal_orders
   │  │  └ symlinked cots_item
   │  ├ product_version
   │  │  └ version1
   │  │      └ tributes.txt
   │  └ 2019_ledger.journal.pgp
   ├ market
   │  ├ ads
   │  └ orders
   ├ prod
   │  └ SNxyz
   │     ├ DMR
   │     └ tests
   ├ LICENSE-econ-1.0.txt
   └ readme.rst


"""


# todo
