---
description: Overview of Revenue Grid scheduler API endpoints
---
# {{ company_name }} Scheduler API Endpoints  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*10 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

{{ product_name }} includes a set of special API endpoints to enable various apps and services to take an advantage of its meeting scheduling capabilities. Provided endpoints are intended for meeting scheduling scenarios:

- Parse own and colleagues’ actual calendar availability data from their MS Outlook calendars   
- Easily perform meetings scheduling in MS Outlook and Salesforce calendars by the means of API calls and update scheduled meetings  

&nbsp;

## Overview

Scheduler API is designed for server-to-server integrations and can perform meeting scheduling/data retrieval across all users in a customer's organization. Any Meeting Organizer referenced by this API should be a valid Revenue Inbox user with [properly configured Office 365 or MS Exchange connectivity](../Authorizing-Sync-Engine-to-Work-with-Your-Data/). The feature is compatible with MS Graph and allows [MS Teams integration](../Sharing-Calendar-Availability-%28Adaptive-view%29/#ms_teams_integration_on_location_selection) through it. It is scalable to accommodate customer-specified volumes of API calls.  
For internal (in-org) users, the API can be used to schedule meetings on users' behalf or retrieve their calendar availability spans.  
External (out of org) contacts may only be referenced as attendees for the meetings scheduled over this API.  

&nbsp;

### API Authorization

