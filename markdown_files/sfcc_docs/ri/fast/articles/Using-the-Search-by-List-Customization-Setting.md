---
description: Learn how to use the Search by field and the associated best use practices.
---
# Using the Search by List Customization Setting  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

On [{{ product_name }} Customization page](../Customization-Settings-Explained/), the central column _Objects in {{ product_name }}_ lists all Salesforce record types displayed in the Add-In / Chrome Extension. Under every record type, there are [relevant customization settings](../Customization-Settings-Explained/#6_customizing_object_card_appearance_and_behavior). This article specifically explains how to use the **Search by** field (under the _Other settings_ category) and provides associated best use practices.  

The **Search by** field allows to set the object’s fields to be used both when {{ product_name }} [searches for existing associated records](../Initial-Search-and-Applied-Record-Filters/) and when [you are searching for a certain record](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-(Adaptive-view)/) of this type. Specifically, when you enter a value to search for in the Sidebar, the value will be matched against the contents of the specified fields of all records of this type in Salesforce.

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b96467c0428631d7a8ae264.png" class="minimized">
</p>

&nbsp;
!!! warning "Important"
    If this field is left blank, then _all_ fields will be covered in the search. Additionally, take into consideration that if too many fields are listed in **Search by**, Salesforce search will take considerably more time to complete, so it is recommended to limit their number to as few as possible (10 fields being the tentative maximum)
  
{{ product_name }} features the possibility to **Search by** the object type using the object type selector in the {{ short_name }} global search.
    
<img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/search-by-object-type.png" style="width: 50%; height: 50%;">
   
&nbsp;  
   
!!! tip "Tip"   
    One more feature avaliable in {{ product_name }} is the **Search by** combination of tags (maximum 5 tags at once). After at least 3 characters are entered, on "Enter" button pressing, the keyword is added as a search tag. The keyword may include spaces

&nbsp;

### **Best use practice tips:**

*   To make records searchable, {{ product_name }} adds the following default **Search by** fields to its standard objects:  
    *   Contact, Lead: Full Name, Email  
    *   Account: Account Name, Website  
    *   Opportunity: Name  
    *   Case, Task, Event: Subject  

If you create custom objects in Salesforce or modify existing objects' field customizations or the **Search by** list, make sure to add to this list the field(s) which uniquely identify these objects, to be used in {{ product_name }} search.

*   Many {{ product_name }} users find it convenient to set the _First name_ and _Last name_ fields separately in the **Search by** field instead of _Full name_. This simplifies search value entry – instead of entering both name and surname into the search box (exact value search is used) you will need to enter only either one of them.
*   Another common best-use practice (requires Salesforce admin permissions to set up): [create in Salesforce](http://help.salesforce.com/articleView?id=adding_fields.htm&type=5) (if it did not exist in your customization) a custom _2nd Email_ field for your email correspondent record types that will store the interlocutor’s secondary (personal) email address, then include the field in **Search by**.  
    
	Secondary addresses are often used in communication besides the primary (business) ones and, since **Search by** also defines [{{ product_name }} initial search process](../Initial-Search-and-Applied-Record-Filters/), this will allow messages received from the secondary address to be properly processed and associated in Salesforce. This is the most convenient way to deal with messages incoming from secondary addresses, however, if creating in Salesforce and populating the _2nd Email_ field for new records is not an option for you, you can find the relevant objects using [{{ product_name }} search](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-(Adaptive-view)/) and link them manually.
  


&#160;
 &#160;

