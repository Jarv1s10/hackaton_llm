---
description: Revenue Grid Email Sidebar Complete List of Functions and Features
---
# The Complete List of the Solution's Functions and Features  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*4 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

***[this article is a work-in-progress]***

&nbsp;

### Sync Engine Functions

!!! tip "Tip"
    **\*** Marks functions carried out by Sync Engine but initiated via the Add-In



[Auto-save in Salesforce all past and future emails](../Save-All-Emails-in-a-Thread/) in a marked thread

[Save in Compose mode](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-%28Adaptive-view%29/#1_saving_an_email_when_revenue_grid_synchronization_is_active) 

Set [*Outbound* or *Inbound* marking in saved emails' dedicated field](../Admin-Managed-Package/#package_contents) in Salesforce

Add an [indication if an item was handled by {{ short_name }} Sync in saved activities' dedicated field](../Admin-Managed-Package/#package_contents)

[Instant sync: Save Calendar items instantly, without waiting for the next Sync session](../Synchronization-Engine-An-Overview/#instant_sync_of_calendar_items). Or adjust the interval between Sync sessions to meet company-specific calendars sync requirements

[Auto-save all new inbound and outbound emails](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_emails_emails_autosharing) from/to [non-blocklisted addresses or domains](../Blocklisting-Email-Addresses-and-Domains/), ensuring that only business correspondence gets processed

[Add Memos to captured items](/Record-Description-and-Add-Quick-Memo/) as detailed notes to self

[Pin the Sidebar so it opens automatically](../Sidebar-Pinning/) whenever you select an MS Outlook item you want to save or view associated data for

[Auto-sync all new non-Private meetings or appointments](../Configuring-Activities-Synchronization-Settings/#automatic_syncing_of_calendar_items_events_autosharing) with your Salesforce calendar

Work with [Salesforce reports directly from the Sidebar](../Salesforce-Reports/)

[Use Salesforce templates](../Using-Salesforce-Templates/) to quickly compose emails or reply to enquiries

[Use the custom category/folder/label in MS Outlook](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#31_by_assigning_the_salesforce_email_category) or in Gmail / Google Calendar interface to easily mark items to be saved in Salesforce

Use all essential {{ short_name }} functions on [mobile devices: iOS and Android smartphones or tablets](../Using-on-iPhone/)

Use all {{ short_name }} 🡘 MS Outlook integration functions on any platforms in [a compatible web browser](../Frequently-Asked-Questions/#supported_browsers_with_outlook_on_the_web) via [MS Outlook on the Web](https://en.wikipedia.org/wiki/Outlook_on_the_web)

Easily sync your [Tasks](../Synchronization-of-Tasks/) and [Contacts](../Synchronization-of-Contacts/) two-way between your mail client and Salesforce

[Use custom color-coding](../Using-the-Solution-for-Salesforce-and-Gmail/#syncing_calendar_events_in_salesforce) to sync Google Events with Salesforce

Auto-resolving: [auto-creates relevant Contacts and Accounts, or Leads](../Synchronization-Engine-An-Overview/#automatic_creation_of_contacts_or_leads_by_rg_email_sidebar_autoresolving), when that is required to link auto-saved activities

Auto-creates relevant records for [previously unknown meeting Attendees](../Synchronization-Engine-An-Overview/#automatic_creation_of_contacts_or_leads_by_rg_email_sidebar_autoresolving)

Ensures that [Events creation or modifying in Salesforce is reflected in MS Outlook or Google Calendar](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#events_down-syncing_from_salesforce_to_mail_clients_calendar)

[Customize activities handling and deletion rules](https://docs.revenuegrid.com/ri/fast/articles/Choosing-What-to-Synchronize/)

[Selectively or automatically save files attached to email and calendar items](../Attachments-Handling-(Basic)/) in Salesforce

[Safe Description](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#calendar_items_description_field_updating_safe_description): ensures that Calendar item's description from doesn't leak to invitees

Sync  [recurring calendar items series](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#synchronizing_series_of_recurring_items) two-way between MS Outlook or Google Calendar and Salesforce

Ensures that [Events initiated via Salesforce Lightning Scheduler](../Partner-Community-Integration/#lightning_scheduler_integration_specifics) are reflected in email client's calendar

[Smart Description: Customized appending of relevant values retrieved from any Event fields to their matching MS Outlook or Google Calendar items](../Using-the-Smart-Description-Feature/). Values retrieval and appending may also be configured involving values from other Salesforce objects' fields

Optionally, Sync Engine may [auto-capture only Inbound or Outbound emails](../Optional-Features/#auto-sync_outbound_sent_or_inbound_inbox_emails_only)

[Conditional calendar items unsyncing](../Synchronization-Engine-An-Overview/#conditional_un-syncing_of_events): depending on the value in a specific Salesforce Event field, the matching item may get auto-removed from email client’s calendar but remain in Salesforce 

[Force or Pause Sync Sessions to manage items capturing](../How-to-Open-Sync-Dashboard-%28Adaptive-view%29/#force_rges_sync); quickly [troubleshoot possible Sync errors and any record creation/update conflicts](../Handling-Sync-Issues/)

A unique optional possibility to link multiple [Business Records](https://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) to Events saved in Salesforce [via {{ product_name }}](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/); this multilinking function is not provided by Salesforce 

{{ product_name }} works with corporate MS Exchange servers via [Exchange Web Services](../Working-With-EWS/), but with Office 365 servers it may work over Exchange Web Services or [MS Graph](https://docs.microsoft.com/en-us/graph/overview). In the latter scenario, {{ short_name }} provides custom integration possibilities with other Microsoft products, e.g. [MS Teams](../Sharing-Calendar-Availability-(Adaptive-view)/#ms_teams_integration_on_location_selection) and others.



&nbsp;

### Add-In Functions (MS Exchange / O365)

Meeting Scheduler: quickly initiate meetings via the [Book Me (share all available slots and let choose any)](../Sharing-Calendar-Availability-(Adaptive-view)/) and [Time Slots (suggest specific time slots)](../How-to-Send-Meeting-Time-Slots-(Adaptive-view)/) features

Easily [register Follow-Ups and Log Calls information](../Log-A-Call/) in Salesforce

[Centralized bulk {{ short_name }} setup](../Email-Integration-Full-Deployment-Scenarios/) and [config management](../Managing-Email-Sidebar-Customizations/)

Save emails [as Salesforce Tasks or EmailMessage objects (Enhanced email)](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#11_emails_saved_as_emailmessages_vs_emails_saved_as_tasks)

Save email and calendar items attachments [as Salesforce Content documents or as Attachments](../Configure-Attachments-Saving-in-Salesforce/). Set specific parameters for files to be saved: [file extensions](../Special-Admin-Panel-Settings/#email_attachment_extensions_allow-list) and sizes, to prevent viruses/trojans or junk files saving

[Directly store documents in dedicated external document storages like DocuSign](../How-to-work-with-DocuSign-Document-Storage-via-the-Sidebar/), access, view and send them via the Sidebar

Instantly [viewing in the email client Sidebar all records related to selected emails and calendar items](../Initial-Search-and-Applied-Record-Filters/#related_records_retrieval_pattern)

[Instantly viewing any record's chosen fields, as well as all associated activities and files](../All-User-Actions-in-Add-In-Sidebar/#4_viewing_the_details_instantly) in the Sidebar

Perform [user-initiated search for relevant Salesforce records](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-(Adaptive-view)/) for a quick reference or to save emails and calendar items with

[Editing email and calendar items' key fields via the Sidebar](../Save-Email-Dialog/) when saving them

[Create any record types directly in Salesforce](../Create-New-Records/)

[The Sidebar indicates an email or calendar item's saving status](../All-User-Actions-in-Add-In-Sidebar/#11_email_event_saving_status_indication_in_sidebar_header)

[Quickly view any activities or records in Salesforce](../Synchronization-of-Tasks/#opening_a_task_directly_in_salesforce) via direct links

[Configure items linking rules](../All-User-Actions-in-Add-In-Sidebar/#7_smart_selection_of_records_to_be_linked) applied on their saving

Quickly [view Leads', Contacts', and Accounts' LinkedIn profiles](../Finding-Social-Profiles-of-Contacts%2C-Leads%2C-and-Accounts-(Classic-view)/)

A [Save dialog](../Save-Email-Dialog/) to get an item saved afresh with another set of linked records or edit its details, if required

[Edit already saved Emails' bodies](../Save-Email-Dialog/#editing_saved_emails_body)

[Track Email opens](../Tracking-Customer-Engagement-with-Magic-Pixel-(Adaptive-view)/), track Link clicks: time, approximate location, device type, opens/clicks count

Displays [{{ short_name }} use tutorial guides](../Frequently-Asked-Questions/#14_what_onboarding_materials_user_guides_are_available_for_the_solution) to enhance the learning curve

[Enable email bodies auto-crop](../Auto-Cropping-of-Previous-Messages-in-Email-Body/) on saving, removing older messages texts

[Automatic deduplication of created records and activities](../Item-Deduplication-Mechanisms/), to ensure that only one instance of each exists, with some exceptions

Easily prevent saving of personal and in-Org correspondence and Appointments / Meetings using [two layers of email address/domain blocklisting](../Two-Layers-Blacklisting/)

Configure handling of [Salesforce Custom objects](https://trailhead.salesforce.com/en/content/learn/modules/data_modeling/objects_intro) or your Org-specific custom objects by {{ short_name }}

[Use configured Salesforce custom buttons via the Sidebar](../Salesforce-Custom-Buttons-Support/)

Configure many aspects of Sidebar usage via [Customization page](../Customization-Settings-Explained/); [share or enforce customized sets of settings among different users or user groups](../Managing-Email-Sidebar-Customizations/), based on their roles in Salesforce and in departments

{{ short_name }} allows [linking file attachments to Business records (WhatID)](../Attachments-Handling-(Basic)/#attachments_linking_to_salesforce_business_records_on_auto-saving)

{{ short_name }} may [create duplicates of saved emails](../Item-Deduplication-Mechanisms/#allow_creating_email_duplicates_in_salesforce), in order to get them linked to all relevant People and Business records, in case your business flow requires that

[Stale thread reminder](../Stale-Thread-Reminder/): indicates if an email you send was not answered within a specified period of time, to initiate sending a follow-up

With the help of [our Support team](mailto:support@revenuegrid.com), configure automatic prefilling of certain values in fields in Save dialog, to save time on their handling

[Get email context-dependent hints](../Context-Specific-Actions/)

[Drag and drop an email signature into the Sidebar](../All-User-Actions-in-Add-In-Sidebar/#create_contacts_via_signature_drag-and-drop) to get its details parsed as a new Contact

Configure user-initiated search patterns in your preferred way, by [setting up the Search By fields](../Using-the-Search-by-List-Customization-Setting/)

Easily install an [all-inclusive {{ company_name }} config Managed package](../Admin-Managed-Package/) to facilitate {{ short_name }} setup on Salesforce side

[Embed handy {{ company_name }} gadgets](../Admin-Managed-Package/#iii_add_revenue_grid_components_to_salesforce_user_interface) into your Salesforce account page to ensure easy an easy functions reach

You may also [save emails without linking them to any records](../Saving-Emails-in-Salesforce-1.-Function-Overview/#saving_any_emails_without_linking_them)

View [data capture statistics and Return on Investment indicators](../Return-on-Investment-ROI-Usage-Efficiency-and-User-Setup-Status-Tools/) for your {{ short_name }} usage

&nbsp;

### Chrome Extension Functions (Gmail / Google Workspace)

Same functions as MS Outlook Add-In's, with the exceptions listed in [this article](../Using-the-Solution-for-Salesforce-and-Gmail/#differences_between_the_exchangeoffice_365_add-in_implementation_and_the_chrome_extension_for_gmail).

&#160;
 &#160;

