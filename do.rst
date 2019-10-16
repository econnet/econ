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
The contributors correspond to the econ's intent.
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

contributors
    nodes above.

econs
    nodes below.

partners
    Sideward; nodes linked via interactions (econs)

siblings
    Sideward, nodes linked via contributors


.. _`docontributor`:

:contributor:

If one depends on a resource, one likes to control that resource.
Society has developed the concept of ownership for that.
Society protects ownership to avoid the stress of constant fights for the resource.
This works well for things.

But the idea to control people means that some people get controlled.
Controlling people is against the principle of equality.

In an econ, owner is replaced by **contributor**
to avoid conflicts with existing legal definitions.

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

.. _`docontrol`:

In an econ, control means decision making.
Decisions need information.

A general principle is: *Those decide that have most information*.
E.g. developers decide about their parts in the product.
If others are concerned, they are consulted and informed about the decision.

If more are concerned, decisions are democratic, either

- by direct vote or
- through elected or otherwise agreed delegation

A decision needs a propose. The proposal is worked out by one person.

There is **no boss**, neither in an econ, nor in an econ lattice.

Someone initiating or coordinating does not decide, but mediates an agreement.
The less coordination needed, the better.

There can be separate econs in the lattice that care about performance monitoring.
Decisions from the gathered information are made by those concerned,
which can be the whole econ lattice.


.. _`dolegal`:

:legal:

The econ rules are not specific to a government.
They need to be compatible (legal) with all involved governments.
The fact that econ lattice consists of econs,
allows each econ to be in a different government.

The major interest of a government is taxes.

- Selling the product adds the `VAT`_ to the final product
  if required by the government
- Taxing of the econ is according location of the econ.
  So profit taxation of a product econ lattice
  spreads over more governments
  with one as a special case.

The government of the bottom econ provides the jurisdiction for potential disputes.
That is not an interest of the government,
but rather of the econ, creditors or product customers.

The bottom econ should be

- a `legal entity`_ (LE)
- not a natural person

The `LE`_ **does not have employees**.

Founding the `LE`_ produces

- ownership of the `LE`_ according usual legislation
- does not produce product ownership

Only subsequent product-relevant work produces product ownership.
The **econ contract** obliges the `LE`_ to care to

- *attribute* to econs the *contribution* to the product version (tributes)
- *distribute* profit proportionally

Profit can be kept in the `LE`_

- as a loan granted to the `LE`_ (bond)
- as `liable capital`_ for `limited liability`_

An initial `LE`_ cannot be a `limited liability`_ `LE`_,
unless the founders forward `liable capital`_, e.g. as perpetual `bonds`_.
Here `liable capital`_ is used to emphasize its purpose as risk capital without defining ownership.
It is better to make the `LE`_ to a `limited liability`_ `LE`_
only before selling the product, because then

- the product owners are known through work done
- the `liable capital`_ can be shared between all contributors
- `liable capital`_ overlaps with outside economy's definition of `equity`_,
  but we keep the distinction by continuing to use `liable capital`_.
- there is no need for `limited liability`_ before actually interacting with the outside economy

The `LE`_ takes the responsibility for the product according `limited liability`_.

The econs working on product parts have their own responsibility to interact with their government,
whether the same or different.
Concentrating the effort of government interaction to saves effort

- is up to the econs
- not product specific and therefore
- outside the `LE`_

.. _`docontent`:

:content:

The product information is mapped to more repos according content encapsulation,
with one being a special case.

