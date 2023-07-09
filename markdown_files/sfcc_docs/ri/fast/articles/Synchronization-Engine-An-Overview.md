---
description: Detailed description of Revenue Grid Synchronization Engine
---
# {{ company_name }} Synchronization Engine: An Overview  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*8 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

The core data synchronization *process* described in this article is not to be confused with the toggleable {{ product_name }} *features*  – auto-syncing of every new inbound or outbound [email](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_emails_emails_autosharing) or [calendar item](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#meeting_appointment_autosaving), or [auto-saving of new emails in specific threads](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_email_threads). Those features are carried out by this process and if synchronization is not [set up](../Authorizing-Sync-Engine-to-Work-with-Your-Data/) or [is suspended](../Handling-Sync-Issues/), these features will not work. Refer to [this comparison article](../AddIn-vs-Sync-Functions/) to learn about the scope of functions performed by the Sync Engine and the [Add-In](../Introduction/) (or the [Chrome Extension](../Using-the-Solution-for-Salesforce-and-Gmail/)).

&nbsp;

![](../assets/images/Using-SmartCloud-Connect/sync.png)

&nbsp;

{{ company_name }} Synchronization ({{ short_name }} Sync Engine) is a recurrent background (server-side) process of two-way data exchange between your email account (on an MS Exchange, Office 365, or Gmail server) and your Salesforce account, that {{ product_name }} performs 24/7 to maintain data mirroring between your email/calendar items and their matching Salesforce objects, also considering your choices and actions in {{ product_name }} and your email client (via the [dedicated category or folder](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#3_besides_using_the_save_button_emails_saving_can_be_performed_in_4_more_easy_ways)). {{ short_name }} Sync does **not** depend on whether [{{ product_name }} Add-In](../Introduction/) is opened in your email client. Sync data is transferred securely server-to-server:

- over [EWS](http://docs.microsoft.com/en-us/previous-versions/office/developer/exchange-server-2010/dd877045(v%3Dexchg.140)) for MS Exchange or Office 365 with Exchange Online
- over [MS Graph](../MS-Graph/) for Office 365 with Exchange Online
- over [TLS](https://support.google.com/a/answer/2520500?hl=en) / [SSL](https://www.lifewire.com/tls-vs-ssl-4156306) for Gmail
- over official secure [Salesforce API](http://trailhead.salesforce.com/en/modules/api_basics) to/from your Salesforce account.

&nbsp;

By default, {{ short_name }} Sync sessions are carried out every 30 minutes; they run regardless of whether {{ product_name }} or MS Outlook/other supported email client is opened or not, as server-to-server data exchange unnoticed by the users.
Since data exchange is carried out between your email server and Salesforce server while your local email client and the Sidebar only serve to display email / calendar data and register your choices and actions, {{ short_name }} Sync does not consume any noticeable amount of your local internet traffic.

The users have the possibility to differentiate between emails they saved via the Save button ([Read and Compose modes](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#2_when_revenue_grid_sync_is_not_active)) and ones auto-saved by {{ short_name }} Sync engine; the former are marked via a custom Salesforce field *AddInEmail* which is added by the advanced [Salesforce integration {{ company_name }} managed package](../Admin-Managed-Package/).

&nbsp;

The key aspects of synchronization process can be flexibly adjusted by the end users individually via [Sync dashboard](../Configuring-Activities-Synchronization-Settings/) and [{{ product_name }} Customization page](../Customization-Settings-Explained/), or by the local admin via [Admin settings](../Special-Admin-Panel-Settings/). Synchronization can be [manually suspended or forced to run sooner than the next scheduled session](../Viewing-Synchronization-Statistics-and-Connection-Statuses/). It may also get suspended due to errors and [monitored for troubleshooting](../Handling-Sync-Issues/).

Maintaining data mirroring is based on [tables of matching fields](../Object-Fields-Mapping-Patterns/) mapped between MS Exchange / Office 365 calendar items/tasks/contacts and corresponding Salesforce objects. These mapping tables are used to compare the values in matching fields and transfer updated values from email server to Salesforce or vice versa, replacing old values in corresponding fields with actual ones.

This ongoing data mirroring process has its [specific exceptions and overriding patterns](../Calendar-Items-Sync-Special-Patterns-Attendees-Lists,-Private-Items,-Item-Unsharing-and-Deletion/) applied in certain cases as required by convenience of use considerations, e.g. for processing [event attendees lists](../Calendar-Items-Sync-Special-Patterns-Attendees-Lists,-Private-Items,-Item-Unsharing-and-Deletion/). In addition, refer to [this article](../Calendars-Syncing-Exceptions/) for in-depth explanations of specific calendars sync exceptions. Finally, there are [custom sync adjustment options](../Special-Sync-Options-Save-Events-As-Other-&-One-Way-Sync/) which alter the reciprocal mirroring principle according to customers' preferences.

!!! note "Note"
    Unlike continuous [mirror-syncing](../Special-Sync-Options-Save-Events-As-Other-&-One-Way-Sync/) of MS Exchange / Office 365 or [Gmail](../Using-the-Solution-for-Salesforce-and-Gmail/) Tasks, Contacts, or calendar items, [saving of emails](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/) is always a [one-way](../Special-Sync-Options-Save-Events-As-Other-&-One-Way-Sync/#one-way_synchronization) Mail server → Salesforce process by definition. In addition, it is performed only one time for each saved email, except for the special case of [Enhanced Emails editing](../Saving-Emails-in-Salesforce-1.-Function-Overview/#editing_already_saved_email_messages_via_the_sidebar)

&nbsp;

Besides this core data mirroring process, synchronization sessions involve several related jobs: checking for emails / events / tasks / contacts assigned Salesforce category or put into Salesforce folder, creation of Salesforce objects based on new emails or calendar items and user input, [finding and linking of related records](../Initial-Search-and-Applied-Record-Filters/) in Salesforce, deletion of the matching object if [the configuration requires that](../Calendar-Items-Sync-Special-Patterns-Attendees-Lists,-Private-Items,-Item-Unsharing-and-Deletion/) (for example, removal from Salesforce of a meeting that got cancelled in Exchange/Office 365).

!!! note "Note"
    Note that in the latest {{ product_name }} updates, resetting/reapplying [Customization settings](../Customization-Settings-Explained/) does not affect calendar items synchronization in any way

&nbsp;

!!! warning "Important"
    Some actions can only be performed via Sync Engine: [calendar items syncing](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/) in Salesforce, [saving of email messages in Compose mode](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/), saving of emails, contacts, or tasks by [assigning them the *Salesforce* category or moving emails to the *Salesforce emails* folder](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#3_besides_using_the_save_button_emails_saving_can_be_performed_in_4_more_easy_ways). Note that because of the sync sessions interval it may take up to 30 minutes for a corresponding item to appear in Salesforce after your performed either of these saving actions.  
    Several other actions involving creation or updating of Salesforce items do <u>not</u> depend on the Sync Engine, since they are performed by [{{ short_name }} Add-In](../Introduction/) immediately in Salesforce. That includes [saving email messages using the Save button in Read mode](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/) or initial saving (creation) of calendar items in Salesforce. See [this comparison table](../AddIn-vs-Sync-Functions/) for complete information

&nbsp;

!!! tip "Tip"
    Besides [regular synchronization settings](../Configuring-Activities-Synchronization-Settings/) {{ product_name }} offers special adjustments to meet your company's specific preferences - [syncing calendar items as other object types besides events](../Special-Sync-Options-Save-Events-As-Other-&-One-Way-Sync/#syncing_calendar_events_as_custom_or_standard_salesforce_objects_eg_tasks) and [one-way synchronization options](../Special-Sync-Options-Save-Events-As-Other-&-One-Way-Sync/#one-way_synchronization)

&nbsp;

&nbsp;

* * *

&nbsp;

&nbsp;

#### Auto-linking of email/event/task items created by Sync

Another important aspect of synchronization is auto-linking of Task/Email message/Event objects created in Salesforce by {{ company_name }} sync. The Salesforce objects mirroring your email messages and calendar items get
automatically associated through [“lookup” relationships](https://help.salesforce.com/articleView?id=overview_of_custom_object_relationships.htm&type=5) ([the “Name” (*WhoID*) and “Related To” (*WhatID*) fields](https://www.forcetalks.com/salesforce-topic/what-is-the-difference-between-whoid-and-whatid-how-can-we-associate-the-task-with-the-salesforce-opportunity-using-whatid/#post-34618)) with a relevant Contact/Lead, Account, and (optionally) Opportunity. This linking pattern is used both on [auto-saving](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_emails_emails_autosharing) and [user-initiated saving through the custom category or dedicated folder](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-%28Adaptive-view%29/#3_besides_using_the_save_button_emails_saving_can_be_performed_in_4_more_easy_ways). 

&nbsp;

&nbsp;

* * *

&nbsp;

&nbsp;

#### Automatic creation of Contacts or Leads by {{ product_name }} (Autoresolving)

On [user-initiated syncing or auto-syncing of calendar items](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/) as well as [emails auto-saving](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_emails_emails_autosharing), {{ product_name }} can automatically create required Leads or Contacts for meeting attendees and email recipients whose addresses were not registered in Salesforce previously ([unresolved](../Special-Admin-Panel-Settings/#auto-create_objects_for_unresolved_meeting_participants_auto-resolving) meeting attendees/email recipients). Created Leads'/Contacts' fields will be populated with data retrieved from the meeting invitation's/email's signature, if one is available.  

The Calendar Event or Task/EmailMessage object created in Salesforce to [match](../Object-Fields-Mapping-Patterns/) the saved item will be linked to this Lead or Contact. Note that {{ short_name }} will be lacking certain details to populate some of auto-created Leads' or Contacts' key fields, so the users should [populate these fields later](../All-User-Actions-in-Add-In-Sidebar/#5_improved_records_browsing_and_updating) via the [Sidebar](../Introduction/) to make them more detailed.  

To request enabling of the Auto-resolving feature for your org, send a corresponding request to [{{ company_name }} support team](mailto:support@revenuegrid.com), specifying if you would prefer Leads or Contacts to be auto-created for unresolved meeting attendees' addresses. Optionally, {{ product_name }} can also create [Person Accounts](https://help.salesforce.com/articleView?id=account_person.htm&type=5) instead of Leads/Contacts.

!!! note "Note"
    Email addresses and domains blocklisted from syncing will **not** be processed on Leads/Contacts auto-resolving (auto-creating) by {{ short_name }} for this user. The blocklist is managed on [two levels](../Two-Layers-Blacklisting/): email addresses and domains can be blocklisted [by an individual {{ short_name }} user](../Configuring-Activities-Synchronization-Settings/#blocklisting_email_addresses_and_domains) and [by the Org Admin](../Special-Admin-Panel-Settings/#emails_domains_blocklisted_from_sync) (e.g. internal domains). Also, a special global setting blocklists all free email services (e.g. *gmail.com*, *yahoo.com*, etc.) from auto-syncing by default. To change or customize this setting, contact our [support team](mailto:support@revenuegrid.com)

&nbsp;

Finally, the latest {{ short_name }} updates include optional advanced smart Lead/Contact auto-resolving mechanisms. See the descriptions of the settings *SalesforceSmartCreateUnresolvedObjects* and *SalesforceEmailCreateAllUnresolvedRecipients* in [this article](../Special-Admin-Panel-Settings/#extra_configuration_settings) to learn more about these mechanisms.  

In addition, {{ short_name }} can optionally auto-create new Accounts to link the auto-created Contacts to in case there is no relevant Account retrieved by [{{ short_name }} Initial Search](../Initial-Search-and-Applied-Record-Filters/). The auto-created Account's *Name* field will be based on the corporate email domain from the attendee's email address. Later the Account's specific details can be [populated by the user](../All-User-Actions-in-Add-In-Sidebar/#5_improved_records_creation_updating_browsing) via the [Sidebar](../Introduction/).

Alternatively, all auto-resolved Contacts can be linked to a specific Account [pre-defined by the local Admin](../Special-Admin-Panel-Settings/#extra_configuration_settings) or [{{ company_name }} support team](mailto:support@revenuegrid.com). Later, such Contacts can be sorted and re-linked to proper Accounts individually by someone in the Org.  

&nbsp;

&nbsp;

* * *

&nbsp;

&nbsp;

#### Instant Sync of Calendar Items

!!! note "Note"
    To enable the instant sync, send a corresponding request to [our CSM team](mailto:support@revenuegrid.com)

&nbsp;

##### MS Outlook Calendar ➝ Salesforce Calendar instant sync  

Instant synchronization (*instant sync*) is available for MS Outlook Meetings, Appointments, and All-Day Events; it enables {{ short_name }} end users to synchronize their calendars with Salesforce calendar in real time within 5 minutes.  

Instant sync only triggers when a calendar item is created, updated, or deleted in MS Outlook; it does **not** trigger on any event updates in Salesforce calendar. Its behavior can be adjusted in [{{ short_name }} Global Settings](../Special-Admin-Panel-Settings/#extra_configuration_settings) (which are usually managed by [RevenueGrid.com CSM team](mailto:support@revenuegrid.com)). Instant sync can also be set to trigger specifically on calendar items creation, calendar items updating, or calendar items deletion.  

When activated by a meeting change in MS Exchange / Office 365, Instant sync auto-triggers [Force synchronization](../How-to-Open-Sync-Dashboard-(Adaptive-view)/#force_scc_sync), this way initiating a sync session ahead of the default 30 minute sync interval; several sequential instant syncs can be performed only with 1-3 minute intervals, not immediately.  

Events instant sync from mailbox to Salesforce is **not** available for [{{ product_name }} Chrome Extension for Gmail](../Using-the-Solution-for-Salesforce-and-Gmail/) and MS Graph users.

&nbsp;

&nbsp;

##### Salesforce Calendar ➝ Email client Calendar  instant sync

Instant calendar Events down-syncing from Salesforce to email client should be [additionally configured](../instant-sync/) after [{{ company_name }} managed package](../Admin-Managed-Package/) is installed in an Org. It works for MS Exchange or Office 365 mailboxes connected over [EWS](../Working-With-EWS/) or [MS Graph](../MS-Graph/) as well as for [Gmail boxes](../Using-the-Solution-for-Salesforce-and-Gmail/#syncing_calendar_events_in_salesforce).

This features enables {{ short_name }} end users to auto-sync new created Salesforce Events with email client's calendar in real time, without a 2 - 30 minute delay. Note that this intant syncing is triggered *only* on Salesforce Events creation. 

Learn about how to configure Salesforce Calendar ➝ Email client Calendar  instant sync in [this article](../instant-sync/)

&nbsp;

* * *

&nbsp;

#### Conditional Un-Syncing of Events

To accommodate specific Events capture flows, the Sync engine can be configured to un-sync (remove) Events having certain criteria from mail client's calendar, so they'll only remain in Salesforce. See [this article](../Special-Admin-Panel-Settings/#conditional_events_un-syncing) for more information.

&nbsp;

* * *

&nbsp;

#### Problematic Events' quick editing on specific errors

This optional feature is only available upon request to [our Support team](mailto:support@revenuegrid.com). It allows to customize the saving flow, ensuring the possibility to quickly modify or correct a value in an Event's field if it has caused a specific Sync error, directly in Salesforce. After this feature is configured and enabled, clicking on the "Event will be saved" indicator for the problematic Event in the [Sidebar](../Introduction/) opens it in Salesforce.



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