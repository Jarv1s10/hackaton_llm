---
description: Detailed overview of Customization Settings in RG Email Sidebar
---
# {{ product_name }} Customization Settings Explained


<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*13 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! note "Note"
    Some Customization features require adding certain auxiliary fields and classes to Salesforce objects; to get them added automatically ask your local Salesforce administrator to install the [{{ company_name }} managed package](../Admin-Managed-Package/) in your Org – it will enable the full scope of {{ short_name }} features on Salesforce side

&nbsp;  

In the latest {{ short_name }} updates Customization page was converted to a tab in {{ company_name }} web platform; its look and functions remained the same.

<p>
    <img src="..\..\assets\images\Configuration-&-Settings\User-Settings\Customization\New-UI\customization.png" class="minimized">
<br>
</p>

&nbsp;

{{ product_name }} Customization page allows the individual users to adjust various aspects of interaction between Salesforce and {{ short_name }} Outlook Add-In / Chrome Extension. This includes viewing, processing, and search patterns for different types of objects and their fields, see the left and central panes of the page.

Also, here you can adjust the appearance and various functional settings of {{ product_name }} for individual users, using the controls on the right pane of the page.

&nbsp;

!!! tip "Tip"
    After adjusting customization settings make sure to click **Save** in the upper right corner of the page to apply the changes  
    ![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/save-button.png)

&nbsp;

