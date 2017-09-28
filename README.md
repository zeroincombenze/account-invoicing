[![Build Status](https://travis-ci.org/zeroincombenze/account-invoicing.svg?branch=7.0)](https://travis-ci.org/zeroincombenze/account-invoicing)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/account-invoicing/badge.svg?branch=7.0)](https://coveralls.io/github/zeroincombenze/account-invoicing?branch=7.0)
[![codecov](https://codecov.io/gh/zeroincombenze/account-invoicing/branch/7.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/account-invoicing/branch/7.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-7.svg)](https://github.com/OCA/account-invoicing/tree/7.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-7.svg)](http://erp7.zeroincombenze.it)


[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)
================================================================================================
================================================================================================

OCA account invoicing modules for Odoo
======================================

This project aim to deal with modules related to manage invoicing in a generic way. You'll find modules that:

 - Add a validation step on invoicing process
 - Add check on invoice
 - Utils and ease of use for invoicing with Odoo
 - ...

Translation Status
[![Transifex Status](https://www.transifex.com/projects/p/OCA-account-invoicing-7-0/chart/image_png)](https://www.transifex.com/projects/p/OCA-account-invoicing-7-0)


[![it](https://github.com/zeroincombenze/grymb/blob/master/flags/it_IT.png)](https://www.facebook.com/groups/openerp.italia/)

Moduli Odoo Italia
==================

Differenze rispetto localizzazione ufficiale Odoo/OCA:

- Corretto errore "import openerp.addons.decimal_precision" https://github.com/OCA/OCB/issues/629

----

OCA, or the Odoo Community Association, is a nonprofit organization whose 
mission is to support the collaborative development of Odoo features and 
promote its widespread use.

http://odoo-community.org/

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


Available addons
----------------
addon | version | OCA version | summary
--- | --- | --- | ---
[account_invoice_currency_rate](account_invoice_currency_rate/) | 0.1 | :repeat: | account_invoice_currency_rate
[account_invoice_customer_ref_unique](account_invoice_customer_ref_unique/) | 1.0 | :repeat: | Unique Customer Reference in Invoice
[account_invoice_default_salesteam](account_invoice_default_salesteam/) | 1.1 | :repeat: | Default Sales Team on Invoice
[account_invoice_force_number](account_invoice_force_number/) | 0.1 | :repeat: | Force Invoice Number
[account_invoice_merge](account_invoice_merge/) | 1.1.1 | :repeat: | Account Invoice Merge Wizard
[account_invoice_partner](account_invoice_partner/) | 0.1 | :repeat: | Automatically select invoicing partner on invoice
[account_invoice_purchase_origin](account_invoice_purchase_origin/) | 1.1 | :repeat: | Account Invoice Purchase Origin
[account_invoice_rounding](account_invoice_rounding/) | 1.0 | :repeat: | Unit rounded invoice
[account_invoice_sale_origin](account_invoice_sale_origin/) | 1.1 | :repeat: | Account Invoice Sale Origin
[account_invoice_shipping_address](account_invoice_shipping_address/) | 0.1.1 | :repeat: | Invoice Shipping Address
[account_invoice_supplier_ref_unique](account_invoice_supplier_ref_unique/) | 1.0 | :repeat: | Unique Supplier Invoice Number in Invoice
[account_invoice_template](account_invoice_template/) | 0.1 | :repeat: | Account Invoice Template
[account_invoice_uom](account_invoice_uom/) | 1.0 | :repeat: | Unit of measure for invoices
[account_invoice_zero](account_invoice_zero/) | 1.0 | :repeat: | Account Invoice Zero
[account_origin_document_on_credit_note](account_origin_document_on_credit_note/) | 1.0 | :repeat: | Origin Document on Credit Note
[invoice_fiscal_position_update](invoice_fiscal_position_update/) | 1.0 | :repeat: | Changing the fiscal position of an invoice will auto-update invoice lines
[invoice_line_description](invoice_line_description/) | 0.1 | :repeat: | Invoice line description
[invoice_line_no_picking_name](invoice_line_no_picking_name/) | 0.1 | :repeat: | Invoice line no picking name
[invoice_validation_wkfl](invoice_validation_wkfl/) | 7.0.1.0.1 | :repeat: | Add "To Send" and "To Validate" states in Invoices
[payment_term_rounding](payment_term_rounding/) | 1.0 | :repeat: | Rounding on payment term
[product_customer_code_invoice](product_customer_code_invoice/) | 1.0 | :repeat: | Product Customer code for account invoice
[sale_order_partial_invoice](sale_order_partial_invoice/) | 1.1 | :repeat: | Sale Partial Invoice
[stock_invoice_picking](stock_invoice_picking/) | 0.1 | :repeat: | Invoice picking
[stock_invoice_picking_incoterm](stock_invoice_picking_incoterm/) | 0.1 | :repeat: | Stock Invoice Picking Incoterm

[//]: # (end addons)

[![chat with us](https://www.shs-av.com/wp-content/chat_with_us.gif)](https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b)
