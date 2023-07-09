# Contact Address Synchronization Limitation

&nbsp;

&nbsp;

**[ This article is work-in-progress ]**

&nbsp;

&nbsp;

SAP Cloud for Customer and MS Outlook have significant design discrepancies in the Contact Address fields area. SAP Cloud for Customer keeps *House Number* and *Street* as 2 separate fields, while MS Outlook keeps both values in a single one.

This inconsistency may lead to House Number and Street fields merging in SAP Cloud for Customer after sync, in case of the Contact update in MS Outlook.

&nbsp;

**Solution**

This is a known limitation of the products. The option to prevent fields merging is to keep SAP Accounts and (or) Contacts **read-only** in MS Outlook. This is a standard option in the SSI Sync settings configuration.

&nbsp;

&nbsp;