---
description: How to prevent duplication of items when using RG Email Sidebar
---
# Item Deduplication Mechanisms Explained  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*5 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

Considering the amount of records processed over {{ product_name }}'s different data handling scenarios by multiple end users and the possibility of simultaneous records updating directly in Salesforce, application of deduplication mechanisms is required to keep the data well organized. This article explains these mechanisms.

&nbsp;

### Allow creating email duplicates in Salesforce

This setting is located in the *Email saving settings* area of {{ product_name }} [Customization settings](../Customization-Settings-Explained/) and it is enabled by default. It can be disabled if that is required by your Salesforce use preferences – specifically if you want no Task/Email message duplicates (clones) to be created in your Salesforce.

Salesforce has a [limitation](http://help.salesforce.com/articleView?id=relationships_considerations.htm&type=5) on [WhoId linking](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/): any Activity can be linked to only one object, so in order to get a [Task](https://help.salesforce.com/articleView?id=task_fields.htm&type=5) or [Email Message](https://help.salesforce.com/articleView?id=000239922&type=1) based on your email correspondence linked to multiple objects {{ product_name }} must create its duplicates (clones) in Salesforce. This is the default behavior preferred by most {{ product_name }} users; if you disable this setting to prevent creation of Activity clones in Salesforce, linking of emails to multiple objects will become unavailable: if you link an Email already linked to an object to another object, the first object will be unlinked.
On modifying the email's primary association you will be prompted to replace the current value in the **Name** field of an already existing Task/Email message with the name of the new object you want to associate the email with. For example, if you first save an email linked to a Contact and then try to save it linked a Lead (in this case, “Robert West”), you will see the following notification:

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b1f92dc2c7d3a0fa9a2e0e7.png)

&nbsp;

Additionally, you can adjust the related setting **Allow creating email duplicates to be linked to these object types** to set what object types Task/Email message duplicates are allowed to be created for, instead of disabling creation of duplicated Activities altogether. If you define this limit, less Activity duplicates will be created in Salesforce. The maximum number of clones that an email can have in this scenario is 10.


<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Using-SmartCloud-Connect\email_duplicates.png" class="minimized">
</p></details>



&nbsp;

!!! note "Note"
    If the **Allow creating email duplicates to be linked to these object types** list is left empty, {{ product_name }} will be allowed to create Task or Email message duplicates for linking to all Salesforce object types

!!! warning "Important"
    Please note that if you adjust the duplicate handling settings in {{ product_name }} Customization, for these changes to be applied you must [log out from {{ product_name }}](../How-to-Change-Email-Address-in-Your-Product-Account-Office-365/) and then [re-log in](../How-to-Install-and-Run-the-Solution-all-configurations/#ii_rg_email_sidebar_logon)

&nbsp;

* * *
&nbsp;

### General email deduplication

The **Allow creating duplicated emails in Salesforce** feature is not to be confused with general Email deduplication  always automatically applied by {{ company_name }} synchronization when email business correspondence is [processed and saved in Salesforce](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/). General deduplication prevents creation of redundant clones of the same email by several users within a Salesforce Org.
After a user in an Org sends or receives an email and saves it in Salesforce, another user from the same Org who receives the message will see an indication that the email has already been saved in Salesforce in the header of [{{ product_name }}](../Introduction/) upon selecting it in the email client:

![](../assets/images/Using-SmartCloud-Connect/How-It-Works/email_is_saved.png)

&nbsp;

For example, if an email is received by several users one Org (via the *To:* or *CC:* field) and all of them save the email in Salesforce via {{ product_name }}, only the first instance will be saved and the rest will be referenced to the first one.

The email's current object associations (linking) set by the first user who saved it in Salesforce will be marked in the Sidebar with [green checkmark circles](../All-User-Actions-in-Add-In-Sidebar/#7_automated_selectionunselection_of_records).
If you modify these associations and save the email in Salesforce, {{ product_name }} will create a clone of the corresponding Task/Email Message object that will be linked according to your preferences, also keeping its initial instance with its original linking for other users in your Org.

&nbsp;

&nbsp;

#### Emails Deduplication setup precondition

To enable general deduplication a custom *InternetMessageId* field (it is included in the [{{ company_name }} managed Salesforce package](../Admin-Managed-Package/)) should be added in Salesforce for Task objects and specified in {{ product_name }} Admin panel setting [**Original email ID**](../Special-Admin-Panel-Settings/#reduce_tasks_duplicates). Or, if you are using [Email Messages](https://help.salesforce.com/articleView?id=000239922&type=1) instead of Tasks, the *MessageIdentifier* field should be entered there.

&nbsp;

* * *
&nbsp;
### Contacts, Events, and Tasks deduplication

Besides preventing Email duplicates creation, {{ product_name }} ensures that no duplicated Contacts or Events are created in your Salesforce Org. This deduplication is handled by [synchronization](../Synchronization-Engine-An-Overview/). Contacts duplication is based on the *Email address* field: instead of creating a new instance of a Contact with the same email address on Contacts syncing {{ product_name }} retrieves the existing one from Salesforce.
Events deduplication is applied based on their *Subject*, *Start Date*, and *Organizer* fields matching; it only concerns Salesforce Events which have attendees (meetings/conference calls). Additional rule applied: if the same event is created or updated in MS Outlook and Salesforce at the same time, only the instance created/updated in MS Outlook will be kept, the other instance will be replaced.
Tasks deduplication is applied based on their *Subject*, *Due Date*, and *Owner* fields matching.

&nbsp;

#### Advanced Events deduplication

{{ product_name }} also has an an advanced Events deduplication mechanism. See [this article](../Precondition-for-Enabling-Advanced-Calendar-Synchronization/) to learn the preconditions for enabling it.   
Advanced deduplication implies that on [calendar items syncing](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/) the [Sync engine](../Synchronization-Engine-An-Overview/) checks for possible existing duplicates based on [Salesforce ClientGuid value](https://salesforce.stackexchange.com/questions/80000/where-is-the-event-clientguid-field) instead of the default way, where natural keys (the Event's *Subject* and *Time* values) are used. This enhances deduplication precision.

{{ product_name }} enables this mechanism automatically as soon as [this field is configured for Salesforce Event objects](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_objects_event.htm).


The *Client GUID* field in Salesforce Event object:

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Using-SmartCloud-Connect\guid-salesforce.png" class="minimized">
</p></details>



&nbsp;

* * *
&nbsp;
### Existing record duplicates merging with conflicts resolution

{{ product_name }} also includes a duplicate records merging feature based on Salesforce [contacts](https://help.salesforce.com/articleView?id=contacts_merge_lex.htm&type=5) / [accounts](https://help.salesforce.com/articleView?id=account_merge_lex.htm&type=5) merging mechanism. It is triggered when one or several users in the same Salesforce Org [create](../Create-New-Records/) a lead, contact, or account based on the same email address; it allows selecting a single preferred option between the non-matching values in record fields (conflicts resolution). After you mark the preferred values and click **Merge** the second instance of the record will be deleted from Salesforce and its associated items will be relinked to the resulting correct instance.

![](../assets/images/Using-SmartCloud-Connect/How-To-s/merging.png)
&nbsp;

&#160;
 &#160;

