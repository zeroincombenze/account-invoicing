[![Build Status](https://travis-ci.org/zeroincombenze/account-invoicing.svg?branch=8.0)](https://travis-ci.org/zeroincombenze/account-invoicing)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/account-invoicing/badge.svg?branch=8.0)](https://coveralls.io/github/zeroincombenze/account-invoicing?branch=8.0)
[![codecov](https://codecov.io/gh/zeroincombenze/account-invoicing/branch/8.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/account-invoicing/branch/8.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-8.svg)](https://github.com/OCA/account-invoicing/tree/8.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-8.svg)](http://wiki.zeroincombenze.org/en/Odoo/8.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-8.svg)](http://wiki.zeroincombenze.org/en/Odoo/8.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-8.svg)](http://erp8.zeroincombenze.it)
































[![en](http://www.shs-av.com/wp-content/en_US.png)](http://wiki.zeroincombenze.org/it/Odoo/7.0/man)

.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

Stock Picking Invoicing Unified
===============================

Odoo allows to select several pickings and click on *Create Draft Invoices*
option to create the corresponding invoice(s)/refund(s). If you have
selected several partners and you have checked the option *Group by partner*,
it will create a single invoice or refund per partner.

But it only takes into account the first picking for selecting the type of the
invoice you are going to create (customer/supplier invoice/refund), mixing all
the lines on it. And not only that: if you have returned pickings, the returned
quantities are summed to the rest, instead of decreasing the amount to invoice,
which is the common practise when you have some returns.

This module fixes this problem, allowing to invoice them all together:
if you have delivered and received goods for the same customer and you
have checked the option *Group by partner*, you will have a single
invoice with the goods delivered and received and the quantities of the
goods received will be negative. So it will avoid you to send both an
invoice and a refund to your customer and have to reconciliate them to
compute the good residual amount.

Installation
------------




Configuration
-------------




Usage
-----







=====

* Select several pickings from any of the menus that allows it (
  *Warehouse > All Operations* and click on any of the lines,
  *Purchases > Invoice Control > On Incoming Shipments*, etc).
* Click on *More > Create Draft Invoices*.
* In the resulting dialog, the proper invoices types that are going to be
  created are computed, and you have to select the journals for that types.
* Click on *Create* button, and the invoices will be correctly created.
* The lines of pickings that are not of the greater picking type are created
  with negative price unit.

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/95/8.0

Known issues / Roadmap
----------------------





* Generated invoices are all seen with the supplier invoice form view, independently of 
  its type.
* Add tests

Bug Tracker
-----------





Bugs are tracked on `GitHub Issues <https://github.com/OCA/account-invoicing/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed feedback
`here <https://github.com/OCA/account-invoicing/issues/new?body=module:%20
stock_picking_invoicing_unified%0Aversion:%20
8.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.


Credits
-------









### Contributors




* Ainara Galdona <ainaragaldona@avanzosc.es>
* Pedro M. Baeza <pedro.baeza@serviciobaeza.com>

### Funders

### Maintainer








.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.

[//]: # (copyright)

----

**Odoo** is a trademark of [Odoo S.A.](https://www.odoo.com/) (formerly OpenERP, formerly TinyERP)

**OCA**, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

**zeroincombenze®** is a trademark of [SHS-AV s.r.l.](http://www.shs-av.com/)
which distributes and promotes **Odoo** ready-to-use on its own cloud infrastructure.
[Zeroincombenze® distribution](http://wiki.zeroincombenze.org/en/Odoo)
is mainly designed for Italian law and markeplace.
Everytime, every Odoo DB and customized code can be deployed on local server too.

[//]: # (end copyright)

[//]: # (addons)

[//]: # (end addons)

[![chat with us](https://www.shs-av.com/wp-content/chat_with_us.gif)](https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b)
