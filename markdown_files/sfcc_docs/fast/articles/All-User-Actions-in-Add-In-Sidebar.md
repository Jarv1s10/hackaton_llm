---
description: An overview of all user actions in RG Email Sidebar
---
# All User Actions in {{ product_name }}  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*12 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! tip "Tip"
    Please also refer to [this article](../Introduction/) for an overview of all icons and buttons included in the updated {{ product_name }} user interface

&nbsp;

[{{ product_name }} Add-In](../Introduction/) / [Chrome Extension](../Using-the-Solution-for-Salesforce-and-Gmail/#using_the_extensions_sidebar) interface always evolves obtaining an even more streamlined and intuitive look and feel. The Sidebar is built upon the following principles:

* All key actions and useful information are available right at hand, no more than 2-3 mouse clicks away from the Sidebar’s home screen
* Fast and convenient navigation among records and between levels of detail of a selected record

* No interface cluttering with any items which have no relevance to the record that the user is currently working with; the user decides what records and record categories to expand

* Single-click selection of individual records or of all records of a specific type directly from the Sidebar's home screen

!!! tip "Tip"
    You can "zoom in" the Sidebar the way you zoom in web pages. To do that, click on the Sidebar, press the *Control (Ctrl)* button and scroll up the mouse wheel. All Sidebar components will be expanded and slightly re-arranged

&nbsp;

### Sidebar size adjustment

To accommodate the expanded controls in the Sidebar's pane, you can also stretch the Sidebar sideways: hover the cursor over the left-hand edge of the Sidebar so it looks like this **⇼**, then hold the left mouse button and stretch the Sidebar to the left.



&nbsp;



Major convenience of use features implemented in the Sidebar's Adaptive view:

### **1.** Items categorizing

!!! tip "Tip"
    To have all needed category tabs (separators) available at all times in the Sidebar, make sure to pin them in [{{ product_name }} Customization settings](../Customization-Settings-Explained/#7_changing_card_order_and_pinning_cards)

&nbsp;

All records are sorted according to their object type and folded under corresponding tab categories (separators) in the Sidebar:

<p><img src="..\..\assets\images\Getting-Started\First-Steps\Using-Adaptive-View\categories.png">
</p>


&nbsp;

The Add-In / Chrome Extension keeps the set of Sidebar tabs (separators) and records you expanded when processing your emails or events, so after you close MS Outlook or the Add-In / Chrome Extension and then open it again, you will not have to expand the needed tabs again.

Below record categories tabs (separators), there are tabs containing special action icons:

   **New records:** the tab appears when there are unresolved (not yet saved in Salesforce and non-internal/blocklisted) messages in your MS Outlook. Refer to [this article](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-(Adaptive-view)/#the_new_records_tab) for more details.

   **Activity Timeline:** [display and manage past and future activities](../Working-with-Activities/), create Tasks and Events. Note that this tab is only displayed if there are associated Taks and Events registered in Salesforce or if the tab was [pinned in {{ short_name }} Customization settings](../Customization-Settings-Explained/#7_changing_card_order_and_pinning_cards).

&nbsp;
&nbsp;

* * *

&nbsp;

#### Smart Actions

Smart Actions are implemented as an easy-to-reach from the key Sidebar screens bottom toolbar.

The set of Smart Actions displayed first without expanding the icon *More...* is defined in [{{ short_name }} Customization settings](../Manage-Smart-Actions/).

- [Enagement panel](../Tracking-Customer-Engagement-with-Magic-Pixel-(Adaptive-view)/)
- [Time slots](../How-to-Send-Meeting-Time-Slots-(Adaptive-view)/)
- [Book me](../Sharing-Calendar-Availability-(Adaptive-view)/)
- [Templates](../Using-Salesforce-Templates/)
- [Reports](../Salesforce-Reports/)
- [Observations panel](../Context-Specific-Actions/): contains clues concerning required {{ product_name }} setup actions and synchronization status along with information about actions and checks carried out by the Add-In / Chrome Extension, e.g. email addresses [filtered as internal/blocklisted](../Initial-Search-and-Applied-Record-Filters/#internal_emails_corporate_domains_and_the_blocklist) or [records merging suggestions](../Item-Deduplication-Mechanisms/#existing_record_duplicates_merging_with_conflicts_resolution)
- [{{ company_name }} Signals](https://docs.revenuegrid.com/articles/Signals/)


<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Getting-Started\First-Steps\Using-Adaptive-View\bottom_toolbar.png">
</p></details>
&nbsp;

##### {{ company_name }} templates

{{ product_name }} used in Revenue Engage context also includes a Smart Action icon *Insert {{ company_name }} Template*. 

This [set of preconfigured templates](https://docs.revenuegrid.com/articles/Templates/) used mostly in [engagement Campaigns communication](https://docs.revenuegrid.com/articles/video-tutorials/#launching_drip_campaign_605) is available in the [full {{ company_name }} revenue intelligence package](https://revenuegrid.com/pricing/). Note that upon request your existing Salesforce templates can be merged into {{ company_name }} templates pool.

After you click this icon, select a relevant template, and click **Insert**, the template gets inserted into the email you are composing in MS Outlook.

&nbsp;

* * *

&nbsp;

### **2.** Creating new records on a couple of clicks

New records - standard Salesforce objects as well as custom added objects - can be instantly created by clicking the **+** (Add) icon in the Sidebar's header or by clicking the **•••** (More actions) button that appears when you hover the mouse over a record category tab:


<details><summary> >>> Click to see an animation <<< </summary>
<p><img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5bd9949a2c7d3a01757a9c61.gif"style="width: 45%; height: 50%;">
</p></details>

&nbsp;
In addition, when you create a new record and there is no relevant Account or Contact registered in Salesforce to link it to (which is mandatory),  you can create one directly from the account selection picklist, by clicking the Create new Account button and populating the fields of the Create Account dialog that appears.

When you need to find specific record(s) saved in Salesforce via {{ product_name }} Add-In / Chrome Extension, in Adaptive view you simply click the Search icon located next to the Add icon in the Sidebar's header and [perform a search](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-(Adaptive-view)/). 

<details><summary> >>> Click to see an animation <<< </summary>
<p><img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5b361c220428630abc0b8d8b.gif"style="width: 45%; height: 50%;">
</p></details>

&nbsp;

* * *

&nbsp;

### **3.** All key actions at hand

To further reduce the number of clicks required to perform an action with a record, a menu listing all applicable actions is available in each record's header right on the Sidebar's home screen, so it takes two clicks to perform any action with a record. It appears as soon as you hover the cursor over a record's header:
<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Getting-Started\First-Steps\Using-Adaptive-View\menu-header.png">
<br>
<br>
<img src="..\..\assets\images\Getting-Started\First-Steps\Using-Adaptive-View\menu-expanded.png">
</p></details>
&nbsp;

Note that the set of actions is specific to each record type and includes creating related records of other types.

&nbsp;

&nbsp;

#### Quick save to a record

In addition, there is a quick save button on records' flashcards (headers) in the Sidebar that allows saving email with a specific record on a single click, without expanding a record's card or searching for it in the Save dialog. The quick save button is accessed by hovering the cursor over the object's icon in the header and clicking on the envelope or event icon that appears in its place.

<p><img src="..\..\assets\images\Getting-Started\First-Steps\Using-Adaptive-View\quick-save.png">
</p>

&nbsp;

If you use this icon in a record's header to quick-save an email as a Salesforce Task ([Enhanced Email](https://help.salesforce.com/s/articleView?id=sf.emailadmin_enhanced_email_considerations.htm&type=5) not enabled), the resulting Task will be linked to this record only.

If you use this icon to save an email as a Salesforce EmailMessage ([Enhanced Email](https://help.salesforce.com/s/articleView?id=sf.emailadmin_enhanced_email_considerations.htm&type=5) enabled), the resulting EmailMessage will be linked to all eligible records associated with addresses included in the email's *To*, *From*, *CC* fields.

&nbsp;


##### Convert a Lead to a Contact

With {{ product_name }}, it takes several clicks to convert a successfully engaged Lead to a Contact in Salesforce. To do that:  
**1\.** Hover the cursor over the lead icon on the right-hand side of the Lead's card in {{ product_name }}

**2\.** Click on the **☰** (Menu) icon that appears

**3\.** Select **Convert to Contact**

**4.** Populate the details in the dialog that appears:  

- Select or create an Account to link the Contact to  
- Set the Status for the converted Lead, i.e. *Closed - Converted*
- (Optional) create an associated Opportunity by entering its name in the field *New Opportunity Name*
- (Optional) select the checkbox *Send Notification Email* to get a notification email from Salesforce upon successful conversion



<details><summary> >>> Click to see an animation <<< </summary>
<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Managing-Contacts\leadtocontact.gif"style="width: 45%; height: 50%;">
</p></details>
&nbsp;

!!! note "Note"
    If you see a pop up notification *"Use one of these records?"* at the bottom of the Sidebar, that means that a Contact based on the same email address already exists in Salesforce

&nbsp;

##### The alternative way:

**1\.** Expand the Lead's card in {{ product_name }}

**2\.** Select **Show more** > **Convert to Contact**  

**3\.** Populate the details in the dialog that appears:  

- Select or create an Account to link the Contact to  
- Set the Status for the converted Lead, i.e. *Closed - Converted*
- (Optional) create an associated Opportunity by entering its name in the field *New Opportunity Name*
- (Optional) select the checkbox *Send Notification Email* to get a notification email from Salesforce upon successful conversion

<details><summary> >>> Click to see an animation <<< </summary>
<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Managing-Contacts\leadtocontact2.gif"style="width: 45%; height: 50%;">
</p></details>

&nbsp;

* * *

&nbsp;

### **4.** Viewing the details instantly

It takes one mouse click to see an animation/collapse a needed record's header to view its full card, with all key details and actions available at hand:

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Getting-Started\First-Steps\Using-Adaptive-View\card_view.png">
</p></details>

&nbsp;
Every record card includes the following tabs:
**Related** tab listing related objects (linked records and items retrieved through [initial search](../Initial-Search-and-Applied-Record-Filters/))
&nbsp;
On this tab you can view records, activities, and attachments associated with selected email or calendar event. This tab is available both in expanded card view and detailed record view.

!!! note "Note"
    For records browsing convenience, if you switch to another item in MS Outlook with the Related tab opened in the Sidebar, the related items list will be updated with items found for the new email/event selected

**Quick memo**: see feature description [here](../Record-Description-and-Add-Quick-Memo/)   

**Log a Call**: register in Salesforce notes summarizing the results of a phone or Internet call made to a contact  

**Add task**: register in Salesforce a task associated with a contact that needs to be performed within specified time frame  

**People**: (specific to Opportunity records) contacts involved in an Opportunity with their roles in it specified  

**Files**: email's/event's file attachments saving in Salesforce  
&nbsp;
&nbsp;

* * *

&nbsp;

### **5.** Improved records creation, updating, browsing

In the Adaptive Sidebar view, records' *Detailed view* is opened for each record individually, by clicking on the **>** (Expand) icon in a record's header.

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Getting-Started\First-Steps\Using-Adaptive-View\details.png">
</p></details>

&nbsp;

In the detailed view you can update any object field's value, by clicking the <img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b3f6da50428630abc0bc6a0.png" style="display: inline-block;vertical-align: middle;width: 18px;margin-left: 1px;height: 14px;object-fit: contain;">  icon next to it.

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Getting-Started\First-Steps\Using-Adaptive-View\edit-fields.png">
</p></details>



&nbsp;



Records headers' layout was also improved, now the headers include information from the records' 4 key fields (the [required (important) fields](../How-the-Solution-Works-with-Required-Fields-and-Layouts-in-Salesforce/#fields_and_related_records) defined in Customization settings), making records much easier to browse through within their category by their headers. In addition, you can open a related record included in the header instantly by clicking on its name.

Note that the fields included into record headers are not shown in their expanded cards (but are shown in detailed record view). Besides, pay attention that the list of fields shown on a card can be expanded by clicking the **Show more fields** button below; the *Show only important fields* button was removed from record cards along with the [Important fields](../Customization-Settings-Explained/) filling progress bar.

&nbsp;

#### Create Contacts via signature drag-and-drop

Besides the standard [Create Salesforce record](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-%28Adaptive-view%29/#creating_new_records_in_salesforce) feature, there is also a special way to instantly create new Contacts.

To create a new Contact:

**1\.** Open an email or meeting invite from/to a new business contact in MS Outlook  

**2\.** [Open {{ product_name }}](../How-to-Install-and-Run-the-Solution-all-configurations/#1_open_the_sidebar)

**3\.** Select (highlight) the signature with the cursor 

**4\.** Drag-and-drop the selection into [{{ product_name }}](../Introduction/) 

Within several seconds you will see the *Create Contact* dialog with auto-filled key fields parsed from the signature.

<details><summary>>>> Click to see an animation <<<</summary>
<p>
    <img src="..\..\assets\images\Features\draganddropfix.gif" style="width: 75%; height: 75%;">
</p>
</details>
&nbsp;



##### Configurations supported for the signature drag-and-drop feature:

- MS Outlook Desktop for Windows or MacOS  
- MS Outlook on the Web (*outlook.com*, *office.com*) opened in Mozilla Firefox browser  

&nbsp;

##### Unsupported configurations:  

- MS Outlook on the Web (*outlook.com*, *office.com*) opened in MS Edge  

- MS Outlook on the Web (*outlook.com*, *office.com*) opened in Google Chrome or a Chromium-based browser  

- MS Outlook on the Web (*outlook.com*, *office.com*) opened in MS Internet Explorer  

- [{{ short_name }} Chrome Extension for Gmail](../Chrome-Extension-Intro/)  

  

&nbsp;

&nbsp;

### **6.** Quick interaction with search results

In Adaptive view records search results are listed on a dedicated search results screen. On this screen, it takes only a couple of clicks to select records which you want to link an email/event to and save it in Salesforce.

!!! note "Note"
    To reduce {{ short_name }} user interface cramming, in the latest product updates the checkboxes next to record headers were removed

&nbsp;

Records' cards or the full detailed card view can also be opened from the [search results screen](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-(Adaptive-view)/) besides [the home screen](../Introduction/).

A related improvement: now, when search results are opened in the Sidebar and you select another item in MS Outlook, the search results are replaced with the new selected item's associated items retrieved by initial search.

&nbsp;

* * *

&nbsp;

### **7.** Smart selection of records to be linked

!!! tip "Tip"
    Also see [this article](../Activities-Linking/) for detailed information on items linking

&nbsp;

After records have been associated (linked) with a saved email or event, they are marked with green checkmark circles, so you will see the actual associations straight away when selecting an email/event, plus you can navigate to [associated Activity](../Working-with-Activities/) by clicking on the checkmark icon.

Two related customization settings were implemented in {{ product_name }} Customization settings to allow advanced managing of records' selection for emails and events: Pre-select records and Disallow linking, please refer to [this article](../Customization-Settings-Explained/#4_defining_record_associations) for more information. 

Additionally, a minor use convenience setting was added in Adaptive view, **Do not select "Auto-save in thread" by default**, please find more information about this feature [here](../Customization-Settings-Explained/#2_application_settings)

&nbsp;

* * *

&nbsp;

### **8.** Easy saving of email or calendar [attachments](../Attachments-Handling-(Basic)/)

!!! tip "Tip"
    Please note that in the latest {{ product_name }} updates there is also an extra file listed among files actually attached to the email - an exact copy of the email message in *.eml* format which you can also save in Salesforce (the "default attachment")

&nbsp;
To save attachments to Salesforce, you need to expand a relevant record's card and then

* Either open the **Related** tab (see the point 3), click the **+** (Add) button next to the **Attachments** category, then select the checkbox next to an attachment and click **Attach** at the bottom

<details><summary> >>> Click to see an animation <<< </summary>
<p><img src="..\..\assets\images\Getting-Started\First-Steps\Using-Adaptive-View\save_attachment_related.gif"style="width: 45%; height: 50%;">
</p></details>

&nbsp;

* Or open the **Files** tab (see the point 3) and click **Attach** next to the needed attachment

<details><summary> >>> Click to see an animation <<< </summary>
<p><img src="..\..\assets\images\Getting-Started\First-Steps\Using-Adaptive-View\save_attachment_files.gif"style="width: 45%; height: 50%;">
</p></details>

&nbsp;

- Alternatively, expand a record's detailed view and select **Show more** > **Attach files**

<details><summary> >>> Click to see an animation <<< </summary>
<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Attachments\save-attach.gif"style="width: 45%; height: 50%;">
</p></details>


&nbsp;


Additionally, the **Add a file** button for direct file attaching was added to record creation dialogs:

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Getting-Started\First-Steps\Using-Adaptive-View\addafile.png">
</p></details>


&nbsp;

* * *

&nbsp;

### **9.** Entered data loss prevention

In updated Adaptive view, when you modified a record's fields or created a new record and then switched to another item in MS Outlook, the following confirmation dialog it displayed, to prevent loss of the data you entered.

<p><img src="..\..\assets\images\Getting-Started\First-Steps\Using-Adaptive-View\confirmation_dialog.png" style="width: 45%; height: 45%;">
</p>

&nbsp;

* * *

&nbsp;

### **10.** More actions at hand

Object type-specific action icons are also included in detailed record view so you do not need to navigate between the views to perform them:

&nbsp;

<p><img src="..\..\assets\images\Getting-Started\First-Steps\Using-Adaptive-View\detailed_view_action_icons.png">
</p>

&nbsp;

* * *

&nbsp;

### **11.** Email / Event saving status indication in Sidebar header

{{ product_name }}'s header in Adaptive view includes a handy indicator of selected Email's or Event's saving status – whether the item is

* **{Item type} is saved.** Clicking on the text will open the saved item's expanded card with all its details.
* **{Item type} will be saved.** The item is queued to be saved on the following [sync session](../Synchronization-Engine-An-Overview/).
* **{Item type} cannot be saved** in Salesforce by {{ short_name }} – see points (5) and (6) in [this article](../Saving-Emails-in-Salesforce-1.-Function-Overview/#under_the_hood_mechanisms_and_special_patterns_applied_on_emails_saving) for more information

<p><img src="..\..\assets\images\Getting-Started\First-Steps\Using-Adaptive-View\save_status.png">
</p>
&nbsp;

* * *

&nbsp;

### **12.** "Continue Editing" function on record fields editing

"Continue editing" is another convenience of CRM data entry feature. It is used on records field values editing via the Sidebar's [Detailed card view](../All-User-Actions-in-Add-In-Sidebar/#4_viewing_the_details_instantly).  

Sometimes {{ short_name }} users want to make updates to several fields before they apply all the changes to the record in Salesforce. To achieve that, they should click the button **Continue editing** instead of Save after editing individual fields:

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\continue-editing2.png" style="width: 50%; height: 50%;">
</p>

&nbsp;

After that, proceed to editing other fields. Note the **⭯** (Revert) icon that appears next to fields which were updated; clicking on it allows to quickly recover the original field value. After the values have been finalized, click on the button **Save changes for this {record type}** in the Detailed view to apply the changes:


<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Using-SmartCloud-Connect\continue-editing1.png" style="width: 50%; height: 50%;">
</p></details>
&nbsp;

Clicking Save in an individual field editing dialog also applies all changes you have made


&nbsp;

&nbsp;

