---
description: The basics of attached files handling mechanisms (for regular users)
---
# Attached Files Handling Mechanisms (User level article)  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*7 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

Files attached to emails and events can be saved in Salesforce [as Content documents (Files) or as Attachment objects](../Customization-Settings-Explained/#9_configure_attachments_saving_in_salesforce), the former being the default way. In either case the files are stored in Salesforce under **Notes & Attachments** of the primary associated object(s).

Saving attachments as Content documents has the advantages of file duplicates prevention in Salesforce storage and file keeping optimization, so it is the recommended way, while the other way is only used when saving attachments as Content documents cannot be enabled.

For Admin level/setup information about handling of attached files, please refer to [this article](../Attachments-Handling-(Advanced)/).

&nbsp;

### Limitations

{{ product_name }} **cannot** save in Salesforce attachments in the following cases:  

- items attached to emails as OneDrive or another cloud location links  
- attachment [added to the email inline](https://www.lifewire.com/insert-inline-image-outlook-1173700)  
- attached files cannot be saved in Salesforce from an email opened in [Compose mode](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/)

&nbsp;

### **Saving Email attachments**

!!! note "Note"
    Please note that several specific aspects of attachment saving/linking mechanisms can be adjusted upon request sent to [our Support team](mailto:support@revenuegrid.com); the patterns described in the article are valid for default setup. For example, in the latest {{ product_name }} the *SalesforceEmailLinkContentToBusinessObject* setting is enabled for all instances by default. That means email attachments saved in Salesforce as Content Files will be linked to related business records besides the Task/Email Message object in Salesforce

&nbsp;

**1\.** If you save an attachment manually along with an email message or event, [by selecting the email/event, marking relevant records in the Sidebar, and clicking the **Save** button in the Sidebar's header](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/), in Salesforce the attachment will be linked only to the Task or [Email message](http://help.salesforce.com/articleView?id=emailadmin_enhanced_email_overview.htm) object created, and the Task/Email message object will be linked to selected objects (which are also specified in the **Name** and **Related to** fields of the *Record email as Activity to Salesforce* dialog)

![](../assets/images/Using-SmartCloud-Connect/How-It-Works/Handling-Email-Attachments/save_dial_2.png)

&nbsp;

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-It-Works\Handling-Email-Attachments\in_SF1.png" class="minimized">
</p>

&nbsp;


**2\.** If you save an attachment manually in one of the [following ways](../All-User-Actions-in-Add-In-Sidebar/#8_more_convenient_email_event_attachments_saving)

* by expanding a record's details and then clicking on **+** (Add) next to *Attachments*

* by clicking **Attach** next to a file listed in the **Files** tab on a record's card or

* by selecting **Attach files** from [the picklist of actions available for a record](../All-User-Actions-in-Add-In-Sidebar/#3_all_key_actions_at_hand)

In these cases the file will be linked only to this specific record.

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-It-Works\Handling-Email-Attachments\in_SF2.png" class="minimized">
</p>

&nbsp;



**3\.** If you save an attachment by assigning the *Salesforce* category to the email/event containing it, it will be saved in Salesforce by [{{ company_name }} synchronization](../Synchronization-Engine-An-Overview/). In this case the attachment can be linked *only* to the corresponding Task/Email message object, while the Task/Email message itself will be linked via the *Name* and *Related to* fields to the relevant Lead/Contact and Account and available Case or Opportunity records (with [linking to Opportunities](../Configuring-Activities-Synchronization-Settings/#linking_to_opportunities) enabled) found by [{{ product_name }} Initial Search](../Initial-Search-and-Applied-Record-Filters/), and the record Owner's profile.  

Note that unlike in the case of manual email/event saving (see point ( **1** ) ), there is no way to save the "default attachment" (the email message in *.eml* format) when the email gets saved in Salesforce by [Sync Engine](../Synchronization-Engine-An-Overview/).

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-It-Works\Handling-Email-Attachments\owner_files.png" class="minimized">
</p>

&nbsp;


**4\.** If [email/event autosaving is enabled](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_emails_emails_autosharing) in sync settings and an email/event containing attachments is received from or sent to a known (registered in Salesforce) contact, on the following synchronization session the email will get saved in Salesforce along with the attachment(s). In this case the linking patterns will be the same as in point ( **3** ). Note that auto-sharing of messages containing attachments should not consume an excessive amount of Salesforce storage space since prevention of storing of duplicates and specific file type/size filtering is applied

!!! note "Note"
    Please pay attention that the patterns described in points 3-4 are only applicable for saving attachments as Content document files; if Attachment objects are used instead the files will be linked only to the corresponding Task/Email message object

&nbsp;

!!! warning "Important"
    To be able to view these files linked to an Activity object (Task or Email message) in Salesforce, make sure to enable the [Related lists > File object to the Task object's page layout](http://help.salesforce.com/articleView?id=admin_files_related_list_setup.htm&type=5) in [Object management settings](http://help.salesforce.com/articleView?id=extend_click_find_objectmgmt_parent.htm&type=5)

&nbsp;
* * *

&nbsp;

### Automatic pre-selection of attachments to be saved in Salesforce

In the latest {{ short_name }} updates the end users can set how files attached to emails or calendar items should be handled by default in the [Save Event dialog](../Save-Email-Dialog/), through pre-selection. A corresponding setting is located at the bottom of the right pane of [{{ short_name }} Customization settings](../Customization-Settings-Explained/#1_how_to_open_customization_page). The available options are:
![](../assets/images/Using-SmartCloud-Connect/How-To-s/Attachments/autoselection.png)
&nbsp;

- **Only autoselect files > 100 kB** - this option allows to prevent saving in Salesforce of small images or animations attached to an email/calendar item as part of the signature, for example; however, the users will be able to select them, if needed
- **Autoselect all attached files** - this option means that any attached files will be autoselected to be saved in Salesforce; but the users will be able to unselect unneeded attachments
- **Do not autoselect attached files** - this option means that no attached files will be autoselected; but the users will be able to select needed files

&nbsp;

* * *

&nbsp;

### The "default attachment" .eml copy of an email

Please also note that if you need to:

* save an exact copy of the email message including all technical delivery data and headers, for example to use it as legal evidence

* if [Salesforce Enhanced email](https://help.salesforce.com/articleView?id=emailadmin_enhanced_email_overview.htm) is not enabled in your Salesforce Org and you need to save special  HTML formatting in the email (e.g. inline tables, diagrams, and so on), or the email's body exceeds the 32,000 characters limit and you need to save the message in Salesforce without truncation applied

in these cases you can attach an exact copy of the message in .eml format to created Task or Email message Salesforce object, to do that select the checkbox next to the "default attachment" *{email subject line}.eml* generated for every email message; note  that you can also rename the .eml file according to your preferences.

![](../assets/images/Using-SmartCloud-Connect/How-It-Works/Handling-Email-Attachments/email_as_act_dial.png)

&nbsp;

The possibility to save this "default attachment" .eml file in Salesforce can be disabled by request sent to [{{ company_name }} support team](mailto:support@revenuegrid.com).



!!! warning "Important"
    Please note that an email attachment cannot be auto-saved in Salesforce by {{ company_name }} synchronization in the following cases: 1. if it exceeds the file size limit in Salesforce, 25 Mb for a single file; 2. if the file's extension is blocklisted in the Global settings managed by [our Support team](mailto:support@revenuegrid.com) or is not allow-listed in [local Admin panel settings](../Special-Admin-Panel-Settings/). However, in the latter case the file can be [saved in Salesforce manually](../All-User-Actions-in-Add-In-Sidebar/#8_more_convenient_email_event_attachments_saving)

&nbsp;

!!! note "Note"
    Please note that with [Salesforce Enhanced email](https://help.salesforce.com/articleView?id=000239922&type=1) enabled, due to a technical limitation, when you save an email along with its attachments in Salesforce via {{ product_name }}, the created Email message object's *HasAttachment* field does not convey accurate information about the presence of these attachments, so this flag/field should be disregarded

&nbsp;

&nbsp;

* * *

&nbsp;

### Saving Files Attached to Calendar Items

Out-of-the-box, saving of event attachments by {{ short_name }} is disabled; in order to enable it you need to send a corresponding request to [{{ company_name }} support team](mailto:support@revenuegrid.com).

Saving in Salesforce of files attached to meetings is performed on [{{ short_name }} Synchronization sesions](../Synchronization-Engine-An-Overview/), along with [saving of the Meetings themselves](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/) as [matching Salesforce Event objects](../Object-Fields-Mapping-Patterns/#ms_outlook_calendar_items).

On saving, the files are linked to created Event objects, they can only be saved as [Salesforce Attachment objects](https://help.salesforce.com/articleView?id=collab_files_differences.htm&type=5) and **not** as Content Documents.

&nbsp;

* * *

&nbsp;

#### Special considerations applied on calendar item attachments saving

**1\.** The attached files' size + the event's body should not exceed 25 Mb  

**2\.** If the *[Don't allow HTML uploads as attachments or document records](https://help.salesforce.com/articleView?id=admin_files_type_security.htm&type=5)* security setting is enabled for your Org, you cannot upload files with the following file extensions: *.htm*, *.html*, *.htt*, .*htx*, *.mhtm*, *.mhtml*, *.shtm*, *.shtml*, *.acgi*, *.svg*  

**3\.** Attachments saving is not supported for a single event belonging to a series of recurring events  

**4\.** A file [extension](../Special-Admin-Panel-Settings/#email_attachment_extensions_whitelist) filter managed via [{{ short_name }} Admin panel](../Special-Admin-Panel-Settings/) and file size filters managed by [{{ company_name }} support team](mailto:support@revenuegrid.com) are applied to prevent saving of potentially unsafe files and various small images from invite signatures  

**5\.** All files attached to the calendar item which pass the above listed filters will get synced, there is no way to select a specific one to be saved

&nbsp;

* * *

&nbsp;

#### Attachments linking to [Salesforce Business records](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) on auto-saving

When MS Outlook calendar items are synchronized in Salesforce [automatically](../Saving-Calendar-Items-in-Salesforce-%28Adaptive-view%29/#meeting_appointment_autosaving) or [semi-automatically](../Saving-Calendar-Items-in-Salesforce-%28Adaptive-view%29/#saving_calendar_items_semi-automatically) by [{{ short_name }} sync engine](../Synchronization-Engine-An-Overview/), files attached to them can [optionally](../Special-Admin-Panel-Settings/#extra_configuration_settings) be processed as well; by default this features is disabled. If attached files auto-syncing is enabled for an Org, all files meeting the above listed criteria will be saved in Salesforce along with the calendar item, as [Content Documents](https://developer.salesforce.com/docs/atlas.en-us.sfFieldRef.meta/sfFieldRef/salesforce_field_reference_ContentDocument.htm) linked to the matching Calendar Event as well as all relevant [Business objects (WhatId)](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/).

&nbsp;

&nbsp;

* * *

&nbsp;

### Attachments added as Google Drive links in [{{ short_name }} Chrome Extension for Gmail](../Chrome-Extension-Intro/)

[{{ product_name }} implementation for Gmail](../Chrome-Extension-Intro/) also supports [saving](../Using-the-Solution-for-Salesforce-and-Gmail/#saving_emails_in_salesforce) and [auto-saving](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_emails_emails_autosharing) in Salesforce of files attached to email messages as [Google Drive links](https://support.google.com/mail/answer/2487407?co=GENIE.Platform%3DDesktop&hl=en), these links are parsed by the Chrome Extension and handled via the [Save email dialog](../Save-Email-Dialog/) as any other attachments.

This feature can optionally be disabled for Enterprise {{ short_name }} customers by request sent to [RevenueGrid.com CSM team](mailto:support@revenuegrid.com) using a [Special {{ short_name }} setting](../Special-Admin-Panel-Settings/#extra_configuration_settings) *GoogleDisableDriveAttachments*.

&nbsp;


<style>
  .banners {
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .banners a.button {
      background-color: #FFC827;
      color: #2F3341;
      box-shadow: 0 5px 35px rgba(146, 146, 146, 0.2);
      padding: 20px;
      font-family: Graphic, arial;
      font-weight: 600;
      line-height: 24px;
      margin-top: -100px;
      border-radius: 3px;
      cursor: pointer;
      transition: .1s;
  }

  .banners a.button:hover {
    transform: scale(1.05);
  }

  .banners a.button a:hover,
  .banners a.button a:visited {
      color: #2F3341;
  }

  .banner-3 a.button {
    margin-left: 45%;
  }
</style>

<br>
<div class="banners banner-3">
  <img src="../../assets/images/banners/banner-3.svg" style="width: 100%; height: 100%;">
  <a class="button" href="https://revenuegrid.com/sign-up/?utm_source=kb_rg&utm_medium=referral&utm_campaign=eac&utm_content=banner" target="_blank">Try {{ company_name }} for free</a>
</div>