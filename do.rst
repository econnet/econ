.. encoding: utf-8
.. vim: syntax=rst

Governance
==========

.. epigraph:: A society is not democratic unless in all interactions.


.. _`doecon`:

:econ:
economic node, interaction node, work node

The name *econ* stands for

- the organizational topology, but especially
- for the ethical values associated with the interactions in this topology.

The perspective to economy from a person corresponds to an **inversion** of the economic hierarchy.
The person is at the top and interactions are its interactions, i.e. belonging to it.

Econs are cohesions of interactions.
Interaction between econs are new econs.

Econs form a mathematical `lattice`_.
An econ corresponds to a node in a `concept lattice`_.
The members of an econ correspond to the node's intent.
*Intent* in `concept lattice`_ are the attributes,
but the English sense of purpose to produce content fits well here.

Maximizing cohesion and minimizing coupling is a way to reduce interactions, i.e. work.
The further down the lattice the less interaction.
The bottom *econ* does the interaction with the outside market via a tested product.

Interaction is done via content.
An econ member is a content contributor.
A content item is a product part.

Content encapsulations map to organizational encapsulations: econs.

- product (coordination)     ->      bottom econ
- product parts              ->      inner econs
- elementary product part    ->      top econ

An econ stays even if the contributing people (team) change.
A person can contribute to more econs.

.. TODO diagram

With a `concept lattice`_ in mind,
these names are used for relations of econs

members
    nodes above.

econs
    nodes below.

partners
    Sideward; nodes linked via interactions (econs)

siblings
    Sideward, nodes linked via members


.. _`doowner`:

:owner:

If one depends on a resource, one likes to control that resource.
Society has developed the concept of ownership for that.
Society protects ownership to avoid the stress of constant fights for the resource.
This works well for things.

But the idea to control people means that some people get controlled.
Controlling people is against the principle of equality.
Also money must not be used to control people.

The outside economy allows ownership and control on companies.
In an econ, ownership and control is

- NOT on people, but
- on content (product part) and
- on the value of the product part according contribution.

People engage in econs because of

- common interest and/or
- prospect of profit when selling the product

There is organizational effort associated with the formation of an econ lattice.
People need to

- find each other
- get to know each other
- get the same understanding of the process (functioning well together)
- map the product work parts to econs
- create communication channels (repos, html sites, chat channels, ...)

The formation effort is associated with the bottom econ.
In the bottom econ

- the product initiator and/or coordinator can record contributions
- another member who recruits a new member can also record his effort there

Owner means co-owner with single-owner as a special case.

- Membership is yes/now.
- Ownership quantifies to share.

.. _`docontrol`:

In an econ, control means decision making.
Decisions need information.

A general principle is: *Those decide that have most information*.
E.g. developers decide about their parts in the product.
If others are concerned, they are consulted and informed about the decision.

There can be separate econs in the lattice that care about performance monitoring.
Decisions from the gathered information need to be made by those concerned,
which can be the whole econ lattice.

If more are concerned, decisions are democratic, either

- by direct vote or
- through elected or otherwise agreed delegation

There is **no boss**, neither in an econ, nor in an econ lattice.

Someone initiating or coordinating does not decide, but mediates an agreement.
The less coordination needed, the better.


.. _`dogovernment`:

:government:

.. How to make econ members profit from the ownership protection of society's laws?

The only interest of the government is taxes.

- Selling adds the `VAT`_ to the final product as required by the government
- Tax of econ is according location of econ.
  So profit taxation spreads over more governments
  with one as a special case.

If there are disputes, a specific jurisdiction needs to be used.
That is not an interest of the government,
but rather of the econ, creditors or product customers.

The jurisdiction is per product, which is represented by the bottom econ.
The government of the bottom econ provides the jurisdiction.

Governments have the concept of `limited liability`_.
The bottom econ should be a `legal entity`_ with
`limited liability`_ (LLE) according used jurisdiction.
The `LLE`_ is

- per product
- does not have employees

The `LLE`_ does not own

