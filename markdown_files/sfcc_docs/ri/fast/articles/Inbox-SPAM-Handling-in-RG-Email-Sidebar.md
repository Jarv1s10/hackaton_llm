---
description: How to exclude SPAM from handling by RG Email Sidebar
---
# Exclude Spam from Handling by {{ product_name }}  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

If Emails auto-saving is enabled and [Leads or Contacts auto-resolving](../Synchronization-Engine-An-Overview/#automatic_creation_of_contacts_or_leads_by_rg_email_sidebar_autoresolving) is set up in your configuration, {{ product_name }} will process SPAM emails from [non-blocklisted email domains](../Configuring-Activities-Synchronization-Settings/#blocklisting_email_addresses_and_domains) which get through to your MS Outlook or Gmail Imbox. That happens because {{ short_name }} processes *all* new non-internal emails in the automatic saving mode and it has no means to differentiate between business emails from previously unknown business contacts and SPAM emails. This way, in this mode {{ product_name }} will also auto-create Leads or Contacts (plus Accounts) in Salesforce based on SPAM email's data.  

If that happens:   

**1\.** Delete the auto-created Lead or Contact plus Account directly in Salesforce. It's one of the basic principles of {{ product_name }} not to delete any records from Salesforce, so that must be performed manually by the user   

**2\.** Select the auto-processed SPAM email in MS Outlook's Inbox and click **Do not sync** in the **Suggested new records** tab in {{ product_name }}. This will add the email address to {{ short_name }}'s [not-for-syncing blocklist](../Configuring-Activities-Synchronization-Settings/#blocklisting_email_addresses_and_domains)   

or you may [mark the SPAM email as Junk mail in MS Outlook](https://support.microsoft.com/en-us/office/overview-of-the-junk-email-filter-5ae3ea8e-cf41-4fa0-b02a-3b96e21de089) so it will be automatically moved from the Inbox, this way preventing its autosaving by {{ product_name }}

&nbsp;

To prevent autosaving of SPAM emails, make sure that they do not get into your Inbox, by using [MS Exchange's anti-SPAM mechanisms](https://docs.microsoft.com/en-us/exchange/antispam-and-antimalware/antispam-and-antimalware?view=exchserver-2019) on both user level and Admin level.

&#160;
 &#160;



