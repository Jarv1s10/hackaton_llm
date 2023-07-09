# How Event Sharing by Attendee Feature Works

&nbsp;

&nbsp;

This article describes the Sharing by Attendee feature and how it works within sharing (saving) events from the MS Exchange / Google calendar to SAP Cloud for Customer by the SSI sync engine.

&nbsp;

## Description of the roles and processes

* **Meeting Organizer** – the organizer of meeting in MS Exchange / Google calendar. The organizer cannot be changed for the meeting

* **Meeting Owner** – the owner of the meeting in SAP Cloud for Customer and it can be modified  
The Meeting Owner field in SAP Cloud for Customer depends on the record type – it is always organizer for Appointments and organizer or owner for Visits. The Meeting Organizer in e-mail client calendar shall always be added as involved party to the Appointment or Visit in SAP Cloud for Customer.

**Sharing by Attendee** feature allows syncing events from the MS Exchange / Google calendar to SAP Cloud for Customer by an attendee. Event shared by attendee will be created in SAP Cloud for Customer with an attendee set as an organizer.

If Meeting Organizer does not exist in SAP Cloud for Customer (external agent) or does not sync (sync is disabled, for example) – the event remains as it was initially synced by an attendee. Also, the attendee would keep the event organizer role in SAP Cloud for Customer if the attendee's synchronization session ran before the organizer's session. Only once Meeting Organizer's sync session is completed, the **takeover** will happen.

**Takeover** – the process when Meeting Organizer, who is syncing, claims ownership of the event previously shared by a different Meeting Owner (attendee). After the takeover, the event continues syncing only by Meeting Organizer.

&nbsp;

Thus, when Meeting Organizer's sync launches, SSI perform event search (by GUID) in SAP Cloud for Customer. Once it is found, Meeting Organizer takes over the event – the event's organizer in SAP Cloud for Customer changes from the attendee to Meeting Organizer. After that event stays in sync only with Meeting Organizer. In the attendee's MS Exchange / Google calendar, who initially shared the event and was its organizer, the event becomes unshared (category is cleared).

!!! warning "Important"
    Note that Sharing by Attendee feature **is not supported** for Recurring Events

&nbsp;

***

&nbsp;

## Example of Sharing by Attendee

Let's take a look at the example of Sharing by Attendee feature in action, where the MS Exchange event Organizer and Attendee are the following:

* Organizer – Tetiana

* Attendee – Anna

&nbsp;

The first screenshot shows the Visit shared by Attendee to the SAP Cloud for Customer before Organizer's synchronization run. Anna is assigned as Visit's Owner and Organizer in this case.

<p>
    <img src="..\..\assets\images\sharing-by-attendee\attendee.png">
</p>

&nbsp;

The second screenshot shows the same Visit in SAP Cloud for Customer after the synchronization is performed by Organizer – Tetiana has taken over the Visit and become its Organizer and Owner.

<p>
    <img src="..\..\assets\images\sharing-by-attendee\organizer.png">
</p>

&nbsp;

!!! note "Note"
    Since SAP Cloud for Customer has a common calendar for all employees, it is not necessary to sync events from all participants individually. It is sufficient to sync event from Organizer or Attendee (Sharing by Attendee feature), so it appears in calendars for all other SAP Cloud for Customer users who are attendees
    
&nbsp;

&nbsp;