# How do the Cancelation and Deletion of Appointments and Visits Work

&nbsp;

&nbsp;

**[ This article is work-in-progress ]**

&nbsp;

&nbsp;

Canceling or deleting Appointments and Visits in SAP Cloud for Customer or MS Exchange results in different outcomes for the calendar items in the opposite side. For example, an action of canceling/deleting an appointment in SAP Cloud for Customer causes an end result for its appointment in MS Outlook (the opposite storage).

!!! note "Note"
    There is **no difference** between Cancel or Delete actions for the SSI. Both of them bring the same result in terms of the SSI synchronization
    

&nbsp;

## Calendar items canceling / deletion patterns

The table below summarizes the outcomes of different user actions on specific kinds of calendar items enforced by SSI synchronization.

&nbsp;

<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <p />
            </th>
            <th>
                <p>Delete/Cancel on SAP Cloud for Customer</p>
            </th>
            <th>
                <p>Cancel on Microsoft Exchange</p>
            </th>
            <th>
                <p>Out of filters</p>
            </th>
        </tr>
        <tr>
            <td>
                <p>Appointment/Visit (no attendees) created in MS Exchange</p>
            </td>
            <td>
                <p>Category is cleared on MS Exchange (event becomes unsynchronized)</p>
            </td>
            <td>
                <p>Event is Canceled/Deleted in SAP Cloud for Customer</p>
            </td>
            <td>
                <p>Category is cleared on MS Exchange (event becomes unsynchronized)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Appointment/Visit (no attendees) created in SAP Cloud for Customer</p>
            </td>
            <td>
                <p>Event is deleted in MS Exchange</p>
            </td>
            <td>
                <p>Event is Canceled/Deleted in SAP Cloud for Customer</p>
            </td>
            <td>
                <p>Event is deleted in MS Exchange</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Appointment/Visit (with attendees) for an <strong>Owner/Organizer</strong></p>
            </td>
            <td>
                <p>Category is cleared on MS Exchange (event becomes unsynchronized)</p>
                <p>Organizer must cancel it from MS Exchange side if needed</p>
            </td>
            <td>
                <p>Event is Canceled/Deleted in SAP Cloud for Customer</p>
            </td>
            <td>
                <p>Category is cleared on MS Exchange (event becomes unsynchronized)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Appointment/Visit (with attendees) for an <b>Attendee</b></p>
            </td>
            <td>
                <p>Category is cleared on MS Exchange (event becomes unsynchronized)</p>
                <p>Attendee must decline it from MS Exchange side if needed</p>
            </td>
            <td>
                <p>Event is Canceled/Deleted in SAP Cloud for Customer</p>
            </td>
            <td>
                <p>Category is cleared on MS Exchange (event becomes unsynchronized)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Appointment/Visit (with attendees) if <b>Owner/Organizer</b> changed for <b>Owner/Organizer</b></p>
                <p>(Changed in SAP Cloud for Customer)</p>
            </td>
            <td>
                <p>Category is cleared on MS Exchange (event becomes unsynchronized)</p>
            </td>
            <td>
                <p>&ndash;</p>
            </td>
            <td>
                <p>&ndash;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Appointment/Visit (with attendees) if <b>Owner/Organizer</b> changed for <b>Attendee</b></p>
                <p>(Changed in SAP Cloud for Customer)</p>
            </td>
            <td>
                <p>Category is cleared on MS Exchange (event becomes unsynchronized)</p>
            </td>
            <td>
                <p>&ndash;</p>
            </td>
            <td>
                <p>&ndash;</p>
            </td>
        </tr>
    </tbody>
</table>

&nbsp;

* * * 

&nbsp;

## Cancel or Delete feature on SAP Cloud for Customer

As Appointments and Visits in SAP Cloud for Customer can be either Canceled or Deleted, the user can customize what the action SSI sync should take.

This feature allows choosing whether Delete or Cancel an Appointment/Visit in SAP Cloud for Customer if it is canceled in MS Exchange.

&nbsp;

To customize the feature:

1. Go to **E-Mail Integration** (1) > **Groupware Settings** (2) > **Settings** tab (3) in SAP Cloud for Customer

2. Find the **Cancel Appointments/Visits in CRM instead of deletion** setting under **Calendar Configuration**

    * **Enable** feature to **cancel** Appointments/Visits in CRM
    
    * **Disable** feature to **delete** Appointments/Visits in CRM

<p>
<img src= "..\..\assets\images\cancel-delete-calendar-items\1.png">
</p>

<!--  -->

&nbsp;

&nbsp;


