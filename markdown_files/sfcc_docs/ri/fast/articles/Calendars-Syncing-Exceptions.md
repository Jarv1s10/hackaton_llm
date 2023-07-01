---
description: Learn about essential exceptions to the calendar items synchronization
---
# Calendars Synchronization: Essential Exceptions  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*3 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

This guide covers exceptions to the [Calendar Items synchronization](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/). Also refer to [this article](../Calendar-Items-Sync-Special-Patterns-Attendees-Lists,-Private-Items,-Item-Unsharing-and-Deletion/) explaining advanced {{ short_name }} sync patterns and to [this article](../Special-Sync-Options-Save-Events-As-Other-&-One-Way-Sync/) explaining available custom sync adjustment settings.
&nbsp;

### In what cases the calendars are not 1:1 identical?

Both Salesforce and MS Exchange / Office 365 have certain technical restrictions which can lead to events not always syncing between the calendars. Some underlying causes are listed in [this Salesforce article](https://help.salesforce.com/articleView?id=exchange_sync_admin_considerations_events_general.htm&type=0).

&nbsp;

**General exceptions:**

&nbsp;

##### No recurring Salesforce Lightning Events downsyncing

A fundamental limitation, presently {{ short_name }} sync engine can synchronize to MS Exchange / Office 365 recurring Salesforce Events created in [Salesforce Classic](https://help.salesforce.com/articleView?id=lex_aloha_comparison.htm&type=5) but not ones created in [Salesforce Lightning](https://help.salesforce.com/articleView?id=lex_aloha_comparison.htm&type=5).

To work with recurring Events via {{ product_name }}, make sure to configure the prerequisites as described in [this article](../Precondition-for-Enabling-Advanced-Calendar-Synchronization/).

&nbsp;

##### Private Meetings or Appointments do not get synced

Meetings or appointments flagged as private in MS Outlook do not get synced to Salesforce, unless a specific [global setting](../Special-Admin-Panel-Settings/#extra_configuration_settings) is enabled to allow that. See [this article](../Saving-Calendar-Items-in-Salesforce-%28Adaptive-view%29/#saving_private_calendar_items) for details.

&nbsp;

* * *

&nbsp;

**Specific Exceptions:**



##### Attendees related exceptions

The only use case that causes a [sync conflict](../Handling-Sync-Issues/) is when an attendee who is a {{ product_name }} user attempts saving to Salesforce a meeting organized by another user before it is saved by the organizer.

Another special consideration is that if an outside organizer or an in-org organizer that doesn't use {{ short_name }} initiates a meeting and it gets saved by a {{ short_name }} user, it will get synced in Salesforce as an Event with no attendees.

&nbsp;

##### If a recurring Meeting series' master item gets updated in MS Exchange / Office 365

• MS Exchange / Office 365 will update all both past and future occurrences  
• Only the future Events will be changed in Salesforce  
• {{ short_name }} handles an update of event series in SFDC in the following way: past events are not changed and no updates are sent to attendees, only the future ones are updated  
• Salesforce will overwrite any changed Event's Description, Location, and *WhatId* relationships for individual events in the series based on the “master” event: all occurrences in Exchange / O365 will get changed, including the exceptions

*Why?*  
• Technical reason. The two systems handle this aspect differently

&nbsp;

&nbsp;

#####  Recurring all-day Events

• Recurring all-day Events do **not** get synced to Salesforce  
• A [sync issue](../Handling-Sync-Issues/) will be logged  
• A custom "Error" category will be applied to the item in MS Outlook indicating a sync issue  

*Why?*  
• A technical reason. Due to time zones handling difficulties for all-day Events



Similarly, recurring all-day Events created in Salesforce do **not** get down-synced to MS Exchange / Office 365.

&nbsp;

&nbsp;

##### Converting an already synced single occurrence item to a recurring series or vice versa

• The resulting recurring series or single occurrence item will **not** get synced to Salesforce  
• A [sync issue](../Handling-Sync-Issues/) will be logged  
• A custom "Error" category will be applied to the item in MS Outlook indicating a sync issue  

*Why?*  
• Technical reason. Salesforce does not allow converting a single occurrence event to a recurring series or vice versa



&nbsp;

* * *

&nbsp;

#### **Time zone auto-sync exceptions**

 If an event created in Exchange uses a time zone that is not supported by Salesforce, the event may not sync. Refer to
[this article](../Historical-Sync-&-Timezones-Matching/#times_zones_matching) for all details.



&#160;
 &#160;

