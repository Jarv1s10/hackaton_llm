---
description: Learn how to work with Save Email / Save Event dialogs in RG Email Sidebar
---
# The Updated Save Email / Save Event Dialogs  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*8 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! tip "Tip"
    If you prefer to save your business communication and meetings in Salesforce automatically or semi-automatically, make use of the [smart and flexible auto-saving options](../Autosaving-Patterns/) included in {{ product_name }}

&nbsp;



The Save dialog appears after you select an email or calendar item in MS Outlook or Gmail Inbox or Sent folder and click the Save button in [{{ product_name }}](../Introduction/) in order to get the item saved in Salesforce. Refer to the articles on [saving emails](../Saving-Emails-in-Salesforce-1.-Function-Overview/) and [syncing calendar items](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/) for more details.

The Save button might be disabled in two cases: if a [service email is selected](../Saving-Emails-in-Salesforce-1.-Function-Overview/#under_the_hood_mechanisms_and_special_patterns_applied_on_emails_saving) or saving is disabled for all object types in *Disallow saving:* [customization setting](../Customization-Settings-Explained/). Also see [this article](../All-User-Actions-in-Add-In-Sidebar/#11_email_event_saving_status_indication_in_sidebar_header) for information on save status indications.

&nbsp;

If this saving pattern is used, MS Exchange / Office 365 or Gmail emails get saved directly by [{{ short_name }} Add-In](../AddIn-vs-Sync-Functions/) in [Read mode](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#2_when_revenue_grid_sync_is_not_active) or by [{{ short_name }} sync engine](../Synchronization-Engine-An-Overview/) in [Compose mode](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#2_when_revenue_grid_sync_is_not_active). In the latter case emails are saved in Salesforce on the following scheduled sync session (within 1-30 minutes). See [this article](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#3_besides_using_the_save_button_emails_saving_can_be_performed_in_4_more_easy_ways) for information on other saving methods.

&nbsp;

&nbsp;

### Save Email dialog

Via this dialog you can:

- Find in Salesforce and select [People and Business record(s)](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) you want to link to the matching Task or Email message object in Salesforce  
- Set the resulting [Salesforce Task](https://help.salesforce.com/articleView?id=tasks.htm&type=5)'s Priority and Status and modify its Subject, if necessary. Or, if [Salesforce Enhanced email](https://help.salesforce.com/articleView?id=emailadmin_enhanced_email_overview.htm&type=5) is enabled in your Org, the resulting [EmailMessage items](https://help.salesforce.com/articleView?id=000313606&type=1&mode=1)'s Subject  
- Mark the attached file(s) you want to [save in Salesforce](../Attachments-Handling-(Basic)/) along with the email, if any; modify the files' names, if necessary  
- Define if you want to auto-save in Salesforce future emails in the same correspondence thread (the *Auto-save new emails within this thread*  checkbox at the bottom). See [this article](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_email_threads) for more information


&nbsp;



![](../assets/images/Using-SmartCloud-Connect/How-To-s/Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/new_save_email_dialog.png)

&nbsp;

To proceed with saving, you need to select People records ([WhoId](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/)) and Business records ([WhatId](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/)) to be linked to the saved email in Salesforce under **Linked records**  – unless the relevant objects have already been retrieved and added by [{{ short_name }} initial search](../Initial-Search-and-Applied-Record-Filters/). Use the *Search Salesforce records* field to find these objects in Salesforce and select them; to remove an object from the list, clear the checkbox on the right-hand side. 

Note that this field is now unified, used for both these object classes. To ensure proper linking according to your [{{ product_name }} settings](../Customization-Settings-Explained/) and Salesforce configuration, the dialog indicates it if there are conflicts in linking of selected objects. See [this article](../Activities-Linking/) to learn more about linking rules.

You can also select or deselect all auto-retrieved related records using a corresponding checkbox above

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Working-with-Activities\select-all.png">
</p></details>

&nbsp;

After related records to be linked have been selected, you may proceed to handling files attached to the email. In the  **Attachments **section, you can select attachments to be saved in Salesforce along with the email. Note that you can also change the files' names on saving, by clicking the **🖉** (Edit) icon next to their names.

In the list you will also see an extra *.eml* file, it is an exact copy of the email that you can save along with the attachments. Refer to [this article](../Attachments-Handling-(Basic)/) for more information. 

!!! note "Note"
    An email attachment cannot be saved in Salesforce in the following cases: **1.** if it exceeds the file size limit in Salesforce – 25 Mb per file; **2.** if the file's extension was not [allow-listed by your local {{ short_name }} Admin](../Special-Admin-Panel-Settings/)

!!! warning "Important"
    Please note that with [Salesforce Enhanced email](http://help.salesforce.com/articleView?id=000239922&type=1) enabled, due to a technical limitation, when you save an email along with its attachments in Salesforce via {{ product_name }}, the created Email Message object's *HasAttachment* field will not convey accurate status regarding the presence of attachments, so this field/flag should be disregarded

&nbsp;

In addition, you can edit the values in the saved item's **Other fields**, these are the key fields of the corresponding [Task](https://help.salesforce.com/articleView?id=task_fields.htm&type=5) or [EmailMessage](https://help.salesforce.com/articleView?id=000313606&type=1&mode=1) objects defines in [{{ short_name }} Customization Settings](../Customization-Settings-Explained/#61_selecting_which_fields_to_show).  
By default, for Task objects you can edit the **Subject**, **Priority**, **Status** (set to *Completed* if you do not prefer to set another value), and for EmailMessage objects you can edit the **Subject** field.

!!! tip "Tip"
    You can add more editable fields to the dialog via [{{ product_name }} customization settings](../Customization-Settings-Explained/#8_customizing_detailed_card_view). There you need to select the Task or EmailMessage object type respectively, and then in the object's Detailed view mark the fields you want to edit via the dialog as *Important* or *Required*

&nbsp;

In addition, if [*Automatic Saving of Email Threads*](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_emails_emails_autosharing) is enabled in your [{{ short_name }} Sync settings](../How-to-Open-Sync-Dashboard-(Adaptive-view)/), you can select the **Auto-save new emails within this thread** checkbox at the bottom of the dialog to get all future emails from/to this correspondent saved in Salesforce automatically, without your involvement.

After populating all necessary fields, click the **Save** button in the upper right corner of the dialog to save the email in Salesforce. Please note that {{ short_name }} passes the special values from email fields populated by the users in Save dialog to all subsequent synced emails, i.e., whatever the user selected for the first email will be the same for all new emails in a thread.

When the email is successfully saved in Salesforce, a success toast notification pops up, signaling that the email was saved in Salesforce and (linked to) *{number of related records}* other objects. Besides, after the email is saved, it will be assigned the blue **Salesforce** category in MS Outlook.



![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b72c7690428631d7a89f398.png)

&nbsp;

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b72d49d0428631d7a89f415.png" class="minimized">
</p>

If [{{ short_name }} synchronization](../Synchronization-Engine-An-Overview/) is active, the user-side differences between saving messages in Read mode and Compose mode is the kind of notification you will get (see the screenshots above) and the fact that messages opened in Compose mode will be saved in Salesforce on the following sync session (within 1-30 minutes), unlike messages opened in Read mode, which are saved immediately.

The Salesforce object created when saving an email is logged in {{ product_name }} **Past activities** under the tab **Activity Timeline** and can be opened in Salesforce directly by clicking the blue **Expand** icon next to it.

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b72c8ae2c7d3a03f89dabdc.png)

&nbsp;

* * *

&nbsp;

#### Editing saved Email's body

In the latest {{ product_name }} updates, there is an optional feature that allows editing emails' bodies on saving to Salesforce. The feature is managed by the setting *Edit email body in Save dialog* in [Customization Settings](../Customization-Settings-Explained/). Note that it's <u>not</u> available in most configurations, unless specifically requested by contacting [our CSM team](mailto:support@revenuegrid.com), this option can be requested by {{ short_company_name }} customers.

This feature's limitations: only bodies of emails saved in [Read mode](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-%28Adaptive-view%29/#2_when_revenue_grid_sync_is_not_active) can be edited on saving; HTML formatting is not supported; it is <u>not</u> available for [Enhanced Emails](https://help.salesforce.com/articleView?id=emailadmin_enhanced_email_considerations.htm&type=5) – that is, only matching [Tasks' Descriptions](https://help.salesforce.com/articleView?id=task_fields.htm&type=5) can be edited. Finally, email bodies exceeding the field's limit (32k characters by default) get auto-truncated.

&nbsp;

* * *
&nbsp;

#### Special considerations: what combinations of records can be linked to saved emails

*Case 1*. If [Allow creating duplicated emails](../Item-Deduplication-Mechanisms/#allow_creating_email_duplicates_in_salesforce) is enabled in {{ company_name }} sync settings, up to 16 objects of different types can be linked via the dialog, the extra objects actually being linked to the clones of the email created in Salesforce by {{ product_name }}.

&nbsp;

*Case 2*.  [Allow creating duplicated emails](../Item-Deduplication-Mechanisms/#allow_creating_email_duplicates_in_salesforce) is disabled, [Salesforce Enhanced email](https://help.salesforce.com/articleView?id=000313606&type=1&mode=1) is **not** enabled, and a Lead is selected to be linked. In this case no other objects can be linked, according to the general Leads processing logics in Salesforce. Similarly, if any other object type was selected, no Lead can be added for linking.

And if a Contact was selected to be linked, no more [People records (WhoId)](https://developer.salesforce.com/forums/?id=906F00000008wZlIAI) can be added but [Business records](https://developer.salesforce.com/forums/?id=906F00000008wZlIAI) can.

&nbsp;

*Case 3*. If [Salesforce Enhanced email](https://help.salesforce.com/articleView?id=000313606&type=1&mode=1) is enabled in your Org and [EmailMessages type was configured in {{ short_name }} Customization settings](../Customization-Settings-Explained/#63_defining_the_searchview_scope), and therefore your emails are saved in Salesforce as EmailMessage objects instead of Tasks, plus [Allow creating duplicated emails](../Item-Deduplication-Mechanisms/#allow_creating_email_duplicates_in_salesforce) (see Case 2) is disabled.

In this scenario, saved emails can be linked to several People records ([WhoId](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/)) (a Lead, Contact, Person Account) and to a single Business record ([WhatId](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/)) only.

&nbsp;
&nbsp;

* * *

&nbsp;

### Save Event Dialog

The *Save this event to Salesforce* dialog appears when you open a sent calendar item in MS Outlook (or Gmail) calendar and click the *Save* button in [{{ product_name }}](../Introduction/). It is used to initiate [the item's synchronization](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/) in Salesforce, linked to relevant  People and Business records.

!!! warning "Important"
    Note that calendar items can only be synced with Salesforce after they are sent

![](../assets/images/Using-SmartCloud-Connect/How-To-s/Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/save_dialog.png)

&nbsp;

To proceed with saving, you need to select People records ([WhoId](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/)) and Business records ([WhatId](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/)) to be linked to the synced calendar item in Salesforce under **Linked records**  – unless the relevant objects have already been retrieved and added by [{{ short_name }} initial search](../Initial-Search-and-Applied-Record-Filters/). Use the *Search Salesforce records* field to find these objects in Salesforce and select them; to remove an object from the list, click the **x** icon on the right-hand side. 

Note that this field is now unified, used for linking objects from both these categories. Since, unlike a Task or EmailMessage, a [Salesforce Event](https://help.salesforce.com/articleView?id=event_fields_lex.htm&type=5) can be linked to a number of [Business and People records](https://www.forcetalks.com/salesforce-topic/what-is-the-difference-between-whoid-and-whatid-how-can-we-associate-the-task-with-the-salesforce-opportunity-using-whatid), there are no linking conflicts/limitations applicable for this field.

&nbsp;

&nbsp;

#### Relevant Account pre-selection

For faster calendar items handling {{ product_name }} can be configured to pre-select an associated Account in the "Save Event" dialog if the Save button was clicked on a specific Contact in the [Sidebar](../Introduction/). The feature doesn't work for Gmail.

&#160;
 &#160;


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