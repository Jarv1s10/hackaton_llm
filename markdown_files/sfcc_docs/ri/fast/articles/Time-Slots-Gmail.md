---
description: Learn how to suggest meeting Time Slots via the RG Chrome Extension
---
# How To Suggest Meeting Time Slots via the [Chrome Extension](../Using-the-Solution-for-Salesforce-and-Gmail/)
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*9 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

{{ product_name }} enables you to schedule meetings with your business contacts without any extra back-and-forth email correspondence. Select available time slots in your calendar, also considering availability of your colleagues involved, create and send out interactive meeting invites, get your calendar automatically updated according to the recipient's time choice. Additionally, {{ product_name }} adds Events created this way to your Salesforce account.


&nbsp;

!!! tip "Tip"
    Also, see [this {{ company_name }} blog article](https://revenuegrid.com/blog/how-to-schedule-a-meeting-by-email/) for special insights
    
&nbsp;

On link opening, selected Time Slots are parsed as a "static shot" that does not exclude suggested slots which got reserved after the link was opened.  

However, any reservations added to the Organizer's calendar later are also considered by the Time Slots system. As soon as a recipient clicks on their preferred slot, {{ product_name }} checks if the slot is still available in the organizer's calendar. In case it is occupied by another reservation, the recipient is suggested to pick another slot. In addition, by refreshing booking page browser window, the recipient can actualize the table after such checks.

Time Slots links can be generated even if [{{ short_name }} Sync Engine](../Synchronization-Engine-An-Overview/) is not running; however, in this case, the resulting meetings cannot be synced in the Salesforce calendar till [syncing is resumed](../Handling-Sync-Issues/).

&nbsp;
    
!!! tip "Tip"
    See [this article](../How-to-Send-Meeting-Time-Slots-(Adaptive-view)/) to learn how to use the Time Slots feature in {{ short_name }} Outlook Add-in

&nbsp;

&nbsp;

* * *

&nbsp;

&nbsp;

## Time Slots links generation steps

To schedule a meeting via the via {{ short_name }} Meeting Scheduler by sharing your preferred time slots through an interactive invitation:

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Gmail\bmg-open.gif" style="width:47.18%; display:inline-block; vertical-align:middle; margin-left:1px;float: right">
</p>

&nbsp;

**1\.** Open an email from/to recipient(s) who you want to initiate a meeting with or create a new email message by clicking the **New email** or the **Reply** button in Gmail and specify one or multiple recipients in the To, Cc, or BCC fields. Then open the {{ product_name }} by clicking the **Open {{ product_name }}** icon

<br><br><br><br><br><br><br><br>

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
            <li>Click <b>Next</b> to proceed with the next Time Slots dialog where you will select the time slots available for booking</li>
        </ul>
    </p>
    <p>
        <b>2.</b> The <b>subject</b> of the meeting. {{ short_name }} prefills it with the email subject, but you can modify it
    </p>
    <p>
        <b>3.</b> The <b>location</b> where the meeting will be held (meeting room, online, etc.)
    </p>
    <p>
        <b>4.</b> The <b>duration</b> of slots for the meeting. You can preset the meeting duration varying from 15 minutes to 8 hours
    </p>
    <p>
        <b>5.</b> The <b>required attendees</b> are prefilled with the email recipients. If the in-org attendees are added to this field, {{ short_name }} analyzes their and the organizer's calendar data and shows only the slots that are available for all meeting participants. The internal in-org attendees added to this field will receive the invite for this meeting once the link recipient books it. More information <a href="#automatic_parsing_of_in-org_mandatory_attendees_availability">here</a>
    </p>
    <p>
        <b>6.</b> The <b>optional attendees</b> who will receive the invite for this meeting once the link recipient books it. It's prefilled with CC email recipients
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
        <b>10.</b> The <b>Slots in</b> drop-down list allows selecting different time zones for time slots if required
    </p>
    <p>
        <b>11.</b> The <b> Body</b> field. Here you can add the meeting description, notes, and other related information
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

* In the **Location** field, you can select a room or location from your Google workspace or manually enter a location (including online services)

* In the **Duration** drop-down list, you can set the meeting slot duration from 15 minutes up to 8 hours

* In the **Attendees (required)** field, you can add the participants whose presence is required at the meeting. It's prefilled with the email recipients. Also, you can add internal attendees who will receive the invite for this meeting once the link recipient books it

!!! note "Note"
    If you add any in-org attendees (they must belong to your Google workspace) in the **Attendees (required)** field, the resulting Booking page will show only the time slots that are available on all in-org attendees and organizer's calendars. This ensures that the selected slot will be convenient and available for all required in-org attendees
&nbsp;    

* In the **Attendees (optional)** field, you can add the participants, who will also receive the invite for this meeting once the link recipient books it, but as optional attendees. Note that optional attendees' calendars are disregarded on building availability table

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sharing-Calendar-Availability-(Adaptive-view)\description.png" style="width:39.9%; display:inline-block; vertical-align:middle; margin-left:1px;float: right; padding: 0px 5px">
</p>

* In the **Body (Description)** field (at the bottom of the Time Slots dialog), you can add additional information for participants, which will be saved as a meeting description in the Google calendar and in Salesforce. Note that the generated email will not include this text in its body

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
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\How-to-Send-Meeting-Time-Slots-(Adaptive-view)\ts-advanced.png" style="width:41.23%; display:inline-block; vertical-align:middle; margin-left:1px;float: right;padding: 10px 5px">
</p>

* Using the **Reminder** field, you can enable and set a [Google reminder](https://support.google.com/calendar/answer/6285327?hl=en&co=GENIE.Platform%3DDesktop) in your Google calendar to notify you before the meeting starts

* Using the **Slots in** drop-down list, you can set the custom time zone for the meeting time slots.  
For example, if your recipient is located in a different time zone. Also, you can quickly find the needed time zone using the search field

&nbsp;

&nbsp;

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\How-to-Send-Meeting-Time-Slots-(Adaptive-view)\ts-next.png" style="width:41.27%; display:inline-block; vertical-align:middle; margin-left:1px;float: right; padding: 5px">
</p>

**6\.** After populating all required fields in the first Time Slots dialog, click **Next** to proceed with the second one

&nbsp;

&nbsp;

### Second Time Slots dialog

#### Select preferred time slots for the meeting

In the second Time Slots dialog, {{ product_name }} reads your Google calendar data and build daily tables of your unoccupied time slots, so you can easily find available time slots and select the preferred ones. Also, if you added any of your colleagues in the **Attendees (required)** field, these tables consider [your colleagues' calendar data](#automatic_parsing_of_in-org_mandatory_attendees_availability) and show only the time slots that are available for all in-org attendees.

&nbsp;

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\How-to-Send-Meeting-Time-Slots-(Adaptive-view)\ts-selector.gif" style="width:41.1%; display:inline-block; vertical-align:middle; margin-left:1px;float: right; padding: 0px 5px">
</p>

**7\.** Select the preferred time slots within the unoccupied spans in the schedule:

* Open the preferred date by clicking the Date selector at the top of the dialog; you can also navigate between days by clicking the arrow icons on either side of the selector

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
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\How-to-Send-Meeting-Time-Slots-(Adaptive-view)\ts-insert.png" style="width:41.23%; display:inline-block; vertical-align:middle; margin-left:1px;float: right; padding: 5px">
</p>

**8\.** Click **Insert** in the upper right corner of the second dialog, and the generated Time Slots links will be automatically inserted into the new email message

&nbsp;

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Gmail\tsg-links.png">
</p>

&nbsp;

Now you can send the email containing the Time Slots links out to the recipient, so they can select a convenient time slot and book a meeting with you.

!!! warning "Important"
    The Time Slot links are valid for **60 days** after they were generated or till the date of the latest proposed slot, whichever comes first. Also, Time Slots links expire once the recipient books the meeting. The 60 days validity period can be adjusted [on a request sent to our CSM team](mailto:support@revenuegrid.com)

&nbsp;

!!! tip "Tip"
    If you want to set up a custom Time slots email message template, refer to [this article](../Using-Salesforce-Templates/#custom_meetings_scheduler_templates)

&nbsp;

&nbsp;

* * *

&nbsp;

&nbsp;

## Automatic Parsing of In-Org Mandatory Attendees' Availability

If any of the meeting's required attendees are your colleagues (their email addresses are recognized as [internal](../Initial-Search-and-Applied-Record-Filters/#internal_emails_corporate_domains_and_the_blocklist)), {{ product_name }} considers their calendar data and reflects it on a schedule in the second Time Slots dialog along with yours. This feature allows you to select time slots suiting your colleagues' calendars:

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\How-to-Send-Meeting-Time-Slots-(Adaptive-view)\ts-colleagues.png">
</p>

&nbsp;

Note that you cannot select time slots within day-long spans reserved for all-day calendar events with *busy* and *out of office* statuses. However, *free* and *tentative* (non-mandatory) all-day events do not impose this limitation and are not indicated in the Time Slots calendar. The same handling patterns are also applied for non-all-day meetings and appointments.

&nbsp;

&nbsp;

* * *

&nbsp;

&nbsp;

## Time Slots Dialog Auto-Filling

In the Time Slots dialog, {{ product_name }} prefills some fields with the default values, the data from the selected email (if any), and your Google account. The following fields will be prefilled:

* *Meeting subject* – the subject of the selected or opened email when the Time Slots icon is clicked in the Sidebar

* *Duration* – 30 minutes

* *Attendees (required)* – recipients from the *To* field of the selected or opened email when the Time Slots icon is clicked

* *Attendees (optional)* – recipients from the *CC* field of the selected or opened email when the Time Slots icon is clicked

* *Reminder* – None

* *Slots in* – time zone specified in your mail account settings

&nbsp;

Also, there is a possibility to set custom values that would be prefilled every time you open the Time Slots dialog in {{ product_name }}. To get this option configured, please send a corresponding request to [our Support team](mailto:support@revenuegrid.com).

&nbsp;

&nbsp;

* * *

&nbsp;

&nbsp;

## How to Select a Time Slot (Recipient Side)

!!! note "Note"
    The Booking page language is set based on the locale specified in the web browser of the Time Slots links recipient

&nbsp;

When a recipient opens the invitation link, they can select the time slot by clicking on their preferred date and time. Additionally, recipients can change the time zone for the available time slots using the drop-down list above the list of available time slots.

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

As soon as a time slot is selected and booked by the recipient, it gets automatically reserved in the organizer's and attendees' calendars, and they will receive a corresponding email notification.

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

&#160;
 &#160;

