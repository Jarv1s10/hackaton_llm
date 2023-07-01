# Questions & Answers

&nbsp;

&nbsp;

**[ This article is work-in-progress ]**

&nbsp;

&nbsp;

### What is the default synchronization interval in SAP Cloud for Customer Server-Side Integration?

The SSI synchronization interval is set to **30 minutes** to balance system functionality and infrastructure load. This interval is fixed in SSI currently.

&nbsp;

* * *

&nbsp;

### How are Contacts linked to Accounts during synchronization?

SSI links Contact to an Account in SAP Cloud for Customer if Contact's "Company" field in MS Outlook contains the Account name. Server-Side Sync performs a search for an Account in CRM:

* if there is a match, Contact will be linked to an existing Account in SAP Cloud for Customer
* if there is no match, SSI will try to create an Account in SAP Cloud for Customer
* if a failure occurs, Contact will be saved to SAP Cloud for Customer without company

&nbsp;

* * *

&nbsp;

### Why are Employee records not displayed in the Add-In when Employee is selected and read-only in Profile Add-In settings?

<p><img src= "..\..\assets\images\q-n-a\1.png" style="width:45%;float:right;margin-left:2%;"/>
</p>

SSI filters out and does not display any Employee records in the Add-In – that is made **by design**. SSI shows only Contact, Account, and Individual Customer records. If there is no e-mail present to perform a search, a blank card to create a new record will be shown in the Add-In.

&nbsp;

* * *

&nbsp;

### Does Server-Side Integration support the "SAP Cloud for Customer tenant copy" procedure?

Server-Side Integration **does not support** the "tenant copy" procedure. Moreover, we do not recommend using the same mailboxes for different tenants. We suggest using different mailboxes and SAP Cloud for Customer users for each tenant.

&nbsp;

&nbsp;