[![Build Status](https://travis-ci.org/zeroincombenze/account-invoicing.svg?branch=9.0)](https://travis-ci.org/zeroincombenze/account-invoicing)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/account-invoicing/badge.svg?branch=9.0)](https://coveralls.io/github/zeroincombenze/account-invoicing?branch=9.0)
[![codecov](https://codecov.io/gh/zeroincombenze/account-invoicing/branch/9.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/account-invoicing/branch/9.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-9.svg)](https://github.com/OCA/account-invoicing/tree/9.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-9.svg)](http://wiki.zeroincombenze.org/en/Odoo/9.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-9.svg)](http://wiki.zeroincombenze.org/en/Odoo/9.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-9.svg)](http://erp9.zeroincombenze.it)


[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
================================================================
   :alt: License: AGPL-3

Refund Returned Pickings from Sales Orders

This module extends the functionality of sales orders to support marking some
returned pickings as "To refund in Sale Order" and to allow you to create
invoices deducting the products that are returned and refunded.

Installation
------------




Configuration
-------------




Usage
-----

-----

-----

-----

=====

To use this module, when some customer returns some refundable products to you
before you created an invoice, you need to:

#. Go to *Sales > Sales Orders > Create*.
#. Choose a customer and add a product whose *Invoicing Policy* is *Delivered
   quantities*, and input some quantity to sell.
#. Confirm the sale.
#. Go to *Delivery > Validate > Apply > Reverse*.
#. Set *Quantity* to a lower quantity than the sold one, and enable
   *To Refund*.
#. Press *Return > Validate > Apply*.
#. Go back to the sale order.
#. Press *Create Invoice > Invoiceable lines > Create and View Invoices*.
#. The created invoice's amount will be the difference between the delivered
   and the returned quantity.

To use this module, when some customer returns some refundable products to you
after you created an invoice, you need to:

#. Go to *Sales > Sales Orders > Create*.
#. Choose a customer and add a product whose *Invoicing Policy* is *Delivered
   quantities*, and input some quantity to sell.
#. Confirm the sale.
#. Go to *Delivery > Validate > Apply*.
#. Return to the sale order.
#. Press *Create Invoice > Invoiceable lines > Create and View Invoices*.
#. The created invoice's amount is the same you sold.
#. Return to the sale order.
#. Go to *Delivery > Reverse*.
#. Set *Quantity* to a lower quantity than the sold one, and enable
   *To Refund*.
#. Press *Return > Validate > Apply*.
#. Return to the sale order.
#. Press *Create Invoice > Invoiceable lines (deduct down payments) >
   Create and View Invoices*.
#. A refund is created for the quantity you returned before.

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/95/9.0

Known issues / Roadmap
----------------------





* This addon is a pseudobackport of a functionality that exists natively in
  v10, plus a fix for https://github.com/odoo/odoo/issues/13974, so this addon
  will never have to be migrated to v10.

Bug Tracker
-----------





Bugs are tracked on `GitHub Issues
<https://github.com/OCA/account-invoicing/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed feedback.

Credits
-------





Images

* Odoo Community Association: `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.

[![Odoo Italia Associazione]]




### Contributors





* Jairo Llopis <jairo.llopis@tecnativa.com>

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
