---
description: Overview and detailed explanation of the special Admin Panel settings
---
# Special Admin Panel Settings  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*14 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! warning "Important"
    To use {{ product_name }} Admin panel, special access permissions are required. To request the permissions for your organization, [contact {{ company_name }} support team by email](mailto:support@revenuegrid.com). Admin panel provides tools for managing end users and some of its key settings it includes duplicate {{ product_name }} [Customization](../Customization-Settings-Explained/) and [Sync](../Configuring-Activities-Synchronization-Settings/) settings on Admin level

&nbsp;

[Admin panel](../How-to-Log-In-to-the-Admin-Panel/) provides a number of settings used to adjust different aspects of {{ company_name }} synchronization, search, and customization functions for organizations as well as individual Add-In / Chrome Extension users.
Some of them duplicate settings available on end users' [Customization page](../Customization-Settings-Explained/) and [Synchronization dashboard](../How-to-Open-Sync-Dashboard-(Adaptive-view)/), but are applied to all users in an organization and cannot be changed by the end users (these settings are greyed-out for them); others are designed to tailor Add-In / Chrome Extension and sync behavior to various specific needs or manage users' access to customization settings.
Finally, there are several configuration field settings required for enabling some of advanced {{ product_name }} features. These features also require creation of custom record fields in Salesforce, which can also be created automatically by [installing the {{ company_name }} package](../Admin-Managed-Package/).

For convenience of use, several commonly used special settings are implemented on the **Other settings** tab of all [user organizations](../Managing-Organizations-via-the-Admin-Panel/) as switch buttons and entry boxes.

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b99460f0428631d7a8b07fb.png" class="minimized">
</p>

&nbsp;

!!! note "Note"
    An Admin can _force_ certain settings, overriding them on a user's  Synchronization or Customization page (admin overridden settings will be displayed as greyed-out), or _allow_ users to adjust these settings individually

&nbsp;

!!! warning "Important"
    Most {{ product_name }} implementations include only the **Allow customization management** setting, the rest customization and configuration settings being managed by [{{ company_name }} support team](mailto:support@revenuegrid.com)

&nbsp;

&nbsp;

### Allow customization management

