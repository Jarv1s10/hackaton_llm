---
description: Tips for using MS Outlook Delegated Calendars
---
# Using MS Outlook Delegated Calendars  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*7 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! tip "Tip"
    Also see [this article](../Delegated-Access-Emails/) to learn how to process emails in {{ product_name }} over Delegated access and [this UVM article](https://www.uvm.edu/it/kb/article/delegate-access/) to learn how to configure and work with Delegated mailbox access

&nbsp;

The Delegated calendars feature allows _Delegates_, {{ product_name }} users with granted delegate access permissions in MS Outlook to view, manage, and [sync in Salesforce calendar](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/) items of other users, calendar _Organizers_ (Delegators), also viewing the contextual Salesforce data about associated records in {{ product_name }}.  

When a meeting or appointment is created, modified, moved, or deleted in delegated access scenario, its associated Salesforce records and Salesforce calendar are updated correspondingly through [{{ short_name }} synchronization](../Synchronization-Engine-An-Overview/), so other concerned individuals in your Salesforce Org can see the changes in the records immediately and react to them.  

Please refer to [this article](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/) for detailed information on how calendar items are processed by {{ product_name }} selectively or automatically.

&nbsp;

* * *
&nbsp;

### Prerequisites and Permissions

Delegated Calendar access and [Delegated Inbox access](../Delegated-Access-Emails/) have the same prerequisites; either of these mailbox data access scenarios or both can be configured if the below prerequisites are met. Handling of MS Outlook Tasks or Contacts by {{ product_name }} <u>via delegated access</u> is currently not supported

- To carry out scenarios through delegated access both involved mail accounts should have {{ short_name }} Add-In installed and [Sync activated](../Synchronization-Engine-An-Overview/). Both accounts should have a [dedicated {{ short_name }} license](https://revenuegrid.com/pricing/)  
- The two accounts should belong to the same MS Exchange instance and Salesforce Org  
- All {{ short_name }} functions are only available if the mailbox Owner (Delegator) [grants Calendar *Editor* permissions](https://support.microsoft.com/en-us/office/allow-someone-else-to-manage-your-mail-and-calendar-41c40c04-3bd1-4d22-963a-28eafec25926) for the Delegate, so it is the recommended permissions level  
- For the feature to work, the Delegate must be using [EWS connectivity](../Working-With-EWS/), **not** [MS Graph](../MS-Graph/)

Also see the section *"Supported {{ short_name }} Actions for Delegated Scenarios for Calendar Items"* below for details on all available use cases.

<br>
***
<br>

### MS Outlook versions that support delegated calendars 

<br>
Delegated Calendars feature is only available to the users of the MS Outlook versions that support [API requirement set 1.8](https://learn.microsoft.com/en-us/javascript/api/requirement-sets/outlook/requirement-set-1.8/outlook-requirement-set-1.8?view=excel-js-preview). *MS Outlook on Windows with a Microsoft 365 subscription* and *a retail one-time purchase MS Outlook* support 1.8 API set starting from the [**Version 1910** (Build 12130.20272)](https://learn.microsoft.com/en-us/javascript/api/requirement-sets/outlook/outlook-api-requirement-sets?view=excel-js-preview&tabs=xmlmanifest#outlook-client-support). 

 <br>
To find out what MS Outlook version you are using, either refer to [this Microsoft Help article](https://support.microsoft.com/en-us/office/about-office-what-version-of-office-am-i-using-932788b8-a3ce-44bf-bb09-e334518b8b19) or follow the instructions provided below    

* Open the Desktop version of MS Outlook, click **File** in the upper left-hand corner of the interface  

* Depending on your version, select **Office Account**, **Account** or **Help** from the list on the left 

* Under **Product Information**, find the information about your MS Outlook version 


<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/product-info.png" class="minimized">
</p>

<br><br>
If you are using an MS Outlook version **older than 1910** or version older than Office 2021, you should consider upgrading to the latest versions to ensure the support of delegated calendars feature in {{ product_name }}.  

<br>
!!! tip "Tip"    
    For more information about your MS Office version, refer to the update history for [Office 2021](https://learn.microsoft.com/en-us/officeupdates/update-history-office-2021) or [Microsoft 365](https://learn.microsoft.com/en-us/officeupdates/update-history-microsoft365-apps-by-date)   

&nbsp;

* * *

&nbsp;

#### Setting Up Delegated Calendar Access in MS Outlook

Please refer to the following Microsoft guides to learn how to set up delegated calendar permissions in MS Outlook and use this feature:

*   [MS Outlook 2016 / 2019 desktop](http://support.office.com/en-us/article/share-an-outlook-calendar-with-other-people-353ed2c1-3ec5-449d-8c73-6931a0adab88)  
*   [MS Outlook on the Web / Office 365](http://support.office.com/en-us/article/calendar-delegation-in-outlook-on-the-web-for-business-532e6410-ee80-42b5-9b1b-a09345ccef1b)  
*   [MS Outlook for Mac](http://support.office.com/en-us/article/become-a-delegate-or-stop-being-a-delegate-in-outlook-for-mac-818da19c-b03c-4a69-926a-76a7c84c3579)  

<br>
The following delegated access permission types are available:  

**Editor:** has full calendar management permissions.  

**Author:** has full calendar management permissions, apart from modifying or processing calendar items created by the Organizer.  

**Reviewer:** this permissions type is insufficient for managing delegated calendars. It only allows viewing calendar entries; no item saving in Salesforce or linking to Salesforce objects is possible with this permissions type.

Managing calendar entries using the delegated calendars feature with {{ product_name }} Add-In requires Author or Editor permissions to be set up: **File > Info tab** **> Account Settings > Delegate Access > Calendar** picklist.

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b7ec4650428631d7a8a4e7f.png)

&nbsp;

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b7daade0428631d7a8a471b.png)

&nbsp;

Delegated calendar permissions can be set up individually: **{MS Outlook Calendar view} > Folder** tab **> Calendar Properties**

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b7dab122c7d3a03f89e0315.png)

&nbsp;

The required permissions level for {{ product_name }} delegated calendars management are **Can edit** or **Delegate**.

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b7ec68d0428631d7a8a4eca.png)

&nbsp;

!!! note "Note"
    The **Delegate can see my private items** or **Can view private events** setting allows a Delegate with Editor or Author permissions to view as well as modify items which the calendar Organizer [marked as private](http://support.office.com/en-us/article/make-an-appointment-or-meeting-private-dc3898f0-22f5-45c6-8cc8-b4d4db84111d). With this setting enabled a Delegate can also remove the _private_ mark from calendar items

&nbsp;

* * *

&nbsp;

#### Setting Up Shared Calendar Access in Salesforce

In order to allow Events in the Organizer's Salesforce calendar to be created or modified by {{ product_name }} via a Delegate's Salesforce account the necessary shared calendar permissions should also be set up in Salesforce. Refer to the following Salesforce help articles to learn how to do that: [article 1](https://help.salesforce.com/articleView?id=calendar_sharing_parent.htm&type=5); [article 2](https://help.salesforce.com/articleView?id=000327324&type=1&mode=1).

&nbsp;

* * *

&nbsp;

#### Delegated Calendar Items Syncing in Salesforce

&nbsp;

To sync a delegated calendar item in Salesforce (initial sharing), you can either assign it the blue Salesforce category in MS Outlook or [find and select](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-(Adaptive-view)/) a relevant existing record and then click the [**Save** button](../Save-Email-Dialog/) at the top of {{ product_name }}. If [{{ short_name }} insta-sync is enabled](../Synchronization-Engine-An-Overview/#instant_sync_of_calendar_items), an item shared this way will be saved in Salesforce instantly. Otherwise it will be saved on the following sync session.  

!!! warning "Important"
    Regardless of who modifies/updates a calendar item, for the changes to be conveyed to Salesforce the item's Organizer must have one's {{ company_name }} synchronization enabled

&nbsp;

&nbsp;

#### Shared Calendar Items Syncing in Salesforce

Items from a shared MS Outlook calendar cannot be synced in a typical configuration; such attempts result in an error notification "Sync is not enabled for Organizer - please try again in 30 minutes and in case you see the same error, contact your Salesforce admin."  
The only way to handle such items is to configure a dedicated [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/) user for the shared calendar and sync items through it. For this scenario: items cannot be in compose more. The shared mailbox Sync user will be treated as the Organizer, the user accessing the shared mailbox will be treated as the Delegate.

&nbsp;

* * *

&nbsp;

### Supported {{ short_name }} Actions for Delegated Scenarios for Calendar Items



|                                                              | Granted  permissions                                         | Available  actions                                           | Salesforce Destination      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | --------------------------- |
| Calendar  access                                             | Delegate + [Calendar permissions Editor](https://support.microsoft.com/en-us/office/allow-someone-else-to-manage-your-mail-and-calendar-41c40c04-3bd1-4d22-963a-28eafec25926)<br />[the only scenario fully compatible with {{ product_name }}] | Manage and process in {{ short_name }} calendar items created by the Owner or the Delegate, as well as inbound meeting invites (on the Owner's behalf)<br />[All saving scenarios in the Calendar](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/) using [{{ product_name }}](../Save-Email-Dialog/) or [custom category](../Saving-Calendar-Items-in-Salesforce-%28Adaptive-view%29/#custom_salesforce_categories_in_ms_outlook)<br /> | Owner’s  Salesforce account |
| Send a meeting invite ([send on behalf of](https://docs.microsoft.com/en-us/microsoft-365/admin/add-users/give-mailbox-permissions-to-another-user?view=o365-worldwide#send-email-on-behalf-of-another-user)) | [Configured as a Delegate](https://support.microsoft.com/en-us/office/allow-someone-else-to-manage-your-mail-and-calendar-41c40c04-3bd1-4d22-963a-28eafec25926) with no special Calendar permissions set | Save created items in [Compose mode](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#2_when_revenue_grid_sync_is_not_active) using [{{ product_name }}](../Save-Email-Dialog/) or [custom category](../Saving-Calendar-Items-in-Salesforce-%28Adaptive-view%29/#custom_salesforce_categories_in_ms_outlook) | Owner’s  Salesforce account |
|                                                              | Delegate  + [Calendar permissions Author](https://support.microsoft.com/en-us/office/allow-someone-else-to-manage-your-mail-and-calendar-41c40c04-3bd1-4d22-963a-28eafec25926) | View Calendar and respond to meeting invites, create meeting invites and process in {{ short_name }} only items created by Delegate using [{{ product_name }}](../Save-Email-Dialog/) or [custom category](../Saving-Calendar-Items-in-Salesforce-%28Adaptive-view%29/#custom_salesforce_categories_in_ms_outlook) | Owner’s  Salesforce account |
|                                                              | Delegate  + [Calendar permissions Reviewer](https://support.microsoft.com/en-us/office/allow-someone-else-to-manage-your-mail-and-calendar-41c40c04-3bd1-4d22-963a-28eafec25926) | No {{ product_name }} actions available, can only view [the Sidebar](../Introduction/) | n/a                         |

 &nbsp;

&nbsp;

* * *

&nbsp;

#### {{ product_name }} Delegated Calendars Access Troubleshooting

Delegated calendars sync issues may occur mainly on initial item sharing in Salesforce, caused by either one of the following issues: {{ company_name }} sync errors, insufficient MS Outlook delegated calendar permissions, insufficient Salesforce permissions.

* Since initial sharing (creation) of events in Salesforce is performed by [{{ company_name }} synchronization](../Synchronization-Engine-An-Overview/), the Organizer's sync must be running for the calendar updates made by a Delegate to be applied in Salesforce. If sync is not running for the Organizer, {{ product_name }} will not be able to save the item created or modified by the Delegate in Salesforce. The corresponding error notification will be displayed that sync is not enabled for the Organizer

  

  ![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b7e87e10428631d7a8a4be2.png)

  &nbsp;

* Once the corresponding Salesforce event record has been created, its further updates and modifications can be performed directly from via the Organizer's or Delegate’s {{ product_name }} Add-In; the changes will be conveyed immediately and will not depend on the sync interval. This way, even if sync is not running for the calendar item Organizer, saving changes to an already existing Salesforce event object can be performed if the Delegate has the permissions to access this event in Salesforce

* If the Delegate does not have the permissions to view the corresponding Salesforce event (however, the Add-In can still obtain the Salesforce event ID from MS Exchange), saving will not be allowed with an error notification that the user has insufficient Salesforce account permissions to save this event

!!! note "Note"
    The same error message is displayed if the event was removed from Salesforce and {{ product_name }} was unable to down-sync this change to MS Exchange 

&nbsp;

* If the Delegate does not have the permissions to modify a corresponding Salesforce event, there will appear an error notification that user has insufficient Salesforce account permissions to update this event, suggesting to contact the Organizer to get the required permissions in Salesforce

&nbsp;

!!! note "Note"
    Delegated calendars also support using the [Send calendar availability](../Sharing-Calendar-Availability-(Adaptive-view)/) and [Send meeting time slots](../How-to-Send-Meeting-Time-Slots-(Adaptive-view)/) features so the Delegate can generate these links for the Delegator's calendar

&nbsp;

* * *

&nbsp;

#### Delegated Calendars and {{ short_name }} Meeting Scheduler

{{ product_name }} features [Time Slots](../How-to-Send-Meeting-Time-Slots-(Adaptive-view)/) or [Calendar Availability](../Sharing-Calendar-Availability-(Adaptive-view)/) can be used for a Delegated access calendar. Generated meeting's formal initiator gets auto-defined based on the content of the *From* field.

The resulting [meeting slots reservation page](../How-to-Send-Meeting-Time-Slots-%28Adaptive-view%29/#how_to_pick_time_slots_recipient_side) also includes an indicator that displays the meeting's actual initiator.  




&#160;
 &#160;

