---
description: How to Configure Attachments Saving in Salesforce to avoid duplication and ensure optimized storage usage
---
# How to Configure Attachments Saving in Salesforce  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! tip "Tip"
    Refer to [this article](../Attachments-Handling-(Basic)/) for an overview of how files attached to emails/meetings are handled by {{ product_name }}  
  
!!! tip "Tip"  
    See [this article](../Customization-Settings-Explained/) for more detailed overview of {{ product_name }} Customization Settings.  

&nbsp;

There are two different object types used for storing email/event attachments in Salesforce, **Content document (File)** (in both Lightning Experience and Salesforce Classic) and **Attachment** (representing the [the older approach](http://help.salesforce.com/articleView?id=lex_gaps_limitations_files_and_content.htm&type=5) used in Salesforce Classic). The differences between them are summarized in [this table](http://help.salesforce.com/articleView?id=collab_files_differences.htm&type=5) (check the columns _CRM Content_ and _Attachments_ respectively).

Using Salesforce Content documents, the recommended way, allows to avoid duplication of stored files and to optimize Salesforce storage use, while Salesforce Attachments are used only when the first option is not available. To determine which type is used for storing attachments in your Org, see [this Forcetalk thread](http://www.forcetalks.com/salesforce-topic/files-vs-attachments-in-salesforce/#post-17905).

Depending on what kind of object is used for storing attachments in your Salesforce, to set up attachment saving via {{ product_name }} you need to enable the respective object in the central column _Objects in {{ product_name }}_ on Customization page.

To set up attachments setting via {{ product_name }}, open Customization page, find the _Content document (File)_ or _Attachment_ type in the left pane _Objects in Salesforce_ and select the checkbox next to it. The object will be added to the central column, all its settings and fields automatically populated. If both object types are selected, _Content document (File)_ will prevail, so if your Salesforce Org uses _Attachment_ objects, make sure that the other box is disabled. And keep in mind that if neither object type is enabled {{ product_name }} will not be able to save attached files in Salesforce.

<details><summary>>>> Click to see an animation <<<</summary>
<p>
    <img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5b9aa2360428631d7a8b16f5.gif">
</p>
</details>

&#160;
 &#160;

