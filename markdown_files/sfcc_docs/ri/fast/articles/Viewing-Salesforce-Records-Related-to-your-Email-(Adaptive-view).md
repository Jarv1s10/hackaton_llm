---
description: Learn how to view the records related to selected email/calendar item (linked items and the related records list)
---
# Viewing Records Related to Selected Email/Calendar Item (Linked Items and the Related Records List)  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

{{ product_name }} Add-In / [Chrome Extension](../Using-the-Solution-for-Salesforce-and-Gmail/) reads key identifying data from your currently selected or opened email/calendar item and retrieves related Salesforce records and activities to be displayed as easy to browse and access cards in [{{ product_name }}](../All-User-Actions-in-Add-In-Sidebar/), enabling the end-users to effectively interact with various relevant CRM objects when working with their correspondence and calendar. Relevant Leads, Contacts, Accounts, Opportunities, Cases, as well as your Org specific [custom objects](../How-to-Add-A-Custom-Object/), both [directly linked in Salesforce](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) and [associated with selected item indirectly](../Initial-Search-and-Applied-Record-Filters/#the_resulting_related_records_list_will_include), are displayed right in your email client next to the email/calendar item being created or processed.

When you select a new or already saved email or calendar item in MS Outlook, {{ product_name }} will display Salesforce records associated with the sender's/recipient's email address as well as Business record already linked to it, is there are any (marked with green checkmark icons). After you expand a related Lead's / Contact's or Account's card in the Sidebar by clicking on its header, you will see all associated items classified into categories. In [this Knowledge Base article](../Initial-Search-and-Applied-Record-Filters/#related_records_retrieval_pattern) you can find more information on what logic is applied on retrieving related items.

<p><img src="../../assets/images/Using-SmartCloud-Connect/How-To-s/View-Related/screen-1.png" class="minimized">
</p>

&nbsp;

Related records cards displayed in the Sidebar show the fields [marked as important](../Customization-Settings-Explained/#8_customizing_detailed_card_view) on {{ short_name }} customization page. To view a record's detailed card, click the **>** button in its header. Note that {{ product_name }} retrieves [custom Salesforce layouts](https://help.salesforce.com/articleView?id=building_page_layouts_for_custom_objects.htm&type=5) used in your Org – thus you will get the same [set and order of fields in your objects' cards](../How-the-Solution-Works-with-Required-Fields-and-Layouts-in-Salesforce/) in [{{ product_name }}](../Introduction/) as in Salesforce.
Here you can also quickly review all associated Activities for a selected object: emails, tasks, follow ups, calls, meetings. To do that, click on the **Activity History** category under **Related** tab on a record's expanded card.
![](../assets/images/Using-SmartCloud-Connect/How-To-s/View-Related/activity_history.png)
&nbsp;
In {{ product_name }} you can also [make use of custom Salesforce buttons or links](../Salesforce-Custom-Buttons-Support/) after [adding them to the object's layout in Salesforce](https://help.salesforce.com/articleView?id=defining_custom_links.htm&type=5).

When you [create a new record in Salesforce](../Create-New-Records/) via the Add-In, relevant fields of the record are automatically prefilled with data retrieved from your currently opened Email or Calendar item.

You can [effectively link](../All-User-Actions-in-Add-In-Sidebar/#7_automated_quick_selectionunselection_of_records) [Salesforce activities](https://help.salesforce.com/articleView?id=activities.htm&type=5) to related records via {{ product_name }}, such as Tasks, Events, Follow-ups, or Calls.


&#160;
 &#160;

