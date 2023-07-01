---
description: Detailed step-by-step guide on how to properly add a custom object to the handling scope
---
# How to Properly Add a Custom Object to the Handling Scope  
  

*3 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

{{ product_name }} can handle certain custom objects from [Salesforce custom objects set](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_objects_list.htm) in "out-of-the-box" configuration, by retrieving corresponding object layouts data from Salesforce; however, other custom objects will require extra setup actions from the end-user/local Salesforce Admin to be properly handled by {{ product_name }}.

**I.** We will explain the necessary setup actions taking the [*Campaigns* object](https://help.salesforce.com/articleView?id=campaigns_supplemental.htm&type=5) as an example. Campaigns is among custom object types which are present in [Salesforce set of objects](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_objects_list.htm), and in their case [enabling the Campaign object card on {{ short_name }} Customization page](../Customization-Settings-Explained/#5_choosing_a_set_of_salesforce_objects_to_display) alone is not enough to add them to {{ short_name }} handling scope. The first point to consider is that such objects may have one or more auxiliary related cards, for example a Campaign has associated *Campaign Member Status*, *Campaign Member*, and *Campaign Field History* cards. They contain additional object data, and their absence in {{ short_name }} processing scope results in primary objects, Campaigns in this case, not being retrieved by [{{ short_name }} initial search](../Initial-Search-and-Applied-Record-Filters/) (that is, brought up in [Related records lists](../Viewing-Salesforce-Records-Related-to-your-Email-(Adaptive-view)/) or by [user-initiated search](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-%28Adaptive-view%29/).

This way, when adding a custom object to the processing scope via {{ short_name }} Customization page, make sure to search for its auxiliary cards, by entering the object's name in the *Quick Find...* field of [Customization page](../Customization-Settings-Explained/)'s left pane *"Objects in Salesforce"*, then enable all relevant cards.

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/custom-object-auxiliary.png" class="minimized">
</p>

&nbsp;

Next, click **Save** in the upper right corner of Customization page to apply the changes and [refresh the Add-In](../All-User-Actions-in-Add-In-Sidebar/#11_minor_interface_improvements). This should include the object into {{ product_name }}'s handling scope (including a [dedicated tab](../All-User-Actions-in-Add-In-Sidebar/#1_records_categorizing) added for this object type on the home screen), as well as [user-initiated search](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-%28Adaptive-view%29/).

&nbsp;

* * *

&nbsp;

**II.** Next, to include the object into the [Related records list](../Initial-Search-and-Applied-Record-Filters/#related_records_retrieval_pattern), you should ensure that your [related Business record's layout](https://help.salesforce.com/articleView?id=customize_layout.htm&type=5) in Salesforce is correspondingly configured. Perform the below steps to do that:

  **1.** Log in to your Salesforce account
  
  **2.** In Salesforce, open **Setup** > **Object Manager** > *{Business record related to the added one, e.g. Contact or Account}* > **Lightning Record page** > open the *{item marked as Org Default}* > **Edit**

<p><img src="../../assets/images/Configuration-&-Settings/User-Settings/Enable-Campaigns-in-SF/sf-org-default.png" class="minimized">
</p>

&nbsp;

  **3.** To add a custom object to the Related list of a Business record:

&nbsp;&nbsp;&nbsp;**3.1.** In the right hand pane of Business record's layout page, click the **Add Tab** button under *Related*

&nbsp;&nbsp;&nbsp;**3.2.** In the page's central pane, open the added **Related** tab 

&nbsp;&nbsp;&nbsp;**3.3.** In the search box of the left hand pane, enter *'related'*

&nbsp;&nbsp;&nbsp;**3.4.** Drag and drop the **Related Lists** item found to the **Related** tab into the central pane

<p><img src="../../assets/images/Configuration-&-Settings/User-Settings/Enable-Campaigns-in-SF/sf-related-lists.png" class="minimized">
</p>

&nbsp;

**4.** Click **Save** in the top right corner of the layout page to apply the layout changes

**5.** Reapply {{ short_name }} customization to enable the layout changes; to do that, [open Customization page](../Customization-Settings-Explained/#1_how_to_open_customization_page) and click **Save** in its upper right corner. Now the added object should be shown in {{ short_name }}'s Related records list

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/custom-object-check.png)

&nbsp;

* * *

&nbsp;

**III.** Finally, to ensure that [{{ short_name }} initial search](../Initial-Search-and-Applied-Record-Filters/) retrieves and displays the objects of the added type, you should set a corresponding Salesforce List View in {{ short_name }}'s *Contextual Search* setting (which will be otherwise set to Do not search):

**1.** If you do not have a corresponding list view for the object in Salesforce, [create a custom Salesforce List View](../How-to-Create-a-Custom-List-View/) for the object that will include all instances of it

**2.** Set the created or your existing view in the [Contextual search filter](../Customization-Settings-Explained/#63_defining_the_searchview_scope) for this object in Customization settings

**3\.** Make sure to apply the changes in Customization by clicking **Save** in the upper right corner



&#160;
 &#160;





