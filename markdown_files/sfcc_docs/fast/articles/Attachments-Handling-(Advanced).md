---
description: Detailed overview of attached files handling mechanisms (for admins)
---
# Attached Files Handling Mechanisms (Admin level article)  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*3 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

This Admin-level article contains information that is useful mostly for local {{ product_name }}/Salesforce admins; please refer to the [Overview article](../Attachments-Handling-(Basic)/) for general information on how attached files are saved in Salesforce and to [this article](../Customization-Settings-Explained/#9_configure_attachments_saving_in_salesforce) to learn how to set up attachments saving in {{ product_name }} Customization.

&nbsp;

#### Preconditions for attachments saving as Content documents ([Salesforce Admin settings](../How-to-Log-In-to-the-Admin-Panel/))

- the setting *Salesforce CRM Content User* must be enabled for the Salesforce user (see below)
- the corresponding settings should be enabled by [{{ company_name }} support team](mailto:support@revenuegrid.com)
- the email containing the attachment has not been [deduplicated](../Customization-Settings-Explained/#3_handling_duplicates)

&nbsp;

* * *

#### Salesforce Content document files

The [Salesforce CRM Content](https://help.salesforce.com/articleView?id=collab_admin_crm_content.htm&type=5) functionality can be enabled in [Salesforce Setup](https://help.salesforce.com/articleView?id=basics_nav_setup.htm&type=5):

![](../assets/images/Using-SmartCloud-Connect/How-It-Works/Handling-Email-Attachments/sf_enable_content_docs.png)
&nbsp;


There is also a separate setting applied for individual users, *Salesforce CRM Content User*:

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-It-Works\Handling-Email-Attachments\SF_content_user.png" class="minimized">
</p>

&nbsp;


!!! warning "Important"
    Please note that Salesforce sets special [access rules](http://help.salesforce.com/articleView?id=collab_files_settings_perms.htm&type=5) for content documents; users (including users with [*View All Data* permission](http://help.salesforce.com/articleView?id=users_profiles_view_all_mod_all.htm&type=5)) can only query files they have access to:
    1. all Salesforce CRM Content files in libraries they are  members of and in their personal library, regardless of the library's permissions.
    2. all Salesforce files they are Owners of - posted on their profile, posted on groups they can see, and shared directly with them

!!! tip "Tip"
    Also refer to [this article](../Special-Admin-Panel-Settings/#linking_email_attachments_to_salesforce_business_objects_besides_the_taskemail_message_object) to learn how to enable linking of attachments saved in Salesforce to other Business records besides Salesforce Tasks/Email messages, via the *Related to* field

&nbsp;

* * *
&nbsp;

#### Salesforce attachments

When a new *Attachment* is added, the following fields are auto-populated:

- *Name* is filled with attachment name
- *Body* is filled with attachment body
- *ContentType* is filled with the attachment's type
- *ParentId* is filled with the ID of created Task object

In addition, a new created *Attachment* supports default record fields.

&nbsp;

* * *
&nbsp;

#### Limitations

Some users in an Org may not be synchronized through the system. In  this case, the identity will not be known, but they are users of Salesforce. Currently, the functionality supports only the specified  identities. The algorithm of user search by email from actors fields  will be implemented additionally.

In rare case, it may need to link more than 100 objects with a *ContentDocument* at once, which exceeds the file share limit. To avoid this, the algorithm will exclude some links, but *Tasks* will be linked at first (see warning in log: *Unexpected  case for shared content '\<attachment name\>' (\<attachment  checksum\>) - \<amount ignored links\> required links will be  ignored*).

&nbsp;

* * *
&nbsp;

#### DocuSign

{{ product_name }} effectively integrates with DocuSign document storage and can save or retrieve attachments from it. See [this article](../How-to-work-with-DocuSign-Document-Storage-via-the-Sidebar/) for more information.

&nbsp;

* * *
&nbsp;

#### Extra adjustments

From [Admin panel](../How-to-Log-In-to-the-Admin-Panel/) you can define which file extensions are allowed to be auto-saved in Salesforce along with an email/event (extensions allow-list):

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-It-Works\Handling-Email-Attachments\whitelist.png" class="minimized">
</p>

&nbsp;
!!! note "Note"
    Please note that attached files with non-allow-listed extensions can still be saved in Salesforce [manually](../All-User-Actions-in-Add-In-Sidebar/#8_more_convenient_email_event_attachments_saving), if the file's size is below the 25 Mb limit

In addition there are more related adjustments which can be enabled on request sent to [our Support team](mailto:support@revenuegrid.com):

- force-saving of files as Attachment objects instead of Content documents  
- auto-saving of files attached to events along with the events  
- set file extensions which should never be auto-saved in Salesforce, e.g. *.exe* or *.bat* files  
- set maximum size of individual files allowed to be auto-saved in Salesforce, to prevent auto-saving of oversized files  
- set minimum size of individual files allowed to be auto-saved in Salesforce, to filter from saving irrelevant small files, for example tiny images from email signatures; this filter is applied to specific file extensions  
- enable/disable Task/Email message object linking to a relevant Opportunity object on email/event auto-saving  
- enable/disable linking of attached files saved as Content documents to related Business records besides the Task/Email message object on email/event auto-saving  
- [autoresolving](../Synchronization-Engine-An-Overview/#automatic_creation_of_contacts_or_leads_by_rg_email_sidebar_autoresolving): automatic creation of Lead or Contact objects in Salesforce for saving emails/calendar items sent to or received from contacts not registered in Salesforce (unresolved recipients/senders), if the email or calendar item gets saved by assigning it the custom *Salesforce* category or moving it to the *Salesforce emails* folder  
- [linking of attachments saved in Salesforce to other Business records besides Salesforce Tasks/Email messages](../Special-Admin-Panel-Settings/#linking_email_attachments_to_salesforce_business_objects_besides_the_taskemail_message_object), via the *Related to* field  



&#160;
 &#160;

