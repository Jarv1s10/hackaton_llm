---
description: Troubleshooting issues with Instant sync of events from Salesforce to MS Outlook
---

# Troubleshooting issues with Instant Events Sync from Salesforce to MS Outlook 

**[this article is work-in-progress]**

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

<br>

Instant sync of calendar items from Salesforce to MS Outlook and is enabled upon request.

After being created, the calendar item is down-synced to the user’s MS Outlook calendar within several minutes. Usually within 5 minutes; however, this interval can be adjusted to match your org’s needs by submitting a corresponding request to the [{{ short_company_name }} support team](mailto:support@revenuegrid.com). 

To use this feature, you must have the latest {{ company_name }} package installed in your Salesforce org.  

**You can get the latest version of the managed package here:**   
<https://login.salesforce.com/packaging/installPackage.apexp?p0=04t1P000000ElXz>

The Publisher name of the package *InvisibleCRM* is an old brand name of {{ company_name }}. 


!!! tip "Tip"  
    Refer to [this article](../Admin-Managed-Package/) for more details on installing and configuring the managed package

<br>

In rare cases, instant sync of calendar items from Salesforce to MS Outlook calendar can function incorrectly. If the calendar items created in Salesforce are not being saved to the mail server calendar within the instant sync time span (5 minutes or custom requested time span). However, the calendar items get down-synced to the mail server calendar during the regular synchronization sessions. 

<hr>

## Check your managed package version

To catch up with the latest Salesforce updates and ensure the new features functioning, we regularly release {{ company_name }} managed package updates. The updated links are published in this article's topmost section or in the [dedicated managed package article's topmost section](../Admin-Managed-Package/).  


The easiest way to check whether you have the latest Managed Package version and to upgrade it if necessary is to:

**1\.** Open the new managed package link in your web browser  

**2\.** Log in to your Salesforce account (it must have Admin permissions in your Org). 


You will see the information about the version you have installed and the latest version to which you should upgrade:
<ul>
<li> <b>Installed</b> – is the version that is currently installed in your org </li>
<li> <b>New Version</b> – is the version that must ensure the proper functioning of all Managed Package's components</li>
</ul>

<p>
    <img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\instant-sync\upgrade.png">
</p> 

&nbsp;

If the Installed and New Version numbers are the same, it means that you have the latest {{ company_name }} Managed Package installed. 


**If the versions differ:**

**3\.** Indicate if you want to upgrade the package for:
<p style="margin-left:7%">
<ul>
<li><i>All users in your Org</i></li>
<li>(recommended) <i>Install for specific Profiles</i>:  which will be using {{ company_name }} components</li>
<li><i>Only for the Admins</i></li>
</ul>
</p>

<p>
<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\instant-sync\upgrade2.png" style="width:90%">
</p>

&nbsp;

**4\.** If you chose *Install for specific Profiles*, set the needed profiles scope using the controls underneath 

!!! note "Note"
    Also see [the relevant Salesforce guide](https://developer.salesforce.com/docs/atlas.en-us.230.0.appExchangeInstallGuide.meta/appExchangeInstallGuide/appexchange_install_installation.htm) for details

&nbsp;

<details><summary> >>> Click to see the controls' screenshots <<< </summary>
<p>
<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\RG-package-2.png">
</p>
<br>
<br>
<br>
<p>
<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\RG-package-3.png">
</p>
<br>
<br>
<br>
<p>
<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\RG-package-4.png">
</p></details>

&nbsp;

**6.** Click the button **Upgrade** underneath

Next, you will see the following notification, click the **Done** button, and soon you will receive an email message from Salesforce confirming that the package was upgraded:

<p>
    <img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\upgrading.png">
</p>

<hr>

## Check the Custom Setting "**ClientID**" 

One of the reasons why instant sync of calendar items from Salesforce to MS Outlook may not function correctly is the lack of **ClientId** value in the *CliendId Config* custom setting. 
<br><br>

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
   <img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\instant-sync\clientid-filled.png" style="width: 45%; float: right;margin-left:2%; margin-right: 10%;">
 <b>6.</b> Make sure that the <i>ClientId</i> is filled with numeric value. If it is correctly prefilled, proceed with <a href="../instant-sync/#check_the_custom_setting_triggersettings">the next step</a>
  <br><br> <br><br>
   <img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\instant-sync\clientid-empty.png" style="width: 45%; float: right;margin-left:2%; margin-right: 10%;">
 <b>7.</b> If ClientId is empty, request a new ClientId from <a href="mailto:support@revenuegrid.com">{{ short_company_name }} support team</a> and enter/paste it in the corresponding field
  <br><br>
 <b>8.</b> Click <b>Save</b> to apply the changes
    <br><br>
 <b>9.</b> Next, proceed with checking the Custom Setting <i>TriggerSettings</i>
 <br>
 </p>

<hr>

## Check the Custom Setting "**TriggerSettings**"

The instant sync of calendar items from Salesforce to MS Outlook may function incorrectly due to misconfiguration of TriggerSettings in Custom Settings.
<br><br>
<p style="margin-left:5%">
<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\instant-sync\setup.png" style="width: 30%; float: right;margin-left:2%; margin-right: 10%;">
<b>1.</b> In the Quick Find box in the left-hand sidebar, enter <b>Custom Settings</b> to quickly find the necessary setting 
    <br><br><br><br><br><br>
<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\instant-sync\trigger.png" style="width: 45%; float: right;margin-left:2%; margin-right: 10%;">
<b>2.</b> On the opened page, find <b>TriggerSettings</b>
    <br><br>
<b>3.</b> Click <b>Manage</b> next to it
    <br><br><br><br>
<b>4.</b> If the page is empty (see the screenshot below), you must create a new custom setting with a new setup owner
<br>
    <img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\instant-sync\no-records.png"  class="minimized">
</p>
<br>
<p style="margin-left:10%">
<b>4.1.</b> Under <i>Default Organization Level Value</i>, lick the <b>New</b> button 
    <br><br>
<b>4.2.</b> Under <i>Trigger Setting Information</i>, select <b>Profile</b> and name it <b>System Administrator</b>
    <br><br>
<b>4.3.</b>  Click <b>Save</b> to apply the changes
    <br><br>
</p>

 <img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\instant-sync\system-admin.gif" style="width:80%" class="minimized">


<p style="margin-left:5%">
<b>5.</b> If a setup owner already exists:
</p>
<p style="margin-left:10%">
<b>5.1.</b> Click <b>Edit</b> next to it
    <br><br>
<b>5.2.</b> Make sure that the checkbox <i>Disable InstantSynkTrigger</i> is <b>NOT</b> selected.
<br><br>
If the checkbox is selected, <b>unselect</b> it and click <b>Save</b>
</p>
<p style="margin-left:5%">
    <b>5.</b> Proceed with connecting {{ company_name }} to your Salesforce configuration
</p>

 <img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\instant-sync\unselect.gif" style="width:80%" class="minimized">

<hr>

## Connect {{ company_name }} to your Salesforce configuration 

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
    Also, it's possible that you will successfully sign in with Salesforce but won't see the the green confirmation message "Connected". In this case, click Connect again and repeat login attempts until you see the green confirmation message "Connected".

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