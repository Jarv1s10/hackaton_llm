# How SSI Synchronization Filter and Auto-Sync Feature Works for Appointments and Visits

&nbsp;

&nbsp;

## The "sliding date period" filter and auto-sync feature

SAP Cloud for Customer Server-Side Integration continuously synchronizes user's calendar items in SAP Cloud for Customer and e-mail client calendars. To improve the synchronization performance, SSI Sync filters old calendar items according to a "sliding date period" that avoids syncing large amounts of irrelevant past events data.

&nbsp;

The "sliding date period" filter allows SSI Sync to keep Appointments and Visits in a synchronization scope that were held **30 days ago and later** (closer to the current date). At the same time, this filter has no limits for future calendar events. Once the event (Appointment / Visit) is out of the synchronization scope, it will be unsynchronized according to the pattern described in [this article](../canceling-deleting-calendar-items/), see the "*Out of Filter*" column. Therefore, the "sliding date period" ensures that all relevant events are kept in sync in both user’s SAP Cloud for Customer and e-mail client calendars.

&nbsp;

Also, the auto-sync meetings feature allows SSI Sync to automatically capture and synchronize MS Outlook events that go **14 days in the past** and **60 days in the future** to SAP Cloud for Customer. Then, they will be in a synchronization scope until they stay within the "sliding date period" described above.

&nbsp;

* * *

&nbsp;

## Processing events not matching filter criteria

When SAP Cloud for Customer Visits and Appointments become too old to match the "sliding date period" filter criteria, SSI Sync will process in the following ways:

* If SAP Cloud for Customer Visit or Appointment ("meeting" in Exchange) has attendees – the event will remain in Exchange (Google) calendar, and the custom SAP category will be cleared out

* If SAP Cloud for Customer Visit or Appointment ("appointment" in Exchange) has no attendees – the event will be deleted from Exchange (Google) calendar

* If Visit or Appointment originated in an e-mail client calendar has no attendees – the event will remain in Exchange (Google) calendar, and the custom SAP category will be cleared out

!!! tip "Tip"
    If you want an appointment with attendees to be **deleted** from the Exchange calendar, the Global Setting *ServiceEventDeletionStrategy* should be set to "0". Also, the appointment itself should be originated in SAP Cloud for Customer

&nbsp;

&nbsp;