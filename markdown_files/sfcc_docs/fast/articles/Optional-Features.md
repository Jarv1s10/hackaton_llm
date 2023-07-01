---
description: The list of optional Revenue Grid features
---
# Optional {{ company_name }} features list  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*7 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

**[The article is work-in-progress]**

&nbsp;

------

&nbsp;


These *Global settings* are normally not available to local admins and can only be adjusted on request sent to [{{ product_name }} Support](mailto:support@revenuegrid.com); please describe in detail your specific preferences and use cases in the request. These settings regulate various aspects of Add-In / Chrome Extension and synchronization functioning and are applied as custom features to meet specific customer needs. Contact us to get the full list of global {{ product_name }} settings.

Finally, besides [regular sync adjustments](../Configuring-Activities-Synchronization-Settings/), {{ product_name }} offers special synchronization settings to meet your company's specific preferences – [syncing calendar items as other object types besides events](../Special-Sync-Options-Save-Events-As-Other-&-One-Way-Sync/#syncing_calendar_events_as_custom_or_standard_salesforce_objects_eg_tasks) and [one-way synchronization options](../Special-Sync-Options-Save-Events-As-Other-&-One-Way-Sync/#one-way_synchronization).

&nbsp;
***
&nbsp;

## Emails handling

&nbsp;

