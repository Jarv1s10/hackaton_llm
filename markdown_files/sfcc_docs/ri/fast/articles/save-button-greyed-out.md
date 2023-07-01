---
description: RGES Add-In's Icons are Greyed Out: How to troubleshoot this issue
---
# How to Resolve the Issue Where the Add-In’s Save Email Button is Greyed Out  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\icon-greyed-out\save-button.png" style="width:45%; display:inline-block; vertical-align:middle; margin-left:1px;float: right">
</p>

If after [installing {{ short_name }} Add-In](../How-to-Install-and-Run-the-Solution-all-configurations/) and opening it, you are still unable to save any email because the Save Email button is greyed-out, unclickable, or unresponsive, that is most probably caused by your [Customization settings](../Customization-Settings-Explained/). 
<br><br><br><br><br>
There are two reasons why this may happen: 

### 1. No objects selected in the Objects in Salesforce list 

If no objects are selected in the [**Objects in Salesforce**](../Customization-Settings-Explained/#5_choosing_a_set_of_salesforce_objects_to_display) list, {{ product_name }} is unable to find any object to link the email to. At least one object should be selected in this list to ensure the seamless saving of emails in Salesforce. 

<p style="margin-left:7%">
<b>1.1.</b> Open {{ product_name }} 
<br><br>
<b>1.2.</b> Click on the <b>Menu</b> button in the Add-In 
<br><br>
<b>1.3.</b> Go to <b>Customization</b> 
<br><br>
<b>1.4.</b> On the opened Customization page, review the selection in the <b>Objects in Salesforce</b> list. Make sure that <b>at least one object</b> is selected. 
<br><br>
<b>1.5.</b> Click <b>Save</b> in the upper left-hand side corner 
<br><br>
<b>1.6.</b> Go back to the Add-In, go to <b>Menu</b> and click <b>Refresh</b> to apply the customization changes 
</p>
 
<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\icon-greyed-out\customization-obj.png" style="width:80%" class="minimized">
</p>
<br><br>

### 2. All object types are disallowed for linking to emails  

If all object types are selected in the Disallow linking to emails for the following objects box, {{ product_name }} is unable to find any object to link the email to. 

<p style="margin-left:7%">
<b>1.1.</b> Open {{ product_name }} 
<br><br>
<b>1.2.</b> Click on the <b>Menu</b> button in the Add-In 
<br><br>
<b>1.3.</b> Go to <b>Customization</b> 
<br><br>
<b>1.4.</b> On the opened Customization page, review the added objects in the <b>Disallow linking to emails for the following objects</b> box. Make sure that <b>at least one object</b> is allowed for linking objects to (is not added to the box) 
<br><br>
<b>1.5.</b> Click <b>Save</b> in the upper left-hand side corner 
<br><br>
<b>1.6.</b> Go back to the Add-In, go to <b>Menu</b> and click <b>Refresh</b> to apply the customization changes 
</p>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\icon-greyed-out\customization-disallow.png" style="width:80%" class="minimized">
</p>