---
description: Learn how to work with Time Slots feature in RG Email Sidebar
---
# Time Slots: Initiate Meetings with Multiple Choice via Meeting Scheduler  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>
<div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*12 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

{{ product_name }} enables you to schedule meetings with your business contacts without any extra back-and-forth email correspondence. Select available time slots in your calendar, also considering availability of your colleagues involved, create and send out interactive meeting invites, get your calendar automatically updated according to the recipient's time choice. Additionally, {{ product_name }} will add activities created this way immediately to your Salesforce.

&nbsp;

!!! tip "Tip"
    Also, see [this {{ company_name }} blog article](https://revenuegrid.com/blog/how-to-schedule-a-meeting-by-email/) for special insights
    
&nbsp;

On link opening, selected Time Slots are parsed as a "static shot" that does not exclude suggested slots which got reserved after the link was opened.  

However, any reservations added to the Organizer's calendar later are also considered by the Time Slots system. As soon as a recipient clicks on their preferred slot, {{ product_name }} checks if the slot is still available in the organizer's calendar. In case it is occupied by another reservation, the recipient is suggested to pick another slot. In addition, by refreshing booking page browser window, the recipient can actualize the table after such checks.

Time Slots links can be generated even if [{{ short_name }} Sync Engine](../Synchronization-Engine-An-Overview/) is not running; however, in this case, the resulting meetings cannot be synced in the Salesforce calendar till [syncing is resumed](../Handling-Sync-Issues/).

&nbsp;
    
!!! tip "Tip"
    See [this article](../Time-Slots-Gmail/) to learn how to use the Time Slots feature in [{{ short_name }} Chrome Extension](../Using-the-Solution-for-Salesforce-and-Gmail/)

<!--
<iframe src="https://player.vimeo.com/video/392007175" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
-->

&nbsp;

&nbsp;

* * *

&nbsp;

&nbsp;

## Time Slots links generation steps

To schedule a meeting via the via {{ short_name }} Meeting Scheduler by sharing your preferred time slots through an interactive invitation:

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sharing-Calendar-Availability-(Adaptive-view)\rg-open-ribbon.png" style="width:39.29%; display:inline-block; vertical-align:middle; margin-left:1px;float: right">
</p>

**1\.** Open an email from/to recipient(s) which you want to initiate a meeting with or create a new email message by clicking the **New email** or the **Reply** button in MS Outlook ribbon and specify one or multiple recipients in the To, Cc, or BCC fields. Then open the {{ product_name }} by clicking the **Open {{ product_name }}** icon.
  
See [this article](../Open-in-Outlook-Web/) to learn how to open the Sidebar in MS Outlook on the Web

<br><br><br>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\How-to-Send-Meeting-Time-Slots-(Adaptive-view)\open-ts.png" style="width:46.82%; display:inline-block; vertical-align:middle; margin-left:1px;float: right">
</p>

**2\.** In {{ product_name }}, click the **Time slots** icon in the **Smart actions** bottom toolbar

&nbsp;

&nbsp;

Once you click the **Time Slots** icon, you will see the following **Time Slots** dialog in the sidebar:

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\How-to-Send-Meeting-Time-Slots-(Adaptive-view)\ts-full.png">
</p>

&nbsp;

<details><summary> >>> Click to view details <<< </summary>
    <p>
        <b>1.</b> Action buttons <b>Cancel</b> and <b>Next</b>:
        <ul>
            <li>Click <b>Cancel</b> to cancel the link creation and leave the Time Slots dialog</li>
            <li>Click <b>Next</b> to proceed with the following Time Slots dialog with a calendar schedule to select the slots available for booking</li>
        </ul>
    </p>
    <p>
        <b>2.</b> The <b>subject</b> of the meeting. {{ short_name }} prefills it with the email subject, but you can modify it
    </p>
    <p>
        <b>3.</b> The <b>location</b> where the meeting will held (meeting room, online, etc.)
    </p>
    <p>
        <b>4.</b> The <b>duration</b> of slots for the meeting. You can preset the meeting duration varying from 15 minutes to 8 hours
    </p>
    <p>
        <b>5.</b> The <b>required attendees</b> are prefilled with the email recipients. If the in-org attendees are added to this field, {{ short_name }} analyzes their and the organizer's calendar data and shows only the slots that are available for all meeting participants. The internal in-org attendees added to this field will receive the invite for this meeting once the link recipient books it. More information <a href="#automatic_parsing_of_in-org_mandatory_attendees_availability">here</a>
    </p>
    <p>
        <b>6.</b> The <b>optional attendees</b> who will receive the invite for this meeting once the link recipient books it. It's prefilled  with CC email recipients
    </p>
    <p>
        <b>7.</b> <b>Business record</b> in Salesforce (Account, Opportunity, Case, etc.), which will be linked with the resulting Salesforce event once the link recipient books a meeting
    </p>
    <p>
        <b>8.</b> <b>People record</b> in Salesforce (Lead, Contact, Person Account, etc.), which will be linked with the resulting Salesforce event once the link recipient books a meeting
    </p>
    <p>
        <b>9.</b> The meeting <b>reminder</b>. Select this checkbox to create a reminder about this meeting
    </p>
     <p>
        <b>10.</b> The <b>Slots in</b> drop-down list allows selecting different time zone for time slots if required
    </p>
    <p>
        <b>11.</b> The <b>main body</b> field. Here you can add the meeting description, notes, and other related information
    </p>
</details>

&nbsp;

&nbsp;

### First Time Slots dialog

#### Fill in the general meeting parameters

**3.** Fill in the basic meeting details in the first Time Slots dialog:

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\How-to-Send-Meeting-Time-Slots-(Adaptive-view)\ts-general.png" style="width:41.27%%; display:inline-block; vertical-align:middle; margin-left:1px;float: right;padding: 10px 5px">
</p>

* The **Meeting subject** field is prefilled with the subject of the related email (if any), and you can edit it according to your needs

* In the **Location** field, you can select a location from your [MS Exchange rooms resources](https://docs.microsoft.com/en-us/exchange/recipients/room-mailboxes?view=exchserver-2019) or manually enter a location (including online services)

* In the **Duration** drop-down list, you can set the meeting slot duration from 15 minutes up to 8 hours

* In the **Attendees (required)** field, you can add the participants whose presence is required at the meeting. It's prefilled with the email recipients. Also, you can add internal attendees who will receive the invite for this meeting once the link recipient books it

!!! note "Note"
    If you add any in-org attendees (they must belong to your Google workspace) in the **Attendees (required)** field, the resulting Booking page will show only the time slots that are [available on all in-org attendees and organizer's calendars](#automatic_parsing_of_in-org_mandatory_attendees_availability). This ensures that the selected slot will be convenient and available for all required in-org attendees
&nbsp;    

* In the **Attendees (optional)** field, you can add the participants, who will also receive the invite for this meeting once the link recipient books it, but as optional attendees. Note that optional attendees' calendars are disregarded on building availability table

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sharing-Calendar-Availability-(Adaptive-view)\description.png" style="width:39.9%; display:inline-block; vertical-align:middle; margin-left:1px;float: right; padding: 0px 5px">
</p>

* In the **Body (Description)** field (placed at the bottom of the Time Slots dialog), you can add additional information for participants, which will be saved as a meeting description in the MS Exchange / Office 365 calendar and in Salesforce. Note that the generated email will not include this text in its body

&nbsp;

&nbsp;

#### Link the meeting with Salesforce records

**4\.** Link the meeting with the [Salesforce Business and People records](https://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/):

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sharing-Calendar-Availability-(Adaptive-view)\bookme-linked.png" style="width:42.33%; display:inline-block; vertical-align:middle; margin-left:1px;float: right;padding: 30px 0px">
</p>

* In the **Save to Salesforce record** search box, you can find and select a Business record (Account, Opportunity etc.), which will be linked with the resulting Salesforce event once the link recipient books a meeting

* In the **Save to Lead or Contact** search box, you can find and select a People record, which will be linked with the resulting Salesforce event once the link recipient books a meeting

!!! note "Note"
    If you faced a situation when the booked meeting had linked to the wrong Contact in Salesforce, refer to [this article](../events-linked-to-wrong-contact/) describing how to resolve the problem and prevent it in the future

&nbsp;

&nbsp;

#### Fill in the advanced meeting parameters

!!! tip "Tip"
    <p>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\How-to-Send-Meeting-Time-Slots-(Adaptive-view)\ts-collapse.gif" style="width:44.08%; display:inline-block; vertical-align:middle; margin-left:1px;float: right; padding: 5px">
    </p>
    If you don't need the Advanced fields and controls in the Time Slots dialog, click the **v** (collapse) icon next to the **Advanced options** section title to hide them

&nbsp;

**5\.** Fill in the optional meeting details under the *Advanced options* tab:

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\How-to-Send-Meeting-Time-Slots-(Adaptive-view)\ts-advanced.png" style="width:41.27%; display:inline-block; vertical-align:middle; margin-left:1px;float: right;padding: 10px 5px">
</p>

* Using the **Reminder** field, you can enable and set an [MS Outlook reminder](http://support.office.com/en-us/article/set-or-remove-reminders-7a992377-ca93-4ddd-a711-851ef3597925) in your Outlook calendar to notify you before the meeting starts

* Using the **Slots in** drop-down list, you can set the custom time zone for the meeting time slots.  
For example, if your recipient is located in a different time zone. Also, you can quickly find the needed time zone using the search field

&nbsp;

&nbsp;

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\How-to-Send-Meeting-Time-Slots-(Adaptive-view)\ts-next.png" style="width:41.27%; display:inline-block; vertical-align:middle; margin-left:1px;float: right; padding: 5px">
</p>

**6\.** After populating all required fields in the first Time Slots dialog, click **Next** to go to the second one

&nbsp;

&nbsp;

### Second Time Slots dialog

#### Select preferred time slots for the meeting

In the second Time Slots dialog, {{ product_name }} reads your MS Exchange / Office 365 calendar data builds daily tables of your unoccupied time slots, so you can easily find available time slots and select the preferred ones. Also, if you added any of your colleagues in the **Attendees (required)** field, these tables consider [your colleagues' calendar data](#automatic_parsing_of_in-org_mandatory_attendees_availability) and show only the time slots that are available for all in-org attendees.

&nbsp;

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\How-to-Send-Meeting-Time-Slots-(Adaptive-view)\ts-selector.gif" style="width:41.14%; display:inline-block; vertical-align:middle; margin-left:1px;float: right; padding: 0px 5px">
</p>

**7\.** Select the preferred time slots within the unoccupied spans in the schedule:

* Open your preferred date by clicking the Date selector at the top of the dialog; you can also navigate between days by clicking the arrow icons on either side of the selector

* Pick meeting time spans that suit you best by clicking on a free slot and dragging the cursor down; selected time spans can be longer than the meeting Duration specified in the previous dialog but cannot be shorter

!!! note "Note"
    If you select several adjacent time slots, they do not get merged, and displayed as separate time slots on the Booking page

&nbsp;

!!! tip "Tip"
    Note that you can select multiple time slots on different dates: after you have selected slots on one date and then switch to another date using the calendar control at the top, all previously selected slots are kept

&nbsp;

&nbsp;

#### Generate and insert Time Slots links

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\How-to-Send-Meeting-Time-Slots-(Adaptive-view)\ts-insert.png" style="width:41.27%; display:inline-block; vertical-align:middle; margin-left:1px;float: right; padding: 5px">
</p>

**8\.** Click **Insert** in the upper right corner of the second dialog, and the generated Time Slots links will be automatically inserted into the new email message

&nbsp;

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\How-to-Send-Meeting-Time-Slots-(Adaptive-view)\ts-email.png">
</p>

&nbsp;

Now you can send the email containing the Time Slots links out to the recipient, so they can select a convenient time slot and book a meeting with you.

!!! warning "Important"
    The Time Slot links are valid for **60 days** after they were generated or till the date of the latest proposed slot, whichever comes first. Also, Time Slots links expire once the recipient books the meeting. The 60 days validity period can be adjusted [on a request sent to our CSM team](mailto:support@revenuegrid.com)

&nbsp;

!!! note "Note"
    Please note that when you are using this feature from the Sidebar running in MS Outlook [on a mobile device](../Using-on-iPhone/), you will not be able to edit the text of the resulting email – a pre-configured [Salesforce message template](https://help.salesforce.com/articleView?id=email_templates_lightning_parent.htm&type=5) will be used instead, and the email with the links you generated will be sent out by the Add-In automatically

&nbsp;

!!! tip "Tip"
    If you want to set up a custom Time slots email message template, refer to [this article](../Using-Salesforce-Templates/#custom_meetings_scheduler_templates)

&nbsp;

&nbsp;

* * *

&nbsp;

&nbsp;

## Automatic Parsing of In-Org Mandatory Attendees' Availability

If any of the meeting's required attendees are your colleagues (their email addresses are recognized as [internal](../Initial-Search-and-Applied-Record-Filters/#internal_emails_corporate_domains_and_the_blocklist)),  {{ product_name }} considers their calendar data and reflects it on a schedule in the second Time Slots dialog along with yours. This feature allows you to select time slots suiting your colleagues' calendars:

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\How-to-Send-Meeting-Time-Slots-(Adaptive-view)\ts-colleagues.png">
</p>

&nbsp;

Note that you can not select time slots within day-long spans reserved for [all-day calendar events](https://support.office.com/en-us/article/create-an-all-day-event-52420de0-8f5a-41b2-a165-070588896c25) with [*busy*, *out of office*, and *working elsewhere*](#calendar_slots_status_parsing_by_meeting_scheduler) statuses. However, [*free* and *tentative*](#calendar_slots_status_parsing_by_meeting_scheduler) (non-mandatory) all-day events do not impose this limitation and are not indicated in the Time Slots calendar. The same handling patterns are also applied for non-all-day meetings and appointments.

&nbsp;

&nbsp;

* * *

&nbsp;

&nbsp;

## Time Slots Dialog Auto-Filling

In the Time Slots dialog, {{ product_name }} prefills some fields with the default values, the data from the selected email (if any), and your MS Exchange / Office 365 account. The following fields will be prefilled:

* *Meeting subject* – the subject of the selected or opened email when the Time Slots icon is clicked in the Sidebar

* *Duration* – 30 minutes

* *Attendees (required)* – recipients from the *To* field of the selected or opened email when the Time Slots icon is clicked

* *Attendees (optional)* – recipients from the *CC* field of the selected or opened email when the Time Slots icon is clicked

* *Reminder* – None

* *Slots in* – time zone specified in your [mail account settings](https://support.microsoft.com/en-us/office/add-remove-or-change-time-zones-5ab3e10e-5a6c-46af-ab48-156fedf70c04)

&nbsp;

Also, there is a possibility to set custom values that would be prefilled every time you open the Time Slots dialog in the {{ product_name }}. To get this option configured, please send a detailed request to [our Support team](mailto:support@revenuegrid.com).

&nbsp;

&nbsp;

* * *

&nbsp;

&nbsp;

## How to select a Time Slot (Recipient Side)

!!! note "Note"
    The Booking page language is set according to the locale specified in the web browser of the Time Slots links recipient

&nbsp;

When a recipient opens the invitation link, they can select the preferred slot by clicking on their preferred date and time. Additionally, recipients can change the time zone for the available time slots using the drop-down list above the list of available time slots.

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\How-to-Send-Meeting-Time-Slots-(Adaptive-view)\booking-ts1.png" class="minimized">
</p>

&nbsp;

!!! note "Note"
     When a recipient clicks on their preferred slot, {{ product_name }} checks if it is still available in the organizer and in-org required attendees' calendars. In case it is occupied, {{ short_name }} suggests recipient to select another slot. Also, the recipient can actualize information about available slots by refreshing the Booking page

&nbsp;

After a recipient selects a slot on the Booking page, they will see a *Booking confirmation* dialog, where they need to click the **Book meeting** button to finish the booking.

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\How-to-Send-Meeting-Time-Slots-(Adaptive-view)\booking-ts2.png" class="minimized">
</p>

&nbsp;

As soon as a time slot is selected and confirmed by the recipient, it gets automatically reserved in the organizer's and attendees' calendars, and they will receive a corresponding email notification.

&nbsp;

!!! warning "Important"
    The time slot links are valid for **60 days**; they expire after the meeting date/time passes or 60 days after they are generated. A meeting may be scheduled for any date in the future, but the recipients must reserve their preferred time slots within 60 days. This validity period can be adjusted [on a request sent to our CSM team](mailto:support@revenuegrid.com)

&nbsp;

If you send Time Slots to multiple recipients (potential attendees), only one meeting can be booked using them. Once the meeting is booked, the Time Slots links get expired. If other recipients try to book the meeting using the same links, they will see the following notification:

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\How-to-Send-Meeting-Time-Slots-(Adaptive-view)\already-scheduled.png">
</p>

&nbsp;

&nbsp;

* * *

&nbsp;

&nbsp;

## Calendar slots Status parsing by Meeting Scheduler

When {{ short_name }} parses occupied slots data from a users' MS Exchange / Office 365 calendar, it applies the following rules to interpret the slots' specific statuses. Keep in mind that this data is **not** parsed continuously in real time, instead it is a "snapshot" of your calendar at the time when the meeting was initiated with {{ short_name }} Meeting Scheduler.

&nbsp;

| Slot status in MS Outlook                    | Slot status in Meeting Scheduler tables |
| -------------------------------------------- | --------------------------------------- |
| {Outside of Work time set in MS Outlook}     | Free                                    |
| Free                                         | Free                                    |
| Busy                                         | Busy                                    |
| Working Elsewhere                            | Busy                                    |
| Tentative                                    | Free                                    |
| Out of Office (OOF)                          | Busy                                    |

&nbsp;

!!! tip "Tip"
    {{ short_name }} features an optional possibility to make the system treat Tentative slots as Busy instead of Free. This mechanics is managed Org-wide or for individual users, via the global setting *ShowTentativeAsBusy*. To enable this function refer to your Admin

&nbsp;

&nbsp;

* * *

&nbsp;

&nbsp;

## MS Teams integration on Location selection

The customers may request [our Support team](mailto:support@revenuegrid.com) to enable a special MS Teams integration option that allows {{ product_name }} users to automatically generate [MS Teams meeting rooms links](https://docs.microsoft.com/en-us/microsoftteams/rooms/) for meetings created with {{ short_name }} Time Slots and Book Me features. This feature is available for Office 365 mailboxes, via [MS Graph](../MS-Graph/) or hybrid MS Graph-[EWS](../Working-With-EWS/) connectivity: the [Add-In](../AddIn-vs-Sync-Functions/) works over Graph and [Sync Engine](../AddIn-vs-Sync-Functions/) works over EWS.

&nbsp;

To generate and send an MS Teams meeting link, once the feature was configured by our Support team or [the local Admin](../How-to-Log-In-to-the-Admin-Panel/):

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\How-to-Send-Meeting-Time-Slots-(Adaptive-view)\MS-Teams.png" style="width:41.27%; display:inline-block; vertical-align:middle; margin-left:1px;float: right;padding: 0px 5px">
</p>

**1\.** In the Time Slots creation dialog, click the **Location** field and enter *MS Teams* (or another custom name configured for your Org) or select this item on the top of the picklist   

&nbsp;

**2\.** Complete Time Slots links generation and send them to the recipient(s)

&nbsp;

&nbsp;

### Special considerations for using this feature

* In order to open the MS Teams meeting link generated this way the recipient does **not** have to belong to your Organization, but must have MS Teams running

* A new unique MS Teams meeting room link is generated for every meeting. Several invitees from inside or outside of your company can join the meeting by opening the MS Teams link

* Note that the MS Teams meeting link is **not** be included in the Time Slots email; instead, it will be added to the MS Outlook meeting created in the recipient's Calendar

!!! tip "Tip"
    To make sure that the recipients do not lose the link, it is recommended to mention in invite email's body that the link for joining the meeting will be available in the meeting's Description on the recipients' MS Outlook calendar as soon as they book the meeting

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\How-to-Send-Meeting-Time-Slots-(Adaptive-view)\Teams-link.png">
</p>

&nbsp;

&nbsp;

* * *

&nbsp;

&nbsp;

## Shared Calendars compatibility

The Book Me and Time Slots features are fully compatible with [MS Exchange / Office 365 Shared calendar](https://docs.microsoft.com/en-us/outlook/troubleshoot/calendaring/how-to-share-calendar-and-contacts) use scenarios. Different users viewing a shared calendar can initiate {{ short_name }} Meeting Scheduler meetings assigned to it by following [the same steps](#to_initiate_a_meeting_by_sharing_your_availability_periods_with_business_contacts), with a single addition, you should specify what calendar you are generating the link for:

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\How-to-Send-Meeting-Time-Slots-(Adaptive-view)\shared-select.png">
</p>

&nbsp;

A Time Slots / Book Me meeting can be created in a shared calendar even if the calendar's account does not have the [{{ short_name }} Add-In](../Introduction/) or [Sync Engine](../Synchronization-Engine-An-Overview/) configured, but in the latter case the resulting meeting will **not** get synced to Salesforce.

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
<div class="banners banner-2">
  <img src="../../assets/images/banners/banner-2.svg" style="width: 100%; height: 100%;">
  <a class="button" href="https://revenuegrid.com/request-demo/?utm_source=kb_rg&utm_medium=referral&utm_campaign=eac_demo&utm_content=banner" target="_blank">Book a free demo</a>
</div>