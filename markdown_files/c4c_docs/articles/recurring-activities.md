# Recurring Calendar Activities (Visit or Appointment) in Add-In

&nbsp;

&nbsp;

**[ This article is work-in-progress ]**

&nbsp;

&nbsp;

## What is recurring activity

A **recurring** or **repeating** event is simply any event that will occur more than once on your calendar. The recurring event may end after a particular number of occurrences, may last up to a fixed End Date or forever. There are certain conditions on how many of those occurrences are synced to SAP Cloud for Customer.

The limit on occurrences that are visible in SAP Cloud for Customer are as follows:

* Daily and weekly frequency: two months
* Monthly frequency: six months
* Events with a yearly pattern are not supported and won't be synced

&nbsp;

It is impossible to create a recurring event via the SAP Cloud for Customer interface, therefore, it is unavailable to create it via SSI Add-In. On the other hand, the SSI sync component can create recurrent events on SAP Cloud for Customer (through API). The recurrent series is not visible on SAP Cloud for Customer, however, it may be found under the related tab of a particular object, such as Contact, in the shape of Recurring Activity (Visit or Appointment).

&nbsp;

**Example of Recurring Activity in Add-In**

"*Monthly meeting with Jason*" under related Contact:

<p>
<img src= "..\..\assets\images\recurring-activity\event-1.png">
</p>

&nbsp;

Detailed view of Recurring Activity (Visit):

<p>
<img src= "..\..\assets\images\recurring-activity\event-2.png">
</p>

&nbsp;

* * *

&nbsp;

### Recurrence EndDate is set to ( - ) dash

Sometimes, it may be noticed that Recurrence EndDate is not showing any End Date and reflecting “ - ” (dash). Such behavior can be observed when a user creates a recurrent activity with a particular count of occurrences, and then it is up-synced from MS Outlook to SAP Cloud for Customer. So if the recurring rule defines the **COUNT OF OCCURRENCES** or **No End Date** (on the MS Outlook side), then we send zero time in **RecurrenceEndDate**. This is system behavior related to SAP Cloud for Customer API limitations. Since it results in reflecting 1970 as the year of the End Date, from the user's perspective, it had been decided to show only a dash to avoid confusion.

MS Outlook appointment with a defined count of occurrences:

<p>
<img src= "..\..\assets\images\recurring-activity\event-outlook.png">
</p>

&nbsp;

&nbsp;