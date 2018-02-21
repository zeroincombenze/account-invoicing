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

Invoices created from picking grouped by product
================================================

This module allows you to group invoices generated from pickings by product
or by product category.

Installation
------------




Configuration
-------------




Usage
-----







=====

This is possible by selecting the related option in the wizard used
for creating draft invoices.

Example

Created the following pickings:

1. picking_1 - partner_1
    1. product_A - category_1
    2. product_B - category_2
2. picking_2 - partner_2
    1. product_C - category_2
    2. product_D - category_3
3. picking_3 - partner_1
    1. product_C - category_2
    2. product_D - category_3
    3. product_A - category_1

Selecting option 'Group by product category' I get the following invoices:

1. invoice_1 - partner_1
    1. product_A - category_1 --> picking_1
    2. product_A - category_1 --> picking_3
2. invoice_2 - partner_1
    1. product_B - category_2 --> picking_1
    2. product_C - category_2 --> picking_3
3. invoice_3 - partner_1
    1. product_D - category_3 --> picking_3
4. invoice_4 - partner_2
    1. product_C - category_2 --> picking_2
5. invoice_5 - partner_2
    1. product_D - category_3 --> picking_2

On the contrary if I select option 'Group by product' I get the following
invoices:

1. invoice_1 - partner_1
    1. product_A - category_1 --> picking_1
    2. product_A - category_1 --> picking_3
2. invoice_2 - partner_1
    1. product_B - category_2 --> picking_1
3. invoice_3 - partner_1
    1. product_C - category_2 --> picking_3
4. invoice_4 - partner_1
    1. product_D - category_3 --> picking_3
5. invoice_5 - partner_2
    1. product_C - category_2 --> picking_2
6. invoice_6 - partner_2
    1. product_D - category_3 --> picking_2

=====

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/95/8.0

Known issues / Roadmap
----------------------




Bug Tracker
-----------





Bugs are tracked on `GitHub Issues
<https://github.com/OCA/account_invoicing/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed feedback.

Credits
-------









### Contributors





* Alex Comba <alex.comba@agilebg.com>

### Funders

### Maintainer








.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.

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
