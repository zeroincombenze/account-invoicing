[![Build Status](https://travis-ci.org/zeroincombenze/account-invoicing.svg?branch=10.0)](https://travis-ci.org/zeroincombenze/account-invoicing)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/account-invoicing/badge.svg?branch=10.0)](https://coveralls.io/github/zeroincombenze/account-invoicing?branch=10.0)
[![codecov](https://codecov.io/gh/zeroincombenze/account-invoicing/branch/10.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/account-invoicing/branch/10.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-10.svg)](https://github.com/OCA/account-invoicing/tree/10.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-10.svg)](http://wiki.zeroincombenze.org/en/Odoo/10.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-10.svg)](http://wiki.zeroincombenze.org/en/Odoo/10.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg)](http://erp10.zeroincombenze.it)
















































[![en](http://www.shs-av.com/wp-content/en_US.png)](http://wiki.zeroincombenze.org/it/Odoo/7.0/man)

   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

Update Supplier Info of product from Supplier Invoice
=====================================================

This module allows to automatically update all products information in vendor bill for which the purchase information on the line are different from the supplier information defined in the product form.

It creates a new supplier information line if there is not any or it updates the first one in the list.

This module adds a new button 'Check Supplier Info' in supplier
invoice form.

.. image:: /account_invoice_supplierinfo_update/static/description/supplier_invoice_form.png


When the user clicks on it, he can see the supplier information changes that will apply. Optionally, he can remove some temporary changes, specially, if,
for example, a supplier applied an exceptional price change.

.. image:: /account_invoice_supplierinfo_update/static/description/main_screenshot.png

* blue: Creates a full new supplier info line
* brown: Updates current settings, displaying price variation (%)

This module adds an extra boolean field 'Supplier Informations Checked' in the
'Other Info' tab inside the supplier invoice form. 
This field indicates that the prices have been checked and
supplierinfo updated (or eventually that the changes have been ignored).

.. image:: /account_invoice_supplierinfo_update/static/description/supplier_invoice_form_other_info_tab.png

Installation
------------





Configuration
-------------





Usage
-----







=====

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/142/8.0

Known issues / Roadmap
----------------------





Bug Tracker
-----------






Bugs are tracked on `GitHub Issues
<https://github.com/OCA/account-invoicing/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback.

Known Issues / Roadmap

* This module does not manage correctly difference if

    * invoice line UoM are not the same as Supplierinfo UoM
    * invoice line taxes are not the same as products taxes. (If one is
      marked as tax included in the price and the other is marked as
      tax excluded in the price)

Credits
-------











### Contributors






* Chafique Delli <chafique.delli@akretion.com>
* Sylvain LE GAL (https://twitter.com/legalsylvain)
* Mourad EL HADJ MIMOUNE <mourad.elhadj.mimoune@akretion.com>

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
