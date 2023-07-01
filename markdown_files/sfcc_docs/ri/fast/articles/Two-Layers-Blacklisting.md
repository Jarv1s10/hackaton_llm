---
description: Learn how to use blocklisting to exclude email addresses or email domains from being saved
---
# Two Layers of Not-for-syncing Blocklists  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

Among other features, {{ product_name }} offers automated saving of Exchange/Office 365 Emails,  Meetings/Appointments, and Contacts in Salesforce. To prevent saving of items not intended to be saved in Salesforce, {{ short_name }} includes two layers of blocklisting based on email address or email domains:

- [Org-wide blocklisting](../Special-Admin-Panel-Settings/#emails_domains_blocklisted_from_sync) (managed via the [Admin panel](../How-to-Log-In-to-the-Admin-Panel/)). This blocklist is used to exclude spam, newsletters, and other unwanted emails from being saved in Salesforce by the users; internal (in-org) domains and addresses are also appended to it
- [User-defined blocklisting](../Configuring-Activities-Synchronization-Settings/#blocklisting_email_addresses_and_domains) (managed via [individual Sync settings](../How-to-Open-Sync-Dashboard-(Adaptive-view)/)). This blocklist is used to exclude personal communication and meetings/appointments as well as personal newsletters from being saved in Salesforce

By default, these blocklists are combined for every individual user and users can remove addresses/domains set on the Admin level from the congregated blocklist.

Additionaly, if a company uses several internal email domains (e.g., *successteam.com*, *success.team*, *successteam.io*), it is impossible to remove these email domains from the blocklist. If admins manually remove any internal email domain in the *ServiceAutoTrackBlackList* setting, on refreshing the Settings page, the deleted email domain will be restored in the blocklist. This is the default designed behavior.

The same happens when a user removes internal domain(s) from their individual Blocklist in {{ short_company_name }} Sync Settings, the deleted domain(s) reappear in the Blocklist after some time.

!!! note "Note"
    Per [customer's request](mailto:support@revenuegrid.com) (option available for Enterprise users only), this behavior can be adjusted so that addresses/domains set by the Admin will be impossible to remove from the blocklist via the users' [individual Synchronization setting](../Configuring-Activities-Synchronization-Settings/#blocklisting_email_addresses_and_domains)

&nbsp;

!!! note "Note"
    Besides the org-wide and user-defined blocklisting described above, another blocklist feature is configured in {{ short_name }}. A special global setting blocklists all free email services (e.g. *gmail.com*, *yahoo.com*, etc.) from [auto-syncing](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_emails_emails_autosharing) by default. To change or customize this setting, contact our [support team](mailto:support@revenuegrid.com)

&#160;
 &#160;

