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

Refund Returned Pickings from Purchase Orders
=============================================

This module extends the functionality of purchase orders to better manage
supplier returns and refunds.

In the purchase order you are able to display, for each line:

* Quantity to Bill, and  Quantity to Refund as separate fields. You have the
  option to create a vendor bill or a refund. In the bill or refund the
  correct quantity will be proposed, based on those fields.

* Billed Quantity and Refunded Quantity, as separate fields.

* Received Quantity and Returned Quantity, as separate fields.



Installation
------------





Configuration
-------------





Usage
-----

-----

-----

-----

-----

-----

=====

Case 1: When you return to a supplier some products, and you have not yet
received the bill from the supplier

#. Go to *Purchases > Purchase > Purchase Orders > Create*.
#. Choose a supplier and add a product whose *Invoicing Policy* is *On Received
   quantities*, and input some quantity to purchase.
#. Confirm the purchase order.
#. Go to *Shipment > Validate > Apply* so as to receive the quantities ordered.
#. Press the button *Reverse*.
#. In the wizard *Reverse Quantity* Set *Quantity* to the quantity to be
   returned. Press *Return* to complete the wizard.
#. On the return picking press *Validate > Apply*.
#. Go back to the purchase order. You will notice that the field *Returned
   Qty* is now the quantity that was returned. The field *Quantity to
   Bill* will show the quantity received less the quantity returned.
#. Press the button *Invoices* to create the vendor bill.
#. The proposed vendor bill will be proposed for the difference between the
   received and the returned quantity.

Case 2: When you return to a supplier some products, and you have already
received a bill from the supplier.

#. Go to *Purchases > Purchase > Purchase Orders > Create*.
#. Choose a supplier and add a product whose *Invoicing Policy* is *On Received
   quantities*, and input some quantity to purchase.
#. Confirm the purchase order.
#. Go to *Shipment > Validate > Apply* so as to receive the quantities ordered.
#. Press the button *Invoices* to create the vendor bill.
#. The proposed vendor bill will be proposed for the quantity received. The
   *Invoice Status* is now 'Invoiced'
#. Go to the original incoming shipment
#. Press the button *Reverse*.
#. In the wizard *Reverse Quantity* Set *Quantity* to the quantity to be
   returned. Press *Return* to complete the wizard.
#. On the return picking press *Validate > Apply*.
#. Go back to the purchase order. It will have  *Invoice Status* as 'Waiting
   Invoces'. You will notice that the field *Returned Qty* is now the quantity
   that was returned. The field *Quantity to Refund* is now the showing the
   quantity returned that was previously billed.
#. Press the button *Refunds* to create the vendor refund bill (since the
   field *Quantity to Invoice* is negative).
#. The proposed vendor refund bill will be proposed for the quantity that is
   to be refunded.
#. If you back to the purchase order, you will notice that *Invoice Status*
   is now 'Invoiced', even when the quantity ordered does not match with the
   quantity invoiced, because you did return some products.

Remark: As part of the 3-way match proces, if you accept that you will not
claim for a refund for the quantity returned to the supplier, just set the
purchase status as 'Done' at the end of the process, and the quantity to
invoice for the items will be set to 0 (because you have accepted the
discrepancies).

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/95/9.0

Known issues / Roadmap
----------------------






* The functionality of return processing with refunds is being discussed with
  Odoo here: https://github.com/odoo/odoo/issues/13974, so this addon may not
  need to be migrated to v10.

* The computation of the quantity invoiced is hacked to overcome an issue in
  one of the tests of Odoo. See https://github.com/OCA/OCB/pull/598

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






### Contributors






* Jordi Ballester Alomar <jordi.ballester@eficent.com>

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