Toggle this switch button to allow or disallow the end users in this organization to manage their individual customization settings via [Customization page](../Customization-Settings-Explained/).  
Please note that to apply this setting the concerned user(s) must [log out from their {{ product_name }} account](../How-to-Change-Email-Address-in-Your-Product-Account-Office-365/) and then [re-log in](../How-to-Install-and-Run-the-Solution-all-configurations/#ii_rg_email_sidebar_logon).

!!! note "Note"
    The **Allow to manage customization** setting can also be applied to individual users via the **Other settings** Admin panel subtab opened for [individual users](../Managing-Users-via-the-Solution-s-Admin-Panel/) instead of organizations

&nbsp;

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b99470f0428631d7a8b080a.png" class="minimized">
</p>

&nbsp;

&nbsp;

### Emails auto-sync

Allows to enable/disable automatic saving of new email messages in Salesforce. Duplicates [the corresponding synchronization setting](../Configuring-Activities-Synchronization-Settings/).  

&nbsp;

### Meetings auto-sync

Allows to enable/disable automatic saving of new created or accepted meetings in Salesforce. Duplicates [the corresponding synchronization setting](../Configuring-Activities-Synchronization-Settings/#automatic_syncing_of_calendar_items_events_autosharing).  

&nbsp;

### Appointments auto-sync

Allows to enable/disable automatic saving of new created appointments in Salesforce. Duplicates [the corresponding synchronization setting](../Configuring-Activities-Synchronization-Settings/#automatic_syncing_of_calendar_items_events_autosharing).

&nbsp;

### Linking to Opportunities

Allows to enable/disable records linking to Opportunity Salesforce objects besides Contacts, Accounts, or Leads. Duplicates [the corresponding synchronization setting](../Configuring-Activities-Synchronization-Settings/#linking_to_opportunities).

&nbsp;

### Organization email domains

Specify corporate email domains used by your organization. This defines what email addresses will be considered _internal_; refer to [this article](../Initial-Search-and-Applied-Record-Filters/#internal_emails_corporate_domains_and_the_blocklist) for more information.  
Please note that to apply this setting the concerned user(s) must [log out from their {{ product_name }} account](../How-to-Change-Email-Address-in-Your-Product-Account-Office-365/) and then [re-log in](../How-to-Install-and-Run-the-Solution-all-configurations/#ii_rg_email_sidebar_logon).

&nbsp;

### Email attachment extensions allow-list

Specify what email attachment file types will be savable in Salesforce on [email/event auto-saving](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_emails_emails_autosharing). If left void, files with any extensions will be saved. This setting doesn't affect attachment files [saved manually](../All-User-Actions-in-Add-In-Sidebar/#8_more_convenient_email_event_attachments_saving).
Please note that to apply this setting the concerned user(s) must [log out from their {{ product_name }} account](../How-to-Change-Email-Address-in-Your-Product-Account-Office-365/) and then [re-log in](../How-to-Install-and-Run-the-Solution-all-configurations/#ii_rg_email_sidebar_logon).

&nbsp;

### Reduce tasks duplicates

Enables/disables preventing multiple Salesforce objects creation for the same email message received and saved by several users in one Salesforce Org. Please refer to [this article](../Item-Deduplication-Mechanisms/#general_email_deduplication/) for more information.
Please note that to apply this setting the concerned user(s) must [log out from their {{ product_name }} account](../How-to-Change-Email-Address-in-Your-Product-Account-Office-365/) and then [re-log in](../How-to-Install-and-Run-the-Solution-all-configurations/#ii_rg_email_sidebar_logon).

**Original email ID field**
This field is mandatory if the **Reduce tasks duplicates** setting is enabled. Here, set the name of the custom field containing the original [email message’s ID in MS Exchange](http://docs.microsoft.com/en-us/exchange/mail-flow/transport-logs/message-tracking) in Salesforce Activities (Tasks or EmailMessages) based on the email. If in your Org emails are saved as [EmailMessage](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_emailmessage.htm) objects rather than Tasks the *MessageIdentifier* field should be used; if emails are saved as Tasks and you installed [{{ company_name }} managed package](../Admin-Managed-Package/) in your Org the *InternetMessageID* field should be used. In case you do not have {{ company_name }} installed in your Org and do not use Salesforce Enhanced Email, you must create this custom field for the Task object in Salesforce. Please refer to [this Salesforce Help article](https://help.salesforce.com/articleView?id=adding_fields.htm&type=5) to learn how to do that.

&nbsp;

### Email direction field

Set the custom name of the field that indicates email direction ( _inbound_ / _outbound_) in Salesforce, e.g. "Message direction". This field will be added in Salesforce.  

**Label for inbound emails**
Set the label that will indicate if a message is inbound (to be displayed in the **Email direction** field).  

**Label for outbound emails**
Set the label that will indicate if a message is outbound (to be displayed in the **Email direction** field).

&nbsp;

### Email threads auto-sync

Enable/disable automatic saving of all emails which belong to a correspondence thread in Salesforce. Duplicates [the corresponding synchronization setting](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_email_threads).  
Please note that to apply this setting the concerned user(s) must [log out from their {{ product_name }} account](../How-to-Change-Email-Address-in-Your-Product-Account-Office-365/) and then [re-log in](../How-to-Install-and-Run-the-Solution-all-configurations/#ii_rg_email_sidebar_logon).


**Thread ID field**

This field is mandatory if the **Email threads auto-sync** setting is enabled. In it, set the custom name of the field that indicates the auto-saved thread's ID (mandatory if the **Email threads auto-sync** setting is enabled) in Salesforce. Similarly to the **Original Email ID** field, this field can be set up as part of the [{{ company_name }} Salesforce package](../Admin-Managed-Package/) - then it will be labeled *ConversationId* or [created manually in Salesforce](https://help.salesforce.com/articleView?id=adding_fields.htm&type=5).

&nbsp;

### Default users Plan

Plans allow enabling customized sets of specific settings for selected users and groups of users. Enter the 
Plan’s _external ID_ string in this field. Please refer to [this article](../Managing-Plans-for-the-Users/) for more information.  

&nbsp;

### Emails / domains blocklisted from sync

Specify email addresses or domains to be excluded from saving in Salesforce, e.g. personal contacts or in-organization ones. Note that the list does not support using [wildcards](https://www.computerhope.com/jargon/w/wildcard.htm). This list complements [the corresponding customization setting](../Blocklisting-Email-Addresses-and-Domains/) - for every user both this corporate blocklist and one's individually managed blocklist will be applied.

Please note that to apply this setting the concerned user(s) must [log out from their {{ product_name }} account](../How-to-Change-Email-Address-in-Your-Product-Account-Office-365/) and then [re-log in](../How-to-Install-and-Run-the-Solution-all-configurations/#ii_rg_email_sidebar_logon).

!!! warning "Important"
    After you make changes in the settings, make sure to click the Save button in the upper right corner of the page to save and apply them

&nbsp;

!!! note "Note"
    Some {{ product_name }} configurations also include the **Global settings** tab with the table of other special settings implemented as fields and values

&nbsp;

* * *

&nbsp;

## Extra Configuration Settings

Unlike the above described *Special settings*, {{ product_name }} *Global settings* are normally not available to local admins and can only be adjusted on request sent to [{{ product_name }} Support](mailto:support@revenuegrid.com); please describe in detail your specific preferences and use cases in the request. These settings regulate various aspects of Add-In / Chrome Extension and synchronization functioning and are applied as custom features to meet specific customer needs. Contact us to get the full list of global {{ product_name }} settings.

Finally, besides [regular sync adjustments](../Configuring-Activities-Synchronization-Settings/), {{ product_name }} offers special synchronization settings to meet your company's specific preferences - [syncing calendar items as other object types besides events](../Special-Sync-Options-Save-Events-As-Other-&-One-Way-Sync/#syncing_calendar_events_as_custom_or_standard_salesforce_objects_eg_tasks) and [one-way synchronization options](../Special-Sync-Options-Save-Events-As-Other-&-One-Way-Sync/#one-way_synchronization).

&nbsp;

&nbsp;

### Linking email attachments to Salesforce Business records besides the Task/Email message object

This special feature that can be enabled on request sent at [{{ company_name }} support Team ](mailto:support@revenuegrid.com) allows linking of [email attachments](../Attachments-Handling-(Basic)/) to other objects besides Salesforce Tasks or Email messages, via the *Related To* field.

&nbsp;

&nbsp;

### Auto-create objects for unresolved meeting participants ([auto-resolving](../Synchronization-Engine-An-Overview/#automatic_creation_of_contacts_or_leads_by_rg_email_sidebar_autoresolving))

When [emails](../Saving-Emails-in-Salesforce-1.-Function-Overview/) or [calendar items](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/) received from or sent to unresolved (previously not registered in Salesforce) email addresses are saved in Salesforce by assigning them the Salesforce category or moving them to the Salesforce emails folder, {{ product_name }} can automatically create corresponding objects in Salesforce to [link](https://help.salesforce.com/articleView?id=overview_of_custom_object_relationships.htm&type=5) the matching Tasks/Email messages or Calendar Events to. Object types which can be created in these cases: Leads or Contacts. To request this feature for your Org, send a detailed request to [{{ company_name }} support team](mailto:support@revenuegrid.com), describing your preferences.

&nbsp;

*SalesforceContactAutoCreateAccount*: {{ product_name }} will auto-create corresponding Accounts on saving a Contact from a previously not registered company; enabled by default.

&nbsp;

*SalesforceContactAutoLookupAccount*: relevant Accounts are automatically retrieved to be linked to auto-created Contacts; enabled by default.

&nbsp;

&nbsp;

### Book Me fine-tuning

*CalendarAvailabilityTerm*: sets the span in the future for which a user's calendar availability is parsed when the **Book me** feature is used; 365 days by default.

&nbsp;

*BookMeLinkExpirationPeriod*: sets the expiration period of Book Me links generated by users in the Org. For different reasons some companies require to set Book me links' lifespan shorter or longer.    
  
&nbsp;  

*ShowTentativeAsBusy*: an optional possibility to make the [Share Calendar Availability (Book Me/Time Slots) feature](../Sharing-Calendar-Availability-(Adaptive-view)) treat Tentative slots as Free instead of Occupied. This mechanics is managed Org-wide or for individual users, via this global setting.

&nbsp;

&nbsp;

### Sync Engine fine-tuning

*ServiceEventSafeDescriptionSync*: allows to disable the [Safe Description](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#calendar_item_description_field_updating_safe_description) feature for an Org or for individual end users.

&nbsp;

*InstantSyncEnabled*: disable/enable [{{ short_name }} Insta-sync](../Synchronization-Engine-An-Overview/#instant_sync_of_calendar_items/).  
*TriggerSyncOnAdd* disable/enable Insta-sync triggering on calendar items creation in MS Outlook Desktop or On the Web version/Gmail  
*TriggerSyncOnUpdate* disable/enable Insta-sync triggering on calendar items updating in MS Outlook Desktop or On the Web version/Gmail  
*TriggerSyncOnDelete* disable/enable Insta-sync triggering on calendar items deletion in MS Outlook Desktop or On the Web version/Gmail

&nbsp;

In the latest {{ product_name }} the *SalesforceEmailLinkContentToBusinessObject* setting is enabled for all instances by default. That means email attachments saved in Salesforce as Content Files will be linked to related business records besides the Task/Email Message object in Salesforce.

&nbsp;

The Global setting *ServiceEventDeletionStrategy* was introduced to manage automatic removal of calendar items from MS Exchange / Office 365 or Gmail calendar by [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/) if they were deleted from Salesforce calendar by the users.

&nbsp;

The *ServiceSyncNotRespondedInvitations* setting is used to enable or disable syncing in Salesforce of inbound meetings which were left unresponded or were declined by the invitee (who is an {{ short_name }} user). Some companies require that in order to get meetings registered in Salesforce even if they were not explicitly accepted. If this setting is disabled, an attempt to sync in Salesforce of a not-responded or declined meeting results in a sync error "*ISE-013: Meeting for attendees cannot be synchronized until the organizer synchronizes it.*"

&nbsp;

*SalesforceEventSmartAutoSharing*: when this setting is set to 1 (enabled), the list of meeting attendees gets re-synced with Salesforce on every [sync session](../Synchronization-Engine-An-Overview/). That is required to get invitees added to the list later registered in Salesforce. If it is set to 0 (disabled), the attendees list gets upsynced to Salesforce only once, on the meeting's initial sharing.

&nbsp;

The *SalesforceEventInviteEmployeeOnly* special setting allows to exclude external (outside of Org contacts) meeting attendees from being synced in Salesforce by {{ short_name }} Sync and getting meeting invites. It is set to 0 by default, change to 1 to enable external attendees from syncing and invitations sending.

&nbsp;

*SalesForceAPICallMinCount*: total [generated API calls](../Salesforce-API-Calls-Limit/) number count. As soon as it is reached, [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/) stops generating API calls

*SalesForceAPICallMinPercent*: [{{ product_name }} API calls](../Salesforce-API-Calls-Limit/) percentage among all Salesforce API calls. As soon as it is reached, [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/) stops generating API calls

&nbsp;

An augmented [objects auto-resolving](../Synchronization-Engine-An-Overview/#automatic_creation_of_contacts_or_leads_by_rg_email_sidebar_autoresolving) mechanism was added, enabled by the global setting *SalesforceSmartCreateUnresolvedObjects* (disabled by default). How this pattern works: If there's a match with an attendee's email address domain in: a) an Account's website field and b) a Contact linked to the Account, {{ short_name }} creates a Contact linked to the Account with this match. Note that popular personal email domains (*gmail.com*, *outlook.com*, etc.) are excluded from this pattern: no Contacts are auto-created for meetings sent or received from addresses on these domains.

If the *Create Person accounts* setting is enabled in [{{ short_name }} global settings](../Special-Admin-Panel-Settings/#extra_configuration_settings), Person accounts are created instead of Contacts. If there's no Account match found to create a Contact and Create Person accounts is disabled, then a Lead is created.  

And another added augmented [objects auto-resolving mechanism](../Synchronization-Engine-An-Overview/#automatic_creation_of_contacts_or_leads_by_rg_email_sidebar_autoresolving) is available, managed by the [global setting](../Special-Admin-Panel-Settings/#extra_configuration_settings) *SalesforceEmailCreateAllUnresolvedRecipients* (disabled by default). How this pattern works: if enabled, Accounts and Leads/Contacts are created for **all** auto-saved incoming and outgoing emails for which no matching [Person/Business records](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) are found in Salesforce.

&nbsp;

*SalesforceEventAutoTrackIncludingNotShared* (0 = disabled, disabled by default). By default, to be saveable in Salesforce an MS Outlook Meeting or Gmail event must have at least one relevant [Business or People record](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) to link it to. Enabling this setting makes it possible to save in Salesforce calendar items which have no relevant Business or People records for linking, which is the case if, for example, the email addresses/domains of all invitees are [blocklisted from syncing](../Configuring-Activities-Synchronization-Settings/#blocklisting_email_addresses_and_domains).

&nbsp;

*SalesforceEmailSafeDescriptionSync*: a setting for disabling the possibility to save Email bodies to Salesforce for all saving scenarios. This special feature that can be enabled on request sent at [{{ company_name }} support Team ](mailto:support@revenuegrid.com) for customers whose CRM capturing excludes Body saving.    

&nbsp;

*SyncPhoneNotesToMeetingDescription*: a setting for excluding meeting notes/invitee's phone number syncing from [Book Me/Time Slots](../Sharing-Calendar-Availability-%28Adaptive-view%29) booking page to the resulting [Salesforce Event]( https://help.salesforce.com/s/articleView?id=sf.viewing_events_lex.htm&type=5), to meet specific customers' privacy/GDPR requirements. 

&nbsp;

#### Auto-sync Outbound (Sent) or Inbound (Inbox) emails only

There is a [sync pattern](../Synchronization-Engine-An-Overview/) adjustment setting available upon customer's request that allows to limit emails auto-syncing scope to Outbound (Sent) or Inbound (Inbox) messages only.

&nbsp;

#### Conditional Events Un-Syncing

*SalesforceEventUnsyncConditions* (disabled by default). To meet certain CRM calendars capture flow requirements, implemented the following optional configurable Calendars sync feature: depending on the value in a specific Event field, the Event gets un-synced from email client's calendar but remains in Salesforce. This mechanism **can** be configured for the fields: 1. Checkboxes; 2. String fields: *Email*, *Phone*, *Text formulae*, *Text areas*, URLs, Picklists; 3. Any numeric fields whose decimal place is 0: *Numbers*, some *Currencies*, *Autonumbers*; 4. Multi-picklists: special case, triggered if a strong match for specified condition value is found.  
It **cannot** be configured for the fields: *Lookup*, *Date*, *Datetime*, *Body*, *Address*, non-filterable fields, encrypted fields, any double-value fields like currencies or other numbers whose decimal place is not 0.  
A sample use case: after a Matter or Case gets closed, its associated Event's status gets changed to ‘vacated’ and the Sync Engine removes the matching items from end users' mailbox calendars.  
{{ short_company_name }} customers may request [our Support team](mailto:support@revenuegrid.com) to enable the feature for them.

&nbsp;

&nbsp;

### Auto-saving and Blocklist Intersections

*SalesforceEmailAutoTrackMode* (default value = "0", General). This setting defines what strategy is used on ["not for syncing" blocklist](../Configuring-Activities-Synchronization-Settings/#blocklisting_email_addresses_and_domains) applying on saved emails linking, while the related setting SalesforceEmailCaptureLinkRule does not involve the blocklist. 

Note that for all SalesforceEmailAutoTrackMode setting values any emails can also be saved to a related record if [assigned the custom "Salesforce" category](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-%28Adaptive-view%29/#31_by_assigning_the_salesforce_email_category) or handled by [the thread saving mechanism](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_email_threads); they get processed by the Add-In with *ForceSync*. 

&nbsp;

#### The ForceSync Scenarios

*ForceSync* implies that an email gets saved in one of the following ways: **A.** by [category assigning](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-%28Adaptive-view%29/#3_besides_using_the_save_button_emails_saving_can_be_performed_in_4_more_easy_ways); **B.** by [moving to the dedicated folder](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-%28Adaptive-view%29/#3_besides_using_the_save_button_emails_saving_can_be_performed_in_4_more_easy_ways); **C.** by using the [Save button](../Save-Email-Dialog/) in the [Sidebar](../Introduction/).

On ForceSync saving emails never get linked to existing objects whose addresses are specified in the blocklist (the Global setting *ServiceAutoTrackBlacklist*) and no corresponding objects get auto-resolved (auto-created) if they are not found in Salesforce. Also see [this article](../Initial-Search-and-Applied-Record-Filters/) for to learn how the blocklist and other filters get applied.

&nbsp;

**Available auto-track modes:**  

*"0" - General* (default value)  
Emails get auto-saved if at least one recipient’s email address is already saved as a People Record in Salesforce. If there is no corresponding record found, the email will NOT be saved to Salesforce

&nbsp;

*"1" - Forced*  
Emails get auto-saved in the *ShareForce* mode, if at least one recipient is NOT blocklisted (internal employees' email addresses are blocklisted as well). If no record is found for the email to be saved to, {{ short_name }} will [create a new People Record in Salesforce](../Synchronization-Engine-An-Overview/#automatic_creation_of_contacts_or_leads_by_rg_email_sidebar_autoresolving). If all recipients are [blocklisted and/or are internal employees](../How-to-Save-Internal-or-Blacklisted-Emails-in-Salesforce-(Adaptive-view)/), the email will NOT be saved to Salesforce

&nbsp;

*"2" - Smart*  
Emails get auto-saved, even if NO recipient’s email addresses are saved as People Records in Salesforce. {{ short_name }} performs a search among Salesforce objects by unresolved emails’ domains. If any Salesforce object with a matching email domain address is found, {{ product_name }} creates a new object linked to the found one and saves the email. 

{{ short_name }} excludes free email services domains (e.g. gmail.com, yahoo.com, etc.) from the search and sync. Also, if all recipients are [blocklisted and/or belong to internal employees](../How-to-Save-Internal-or-Blacklisted-Emails-in-Salesforce-(Adaptive-view)/), the email will NOT be saved to Salesforce

&nbsp;

*"3" - Useful*  
Emails get auto-saved if at least one recipient’s email address is saved as a People Record in Salesforce (like in the “*General*” mode), but with additional rules applied. If the email can be linked with any Business Record, it will get auto-saved **ONLY** if at least one recipient’s email address is NOT blocklisted and is saved as People Record in Salesforce,  or if an auto-created independent [Business Record](https://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) gets linked. The latter case implies one of the following: 1. object reference links were found in email body or 2. reference links were found and email thread got identified by conversation text. 

This pattern ensures disabling of email auto-saving in case all email addresses in a new incoming or outgoing email are [blocklisted or internal](../How-to-Save-Internal-or-Blacklisted-Emails-in-Salesforce-(Adaptive-view)/), although a business object was captured in the email.  

&nbsp;

*"4" - Flexible*    
Emails get auto-saved, if at least one recipient’s email address is NOT blocklisted and is not saved as a People Record in Salesforce. In such case, {{ short_name }} creates a Salesforce object to link the email to and saves the email to the newly created Salesforce object. If {{ short_name }} identifies any Business Record related to the unsaved recipient’s email address, the new Salesforce object and the email will be linked to this Business Record as well.

{{ product_name }} excludes free email services domains (e.g. gmail.com, yahoo.com, etc.) from the search and sync scope. Also, if all recipients are [blocklisted and/or are internal employees](../How-to-Save-Internal-or-Blacklisted-Emails-in-Salesforce-(Adaptive-view)/), the email will NOT be saved to Salesforce.
&nbsp;

&nbsp;

### Add-In fine-tuning

*SalesforceAddinCustomization*: disable/enable the local Admin's ability to set the default (initial) customization to be applied for new {{ short_name }} users or after a reset to default customization. More information [here](../Managing-Email-Sidebar-Customizations/#default_customization_settings).      
&nbsp;    
  
*ServiceEmployeeCleanupInactivePeriod*: the optional auto-deletion of inactive users from {{ short_name }} database. It is carried out daily, based on *Inactive user* criteria: users that did not open the Add-In and had no Sync sessions over a set period of time (6 months by default). Also includes new users who never ran Sync nor opened the Add-In over 6 months. Only non-admin users get deleted. Inactive users get removed from both ServerSync and MailApp databases. Auto-deletion and Inactive users parameters can be set up individually for different tenants (Global Settings). It can be enabled [upon request](mailto:support@revenuegrid.com).

&nbsp;

&nbsp;

### Gmail / Google Calendar processing fine-tuning

*GoogleDisableDriveAttachments* ([{{ short_name }} Chrome Extension for Salesforce and Gmail](../Using-the-Solution-for-Salesforce-and-Gmail/) only) – this setting allows to define whether files attached to emails as Google drive links could be [shared](../Attachments-Handling-(Basic)/) in Salesforce. Google Drive files sharing via {{ short_name }} is enabled by default (set to 0); when set to 1, Google drive files sharing is disabled. This setting is used by those customers who prefer not to authenticate {{ short_name }} access to their Google Drive files, for any considerations. 

&nbsp;

*GoogleCalendarLastActivityTimeSpan* (set to 15 by default). Defines the time span in the past from the current date over which color-marked Gmail calendar events get synced in Salesforce. This is necessary to delimit the range of the [sliding time window](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#meeting_appointment_autosaving) which applies {{ short_name }} Extension's events color-marking to events, see point ( **3** ) in [this article](../Using-the-Solution-for-Salesforce-and-Gmail/#saving_emails_in_salesforce) for more information. After the events pass out of the range they regain the color-marking they had previously, if any.

&nbsp;

*GoogleEnableRecurrentEvents*: 2-way synchronization of recurring Google Calendar Events series. Syncing is performed by color-coding or [via Save button](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#saving_calendar_items_semi-automatically) or enabled [auto-saving](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#meeting_appointment_autosaving) in [Sync Settings](../How-to-Open-Sync-Dashboard-(Adaptive-view)); syncing a single event in a series syncs the entire series. The number of occurrences that can be synced is based on [Salesforce limit]( https://help.salesforce.com/s/articleView?id=sf.creating_events_cex.htm&type=5#:~:text=Maximum%20Number%20of%20Single%20Events%20in%20a%20Series). Generally, private Google Events cannot be synced.    


&nbsp;

&#160;
 &#160;

