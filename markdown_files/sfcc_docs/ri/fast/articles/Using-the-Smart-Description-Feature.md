---
description: Complete guide on using the Smart Description feature with Events, Contacts, Tasks, and Custom objects
---
# Using the Smart Description Feature with Events, Contacts, Tasks, and Custom objects  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! tip "Tip"
    Smart Description is an additional feature that can be enabled at a request sent to {{ short_company_name }} Support team. A related feature readily available in standard {{ product_name }} configuration - [adding a quick memo](../Record-Description-and-Add-Quick-Memo/)

&nbsp;

{{ product_name }} can fetch the content of any target field of a Salesforce object, including [custom ones](https://help.salesforce.com/articleView?id=dev_objectedit.htm&type=5), and automatically insert it into a chosen text field of a Meeting, Contact, or Task MS Exchange / Office 365 or Gmail item; the *Description* field, for example. This mechanism makes retrieval of needed data from standard as well as [custom added fields](https://help.salesforce.com/articleView?id=customize_customfields.htm&type=5) convenient and flexible, thus unlocking implementation of various custom solutions for smart target Salesforce data displaying or appending to items' fields shown in MS Outlook.

!!! note "Note"
    Retrieval of smart description fields values works only [one-way](../Special-Sync-Options-Save-Events-As-Other-&-One-Way-Sync/#one-way_synchronization), from Salesforce to MS Exchange / Office 365 or Gmail, thus any changes you may make in a text field containing smart description data in your email client will **not** be up-synced to Salesforce and will be overwritten on the following sync session, replaced by the field's content fetched from Salesforce afresh

&nbsp;

An example of the Smart Description feature application is automatic appending a Contact's *phone number*, *position*, *organization's address*, or any details contained in a Contact's standard or custom fields, to the Description of a Meeting scheduled with this Contact, to make it more informative and thus faster to process. 

The following delimiter is used to separate appended smart description data from the field's original content: *++++++++++++++++++++++++++++++++++*

A sample MS Outlook meeting with appended smart description data from Salesforce:

<p><img src="../../assets/images/Using-SmartCloud-Connect/How-It-Works/appointment_sample.png" class="minimized">
</p>

&nbsp;

!!! warning "Important"
    Please note that when some informative Smart description details are appended to a meeting's Description, they may also be seen by the corresponding Meeting's attendees, including the external ones, e.g. the customers, so be considerate about what sensitive information can be included in an Event's Smart description. See [this article](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#calendar_item_description_field_updating_safe_description) for more details

&nbsp;

Similarly, a Task's or Contact's fields filling in MS Outlook or Gmail can be enhanced by automatic addition of extra details contained in any relevant objects' standard or custom fields, while their Notes field can be used by {{ short_name }} Sync for target Salesforce data displaying according to end users' preferences, in addition to what is displayed in the [Add-In (Sidebar)](../Introduction/) .

To enable the Smart Description feature for your Org, [contact us](mailto:support@revenuegrid.com) with a corresponding request specifying:

* object fields which you want to retrieve data from
* target text fields to which it should be added



&#160;
 &#160;

