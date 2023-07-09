# How Calendar Items Are Processed in SSI

&nbsp;

SAP Cloud for Customer SSI offers a convenient automated workflow for calendar items processing based on server-side synchronization, effectively mirroring your MS Exchange / Office 365 / Gmail and SAP Cloud for Customer calendars, with a small number of non-mirrored exceptions.

Synchronization of MS Exchange / Office 365 / Gmail calendar items – meetings, appointments, all-day events – is performed by [SAP Cloud for Customer SSI Sync](../C4C-SSI-Sync-Overview/) on sync sessions which are carried out every 30 minutes on server-side, unless insta-sync is triggered (see the [Meetings](#meetings) section below).

Calendar items can be saved with the following objects: Individual Customer, Lead, Contact, Account, Opportunity, Ticket, optionally Sales Orders or Sales Quotes, Tasks, E-Mails.

&nbsp;

!!! tip "Tip"
    All MS Exchange / Office 365 calendar item types ([Appointments, Meetings, and All-day Events](https://www.techwalla.com/articles/the-difference-between-appointments-meeting-requests-in-microsoft-outlook)), can be synchronized as [SAP Cloud for Customer Visits](https://help.sap.com/docs/SAP_CLOUD_FOR_CUSTOMER/24765b551a014b779b95c7b07d8e9079/a9c1daef0c5148118ac2f566773fa047.html) by SSI, if you choose that

&nbsp;

* * *

&nbsp;

## Syncing MS Exchange calendar items

### Appointments

To synchronize an MS Exchange / Office 365 appointment with SAP Cloud for Customer calendar:

- Right-click the Appointment in your MS Exchange / Office 365 calendar
- Select **Categorize** > **SAP Cloud for Customer** category; or, to sync the Appointment as a Visit in SAP Cloud for Customer, assign it the **Visit** category

<p>
<img src="..\..\assets\images\Events\category.png">
</p>

&nbsp;

An Appointment marked this way will be synchronized with your SAP Cloud for Customer calendar on the following sync session (within 1-30 minutes). As long as the category remains on the appointment, any future updates made to the Appointment in either MS Outlook Desktop / On the Web or SAP Cloud for Customer will be mirrored on the other side.

!!! note "Note"
    Disregard the custom categories *Account*, *Error in SAP Cloud for Customer SSI*, *Individual Customer* when dealing with calendar items, these are used for syncing Contacts

&nbsp;

&nbsp;

### Meetings

The procedure to get a meeting synchronized in SAP Cloud for Customer is the same as for appointments, but they are synced within 1-3 minutes, via insta-sync, which forces a sync session to run after a meeting assigned the custom *SAP Cloud for Customer SSI* category is created, updated, or deleted.

&nbsp;

&nbsp;

### All-day Events

The procedure to get a meeting synchronized in SAP Cloud for Customer is the same as for appointments and meetings. All-day Events are synchronized within 1-30 minutes (no insta-sync applied). An All-day Event's duration should be less or equal to 24 hours for SAP Cloud for Customer SSI to process it.

&nbsp;

* * *

&nbsp;

## Syncing Google calendar items

Working with Google calendar items, SAP Cloud for Customer SSI for Gmail extension creates a dedicated *SAP Appointments Calendar* and a *SAP Visits Calendar* in Gmail calendar, which are used to synchronize your Gmail events with SAP Cloud for Customer as Appointments or Visits.

&nbsp;

* * *

&nbsp;

## Syncing SAP Cloud for Customer calendar items

When syncing Visits from SAP Cloud for Customer to MS Exchange calendar, you can select which (Organizer or Owner) calendar they should be saved.

* Go to **E-Mail Integration** (1) > **Groupware Settings** (2) > **Settings** (3)
* Find **Sync Visit To:** feature in the **E-Mail Configuration** section
* Select *Organizer* or *Owner* to define the calendar

<p>
<img src="..\..\assets\images\Events\sync-visit-to.png">
</p>

&nbsp;

Note that this feature is applicable only to Visits syncing. SAP Cloud for Customer Appointments are synced strictly to Organizer's calendar.

&nbsp;

&nbsp;