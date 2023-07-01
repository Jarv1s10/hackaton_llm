---
description: How to create new Salesfoce records using RG Email Sidebar
---
# Creating New Records via the Sidebar  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*4 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

Via {{ product_name }} [Add-In / Chrome Extension Sidebar](../Introduction/) you can instantly create new records of any type used in your Salesforce Org, [including custom ones](../How-to-Add-A-Custom-Object/).

!!! tip "Tip"
    See [this article](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-(Adaptive-view)/) to learn how to search for existing Salesforce records directly from your email client using {{ product_name }}

&nbsp;

### Creating New Records in Salesforce

!!! note "Note"
    If you do not see a needed type in the Create picklist, make sure that the object is [configured to be handled by {{ short_name }}](../How-to-Add-A-Custom-Object/) and that [**Allow create** is enabled for this object in {{ short_name }} Customization settings](../Customization-Settings-Explained/#6_customizing_object_card_appearance_and_behavior)

&nbsp;

{{ short_name }} Add-In creates business records directly in Salesforce, so this function also works when [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/) is not active for any reason

To create new Salesforce People or Business records, do the following:

**1\.**   Click on the **\+** (Create) icon in the upper right corner of the Sidebar and select the necessary record type from the picklist

<details><summary>>>> Click to see an animation <<<</summary>
<p>
    <img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5bd9949a2c7d3a01757a9c61.gif"style="width: 45%; height: 50%;">
</p>
</details>

&nbsp;

!!! note "Note"
    You can also customize the Add-In / Chrome Extension to add more record types to the picklist, including [custom object types](../How-to-Add-A-Custom-Object/) used in your Org. See [this article](../Customization-Settings-Explained/#66_hiding_record_cards_in_search_results_hide_on_search) for complete information

&nbsp;

**2\.**   Next, in the **Create {record type}** dialog that appears, fill in the required fields. Note that some fields are already prefilled with relevant data from your email message or calendar item. You can also clear the **Show only important fields **checkbox to see all available fields in the record; when the box is selected, {{ product_name }} only shows the fields which are required, marked as Important in Customization settings, or already contain some data in Salesforce.  
    In addition, in this dialog you can set the record's Owner in Salesforce, this way assning new records to other people in your team, if needed  

<details><summary>>>> Click to see a screenshot <<<</summary>
<p>
    <img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5bab7c132c7d3a04dd5afb92.png" class="minimized">
</p>
</details>
&nbsp;

**3\.**   Click **Create** to save the record to Salesforce. If you want to immediately see this record as a card in {{ product_name }}, click the **{{ product_name }} logo** to refresh the Sidebar

&nbsp;

!!! tip "Tip"
    {{ product_name }} can optionally auto-fill the *Address* field for new created Contacts based on their associated Account's Address. This function can be enabled through a corresponding request sent to [our Support team](mailto:support@revenuegrid.com)

&nbsp;

!!! note "Note"
    If you create a record that requires Account linking, such as a Contact or Opportunity, and there is no relevant Account registered in your Org which you could put in created record's **Related To** field, you can create one directly, right from the same dialog:  
    ![](../assets/images/Using-SmartCloud-Connect/How-To-s/create-acc.png)

&nbsp;

&nbsp;

### An alternative records creation method

**1\.**   On the Home page, hover the cursor over the needed tab (record category); the **•••** (More) icon will appear. Click on the icon and select **New {Record type}**

<details><summary>>>> Click to see an animation <<<</summary>
<p>
    <img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5b361c220428630abc0b8d8b.gif"style="width: 45%; height: 50%;">
</p>
</details>
&nbsp;
Next, folow the steps **2.** and **3.** described above.

&nbsp;


&nbsp;

!!! warning "Important"
    On creating or modifying an Opportunity record or any other object that has a _Date_ field, fill in this field <u>only</u> in the following way: click the **📅 Calendar** icon next to the field and pick the date in the pop-up selector. Please do not click on the field afterwards, or the Date you selected will not be accepted by the Sidebar

&nbsp;
!!! note "Note"
    If you create a Salesforce Event in this dialog, it may appear in your MS Outlook or Gmail calendar as an Appointment rather than a meeting. See [this article](../Create-New-Event/) for complete information


&nbsp;

&nbsp;

### Creating Person Accounts

Note that to be able to create and manage [Salesforce Person Accounts](https://help.salesforce.com/articleView?id=account_person.htm&type=5) via {{ short_name }} Add-In, you need to [enable a corresponding checkbox in {{ short_name }} Customization settings](../Customization-Settings-Explained/#62_specifying_card_sort_order).

&nbsp;

&nbsp;

* * *

&nbsp;

&nbsp;

### The Suggested Records Tab

If you receive, compose, or send a message or meeting invitation from/to an email address that has no matching Lead, Contact or Account record registered in your Salesforce Org (an unresolved sender/recipient), {{ product_name }} will prompt you to select how to handle this email address via the **Suggested new records** Sidebar tab which appears only when a messages containing unresolved email addresses is selected in your mailbox or composed. In this tab, you can create an Account, Contact, or Lead record based on this address - its key fields of the record will be prefilled with corresponding information retrieved from the message, or [mark the email address or domain as blocklisted from saving in Salesforce](../Initial-Search-and-Applied-Record-Filters/#internal_emails_corporate_domains_and_the_blocklist) by clicking **Do not sync**. Note that this choice can be undone either right from this tab by clicking the **Undo** button or later via [the blocklisted Domains synchronization setting](../Configuring-Activities-Synchronization-Settings/#blocklisting_emails_and_domains).

<p>
    <img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5bc7562f042863158cc78b0a.png">
</p>



&nbsp;

!!! tip "Tip"
    In addition, {{ product_name }} can create matching Leads or Contact automatically (autoresolving), if the corresponding setting is enabled for your Org. Refer to [this article](../Synchronization-Engine-An-Overview/#automatic_creation_of_contacts_or_leads_by_rg_email_sidebar_autoresolving) for more information about this feature



&#160;
 &#160;

