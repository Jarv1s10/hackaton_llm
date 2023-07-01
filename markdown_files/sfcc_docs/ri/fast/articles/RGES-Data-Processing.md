---
description: Data handling & organization in RG Email Sidebar explained
---
# Data Handling & Organization  
  

*3 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! note "Note"
    Other {{ company_name }} components (Intelligence Package and the Engagement Package), handle and store different scopes of business and user data, which is required to perform their functions. See [this article](https://docs.revenuegrid.com/articles/Privacy-and-Security/#product-specific_privacy_terms) for complete information. Also check out the [full {{ company_name }} Privacy Policy](https://revenuegrid.com/privacy-policy/)

&nbsp;
## Data Handling

{{ short_name }} alone does **not** persistently store any of your Salesforce, MS Exchange / O365 / Google data, e.g. Contacts, Emails, calendar items, Tasks. It solely transfers relevant data between your email server and your Salesforce over secure MS Azure protocols via TLS 1.2 encrypted protocol in-transit and at rest. The product's interactions with your Salesforce are authorized via the native OAuth method. Similarly, mail server interactions are authorized via supported secure mechanisms like O365 / Exchange OAuth or Google OAuth. Thus, no user login credentials are stored by {{ short_name }} either.  
Only the following data types get temporarily stored in {{ short_name }} Azure infrastructure:  

- {{ short_name }} user full name and email address for authentication purposes
- Key diagnostics details: non-personal data, such as: email or meeting identifiers in the system, *Sent* and *Received* dates, along with user setting configurations. These are needed solely for customer support and troubleshooting purposes. The logs get encrypted for secure transferring and keeping, they can only be accessed by entitled Support specialists to investigate issues. All diagnostics data gets automatically purged from the system 90 days after collection
- Starting with the May 2022 update, we also introduce an advanced logging mode that can be enabled for complex troubleshooting cases upon a customer's request. In this mode, the logging system retrieves additional details for our specialists' immediate investigation, the mode's Enabled or Disabled status is always known to the user that requested assistance  

&nbsp;
* * *
&nbsp;

## Data Backups

{{ short_name }} does **not** back up any of your business data, all your data is stored in your email client / calendar and Salesforce.  


Only end users’ {{ short_name }} setup ([Customization](../Customization-Settings-Explained/) and [Sync settings](../Configuring-Activities-Synchronization-Settings/)) and [Org configuration data](../Managing-Organizations-via-the-Admin-Panel/) get continuously and automatically backed up. This config data is kept in the infrastructure as multiple timestamped copies, ensuring the possibility to perform point-in-time restores, if required.  
Additionally, {{ short_name }} Customization settings be exported to a .json file. by the end users themselves or by the Admin users in bulk, and then this setup can be applied for other users by importing the .json file. See more details in [this article](../Managing-Email-Sidebar-Customizations/).

&nbsp;

&nbsp;

* * *

&nbsp;

## Handled Data Organization

{{ short_name }} has several mechanisms for keeping handled data well organized, this way optimizing Salesforce storage use:


&nbsp;

### Emails and Calendar items

To ensure smart selective saving of emails, {{ short_name }} includes several layers of sorting what gets processed. See [this article](../Saving-Emails-in-Salesforce-1.-Function-Overview/#under_the_hood_mechanisms_and_special_patterns_applied_on_emails_saving) for complete information. Emails can be saved as Tasks or as EmailMessages, see [this article](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-%28Adaptive-view%29/#11_emails_saved_as_emailmessages_vs_emails_saved_as_tasks) for details.

&nbsp;

### Deduplication

Prevents creation of unneeded clones of the same Email, Calendar, Contact, or Task item. See [this article](../Item-Deduplication-Mechanisms/) for complete information.

&nbsp;

### File attachments

!!! tip "Tip"
    Also see [this article](../Attachments-Handling-(Advanced)/) for in-depth information

&nbsp;

With {{ short_name }}, you can fully control the criteria what attachments should be saved in Salesforce: Max size limit (up to 25 MB), Min size limit (to prevent signature pictures saving), file extensions control: an extensions blocklist and an allow-list. See [this article](../Attachments-Handling-%28Basic%29/#special_considerations_applied_on_calendar_item_attachments_saving) for more information.

Attachments can also be saved as Content Documents (Files); this allows saving storage in Salesforce: every attached file gets saved only once, even if the email gets saved with multiple Salesforce records. See [this article](../Configure-Attachments-Saving-in-Salesforce/) for details.

&nbsp;