---
description: How to disable syncronization of specific types of items from your mail client to Salesforce
---
# Choosing What to Downsync from Salesforce to Your Mail Client  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

Besides [emails](../Saving-Emails-in-Salesforce-1.-Function-Overview/), [{{ company_name }} Sync engine](../Synchronization-Engine-An-Overview/) can synchronize with Salesforce the following item types:

*   [Calendar items](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/)  
*   [Tasks](../Synchronization-of-Tasks/)  
*   [Contacts](../Synchronization-of-Contacts/) (incl. focusing of available contacts with a preset [Salesforce view](https://help.salesforce.com/articleView?id=listviews_parent.htm&type=5) filter)  

Using the **General** subtab on the Sync Setting page, you can choose which types of items should be synchronized from Salesforce to Exchange/Office 365 or Gmail ([down-syncing](../Special-Sync-Options-Save-Events-As-Other-&-One-Way-Sync/#one-way_synchronization) only).

!!! warning "Important"
    Note that disabling the switch button for an item type via the Sync Settings page does **not** mean that items of this type won't be synced from your mail client to Salesforce over their usual syncing patterns (see the articles linked above)

<br>

!!! warning "Important"
    Depending on your license, the appearance of your Sync Settings page may be different. Below you can find instructions on how to renew access credentials on the **Legacy** and **New** Sync Settings pages. Proceed with the steps according to the appearance of your Sync Setting page:

    * [New Sync Settings page](#choose_what_to_sync_on_the_new_sync_settings_page)

    * [Legacy Sync Settings page](#choose_what_to_sync_on_the_legacy_sync_settings_page)


&nbsp;

## Choose what to sync on the new Sync Settings page


To choose which records should be down-synced:

**1\.**  [Open the Sync Settings page](../How-to-Open-Sync-Dashboard-(Adaptive-view)/). You will see the General subtab with sections for each item type  


<p><img src="..\..\assets\images\Configuration-&-Settings\User-Settings\what-to-sync\sync-blocks-2.png" class="minimized">
</p>

&nbsp;

**2\.**  Disable or enable Salesforce → mail server synchronization ([down-syncing](../Special-Sync-Options-Save-Events-As-Other-&-One-Way-Sync/#one-way_synchronization)) for different item types using the switch buttons

&nbsp;
* * *

&nbsp;

#### Synchronizing Tasks and Calendar Events

{{ product_name }} only synchronizes those tasks and calendar items which you are an Assignee or Participant of. In addition, to prevent {{ product_name }} from synchronizing outdated and irrelevant tasks and events, it applies [sliding time window](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#meeting_appointment_autosaving) dynamic filtering so only the activities that are presently happening or are coming soon are synchronized. {{ product_name }} uses the following criteria for tasks and calendar events:

*   **Tasks:** {{ company_name }} synchronizes either non-completed tasks or completed tasks which were Due or were Modified over the last 2 weeks. Older tasks are omitted
*   **Calendar Items:** {{ product_name }} only [synchronizes meetings and appointments](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/) which occurred no earlier than 2 weeks in the past from the present date. Older meetings are omitted from syncing. For future calendar items syncing, the limit is 60 days; all calendar items scheduled to occur within 60 days from current date are synchronized with Salesforce

&nbsp;

* * *

&nbsp;

#### Choosing Which Contacts to Synchronize

!!! tip "Tip"
    Also refer to [this article](../Synchronization-of-Contacts/) for more information on managing contacts via {{ short_name }}

For contacts, you can further refine your synchronization criteria:

**1\.** In the **Contacts** block, click **Customize scope**  

<p><img src="..\..\assets\images\Configuration-&-Settings\User-Settings\what-to-sync\customize.png" style="width:80%;">
</p> 

&nbsp;

**2\.** Choose one of the following options: 

<img src="..\..\assets\images\Configuration-&-Settings\User-Settings\what-to-sync\view.png" style="width:50%; display:inline-block; vertical-align:middle; margin-left:10px; float: right">

*   **All available Contacts** – synchronize all available contacts
*   **Only my Contacts** – synchronize your contacts only, that is the contacts where you are a contact owner
*   **Custom Salesforce view** (and then select the desired Salesforce contact view) – synchronize contacts available in the selected Salesforce view only


**3\.** Click **Apply** to save your selection

&nbsp;

* * *

&nbsp;

#### Disabling Server-Side Deletion of Tasks and Contacts

If you do **not** want to have your Tasks or Contacts auto-deleted from Salesforce after you delete them from your mail server:

On the **General** tab, in the necessary block (Tasks or Contacts), enable the **Forbid to remove** switch button to disable Auto-removal from Salesforce for this item type

<p><img src="..\..\assets\images\Configuration-&-Settings\User-Settings\what-to-sync\forbid.png" style="width:80%;">
</p> 

&nbsp;


!!! note "Note"
    If Auto-removal is disabled and the Tasks/Contacts downsyncing switch (see above) is enabled, synchronized Task or Contact removal via the mail client will result in the it being restored by [{{ short_name }} Synchronization](../Synchronization-Engine-An-Overview/) on the following sync session



 
<br> 
<hr>
<br>

## Choose what to sync on the legacy Sync Settings page 
 
 
 Via the Dashboard's *Filters* tab, you can choose which types of items should be synchronized from Salesforce to Exchange/Office 365 or Gmail ([down-syncing](../Special-Sync-Options-Save-Events-As-Other-&-One-Way-Sync/#one-way_synchronization) only).

!!! warning "Important"
    Note that disabling the switch for an item type via Dashboard Filters does **not** mean that items of this type won't be synced from your mail client to Salesforce over their usual syncing patterns (see the articles linked above)

&nbsp;

To choose which records should be down-synced, do the following:

**1\.**  [Open the Dashboard](../How-to-Open-Sync-Dashboard-(Adaptive-view)/) and go to the **Sync settings > Filters** page. You will see blocks with each item type  

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5832d745903360645bfa692e.png" class="minimized">
</p></details>

&nbsp;

**2\.**  Disable or enable Salesforce → mail server synchronization ([down-syncing](../Special-Sync-Options-Save-Events-As-Other-&-One-Way-Sync/#one-way_synchronization)) for different item types using the switch buttons

&nbsp;
* * *

&nbsp;

#### Synchronizing Tasks and Calendar Events

{{ product_name }} only synchronizes those tasks and calendar items which you are an Assignee or Participant of. In addition, to prevent {{ product_name }} from synchronizing outdated and irrelevant tasks and events, it applies [sliding time window](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#meeting_appointment_autosaving) dynamic filtering so only the activities that are presently happening or are coming soon are synchronized. {{ product_name }} uses the following criteria for tasks and calendar events:

*   **Tasks:** {{ company_name }} synchronizes either non-completed tasks or completed tasks which were Due or were Modified over the last 2 weeks. Older tasks are omitted
*   **Calendar Items:** {{ product_name }} only [synchronizes meetings and appointments](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/) which occurred no earlier than 2 weeks in the past from the present date. Older meetings are omitted from syncing. For future calendar items syncing, the limit is 60 days; all calendar items scheduled to occur within 60 days from current date are synchronized with Salesforce

&nbsp;

* * *

&nbsp;

#### Choosing Which Contacts to Synchronize

!!! tip "Tip"
    Also refer to [this article](../Synchronization-of-Contacts/) for more information on managing contacts via {{ short_name }}

For contacts, you can further refine your synchronization criteria:

**1\.** In the **Contacts** block, click **Customize**  

   ![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5832d830c697916f5d05300b.png)  

&nbsp;

**2\.** Choose one of the following options: 

   ![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5832d7ca903360645bfa6937.png)
&nbsp;

*   **All contacts** – synchronize all available contacts
*   **Only my contacts** – synchronize your contacts only, that is the contacts where you are a contact owner
*   **Custom view** (and then select the desired Salesforce contact view) – synchronize contacts available in the selected Salesforce view only

**3\.** Click **Save** to save your selection

&nbsp;

* * *

&nbsp;

#### Disabling Server-Side Deletion of Tasks and Contacts

   If you do **not** want to have your Tasks or Contacts auto-deleted from Salesforce after you delete them from your mail server, do the following:

**1\.**  In the Dashboard, under **Sync settings**, click **Detailed Settings** 

<p><img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\574d86df9033605108fde722.png" class="minimized">
</p>

&nbsp;

**2\.**  Toggle the switch button to disable Auto-removal from Salesforce for this item type.

!!! note "Note"
    If Auto-removal is disabled and the Tasks/Contacts downsyncing switch (see above) is enabled, synchronized Task or Contact removal via the mail client will result in the it being restored by [{{ short_name }} Synchronization](../Synchronization-Engine-An-Overview/) on the following sync session



&#160;
 &#160;

