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

Account Payment Term Extension

This module extends the functionality of payment terms to :

* support rounding, months and weeks on payment term lines
* allow to set more than one day of payment in payment terms
* allow to apply a chronological order on lines
 * for example, with a payment term which contains 2 lines
  * on standard, the due date of all lines is calculated from the invoice date
  * with this feature, the due date of the second line is calculated from the due date of the first line

Installation
------------





Configuration
-------------






To configure the Payment Terms and see the new options on the Payment Term Lines, you need to:

#. Go to the menu Accounting > Configuration > Management > Payment Terms.

To use multiple payment days, define for each payment term line which payment days apply, separated by spaces, commas or dashes.

Usage
-----

-----

-----

-----

-----

Known issues / Roadmap
----------------------





Bug Tracker
-----------






Bugs are tracked on `GitHub Issues
<https://github.com/OCA/account-invoicing/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed `feedback
<https://github.com/OCA/
account-invoicing/issues/new?body=module:%20
account_payment_term_extension%0Aversion:%20
9.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Credits
-------






Images

* Odoo Community Association: `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.
* https://openclipart.org/detail/198659/mono-template-invoice
* https://openclipart.org/detail/5571/calendar-icon-large

[![Odoo Italia Associazione]]





### Contributors






* Yannick Vaucher <yannick.vaucher@camptocamp.com>
* Alexis de Lattre <alexis.delattre@akretion.com>
* Julien Coux <julien.coux@camptocamp.com>
* Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>

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
