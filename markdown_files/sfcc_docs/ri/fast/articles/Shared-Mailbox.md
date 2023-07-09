---
description: Learn how RG Email Sidebar works with Exchange shared mailboxes
---
# How the Solution Works with Exchange Shared Mailboxes  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

An [Exchange Shared mailbox](https://docs.microsoft.com/en-us/exchange/collaboration/shared-mailboxes/shared-mailboxes?view=exchserver-2019) is a special kind of mailbox that can be accessed and used by a group of ordinary end users. The group's members can also be enabled to work with email and calendar data stored in the shared mailbox using {{ product_name }} [Add-In](../Introduction/) and [Sync engine](../Synchronization-Engine-An-Overview/), with several limitations.

Exchange Shared mailboxes can be used in the [default "Show from" >  Set Shared mailbox's address manner](https://support.microsoft.com/en-ie/office/access-another-person-s-mailbox-a909ad30-e413-40b5-a487-0ea70b763081) in both MS Outlook Desktop (Windows, MacOS) and [Outlook on the Web](https://en.wikipedia.org/wiki/Outlook_on_the_web) (<http://outlook.live.com>, <https://outlook.office.com>); in the latter case it must be running in a [supported web browser](../Supported-Email-Clients-for-Microsoft-Office-365-%28with-Exchange-Online-plan%29/#browsers) to ensure {{ product_name }} functioning.  
In addition, Outlook on the Web features an alternative shared mailboxes use flow [Open another mailbox in a separate window](https://support.microsoft.com/en-ie/office/access-another-person-s-mailbox-a909ad30-e413-40b5-a487-0ea70b763081) which is incompatible with [{{ short_name }} Add-In](../Introduction/) but allows basic interaction using [{{ company_name }} Sync](../Synchronization-Engine-An-Overview/): via the [custom folder / category](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-%28Adaptive-view%29/#3_besides_using_the_save_button_emails_saving_can_be_performed_in_4_more_easy_ways) or [auto-sync](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_emails_emails_autosharing).

&nbsp;

&nbsp;

#### {{ product_name }} use scenarios available for shared mailboxes



| Function                                                     | Default "Show From" usage mode (Desktop or OWA)              | "Open another mailbox" usage mode (OWA only)                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [Install {{ short_name }} Add-In from AppSource or URL / File](../How-to-Install-and-Run-the-Solution-for-Office-365-Mailboxes/) | Add-In is installed for individual mailboxes connected to the Shared mailbox | Cannot be installed                                          |
| [Save emails by category assigning](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-%28Adaptive-view%29/#3_besides_using_the_save_button_emails_saving_can_be_performed_in_4_more_easy_ways) | Full                                                         | Full; Categorize unavailable for items opened in a dedicated window |
| [Auto-save emails](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_emails_emails_autosharing) | Full                                                         | Full                                                         |
| Working with the Sidebar in [Compose mode](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#1_saving_an_email_when_revenue_grid_synchronization_is_active): [Related records retrieval](../Initial-Search-and-Applied-Record-Filters/#related_records_retrieval_pattern) and [creation](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-%28Adaptive-view%29/#creating_new_records_in_salesforce), [Save button](../Save-Email-Dialog/), [other functions](../All-User-Actions-in-Add-In-Sidebar/) | Full                                                         | Sidebar unavailable                                          |
| Working with the Sidebar in [Read mode](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#1_saving_an_email_when_revenue_grid_synchronization_is_active): [Related records retrieval](../Initial-Search-and-Applied-Record-Filters/#related_records_retrieval_pattern) and [creation](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-%28Adaptive-view%29/#creating_new_records_in_salesforce), [Save button](../Save-Email-Dialog/), [other functions](../All-User-Actions-in-Add-In-Sidebar/) | Full. Limitation: Invalid "Item cannot be saved" indication is displayed for successfully saved items | Sidebar unavailable                                          |
| [Save calendar items by category assigning](../Saving-Calendar-Items-in-Salesforce-%28Adaptive-view%29/#saving_calendar_items_semi-automatically) | Full                                                         | Full; Limitation: *Categorize* unavailable for items opened in a dedicated browser window |
| [Auto-save calendar items](../Saving-Calendar-Items-in-Salesforce-%28Adaptive-view%29/#meeting_appointment_autosaving) | Full                                                         | Full                                                         |
| Working with calendar items via the Sidebar: [Related records retrieval](../Initial-Search-and-Applied-Record-Filters/#related_records_retrieval_pattern) and [creation](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-%28Adaptive-view%29/#creating_new_records_in_salesforce), [other functions](../All-User-Actions-in-Add-In-Sidebar/) | Yes. Limitation: no [Save](../Save-Email-Dialog/) button     | Sidebar unavailable                                          |

&nbsp;

!!! tip "Tip"
    Also see [this article](../Shared-Regular/) to learn how to convert a Shared mailbox to a Regular mailbox, in case that is required for your {{ product_name }} use scenarios

&nbsp;

&nbsp;

### How to configure {{ short_name }} to work with Shared mailboxes

To perform all above listed user actions with items located in Shared mailboxes, the following configuration actions must be performed by the local {{ short_name }} Admin or by [{{ product_name }} Support team](mailto:support@revenuegrid.com):

**1\.** A dedicated Salesforce account should be created for the Shared mailbox, in the same Org as the end users  

**2\.** The Shared mailbox must be [provisioned in {{ product_name }} Admin panel](../Managing-Users-via-the-Solution-s-Admin-Panel/)  

**3\.** The Sync engine must be [activated](../Authorizing-Sync-Engine-to-Work-with-Your-Data/) for the Shared mailbox [via Exchange Impersonation](../Impersonation-O365/)  



&nbsp;

&nbsp;



