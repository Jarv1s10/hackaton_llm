---
description: Detailed overview of Calendar Items Sync Special Patterns in RG Email Sidebar
---
# Calendar Items Sync Special Patterns: Attendees Lists, Private Items, Items Unsyncing and Deletion  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*8 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! tip "Tip"
    Also refer to [this article](../Calendars-Syncing-Exceptions/) for information on general calendars syncing exceptions

&nbsp;

#### Attendees Lists and Meeting Acceptance Statuses

&nbsp;

##### Outgoing meetings (organized by {{ short_name }} user)

Сalendar items sync between MS Exchange and Salesforce does not always follow the [one-to-one mirroring pattern](../Object-Fields-Mapping-Patterns/#ms_outlook_calendar_items) (i.e. when the contents of matching objects' fields in email client and Salesforce are reciprocally synchronized). Instead, different rules are applied to Salesforce-to-Exchange and Exchange-to-Salesforce items sync to ensure that no attendees are lost from an event in email client. 

Specifically, if you update a calendar item's list of attendees:

*   When a new attendee is added to an event in Salesforce: he/she will be added to the matching Exchange item, with _Unknown_ attendance status

*   When an attendee is removed from an event in Salesforce: no changes will be made in the matching Exchange item's attendees list

*   When a new attendee is added to a calendar item in Exchange: he/she will be added to the matching Salesforce item, with a corresponding attendance status (see the note below for more information) 

*   When an attendee is removed from an event in Exchange: he/she will be removed from the matching Salesforce item, regardless of the attendance status


  In addition to that, due to the specifics of MS Exchange's status assigning mechanisms, when you create a calendar item, its attendees' statuses can only be properly synced from Exchange to Salesforce but not the other way around:

  *   When a calendar item is created in email client and then synced with Salesforce (up-synced), its attendees’ statuses will be conveyed exactly  


  *   When an event is created in Salesforce and then synced with email client (down-synced), any attendees’ statuses including *Declined* will be set to *Unknown*

!!! note "Note"
    While the *Accepted* or *Declined* attendance statuses are transferred from Exchange to Salesforce exactly, *NoResponseReceived*, *Tentative*, *Organizer*, *Unknown* statuses are all changed to *Undecided*

&nbsp;

##### Continuous Attendees list syncing

In order to ensure real-time handling of [People records (WhoIds)](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) involved in a synced meeting, [optional](../Special-Admin-Panel-Settings/#extra_configuration_settings) continuous syncing of the invitees list was implemented. If it's not enabled, the attendees list is synced only on events' initial sharing and remains unchanged afterwards.

&nbsp;

##### Incoming meetings (organized by an external contact, {{ short_name }} user is an invitee)

When you up-sync (email client → Salesforce) or down-sync (Salesforce → email client) an incoming meeting (one organized by another person - an external or in-org contact), due to a limitation in MS Exchange its *Accepted* meeting status will be changed to *Unknown* in either of these cases.

&nbsp;

##### Syncing Non-responded or Declined meetings

In the latest {{ short_name }} updates, a [special setting](../Special-Admin-Panel-Settings/#extra_configuration_settings) was introduced to manage the possibility to sync in Salesforce of inbound meetings which were left unresponded or were declined by the invitee (who is a {{ short_name }} user). Some companies require that in order to get meetings registered in Salesforce even if they were not explicitly accepted. If this setting is disabled, an attempt to sync in Salesforce of a non-responded or declined meeting results in a sync error "*ISE-013: Meeting for attendees cannot be synchronized until the organizer synchronizes it.*"

&nbsp;

* * *

&nbsp;

#### Detailed explanation of specific calendar items handling cases

!!! tip "Tip"
    Make sure to refer to [this table](../Calendar-Items-Sync-Special-Patterns-Attendees-Lists%2C-Private-Items%2C-Item-Unsharing-and-Deletion/#items_unsyncing_deletion_patterns) to see the whole scope of items handling scenarios

&nbsp;

The events handling patterns are governed by the principle of making user calendars in Salesforce and in email client one-to-one identical through {{ company_name }} synchronization, with several exceptions caused either by convenience of use considerations or specific limitations in email client. One of the key factors to be considered is whether an event has external attendees, as that affects items processing in email client.

&nbsp;

**Use case 1: applies both to events which have attendees and ones which have no attendees**

If you create a calendar item in email client and [save it in Salesforce](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/), then unassign the "Salesforce" category from the event in email client: the event will not be removed from Salesforce and the "Salesforce" category will be automatically reassigned to it on the following [sync session](../Synchronization-Engine-An-Overview/). This behavior is defined by an events handling policy that allows deleting events from Salesforce only if they were deleted from email client, not just unsynced.

&nbsp;

**Use case 2: applies to events which have attendees (meetings)**

If you are an event's owner (set in [the Assigned To event field](http://help.salesforce.com/articleView?id=event_fields_lex.htm&type=5)) and organizer in Salesforce and the event got [synchronized](../Synchronization-Engine-An-Overview/) with your email client calendar (down-synced) by {{ product_name }}, and then you delete it in Salesforce: the event will be removed from Salesforce but will remain in email client, the "Salesforce" category will be unassigned from it. This behavior is determined by a limitation in email client.

&nbsp;

**Use case 3: applies to events which have no attendees (appointments)**

1. If you create a calendar item in email client and [save it in Salesforce](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/), then delete it from Salesforce: the event will be removed from Salesforce but will remain in email client, the "Salesforce" category will be unassigned from it. This behavior is determined by a limitation in email client  
2. If you create a calendar item in email client and [save it in Salesforce](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/), then delete it in email client: the event will be removed from Salesforce as well (up-synced), to maintain one-to-one calendars synchronization  
3. If you create a calendar item in email client and [save it in Salesforce](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/), and then the event anyhow leaves the [sliding time window covered by sync](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#meeting_appointment_autosaving): the "Salesforce" category will be unassigned from it in email client; no changes made to the event in email client will be reflected in Salesforce. This behavior is defined by the sliding time window mechanism (two weeks in the past from the present date)  
4. If you create an event in Salesforce and it gets "down-synced" to email client, then you unassign the "Salesforce" category from it in email client: the event will not be removed from Salesforce and the "Salesforce" category will be automatically reassigned to it on the following [sync session](../Synchronization-Engine-An-Overview/). This behavior is defined by an events handling policy that allows deleting events from Salesforce only if they were deleted from email client, not just unsynced  
5. If you create an event in Salesforce and it gets "down-synced" to email client, then you delete it in email client: the event will be deleted both from email client and from Salesforce, to maintain one-to-one calendars synchronization  
6. If you create an event in Salesforce and it gets "down-synced" to email client and then the event anyhow leaves the [sliding time window covered by sync](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#meeting_appointment_autosaving): it will be automatically deleted in email client, but will remain in Salesforce. This behavior is defined by the sliding time window mechanism  
7. If you create an event in Salesforce and it gets "down-synced" to email client, and then you delete it in Salesforce: the event will be deleted both from email client and from Salesforce, to maintain the one-to-one calendars sync principle  
8. If you create an event in Salesforce and it gets "down-synced" to email client, then {{ product_name }} Add-In [gets deactivated](../Uninstalling-All-Product-Components/): the event will remain in Salesforce but will be automatically deleted in email client  

!!! note "Note"
    Please note that major {{ product_name }} updates may also result in removal from email client or Gmail of events which fall under the case ( **8** ); however, this **only** concerns events which occurred in the past. This is required by certain synchronization engine updates

&nbsp;

* * *

&nbsp;

#### Private Calendar Items

Calendar items [flagged as private](http://support.office.com/en-us/article/make-an-appointment-or-meeting-private-dc3898f0-22f5-45c6-8cc8-b4d4db84111d) are handled according to the following rules:

  *   When a private calendar item is assigned the Salesforce category in email client: the event is saved in Salesforce without the Private attribute
  *   When a private calendar item is saved in Salesforce by clicking the Save button: the event is saved in Salesforce without the Private attribute
  *   When [events auto-syncing](../Configuring-Activities-Synchronization-Settings/#automatic_syncing_of_calendar_items_events_autosharing) is enabled, private events are not automatically saved in Salesforce

&nbsp;

* * *

&nbsp;

#### Items Unsyncing / Deletion Patterns

!!! tip "Tip"
    Also see [this article](../Saving-Calendar-Items-in-Salesforce-%28Adaptive-view%29/#removing_from_salesforce_calendar_items_synced_by_mistake) to learn about the user-initiated unsyncing possibility

&nbsp;

!!! note "Note"
    There's also the [Global setting](../Special-Admin-Panel-Settings/#extra_configuration_settings) *ServiceEventDeletionStrategy* that makes it possible to perform automatic deletion of calendar items from MS Exchange calendar by [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/) if they were deleted from Salesforce calendar by the users

&nbsp;

The table below summarizes the outcomes of different user actions on specific kinds of calendar items, enforced by [{{ company_name }} synchronization](../Synchronization-Engine-An-Overview/).

!!! tip "Tip"
    Also see the details how to use the [handy *Unsync* category use scenario](../Frequently-Asked-Questions/#33_i_synchronized_an_outlook_calendar_meeting_appointment_in_sales_by_mistake_how_can_i_delete_it_via_revenue_inbox)

&nbsp;

| User action /<br/>Item type                                  | If SF category is unassigned in email client | If deleted in email client                     | If [SF Unsync category assigned](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#removing_from_salesforce_calendar_items_synced_by_mistake_salesforce_unsync) in email client | If moves out of the sliding time window | If deleted in Salesforce<br />(ServiceEventDeletionStrategy  disabled) | If {{ short_name }} [is deactivated](../Uninstalling-All-Product-Components/) |
| ------------------------------------------------------------ | -------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------ | --------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Appointment (no attendees) created in email client           | SF category gets restored                    | Gets deleted in   Salesforce                   | Gets deleted in Salesforce                                   | SF category is removed in email client  | SF Category is removed in email client                       | SF category is removed from email client master category list |
| Appointment (no attendees) created in Salesforce             | SF category gets restored                    | Gets deleted in   Salesforce                   | Gets deleted in   Salesforce                                 | Gets deleted in email client            | Gets deleted in email client                                 | Gets deleted in email client                                 |
| Meeting: Organizer in email client; Owner a {{ short_name }} registered user | SF category gets restored                    | Gets deleted in   Salesforce                   | Gets deleted in   Salesforce                                 | SF category is removed in email client  | SF category is removed in email client                       | SF category is removed from email client master category list |
| Meeting: External Organizer (not a {{ short_name }} registered user) | SF category gets restored                    | Gets deleted in   Salesforce                   | Gets deleted in   Salesforce                                 | SF category is removed in email client  | SF category is removed in email client                       | SF category is removed from email client master category list |
| Meeting: In-org Organizer (is a {{ short_name }} registered user) | SF category gets restored                    | The attendee is deleted/declined in Salesforce | The attendee is deleted/declined in Salesforce               | SF category is removed in email client  | SF category   is removed in email client                     | SF category is removed from email client master category list |



&#160;
 &#160;

