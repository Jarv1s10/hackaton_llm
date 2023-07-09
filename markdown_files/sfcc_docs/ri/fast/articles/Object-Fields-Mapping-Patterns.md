---
description: Detailed explanation of fields mapping (MS Exchange or Gmail ↔ Salesforce)
---
# Item Fields Mapping Explained (MS Exchange or Gmail ↔ Salesforce)  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*3 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! tip "Tip"
    To ensure that {{ product_name }} can function with full efficiency, ask your local Salesforce Admin to [install the {{ company_name }} managed package](../Admin-Managed-Package/) in your Org; the package adds a [set of service extra fields](../Admin-Managed-Package/#specific_fields_classes_and_components_the_invisible_suite_package_adds_to_your_salesforce_configuration) to several Salesforce object types

&nbsp;

{{ product_name }} for Salesforce functioning is based on [syncing](../Synchronization-Engine-An-Overview/) and [directly updating](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#1_saving_an_email_when_smartcloud_connect_synchronization_is_active) the contents of matching fields between MS Exchange and Salesforce objects. This article explains typical field matching patterns applied by {{ product_name }} for standard Salesforce objects.

* MS Exchange Emails are matched with Salesforce [Task](https://help.salesforce.com/articleView?id=task_fields.htm&type=5) or [Email Message](https://help.salesforce.com/articleView?id=000239922&type=1) objects, depending on your org's [Salesforce configuration](https://help.salesforce.com/articleView?id=emailadmin_enhanced_email_considerations.htm&type=5)
* MS Exchange [Meetings/Appointments/Events](https://support.office.com/en-us/article/introduction-to-the-outlook-calendar-d94c5203-77c7-48ec-90a5-2e2bc10bd6f8) are [matched](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/) with Salesforce [Event](https://help.salesforce.com/articleView?id=events_and_calendars.htm&type=5) objects
* MS Exchange [Tasks](https://support.office.com/en-us/article/create-tasks-and-to-do-items-45a94e7b-a4ee-46ea-9823-c3423c0eab8e) are matched with Salesforce [Task](https://help.salesforce.com/articleView?id=task_fields.htm&type=5) objects
* MS Exchange [Contacts](https://docs.microsoft.com/en-us/exchange/recipients-in-exchange-online/manage-mail-contacts) are matched with Salesforce [Contact](https://help.salesforce.com/articleView?id=contacts_overview.htm&type=5) objects

!!! note "Note"
    Note that in [certain custom configurations](../Special-Sync-Options-Save-Events-As-Other-&-One-Way-Sync/#syncing_calendar_events_as_custom_or_standard_salesforce_objects_eg_tasks) Tasks or other Salesforce objects may also by matched with MS Exchange calendar items; in these cases field mapping patterns will be set differently

&nbsp;

&nbsp;

#### **[MS Outlook emails](https://docs.microsoft.com/en-us/dotnet/api/microsoft.exchange.webservices.data.emailmessage?view=exchange-ews-api): MS Exchange → Salesforce [saving](../Special-Sync-Options-Save-Events-As-Other-&-One-Way-Sync/#one-way_synchronization) **

<p><img src="../../assets/images/Using-SmartCloud-Connect/How-It-Works/combined.png" class="minimized">
</p>

&nbsp;

| Field or control label or {hidden field} in MS Outlook Desktop / On the Web | MS Exchange / Office 365 field name | Salesforce ([Enhanced Email](https://help.salesforce.com/articleView?id=emailadmin_enhanced_email_considerations.htm&type=5) not enabled), emails saved as Tasks | Salesforce ([Enhanced Email](https://help.salesforce.com/articleView?id=emailadmin_enhanced_email_considerations.htm&type=5) enabled), emails saved as EmailMessages |
| ------------------------------------------------------------ | ----------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| "Subject" line                                               | Subject                             | Subject                                                      | Subject                                                      |
| "Body" box                                                   | Body                                | Comments                                                     | Description                                                  |
| {Sent time/date}                                             | DateTimeSent                        | Comments                                                     | DateTimeSent                                                 |
| {Received time/date}                                         | DateTimeReceived                    | Comments                                                     | DateTimeReceived                                             |
| "From" line                                                  | From                                | Comments                                                     | FromAddress                                                  |
| "To" line                                                    | ToRecipients                        | Comments                                                     | ToAddress                                                    |
| "CC" line                                                    | CcRecipients                        | Comments                                                     | CcAddress                                                    |
| "BCC" line                                                   | BccRecipients                       | Comments                                                     | BccAddress                                                   |
| {Inbox/Sent folder placement}                                | IsReceived                          | IsInbound                                                    | IsReceived                                                   |
| {the "has # attachments" indicator}                          | Attachments                         | n/a                                                          | HasAttachments (does not reflect the actual state)           |
| {[the "normal, personal, private, confidential" flag](https://support.office.com/en-us/article/mark-your-email-as-normal-personal-private-or-confidential-4a76d05b-6c29-4a0d-9096-71784a6b12c1)} | Sensitivity                         | IsPrivate                                                    | IsPrivate                                                    |
| {Message-ID GUID}                                            | IntenetMessageId                    | InternetMessageId                                            | GroupwareItemID                                              |
| {[technical details about the message](https://support.office.com/en-ie/article/view-internet-message-headers-cd039382-dc6e-4264-ac74-c048563d212c)} | InternetMessageHeaders              | n/a                                                          | Headers                                                      |
| {[ID of the correspondence thread the email belongs to](https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/conversationid) used for [this feature](../Save-All-Emails-in-a-Thread/)} | ConversationId                      | ConversationId                                               | ConversationId                                               |
| n/a                                                          | n/a                                 | IsCreatedBySync <br />(used to define if the email was saved by [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/)) | IsCreatedBySync <br />(used to define if the email was saved by [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/)) |



&nbsp;

#### **[MS Outlook calendar items](https://docs.microsoft.com/en-us/dotnet/api/microsoft.exchange.webservices.data.calendarevent?view=exchange-ews-api)**

<p><img src="../../assets/images/Using-SmartCloud-Connect/How-It-Works/event_ol.png" class="minimized">
</p>

&nbsp;

| Field or control label or  {hidden field} in MS Outlook Desktop / On the Web | MS Exchange / Office 365 field name | Salesforce Event object                     |
| ------------------------------------------------------------ | --------------------------------- | ------------------------------------------- |
| {item's recurrence flag and related data}                    | Recurrence                        | IsRecurrence2 and ServerSync_RecurrenceData |
| n/a                                                          | MimeContent                       | MimeContent                                 |
| "Subject" line                                               | Subject                           | Subject                                     |
| "Body" box                                                   | Body                              | Description                                 |
| "Location" line                                              | Location                          | Location                                    |
| "All day event" checkbox                                     | IsAllDayEvent                     | IsAllDayEvent                               |
| "Start time" field                                           | Start                             | StartDateTime                               |
| Start timezone field                                         | StartTimeZone                     | StartTimeZone                               |
| "End time" field                                             | End                               | EndDateTime                                 |
| End timezone field                                           | EndTimeZone                       | EndTimeZone                                 |
| "Reminder" time span picklist                                | ReminderMinutesBeforeStart        | ReminderMinutesBeforeStart                  |
| {reminder enabled}                                           | IsReminderset                     | IsReminderSet                               |
| {the date/time of event start}                               | ReminderDueBy                     | ReminderDateTime                            |
| [The "Show as:" picklist (free, working elsewhere, tentative, busy, out of office)](https://support.office.com/en-us/article/add-time-away-from-the-office-to-coworkers-outlook-calendars-69fe38aa-7b5f-4225-8b69-47f47092e65e) | LegacyFreeBusyStatus              | ShowAs                                      |
| {contacts/email addresses added to the meeting as [Required](https://support.office.com/en-us/article/video-create-a-meeting-d811f1df-0459-4b24-b7fb-a3d471ebb66e); the "To" field} | RequiredAttendees                 | ServerSync_NamedRequiredAttendees           |
| {contacts/email addresses added to the meeting as [Optional](https://support.office.com/en-us/article/video-create-a-meeting-d811f1df-0459-4b24-b7fb-a3d471ebb66e); the "CC" field} | OptionalAttendees                 | ServerSync_NamedOptionalAttendees           |
| {contacts/email addresses added to the meeting as [Resources](https://support.office.com/en-us/article/add-bcc-recipients-to-a-meeting-request-fcaff39e-7fcd-4a77-81e9-b609c57dadb1); the "BCC" field} | Resources                         | ServerSync_NamedResources                   |
| {the calendar item Organizer's address}                      | Organizer                         | ServerSync_NamedOrganizer                   |
| {[the item's actual status: none, meeting, received, canceled](https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/appointmentstate)} | AppointmentState                  | ServerSync_IsOrganizer                      |
| {[the indicator if the item is private, personal, confidential](https://support.office.com/en-us/article/mark-your-email-as-normal-personal-private-or-confidential-4a76d05b-6c29-4a0d-9096-71784a6b12c1)} | Sensitivity                       | IsPrivate                                   |



&nbsp;

* * *

&nbsp;

#### **[MS Outlook Tasks](https://docs.microsoft.com/en-us/dotnet/api/microsoft.exchange.webservices.data.task?view=exchange-ews-api)**

| Field or control label or  {hidden field} in MS Outlook Desktop / On the Web | MS Exchange / Office 365 field | Salesforce                                                  |
| ------------------------------------------------------------ | ---------------------------- | ----------------------------------------------------------- |
| "Subject" line                                               | Subject                      | Subject                                                     |
| "Priority" flag                                              | Importance                   | Priority                                                    |
| "Reminder" checkbox                                          | IsReminderSet                | IsReminderSet                                               |
| Reminder's Date field                                        | ReminderDueBy                | ReminderDateTime                                            |
| "Description" box                                            | Body                         | Description                                                 |
| "Description" box                                            | Body                         | [SmartDescription](../Using-the-Smart-Description-Feature/) |
| "Due date" field                                             | DueDate                      | ActivityDate                                                |
| "Status" field                                               | Status                       | Status                                                      |
| "Private" flag                                               | Sensitivity                  | IsPrivate                                                   |



&nbsp;

* * *

&nbsp;

#### **[MS Outlook Contacts](https://docs.microsoft.com/en-us/dotnet/api/microsoft.exchange.webservices.data.contact?view=exchange-ews-api)**

| Field or control label or {hidden field} in MS Outlook Desktop / On the Web | MS Exchange / Office 365 | Salesforce                                  |
| ------------------------------------------------------------ | ---------------------- | ------------------------------------------- |
| {the full Name field}                                        | GivenName              | FirstName                                   |
| {the full Name field}                                        | Surname                | LastName                                    |
| {the full Name field}                                        | MiddleName             | MiddleName                                  |
| {the full Name field}                                        | Salutation             | Salutation                                  |
| {the full Name field}                                        | Generation             | Suffix                                      |
| "Job Title" field                                            | JobTitle               | Title                                       |
| "Company" field                                              | CompanyName            | ServerSync_CompanyName                      |
| "Web Page Address" field                                     | WebPage                | Link to the Contact's profile in Salesforce |
| "E-mail" field                                               | EmailAddresses         | Email                                       |
| "Primary Phone" field                                        | PhoneNumbers           | Phone                                       |
| "Mobile Phone" field                                         | PhoneNumbers           | MobilePhone                                 |
| "Business Phone" field                                       | PhoneNumbers           | BusinessPhoneNumber                         |
| "Business Fax" field                                         | PhoneNumbers           | Fax                                         |
| "Assistant's Phone" field                                    | PhoneNumbers           | AssistantPhone                              |
| "Home Phone" field                                           | PhoneNumbers           | HomePhone                                   |
| "Other Phone" field                                          | PhoneNumbers           | OtherPhone                                  |
| {description box}                                            | Body                   | Description                                 |
| {description box}                                            | Body                   | SmartDescription                            |
| "Assistant" field                                            | AssistantName          | AssistantName                               |
| "Business Street" field                                      | PhysicalAddresses      | MailingStreet                               |
| "Business City" field                                        | PhysicalAddresses      | MailingCity                                 |
| "Business State" field                                       | PhysicalAddresses      | MailingState                                |
| "Business Postal Code" field                                 | PhysicalAddresses      | MailingPostalCode                           |
| "Business Country/Region" field                              | PhysicalAddresses      | MailingCountry                              |
| "Other Street" field                                         | PhysicalAddresses      | OtherStreet                                 |
| "Other City" field                                           | PhysicalAddresses      | OtherCity                                   |
| "Other State" field                                          | PhysicalAddresses      | OtherState                                  |
| "Other Postal Code" field                                    | PhysicalAddresses      | OtherPostalCode                             |
| "Other Country/Region" field                                 | PhysicalAddresses      | OtherCountry                                |
| "Birthday" field                                             | Birthday               | Birthdate                                   |
| "Department" field                                           | Department             | Department                                  |
| "Private" flag                                               | Sensitivity            | IsPrivate                                   |

&nbsp;

* * *

&nbsp;

#### [Google Tasks](https://support.google.com/tasks/answer/7675772?co=GENIE.Platform%3DDesktop&hl=en)

**Task statuses mapping**

| Google Task status | Salesforce Task status |
| ------------------ | ---------------------- |
| needsAction        | Notes                  |
| needsAction        | InProgress             |
| completed          | Completed              |
| needsAction        | WaitingOnOthers        |
| needsAction        | Deferred               |

&nbsp;





| Google Task field | Salesforce Task field  |
| ----------------- | ---------------------- |
| n/a               | Assigned to            |
| n/a               | Recurrence interval    |
| n/a               | Repeat this task       |
| n/a               | Call type              |
| Title             | Subject                |
| n/a               | Call object identifier |
| n/a               | Call result            |
| n/a               | Task subtype           |
| Due (date only)   | Due date               |
| n/a               | Phone                  |
| n/a               | Call duration          |
| n/a               | Priority               |
| n/a               | Created by             |
| Notes             | Comments               |
| Status            | Status                 |
| n/a               | Name (WhoId)           |
| n/a               | Related to (WhatId)    |
| n/a               | Email address          |
| n/a               | Last modified by       |
| Not supported     | Recurring Tasks        |
| Not supported     | Custom added fields    |





&nbsp;

!!! warning "Important"
    Note that several special use fields required for certain {{ product_name }} features to work must be added to Salesforce objects as part of {{ product_name }} setup in your Org. Refer to [this article](../Admin-Managed-Package/) for more information about them.



&#160;
 &#160;

