---
description: Detailed overview of "Save All Emails in a Thread" function
---
# Save All Emails in a Thread Function Explained  
  

*4 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

{{ product_name }} includes the possibility to auto-save entire user-selected email communication threads to Salesforce. Mark an important thread for auto-saving once and no update from a prospect or partner will ever be omitted from CRM capturing.

After a thread is marked for saving, all non-[blocklisted/internal](../Initial-Search-and-Applied-Record-Filters/#internal_emails_corporate_domains_and_the_blocklist) past and future emails which belong to the thread will be auto-saved as Salesforce Activities: [completed Tasks or Email message objects](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-%28Adaptive-view%29/#11_emails_saved_as_emailmessages_vs_emails_saved_as_tasks) linked to Contacts or Leads specified on first email's saving.  

!!! note "Note"
    The function works retrospectively, also saving all past emails from the same thread

&nbsp;

### Feature prerequisites

As soon as all prerequisites listed below are met, the checkbox ''*Auto-save new emails within this thread*" appears at the bottom of [{{ product_name }} Save dialog](../Save-Email-Dialog/).

- *ServiceEmailAutoTrackConversations* should be enabled in your Org's Special settings. See [this article](../Special-Admin-Panel-Settings/#email_threads_auto-sync) for details

- If in your Org [emails are saved as Salesforce Tasks and not as EmailMessage objects](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#11_emails_saved_as_emailmessages_vs_emails_saved_as_tasks), a custom field ''*ConversationId*" must be added to the Activity object. See [this Salesforce article](https://help.salesforce.com/s/articleView?id=000335522&type=1) to learn how to do that.  
[The EmailMessage object](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-%28Adaptive-view%29/#11_emails_saved_as_emailmessages_vs_emails_saved_as_tasks) does **not** require custom field adding to use this feature  

- Email threads saving should also be enabled in individual user's Sync settings. See [this article](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_email_threads) for details

- Note that currently this feature is unavailable via [MS Graph connectivity](../MS-Graph/)

&nbsp;

&nbsp;

### Save all emails in a thread usage

After the setting is enabled as described above, to save all emails in a conversation thread:  
**1\.** Select any email in a thread and click **Save** in {{ product_name }} to open [Save dialog](../Save-Email-Dialog/)  
**2\.** Set all needed parameters for email saving in the dialog. These parameters will be applied to all auto-saved emails in the thread  
**3\.** Select the **Auto-save new emails within this thread** checkbox at the bottom of the dialog   
**4\.** Click **Save** at the top of the dialog  

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b07f2b80428635ba8b2bc42.png)

&nbsp;

&nbsp;

### Manage default checkbox state in Save dialog

The default state of this checkbox in Save dialog can be set in Add-In Customization settings. See the setting "*Do not select “Auto-save in thread” by default*" in [this article](../Customization-Settings-Explained/#2_application_settings).

&nbsp;

&nbsp;

### Specific use nuances

- The feature works in both [Read and Compose modes](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-%28Adaptive-view%29/#ways_to_save_an_email_in_salesforce)
- The initial email in a thread marked for autosaving must be located in your email client's *Inbox* or *Sent* folder, otherwise saving won't be performed  
- Saving is performed by [{{ short_name }} Sync Engine](../Synchronization-Engine-An-Overview/), so it's not instant but requires between 1 and 30 minutes, depending on sync session cycle 
- Like in other saving scenarios, emails saved this way get the custom "*Salesforce*" category
- [Service emails](../Saving-Emails-in-Salesforce-1.-Function-Overview/#6_the_add-in_chrome_extension_does_not_work_with_service_emails) saving is not supported, like in any other saving scenarios
- All emails in the thread get linked to the same records selected in the Save dialog for the first saved email. If new recipients are added to the thread, their email addresses are **not** matched with Salesforce records for linking    
- For auto-save in a thread scenario, {{ product_name }} passes the special values from email fields populated by the users in Save dialog to all subsequent synced emails, i.e., whatever the user selected for the first email will be the same for all new emails in a thread.

&nbsp;

&nbsp;

#### Linking Specifics for Save All Emails in a Thread



When a user saves an email linking it to a Salesforce record that was not [auto-retrieved and displayed in the Sidebar after email selection](../Initial-Search-and-Applied-Record-Filters/#related_records_retrieval_pattern), i.e. a user selected one that does not match any addresses in the email's fields From, To, and Cc or its body/signature, auto-saved thread emails' linking may follow either of the two patterns:

**A\.** The initial email in a thread marked for autosaving was saved with a [People record (WhoID)](https://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) in [Save dialog](../Save-Email-Dialog/)  

**B\.** The initial email in a thread marked for autosaving was saved with a [Business record (WhatID)](https://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) in [Save dialog](../Save-Email-Dialog/)  

&nbsp;

##### A. Linking to a Business record

If you're linking the email to a selected Business record, e.g. an Opportunity, Case, or Matter, and it was not retrieved on [initial search](../Initial-Search-and-Applied-Record-Filters/): the first selected email will be saved and linked to this record, and so will all other emails in this thread.

&nbsp;

##### B. Linking to a People record

If you're linking the email to a selected People record, e.g. a Contact, Lead, or Person Account, and it is absent in the email's fields From, To, and Cc or the email's body/signature and therefore was not retrieved on [initial search](../Initial-Search-and-Applied-Record-Filters/): the first selected email in the thread will be saved and successfully linked to this record, but all other emails in this thread will be saved in Salesforce and they will **not** be linked to that People record.

&nbsp;

The related [Global setting](../Special-Admin-Panel-Settings/#extra_configuration_settings) is *EmailAutoTrackConversations*, where *Business* records should be set in *RelatedToId*.

&nbsp;

&nbsp;

#### Save All Emails in a Thread: Specific Use Cases

Review the following sample use case to learn how linking works when multiple {{ short_name }} users are involved:    

**1\.** User #1 saves an initial email from a thread, it gets auto-linked to an auto-retrieved Opportunity A  
**2\.** User #2 auto-saves another email from the same thread. User 2 has an extra saving rule that also links the email to the related Account A. So the email will be linked to both Opportunity A and Account A  
**3\.** User #1 saves another email from the same thread via [Save Email dialog](../Save-Email-Dialog/), linking it to Opportunity B. As a result the email will be linked to Opportunity B only  
**4\.** User #2 auto-saves another email from the same thread, linked to Account A and Account B auto-retrieved from the email. Now the email will be linked to: Opportunity A (linked on action **1**), Account A (linked on action **2**), Opportunity B (linked on action **3**), and captured Account B  

&#160;
 &#160;

