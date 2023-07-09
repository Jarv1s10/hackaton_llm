---
description: Learn how to use Revenue Grid API Calls for Salesforce Lightning Scheduler
---
# {{ company_name }} API Calls for Salesforce Lightning Scheduler  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*13 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

Starting with Salesforce Spring 2021 update, customers who use [Salesforce Lightning Scheduler](https://help.salesforce.com/articleView?id=ls_overview.htm&type=5) can do the following via {{ company_name }}'s Lightning Scheduler adapter (LSA):

- parse own and colleagues’ actual calendar availability data from their MS Outlook calendars to be used in [Salesforce Lightning Scheduler](https://help.salesforce.com/articleView?id=ls_overview.htm&type=5)
- easily down-sync to MS Outlook calendar their Salesforce Events created with Scheduling App, this way ensuring that their calendars are always up to date and in sync

!!! tip "Tip"
    Also see [this {{ company_name }} article](https://revenuegrid.com/blog/salesforce-lightning-scheduler/) for more information on using Salesforce Lightning Scheduler

&nbsp;

{{ company_name }} ensures this possibility by establishing interaction between [Salesforce Lightning Scheduler](https://help.salesforce.com/articleView?id=ls_overview.htm&type=5) and the users' Exchange accounts over several API endpoints. This article explains how these API methods and properties work.

!!! tip "Tip"
    Also see this video <https://youtu.be/D6betOrxAwo> to learn in detail how the users work with {{ product_name }} in Salesforce Lightning Scheduler

&nbsp;

### Specific calendar actions performed over API

- Read, Create, Update, Delete calendar items on MS Exchange servers. This also includes: attendees availability spans parsing from their calendars; adding a booked Appointment based on a Lightning Scheduler Event to the attendees' calendars
- Checking if the above listed actions were performed successfully; troubleshooting possible errors, e.g. Exchange data access issues
- Indicating which attendee is the meeting's organizer

&nbsp;

**Prerequisites:**

Slightly different sets of prerequisites are required to perform the call *Read* (retrieve availability) and the calls *Create, Update, Delete.*

For *Read* method the prerequisites are:

- Create a [{{ company_name }} Org](../Managing-Organizations-via-the-Admin-Panel/) which the attendees belong to
- {{ company_name }} *access_token* acquired for a special user, a user belonging to the same {{ short_company_name }} Org with a valid MS Exchange credentials setup
- Other users whose availability is retrieved should belong to the same Exchange Org as the special user

&nbsp;

For *Create, Update, Delete* calls, the prerequisites are as follows:

- Create a [{{ company_name }} Org](../Managing-Organizations-via-the-Admin-Panel/) authorized via a service Impersonation Account which the attendees belong to
- All users whose Lightning Scheduler Events will be down-synced to Outlook should belong to the same [{{ company_name }} Org](../Managing-Organizations-via-the-Admin-Panel/)
- {{ company_name }} *access_token* acquired for a user belonging to the same [{{ short_company_name }} Org](../Managing-Organizations-via-the-Admin-Panel/) that has Organization Admin permissions in the {{ short_company_name }} Org (the *updateOrganization* setting)
- Note that users mailboxes' [email aliases](https://docs.microsoft.com/en-us/microsoft-365/admin/email/add-another-email-alias-for-a-user?view=o365-worldwide) are not supported for these methods: each Salesforce user is matched with a single {{ company_name }} user / email address

&nbsp;

**Special notes:**

All date and time properties in the calls and responses are set in the [ISO 8601 standard](https://en.wikipedia.org/wiki/ISO_8601): **YYYY-MM-DDThh:mm:ssZ**

All input and output dates and times are set in GMT time zone.

&nbsp;

&nbsp;

### Access authorization token

Access authorization required to work with MS Exchange data is granted using an *access_token* acquired by [{{ company_name }} Sync Engine](../Synchronization-Engine-An-Overview/).

&nbsp;



**Salesforce Lightning Scheduler - Exchange downsyncing**

When Events created in Lightning Scheduler get down-synchronized to MS Outlook calendar, due to a technical limitation in MS Exchange {{ company_name }} creates a set of overlapping Appointments instead of a Meeting for every Attendee and the Event's Organizer.

&nbsp;

&nbsp;

### Endpoint 1: attendees' calendar availability retrieval from Outlook calendar (Read)



This call is used to collect available slots data from an attendee's MS Exchange calendar data. It has the following properties:

**Tenant_URL** stands for the URL of {{ short_company_name }} Tenant which the organizer belongs to

**From** and **to** availability dates/time span defining the time period during which a meeting is possible, e.g. *from=2020-10-15T00:00:00Z&to=2020-10-17T12:00:00Z*

**salesforceCorrelationId** is an extra technical property which is acquired by Salesforce Lightning Scheduler, it is used for troubleshooting purposes

&nbsp;

The API Read call's body includes the following properties:

**email** the email addresses of attendees from the same MS Exchange Org. Clauses on different attendees' availability are included as separate clauses in brackets

**serviceResourceId** is a technical property required by the Lightning Scheduler

**isOrganizer** indicates if the attendee is the meeting's Organizer; this additional property is included for future use possibilities

&nbsp;

#### **A sample Read request**

```
POST {TENANT_URL}/api/salesforce/scheduler/availability?from=2020-10-15T00:00:00Z&to=2020-10-17T12:00:00Z&salesforceCorrelationId=abcdefg
Body:
[
    {
        "email": "attendee1@contoso.com",
        "serviceResourceId": "12345",
        "isOrganizer": true
    },
    {
        "email": "attendee2@contoso.com",
        "serviceResourceId": "54321"
    }
]
```

&nbsp;

The API Read response includes the following data retrieved for every attendee listed in the call:

**serviceResourceId** is a technical property required by the Lightning Scheduler  

**errorCode** indicates an error code for troubleshooting, if an error occurred. *NoError* is displayed if there were no errors; other error indicators are also self-explanatory  

**unavaialbleTimeSlots** is the retrieved data on the occupied slots in the attendee's calendar over the period specified in the call, in supported format YYYY-MM-ddThh:mm:ssZ. Data on different occupied slots is listed as separate clauses in brackets  

**TimeMin** is the date and time of the start of an occupied span in the attendee's calendar in supported format YYYY-MM-ddThh:mm:ssZ  

**TimeMax** is the date and time of the end of an occupied span in the attendee's calendar in supported format YYYY-MM-ddThh:mm:ssZ  



#### **A sample Read response**

```
[
    {
        "serviceResourceId": "12345",
        "errorCode": "NoError",
        "unavailableTimeslots": [
            {
                "timeMin": "2020-10-16T10:00:00Z",
                "timeMax": "2020-10-16T12:00:00Z",
            },
            {
                "timeMin": "2020-10-16T14:00:00Z",
                "timeMax": "2020-10-16T15:00:00Z",
            },
        ]
    },
    {
        "serviceResourceId": "54321",
        "errorCode": "NoError",
        "unavailableTimeslots": [
            {
                "timeMin": "2020-10-16T10:00:00Z",
                "timeMax": "2020-10-16T16:00:00Z",
            }
        ]
    },
]
```



&nbsp;

* * *

&nbsp;

### Endpoint 2: saving a Lightning Scheduler Event as an Appointment in Outlook calendar (Create)



This call is used to create (down-sync) an Appointment in MS Exchange based on a Lightning Scheduler Event. It has the following properties:

**Tenant_URL** stands for the URL of {{ short_company_name }} Tenant which the organizer belongs to



API call's body includes the following properties:

**id** alphanumerical value, unique ID of the Lightning Scheduler Event that a matching Outlook Appointment should be created for

**organizerEmail** email address of the Event's Organizer

**body** body (description) of the Appointment to be created

**subject** subject of the Appointment to be created

**location** location of the Appointment to be created

**startTime** start date/time of the Appointment to be created in supported format YYYY-MM-ddThh:mm:ssZ

**endTime** end date/time of the Appointment to be created in supported format YYYY-MM-ddThh:mm:ssZ

**salesforceCorrelationId** is an extra technical property which is acquired by Salesforce Lightning Scheduler, it is used for troubleshooting purposes



**attendees** list of attendees of the Appointment to be created

**email** email addresses of the attendees from the same MS Exchange Org. Clauses on different attendees are included as separate clauses in brackets.

**isRequired** defines if an attendee is required or optional: true or false

&nbsp;

#### **A sample Create request**

```
POST {TENANT_URL}/api/salesforce/scheduler/postback
Body:
{
    "id": "abcde-fghij-klmno-pqrst-uvwxyzfb3f11e",
    "organizerEmail": "test@contoso.com",
    "body": "meeting description",
    "subject": "meeting subject",
    "location": "meeting room 1",
    "startTime": "2020-10-16T10:00:00Z",
    "endTime": "2020-10-20T23:00:00Z",
    "salesforceCorrelationId": "ac3b40b4-2c33-463b-8bfe-8bcf077d7539",
    "attendees": [
        {
            "email": "attendee1@contoso.com",
            "isRequired": "true",
        },
        {
            "email": "attendee2@contoso.com",
            "isRequired": "false",
        }
    ]
}
```

&nbsp;



The API Create response includes the following data retrieved for every attendee included in the call:

**email** is the email addresses of attendees. Responses on different attendees' availability are included as separate clauses in brackets

**errorCode** indicates an error code  for troubleshooting, if an error occurred. *NoError* is displayed if there were no errors; other error indicators are also self-explanatory

&nbsp;

#### **A sample Create response**

```
[
    {
        "email": "test@contoso.com",
        "errorCode": "NoError"
    },
    {
        "email": "attendee1@contoso.com",
        "errorCode": "ErrorMailRecipientNotFound"
    },
    {
        "email": "attendee2@contoso.com",
        "errorCode": "NoError"
    }
]
```

&nbsp;

* * *

&nbsp;

### Endpoint 3: updating an Appointment in Outlook calendar (Update / Modify)



**Tenant_URL** stands for the URL of {{ short_company_name }} Tenant which the organizer belongs to



API call's body includes the following properties:

**original** fields of the item before updating / modifying

**id** alphanumerical value, unique ID of the Lightning Scheduler Event whose matching Appointment should be updated / modified

**organizerEmail** email address of the Event's Organizer

**body** body (description) of the Appointment to be updated / modified

**subject** subject of the Appointment to be updated / modified

**location** location of the Appointment to be updated / modified

**startTime** start date/time of the Appointment to be updated / modified, in supported format YYYY-MM-ddThh:mm:ssZ

**endTime** end date/time of the Appointment to to be updated / modified, in supported format YYYY-MM-ddThh:mm:ssZ



**attendees** list of attendees of the Appointment to be updated / modified:

**email** the email addresses of attendees from the same MS Exchange Org. Clauses on different attendees are included as separate clauses in brackets

**isRequired** defines if an attendee is required or optional: true or false


&nbsp;


**new** updated fields of the item

*Note:* only the updated **new** values differ from the **original** values, but the call's syntax requires including the unchanged values as well

**organizerEmail** email address of the Event's Organizer

**body** (description) updated body of the Appointment

**subject** updated subject of the Appointment to be updated / modified

**location** updated location of the Appointment to be updated / modified

**startTime** updated start date/time of the Appointment to be updated / modified, in supported format YYYY-MM-ddThh:mm:ssZ

**endTime** updated end date/time of the Appointment to to be updated / modified, in supported format YYYY-MM-ddThh:mm:ssZ



**attendees** updated list of attendees of the Appointment:

**email** the email addresses of attendees from the same MS Exchange Org. Clauses on different attendees are included as separate clauses in brackets

**isRequired** defines if an attendee is required or optional: true or false


**salesforceCorrelationId** is an extra technical property which is acquired by Salesforce Lightning Scheduler, it is used for troubleshooting purposes

&nbsp;

#### **A sample Update request**



```
PUT {TENANT_URL}/api/salesforce/scheduler/postback
Body:
{
    "original": {
        "id": "abcde-fghij-klmno-pqrst-uvwxyzfb3f11e",
        "organizerEmail": "test@contoso.com",
        "body": "meeting description",
        "subject": "meeting subject",
        "location": "meeting room 1",
        "startTime": "2020-10-16T10:00:00Z",
        "endTime": "2020-10-20T23:00:00Z",
        "attendees": [
            {
                "email": "attendee1@contoso.com",
                "isRequired": "true",
            },
            {
                "email": "attendee2@contoso.com",
                "isRequired": "false",
            }
        ]
    },
    "new": {
        "organizerEmail": "test@contoso.com",
        "body": "meeting description",
        "subject": "meeting subject",
        "location": "meeting room 1",
        "startTime": "2020-10-16T10:00:00Z",
        "endTime": "2020-10-20T23:00:00Z",
        "attendees": [
            {
                "email": "attendee1@contoso.com",
                "isRequired": "true",
            },
            {
                "email": "attendee2@contoso.com",
                "isRequired": "false",
            }
        ]
    }
    "salesforceCorrelationId": "ac3b40b4-2c33-463b-8bfe-8bcf077d7539"
}
```


The API Update response includes the following data retrieved for every attendee included in the call:

**email** is the email addresses of attendees. Response on different attendees are included as separate clauses in brackets

**errorCode** indicates an error code for troubleshooting, if an error occurred. *NoError* is displayed if there were no errors; other error indicators are also self-explanatory

&nbsp;

#### **A sample Update response**

```
[
    {
        "email": "test@contoso.com",
        "errorCode": "NoError"
    },
    {
        "email": "attendee1@contoso.com",
        "errorCode": "NoError"
    },
    {
        "email": "attendee2@contoso.com",
        "errorCode": "ErrorMailRecipientNotFound"
    }
]
```

&nbsp;

* * *

&nbsp;

### Endpoint 4: deleting an Appointment from Outlook calendar (Delete)



**Tenant_URL** stands for the URL of {{ short_company_name }} Tenant which the organizer belongs to

**id** alphanumerical value, unique ID of the Lightning Scheduler Event whose matching Appointment should be deleted

**organizerEmail** email address of the Event's Organizer

**attendees** list of the attendees of the item to be deleted; their emails are listed in quotation marks, no separate clauses required

&nbsp;

#### **A sample Delete request**

```
DELETE {TENANT_URL}/api/salesforce/scheduler/postback
Body:
{
    "id": "abcde-fghij-klmno-pqrst-uvwxyzfb3f11e",
    "organizerEmail": "organizer@contoso.com",
    "attendees": [
        "attendee1@contoso.com",
        "attendee2@contoso.com"
    ]
}
```



The API Delete response includes the following data retrieved for every attendee included in the call:

**email** is email addresses of the attendees. Responses on different attendees included as separate clauses in brackets

**errorCode** indicates an error code for troubleshooting, if an error occurred. *NoError* is displayed if there were no errors; other error indicators are also self-explanatory

&nbsp;

#### **A sample Delete response**

```
[
    {
        "email": "organizer@contoso.com",
        "errorCode": "NoError"
    },
    {
        "email": "attendee1@contoso.com",
        "errorCode": "NoError"
    },
    {
        "email": "attendee2@contoso.com",
        "errorCode": "ErrorMailRecipientNotFound"
    }
]
```


&nbsp;

&nbsp;

