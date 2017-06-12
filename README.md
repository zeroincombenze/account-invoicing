[![Build Status](https://travis-ci.org/zeroincombenze/account-invoicing.svg?branch=10.0)](https://travis-ci.org/zeroincombenze/account-invoicing)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/account-invoicing/badge.svg?branch=10.0)](https://coveralls.io/github/zeroincombenze/account-invoicing?branch=10.0)
[![codecov](https://codecov.io/gh/zeroincombenze/account-invoicing/branch/10.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/account-invoicing/branch/10.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-10.svg)](https://github.com/OCA/account-invoicing/tree/10.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-10.svg)](http://wiki.zeroincombenze.org/en/Odoo/dev/10.0)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-10.svg)](http://wiki.zeroincombenze.org/en/Odoo/10.0/account-)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg)](http://erp10.zeroincombenze.it)

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
addon | version | summary
--- | --- | ---
[account_group_invoice_line](account_group_invoice_line/) | 10.0.1.0.0 | Add option to group invoice lines per account
[account_invoice_check_total](account_invoice_check_total/) | 10.0.1.0.0 | Check if the verification total is equal to the bill's total
[account_invoice_fiscal_position_update](account_invoice_fiscal_position_update/) | 10.0.1.0.0 | Changing the fiscal position of an invoice will auto-update invoice lines
[account_invoice_force_number](account_invoice_force_number/) | 10.0.1.0.0 | Allows to force invoice numbering on specific invoices
[account_invoice_merge](account_invoice_merge/) | 10.0.1.0.0 | Merge invoices in draft
[account_invoice_partner](account_invoice_partner/) | 10.0.1.0.0 | Replace the partner by an invoice contact if found
[account_invoice_refund_link](account_invoice_refund_link/) | 10.0.1.0.0 | Link refund invoice with its original invoice
[account_invoice_supplier_ref_unique](account_invoice_supplier_ref_unique/) | 10.0.1.0.0 | Checks that supplier invoices are not entered twice
[account_invoice_supplierinfo_update](account_invoice_supplierinfo_update/) | 10.0.1.0.0 | In the supplier invoice, automatically updates all products whose unit price on the line is different from the supplier price
[account_payment_term_extension](account_payment_term_extension/) | 10.0.1.0.0 | Adds rounding, months, weeks and multiple payment days properties on payment term lines


Unported addons
---------------
addon | version | summary
--- | --- | ---
[account_invoice_customer_ref_unique](account_invoice_customer_ref_unique/) | 1.0 (unported) | Unique Customer Reference in Invoice
[account_invoice_line_description](account_invoice_line_description/) | 8.0.1.0.0 (unported) | Account invoice line description
[account_invoice_line_sort](account_invoice_line_sort/) | 8.0.0.1.0 (unported) | Manage sort of customer invoice lines by customers
[account_invoice_merge_payment](account_invoice_merge_payment/) | 8.0.0.1.0 (unported) | Use invoice merge regarding fields on Account Payment Partner
[account_invoice_merge_purchase](account_invoice_merge_purchase/) | 8.0.1.0.0 (unported) | Compatibility between purchase and account invoice merge
[account_invoice_period_usability](account_invoice_period_usability/) | 8.0.1.0.0 (unported) | Display in the supplier invoice form the fiscal period next to the invoice date
[account_invoice_pricelist](account_invoice_pricelist/) | 8.0.1.0.0 (unported) | Add partner pricelist on invoices
[account_invoice_rounding](account_invoice_rounding/) | 8.0.1.0.0 (unported) | Unit rounded invoice
[account_invoice_shipping_address](account_invoice_shipping_address/) | 8.0.0.1.1 (unported) | Adds a shipping address field to the invoice.
[account_invoice_template](account_invoice_template/) | 0.1 (unported) | Account Invoice Template
[account_invoice_uom](account_invoice_uom/) | 8.0.1.0.0 (unported) | Unit of measure for invoices
[account_invoice_validation_workflow](account_invoice_validation_workflow/) | 8.0.1.0.1 (unported) | Add "To Send" and "To Validate" states in Invoices
[account_invoice_zero_autopay](account_invoice_zero_autopay/) | 8.0.1.0.0 (unported) | Account Invoice Zero Autopay
[product_customer_code_invoice](product_customer_code_invoice/) | 1.0 (unported) | Product Customer code for account invoice
[sale_order_partial_invoice](sale_order_partial_invoice/) | 1.1 (unported) | Sale Partial Invoice
[sale_timesheet_invoice_description](sale_timesheet_invoice_description/) | 9.0.1.0.0 (unported) | Add timesheet details in invoice line
[stock_invoice_picking_incoterm](stock_invoice_picking_incoterm/) | 0.1 (unported) | Stock Invoice Picking Incoterm
[stock_picking_invoicing](stock_picking_invoicing/) | 8.0.1.0.0 (unported) | Stock Picking Invoicing

[//]: # (end addons)

Translation Status
------------------
[![Transifex Status](https://www.transifex.com/projects/p/OCA-account-invoicing-10-0/chart/image_png)](https://www.transifex.com/projects/p/OCA-account-invoicing-10-0)

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
