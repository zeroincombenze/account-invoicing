[![Build Status](https://travis-ci.org/zeroincombenze/account-invoicing.svg?branch=8.0)](https://travis-ci.org/zeroincombenze/account-invoicing)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/account-invoicing/badge.svg?branch=8.0)](https://coveralls.io/github/zeroincombenze/account-invoicing?branch=8.0)
[![codecov](https://codecov.io/gh/zeroincombenze/account-invoicing/branch/8.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/account-invoicing/branch/8.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-8.svg)](https://github.com/OCA/account-invoicing/tree/8.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-8.svg)](http://wiki.zeroincombenze.org/en/Odoo/8.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-8.svg)](http://wiki.zeroincombenze.org/en/Odoo/8.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-8.svg)](http://erp8.zeroincombenze.it)
































[![en](http://www.shs-av.com/wp-content/en_US.png)](http://wiki.zeroincombenze.org/it/Odoo/7.0/man)

OCA account invoicing modules for Odoo
======================================

This project aim to deal with modules related to manage invoicing in a generic way. You'll find modules that:

 - Add a validation step on invoicing process
 - Add check on invoice
 - Unit rounded invoice
 - Utils and ease of use for invoicing with Odoo
 - ...

[//]: # (addons)


Available addons
----------------
addon | version | OCA version | summary
--- | --- | --- | ---
[account_group_invoice_lines](account_group_invoice_lines/) | 8.0.1.1.0 | :repeat: | Add option to group invoice line per account
[account_invoice_force_number](account_invoice_force_number/) | 8.0.0.1.0 | :repeat: | Allows to force invoice numbering on specific invoices
[account_invoice_line_description](account_invoice_line_description/) | 8.0.1.0.1 | :repeat: | Account invoice line description
[account_invoice_line_price_subtotal_gross](account_invoice_line_price_subtotal_gross/) | 8.0.1.0.0 | :repeat: | Show gross price in subtotal for for account.invoice.line
[account_invoice_line_sort](account_invoice_line_sort/) | 8.0.0.1.0 | 8.0.0.1.1 | Manage sort of customer invoice lines by customers
[account_invoice_merge](account_invoice_merge/) | 8.0.2.0.0 | 8.0.2.0.1 | Account Invoice Merge Wizard
[account_invoice_merge_payment](account_invoice_merge_payment/) | 8.0.0.1.0 | 8.0.0.1.1 | Use invoice merge regarding fields on Account Payment Partner
[account_invoice_merge_purchase](account_invoice_merge_purchase/) | 8.0.1.0.0 | 8.0.2.0.1 | Compatibility between purchase and account invoice merge
[account_invoice_partner](account_invoice_partner/) | 8.0.0.2.0 | :repeat: | Automatically select invoicing partner on invoice
[account_invoice_period_usability](account_invoice_period_usability/) | 8.0.1.0.0 | :repeat: | Display in the supplier invoice form the fiscal period next to the invoice date
[account_invoice_pricelist](account_invoice_pricelist/) | 8.0.1.0.0 | 8.0.1.1.0 | Add partner pricelist on invoices
[account_invoice_reopen](account_invoice_reopen/) | 1.1 | :x: | Invoice Reopen
[account_invoice_rounding](account_invoice_rounding/) | 8.0.1.0.0 | :repeat: | Unit rounded invoice
[account_invoice_shipping_address](account_invoice_shipping_address/) | 8.0.0.1.1 | :repeat: | Adds a shipping address field to the invoice.
[account_invoice_supplier_number_info](account_invoice_supplier_number_info/) | 8.0.1.0.0 | :repeat: | Allows to force invoice numbering on specific invoices
[account_invoice_supplier_ref_unique](account_invoice_supplier_ref_unique/) | 8.0.1.1.0 | :repeat: | Checks that supplier invoices are not entered twice
[account_invoice_uom](account_invoice_uom/) | 8.0.1.0.0 | :repeat: | Unit of measure for invoices
[account_invoice_validation_workflow](account_invoice_validation_workflow/) | 8.0.1.0.1 | :repeat: | Add "To Send" and "To Validate" states in Invoices
[account_invoice_zero_autopay](account_invoice_zero_autopay/) | 8.0.1.0.0 | :repeat: | Account Invoice Zero Autopay
[account_payment_term_extension](account_payment_term_extension/) | 8.0.1.0.0 | :repeat: | Adds rounding, months and weeks properties on payment term lines
[invoice_fiscal_position_update](invoice_fiscal_position_update/) | 8.0.1.0.0 | :repeat: | Changing the fiscal position of an invoice will auto-update invoice lines
[sale_order_line_price_subtotal_gross](sale_order_line_price_subtotal_gross/) | 8.0.1.0.0 | :repeat: | Show gross price in subtotal for for sale.order.line
[stock_picking_invoice_product_group](stock_picking_invoice_product_group/) | 8.0.1.0.0 | :repeat: | Invoices created from picking grouped by product or by product category
[stock_picking_invoicing](stock_picking_invoicing/) | 8.0.1.0.0 | :x: | Stock Picking Invoicing
[stock_picking_invoicing_incoterm](stock_picking_invoicing_incoterm/) | 8.0.1.0.0 | :repeat: | Stock Picking Invoicing Incoterm
[stock_picking_invoicing_incoterm_sale](stock_picking_invoicing_incoterm_sale/) | 8.0.1.0.0 | :repeat: | Copy incoterm from sale to invoice and to picking
[stock_picking_invoicing_unified](stock_picking_invoicing_unified/) | 8.0.1.0.0 | :repeat: | Create invoices/refunds from pickings of different types


Unported addons
---------------
addon | version | OCA version | summary
--- | --- | --- | ---
[account_invoice_customer_ref_unique](account_invoice_customer_ref_unique/) | 1.0 (unported) | :repeat: | Unique Customer Reference in Invoice
[account_invoice_template](account_invoice_template/) | 0.1 (unported) | :repeat: | Account Invoice Template
[product_customer_code_invoice](product_customer_code_invoice/) | 1.0 (unported) | :repeat: | Product Customer code for account invoice
[sale_order_partial_invoice](sale_order_partial_invoice/) | 1.1 (unported) | :repeat: | Sale Partial Invoice

[//]: # (end addons)

Translation Status
[![Transifex Status](https://www.transifex.com/projects/p/OCA-account-invoicing-8-0/chart/image_png)](https://www.transifex.com/projects/p/OCA-account-invoicing-8-0)

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

[![chat with us](https://www.shs-av.com/wp-content/chat_with_us.gif)](https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b)
