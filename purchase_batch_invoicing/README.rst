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

Purchase Batch Invoicing
========================

This module extends the functionality of purchases to support batch invoicing
purchase orders and to allow you to choose if you want them grouped by purchase
order or by vendor.

Installation
------------





Configuration
-------------






An automated task is included to invoice all pending purchase orders every
week, but it is disabled by default. To enable it:

#. Have *Administration / Settings* permissions.
#. Go to *[Your user menu] > About > Activate the developer mode*.
#. Go to *Settings > Technical > Automation > Scheduled Actions > Invoice all
   pending purchase orders > Edit*.
#. Enable it by clicking on *Active* and set the date accordingly.
#. Save.

Usage
-----

-----

-----

-----

-----

-----

=====

To use this module, you need to:

#. Have *Purchase / User* permissions.
#. Go to *Purchases > Purchase > Purchase Orders > Create* and fill the form.
#. Press *Confirm*.
#. Press *Receive Products*.
#. Press *Validate > Apply*.
#. Repeat above steps a couple of times.
#. Go back to *Purchase Orders*, select those you just created and press
   *Action > Batch Invoice*. Alternatively, you can use the *Create Invoice*
   button in the purchase order form.
#. You get a wizard with a list of ready-to-invoice purchase orders. Choose the
   *Grouping* method.

   .. figure:: /purchase_batch_invoicing/static/description/wizard.png
      :alt: Purchase order batch invoicing wizard

#. Press *Accept*.
#. You will get to a screen where you can see all the vendor bills you just
   generated.

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/95/9.0

Known Issues / Roadmap

It would be nice to be able to group invoices by PO line.

Known issues / Roadmap
----------------------





Bug Tracker
-----------






Bugs are tracked on `GitHub Issues
<https://github.com/OCA/account-invoicing/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed feedback.

Credits
-------











### Contributors






* Jairo Llopis <jairo.llopis@tecnativa.com>
* Pedro M. Baeza <pedro.baeza@tecnativa.com>

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
