---
description: Detailed explanation of how RG Email Sidebar establishes interaction with MS Exchange via a dedicated Apex class
---
# MS Exchange Integration via Apex Class  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>
&nbsp;

*3 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

Besides [custom API endpoints](../Lightning-Scheduler-API/), {{ product_name }} can establish interaction with MS Exchange via a dedicated Apex class.

### MS Exchange calendar actions performed using Apex class methods

- Read, Create, Delete calendar items on MS Exchange servers. This also includes: attendees availability spans parsing from their calendars; adding a booked meeting into attendees' calendars; reserving chosen time slots  
- Checking if the above listed actions were performed successfully; troubleshooting possible errors, e.g. Exchange data access issues  

&nbsp;

&nbsp;

**Special notes:**

All date and time properties in the calls and responses are set in the [ISO 8601 standard](https://en.wikipedia.org/wiki/ISO_8601): **YYYY-MM-DDThh:mm:ssZ**

All input and output dates and times are set in GMT time zone.

&nbsp;

&nbsp;

### Access authorization token

Access authorization required to work with MS Exchange data is granted using an *access_token* acquired by [{{ company_name }} Sync Engine](../Synchronization-Engine-An-Overview/).

&nbsp;

&nbsp;



### Apex Class Methods (Revised)

&nbsp;

#### Method getTimeSlotsFromOutlook

Use this method to retrieve an access URL value required to perform actions on calendars.

Method use sample:

*Parameters*  

- **startDateTime** start of availability dates/time span defining the period during which a meeting is possible, e.g. *2020-10-15T00:00:00Z*  
- **endDateTime** end of availability dates/time span defining the period during which a meeting is possible, e.g. *2020-10-17T12:00:00Z*  
- **emailsToCheckAvailability** the list of email addresses whose calendar availability you want to retrieve. They should belong to your MS Exchange Org. Example:  
   List<String> emailsToCheckAvailability = new list<String> { 'colleague1@mycompany.com' , 'colleague2@mycompany.com' }   
- **accessToken** the *access_token* string acquired by {{ short_name }} Sync Engine to access MS Exchange data  
- **tenant** Sync URL specific to the tenant allocated for your Organization, e.g. *https://lsa-staging-sync.revenuegrid.com*




````

global static void getTimeSlotsFromOutlook(Datetime startDateTime, Datetime endDateTime, List<String> emailsToCheckAvailability, String accessToken, String tenant)
{
HttpResponse resp = request
(
getUrl(startDateTime, endDateTime, tenant),
'POST',
getAuthHeader(accessToken),
getBodyAvailability(emailsToCheckAvailability),
'getTimeSlots',
null,
'SM001_getTimeSlotsMock'
);
System.debug('resp.getBody()' + resp.getBody());
}
````


&nbsp;

* * *

&nbsp;



#### Method createOutlookEvent

Use this method to create calendar items in MS Exchange.

Method use sample:

*Parameters*    

- **accessToken** the *access_token* string acquired by {{ short_name }} Sync Engine to access MS Exchange data  **URL** the URL string retrieved by the getUrl method  
- **tenant** Sync URL specific to the tenant allocated for your Organization, e.g. *https://lsa-staging-sync.revenuegrid.com*
- **eventToCreate** meeting's properties in JSON format. See the dedicated section of this article for details



````
global static void createOutlookEvent(Event eventToCreate, String accessToken, String tenant)
{
try
{
HttpResponse resp = request
(
getUrlMeeting(tenant),
'POST',
getAuthHeader(accessToken),
getBody(eventToCreate, 'CREATE'),
'meeting',
null,
'SM001_getTimeSlotsMock'
);
}catch(Exception e)
{
system.debug('Error: '+e.getMessage()+' '+e.getStackTraceString());
}
}
````
&nbsp;

* * *

&nbsp;

#### Method deleteOutlookEvent


Use this method to delete calendar items in MS Exchange.

Method use sample:

*Parameters*   

- **accessToken** the *access_token* string acquired by {{ short_name }} Sync Engine to access MS Exchange data  **URL** the URL string retrieved by the getUrl method   
- **eventToDelete** meeting's properties in JSON format. See the dedicated section of this article for details
- **tenant** Sync URL specific to the tenant allocated for your Organization, e.g. *https://lsa-staging-sync.revenuegrid.com*



````
global static void deleteOutlookEvent(Event eventToDelete, String accessToken, String tenant)
{
try
{
HttpResponse resp = request
(
getUrlMeeting(tenant),
'DELETE',
getAuthHeader(accessToken),
getBody(eventToDelete, 'DELETE'),
'meeting',
null,
'SM001_getTimeSlotsMock'
);
}catch(Exception e)
{
system.debug('Error: '+e.getMessage()+' '+e.getStackTraceString());
}
}
````

&nbsp;

* * *

&nbsp;

#### Meeting parameters in JSON format

**id** stands for the unique Item ID in the system. Same Id should be used consistently for the same calendar item.  
**isRequired** is a true or false value that defines if an attendee is optional or required  
**salesforceCorrelationId** an extra technical parameter which is generated by Salesforce, it may be used for troubleshooting purposes

##### **Create item**

````
{
"id":"18p09032002jmvP11",
"organizerEmail":"jadatran@contoso.com",
"body":"Agenda: 1, 2, 3",
"subject":"project progress update 2",
"location":"Meeting Room 1",
"startTime":"2022-02-04T01:00:00.000Z",
"endTime":"2022-02-04T02:00:00.000Z",
"salesforceCorrelationId":"16bf7d3b-2055-4f70-bнfd-b0061a38ad1f",
"attendees":[
{
"email":"jadatran@contoso.com",
"isRequired":"true"
}
]
}

````

&nbsp;

&nbsp;

##### **Delete item**

````
{
"id":"08p09103202jmvP11",
"organizerEmail":"jadatran@contoso.com",
"attendees":[
"jadatran@contoso.com"
]
}

````





&nbsp;
&nbsp;

