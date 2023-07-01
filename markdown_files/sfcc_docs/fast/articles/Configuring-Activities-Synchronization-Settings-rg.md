---
description: Detailed overview of RG Email Sidebar activities synchronization settings
---
# {{ company_name }} Synchronization Settings Explained  
  
**[new Sync Settings page]**

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*4 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! warning "Important"
    Depending on your product license, **the appearance of your Sync Settings page may differ from the one described below**. If you see a different Sync Settings page, refer to [this article](../Configuring-Activities-Synchronization-Settings/).

&nbsp;

!!! tip "Tip"
    Some Synchronization features require adding certain auxiliary fields and classes to Salesforce objects; to get them added automatically ask your local Salesforce administrator to install the [{{ company_name }} managed Salesforce app](../Admin-Managed-Package/) in your Org – it will enable the full scope of {{ short_name }} features on the Salesforce side

&nbsp;

{{ product_name }} includes a number of settings that define how Emails, Calendar items, Contacts, or Tasks are processed into Salesforce.

This article explains all [{{ short_name }} Sync Engine](../Synchronization-Engine-An-Overview/) settings which can be managed by individual users or in bulk by [the Admins](../How-to-Log-In-to-the-Admin-Panel/). The Dashboard's functions and Sync settings are mostly identical for MS Exchange / Office 365 and Gmail accounts, with the exception of several [MS Exchange specific functions](../Using-the-Solution-for-Salesforce-and-Gmail/#differences_between_the_exchangeoffice_365_add-in_implementation_and_the_chrome_extension_for_gmail).

<p><img src="../../assets/images/Configuration-&-Settings/User-Settings/new-sync-settings-page/new-sync-settings.png" style="width:90%;"></p>

&nbsp;


&nbsp;
***
&nbsp;

### To access Sync settings:

In {{ product_name }}, click **Menu** and go to **Open {{ company_name }} in browser**. Next, click on your profile picture in the upper right hand side corner, then go to **Settings** > ** Sync** section  

<br>
The Sync Settings section includes four tabs:

<p style="margin-left: 5%">
<b>General</b> where you can change the general sync patterns for Events, Calendar items, Tasks and Contacts, and view the last sync session's, force or pause sync
<br><br>
<b>Issues</b> where you will see all sync issues, their descriptions and related objects
<br><br>
<b>Linking rules</b> where you can configure linking of saved items to Opportunities in Salesforce
<br><br>
<b>Blocklist</b> where you can manage the blocklisted email addresses and email domains

</p>

&nbsp;

* * *

&nbsp;

## Emails saving

<p><img src="../../assets/images/Configuration-&-Settings/User-Settings/new-sync-settings-page/emails.png" style="width:50%; display:inline-block; vertical-align:middle; margin-left:1px;float: right"></p>

You can manage automatic emails saving patterns in the **Emails** box on the **General** tab. 



<br><br>

### Automatic Saving of Emails (emails autosharing)