!!! warning "Important"
    To discard any recent changes you made, you can click **Discard changes**. However, once an updated customization is saved by clicking the **Save** button, you can only **Reset to [default settings](../Managing-Email-Sidebar-Customizations/#default_customization_settings)**, so no other previous sets of settings can be restored

&nbsp;

!!! note "Note"
    Since [some {{ short_name }} Outlook Add-In features](../Using-the-Solution-for-Salesforce-and-Gmail/#differences_between_the_exchangeoffice_365_add-in_implementation_and_the_chrome_extension_for_gmail) are not available in [{{ short_name }} Chrome Extension](../How-to-Set-Up-the-Chrome-Extension-for-Salesforce-and-Gmail/), their associated settings cannot be managed in {{ short_name }} Customization settings of {{ short_name }} implementation for Gmail

&nbsp;

* * *

&nbsp;

### **1\. How to Open Customization Page**

<p>
    <img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/open-customization.png" style="width: 40%; float: right;margin-left:2%;">
</p>
Click the **☰** (Menu) button in the header of [{{ product_name }}](../Introduction/) and then select **Customization** to open {{ product_name }} Customization settings page in your web browser.

<br><br>


&nbsp;

* * *

&nbsp;

### **2\. Application Settings**

The controls in the right pane of Customization page enable you to adjust the range of settings defining various aspects of the Add-In’s / Chrome Extension’s behavior.


Refer to [this article](../Application-Settings/) for complete information on **Application Settings** in **{{ short_name }} Customization Settings**.


&nbsp;

* * *
&nbsp;

### **3\. Duplicates for Objects Linking**

Refer to [this article](../Item-Deduplication-Mechanisms/) for complete information on the **Allow creating duplicated emails in Salesforce** setting and the **Allow creating email duplicates to be linked to these object types** field which makes this setting more flexible.

Also see [this article](../Activities-Linking/) for information on objects linking mechanics.

!!! warning "Important"
    Please note that if you adjust the duplicate handling settings, for these changes to be applied you must [log out from {{ product_name }} Add-In](https://docs.revenuegrid.com/ri/fast/assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b3a275f0428630abc0ba0da.png) and then [re-log in](../How-to-Install-and-Run-the-Solution-all-configurations/#ii_rg_email_sidebar_logon)

&nbsp;

* * *

&nbsp;

### **4\. Defining Record Associations (Smart Linking)**

In {{ short_name }} Customization settings, you can adjust Add-In / Chrome Extension behavior when it [processes new emails or events](../Initial-Search-and-Applied-Record-Filters/).

Refer to [this article](../Defining-Record-Associations-%28Smart-Linking%29/) for complete information on Defining Record Associations.

&nbsp;

* * *
&nbsp;

### **5\. Choosing a Set of Salesforce Objects to Display**

!!! note "Note"
    In case your Org uses custom object types, refer to [this article](../How-to-Add-A-Custom-Object/) to learn how to configure their handling in {{ product_name }}

&nbsp;

To change the set of Salesforce objects handled via [{{ product_name }}](../Introduction/), by enabling object types in the left pane:   

**5.1\.** Use the **Quick Find** field to search for the needed Salesforce object

<p>
    <img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\quick-find.gif">
</p>

&nbsp;

**5.2\.** After an object is selected, its object card will appear in the central pane *Objects in {{ product_name }}*. If necessary, adjust the fields and settings on the card to customize how this object will be handled

<p>
    <img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\objects-in-rg.gif">
</p>

&nbsp;

!!! warning "Important"
    To ensure the proper functioning of the {{ short_name }} Add-In, **at least one object should be selected in the Objects in Salesforce** list. If no object is selected, the [Save button in the Sidebar will grey out and become unclickable](../save-button-greyed-out/), and you will not be able to save any emails or events

&nbsp;

&nbsp;

* * *

&nbsp;

### **6\. Customizing Object Card Appearance and Behavior**

You can set up how object cards appear and behave in {{ product_name }} by making the following adjustments on the **Customization** page (the central column _Objects in {{ product_name }}_). These settings are defined specifically for every object type enabled in {{ product_name }} handling scope; note that some custom objects require [additional configuring](../How-to-Add-A-Custom-Object/) to [be handled](../How-to-Add-A-Custom-Object/) by {{ product_name }}.

&nbsp;

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**6.1.** **Selecting which fields to show**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;You can have up to four object fields shown on an unexpanded card. To define which fields to show, pick the needed field names in the list; to remove an unneeded field use the **X** icon.

<p>
    <img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/card-preview.png">
</p>

&nbsp;

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**6.2.** **Specifying card sort order**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use the **Sort by** picklist to set the order in which object cards will appear on the [Sidebar's home screen](../Introduction/) or in search results.

<p>
    <img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/card-sort-by.png">
</p>

&nbsp;

&nbsp;

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**6.3.** **Defining the search/view scope**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;To get focused results, {{ product_name }} Add-in applies custom [Salesforce views (filters)](http://help.salesforce.com/articleView?id=listviews_parent.htm&type=5) when [searching for records](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-%28Adaptive-view%29/#searching_for_records_in_salesforce_user-initiated_search), and you can specify which filter you want to be applied for every object type, by selecting them in the **Global search filter** picklist.

<p>
    <img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/card-glob-filter.png">
</p>

&nbsp;

For example, if you want {{ product_name }} to search only among the Accounts created by you, set *My Accounts* in the picklist opened for the Accounts type in Customization page's central pane 

!!! tip "Tip"
    Besides the pre-set views you can add your own [custom created Salesforce views](https://help.salesforce.com/articleView?id=customviews.htm&type=5) – {{ product_name }} will automatically take up all custom list views you create in Salesforce

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Besides this general scope focusing mechanism, you can also set additional filtering to be applied on handling of specific types of records in the Sidebar, using the **Contextual search filter** setting.

<p>
    <img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/card-context-filter.png">
</p>

&nbsp;

Contextual search filter also uses pre-set or custom created views, to focus Related and searched for records in the Sidebar, based on specific field values criteria, e.g. *Status*, *Created date*, *Priority*, etc. For example, if the *Default {{ product_name }}* filter is set for Opportunity objects, only non-closed Opportunities are shown and handled by {{ short_name }}, but if you want to make this scope focused according to your needs, you can [create your own view according to your preferences](http://trailhead.salesforce.com/en/content/learn/modules/lex_customization/lex_customization_list) and apply it.

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The animation below demonstrates how to change the view filters for different object types

<p>
    <img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\global-context-filters.gif" class="minimized">
</p>

&nbsp;

&nbsp;

#### Default {{ product_name }} filters

There is a selection of pre-set Global view filters available for every object type that suit various records filtering needs, most of them are the [standard pre-set Salesforce views](https://trailhead.salesforce.com/content/learn/modules/lightning-experience-for-salesforce-classic-users/work-with-list-views), but some are peculiar to {{ product_name }}. In the latter case, to see a default filter's criteria hover the mouse over it in the picklist.

!!! warning "Important"
    Note that the default {{ product_name }} filters are not the same as the Default filters you use in Salesforce. In addition, for some types like Email messages or Tasks the default Contextual search selection is *Do not search*

&nbsp;

The table of object type-specific Default {{ product_name }} filters' parameters for your reference:



| Object type      | Default Global filter parameters                             | Default Contextual filter value |
| ---------------- | ------------------------------------------------------------ | ------------------------------- |
| EmailMessage     | All [EmailMessages](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-%28Adaptive-view%29/#11_emails_saved_as_emailmessages_vs_emails_saved_as_tasks) created no more than 100 days in the past | *Do not search*                 |
| Task             | All [Tasks](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-%28Adaptive-view%29/#11_emails_saved_as_emailmessages_vs_emails_saved_as_tasks) created no more than 100 days in the past | *Do not search*                 |
| Event            | All Events created no more than 365 in the past or scheduled within 100 days in the future | *Do not search*                 |
| Attachment       | All Attachments                                              | *Do not search*                 |
| Content document | All Content documents                                        | *Do not search*                 |
|                  |                                                              |                                 |
| Account          | All Accounts                                                 | *n/a*                           |
| Lead             | All Leads not converted to Contacts                          | *n/a*                           |
| Contact          | All Contacts                                                 | *n/a*                           |
| Case             | Only non-closed Cases created no more than 90 days in the past | user defined                    |
| Opportunity      | Only non-closed Opportunities whose Closing date is due no more than 365 days in the past or in the feature | user defined                    |
| User             | Only Active users in the Org                                 | *n/a*                           |
| Product          | All Products                                                 | *Do not search*                 |
| Price book       | All Price books                                              | *Do not search*                 |

&nbsp;

!!! warning "Important"
    Both [user-initiated search](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-(Adaptive-view)/#searching_for_records_in_salesforce_adaptive_view) and [initial search](../Initial-Search-and-Applied-Record-Filters/) results are affected by this filter. To avoid confusion, refer to [this article](../Initial-Search-and-Applied-Record-Filters/#additional_notes_on_the_global_search_filter_setting) for special considerations about using this filter

&nbsp;

&nbsp;

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**6.4.** The **Search by** list

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This customization setting allows to define what object fields are used both when {{ product_name }} [retrieves existing associated records](../Initial-Search-and-Applied-Record-Filters/) and when [you are searching for a certain record](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-(Adaptive-view)/) of this type. Refer to [this article](../Using-the-Search-by-List-Customization-Setting/) to learn how to use this setting.

<p>
    <img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/card-search-by.png">
</p>

&nbsp;

&nbsp;

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**6.5.** **Allow creating or updating records**

Select the **Allow create** or **Allow update** checkboxes to allow selected card type objects to be created or updated, respectively, via record cards.

<p>
    <img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/allows.png">
</p>

!!! warning "Important"
    This checkbox is completely unrelated to Salesforce permissions – it only adds an additional permissions level within {{ product_name }}. For example, if a user is not allowed to create or update **Lead** records in Salesforce, one will not be able to create or update these records regardless of this setting's status  

&nbsp;

!!! note "Note"
    The Account type opened in the central pane has an additional setting **Allow create Person Accounts**, which is displayed if [Salesforce Person Accounts](https://help.salesforce.com/articleView?id=account_person.htm&type=5) are enabled in your Org. When enabled, this setting allows Person Accounts to be [created via {{ short_name }}](../Create-New-Records/)
    <p>
        <img src="..\..\assets\images\Configuration-&-Settings\User-Settings\Customization\allow-pa.png">
    </p>

&nbsp;

&nbsp;

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**6.6.** **Hiding record cards in search results (Hide on search)**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;You can select object types not to be displayed in {{ product_name }} search results. Enabling this setting also removes selected object types from [related records list](../Initial-Search-and-Applied-Record-Filters/).

<p>
    <img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5b2a09a02c7d3a0fa9a3335c.gif" class="minimized">
<br>
</p>

&nbsp;

* * *

&nbsp;

### **7\. Changing Card Order and Pinning Cards**

You can adjust the cards' order in the Sidebar by either dragging them in the list or by clicking the **•••** (More) icon in a card's upper right corner and moving the cards to the top or the bottom of the list.

<p>
    <img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets/57398d2e903360669faf1f0a\images\5b23b9230428632c466aeee7.gif">
</p>

&nbsp;

!!! note "Note"
    The category tabs (section, separators) order can also be adjusted directly on {{ product_name }}'s Home screen: hover the mouse over an items category, e.g. Activity Timeline, then click the **•••** (More) icon that appears on the right-hand side and then select either *Move tab to Top* or *Move tab to Bottom*

&nbsp;

&nbsp;

You can pin object type cards to keep their category tabs (sections, separators), including the *Suggested New Records* tab, constantly displayed in the Sidebar, even if {{ product_name }} cannot retrieve related items of that type from Salesforce.  
To do that, find the item type's card in the central pane and toggle the **📌** (Pin) icon the card's upper right corner.

!!! tip "Tip"
    The set of cards recommended for pinning pin besides all Salesforce record types handled in your company: Activity Timeline, Tasks, Events, Emails. That ensures that their category tabs (sections, separators) are available even for a new Salesforce account that contains no such records

&nbsp;

For example, if the **Case** card is not pinned and no Case related to selected email or calendar item is found in Salesforce, this object category will not be displayed in the Sidebar.  

<p><img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\pin-card.png">
</p>

&nbsp;

* * *

&nbsp;

### **8\. Customizing Detailed Card View**

In addition, via the page's central pane, you can define which record fields will be handled as **Important**. Important fields are listed for viewing and editing in an object's card, as well as in the [Create new {record type}](../Create-New-Records/) dialog and the [Save email / Save event dialog](../Save-Email-Dialog/).

To expand all Important fields of the object, click **Show more record fields** below the showed fields. To display all record fields, click the **\>** (Expand) icon in a record card's header to open the detailed object card, where you also can view and edit all the fields.

<p>
    <img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/more-fields.png">
</p>

&nbsp;

!!! warning "Important"
    Please note that a field is also handled as **Important** if it is set to be auto-prefilled with data (when viewed in the [create a new record in Salesforce dialog](../Create-New-Records/))

&nbsp;

To customize the detailed view, do the following:

**8.1\.** On the Customization page, click **Detailed view** for an object's card.

<p>
    <img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/object-card.png">
</p>

&nbsp;

**8.2\.** Click the field you want to add to the card. You can use the **Filter** field to search for Salesforce fields that are not currently enabled in the Sidebar.

<p>
    <img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/detailed-view.png">
</p>

<details><summary>>>> Click to view details <<<</summary>
<p>
    <b>1.</b> Save or Discard changes<br>
    <b>2.</b> Mark fields as <em>Important</em>, <em>Force Required</em>, or remove them from the list<br>
    <b>3.</b> Use Filter to find the necessary field<br>
    <b>4.</b> Click the <b>+</b> (add) button to add fields
</p>
</details>

&nbsp;

!!! note "Note"
    The order of fields placement on record cards **cannot** be adjusted in {{ short_name }} settings, as {{ product_name }} respects their order set in Salesforce; if you need to change it, [make the corresponding updates in your Salesforce configuration](https://help.salesforce.com/articleView?id=customize_layout.htm&type=5)

&nbsp;

&nbsp;

**8.3\.** Click on the **🖉** (Edit) icon to adjust an object field's special parameters; there, you can mark the field as **Important** or **Force Required**. These parameters are only used by [{{ short_name }} Add-In](../Introduction/) or [Chrome Extension](../Using-the-Solution-for-Salesforce-and-Gmail/) and have no ties in Salesforce of any kind.

&nbsp;

#### Marking Fields as Important

<p>
    <img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\toggle-important.gif">
</p>

&nbsp;

Important fields are prioritized for displaying when you create new records or view existing ones in the Sidebar. To display all fields, open the detailed object card or, if you are creating a new record, clear the **Show only important fields** checkbox.

<p><img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\new-record.png">
</p>

&nbsp;

#### Mark Fields as Force Required

To enhance fields filling flow via {{ short_name }}, after the [Autumn 2021 update](../Release-Notes/#revenue_inbox_2108_autumn_2021_release_notes) {{ product_name }} Customization includes a possibility to set specific fields of Salesforce objects processed or edited via [{{ short_name }} Add-In](../Introduction/) as *Force Required*. That implies specified fields' filling becomes mandatory when a user [creates](../Create-New-Records/) or modifies an object that contains the field in the Sidebar.

*Force Required* is located in the same field parameters as *Important* (see above).

<p><img src="..\..\assets\images\Configuration-&-Settings\User-Settings\Customization\toggle-force.gif">
</p>

&nbsp;

**8.4\.** Click **Done**  

!!! warning "Important"
    Please note that if you adjust objects' or fields' settings, for these changes to be applied you must [log out from {{ product_name }} Add-In](https://docs.revenuegrid.com/ri/fast/assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b3a275f0428630abc0ba0da.png) and then [re-log in](../How-to-Install-and-Run-the-Solution-all-configurations/#ii_rg_email_sidebar_logon)

&nbsp;

* * *

&nbsp;

### **9\. Configure Attachments Saving in Salesforce**

!!! tip "Tip"
    Refer to [this article](../Attachments-Handling-(Basic)/) for an overview of how files attached to emails/meetings are handled by {{ product_name }}

&nbsp;

Using the {{ short_name }} Customization page, you can set up the preferred attachment saving in your Salesforce account. 

Refer to [this article](../Configure-Attachments-Saving-in-Salesforce/) for more information on **Configuring Attachment Saving in Salesforce** using **{{ short_company_name }} Sidebar Customization Settings**.

&nbsp;

* * *

&nbsp;

### Attachments auto-selection

In the latest {{ short_name }} updates end users can set how [files attached to emails or calendar items](../Attachments-Handling-(Basic)/) should be handled by default, through auto-selection. This setting is located at the bottom of the right pane of Customization settings. The available options are:

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Attachments\autoselection.png">
</p>

&nbsp;

- **Autoselect only attached files > 100 KB** – this option allows to prevent saving in Salesforce of small images or animations attached to an email/calendar item as part of the signature, for example; however, the users will be able to select them, if needed  
- **Preselect the attechment file type in Save dialog** – only the specified file types will be autoselected for saving to Salesforce in the Add-In's save dialog. After selecting this option, the box for specifying file types will appear underneath. Specify file types without any dots, *e.g., txt*   
- **Autoselect all attached files** –  all attached files will be autoselected to be saved in Salesforce; but the users will be able to unselect unneeded attachments
- **Do not autoselect attached files** – no attached files will be autoselected; but the users will be able to select needed files


&nbsp;

* * *

&nbsp;

### **10\. Default Customization Settings**

If you have changed some of the above described settings and the resulting Add-In / Chrome Extension behavior does not meet your preferences, you can always revert to the default behavior by clicking the button **Reset to default settings** at the top of Customization page. The default set of settings is defined specifically for your {{ product_name }} implementation by [{{ company_name }}](mailto:support@revenuegrid.com) and [your local assigned administrator](../Special-Admin-Panel-Settings/); during a reset all object-specific and Add-In / Chrome Extension behavior settings are reverted to their default values except for the **[Use Adaptive view](../All-User-Actions-in-Add-In-Sidebar/)** one. Please note that user-specified settings can be backed up and recovered from another user in the same organization using [customization management mechanisms](../Managing-Email-Sidebar-Customizations/).

&nbsp;

&nbsp;

#### Setting the Default (Initial) Customization

In the latest {{ product_name }} updates the default (initial) set of customization settings can be defined by [local {{ product_name }} Admin](../How-to-Log-In-to-the-Admin-Panel/), to be applied right after the Solution is installed or after customization is reset to default by clicking the **Reset to default  settings** button in Customization page header. This feature enables quick uniform management of settings for different user categories and  facilitates restoring product functioning after unwanted adjustments  were made in the settings.

&#160;
 &#160;

