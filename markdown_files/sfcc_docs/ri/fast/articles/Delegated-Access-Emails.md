---
description: How to work with emails via Exchange delegated access
---
# Working with Emails via Exchange Delegated Access  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! tip "Tip"
    Also see [this article](../Using-MS-Outlook-Delegated-Calendars/) to learn how to work with MS Exchange Delegated calendars

&nbsp;

!!! tip "Tip"
    Also see [this UVM article](https://www.uvm.edu/it/kb/article/delegate-access/) to learn how to configure and work with Delegated mailbox access

&nbsp;

MS Exchange Delegated (Shared) email access allows _Delegates_ – {{ product_name }} users with granted delegate access permissions – to read, compose, and save in Salesforce MS Outlook emails on behalf of actual mailbox *Owners* (Delegators), also viewing the contextual data from Salesforce about associated records in {{ product_name }}.  

When an email is processed in this scenario, its associated Salesforce records are updated correspondingly, so other concerned individuals in your Salesforce Org can see the changes in the records immediately and react to them. By default, only emails from the *Inbox* folder of the Owner can be viewed and processed.

Presently, the feature only works over [EWS](../Working-With-EWS/), but not [MS Graph](../MS-Graph/).

Also refer to [this article](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/) for detailed information on how to save emails in Salesforce selectively and automatically over {{ product_name }}.

&nbsp;

* * *
&nbsp;

### Prerequisites and Permissions

Delegated mailbox access and [Delegated calendar access](../Using-MS-Outlook-Delegated-Calendars/) have the same prerequisites; either one of these access scenarios or both can be configured if the below prerequisites are met. Handling of MS Outlook Tasks or Contacts by {{ product_name }} <u>via delegated access</u> is currently not supported.

- To carry out scenarios through delegated access both involved mail accounts should have {{ short_name }} Add-In installed and [Sync activated](../Synchronization-Engine-An-Overview/), as [two separate {{ short_name }} licenses](https://revenuegrid.com/pricing/)  
- The two accounts should belong to the same MS Exchange instance and Salesforce Org  
- All {{ short_name }} functions are only available if the mailbox Owner (Delegator) [grants Inbox *Editor* permissions](https://support.microsoft.com/en-us/office/allow-someone-else-to-manage-your-mail-and-calendar-41c40c04-3bd1-4d22-963a-28eafec25926) for the Delegate, so it is the recommended permissions level

<details><summary>>>> Click to see a screenshot <<<</summary>
<p>
    <img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Delegate-Access\delegate-permissions.png">
</p></details>
&nbsp;

Also see the section *"Supported {{ short_name }} Actions for Delegated Scenarios for Emails"* below for details on all available use cases.

<br>
***
<br>

### MS Outlook versions that support delegated mailbox access 

<br>
Delegated mailbox access is only available to the users of the MS Outlook versions that support [API requirement set 1.8](https://learn.microsoft.com/en-us/javascript/api/requirement-sets/outlook/requirement-set-1.8/outlook-requirement-set-1.8?view=excel-js-preview). *MS Outlook on Windows with a Microsoft 365 subscription* and *a retail one-time purchase MS Outlook* support 1.8 API set starting from the [**Version 1910** (Build 12130.20272)](https://learn.microsoft.com/en-us/javascript/api/requirement-sets/outlook/outlook-api-requirement-sets?view=excel-js-preview&tabs=xmlmanifest#outlook-client-support). 

 <br>
To find out what MS Outlook version you are using, either refer to [this Microsoft Help article](https://support.microsoft.com/en-us/office/about-office-what-version-of-office-am-i-using-932788b8-a3ce-44bf-bb09-e334518b8b19) or follow the instructions provided below    

* Open the Desktop version of MS Outlook, click **File** in the upper left-hand corner of the interface  

* Depending on your version, select **Office Account**, **Account** or **Help** from the list on the left 

* Under **Product Information**, find the information about your MS Outlook version 


<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/product-info.png" class="minimized">
</p>

<br><br>
If you are using an MS Outlook version **older than 1910** or version older than Office 2021, you should consider upgrading to the latest versions to ensure the support of delegated mailbox access in {{ product_name }}.  

<br>
!!! tip "Tip"    
    For more information about your MS Office version, refer to the update history for [Office 2021](https://learn.microsoft.com/en-us/officeupdates/update-history-office-2021) or [Microsoft 365](https://learn.microsoft.com/en-us/officeupdates/update-history-microsoft365-apps-by-date)   

&nbsp;


&nbsp;

* * *

 &nbsp;

### Supported {{ short_name }} Actions for Delegated Scenarios for Emails

Delegated email access can be used in two different modes, Compose new email mode ([*Send on behalf of*](https://docs.microsoft.com/en-us/microsoft-365/admin/add-users/give-mailbox-permissions-to-another-user?view=o365-worldwide#send-email-on-behalf-of-another-user) or *Inbox access* with different sets of permissions

&nbsp;

|                                                              | Granted  permissions                                         | Available {{ short_company_name }} actions                                         | Salesforce Destination      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | --------------------------- |
| Inbox access                                                 | Delegate  + [Inbox permissions  Editor](https://support.microsoft.com/en-us/office/allow-someone-else-to-manage-your-mail-and-calendar-41c40c04-3bd1-4d22-963a-28eafec25926)<br />[the only scenario fully compatible with {{ product_name }}] | Manage and process in {{ short_name }} any emails in Owner’s Inbox folder or in [Compose mode](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#2_when_revenue_grid_sync_is_not_active): all saving scenarios [using the Sidebar](../Save-Email-Dialog/) or [the custom folder/category](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#3_besides_using_the_save_button_emails_saving_can_be_performed_in_4_more_easy_ways) | Owner’s  Salesforce account |
| Compose  new mode ([send on behalf of](https://docs.microsoft.com/en-us/microsoft-365/admin/add-users/give-mailbox-permissions-to-another-user?view=o365-worldwide#send-email-on-behalf-of-another-user)) | [Configured as a Delegate](https://support.microsoft.com/en-us/office/allow-someone-else-to-manage-your-mail-and-calendar-41c40c04-3bd1-4d22-963a-28eafec25926) with no special Inbox permissions set | Save emails in [Compose mode](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#2_when_revenue_grid_sync_is_not_active) using [{{ product_name }}](../Save-Email-Dialog/) or [custom folder/category](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#3_besides_using_the_save_button_emails_saving_can_be_performed_in_4_more_easy_ways) | Owner’s  Salesforce account |
| Inbox access                                                 | Delegate  + [Inbox permissions Author](https://support.microsoft.com/en-us/office/allow-someone-else-to-manage-your-mail-and-calendar-41c40c04-3bd1-4d22-963a-28eafec25926) | View Inbox emails or create and manage created emails; process in {{ short_name }} **only** Inbox emails the Delegate sent to the Owner oneself [using the Sidebar](../Save-Email-Dialog/) or [the custom folder/category](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#3_besides_using_the_save_button_emails_saving_can_be_performed_in_4_more_easy_ways) | Owner’s  Salesforce account |
| Inbox access                                                 | Delegate  + [Inbox permissions Reviewer](https://support.microsoft.com/en-us/office/allow-someone-else-to-manage-your-mail-and-calendar-41c40c04-3bd1-4d22-963a-28eafec25926) | No {{ product_name }} actions available, can only view [the Sidebar](../Introduction/) | n/a                         |


&nbsp;

&nbsp;