Scheduler API supports 3 authorization methods:  

  - (Legacy approach, disabled by default) Via Administrator user login/password  
  - (Recommended) [OAuth 2.0 Refresh token](https://datatracker.ietf.org/doc/html/rfc6749#section-1.5) flow  
  - (Single tenant deployments <u>only</u>) [HMAC](https://en.wikipedia.org/wiki/HMAC) custom authentication  


&nbsp;

All date and time properties in the requests and responses are set in the [ISO 8601 standard](https://en.wikipedia.org/wiki/ISO_8601): **YYYY-MM-DDThh:mm:ssZ**

All input and output dates and times are set in GMT time zone.

&nbsp;

&nbsp;

## {{ short_company_name }} Scheduler API Endpoints

&nbsp;

### Endpoint 1: Schedule a Meeting in Outlook Calendar

This API allows the caller to create meetings on behalf of a certain internal organizer and invite one or multiple internal (in-org) or external attendees. The meeting invite will be sent out to all listed attendees; the requested slot will be reserved as *Busy* for all participants. 

The attendees may accept, decline, or forward a meeting invite to additional attendees. These details can later be read over the [meeting data retrieval API (Endpoint 4)](../Scheduler-API-Endpoints/#endpoint_4_retrieve_previously_created_meetings_details_from_outlook_calendar).

&nbsp;

**API request parameters**  

*Note:* All parameters except those marked as (optional) are required  

- **TENANT_URL** URL of {{ company_name }} Tenant allocated for your organization  

- **id** a non-void alphanumerical value, unique ID of the Meeting in your system. {{ company_name }} accepts any identifier here and requires passing of the same identifier to API for any further modifications of the meeting  

- **organizerEmail** email address of Meeting Organizer  

- **attendees** the list of Meeting attendee entries:  

    - **email** attendees' email addresses  

    - **isRequired** defines if an attendee is required or optional: true or false  


- **body** Body (description) of the Meeting, in plain text format  

- **subject** Meeting's subject  

- **startTime** start date/time of the Meeting in supported format *YYYY-MM-ddThh:mm:ssZ*  

- **endTime** end date/time of the Meeting in supported format *YYYY-MM-ddThh:mm:ssZ*

- **location** location of the Meeting; may include a Zoom or WebEx meeting URL or a room name

*Note:* for Office 365 users with [MS Graph connectivity](../MS-Graph/), you may set the location "MS Teams" to [set up a meeting in MS Teams](../Sharing-Calendar-Availability-%28Adaptive-view%29/#ms_teams_integration_on_location_selection); room link will be auto-generated and appended to meeting Body  



- **salesforceCorrelationId** (optional) used for telemetry correlation; specify a request ID for end-to-end telemetry tracking 

&nbsp;

#### **Sample request**

````
POST {TENANT_URL}/api/salesforce/scheduler/meeting
Body:
{
    "id": "f9b58255-8e2e-81e2-a6db-27461fa3f11e",
    "organizerEmail": "organizer@contoso.com",
    "body": "meeting description",
    "subject": "meeting subject",
    "location": "meeting room 1",
    "startTime": "2020-10-16T10:00:00Z",
    "endTime": "2020-10-20T23:00:00Z",
    "salesforceCorrelationId": "ac7b40b4-2c33-723b-8aaie-8bpf077z7539",
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
````

&nbsp;

#### **Sample response**

````
{
    "email": "organizer@contoso.com",
    "errorCode": "NoError"
}
````
&nbsp;

* * *

&nbsp;

### Endpoint 2: Update a previously created Meeting in Outlook calendar


This API allows updating a meeting previously created over Scheduler API by changing the date, time, meeting attendees list, or other meeting properties.

&nbsp;

*Special notes:*  

- All parameters except those marked as (optional) are required

- The ‘*organizerEmail*’ parameter cannot be changed later. If you need to modify it: delete the meeting for the original organizer and re-schedule it for another organizer 

- Include in the request <u>only</u> those meeting properties you want to change. Omitted properties will keep their original values

- Making any changes to a meeting results in update notifications being auto-sent to all attendees. After getting such updates, the attendees will be able to accept or decline the meeting afresh   

&nbsp;

**API request parameters**

- **TENANT_URL** URL of {{ company_name }} Tenant allocated for your organization

- **id** a non-void alphanumerical value. Unique ID of the Meeting in your system, consistent with one used for the Schedule a Meeting call 

- **organizerEmail** email address of Meeting Organizer

- **attendees** (optional) list of Meeting attendee entries:  

- **email** attendees' email addresses  
    - **isRequired** defines if an attendee is required or optional: true or false  

    - **body** (optional) Body (description) of the Meeting, in plain text format  

*Note*: Modifying Body of an existing meeting that was sent as an MS Teams invitation may override the meeting link appended to the Body  

- **subject** (optional) Meeting's subject

- **startTime** (optional) start date/time of the Meeting in supported format *YYYY-MM-ddThh:mm:ssZ*

- **endTime** (optional) end date/time of the Meeting in supported format *YYYY-MM-ddThh:mm:ssZ*

- **location** (optional) location of the Meeting; may include a Zoom or WebEx meeting URL or a room name

*Note:* for Office 365 users with [MS Graph connectivity](../MS-Graph/), you may set the location "MS Teams" to [set up a meeting in MS Teams](../Sharing-Calendar-Availability-%28Adaptive-view%29/#ms_teams_integration_on_location_selection); room link will be auto-generated and appended to meeting Body

- **salesforceCorrelationId** (optional) used for telemetry correlation; specify a request ID for end-to-end telemetry tracking 

&nbsp;

#### **Sample request**

(includes meeting Subject modifying and adding an extra attendee, other properties were left unchanged) 

````
PATCH {TENANT_URL}/api/salesforce/scheduler/meeting
Body:
{
  "id": "f9b58255-8e2e-81e2-a6db-27461fa3f11e",
  "organizerEmail": "organizer@contoso.com",
  "subject": "New subject",
  "salesforceCorrelationId": "ac7b40b4-2c33-723b-8aaie-8bpf077z7539",
  "attendees": [
      {
          "email": "attendee1@contoso.com",
          "isRequired": "true",
      },
      {
          "email": "attendee2@contoso.com",
          "isRequired": "false",
      },
      {
          "email": "attendee3@contoso.com",
          "isRequired": "true",
      }
  ]
}

````
&nbsp;

#### **Sample response**

````
{
    "email": "organizer@contoso.com",
    "errorCode": "NoError"
}
````
&nbsp;

* * *

&nbsp;

### Endpoint 3: Delete a Meeting from Outlook calendar

This API allows deleting meetings previously created over Scheduler API.

&nbsp;

**API request parameters ** 

- **TENANT_URL** URL of {{ company_name }} Tenant allocated for your organization  

- **id** a non-void alphanumerical value. Unique ID of the Meeting in your system, consistent with one used for the Schedule a Meeting call

- **organizerEmail** email address of Meeting Organizer

- **salesforceCorrelationId** (optional) telemetry correlation, specify a request ID for end-to-end telemetry tracking

&nbsp;

#### **Sample request**

````
DELETE {TENANT_URL}/api/salesforce/scheduler/meeting
Body:
{
  "id": "f9b54553-8e2a-47r2-a6db-27425fb3f11e",
  "organizerEmail": "organizer@contoso.com",
  "salesforceCorrelationId": "1234567—9012-3456-789012345678"
}
````

&nbsp;

#### **Sample response**

````
{
  "email": "organizer@contoso.com",
  "errorCode": "NoError"
}
````



&nbsp;

* * *

&nbsp;

### Endpoint 4: Retrieve previously created Meeting's details from Outlook Calendar

This API allows retrieving meeting details for meetings previously created over Scheduler API, including registered attendee reactions to the Meeting invite: *No response*, *Accepted*, *Declined*.

&nbsp;

**GET string parameters**

*Note:*  All parameters except those marked as (optional) are required

- **TENANT_URL** URL of {{ company_name }} Tenant allocated for your organization  

- **id** a non-void alphanumerical value. Unique ID of the Meeting in your system, consistent with one used for the Schedule a Meeting call  

- **organizerEmail** email address of Meeting Organizer  

- **salesforceCorrelationId** (optional) telemetry correlation added at the end of the query string, specify a request ID for end-to-end telemetry tracking  

&nbsp;

#### **Sample request**

```
GET {TENANT_URL}/api/salesforce/scheduler/meeting?id=f9b58255-8e2e-81e2-a6db-27461fa3f11e&organizerEmail=organizer@contoso.com&salesforceCorrelationId=ac7b40b4-2c33-723b-8aaie-8bpf077z7539
```

&nbsp;

**API response parameters**

The API response includes the following data retrieved for Meeting attendees.

- **id** a non-void alphanumerical value. Unique ID of the Meeting in your system, consistent with one used for the Schedule a Meeting call 

- **organizerEmail** email address of Meeting Organizer

- **attendees** list of Meeting attendee entries:  

    - **email** attendees' email addresses  

    - **isRequired** defines if an attendee is required or optional: true or false  

    - **response** each attendee's reaction to the invite: “*NoResponseReceived*”, “*Accepted*”, “*Declined*”, “*Tentative*”, “*Organizer*”, or “*Unknown*”  


- **body** Body (description) of the Meeting, in plain text format

- **subject** Meeting's subject

- **startTime** start date/time of the Meeting in supported format *YYYY-MM-ddThh:mm:ssZ*

- **endTime** end date/time of the Meeting in supported format *YYYY-MM-ddThh:mm:ssZ*

- **location** location of the Meeting; may include a Zoom or WebEx meeting URL or a room name

&nbsp;

#### **Sample response: Success**

````
{
  "id": "f9b58255-8e2e-81e2-a6db-27461fa3f11e",
  "organizerEmail": "organizer@contoso.com",
  "body": "meeting description",
  "subject": "meeting subject",
  "location": "meeting room 1",
  "startTime": "2020-10-16T10:00:00Z",
  "endTime": "2020-10-20T23:00:00Z",
  "attendees": [
      {
          "email": "attendee1@contoso.com",
          "isRequired": "true",
          "response": "Accept"
      },
      {
          "email": "attendee2@contoso.com",
          "isRequired": "false",
          "response": "Decline"
      }
  ]
}

````

&nbsp;

#### **Sample response: Error**

````
{  
  "email": "organizer@contoso.com",
  "errorCode": "MeetingNotFound"
}


````
&nbsp;

* * *

&nbsp;

### Endpoint 5: Retrieve attendees' calendar availability from Outlook Calendars

This call is used to collect occupied slots data from attendees’ calendars in your MS Exchange Organization. 

**POST query string Parameters**

- **TENANT_URL** URL of {{ company_name }} Tenant allocated for your organization  

- **From** and **To** the date-time span to check for occupied slots added at the end of the query string, e.g. *from=2020-10-15T00:00:00Z&to=2020-10-17T12:00:00Z*  

- **salesforceCorrelationId** (optional) telemetry correlation added at the end of the query string, specify request ID for end-to-end telemetry tracking  

API POST body includes the following property:  

- **email** email addresses of attendees to retrieve occupied slots for.  

*Note:* this API works <u>only</u> for users from the same MS Exchange Organization  

&nbsp;

#### **Sample request**

````
POST {TENANT_URL}/api/salesforce/scheduler/availability?from=2020-10-15T00:00:00Z&to=2020-10-17T12:00:00Z&salesforceCorrelationId=abcdefg
[
    {
     "email": "attendee1@contoso.com"
    },
    {
     "email": "attendee2@contoso.com"
    }
]

````
&nbsp;

#### **Sample response**

Availability API response includes the following data for every attendee listed in the request:  

- **errorCode** indicates an error code for troubleshooting, if an error occurred. NoError is displayed if there were no errors; other error indicators are also self-explanatory  

- **unavaialbleTimeSlots** contains the list of attendee calendars' unavailable slots, each slot is defined by two parameters:  

    - **timeMin** is the date and time of the start of an occupied span in the attendee's calendar in supported format *YYYY-MM-ddThh:mm:ssZ*  

    - **timeMax** is the date and time of the end of an occupied span in the attendee's calendar in supported format *YYYY-MM-ddThh:mm:ssZ*  



````
[
    {
        "email": "attendee1@contoso.com",
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
        "email": "attendee2@contoso.com",
        "errorCode": "NoError",
        "unavailableTimeslots": [
            {
                "timeMin": "2020-10-16T10:00:00Z",
                "timeMax": "2020-10-16T16:00:00Z",
            }
        ]
    }
]

````
&nbsp;

&nbsp;

