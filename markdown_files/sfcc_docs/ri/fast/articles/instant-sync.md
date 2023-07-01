---
description: How to configure instant sync of events from Salesforce to MS Outlook
---

# Instant Events Sync from Salesforce to MS Outlook 

**[this article is work-in-progress]**

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

<br>

One of the features included in the {{ company_name }} Salesforce managed package is the instant down-sync of calendar items from Salesforce to MS Outlook. This feature can be enabled upon request to the [{{ short_company_name }} support team](mailto:support@revenuegrid.com). 

After installing [{{ company_name }} managed package](../Admin-Managed-Package/) in an Org, admin must configure the instant calendar Events down-syncing from Salesforce to email client should separately as described in this article. This feature works for MS Exchange or Office 365 mailboxes connected over [EWS](../Working-With-EWS/) or [MS Graph](../MS-Graph/) as well as for [Gmail boxes](../Using-the-Solution-for-Salesforce-and-Gmail/#syncing_calendar_events_in_salesforce).

This features enables {{ product_name }} end users to auto-sync newly created Salesforce Events with email client's calendar in real time. Note that this intant syncing is triggered *only* on Salesforce Events creation. 

After being created, the calendar item is down-synced to the user’s MS Outlook calendar within several minutes. Usually within 5 minutes; however, this interval can be adjusted to match your org’s needs by submitting a corresponding request to the [{{ short_company_name }} support team](mailto:support@revenuegrid.com). 

!!! note "Note"  
    By default, the refresh token for this feature expires in 30 days after the connection. Thus the [Connection refreshment procedure](https://docs.revenuegrid.com/ri/fast/articles/instant-sync/#refresh_rg_connection_to_salesforce_config) should be performed every 30 days. If your Org requires, the refresh token expiration period can be prolonged by sending a corresponding request to [our support team](mailto:support@revenuegrid.com)

<br>

<hr>

## Install {{ company_name }} Salesforce managed package

To use this feature, you must have the latest {{ company_name }} package installed in your Salesforce org.  

**You can get the latest version of the managed package here:**   
<https://login.salesforce.com/packaging/installPackage.apexp?p0=04t1P000000ElXz>

The Publisher name of the package *InvisibleCRM* is an old brand name of {{ company_name }}. 


!!! tip "Tip"  
    Consult [this article](../Admin-Managed-Package/) for more details on installing and configuring the managed package


<br>

<hr>

## Add the Custom Setting "**ClientID**" 

!!! note "Note"
    For performing this step, request "**ClientID**" from <a href="mailto:support@revenuegrid.com">{{ short_company_name }} support team</a> in advance

<p style="margin-left:5%">
<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\instant-sync\gear.png" style="width: 30%; float: right;margin-left:2%; margin-right: 10%;">
 <b>1.</b> Click on the <b>Gear</b> ⚙  icon and select <b>Setup</b>
    <br><br><br><br><br><br><br>
<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\instant-sync\setup.png" style="width: 30%; float: right;margin-left:2%; margin-right: 10%;">
<b>2.</b> In the Quick Find box in the left-hand sidebar, enter <b>Custom Settings</b> to quickly find the necessary setting 
    <br><br><br><br><br>
 <img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\instant-sync\client-config.png" style="width: 45%; float: right;margin-left:2%; margin-right: 10%;">
 <b>3.</b> On the opened page, find the <b>CliendId Config</b> setting
    <br><br>
 <b>4.</b> Click <b>Manage</b> next to it
 <br><br> <br><br>
 <img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\instant-sync\clientid-edit.png" style="width: 30%; float: right;margin-left:2%; margin-right: 10%;">
 <b>5.</b> On the CliendId Config page, click <b>Edit</b>
  <br><br><br><br><br>
    <img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\instant-sync\clientid-empty.png" style="width: 45%; float: right;margin-left:2%; margin-right: 10%;">
 <b>6.</b> Copy and paste the <i>ClientId</i> numeric value obtained from {{ short_company_name }} support team in the corresponding field.  <br><br>
  <br><br>
 <b>7.</b> Click <b>Save</b> to apply the changes
    <br><br>
 </p>

<hr>

## Connect {{ company_name }} to your Salesforce configuration 

!!! note "Note"
    For performing this step, request "**ServerSyncTenantUrl**" from <a href="mailto:support@revenuegrid.com">{{ short_company_name }} support team</a> in advance or generate it on your own following the instructions provided in [this article](../How-to-generate-tenant-urls/)

<p style="margin-left:5%">
<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\instant-sync\sales-console.png" style="width: 35%; float: right;margin-left:2%; margin-right: 10%;">
 <br><br>
<b>1.</b> Go to <b>App Launcher</b>
    <br><br>
<b>2.</b> Switch to <b>Sales Console</b>
    <br><br> <br><br> <br><br>
 <img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\instant-sync\nav-menu-rg.png" style="width: 35%; float: right;margin-left:2%; margin-right: 10%;">  
<b>3.</b> Open the <i>Navigation menu</i> and select the option <b>Connect {{ short_company_name }} to Salesforce Config</b>
<br><br> 
If you see <b>no</b> option *Connect {{ short_company_name }} to Salesforce Config* on the Navigation menu list refer to <a href="../instant-sync/#how_to_add_connect_rg_to_salesforce_config_to_the_navigation_menu">the instructions provided below</a>.
 <br><br> <br><br>
<b>4.</b> In the “<i>Enter your tenant URL here...</i>” field, enter the <b>ServerSyncTenantUrl</b> obtained from our support team
<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\instant-sync\connect.png">
</p>

!!! note "Note"
    ServerSyncTenantUrl should follow this pattern: *https://[ your tenant ]-sync.revenuegrid.com/* .  
    If you do not know your ServerSyncTenantUrl, you can either request it from [{{ short_company_name }} support team](mailto:support@revenuegrid.com) or generate it on your own following [the guidelines in this {{ company_name }} instruction](../How-to-generate-tenant-urls/)
    <br>
<p style="margin-left:5%">
<b>5.</b> Click <b>Connect</b>. 
    <br><br>
<b>6.</b> Next, you will see a standard Salesforce OAuth window
<br><br>
<b>7.</b> Log in to it with Salesforce credentials to authorize data access for integration
</p>

!!! warning "Important"
    It may require several attempts to authorize it due to the technical peculiarities of Salesforce API authorization functioning; you may sometimes see an error  "*OAuth Error: We can't authorize you ... OAUTH_APPROVAL_ERROR_GENERIC*", please disregard it and continue login attempts until you see the green confirmation message "Connected".
    Also, it's possible that you will successfully sign in with Salesforce but won't see the the green confirmation message "Connected". In this case, click **Connect** again and **repeat login attempts until you see the green confirmation message "Connected"**.

<br>
After connecting {{ company_name }} to your Salesforce configuration, instant sync of calendar items from Salesforce to MS Outlook should function as expected.

<hr>

### How to add "Connect {{ short_company_name }} to Salesforce Config" to the Navigation menu 


If the option *Connect {{ short_company_name }} to Salesforce Config* is not on the list in the Navigation menu, to add it: 

<p style="margin-left:5%">
 <img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\instant-sync\edit.png" style="width: 45%; float: right;margin-left:2%; margin-right: 10%;">  
<br><br>
<b>1.</b> Open the Navigation Menu 
<br><br>
<b>2.</b> Click the <b>Edit</b> button 
<br><br><br><br><br><br><br><br>
<b>3.</b> In the opened window, click <b>Add More Items</b>
<br>
 <img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\instant-sync\add-more-items.png" style="width: 80%">  
<br><br>
<b>4.</b> In the next window, in the <i>Search all items</i> field, enter <b>Connect {{ short_company_name }} to Salesforce Config</b> to quickly find the necessary item 
<br><br>
<b>5.</b> Click the <b>Plus</b> button next to it 
<br>
<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\instant-sync\add-items.png" style="width: 80%">  
<br><br>
<b>6.</b> Next, click <b>Add 1 Nav Item</b> 
<br>
<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\instant-sync\add-1.png" style="width: 80%">  
<br><br>
<b>7.</b> Click <b>Save</b> to apply the changes 
<br><br>
<b>8.</b> Proceed with <a href="../instant-sync/#:~:text=3.%20Open%20the%20Navigation%20menu">the step 3</a> in Connect {{ company_name }} to your Salesforce configuration
</p>

<br>
<hr>
<br>

## Refresh {{ short_company_name }} connection to Salesforce config

In the default configuration of instant sync, the refresh token for this feature expires in 30 days after the connection. Thus, the admins shoud re-connect {{ short_company_name }} to Salesforce config every 30 days. 

!!! tip "Tip"  
    If your Org requires, the refresh token expiration period can be prolonged. To find out more about this option, sending a corresponding request to the [{{ short_company_name }} support team](mailto:support@revenuegrid.com)

<p style="margin-left:5%">
<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\instant-sync\sales-console.png" style="width: 35%; float: right;margin-left:2%; margin-right: 10%;">
 <br><br>
<b>1.</b> Go to <b>App Launcher</b>
    <br><br>
<b>2.</b> Switch to <b>Sales Console</b>
    <br><br> <br><br> <br><br>
 <img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\instant-sync\nav-menu-rg.png" style="width: 35%; float: right;margin-left:2%; margin-right: 10%;">  
<b>3.</b> Open the <i>Navigation menu</i> and select the option <b>Connect {{ short_company_name }} to Salesforce Config</b>
<br><br> 
If you see <b>no</b> option Connect {{ short_company_name }} to Salesforce Config on the Navigation menu list refer to <a href="../instant-sync-troubleshooting/#how_to_add_connect_rg_to_salesforce_config_to_the_navigation_menu">the instructions provided below</a>.
 <br><br> <br><br>
<b>4.</b> In the next window that opens, click <b>Disconnect</b> 
<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\instant-sync\disconnect.png">
 <br><br>
<b>5.</b> You will see the green Disconnected status pop-up 
 <br><br>
<b>6.</b> In the “<i>Enter your tenant URL here...</i>” field, enter the <b>ServerSyncTenantUrl</b>
<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\instant-sync\connect.png">
</p>

!!! note "Note"
    ServerSyncTenantUrl should follow this pattern: *https://[ your tenant ]-sync.revenuegrid.com/* .  
    If you do not know your ServerSyncTenantUrl, you can either request it from [{{ short_company_name }} support team](mailto:support@revenuegrid.com) or generate it on your own following [the guidelines in this {{ company_name }} instruction](../How-to-generate-tenant-urls/)
    <br>
<p style="margin-left:5%">
<b>7.</b> Click <b>Connect</b>. 
    <br><br>
<b>8.</b> Next, you will see a standard Salesforce OAuth window
<br><br>
<b>9.</b> Log in to it with Salesforce credentials to authorize data access for integration
</p>

!!! warning "Important"
    It may require several attempts to authorize it due to the technical peculiarities of Salesforce API authorization functioning; you may sometimes see an error  "*OAuth Error: We can't authorize you ... OAUTH_APPROVAL_ERROR_GENERIC*", please disregard it and continue login attempts until you see the green confirmation message "Connected".
    Also, it's possible that you will successfully sign in with Salesforce but won't see the the green confirmation message "Connected". In this case, click **Connect** again and **repeat login attempts until you see the green confirmation message "Connected"**.

<br>
After connecting {{ company_name }} to your Salesforce configuration, instant sync of calendar items from Salesforce to MS Outlook should function as expected.

<hr>