- the product nor
- the bank account
- nor anything else related to the product

Initial capital coming from those founding the `LLE`_
are loans to the `LLE`_ and don't produce ownership.

Founding an `LLE`_ does not produce ownership.

Only subsequent working on the product produces ownership,
independent of whether

- founders or
- non-founders

The `LLE`_'s does not have profit. Every income from product sale is a loan granted to the `LLE`_.

The `LLE`_

- records the ownership and
- distributes the product profit
- takes the responsibility for the product according `limited liability`_

The econs working on product parts have their own responsibility to interact with their government,
whether the same or different.
Concentrating the effort of government interaction to saves effort

- is up to the econs
- not product specific and therefore
- outside the `LLE`_

.. _`docontent`:

:content:

The product information is mapped to more repos according content encapsulation,
with one being a special case.

- product governance (values, rules, monitoring, contracts, ...) (this repo)
- product financing (expenses, income, liabilities, ...)
- product development (hardware, software, test, development docs, usage docs, license, ...)
- product production (`SOP`_'s, `DMR`_, `DHF`_, ...)
- product marketing

All repos have *work share* information for the repo.
The work share needs to be stored with the content created,
because the license demands profit distribution according work share.

The *members* are owners and have access to all information.
It allows them

- to do their work (development and production)
- to check the fairness (work share's, financing and marketing)
- interact (governance)

The repos are a communication channel.
Even if delegation reduces the actual need to access certain repos,
communication to the delegation needs to be able to link to the information.

The content is linked across repos.

*Non-members*

- get access to the development repo(s) according |informopenness| value
- do not get access to information about the organization of the development

.. _`doproduct`:

:product:

An econ does not provide work as service to an outside company to produce a product
without also profiting from the sales of the product.

The econ lattice

- produces a finished (technical) product
- maintains and improves the product
- helps in using the product
- possibly recycles the product

The product is the output item to the outside economy.
There are also input items from the outside economy.
Work refers only to the conversion of input items to the product.

Only product parts that are developed internally need work and thus an econ.
Product parts from the outside economy
need work to select the right version and supplier,
but there is no need for a separate econ.

The `LLE`_ exists during the `product lifetime`_,
from development to recycling.

A new product has a new `LLE`_ and a new econ lattice,
as every econ corresponds to a product work part.

A new version of a product has the same `LLE`_,
but possibly a changed econ lattice.

The income for a product version is distributed according the *product version*'s ownership.

If a product gets modified, some work might be replaced.
Then the according worker's share becomes smaller with the new product version.
Ownership vanishes
if (past) contributions stop to be *relevant* for the currently sold product version.

If new people take over the development, their effort will produce income for them in future product versions.
Previous developers will still get their profit share on relevant work.
Previous developers can still check for fairness.

.. _`dolicense`:

:license:

The license cannot be GPL,
because selling of the product demands profit distribution according work shares.

The license should be compatible with GPL
as existing open source software/hardware is the basis.

Software created along the product development,
but not directly linked to the product
should be released as GPL.
These efforts will not be considered in the product profit distribution,
but simplifies the product profit distribution,
because different products do not get linked by such common (software) infrastructure.

Finance
=======

.. _`dowork`:

:work:

In the econ lattice

- **work investment produces ownership**
- **money investment does not produce ownership**

.. note:: Work produces ownership.

    There in no employment according outside economy,
    as that produces inequality,
    because the actual value of work is not forwarded to the worker.

    Not using employment is the major difference
    between the econ lattice and tradictional companies.

The actual value of internal work is only determined by the success of the product on the market.
To stop inequality from growing, it is essential

- *not to give a price to work using an outside currency*

because the outside price of work is completely decoupled from the actual value of work.

The outside economy is not uniform.
Every country has its own work price.
Econ extends on this idea:

- an econ lattice for a product is its own encapsulation and
- needs to have its *own internal work unit*

The *internal work unit* needs to be described (not valued)
based on work that is frequent in the product development.
The internal work unit is not yet priced by the product sales to the outside economy.

Producing a product still involves different kinds of work.
When quantifying work internally,

- the kind of work has more weight
- than the person who does the work

Both aspects can be considered with a `performance`_ factor (`p`),
that maps the internal work unit to the work unit for

- a specific work done by
- a specific person using
- a specific personal tool

The *work value* includes the tools needed to perform the work.
The person who needs a computer or car to do its work
gets a work value that accounts for these tools.

The outside economy has a `minimum wage`_.
Work turning out to be less valuable than the outside economy's `minimum wage`_,
needs to be

- revalued or
- automated

Automation is important

- to increase the internal work value
- to keep the final product competitive and
- to produce profit for members (to allow them to work on new products)

.. _`doworkshare`:

:work share:

Internal work records are internal capital: work shares.

Work does not need to be measured in time.
Work can be measured by result, e.g.

- by products sold
- by customers acquired
- by members recruited
- ...

The work shares are recorded in (separate) internal units.
When pricing the product for the outside market,
the internal work measures can to be considered
with temporary and acceptable conversion factors to the outside work price.

How and how precise work is recorded needs to be agreed upon.
There should be an effort in the fair attribution of work,
but how much is up to the members.
Micro-recording and micro-payments produce more effort than value
and thus produce deficit.

Work shares can be

- donated
- inherited
- used as pledge for a loan,
  if accepted by a creditor
- basically also sold,
  but a price is probably hard to agree upon,
  since the actual value in the outside economy is unknown

**Work shares** document the ownership.

Work shares produce delayed income in an outside currency,
when the product of the work is sold.

Only work is considered that is **relevant** for the currently sold **product version**,

- either current work or
- work in the past

**Relevant** is necessary to make it fit to reality.

**Relevant work** requires the work value to be associated with product parts.
When the part is replaced that work becomes irrelevant.
For `diversification`_ people should contribute to more parts.

The output from more econs is used in a integrating econ.
Such an integrating econ has

- direct top level econs (integrators) and
- inner econs

as owners.

Ownership share is product ownership share.
Product ownership shares of people (top nodes) are calculated
via the **product lattices** traversing the inner nodes.
This calculation is done for every product version,
as contributions change between product versions.

The profit distribution is done differently for every product version sold.

The work share is no single paper or data point, but

- calculated through an algorithm that uses
- data recorded throughout the product lattice
- for a product version

Work that is not related to the specific product is its own product that
comes from the outside economy.

.. _`dofinancing`:

:financing:

The major costs for technical products are development.
If developers can afford to wait for the revenue via sale of the finished product,
there is not much money needed.

Before actual income, the money can come from

- loans
- donations

Financing through loans follows from defining ownership via work share.
Money cannot be used to change ownership of an econ lattice.
There is *no owner's equity* in the `balance sheet`_.
Ownership is only defined by work share,
which is calculated from work share data
for every product version.

Money can change ownership indirectly:
If someone is payed by a third party
in exchange of forwarding its work shares to that party.

To keep workers from engaging in such relations

- the prospect of bigger profit if not directly payed should help
- else regular loans to the worker can be granted by the econ lattice, financed by loans.

Loans don't change ownership.
The profit through ownership is higher than
the interest on loans. Also,
the interest on loans can be considered in the pricing of the product.

- Founders, non-founders, owners or non-owners can give loans to the `LLE`_.
- The `LLE`_ can give loans to the owners as profit advances.

The `balance sheet`_ thus balances

- only assets vs liabilities
- instead of assets vs liabilities and owner's equity

The interest on loans varies, but is at least as high as inflation of the outside economy.

The owners have control over the financial channels (e.g. bank account),
but it is normally delegated to buyers and sellers,
which register the financial flows in the repo,
for everybody to check,
with additional checks from specialized fairness checkers.

.. _`doeconvalue`:

:econ value:

The value of an econ lattice is

- the product econ lattice (internal structure)
- the product work shares defining ownership on product sales
- the product customers (external structure)

There is no need to calculate the full value of an econ lattice,
because it cannot be sold as a whole.
An interested buyer would have to contact every contributor
and agree on a price for its work shares separately.

The product developers can freely regroup for other products, also concurrently.
The developers of a product cannot be bought without employing everybody,
but that would mean control from the employer,
which would reduce personal freedom and profit.
It is unlikely that all people involved in the product development would agree to that.

The customers cannot be bought other than through the owners of the product.

.. _`doprofit`:

:profit:

Period profit is income - expenses of the period.

Expenses are only related to the product.
Investment in big machines not related exclusively to the product,
need to be handled by a separate econ lattice.

Working tools like the computer or a car belong to the person (top econ).
They are considered in the internal work value.

*Work is not an expense*,
because the profit becomes the reward for the work.

Profit from the product sales of the period is attributed to owners for every product version.
This capital attribution

- is a result of ownership and
- does not produce ownership change.

The profit belongs to the owner not to the `LLE`_.
Some profit can be kept in the `LLE`_
as loan from the owners to it `LLE`_,
if owner and `LLE`_ agree to do so.
It needs to be a *loan* instead of *owner's equity*,
because ownership is only reach via work and not money.

Profit maximization of the `LLE`_
means maximizing the profit of each member.
Every member helps each other to maximize their profit.
This kind of profit maximization is morally good,
unless it damages to the outside world.

.. _`doadvances`:

:advances:

Work

- produces ownership and
- delayed profit, not immediate profit

Profit advances constitute regular payments to owners, currently contributing or not,
to allow them to use products of the outside economy already before revenue from sales of the product.

The `LLE`_ corresponding to a product econ accepts work shares as a pledge for loans.

Advances are loans of the `LLE`_ to the owners
and are balanced with profit at the end of the period.
If the econ does not make profit, profit advances are liabilities forwarded to the next period.
If the `LLE`_ gets bankrupt, then advances are lost.
The risk is take by the `LLE`_.

The amount of profit advances is based on previous profits,
or if the money is available, based on expected profit.

Advances are a compromise of the owners between

- risk of third party take-over of developers
- risk of diminished or no advances
- risk of abandonment of a potentially profitable product

  As development is public the results might be reused by someone even after abandonment.
  Since the licence demands distribution of profit according work share,
  there is a slight change that a fair other econ lattice builds around the project later.

As profit, also risk must be distributed between owners proportional to ownership.
This means that advances, if any, must be given to all owners proportional to ownership.

The owners decide together the amount of advances to pay, and whether at all.

If advances are payed, there is a minimum, e.g. for someone new at an econ,
which, having no ownership yet, would otherwise not get payed.
As advances are loans, this is not money for free.
But if the `LLE`_ gets bankrupt the money is lost.
The extra risk is taken indirectly by the current owners.

.. _`legal entity`: https://en.wikipedia.org/wiki/Legal_person
.. _`LLE`: `limited liability`_
.. _`limited liability`: https://en.wikipedia.org/wiki/Limited_liability_company
.. _`lattice`: https://en.wikipedia.org/wiki/Lattice_(order)
.. _`concept lattice`: https://en.wikipedia.org/wiki/Formal_concept_analysis
.. _`product lifetime`: https://en.wikipedia.org/wiki/Product_lifetime
.. _`evolutionary systems`: https://rolandpuntaier.blogspot.com/2019/01/evolution.html
.. _`minimum wage`: https://en.wikipedia.org/wiki/Minimum_wage
.. _`performance`: https://www.investopedia.com/terms/f/financialperformance.asp
.. _`balance sheet`: https://en.wikipedia.org/wiki/Balance_sheet
.. _`DMR`: https://en.wikipedia.org/wiki/Device_Master_Record
.. _`DHF`: https://en.wikipedia.org/wiki/Design_history_file
.. _`SOP`: https://en.wikipedia.org/wiki/Standard_operating_procedure
.. _`diversification`: https://en.wikipedia.org/wiki/Diversification_(finance)
.. _`VAT`: https://en.wikipedia.org/wiki/Value-added_tax
