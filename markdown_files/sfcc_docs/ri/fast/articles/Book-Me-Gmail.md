---
description: How to share your calendar availability periods (Book Me) using RG Email Sidebar
---
# How To Use Book Me in the [Chrome Extension](../Using-the-Solution-for-Salesforce-and-Gmail/)  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*11 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

The Share Calendar Availability (*Book me*) feature allows parsing your and your colleagues' availability periods based on Google calendar data to be sent to your business contacts, for example to negotiate a meeting time convenient for all participants involved or to schedule a series of meetings with different contacts. 

The unoccupied time slots from meeting organizer calendar(s) are parsed to be saved as a link to an interactive scheduling table webpage (Booking page). 

When building availability tables without specified "Until" date on Book Me link creation page, {{ short_name }} shows the unoccupied time slots from calendar(s) over a 365 day span. This limit can be adjusted by request sent to [our CSM team](mailto:support@revenuegrid.com). 

&nbsp;

!!! tip "Tip"
    Also, see [this {{ company_name }} blog article](https://revenuegrid.com/blog/how-to-schedule-a-meeting-by-email/) for special insights about scheduling meetings via emails

&nbsp;

The organizer's and required in-org invitees' availability spans are parsed on Book Me link generation, and later if a another slot gets occupied that is also reflected on the [Booking page](../Sharing-Calendar-Availability-%28Adaptive-view%29/#how_to_book_a_slot_recipient_side) viewed by the recipient.  

As soon as a recipient clicks on their preferred slot, {{ product_name }} checks if the slot is still available in the organizer's and required in-Org attendees' calendars. In case it was occupied by another booking, the recipient is suggested to pick another slot. In addition, by refreshing Booking page browser window, the recipient can actualize the availability table after such checks.      


&nbsp;

Book Me links can be generated by the Add-In even if [{{ short_name }} Sync Engine](../Synchronization-Engine-An-Overview/) is not running; however, in this case, if any slot is booked, the resulting meetings won't be synced in the Salesforce calendar till [syncing is resumed](../Handling-Sync-Issues/).

&nbsp;
    
!!! tip "Tip"
    See [this article](../Sharing-Calendar-Availability-%28Adaptive-view%29/) to learn how to use the Book Me feature in {{ short_name }} Outlook Add-In

&nbsp;

&nbsp;

* * *

&nbsp;

## To share your availability periods with your contacts

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Gmail\bmg-open.gif" style="width:47.18%; display:inline-block; vertical-align:middle; margin-left:5px;float: right">
</p>

&nbsp;

**1\.** Open {{ product_name }} for a relevant opened or new created email message in Gmail by clicking the **Open {{ product_name }}** icon

<br><br><br><br><br><br><br><br>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sharing-Calendar-Availability-(Adaptive-view)\open-bookme.png" style="width:46.82%; display:inline-block; vertical-align:middle; margin-left:1px;float: right">
</p>

**2\.** In the Sidebar, click on the **Book Me** icon in the **Smart Actions** bottom toolbar

&nbsp;

&nbsp;

Once you click on the **Book Me** icon, you will see the following **Book Me** page in the Sidebar:

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sharing-Calendar-Availability-(Adaptive-view)\bookme-full.png">
</p>

&nbsp;

<details><summary> >>> Click to view details <<< </summary>
    <p>
        <b>1.</b> Action buttons <b>Cancel</b> and <b>Insert</b>:
        <ul>
            <li>Click <b>Cancel</b> to cancel the link creation and leave the Book Me dialog</li>
            <li>Click <b>Insert</b> to generate the Book Me link after filling in all required fields</li>
        </ul>
    </p>
    <p>
        <b>2.</b> The <b>subject</b> of the meeting. {{ short_name }} prefills it with the email subject, but you can modify it
    </p>
    <p>
        <b>3.</b> The <b>location</b> where the meeting will be held (meeting room, online, etc.)
    </p>
    <p>
        <b>4.</b> The <b>duration</b> of time slots for the meeting. You can select up to three different slots durations
    </p>
    <p>
        <b>5.</b> The <b>required attendees</b> are prefilled with the email recipients. If the in-org attendees are added to this field, {{ short_name }} analyzes their and the organizer's calendar data and shows only the slots that are available for all meeting participants. The internal in-org attendees added to this field will receive the invite for this meeting once the link recipient books it
    </p>
    <p>
        <b>6.</b> The <b>optional attendees</b> who will receive the invite for this meeting once the link recipient books it. It's prefilled with CC email recipients
    </p>
    <p>
        <b>7.</b> <b>Business record</b> in Salesforce (Account, Opportunity, Case, etc.), which will be linked to the resulting Salesforce event once the link recipient books the meeting
    </p>
    <p>
        <b>8.</b> <b>People record</b> in Salesforce (Lead, Contact, Person Account, etc.), which will be linked to the resulting Salesforce event once the link recipient books the meeting
    </p>
    <p>
        <b>9.</b> Allow or disallow to <b>invite additional participants</b> (as optional attendees) while booking a meeting on the Booking page
    </p>
    <p>
        <b>10.</b> The <b>time buffer between the meetings</b>. You can set a minimum time gap between meetings to get ready for the next one or have a break
    </p>
    <p>
        <b>11.</b> The meeting <b>reminder</b>. Select this checkbox to create a reminder about this meeting
    </p>
    <p>
        <b>12.</b> The <b>minimal span between the moment of booking and the actual start</b> of the meeting. 
        For example, this parameter won't allow anybody to book a meeting within 30 minutes from now, even if you have an available slot
    </p>
    <p>
        <b>13.</b> <b>Disregard organizer's calendar</b>. If enabled, this parameter allows selecting the occupied slots on the organizer's calendar for booking meetings. Mind that the organizer's status will be set to "*Free*" for the booked meetings
    </p>
    <p>
        <b>14.</b> Select the <b>weekdays</b> available for the meeting booking
    </p>
    <p>
        <b>15.</b> Set the <b>day hours</b> available for the meeting booking
    </p>
    <p>
        <b>16.</b> Set the <b>dates range</b> available for the meeting booking
    </p>
    <p>
        <b>17.</b> The <b>body</b> field. Here you can add the meeting description, notes, and other related information
    </p>
    <p>
        <b>18.</b> <b>Manage defaults</b> opens the <b>Book Me defaults</b> page, where you can set the default field values that will be prefilled in the <b>Book Me</b> dialog when you open it. More information <a href="#managing_book_me_defaults">here</a>
    </p>
</details>

&nbsp;

&nbsp;

### Fill in the general meeting parameters

**3\.** Fill in the basic meeting details in the opened Book Me dialog:

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sharing-Calendar-Availability-(Adaptive-view)\bookme-general.png" style="width:47.05%; display:inline-block; vertical-align:middle; margin-left:1px;float: right;padding: 30px 0px">
</p>

* The **Meeting subject** field is prefilled with the subject of the related email (if any), and you can edit it if necessary

* In the **Location** field, you can select a room or location from your Google workspace or manually enter a location (including online services)

* In the **Duration**, you can select up to three different meeting slot durations that the Book Me link recipients may choose among on the resulting Booking page

* In the **Attendees (required)** field, you can add the participants whose presence is required at the meeting. It's prefilled with the email recipients. Also, you can add internal attendees who will receive the invite for this meeting once the link recipient books it

!!! note "Note"
    If you add any in-org attendees (they must belong to your Google workspace) in the **Attendees (required)** field, the resulting Booking page will show only the time slots that are available on all in-org attendees and organizer's calendars. This ensures that the selected slot will be convenient and available for all required in-org attendees

* In the **Attendees (optional)** field, you can add the participants, who will also receive the invite for this meeting once someone books it, but as optional attendees. Note that optional attendees' calendars are disregarded on building availability table

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sharing-Calendar-Availability-(Adaptive-view)\description.png" style="width:39.9%; display:inline-block; vertical-align:middle; margin-left:1px;float: right; padding: 0px 5px">
</p>

* In the **Body (Description)** field (at the bottom of the Book Me dialog), you can add additional information for participants, which will be saved as a meeting description in the Google calendar and in Salesforce. This field is limited to 32k characters, if the description text is longer, it will be truncated to match this limit. Note that the generated email will not include this text in its body

&nbsp;

&nbsp;

### Link the meeting with Salesforce records

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

### Fill in the advanced meeting parameters

!!! tip "Tip"
    <p>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sharing-Calendar-Availability-(Adaptive-view)\collapse-advanced.gif" style="width:42.98%; display:inline-block; vertical-align:middle; margin-left:1px;float: right; padding: 5px">
    </p>
    If you don't need the Advanced fields and controls in the Book Me dialog, click the **v** (collapse) icon next to the **Advanced options** section title to hide them

&nbsp;

**5\.** Fill in the Advanced meeting details to customize the calendar availability according to your needs:

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sharing-Calendar-Availability-(Adaptive-view)\inviting.png" style="width:41.27%; display:inline-block; vertical-align:middle; margin-left:1px;float: right;padding: 10px 5px">
</p>

* Select the **Allow inviting guests** checkbox to allow recipients of the generated Book Me link to invite extra guests as optional attendees. Recipient can add up to 10 guest emails on the Booking page

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sharing-Calendar-Availability-(Adaptive-view)\buffer.png" style="width:41.27%; display:inline-block; vertical-align:middle; margin-left:1px;float: right;padding: 10px 5px">
</p>

* **Time buffer b/w meetings** allows you to set a gap between consecutive meetings booked by different recipients via the Book Me links, so you can prepare for the next meeting or have a break

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sharing-Calendar-Availability-(Adaptive-view)\reminder.png" style="width:41.27%; display:inline-block; vertical-align:middle; margin-left:1px;float: right;padding: 5px 5px">
</p>

* Using the **Reminder** field, you can enable and set a [Google reminder](https://support.google.com/calendar/answer/6285327?hl=en&co=GENIE.Platform%3DDesktop) in your Google calendar to notify you before the meeting starts

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sharing-Calendar-Availability-(Adaptive-view)\span-bw.png" style="width:41.27%; display:inline-block; vertical-align:middle; margin-left:1px;float: right;padding: 10px 5px">
</p>

* Using the **Minimal span between booking & actual start** field, you can set from 30 minutes up to 7 days span to ensure that you will have enough time to get prepared for the meeting after a slot is picked by Book Me link recipient

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sharing-Calendar-Availability-(Adaptive-view)\disregard.png" style="width:41.23%; display:inline-block; vertical-align:middle; margin-left:5px;float: right;padding: 10px 5px">
</p>

* Select the **Disregard organizer's calendar** to allow recipients of the generated Book Me link to book meetings on the occupied slots of your (organizer's) calendar. Note that if this parameter is enabled, your (organizer's) status on the booked meetings will be shown as **Free**. This feature is useful if you organize meetings for other people, where your participation is optional or not required.

&nbsp;

!!! tip "Tip"
    {{ short_name }} features an optional possibility to make the system treat Tentative slots as Busy instead of Free. This mechanics is managed Org-wide or for individual users, via the global setting *ShowTentativeAsBusy*. To enable this function refer to your Admin

&nbsp;

The advanced parameters described below allow you to set the calendar availability limits by selecting the weekdays, work hours, and dates range for generating available meeting slots on the Booking page. Adjust these limits to set the availability spans specific to your regular work schedule, for example if you are only available for meeting the customers on Mondays and Thursdays from 2:30pm until 5pm; in some scenarios you may also need to make these limits broader, for example if you want to arrange a Book Me meeting outside of your working hours or on a weekend.

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sharing-Calendar-Availability-(Adaptive-view)\availability.gif" style="width:41.27%; display:inline-block; vertical-align:middle; margin-left:1px;float: right;padding: 0px 5px">
</p>

* The **Available on (days of the week)** selection allows you to define the weekdays which will be available or unavailable for the meeting booking. For example, you can select the weekends to be available meeting booking or disable meetings scheduling on Mondays

* Using the **From** and **Until** drop-down lists, you can set the hours range that will be used for generating available slots to book the meeting

* The **From date** and **To date** calendar fields allow you to define the dates range that will be shown with the available slots on the Booking page. For example, you can use them for limited-time activities (conferences, field visits, business trips, etc.)

&nbsp;

!!! note "Note"
    {{ short_name }} prefills the **Available on (days of the week)** selection and the **From** and **Until** down-drop lists with the default values. Also, you can adjust the prefilled values using the [Book Me defaults](#managing_book_me_defaults) feature
    
&nbsp;

&nbsp;

### Generate and insert the Book Me link

Once all necessary fields in Book Me dialog are filled in, {{ product_name }} is ready to generate a short link to a Booking web page with a table showing the available time slots based on your calendar data, your colleagues (if any) calendar data, and other specified parameters.

&nbsp;

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sharing-Calendar-Availability-(Adaptive-view)\insert.png" style="width:39.42%; display:inline-block; vertical-align:middle; margin-left:1px;float: right;padding: 0px 0px">
</p>

**6\.** Click **Insert** in the upper right corner of the page, and the link will be automatically inserted into the new email message

<p>
    <img src="../../assets/images/Using-SmartCloud-Connect/How-To-s/Gmail/bmg-link.png">
</p>

&nbsp;

Now you can add other information to the email containing the Book Me link and send it to the recipients, so they can select a convenient day and time and book a meeting with you.

&nbsp;

!!! tip "Tip"
    If you want to set a custom share calendar availability message template, refer to [this article](../Using-Salesforce-Templates/#custom_meeting_scheduler_templates)

&nbsp;

&nbsp;

* * *

&nbsp;

## Book Me Dialog Auto-Filling

In the Book Me dialog, {{ product_name }} prefills some fields with the default values, the data retrieved from the selected email (if any), and your Google account. The following fields are prefilled with default values:

* *Meeting subject* – the subject of the selected or opened email when the Book Me icon is clicked in the Sidebar

* *Duration* – 30 minutes

* *Attendees (required)* – recipients from the *To* field of the selected or opened email when the Book Me icon is clicked

* *Attendees (optional)* – recipients from the *CC* field of the selected or opened email when the Book Me icon is clicked

* *Time buffer b/w meetings* – 0 minutes

* *Reminder* – None

* *Minimal span between booking & actual start* – 0 minutes

* *Available on (days of the week)* – from Monday till Friday

* *From* and *Until* – from 8:00 AM till 5:00 PM

&nbsp;

&nbsp;

### Managing Book Me defaults

Also, using the **Book Me defaults** feature, you can set custom values that would be prefilled every time you open the Book Me dialog in {{ product_name }}.

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sharing-Calendar-Availability-(Adaptive-view)\manage-defaults.png" style="width:41.27%; display:inline-block; vertical-align:middle; margin-left:1px;float: right;padding: 5px 5px">
</p>

To open the **Book Me defaults** page, open {{ product_name }}, click the **Book Me** icon in the Smart Actions bottom toolbar, and click **Manage defaults** at the bottom of the Book Me dialog.

&nbsp;

On the opened Book Me defaults page, you can manage the default values for the **General** and **Advanced** options:

* In the **General** section, you can set the defaults for *Meeting subject format*, *Meeting subject*, *Location*, *Duration*, *Time buffer b/w meetings*, *Attendees (required)*, *Attendees (optional)*, and *Body (Description)*

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sharing-Calendar-Availability-(Adaptive-view)\defaults-general.png">
</p>

&nbsp;

* In the **Advanced** section, you can set the defaults for *Reminder*, *Minimal span between booking & actual start*, *Maximum allowed events per day for this type of event*, *Available on (days of the week)*, *From* and *Until* time range, *Allow inviting guests*, and *Disregard organizer's calendar* parameters

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sharing-Calendar-Availability-(Adaptive-view)\defaults-advanced.png">
</p>

&nbsp;

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sharing-Calendar-Availability-(Adaptive-view)\defaults-save.png" style="width:37.04%; display:inline-block; vertical-align:middle; margin-left:1px;float: right;padding: 0px 0px">
</p>

Once you customize the *Book Me defaults* according to your preferences, click **Save** and refresh {{ product_name }} to apply the changes.

&nbsp;

&nbsp;

* * *

&nbsp;

&nbsp;

## How to Book a Slot (Recipient Side)

!!! note "Note"
    The Booking page language is set based on the locale specified in the web browser of the Book Me link recipient

&nbsp;

When the recipient opens the Book Me link, they can select the time slot by clicking on the preferred date and time. The time zone of the generated Booking page will be pre-set for each recipient based on their email client data. Also, they can select a specific time zone using the drop-down list above the list of available time slots.

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sharing-Calendar-Availability-(Adaptive-view)\booking-page1.png" class="minimized">
</p>

&nbsp;

!!! note "Note"
    When a recipient clicks on the preferred slot, {{ product_name }} checks if it is still available in the organizer and in-org required attendees' calendars. In case it is occupied, {{ short_name }} suggests recipient to select another time slot. Also, the recipient can actualize information about available slots by refreshing the Booking page

&nbsp;

After recipient selects a slot on the Booking page, they also need to fill in their *Full name* and *Email* address in the *Booking Confirmation* dialog and click the **Book meeting** button.

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sharing-Calendar-Availability-(Adaptive-view)\booking-page2.png" class="minimized">
</p>

&nbsp;

As soon as a slot is selected and booked by the recipient, it gets automatically reserved in your calendar, and you receive a corresponding email notification.

!!! note "Note"
    To prevent calendar spamming activities via the Book Me link, a [standard reCAPTCHA v3 anti-bot check](https://www.google.com/recaptcha/intro/v3.html) is implemented on the Booking page

&nbsp;

&nbsp;

### The Extra Fields: Phone Number and Notes

The Booking page also includes the optional fields *Phone number* and *Notes*. These fields allow meeting attendees to share their phone numbers with the Organizer and other participants for direct connection or providing extra details prior to the meeting.

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sharing-Calendar-Availability-(Adaptive-view)\extra-fields.png">
</p>
    
!!! warning "Important"
    Since entered *Phone number* and *Notes* get appended to the meeting’s *Description*, they also get conveyed to **all** required and optional meeting invitees. For this reason, the recipients should always consider the privacy requirements for the *Phone number* sharing and what information can be listed in meeting *Notes*

&nbsp;

&nbsp;

&#160;
 &#160;



