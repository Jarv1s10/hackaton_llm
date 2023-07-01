---
description: In-depth overview of calendar items (Meetings, Appointments, Events) sync patterns in Salesforce
---
# How to Sync Calendar Items (Meetings, Appointments, Events) in Salesforce  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*15 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! tip "Tip"
    Also refer to [this article](../Calendars-Syncing-Exceptions/) to learn about essential calendars sync exceptions and to [this article](../Object-Fields-Mapping-Patterns/#ms_outlook_calendar_items) for detailed information on how fields are matched between MS Exchange / Office 365 and Salesforce records

&nbsp;

The general pattern of saving a calendar item (MS Outlook [meeting](http://support.office.com/en-us/article/schedule-a-meeting-with-other-people-5c9877bc-ab91-4a7c-99fb-b0b68d7ea94f) / [appointment](http://support.office.com/en-us/article/create-or-schedule-an-appointment-be84396a-0903-4e25-b31c-1c99ce0dacf2) / all-day event) depends on whether it is initial saving, on which the [corresponding](../Object-Fields-Mapping-Patterns/) [Salesforce event object](http://help.salesforce.com/articleView?id=events_and_calendars.htm&type=5) is created or it involves updating / modifying of an existing event. Initial saving is performed by {{ company_name }} synchronization, therefore sync must be running when you are saving a new calendar item to Salesforce; however, updating / modifying an event object already existing in Salesforce is performed by the Add-In directly and immediately.  
To prevent creation of several instances of the same event, [events deduplication](../Item-Deduplication-Mechanisms/#contacts_and_events_deduplication) is performed on server side during [events syncing](../Synchronization-Engine-An-Overview/). Please also refer to [this article](../Calendar-Items-Sync-Special-Patterns-Attendees-Lists,-Private-Items,-Item-Unsharing-and-Deletion/) for complete information about patterns applied with regard to attendees' lists on Exchange → Salesforce and Salesforce → Exchange syncing.

!!! note "Note"
    In the latest {{ product_name }} updates [group (public) calendar events](https://support.office.com/en-us/article/create-view-or-delete-a-calendar-group-04fc64f2-b658-450b-8dce-dd27ed660570) saving is also fully supported, it is performed in the same ways as saving of regular calendar events. At that, note that only 24 hours long or shorter events can be saved (due to [a Salesforce limitation](https://help.salesforce.com/articleView?id=creating_events_cex.htm&type=5))

&nbsp;

{{ product_name }} also offers a unique optional possibility to link multiple [Business Records](https://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) to Events saved in Salesforce [via {{ short_name }} Sync](../Synchronization-Engine-An-Overview/); this function is not available in Salesforce out-of-the-box.  
This feature requires [{{ company_name }} Salesforce managed package installation](../Admin-Managed-Package/) and can be enabled upon request.



&nbsp;

#### Meeting / Appointment Autosaving

!!! warning "Important"
    The "sliding time window" limit: {{ short_name }} Sync only autosaves meetings and appointments which occurred no earlier than 14 days in the past from the present date. Older meetings are omitted from syncing, unless specifically [saved by user](../Saving-Calendar-Items-in-Salesforce-%28Adaptive-view%29/#saving_calendar_items_semi-automatically). Similarly, for future calendar items syncing the limit is 60 days in the future. Only calendar items scheduled to occur within 60 days from the current date are synchronized with Salesforce calendar.  
    The sliding time window ensures that relevant events are kept in sync over long periods of time, while also allowing to avoid syncing very large amounts of irrelevant past events data. Autosaving is carried out on [synchronization sessions](../Synchronization-Engine-An-Overview/), so it is performed with a 10 - 20 minute delay and it requires [{{ short_name }} Sync to be running](../Authorizing-Sync-Engine-to-Work-with-Your-Data/)

&nbsp;

If the [meeting auto-saving or appointment auto-saving switches](../Configuring-Activities-Synchronization-Settings/#automatic_syncing_of_calendar_items_events_autosharing) are enabled in {{ product_name }} [sync settings](../Configuring-Activities-Synchronization-Settings/#automatic_syncing_of_calendar_items_events_autosharing), the Sync ending will automatically save in Salesforce respectively all meetings or all appointments which you create or accept (also tentatively accept) in email client.

Recurring calendar items can be synchronized automatically like any other items if [Advanced calendaring is enabled in your Salesforce org](../Precondition-for-Enabling-Advanced-Calendar-Synchronization/). When a calendar item is autosaved, it will be linked to Related records retrieved for the item by [{{ product_name }} Initial Search](../Initial-Search-and-Applied-Record-Filters/). Calendar items which do not get autosaved are ones marked as private, internal (in-company) or blocklisted (e.g. personal) ones, and non-linked events.


&nbsp;

!!! tip "Tip"
    In the latest {{ product_name }} updates it is possible to set up [one-way](../Special-Sync-Options-Save-Events-As-Other-&-One-Way-Sync/#one-way_synchronization) auto-syncing of [Salesforce Public (group) calendar events](https://help.salesforce.com/articleView?id=customize_groupcal.htm&type=5) (presently only available in Salesforce Classic) with MS Outlook calendar; additionally, these events can be put into [different event categories](https://support.office.com/en-us/article/assign-a-color-category-to-a-calendar-appointment-meeting-or-event-750596d9-707d-4412-8c0e-7fdc0fc52527). Presently, this feature is enabled by request sent to [our Support team](mailto:support@revenuegrid.com); the request should contain a detailed description of your use case

&nbsp;

Please also note that calendar items synchronization follows [slightly different scenarios](../Calendar-Items-Sync-Special-Patterns-Attendees-Lists,-Private-Items,-Item-Unsharing-and-Deletion/) depending on whether internal or external contacts are involved and other factors.

&nbsp;
* * *

&nbsp;

#### Saving Calendar Items Semi-Automatically

!!! note "Note"
    Note if you need to save a new calendar item to Salesforce and [{{ short_name }} sync](../Synchronization-Engine-An-Overview/) is not active for any reason, saving it is not possible until you [enable {{ short_name }} Sync](../Authorizing-Sync-Engine-to-Work-with-Your-Data/). However, if a corresponding Salesforce Event record was created earlier, updating of its field values is made by the Add-In directly and does not require Sync to be running

&nbsp;

Calendar items can also be saved in Salesforce selectively in one of the following ways:

!!! tip "Tip"
    The category/custom folder calendar items syncing method is also handy when you need to save a calendar item from a stationary or mobile device if it goes offline for some periods of time (e.g. when losing wi-fi connection). Items saved in this way will be upsynced to Salesforce as soon as Internet connection is available.  
    In addition, this option can be effectively used to process multiple items

&nbsp;

**1.** By assigning them the custom Salesforce category:  

*   click **Categorize** in MS Outlook ribbon and select **Salesforce** from the picklist
*   or right-click the item and select **Categorize** > **Salesforce**

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b8440480428631d7a8a6bc9.png" class="minimized">
</p>

&nbsp;

**2.** By clicking the **Save** button at the top of {{ product_name }} for the calendar item opened in a separate MS Outlook window.



![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b84417a0428631d7a8a6be9.png)

&nbsp;

After you click **Save**, there will appear the *Save current event as an Activity in Salesforce* dialog:

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b85624f2c7d3a03f89e32da.png)

&nbsp;

In this dialog, you may change the primary record (a key Lead or Contact) that the Event will be linked to in Salesforce through [WhoId relationship](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) via the **Name** field or specify an additional Business record to be [associated](https://help.salesforce.com/articleView?id=task_fields.htm&type=5) with it using the optional **Related To** field.

Either way, if it is initial saving of the calendar item, it will be saved in Salesforce on the next synchronization session; if the event object already exists, it will be updated immediately.

!!! note "Note"
    By default, [internal (in-company) meetings](../Initial-Search-and-Applied-Record-Filters/#internal_emails_corporate_domains_and_the_blocklist) (calendar items in which all attendees and the organizer belong to the same company) can only be saved in Salesforce manually using the described above procedures. However, there is also an [Admin panel setting](../Special-Admin-Panel-Settings/) that allows saving internal events in Salesforce automatically; you can request that by sending us an email to [our Support team](mailto:support@revenuegrid.com). Additionally, please note that if an event's attendees list contains only unresolved email addresses (ones having no Salesforce records associations), this event can only be saved in Salesforce after you [create](../Create-New-Records/) at least one corresponding contact association in Salesforce

&nbsp;

![](../assets/images/Using-SmartCloud-Connect/How-To-s/Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/save_dialog.png)

&nbsp;

![](../assets/images/Using-SmartCloud-Connect/How-To-s/Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/create_event_dialog.png)

&nbsp;

&nbsp;



#### Removing from Salesforce Calendar Items Synced by Mistake (Salesforce Unsync)

In the latest product updates it is possible delete (unsync) Events created in Salesforce by {{ short_name }} sync. This function allows the users to easily remove an item synced to Salesforce by mistake, also in bulk.
To remove a synced calendar item from Salesforce: assign it the custom *"Salesforce Unsync"* category in MS Outlook and wait for the next [Sync session](../Synchronization-Engine-An-Overview/); that may take between 1 and 30 minutes.

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Unsync-Event\unsync-owa.png" style="width: 70%; height: 70%;">
</p></details>

&nbsp;


* * *

&nbsp;

#### Synchronizing Series of Recurring Items

!!! warning "Important"
    Presently, there is a limitation on syncing of recurring meetings/appointments series if your are using [Salesforce Lightning Experience](https://trailhead.salesforce.com/content/learn/modules/lex_migration_introduction/lex_migration_introduction_whatis): series of recurring calendar items created in Salesforce Lightning Experience cannot be *downsynced* to MS Exchange / Office 365 by {{ product_name }}.  
    At that, series of recurring MS Exchange / Office 365 calendar items can be *upsynced* to Salesforce Lightning, but only as [Salesforce Classic format events](https://help.salesforce.com/articleView?id=viewing_events_cex.htm&type=5); therefore, they will be uneditable via Salesforce Lightning. As a workaround, you can temporarily [switch to Salesforce Classic](https://help.salesforce.com/articleView?id=000230642&type=1) to edit them in Salesforce or edit them in MS Outlook and upsync the changes

&nbsp;

If you need to save series of recurring calendar entries in Salesforce, please refer to [this article](../Precondition-for-Enabling-Advanced-Calendar-Synchronization/) to learn how to enable this possibility in Salesforce. In addition, recurring events saving needs to be enabled in [{{ product_name }} Admin panel](../Special-Admin-Panel-Settings/#extra_configuration_settings); contact us to [our Support team](mailto:support@revenuegrid.com) to request that.

Series of recurring events can be saved in one of the following ways:  

**1\.** In MS Outlook / Office.com, open the Calendar and right-click on an item which belongs to the series being saved, then assign it the custom **Salesforce** category  

or

**2\.** Double-click on an item which belongs to the series and select **The entire series** in the "Open Recurring Item" dialog window 

![](../assets/images/Using-SmartCloud-Connect/How-To-s/Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/open-recurring.png)

&nbsp;

Then, to get it saved in Salesforce, you can either assign the series the custom **Salesforce** category or [open the Sidebar](../How-to-Install-and-Run-the-Solution-all-configurations/#1_to_open_the_sidebar) for it and [use the **Save** button](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#saving_calendar_items_semi-automatically); in the latter case you can also choose specific Salesforce records to link the saved Event to instead of ones defined by {{ short_name }} automatically.

The series will be synced on the following [sync session](../Synchronization-Engine-An-Overview/).

In addition, please note that in the latest {{ product_name }} updates recurring events can also be saved in Salesforce automatically if [meetings/appointments auto-saving](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#meeting_appointment_autosaving) is enabled in [Sync settings](../How-to-Open-Sync-Dashboard-(Adaptive-view)/).

&nbsp;

* * *

&nbsp;

#### Custom Salesforce Categories in MS Outlook

The following custom Salesforce categories are assigned to calendar items in MS Outlook to indicate their sync status.

Blue _Salesforce_ category: item already saved or marked to be saved in Salesforce by sync

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b8560b40428631d7a8a75a9.png" class="minimized">
</p>

&nbsp;

Red _Sync Error_ category: item synchronization error. See [this article](../Handling-Sync-Issues/) to learn how to monitor and resolve sync errors.

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b858d0a2c7d3a03f89e34cd.png" class="minimized">
</p>

&nbsp;

Besides these statuses there are other colored categories assigned to emails and calendar items, which provide additional information, for example “_Status: Tracked successfully._”, for items already saved in Salesforce, automatically [through synchronization](../Synchronization-Engine-An-Overview/) linked to pre-existing records or using the [Save button](../Save-Email-Dialog/), also for emails saved in [Compose mode](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-%28Adaptive-view%29/#2_when_revenue_grid_sync_is_not_active)) or “_Status: Required fields are missing: ..._” explaining a [sync issue](../Handling-Sync-Issues/)'s cause.

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b8524f70428631d7a8a731d.png" class="minimized">
</p>

&nbsp;

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b85250d2c7d3a03f89e3053.png)

Note that in MS Outlook calendar view, items saved or marked to be saved in Salesforce by sync and items with synchronization errors are accordingly color-marked, so you can instantly tell their status:

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b858acb2c7d3a03f89e34b9.png" class="minimized">
</p>

&nbsp;

* * *

&nbsp;

#### Monitoring Events Synchronization Issues

If something went wrong about calendar items synchronization, you can [track error causes in sync Issues > Events](../Handling-Sync-Issues/) on [{{ company_name }} sync dashboard](../How-to-Open-Sync-Dashboard-(Adaptive-view)/).

&nbsp;

* * *

&nbsp;

#### Unresolved Meeting Participants

An [_unresolved meeting participant_](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-(Adaptive-view)/#the_new_records_tab) is one whose email address has no corresponding record registered in Salesforce.  
When a meeting invitation is received from (or sent to) an unresolved attendee and then the meeting [gets saved in Salesforce](../Save-Email-Dialog/) by the user and {{ product_name }} finds no matching record to save the Event to, you will be prompted to create a corresponding record .

&nbsp;

!!! note "Note"
    {{ product_name }} can automatically create a corresponding Contact, Account, Lead, [or opportunity](../Configuring-Activities-Synchronization-Settings/#linking_to_opportunities) record for unresolved meeting participants - refer to [this article](../Synchronization-Engine-An-Overview/#automatic_creation_of_contacts_or_leads_by_rg_email_sidebar_autoresolving) for more information on this feature. Contact [{{ company_name }} support team](mailto:support@revenuegrid.com) to enable this feature.

&nbsp;

* * *

&nbsp;

#### Continuous updating of meeting attendees lists

In the latest {{ short_name }} updates the list of meeting attendees can optionally get re-synced with Salesforce on every [sync session](../Synchronization-Engine-An-Overview/) (previously, it was upsynced to Salesforce only once, on the meeting's initial saving). That is required to get invitees added to the list later registered in Salesforce. This function is managed in [{{ product_name }} special settings](../Special-Admin-Panel-Settings/#extra_configuration_settings), setting name *SalesforceEventSmartAutoSharing*.

&nbsp;

* * *

&nbsp;

#### Calendar Items' Description Field Updating: Safe Description

There is one more important principle you should be aware of about [syncing of meetings between your email client's calendar and Salesforce calendar](../Synchronization-Engine-An-Overview/).

By default, when a calendar item's syncing between your email client and Salesforce is performed by {{ product_name }}, only its original body (description) is conveyed to Salesforce, and **no** future updates made in the description on either side are reflected on the other.

This principle is applied to prevent the cases when an end user would add some internal-use-only or sensitive notes to an event's description in Salesforce – and without Safe Description applied these notes would be down-synced to the meeting's description on email server and then automatically sent to all meeting invitees, along with any other meeting updates, potentially causing unwanted situations.

However, this principle **does not** apply to significant changes, i.e., the ones introduced to the meeting *Subject*, *Assigned to* field, and/or *Start/End date/time* in Salesforce after its initial saving to the CRM. In case of such changes, meeting notes are down-synced to the meeting’s description and thus become visible to the meeting invitees.   

A suggested workaround in such situations is first to introduce the necessary change to the meeting *Subject*, *Assigned to* field, meeting’s *Start/End date/time*, wait for the meeting to sync or force sync it to Salesforce, and then **update the meeting notes after the meeting’s synchronization**. 


If you prefer to disable application of the Safe Description principle for your entire Org or for specific {{ short_name }} users, send a corresponding request to [{{ company_name }} support team](mailto:support@revenuegrid.com).

&nbsp;

* * *

&nbsp;

#### Saving Private Calendar Items

Please note that calendar items [marked as private](http://support.office.com/en-us/article/make-an-appointment-or-meeting-private-dc3898f0-22f5-45c6-8cc8-b4d4db84111d) are never saved in Salesforce by {{ product_name }} [meeting/appointment auto-saving](../Configuring-Activities-Synchronization-Settings/#automatic_syncing_of_calendar_items_events_autosharing) in the default configuration; however you can still save private calendar items manually by assigning them the Salesforce category or by using the Save button, provided you have the access permission (e.g when working with another user's calendar via [delegated calendars](../Using-MS-Outlook-Delegated-Calendars/)).  
Customers may request private calendar items autosaving if their flow requires that, using the [special setting](../Special-Admin-Panel-Settings/#extra_configuration_settings) *ExchAutoTrackPrivateEvents*.

&nbsp;

* * *

&nbsp;

#### Syncing Non-responded or Declined meetings

In the latest {{ short_name }} updates, a [special setting](../Special-Admin-Panel-Settings/#extra_configuration_settings) was introduced to manage the possibility to sync in Salesforce of inbound meetings which were left unresponded or were declined by the invitee (who is a {{ short_name }} user). Some companies require that in order to get meetings registered in Salesforce even if they were not explicitly accepted. If this setting is disabled, an attempt to sync in Salesforce of a non-responded or declined meeting results in a sync error "*ISE-013: Meeting for attendees cannot be synchronized until the organizer synchronizes it.*"

&nbsp;

* * *

&nbsp;

#### Events Down-Syncing from Salesforce to Mail Client's Calendar

&nbsp;

If you create an Event or modify an existing Event directly in Salesforce, these Salesforce Calendar updates get automatically _down-synced_ by [{{ short_name }} Sync engine](../Synchronization-Engine-An-Overview/): the corresponding calendar item will be automatically created or modified in MS Outlook or Gmail Calendar. Events modifications get to email client's calendar within 1-30 minutes but new created Events [get down-synced instantly](../Synchronization-Engine-An-Overview/#salesforce_calendar_email_client_calendar_insta-sync).

However, if an event object is deleted directly in Salesforce, its matching MS Exchange / Gmail calendar item will **not** be deleted from mail client, it will only lose the Salesforce category / color coding. 

Note that if a calendar item's _Organizer_ cancels it using the regular meeting / appointment / event cancelling procedure in MS Outlook, the corresponding Salesforce object will be deleted as well on the following sync session.

!!! warning "Important"
    In the latest {{ product_name }} updates a [special high-level setting](../Special-Admin-Panel-Settings/#extra_configuration_settings) was implemented that allows to perform automatic Removal of calendar items from MS Outlook/Gmail calendar by [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/) if they were deleted from Salesforce Calendar

&nbsp;

* * *

&nbsp;

#### Smart Actions in {{ product_name }} Opened for a Calendar Item

Please note that only three [Smart Actions](../All-User-Actions-in-Add-In-Sidebar/#1_records_categorizing) are available for events in {{ product_name }} - [Engagement Panel](../How-to-Use-the-Solution-s-Engagement-Panel/), Salesforce Reports, and [Observations](../Context-Specific-Actions/).

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b853ace0428631d7a8a73e0.png)

&nbsp;

* * *

&nbsp;

#### Meetings Sync Common Scenarios

The patterns of meetings saving in Salesforce vary in different situations depending on what kind of meeting participants are involved. Some of the common scenarios are described below:

**1.** The meeting organizer is an internal user (a user that belongs to your Salesforce org), i.e. a colleague from your organization. You are among the attendees, you have accepted the meeting and your meeting auto-saving is enabled; the organizer’s meeting auto-saving is not enabled. In this case the meeting will not be saved in your Salesforce until the organizer either saves the meeting in Salesforce manually, e.g. by assigning it the Salesforce category, or enables auto-saving. The corresponding “waiting for the organizer to synchronize the event” notification will be displayed in [Dashboard Issues > Events](../Handling-Sync-Issues/#resolving_synchronization_issues)  

**2.** You are the meeting organizer. The meeting will be saved in Salesforce for you and for those of the attendees who are internal Salesforce users only if your meeting auto-saving is enabled or you have saved the meeting manually. In Salesforce, the corresponding event object will be linked to associated records of the attendees which are external contacts  

**3.** The meeting organizer is not an internal Salesforce user (e.g. a colleague or contact that does not belong to your Salesforce org). In this case all meeting attendees which are internal users and enabled the auto-saving setting or saved the meeting manually will get the received appointment saved in Salesforce as its owners. It will be saved as an event Salesforce object linked to the relevant records of all external contacts involved (the organizer and some of the attendees).  
This way, the event object will be linked to relevant records of all external contact attendees for as many times as many meeting participants which are internal Salesforce users (auto-)save the meeting, each of them indicated as the owner of this meeting. However, it remains the same single event object, since the meeting has one single MS Outlook GUID.

**An example to clarify the scenario #3**  
For instance, there are four persons involved in the meeting:  
**IU1**: an internal Salesforce user with meetings auto-saving enabled  
**IU2**: another internal Salesforce, this one with event sync filters turned on but meetings auto-saving disabled  
**EU1**: an external contact already registered in your Salesforce CRM  
**EU2**: an external contact not yet registered in your Salesforce CRM  

**EU1** is the meeting organizer. **EU2**, **IU1**, and **IU2** are the attendees. In this case **IU1**’s contact will be linked and added to the Activity History for **EU1**.  
**IU1** will be set as the meeting’s assignee in Salesforce. The attendees won't be shown. In the default {{ product_name }} configuration, the initial description from MS Outlook will be used in the event’s detailed view: 'From:’ **EU1** and 'To/CC:' **EU2**, **IU1**, **IU2**.  

If **IU2** saves the meeting in Salesforce by assigning it the Salesforce category in MS Outlook, {{ company_name }} sync will create the meeting in the Activity History for **EU1**. In this case **IU2** will be set as the event’s assignee in Salesforce.  
Essentially, this way this event (with its specific MS Outlook GUID) will be duplicated. This is expected behavior, since sync is performing its regular patterns. At this point it is expected from **IU1** and **IU2** to negotiate who is going to be will be the event’s ultimate assignee, since there may be many attendees.

&nbsp;

* * *

&nbsp;

#### Calendar items which {{ short_name }} cannot sync

• Ordinary MS Exchange / Office 365 [All-day events](https://support.office.com/en-us/article/create-an-all-day-event-52420de0-8f5a-41b2-a165-070588896c25) which have a duration of over 14 days ([a Salesforce limitation](https://help.salesforce.com/articleView?id=creating_events_cex.htm&type=5)). A corresponding [sync issue](../Handling-Sync-Issues/) will be logged.  
• Recurring Outlook All-day events and Salesforce Events which have a duration of over 24 hours. A corresponding [sync issue](../Handling-Sync-Issues/) will be logged.  
• Any calendar items set in [problematic time zones](../Historical-Sync-&-Timezones-Matching/#times_zones_matching)  
• Calendar items outside out of the [sliding time window](../Saving-Calendar-Items-in-Salesforce-%28Adaptive-view%29/#meeting_appointment_autosaving), unless configured differently

&nbsp;

* * *

&nbsp;


#### Saving Calendar Items' Attachments

In the latest {{ short_name }} updates files attached to calendar items can be saved in Salesforce as Attachment objects, along with the items. Please refer to [this article](../Attachments-Handling-(Basic)/#saving_files_attached_to_calendar_items) for more information.

&nbsp;

* * *

&nbsp;

#### Do more with {{ product_name }}

Several key aspects of events syncing patterns can be fine-tuned according to your preferences via [customization settings](../Customization-Settings-Explained/), [Admin panel settings](../Special-Admin-Panel-Settings/), or [the extra settings managed by RevenueGrid Support team](../Special-Admin-Panel-Settings/#extra_configuration_settings). Refer to the following articles to learn more about these possibilities: [saving custom and standard Salesforce records as calendar items and one-way syncing](../Special-Sync-Options-Save-Events-As-Other-&-One-Way-Sync/); [other on-request adjustments](../Special-Admin-Panel-Settings/#extra_configuration_settings).



&#160;
 &#160;

