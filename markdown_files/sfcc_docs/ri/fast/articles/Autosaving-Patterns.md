---
description: Detailed overview of Revenue Grid Email Sidebar auto-saving patterns
---
# Auto-saving Patterns Explained  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*3 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

## Emails auto-saving

 {{ product_name }} can [synchronize](../Synchronization-Engine-An-Overview/) new incoming and outgoing [emails](../Saving-Emails-in-Salesforce-1.-Function-Overview/) in Salesforce [automatically](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_emails_emails_autosharing), semi-automatically via [save all emails in a thread](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_email_threads), or [semi-automatically](../Saving-Calendar-Items-in-Salesforce-%28Adaptive-view%29/#saving_calendar_items_semi-automatically) through the dedicated folder/category or the Quick save button in MS Outlook ribbon. The saving patterns applied for these scenarios are identical. 



The matching Task or Email message item created in Salesforce is linked to automatically discovered relevant [Business records](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) (such as an Account, Opportunity, etc.) and to [People records](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) retrieved based on recipients' or sender's email addresses. If no Business and People records are found in Salesforce, {{ product_name }} can optionally auto-create corresponding records in Salesforce. See [this article](../Synchronization-Engine-An-Overview/#automatic_creation_of_contacts_or_leads_by_rg_email_sidebar_autoresolving) and the [Optional settings](../Autosaving-Patterns/#optional_settings) section below for more information.

&nbsp;

* * *

&nbsp;

## Events auto-saving

Events (calendar items) auto-saving patterns are more complex. {{ product_name }} can [synchronize](../Synchronization-Engine-An-Overview/) new incoming and outgoing [calendar items](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/) in Salesforce [automatically](../Saving-Calendar-Items-in-Salesforce-%28Adaptive-view%29/#meeting_appointment_autosaving) or [selectively](../Saving-Calendar-Items-in-Salesforce-%28Adaptive-view%29/#saving_calendar_items_semi-automatically), through the dedicated folder/category or the Quick save button in MS Outlook ribbon; the auto-saving patterns applied in these cases are identical. Calendar items are always saved by [{{ short_name }} sync engine](../Synchronization-Engine-An-Overview/) and it takes a couple of minutes to get a new meeting auto-synced in Salesforce via [instant sync](../Synchronization-Engine-An-Overview/#instant_sync_of_calendar_items).

The matching Calendar Event item created in Salesforce is linked to automatically discovered [Business records](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) (such as Accounts, Opportunities, etc.) and to [People records](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) retrieved based on attendees' email addresses. If no Business and People records are found in Salesforce, {{ product_name }} can optionally auto-create corresponding records in Salesforce. See [this article](../Synchronization-Engine-An-Overview/#automatic_creation_of_contacts_or_leads_by_rg_email_sidebar_autoresolving) and the [Optional settings](../Autosaving-Patterns/#optional_settings) section below for more information.

Non-accepted or Declined meetings can optionally be synced in Salesforce as well, see [this article](../Calendar-Items-Sync-Special-Patterns-Attendees-Lists%2C-Private-Items%2C-Item-Unsharing-and-Deletion/#syncing_non-responded_or_declined_meetings) for details. Files attached to meetings or appointments do **not** get saved along with synced meetings, unless a corresponding [global setting](../Special-Admin-Panel-Settings/#extra_configuration_settings) is enabled for your Org by request. An MS Outlook meeting's description is only saved in Salesforce once and will **not** get updated in the future due to [Safe Description](../Saving-Calendar-Items-in-Salesforce-%28Adaptive-view%29/#calendar_items_description_field_updating_safe_description) considerations. Unlike the description, by default a meeting's attendees list get synced continuously, see more information [here](../Calendar-Items-Sync-Special-Patterns-Attendees-Lists%2C-Private-Items%2C-Item-Unsharing-and-Deletion/#continuous_attendees_list_syncing). Private calendar items do not get saved but reserve slots in the Salesforce calendar; read the details in [this article](../Saving-Calendar-Items-in-Salesforce-%28Adaptive-view%29/#saving_private_calendar_items). 

For all in-org (internal) meeting attendees Salesforce creates copies of the synced [Event object](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_objects_event.htm?search_text=event), as child Events under the organizer's parent Event.

Calendar items synchronization is a two-way process, so calendar updates made on either side are mirrored, but there are also optional [one-way syncing options](../Special-Sync-Options-Save-Events-As-Other-%26-One-Way-Sync/#one-way_synchronization) available. [Series of recurring calendar items](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#synchronizing_series_of_recurring_items) also get synchronized by {{ short_name }}.

Not all calendar items can be mirrored in Salesforce, see [this article](../Calendars-Syncing-Exceptions/#in_what_cases_the_calendars_are_not_11_identical) to learn more about the exceptions.

Finally, refer to [this article](../Calendar-Items-Sync-Special-Patterns-Attendees-Lists%2C-Private-Items%2C-Item-Unsharing-and-Deletion/) for specific nuances about various calendar items syncing use cases.

&nbsp;

* * *

&nbsp;

### Optional settings

{{ product_name }} has more ["hidden" settings](../Special-Admin-Panel-Settings/#extra_configuration_settings) used to adjust the patterns applied on [automatic creation of records](../Synchronization-Engine-An-Overview/#automatic_creation_of_contacts_or_leads_by_rg_email_sidebar_autoresolving) for both auto-saved email and calendar items.

In the latest {{ product_name }} updates an augmented [objects auto-resolving](../Synchronization-Engine-An-Overview/#automatic_creation_of_contacts_or_leads_by_rg_email_sidebar_autoresolving) mechanism was added, enabled by the global setting *SalesforceSmartCreateUnresolvedObjects* (disabled by default). How this pattern works:

If there's a match with an attendee's or recipient's/sender's email address domain in: a) an Account's *Website* field and b) email domain of a Contact linked to the Account, {{ short_name }} creates a Contact linked to the Account with this match.

Note that popular personal email domains (*gmail.com*, *outlook.com*, etc.) are excluded from this pattern: no Contacts are auto-created for meetings and emails sent or received from addresses on these domains. If the *Create Person accounts* setting is enabled in [{{ short_name }} global settings](../Special-Admin-Panel-Settings/#extra_configuration_settings) in your configuration, [Person accounts](https://help.salesforce.com/articleView?id=account_person.htm&type=5) are created instead of Contacts. If there's no Account match found to create a linked Contact and Create Person accounts is disabled, then a Lead is auto-created.  

&nbsp;

Another available augmented [objects auto-resolving mechanism](../Synchronization-Engine-An-Overview/#automatic_creation_of_contacts_or_leads_by_rg_email_sidebar_autoresolving), managed by the [global setting](../Special-Admin-Panel-Settings/#extra_configuration_settings) *SalesforceEmailCreateAllUnresolvedRecipients* (disabled by default). How this pattern works: if enabled, Accounts and Leads/Contacts are created for **all** auto-saved incoming and outgoing emails or calendar items for which no matching [Person/Business records](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) are found in Salesforce.

Also refer to [this article](../Special-Admin-Panel-Settings/#auto-create_objects_for_unresolved_meeting_participants_auto-resolving) for information on more optional settings which regulate Calendar items syncing patterns.

&#160;
 &#160;

