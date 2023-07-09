# SSI Initial Search and Applied Record Filters

&nbsp;

&nbsp;

In SSI, automatic search for relevant SAP Cloud for Customer records (initial search) follows a specific algorithm of interactions between SSI Add-In, MS Exchange / Office 365 / Gmail, and SAP Cloud for Customer. The information below describes the general relevant records retrieval principle applied by the Add-In.

&nbsp;

&nbsp;

## Related records retrieval pattern

On [SSI Sidebar opening](../How-to-Open-C4C-SSI-Sidebar/) for a specific e-mail or calendar item, SSI Add-In searches for SAP Cloud for Customer objects which are referenced (involved) in the e-mail/meeting.

!!! tip "Tip"
    If you need to perform initial search for an object afresh after something was changed about it or relevant SAP Cloud for Customer records, press the **Refresh** icon located in the upper left corner of the [Sidebar](../How-to-Use-C4C-SSI/)

&nbsp;

Referencing of relevant objects is based on parsing of e-mail addresses from the fields:

* *To*, *From*, *CC*, and *BCC* (only in composing mode) for the E-Mails

* *Organizer*, *Required*, and *Optional* attendees for the calendar items

&nbsp;

&nbsp;

## Related records search algorithm

* Add-In will show all Contacts, Individual Customers, Leads, and Accounts found in SAP Cloud for Customer by the e-mail addresses parsed from the e-mail or calendar item

* [Employee object is never shown in the Add-In, however, SSI still processes them](../questions-and-answers/#why_are_employee_records_not_displayed_in_the_add-in_when_employee_is_selected_and_read-only_in_profile_add-in_settings). If any activity includes only the employee's e-mail address, no cards will be shown during the initial search

* Blocklisted e-mail addresses and domains are filtered out of the initial search scope. Therefore, if any SAP Cloud for Customer object's e-mail address or domain is blocklisted, this card will never be shown in the Add-In during the initial search. Refer to [this article](../blocklist/) for more information

* When SSI cannot find an SAP Cloud for Customer object with a matching e-mail address from the initial search scope, SSI suggests creating a new Contact or Lead based on that e&#8209;mail address and shows "*Not Found in SAP*" card with a corresponding **Contact** and **Lead** buttons in the Sidebar. Refer to [this article](../Create-Records/#creating_objects_via_not_found_in_sap_cards) for more information

* Add-In will show all additional objects already linked to the e-mail or calendar item in SAP Cloud for Customer, even if these objects were not parsed during the previous initial search before linking

&nbsp;

&nbsp;