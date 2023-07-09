---
description: The step-by-step guidance on how to set up the sync of rooms from the MS Exchange calendar to the corresponding Salesforce calendar
---
# How to Set Up Rooms Syncing from MS Exchange Calendar to Salesforce Calendar


<i>For users of the Email Sidebar on:</i><br><br>
<div class="container"
        style="
        display: inline-block;
        height: 42px;
        width: 162px;
        padding: 5px 10px;
        background-color: #fff;">
        <img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" 
            style="
        	height: 100%;
            object-fit: contain;
            vertical-align: middle;">
</div>
<div class="container"
        style="
        display: inline-block;
        height: 42px;
        width: 163px;
        padding: 5px 10px;
        background-color: #fff;">
        <img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" 
            style="
        	height: 100%;
            object-fit: contain;
            vertical-align: middle;">
</div>

&nbsp;

*3 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

Rooms syncing from the MS Exchange calendar to the Salesforce calendar is a feature that allows displaying MS Exchange room availability data in Salesforce using [{{ short_company_name }} Sync Engine](../How-the-Solution-Works-and-What-It-Syncs/).

{{ short_company_name }} Sync Engine can detect and sync the room availability data along with event data from MS Exchange to Salesforce, so users can see the full information about a particular MS Exchange room (i.e., when room is occupied, what event will hold there, when it is available) right in their Salesforce calendar.

&nbsp;

This article describes step-by-step guidance on how to set up the sync of rooms from the MS Exchange calendar to the corresponding Salesforce calendar. This feature is controlled by serversync setting *SalesforceEventReadResourceLocation* which enables ("1") or disables (default value "0") special location handling for Events. This feature supports only one-way synchronization from MS Exchange to Salesforce. Therefore, all relevant changes in MS Exchange will be reflected in Salesforce after synchronization.

Proceed with the following steps to set up the sync of rooms from the MS Exchange calendar to the Salesforce calendar.

&nbsp;

### 1. In Admin Panel

<p style="margin-left:5%">
<b>1.1.</b> Open <a href="../How-to-Log-In-to-the-Admin-Panel/">{{ company_name }} Admin Panel</a> and go to the <b>Settings</b> tab
<br><br>
<b>1.2.</b> Find the following settings and set the value = 1 for each to enable them:
</p>

<p style="margin-left:10%">
<b>a.</b> <i>SalesforceEventLinkResourceLocation</i> = 1
<br><br>
<b>b.</b> <i>SalesforceEventReadResourceLocation</i> = 1
</p>

<p>
    <img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\sync-rooms-to-sf\1.png">
</p>

&nbsp;

&nbsp;

### 2. In MS Exchange

<p style="margin-left:5%">
<b>2.1.</b> Check the list of available rooms in the MS Exchange calendar. To find all available rooms list, you can use the Room Finder in your calendar. Also, consult <a href="https://support.microsoft.com/en-us/office/use-the-scheduling-assistant-and-room-finder-for-meetings-in-outlook-2e00ac07-cef1-47c8-9b99-77372434d3fa">this Microsoft article</a> describing how to use the Room Finder

<br><br>

<b>2.2.</b> Copy the names of the MS Exchange rooms – you will need them for the configuring in Salesforce
</p>

<p>
    <img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\sync-rooms-to-sf\rooms-list.png">
</p>

&nbsp;

&nbsp;

### 3. In Salesforce

<p style="margin-left:5%">
<b>3.1.</b> Switch to Lightning Experience as described in <a href="https://help.salesforce.com/s/articleView?id=000387519&type=1">this article</a>

<br><br>

<img src="..\..\..\..\assets\images\intelligence-package\collaborative-forecasts\gear.png" style="width:46%; display:inline-block; vertical-align:middle; margin-left:5px; float: right">

<b>3.2.</b> Click the <b>Gear</b> (Setup Menu) icon in the upper right corner of the page to open <a href="https://help.salesforce.com/s/articleView?id=sf.basics_nav_setup.htm&type=5">Salesforce Setup menu</a>

<br><br><br><br><br><br><br><br>

<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\sync-rooms-to-sf\quick-find.png" style="width:34.65%; display:inline-block; vertical-align:middle; margin-left:8px; float: right">

<b>3.3.</b> In the <i>Quick Search</i> box in the upper left corner, type "<i>Public Calendars and Resources</i>" to quickly find the necessary tab
<br><br>
<b>3.4.</b> Select <b>Public Calendars and Resources</b>

<br><br><br><br><br><br>

<b>3.5.</b> On the <b>Resources</b> tab, <a href="https://help.salesforce.com/s/articleView?id=sf.customize_groupcal.htm&type=5">create the resources</a> with names similar to rooms in MS Exchange, the ones you copied in step 2.2. Click the <b>New</b> button on this tab to start the creation
</p>

<p>
    <img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\sync-rooms-to-sf\resources2.png">
</p>

&nbsp;

!!! note "Note"
    Matching of Exchange rooms with Salesforce resources is based on the exact room/resource name (non-case sensitive) and to active resources in Salesforce only

&nbsp;

Once all configurations are completed, the rooms specified in the MS Exchange calendar items will be synced to the relevant public Resource calendars in Salesforce. Also, for every shared event, the sync engine will add a resource (room) to the corresponding event in the Salesforce calendar:

* as a *Text* item to the *Location* field, and

* as a *Resource* item to the *Attendee* field

&nbsp;

Currently, the rooms syncing feature is based on the following principle: MS Exchange event with only **one** room (location) can be synced to the public Resource calendar in Salesforce. If more than one room is specified in the MS Exchange event, the sync engine will save them only as a text to the *Location* field of the relevant Salesforce event and not link to any public Resource.

&nbsp;

&nbsp;

***

&nbsp;

## How to add public (shared) Resource calendars in Salesforce

<p>
    <img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\sync-rooms-to-sf\add-calendars2.png" style="width:40.48%; display:inline-block; vertical-align:middle; margin-left:2px; float: right">
</p>

<p style="margin-left:5%"><br>
<b>1.</b> Open Salesforce Sales Console and go to the <b>Calendar</b> tab
<br><br>
<b>2.</b> Find <i>Other Calendars</i> on the right-hand pane, click the <b>Gear</b> (Options) icon, and select <b>Add Calendars</b>
<br><br><br>
<b>3.</b> In the opened <b>Add Calendars</b> dialog, switch from "People" to "Public Calendars and Resources" using the button on the left-hand side of the <i>Select Calendar Type</i> box
<br><br>
<b>4.</b> Start entering the name of the room/resource in the <i>Select Calendar Type</i> box and select the necessary one from the  drop-down list
<br><br>
<b>5.</b> Click the <b>Add</b> button to add the selected room/resource to your Salesforce calendar
</p>

<p>
    <img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\sync-rooms-to-sf\room1.gif" style="border: 1px solid #D7DBDD;">
</p>

<p style="margin-left:5%"><br>
<b>6.</b> The selected Resource calendar should appear in your Salesforce calendar, displaying slots when this room/resource is occupied
</p>

To add more public Resource calendars for other rooms, repeat steps 2-5 described above.