!!! tip "Tip"
    Also see [this article](../Special-Admin-Panel-Settings/#auto-saving_and_blocklist_intersections) for detailed information on auto-saving flow options and blocklist intersections

&nbsp;

You can get all relevant (see point **5** in [this article](../Saving-Emails-in-Salesforce-1.-Function-Overview/#under_the_hood_mechanisms_and_special_patterns_applied_on_emails_saving)) incoming and outgoing email messages (*Inbox* and *Sent* folders) automatically saved in Salesforce. With automatic saving enabled, your email messages will be automatically saved as Salesforce Tasks or [Email messages](http://help.salesforce.com/articleView?id=emailadmin_enhanced_email_overview.htm&type=5) linked to related Contacts, Leads, and other Salesforce objects retrieved according to [these principles](../Initial-Search-and-Applied-Record-Filters/#the_resulting_related_records_list_will_include). Emails autosaving is performed not immediately but on the following [synchronization session](../Synchronization-Engine-An-Overview/).  


If you receive or send an email from/to an unresolved (not previously registered in Salesforce) Contact or Lead, {{ product_name }} can create a relevant Salesforce automatically to autosave it. See [this article](../Synchronization-Engine-An-Overview/#automatic_creation_of_contacts_or_leads_by_rg_email_sidebar_autoresolving) for more information.

<br>

<p><img src="../../assets/images/Configuration-&-Settings/User-Settings/new-sync-settings-page/auto-saving.png" style="width:50%; display:inline-block; vertical-align:middle; margin-left:1px;float: right"></p>

To enable or disable automatic emails saving by {{ short_name }}: in the **Emails** block, toggle the **Enable Auto-Saving** switch button.


&nbsp;

&nbsp;

#### Inbox Spam Handling Prevention

With enabled Emails auto-saving and set up Leads or Contacts auto-resolving in your cofiguration, {{ product_name }} will process SPAM emails from non-blocklisted email domains which get through to your MS Outlook or Gmail Imbox.

Refer to [this article](../Inbox-SPAM-Handling-in-RG-Email-Sidebar/) for сomplete information on inbox spam handling prevention with {{ product_name }}.

&nbsp;

* * *

&nbsp;

### Automatic saving of Email Threads


With {{ short_name }}, you can automatically save emails in a marked thread. See [this article](../Save-All-Emails-in-a-Thread/) for complete information on how to use this feature.

&nbsp;

<p><img src="../../assets/images/Configuration-&-Settings/User-Settings/new-sync-settings-page/auto-saving-thread.png" style="width:50%; display:inline-block; vertical-align:middle; margin-left:1px;float: right; margin-top:1rem;"></p>

To enable this feature: in the *Emails* box, set the **Auto-Save All Emails In a Thread** switch to Enabled.


<br><br>
!!! warning "Important"
    After you toggle the **Auto-save all emails in thread** setting, for the changes to be applied you must [log out from {{ short_name }} Add-In](https://docs.revenuegrid.com/ri/fast/assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b3a275f0428630abc0ba0da.png) and then [re-log in](../How-to-Install-and-Run-the-Solution-all-configurations/#ii_rg_email_sidebar_logon)

&nbsp;
&nbsp;

* * *

&nbsp;

## Calendar items saving

<p><img src="../../assets/images/Configuration-&-Settings/User-Settings/new-sync-settings-page/events.png" style="width:50%; display:inline-block; vertical-align:middle; margin-left:1px;float: right;"></p>

You can manage the automatic calendar items saving patterns in the **Events** box on the **General** tab. 


<br><br><br>
### Automatic Syncing of [Calendar Items](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/) (events autosharing)

You can have all your incoming and outgoing Calendar items automatically synced in Salesforce, with specific exceptions listed in [this article](../Calendars-Syncing-Exceptions/). Note that {{ short_name }} will also auto-create new Salesforce records to sync meetings which involve new business contact, see [this article](../Synchronization-Engine-An-Overview/#automatic_creation_of_contacts_or_leads_by_rg_email_sidebar_autoresolving) to learn the details.

With automatic meetings syncing enabled, your meetings will be automatically synced up to your Salesforce calendar and also to the calendars of your colleagues who use {{ product_name }}, if they were invited.

!!! note "Note"
    Syncing of new Calendar items and their updates can also be performed within several minutes, via [instant syncing](../Synchronization-Engine-An-Overview/#instant_sync_of_calendar_items). This option can be enabled upon request

&nbsp;

<p><img src="../../assets/images/Configuration-&-Settings/User-Settings/new-sync-settings-page/meetings.png" style="width:50%; display:inline-block; vertical-align:middle; margin-left:1px;float: right;"></p>

To enable automatic syncing of meetings, toggle the **Auto-save meetings** switch button.


<br><br><br>

!!! note "Note"
    If all of the meeting's attendees are blocklisted, the meeting will **not** be synced up to Salesforce. But if at least one meeting's attendee is not on the blocklist, the calendar item will be synced with Salesforce 
<br><br>
<p><img src="../../assets/images/Configuration-&-Settings/User-Settings/new-sync-settings-page/appointments.png" style="width:50%; display:inline-block; vertical-align:middle; margin-left:1px;float: right;"></p>

With automatic syncing of appointments enabled, your appointments will be automatically synced with your Salesforce calendar. To enable automatic saving of appointments, toggle the **Auto-save appointments** switch button.



<br>
<br>

### Events down-syncing from Salesforce to mail client’s calendar


In *Events* box, you can also configure down-syncing of calendar items from Salesforce to your mails client's calendar using **Sync my Salesforce calendar** switch button.

If you create an Event or modify an existing Event directly in Salesforce, these Salesforce Calendar updates get automatically down-synced by {{ short_name }} Sync engine: the corresponding calendar item will be automatically created or modified in MS Outlook or Gmail Calendar. Events modifications get to email client’s calendar within 1-30 minutes but new created Events get down-synced instantly.

<br>
<p><img src="../../assets/images/Configuration-&-Settings/User-Settings/new-sync-settings-page/events-sync.png" style="width:50%; display:inline-block; vertical-align:middle; margin-left:1px;float: right;"></p>

To enable automatic down-syncing of events from Salesforce to your mail client’s calendar, toggle the **Sync my Salesforce calendar** switch button.


<br><br><br>
!!! warning "Important"
    Note that if you disable this switch button, the calendar items that were created in Salesforce and down-synced from Salesforce to your mail client will be removed from your mail client’s calendar.


!!! tip "Tip"
    Refer to [this article](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#events_down-syncing_from_salesforce_to_mail_clients_calendar) for more details on events down-syncing from Salesforce to mail client's calendar.

&nbsp;

* * *

&nbsp;

## Tasks saving

{{ product_name }} only synchronizes those tasks which you are an Assignee of. In addition, to prevent {{ product_name }} from synchronizing outdated and irrelevant tasks, it applies sliding time window dynamic filtering so only the activities that are presently happening or are coming soon are synchronized. 
 
{{ company_name }} synchronizes either non-completed tasks or completed tasks which were Due or were Modified over the last 2 weeks. Older tasks are omitted.
<br><br>
<p><img src="../../assets/images/Configuration-&-Settings/User-Settings/new-sync-settings-page/tasks.png" style="width:50%; display:inline-block; vertical-align:middle; margin-left:1px;float: right;"></p>

You can further manage the automatic tasks saving patterns in the **Tasks** box on the **General** tab. 


<br><br>
<br>
 
### Tasks down-syncing from Salesforce to mail client


In the *Tasks* box, you can configure down-syncing of tasks from Salesforce to your mails client using **Sync my Salesforce tasks** switch button. 

<br>
<p><img src="../../assets/images/Configuration-&-Settings/User-Settings/new-sync-settings-page/tasks-sync.png" style="width:50%; display:inline-block; vertical-align:middle; margin-left:1px;float: right;"></p>

To enable Tasks down-syncing from Salesforce to your mail client, enable the **Sync my Salesforce tasks** switch button.


<br><br><br>
!!! warning "Important"
    Note that if you disable this switch button, the tasks that were created in Salesforce and down-synced from Salesforce to your mail client will be removed from your mail client.

<br><br>
<p><img src="../../assets/images/Configuration-&-Settings/User-Settings/new-sync-settings-page/tasks-forbid.png" style="width:50%; display:inline-block; vertical-align:middle; margin-left:1px;float: right;"></p>

To ensure that tasks deletion in your mail client will **not** result in these tasks deletion in Salesforce, toggle the **Forbid to remove** switch button. In this scenario, the only way to delete from your mail client the tasks that were previously down-synced from Salesforce is to delete them in Salesforce.

If this switch button is disabled, deleting of tasks in your mail client will lead to their deleting in Salesforce.

&nbsp;

* * *

&nbsp;

## Contacts saving

<p><img src="../../assets/images/Configuration-&-Settings/User-Settings/new-sync-settings-page/contacts.png" style="width:50%; display:inline-block; vertical-align:middle; margin-left:1px;float: right;"></p>

You can manage some the automatic contacts saving patterns in the **Contacts** box on the **General** tab. 


<br><br><br>

### Contacts down-syncing from Salesforce to mail client


In the *Contacts* box, you can configure down-syncing of contacts from Salesforce to your mail client using **Sync my Salesforce contacts** switch button. 

To enable contacts down-syncing from Salesforce to your mail client, enable the **Sync my Salesforce contacts** switch button.

!!! warning "Important"
    Note that if you disable this switch button, the contacts that were created in Salesforce and down-synced from Salesforce to your mail client will be removed from your mail client.
<br>
<br>

Additionally, you can further refine the filters for down-syncing contacts from Salesforce to your mail client:

**1\.** Click **Customize scopes**

<p><img src="../../assets/images/Configuration-&-Settings/User-Settings/new-sync-settings-page/contacts-customize.gif" style="width:50%; display:inline-block; vertical-align:middle; margin-left:1px;float: right;"></p>

**2\.** Select one of the following down-syncing filters:

<p style="margin-left:5%">
<b>All contacts</b> – synchronize all available contacts
<br>
<b>Only my contacts</b> – synchronize your contacts only, that is the contacts where you are a contact owner
<br>
<b>Custom view</b> (and then select the desired Salesforce contact view) – synchronize contacts available in the selected Salesforce view only
</p>
**3\.** Click **Apply** to save your selection


<br><br>
<p><img src="../../assets/images/Configuration-&-Settings/User-Settings/new-sync-settings-page/contacts-forbid.png" style="width:50%; display:inline-block; vertical-align:middle; margin-left:1px;float: right;"></p>

To ensure that Contacts deletion in your mail client will **not** result in these contacts deletion in Salesforce, toggle the **Forbid to remove** switch button. In this scenario, the only way to delete your mail client the contacts that were down-synced from Salesforce is to delete them in Salesforce.

If this switch button is disabled, deleting of these contacts in your mail client will lead to their deleting in Salesforce.

&nbsp;

* * *
&nbsp;

## Issues

When {{ short_name }} Sync Engine encounters conflicts between synchronized data sources or is unable to run synchronization to less obvious reasons, the synchronization issues are logged on the "Issues" tab. Every issue’s log usually includes a sync error code or notification returned by {{ product_name }} and indicates the source of the error, date and time when the error occurred. 

<p><img src="../../assets/images/Configuration-&-Settings/User-Settings/new-sync-settings-page/issues.png" style="with:80%"></p>


&nbsp;

* * *

&nbsp;

## Linking to Opportunities

You can also have your emails associated not only with Contacts and Leads, but also with related Opportunities, saved to Salesforce. These related Opportunities must satisfy all of the following requirements:

*   You are the owner of the Opportunity
*   The account associated with the Opportunity contains a contact of the person whose email address is specified in the From, To, or CC fields

If several Opportunities satisfy these requirements, the email will be saved to the most recent one. If such an Opportunity was not found, the email will be saved to the Account that is associated with the related Contact. However, if neither an Opportunity nor an associated Account were found, the email will not be saved at all. This setting applies only to automatic email/event saving, not to manual saving of events/emails.


<br>
<p><img src="../../assets/images/Configuration-&-Settings/User-Settings/new-sync-settings-page/linking-rules.png" style="width:50%; display:inline-block; vertical-align:middle; margin-left:1px;float: right;"></p>

To enable the possibility to [link](../Activities-Linking/) saved Emails to Salesforce Opportunities, on the **LINKING RULES** tab, toggle the **Link to Opportunities** switch button.



&nbsp;

* * *

&nbsp;

## Blocklisting Email Addresses and Domains


{{ product_name }} offers the possibility to **blocklist** email messages and calendar items from/to certain addresses or domains from being saved with Salesforce.


To add specific email addresses and domains to the blocklist:

<br>
<p><img src="../../assets/images/Configuration-&-Settings/User-Settings/new-sync-settings-page/blocklist-new.gif" style="width:60%; display:inline-block; vertical-align:middle; margin-left:1px;float: right;"></p>

**1\.** Switch to the **Blocklist** tab  

**2\.** Click **Change**  

**3\.** Enter the email addresses and domains in the corresponding box  

**4\.** Click **Apply** to save the changes

<br>
See [this article](../Blocklisting-Email-Addresses-and-Domains/) for more information on **Blocklisting Email Addresses and Domains** with {{ product_name }}.

Also, a special global setting blocklists all free email services (e.g., *gmail.com*, *outlook.com*, etc.) from syncing by default, so you don’t need to add all of them to the Blocklist. To change or customize this setting, contact our [support team](mailto:support@revenuegrid.com).

!!! warning "Important"
    Please note that if you update the list of **Blocklisted email addresses/domains**; for these changes to be applied you must [log out from {{ short_name }} Add-In](https://docs.revenuegrid.com/ri/fast/assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b3a275f0428630abc0ba0da.png) and then [re-log in](../How-to-Install-and-Run-the-Solution-all-configurations/#ii_rg_email_sidebar_logon)


&nbsp;

* * *

&nbsp;

## Other Sync Adjustments

Besides above-described regular sync adjustments, {{ product_name }} offers special synchronization settings to meet your company's specific preferences - [syncing calendar items as other object types besides events](../Special-Sync-Options-Save-Events-As-Other-&-One-Way-Sync/#syncing_calendar_events_as_custom_or_standard_salesforce_objects_eg_tasks) and [one-way synchronization options](../Special-Sync-Options-Save-Events-As-Other-&-One-Way-Sync/#one-way_synchronization).





&#160;
 &#160;