- product governance (values, rules, monitoring, contracts, ...) (this repo)
- product financing (expenses, income, `liabilities`_, ...)
- product development (hardware, software, test, development docs, usage docs, license, ...)
- product production (`SOP`_'s, `DMR`_, `DHF`_, ...)
- product marketing

The product-related effort to create the content is called **tribute**.

All repos have *tribute* information for the repo.
The tribute records are stored with the content created,
because the econ contract demands profit distribution proportional to tribute.

The *contributors* have access to all information.
It allows them

- to do their work (development and production)
- to check the fairness (tribute, financing and marketing)
- interact (governance)

The repos are a communication channel.
Even if delegation reduces the actual need to access certain repos,
communication to the delegation is based on the information.

The content is linked across repos.

*Non-contributors*

- get access to the development repo(s) according |infoopenness| value
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

Only product parts that are developed internally require work and thus an econ.
Product parts from the outside economy
require work to select the right item and supplier,
but there is no need for a separate econ.

The `LE`_ exists during the `product lifetime`_,
from development to recycling.

A new product has a new `LE`_ and a new econ lattice,
as every econ corresponds to a product work part.

A new version of a product has the same `LE`_,
but possibly a changed econ lattice.

The tribute depends on the *product version*.
If a product gets modified, some work might be replaced.
Then the according tribute becomes smaller with the new product version.
Tribute vanishes
if (past) contributions stop to be *relevant* for the currently sold product version.

If new people take over the development, their effort will produce income for them in future product versions.
Previous developers will still get their profit share on relevant work (tribute).
Previous developers can still check for fairness.

.. _`dolicense`:

:license:

The license cannot be GPL,
because selling of the product demands profit distribution according tribute.

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

In the econ lattice there in no employment according outside economy,
as a separate labor market produces inequality,
because the actual value of work is not forwarded to the worker.

Not using employment is the major difference
between the econ lattice and traditional companies.
Profit sharing or advanced payments are usual practices between partners.

The actual value of internal work is only determined by the success of the product on the market.
To stop inequality from growing, it is essential

- *not to give a price to product-internal work using an outside currency*

The outside price of work is decoupled from the actual value of work
and cannot be a reference.

The outside economy is not uniform.
Every country has its own work price.
This idea is extended:

- product development is its own encapsulation and
- has its *own internal unit* (**tribute unit**)

The *tribute unit* is described (not valued)
based on work that is frequent in the product development.
The internal work unit is not yet priced by the product sales to the outside economy.

Producing a product still involves different kinds of work.
When quantifying work internally,

- the kind of work has more weight
- than the person who does the work

Both aspects can be considered with a `performance`_ factor (`p`),
that maps the *tribute unit* to the **work unit** based on

- a specific work done by
- a specific person using
- a specific personal tool

`p` includes the tools required to perform the work.
The person who needs a computer or car to do its work
gets a `p` that accounts for these tools.

Work units can also be results, e.g.

- products sold
- customers acquired
- contributors recruited
- ...

The outside economy has a `minimum wage`_.
Work turning out to be less valuable than the outside economy's `minimum wage`_,

- is revalued or
- automated

Automation is important

- to increase the performance factor (`p`)
- to keep the final product competitive and
- to produce profit for contributors (to allow them to work on new products)

.. _`dotribute`:

:tribute:

Tributes are internal records for product-related efforts.

Product-related effort is not measure with an external currency,
because the product value in the market is yet unknown.

The tribute record consists of:

- quantity
- work unit

Latest when pricing the product for the outside market,
the internal work units are considered

- in the product price
- in relating the work units to a **tribute unit**

In this process temporary and acceptable conversion factors to the outside work price are used.

How and how precise work is recorded needs to be agreed upon.
There should be an effort in the fair attribution of work,
but how much is democratically decided by the contributors.
Micro-recording and micro-payments produce more effort than value
and thus produce deficit.

Tributes only consider **relevant work** for the currently sold **product version**,

- either current work or
- work in the past

*Relevancy* is necessary to make it fit to reality.

*Relevancy* requires the tributes to be associated with product parts.
When the part is replaced that work becomes irrelevant.
For `diversification`_ people should contribute to more parts.

*Relevancy* does not only refer to technical development of the product,
but to all aspect to make the product successful on the market.
E.g. it includes marketing efforts.

Work that is not related to the specific product is its own product that
comes from the outside economy.

The output from more econs is used in a integrating econ.
Such an integrating econ has as contributors

- direct top level econs (integrators) and
- inner econs

Final tributes are calculated per product version,
as contributions change between product versions.
Product version tributes of people (top nodes)
are calculated via the **product lattices**, 
traversing the inner nodes.

The product repo(s) have a "tribute" file updated before fixing the version.
The profit distribution is done

- separately for every product sold
- based on the tribute of the product version

Tributes document the product ownership.
Tributes produce delayed income in an outside currency when the product is sold.

Tributes can be

- donated
- inherited
- used as pledge for a loan,
  if accepted by a creditor
- basically also sold,
  but a price is probably hard to agree upon,
  since the actual value in the outside economy is unknown

.. _`dofinancing`:

:financing:

The major costs for technical products are development.
If developers can afford to wait for the revenue via sale of the finished product,
there is not much money needed.

Before actual income, the money can come from

- bonds
- donations

Financing through `stock`_ cannot be used, because

- ownership is defined by work (tributes)
- not via capital

Money cannot be used to change ownership of the `LE`_.
Bonds don't change ownership.
The profit through ownership is higher than
the interest on bonds. Also,
the interest on bonds can be considered in the pricing of the product.

Money can change ownership indirectly:
If a worker is payed

- to produce tribute and
- to forward tribute to the paying party

To keep workers from engaging in such relations

- the prospect of bigger profit if not directly payed should help
- else regular profit advances to the worker can be granted by the `LE`_

The `balance sheet`_ balances

- `assets` versus
- `liabilities`_ and `liable capital`_

`retained earings`_ per default becomes `liable capital`_.
unless distributed according tributes.
The owners can then re-invested it as `bonds`.

The interest on loans varies (bonds, profit advances),
but is at least as high as inflation of the outside economy.

The owners have control over the financial channels (e.g. bank account),
but it is normally delegated to buyers and sellers,
which register the financial flows in the repo,
for everybody to check,
with additional checks from specialized fairness checkers.

.. _`doeconvalue`:

:econ value:

The value of an econ lattice is

- the product econ lattice (internal structure)
- the product work shares defining ownership on product sales (tributes)
- the product customers (external structure)

There is no need to calculate the full value of an econ lattice,
because it cannot be sold as a whole.
An interested buyer would need to agree on a price for every contributor's tribute separately.

The product developers can freely regroup for other products, also concurrently.
The developers of a product cannot be bought without employing everybody,
but that would mean control from the employer,
which would reduce personal freedom and profit.
It is unlikely that all people involved in the product development would agree to that.

The customers cannot be bought other than through the owners of the product.

.. _`doprofit`:

:profit:

`LE`_ period: profit = income - expenses.

Expenses are only related to the product.
Investment in big machines not related exclusively to the product,
need to be handled by a separate `LE`_.

Working tools like the computer or a car belong to the person (top econ).
They are considered in the performance factor (`p`).

*Work is not an expense*,
because the profit becomes the reward for the work.

Profit from the product sales of the period is attributed to owners for every product version.
This capital attribution

- is a result of ownership and
- does not produce ownership change.

The profit

- first belongs to the `LE`_ (`retained earnings`_)
- is forwarded to the owners according tributes
- can be reinvested as `ponds`_

Profit maximization of the `LE`_
means maximizing the profit of each member.
Every member helps each other to maximize their profit.
This kind of profit maximization is morally good,
unless it damages to the outside world.

.. _`doadvances`:

:advances:

Work

- produces ownership and
- delayed profit
- not immediate profit

Profit advances constitute regular payments to owners, currently contributing or not,
to allow them to use products of the outside economy already before revenue from sales of the product.

The `LE`_ corresponding to a product accepts work shares as a pledge for profit advances.

Advances are

- loans of the `LE`_ to the contributor
- are payed back using profit at the end of the period or forwarded to the next period
- not reward for work (not wages)

Advances must be payed back to the `LE`_,
if a contributor stops contributing
before the product is finished, i.e. ready for the market.

If the `LE`_ gets bankrupt, then profit advances might be unrecoverable.

The risk is

- taken by creditors if financed by bonds.
- considered via the interest rate on the bonds.

The amount of profit advances is based on

- previous profits or
- expected profit, if the money is available

Advances are a compromise for

- risk of third party take-over of contributors
- risk of diminished or no advances
- risk of abandonment of a potentially profitable product

  As development is public the results might be reused by someone even after abandonment.
  Since the licence demands distribution of profit according tributes,
  there is a slight change that a fair other econ lattice continues later.

The `LE`_ agrees with the contributors whether to pay advances.
The amount of advances is agreed separately with every contributor.
The information is public.


.. _`LE`: `legal entity`_
.. _`legal entity`: https://en.wikipedia.org/wiki/Legal_person
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
.. _`bonds`: https://en.wikipedia.org/wiki/Bond_(finance)
.. _`liable capital`: https://en.wikipedia.org/wiki/Equity_(finance)#Owner's_equity
.. _`equity`: https://en.wikipedia.org/wiki/Equity_(finance)
.. _ `assets`: https://en.wikipedia.org/wiki/Asset
.. _`liabilities`: https://en.wikipedia.org/wiki/Liability_(financial_accounting)
.. _`retained earings`: https://en.wikipedia.org/wiki/Retained_earnings
.. _`stock`: https://en.wikipedia.org/wiki/Stock
