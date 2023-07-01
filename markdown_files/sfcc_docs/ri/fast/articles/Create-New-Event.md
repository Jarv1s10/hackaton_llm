---
description: Mirroring of created salesforce events in email client's calendar
---
# Created Salesforce Events Mirroring in Email Client's Calendar  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

After you create a Salesforce Event using [Create dialog](../Create-New-Records/) in the Sidebar, due to a technical limitation the resulting Event has no attendees and therefore gets [down-synced](../Special-Sync-Options-Save-Events-As-Other-%26-One-Way-Sync/#one-way_synchronization) to MS Outlook or Gmail as an Appointment.

To convert the attendee-less Appointment into a Meeting, you can add attendees to the item directly either in Salesforce or in MS Outlook / Google calendar; the matching item will get auto-updated accordingly. After attendees are added to the calendar item, corresponding records also get auto-linked to the Event in Salesforce.

&nbsp;

&nbsp;

### Invites Auto-Sending on Attendee List Updates

[Salesforce Classic and Salesforce Lightning](https://help.salesforce.com/articleView?id=sf.lex_aloha_comparison.htm&type=5) apply slightly different Events handling patterns. Because of that, there is a minor discrepancy in updates auto-sending:

- if an Event's Attendees list gets updated so it has at least one attendee besides the organizer in Salesforce Classic, Salesforce sends out an invite requesting the new attendees to Accept or Decline it
- if an Event's Attendees list gets updated so it has at least one attendee besides the organizer in Salesforce Lightning, no notification is sent out by Salesforce. However, as soon as a Salesforce Event gets any attendees, [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/) conveys the list to MS Exchange or Gmail server, the matching Appointment becomes a Meeting and the mail server sends out an invite requesting the new attendees to Accept or Decline it





&#160;
 &#160;

