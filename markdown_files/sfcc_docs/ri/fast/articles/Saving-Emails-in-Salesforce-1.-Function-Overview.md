---
description: Detailed overview of the mechanisms involved in saving email messages in Salesforce
---
# Saving Emails in Salesforce: An Overview  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*7 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

The basis of {{ product_name }} functioning is carrying out special interactions between MS Exchange / Office 365 or Google mail/calendar and Salesforce through data transfer and synchronization between [their matching objects' fields](../Object-Fields-Mapping-Patterns/). One of the key features of {{ product_name }} is saving (sharing) emails/events as records in Salesforce and modifying them directly via the [Sidebar](../Introduction/). This article provides a detailed overview of the mechanisms involved in saving email messages in Salesforce.

&nbsp;

**Primary Emails Processing**

An email received or sent in MS Exchange / Office 365 or Gmail consists of the following elements: the sender’s email address, the recipients’ email addresses (the _To_, _CC_, and _BCC_ lines), the date and time of sending, the email’s subject line, message body and its formatting , the sender’s signature, and the files attached to the email. When {{ product_name }} for Salesforce processes a message opened in MS Outlook, it obtains all this data from MS Exchange/Gmail and based on the email address determines whether the message is [internal or blocklisted from Salesforce synchronization](../Initial-Search-and-Applied-Record-Filters/#internal_emails_corporate_domains_and_the_blocklist) and finds in Salesforce the records related to it based on the senders’ and recipients’ addresses extracted. Also refer to [this article](../Initial-Search-and-Applied-Record-Filters/) to learn more about these filtering mechanisms.

Emails classified as internal / blocklisted (see the article linked above) are <u>not</u> saved in Salesforce automatically and besides the **Save** button in {{ product_name }} is disabled for them. When such message is opened, to indicate why the message cannot be saved in Salesforce there appears a notification under **Smart Actions** > **More...** > **Observations** "_Some not important emails were filtered:_" with the list of internal or blocklisted email addresses the message contains.

Also see [this article](../Special-Admin-Panel-Settings/#auto-saving_and_blocklist_intersections) for information on alternative scenarios available for of different saving modes with  the [Blocklist](../Configuring-Activities-Synchronization-Settings/#blocklisting_email_addresses_and_domains).



<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5b71aff12c7d3a03f89da34e.png">
</p></details>

&nbsp;


Refer to [this article](../How-to-Save-Internal-or-Blacklisted-Emails-in-Salesforce-(Adaptive-view)/) to learn how to save such emails in Salesforce without [removing their addresses/domains from the blocklist](../Initial-Search-and-Applied-Record-Filters/).

!!! note "Note"
    If the message’s full addresses list contains at least one non-internal/blocklisted email address, the message will be saveable in Salesforce as a brand new record or as one linked to [associated](https://help.salesforce.com/articleView?id=overview_of_custom_object_relationships.htm&type=5) existing records

&nbsp;

* * *

&nbsp;

### "Under the hood" mechanisms and special patterns applied on Emails saving

**1\.** When a message is opened in {{ product_name }}, the Add-In / Chrome Extension retrieves the described above [message elements](../Object-Fields-Mapping-Patterns/#ms_outlook_emails) from MS Exchange/Gmail. Besides the email addresses, useful data from the message’s signature (name, surname, position, phone number, company name and website address, etc.) as well as email addresses, links, or phone numbers  contained in message body are extracted and used to search for related records in the next step.

&nbsp;

**2\.** Next, [Related records search in Salesforce](../Initial-Search-and-Applied-Record-Filters/) is performed to determine if there has been previous communication (that is, saved Salesforce  records) related to message sender/recipients and other contact data found in the message. Furthermore, at this step {{ product_name }} obtains relevant contextual information about the message to be displayed in the Sidebar and put in prefilled record fields, if related records are found.  

&nbsp;

**3\.** {{ company_name }} auto-synchronization only handles emails located in the *Inbox*, *Sent* and custom *Salesforce* folders of MS Outlook, it will **not** process emails assigned the Salesforce category but located in other folders. The same concerns saving all emails in a thread, it applies only to the items in the *Inbox* and *Sent* MS Outlook folders.    
  
For special emails saving scenarios requested by some customers, {{ product_name }} also offers on-demand possibility to save any emails located in custom mailbox folders/subfolders. In this email auto-sync scenario, the customer can create new custom folders any time and exclude folders the customer doesn't want to sync. 

&nbsp;

**4\.** Unlike [calendar items syncing](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/), emails saving and auto-saving is always a [one-way](../Special-Sync-Options-Save-Events-As-Other-&-One-Way-Sync/) MS Exchange/Gmail → Salesforce process; saving of an individual email is only performed once, unless you delete its matching entry in Salesforce, and its content is not synchronized in any way in the future. For example, if you modify a [Task/Email message](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#1_saving_an_email_when_smartcloud_connect_synchronization_is_active) Salesforce object based on an email message, these changes do not get [down-synchronized](../Synchronization-Engine-An-Overview/) to your MS Exchange / Office 365 or Gmail and only remain in Salesforce.   
There is also a special custom scenario where a saved email gets deleted from Salesforce to allow editing its Body via the Sidebar. See [this section of the article](../Saving-Emails-in-Salesforce-1.-Function-Overview/#editing_already_saved_email_messages_via_the_sidebar) for complete information

&nbsp;

**5\.** Emails categories which do **not** get auto-saved if [the corresponding Sync setting](../Configuring-Activities-Synchronization-Settings/#automatic_sharing_of_emails) is on:

- [Internal emails](../Special-Admin-Panel-Settings/#organization_email_domains)
- Emails from/to addresses/domains [blocklisted from syncing](../Configuring-Activities-Synchronization-Settings/#blocklisting_emails_and_domains) on the [Org level or individual level](../Two-Layers-Blacklisting/)  
- Out-of-the-box (with default config), {{ short_name }} emails and calendar items that have no relevant Business or People records for linking, do not get auto-processed    
- Emails placed into any other folders of your email client but *Inbox*, *Sent*, or the custom *Salesforce Emails* one
- Service emails (see below)  

&nbsp;

#### **6\.** The Add-In / Chrome Extension does **not** work with Service emails

Service email messages cannot be saved in Salesforce or processed in any way, so the Add-In / Chrome Extension cannot be opened for the following types of emails:

*   [MS Outlook message read receipts](http://support.office.com/en-us/article/add-and-request-read-receipts-and-delivery-notifications-a34bf70a-4c2c-4461-b2a1-12e4a7a92141)
*   MS Outlook calendar item acceptance/declining/update notifications
*   MS Outlook delivery failure notifications  

When an email of this kind is selected in MS Outlook Desktop or On the Web version, the *Open {{ product_name }}* icon and related icons are greyed out in [{{ product_name }} Cloud (Web) implementation](../Desktop-MSI-and-Cloud-Web-Implementations-Comparison/#cloud_web_version_features_not_present_in_the_desktop_msi_version); the Sidebar is automatically closed for such emails in [{{ product_name }} desktop/MSI implementation](../Desktop-MSI-and-Cloud-Web-Implementations-Comparison/#desktop_msi_features_not_present_in_the_cloud_web_version).  

&nbsp;

**7.** The is also a [special synchronization setting available on request](../Special-Admin-Panel-Settings/#extra_global_settings) that enables [autosaving](../Configuring-Activities-Synchronization-Settings/#automatic_sharing_of_emails) of outbound emails **only**. Note that enabling this option does not exclude the possibility to save non-outbound emails [using the **Save** button](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#1_saving_an_email_when_smartcloud_connect_synchronization_is_active).  

&nbsp;

**8\.** Note that emails which you saved in Salesforce using the [Save button](../Save-Email-Dialog/#save_email_dialog) or via any other method are auto-assigned the custom blue *Salesforce* category in MS Outlook or the Salesforce label in Gmail, so you can see if you have already processed it. However, that may happen within 1-30 minutes after saving, since categories get assigned by [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/).

{{ product_name }} can also be used to save emails from a [Shared Outlook mailbox](https://support.office.com/en-ie/article/open-and-use-a-shared-mailbox-in-outlook-d94a8e9e-21f1-4240-808b-de9c9c088afd).

&nbsp;

#### **9\.** The "ForceSync" mode

*ForceSync* implies that an email gets saved in one of the following ways: **A.** by [category assigning](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-%28Adaptive-view%29/#3_besides_using_the_save_button_emails_saving_can_be_performed_in_4_more_easy_ways); **B.** by [moving to the dedicated folder](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-%28Adaptive-view%29/#3_besides_using_the_save_button_emails_saving_can_be_performed_in_4_more_easy_ways); **C.** by using the [Save button](../Save-Email-Dialog/) in the [Sidebar](../Introduction/). In other words, it's user-initiated saving, [auto-saving by {{ short_name }} Sync](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_emails_emails_autosharing) 

&nbsp;

* * *

&nbsp;

##### Editing already saved Email Messages via the Sidebar

In the latest updates, it is possible to edit the fields of already saved [Enhanced Email messages](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#11_emails_saved_as_emailmessages_vs_emails_saved_as_tasks) via the Sidebar: SFDC records linked to email (*Related To*): both [WhatID People Records and WhoID Business Records](https://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/), *Subject*, *Body*, and some other key ones. In this scenario, the email gets deleted and then re-created in Salesforce.

To edit an already saved Email Message in Salesforce:

- Select the corresponding email in MS Outlook
- Click on <u>Email is saved</u> in the Sidebar's header
- Edit the fields as needed by clicking the **🖉** (Edit) icon next to them
- Click the **Save** button in the dialog to apply the changes in Salesforce

!!! tip "Tip"
    Note that you can revert the changes by clicking the **⟲** (Undo) icon next to a changed field

&nbsp;

!!! note "Note"
    In order to edit a saved EmailMessage, you should have sufficient access permissions: be the email's Owner allowed to [delete objects of this type from Salesforce](https://help.salesforce.com/articleView?id=000323372&type=1&mode=1).

&nbsp;

* * *

&nbsp;

##### The Magic Anchor feature (used to synchronize emails sent *from Salesforce*)

In addition, {{ product_name }} can be configured to auto-link replies to emails you [send from Salesforce](https://help.salesforce.com/articleView?id=emailadmin_send_email_from_salesforce_overview.htm&type=5) to a single relevant Contact or Lead - only when [the item is handled by sync](../Synchronization-Engine-An-Overview/). [Contact us](mailto:support@revenuegrid.com) if emails sending from Salesforce is often used in your Org and you want to have the recipients' replies linked to a single relevant Contact / Lead.

&nbsp;

* * *

&nbsp;

##### Linking a saved email to a Contact and a [Support Case](https://help.salesforce.com/articleView?id=cases_def.htm&type=5) at the same time

{{ short_name }} can link emails saved as Salesforce Tasks to a Contact and a Support Case at the same time, according to user selections in [Save email dialog](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#1_saving_an_email_when_smartcloud_connect_synchronization_is_active). To perform that, the following Salesforce configuration prerequisite is required:

- Make sure that [Salesforce Email-to-Case](https://help.salesforce.com/articleView?id=customizesupport_enabling_email_to_case.htm&type=5) is enabled in your Org  
- Salesforce setting *Enable Email Drafts for Cases* must be enabled as well. Refer to [this Salesforce help article](https://help.salesforce.com/articleView?id=case_interaction_enabling_email_drafts.htm) to learn how to do that  

&nbsp;

* * *

&nbsp;

##### Saving any emails without linking them 

For special emails saving scenarios requested by some customers, {{ product_name }} also offers the possibility to save any emails with no established relation to any Salesforce records. That is, on creation of the matching Tasks or EmailMessages in Salesforce their [*WhoId* and *WhatId*](https://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) fields are left blank. To enable this function, submit a corresponding request to [our Support team](mailto:support@revenuegrid.com).

&nbsp;

&nbsp;

&nbsp;

Please proceed to the next section of this article to learn how to save an email in Salesforce from {{ product_name }}:  

[Saving Emails in Salesforce: 2. Ways to save an Email](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/)

Also refer to [this article](../Object-Fields-Mapping-Patterns/#ms_outlook_emails) for detailed information on how MS Outlook/Exchange Email and Salesforce Task/Email message fields are matched when an email message is saved in Salesforce via {{ product_name }}.



&#160;
 &#160;