*SalesforceEmailAutoTrackIncludingNotShared* (disabled by default): a possibility to auto-save emails in Salesforce independently, without corresponding [People records](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) auto-creation or [Business records](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/)  linking. With this setting enabled, it is possible to save in Salesforce emails which have no relevant Business or People records for linking, which is the case if, for example, the email addresses/domains are [blocklisted from syncing](../Configuring-Activities-Synchronization-Settings/#blocklisting_email_addresses_and_domains).    
&nbsp;

*SalesforceEmailSafeDescriptionSync*: a setting for disabling the possibility to save Email bodies to Salesforce for all saving scenarios. This special feature that can be enabled on request sent at [{{ company_name }} support Team ](mailto:support@revenuegrid.com) for customers whose CRM capturing excludes Body saving.    
&nbsp;

##### Auto-sync Outbound (Sent) or Inbound (Inbox) emails only

There is a [sync pattern](../Synchronization-Engine-An-Overview/) adjustment setting that allows to limit emails auto-syncing scope to Outbound (Sent) or Inbound (Inbox) messages only.

&nbsp;

##### Linking email attachments to Salesforce Business records besides the Task/Email message object

This special feature that can be enabled on request sent at [{{ company_name }} support Team ](mailto:support@revenuegrid.com) allows linking of [email attachments](../Attachments-Handling-(Basic)/) to other objects besides Salesforce Tasks or Email messages, via the *Related To* field.
&nbsp;

In the latest {{ product_name }} the *SalesforceEmailLinkContentToBusinessObject* setting is enabled for all instances by default. That means email attachments saved in Salesforce as Content Files will be linked to related business records besides the Task/Email Message object in Salesforce.

&nbsp;
&nbsp;
* * *
&nbsp;

## Calendar items handling

&nbsp;

*SalesforceEventAutoTrackIncludingNotShared* (0 = disabled, disabled by default). By default, to be saveable in Salesforce an MS Outlook Meeting or Gmail event must have at least one relevant [Business or People record](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) to link it to. Enabling this setting makes it possible to save in Salesforce calendar items which have no relevant Business or People records for linking, which is the case if, for example, the email addresses/domains of all invitees are [blocklisted from syncing](../Configuring-Activities-Synchronization-Settings/#blocklisting_email_addresses_and_domains). 
&nbsp;      
  
*CalendarAvailabilityTerm*: sets the time span in the future for which a user's calendar availability is parsed when the **Book me** feature is used; 365 days by default.    
&nbsp;

*ServiceEventSafeDescriptionSync*: allows to disable the [Safe Description](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#calendar_item_description_field_updating_safe_description) feature for an Org or for individual end users.    
&nbsp;

*ServiceEventDeletionStrategy*: introduced to manage automatic removal of calendar items from MS Exchange / Office 365 or Gmail calendar by [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/) if they were deleted from Salesforce calendar by the users.    
&nbsp;

The *ServiceSyncNotRespondedInvitations* setting is used to enable or disable syncing in Salesforce of inbound meetings which were left unresponded or were declined by the invitee (who is an {{ short_name }} user). Some companies require that in order to get meetings registered in Salesforce even if they were not explicitly accepted. If this setting is disabled, an attempt to sync in Salesforce of a not-responded or declined meeting results in a sync error "*ISE-013: Meeting for attendees cannot be synchronized until the organizer synchronizes it.*"      
&nbsp;

*ShowTentativeAsBusy*: an optional possibility to make the [Share Calendar Availability (Book Me/Time Slots) feature](../Sharing-Calendar-Availability-(Adaptive-view)/) treat Tentative slots as Free instead of Occupied. This mechanics is managed Org-wide or for individual users, via this global setting.
&nbsp;    
    
  
*SyncPhoneNotesToMeetingDescription*: a setting for excluding meeting notes/invitee's phone number syncing from [Book Me/Time Slots](../Sharing-Calendar-Availability-%28Adaptive-view%29/) booking page to the resulting [Salesforce Event]( https://help.salesforce.com/s/articleView?id=sf.viewing_events_lex.htm&type=5), to meet specific customers' privacy/GDPR requirements.  

&nbsp;

##### Auto-create objects for unresolved invitees or recipients ([auto-resolving](../Synchronization-Engine-An-Overview/#automatic_creation_of_contacts_or_leads_by_rg_email_sidebar_autoresolving))

When [emails](../Saving-Emails-in-Salesforce-1.-Function-Overview/) or [calendar items](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/) received from or sent to unresolved (previously not registered in Salesforce) email addresses are saved in Salesforce by assigning them the Salesforce category or moving them to the Salesforce emails folder, {{ product_name }} can automatically create corresponding objects in Salesforce to [link](https://help.salesforce.com/articleView?id=overview_of_custom_object_relationships.htm&type=5) the matching Tasks/Email messages or Calendar Events to. Object types which can be created in these cases: Leads or Contacts. To request this feature for your Org, send a detailed request to [{{ company_name }} support team](mailto:support@revenuegrid.com), describing your preferences.    
&nbsp;

*SalesforceContactAutoCreateAccount*: {{ product_name }} will auto-create corresponding Accounts on sharing a Contact from a previously not registered company; enabled by default.    
&nbsp;

*SalesforceContactAutoLookupAccount*: relevant Accounts are automatically retrieved to be linked to auto-created Contacts; enabled by default.    
&nbsp;

*SalesforceEventSmartAutoSharing* – when this setting is set to 1 (enabled), the list of meeting attendees gets re-synced with Salesforce on every [sync session](../Synchronization-Engine-An-Overview/). That is required to get invitees added to the list later registered in Salesforce. If it is set to 0 (disabled), the attendees list gets upsynced to Salesforce only once, on the meeting's initial sharing.    
&nbsp;

The *SalesforceEventInviteEmployeeOnly* special setting allows to exclude external (outside of Org contacts) meeting attendees from being synced in Salesforce by {{ short_name }} Sync and getting meeting invites. It is set to 0 by default, change to 1 to enable external attendees from syncing and invitations sending.    
&nbsp;

An augmented [objects auto-resolving](../Synchronization-Engine-An-Overview/#automatic_creation_of_contacts_or_leads_by_rg_email_sidebar_autoresolving) mechanism was added, enabled by the global setting *SalesforceSmartCreateUnresolvedObjects* (disabled by default). How this pattern works: If there's a match with an attendee's email address domain in: a) an Account's website field and b) a Contact linked to the Account, {{ short_name }} creates a Contact linked to the Account with this match. Note that popular personal email domains (*gmail.com*, *outlook.com*, etc.) are excluded from this pattern: no Contacts are auto-created for meetings sent or received from addresses on these domains.    
&nbsp;

If the *Create Person accounts* setting is enabled in [{{ short_name }} global settings](../Special-Admin-Panel-Settings/#extra_configuration_settings), Person accounts are created instead of Contacts. If there's no Account match found to create a Contact and Create Person accounts is disabled, then a Lead is created.    
&nbsp;

And another added augmented [objects auto-resolving mechanism](../Synchronization-Engine-An-Overview/#automatic_creation_of_contacts_or_leads_by_rg_email_sidebar_autoresolving) is available, managed by the [global setting](../Special-Admin-Panel-Settings/#extra_configuration_settings) *SalesforceEmailCreateAllUnresolvedRecipients* (disabled by default). How this pattern works: if enabled, Accounts and Leads/Contacts are created for **all** auto-saved incoming and outgoing emails for which no matching [Person/Business records](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) are found in Salesforce.


&nbsp;
##### Instant Sync (sync auto-forcing)

*InstantSyncEnabled*: disable/enable [{{ short_name }} Instant sync](../Synchronization-Engine-An-Overview/#instant_sync_of_calendar_items/).    
&nbsp;  

*TriggerSyncOnAdd*: disable/enable Instant sync triggering on calendar items creation in MS Outlook Desktop or On the Web version/Gmail.    
&nbsp;  

*TriggerSyncOnUpdate*: disable/enable Instant sync triggering on calendar items updating in MS Outlook Desktop or On the Web version/Gmail.    
&nbsp;  

*TriggerSyncOnDelete*: disable/enable Instant sync triggering on calendar items deletion in MS Outlook Desktop or On the Web version/Gmail.

&nbsp;

&nbsp;

* * *

&nbsp;

## Salesforce objects handling

&nbsp;

* * *

&nbsp;

## Misc. Adjustments


*SalesforceAddinCustomization*: disable/enable the local Admin's ability to set the default (initial) customization to be applied for new {{ short_name }} users or after a reset to default customization. More information [here](../Managing-Email-Sidebar-Customizations/#default_customization_settings).    
&nbsp;    
  
*ServiceEmployeeCleanupInactivePeriod*: the optional auto-deletion of inactive users from {{ short_name }} database. It is carried out daily, based on *Inactive user* criteria: users that did not open the Add-In and had no Sync sessions over a set period of time (6 months by default). Also includes new users who never ran Sync nor opened the Add-In over 6 months. Only non-admin users get deleted. Inactive users get removed from both ServerSync and MailApp databases. Auto-deletion and Inactive users parameters can be set up individually for different tenants (Global Settings). It can be enabled [upon request](mailto:support@revenuegrid.com).

&nbsp;
* * *
&nbsp;
## Gmail Extension Adjustments

*GoogleDisableDriveAttachments* ([{{ short_name }} Chrome Extension for Salesforce and Gmail](../Using-the-Solution-for-Salesforce-and-Gmail/) only). This setting allows to define whether files attached to emails as Google drive links could be [shared](../Attachments-Handling-(Basic)/) in Salesforce. Google Drive files sharing via {{ short_name }} is enabled by default (set to 0); when set to 1, Google drive files sharing is disabled. This setting is used by those customers who prefer not to authenticate {{ short_name }} access to their Google Drive files, for any considerations. 
&nbsp;

*GoogleCalendarLastActivityTimeSpan* (set to 15 by default). Defines the time span in the past from the current date over which color-marked Gmail calendar events get synced in Salesforce. This is necessary to delimit the range of the [sliding time window](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#meeting_appointment_autosaving) which applies {{ short_name }} Extension's events color-marking to events, see point ( **3** ) in [this article](../Using-the-Solution-for-Salesforce-and-Gmail/#saving_emails_in_salesforce) for more information. After the events pass out of the range they regain the color-marking they had previously, if any.  
&nbsp;

*GoogleEnableRecurrentEvents*: 2-way synchronization of recurring Google Calendar Events series. Syncing is performed by color-coding or [via Save button](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#saving_calendar_items_semi-automatically) or enabled [auto-saving](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#meeting_appointment_autosaving) in [Sync Settings](../How-to-Open-Sync-Dashboard-(Adaptive-view)/); syncing a single event in a series syncs the entire series. The number of occurrences that can be synced is based on [Salesforce limit]( https://help.salesforce.com/s/articleView?id=sf.creating_events_cex.htm&type=5#:~:text=Maximum%20Number%20of%20Single%20Events%20in%20a%20Series). Generally, private Google Events cannot be synced.    

&nbsp;
***
&nbsp;

## Typical product features config


**Typical Add-In Config**

| Function                                                     | Typical status                                      | Usage          |
| ------------------------------------------------------------ | --------------------------------------------------- | -------------- |
| Meeting Scheduler  Time slots   Book Me                      | Enabled                                             | Medium to high |
| Engagement (track email opens)                               | Enabled                                             | Medium to high |
| CRM Email Templates                                          | Enabled                                             | Seldom         |
| Quick access to recent Salesforce reports                    | Enabled                                             | Seldom         |
| Salesforce Chatter                                           | Enabled                                             | Seldom         |
| Include internal contacts into search results                | Disabled                                            |                |
| Linking email attachments to Salesforce Business records besides the Task / Email message Object | Disabled                                            |                |
| Creation/modification of records                             | Enabled                                             | High           |
| Custom objects usage                                         | Customization                                       | High           |
| Customization for end-users/admins                           | End-users when smaller companies, admins for larger | High           |
|                                                              |                                                     |                |

 

 

 

**Typical Sync config**

| General                                                      | Typical status    | Usage                                     |
| ------------------------------------------------------------ | ----------------- | ----------------------------------------- |
| Link to Opportunities                                        | Enabled           | Medium                                    |
| Smart description                                            | Disabled          | Nice to have when enabled                 |
| blocklisted Domains                                          | Enabled           | High                                      |
| Prefilling of special fields by {{ short_company_name }} (e.g. mark a field  ‘Created by {{ short_company_name }}’ if a record was created by {{ short_company_name }}) | 50/50             | Nice to have when enabled                 |
| Mark inbound/outbound emails in some custom  fields          | 50/50             | Nice to have when enabled                 |
| Enhanced email vs. Tasks usage                               | 50/50             | Either way, depending on the requirements |
| Emails                                                       |                   |                                           |
| Manual                                                       | Enabled           | High                                      |
| Auto-Saving                                                  | 50/50             | Enabled for most                          |
| Emails Deduplication                                         | Enabled           | High                                      |
| Auto Track correspondence threads                            | 50/50             | High                                      |
| Email Body Cropping                                          | Disabled          | Seldom                                    |
| Save the *.eml* copy of an email as attachment               | Enabled           | Seldom                                    |
| Auto-Create Unresolved recipients as Leads  or Contacts      | 50/50             | Nice to have when enabled                 |
| Events                                                       |                   |                                           |
| Saving Calendar Items manually via Add-In                    |                   |                                           |
|                                                              | Meetings          | Allowed                                   |
|                                                              | Appointments      | Allowed                                   |
|                                                              | Internal meetings | Allowed                                   |
|                                                              | Recurrent events  | Allowed                                   |
| Meetings Auto-Syncing                                        | Enabled           | High                                      |
| Appointments Auto-Syncing                                    | 50/50             | Medium                                    |
| Internal meetings auto-syncing                               | Disabled          | Medium                                    |
| Recurrent events auto-syncing                                | Enabled           | Medium                                    |
| Linking event attachments to Salesforce  Business Objects besides the Event Object | Disabled          |                                           |
| Auto-Create Unresolved Meeting attendees as  Leads or Contacts | 50/50             | Nice to have when enabled                 |
| Safe Description feature                                     | Enabled           | Usually used                              |
| In case you have required fields on Event  Object in Salesforce, specify field API name and exact value that should be  set as default for Synchronization Engine | Disabled          |                                           |
| Tasks                                                        |                   |                                           |
| Auto Sync Salesforce Tasks to Outlook Tasks                  | 50/50             | Seldom                                    |
| Contacts                                                     |                   |                                           |
| Auto Sync Salesforce Contacts to Outlook  Contacts           | Enabled           | Medium to High                            |
|                                                              |                   |                                           |
| Return on Investment                                         | Enterprise only   | Medium                     |

 &nbsp;

&nbsp;

