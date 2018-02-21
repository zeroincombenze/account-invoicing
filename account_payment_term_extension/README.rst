[![Build Status](https://travis-ci.org/zeroincombenze/account-invoicing.svg?branch=8.0)](https://travis-ci.org/zeroincombenze/account-invoicing)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/account-invoicing/badge.svg?branch=8.0)](https://coveralls.io/github/zeroincombenze/account-invoicing?branch=8.0)
[![codecov](https://codecov.io/gh/zeroincombenze/account-invoicing/branch/8.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/account-invoicing/branch/8.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-8.svg)](https://github.com/OCA/account-invoicing/tree/8.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-8.svg)](http://wiki.zeroincombenze.org/en/Odoo/8.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-8.svg)](http://wiki.zeroincombenze.org/en/Odoo/8.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-8.svg)](http://erp8.zeroincombenze.it)
































[![en](http://www.shs-av.com/wp-content/en_US.png)](http://wiki.zeroincombenze.org/it/Odoo/7.0/man)

Account Payment Term Extension
==============================

This module was written to extend the functionality of payment terms to support rounding, months and weeks on payment term lines.

By default in Odoo, if you have a payment term of *30 days end of months* and you invoice on January 30, you will have a due date on March 31st. With this module, if you configure the payment term line with months = 1, days = 0 and days2 = -1, you will have a due date on February 28th.

This module also adds support for payment terms such as *End of month 45 days* (which is not the same as *45 days end of month* !).

Installation
------------




Configuration
-------------





To configure the Payment Terms and see the new options on the Payment Term Lines, go to the menu Accounting > Configuration > Miscellaneous > Payment Terms.

Usage
-----







Known issues / Roadmap
----------------------




Bug Tracker
-----------




Credits
-------









### Contributors





* Yannick Vaucher <yannick.vaucher@camptocamp.com>
* Alexis de Lattre <alexis.delattre@akretion.com>

### Funders

### Maintainer








.. image:: http://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: http://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose mission is to support the collaborative development of Odoo features and promote its widespread use.

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
