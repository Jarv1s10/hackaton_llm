---
description: How to resolve the synchronization error "MALFORMED_QUERY: Semi join sub-selects are only allowed at the top level WHERE expressions..."
---
# How to Resolve *MALFORMED_QUERY: Semi join sub-selects are only allowed at the top level WHERE expressions...* Sync Error
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container"
        style="
        display: inline-block;
        height: 42px;
        width: 162px;
        padding: 5px 10px;
        background-color: #fff;">
        <img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" 
            style="
        	height: 100%;
            object-fit: contain;
            vertical-align: middle;">
</div>
<div class="container"
        style="
        display: inline-block;
        height: 42px;
        width: 163px;
        padding: 5px 10px;
        background-color: #fff;">
        <img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" 
            style="
        	height: 100%;
            object-fit: contain;
            vertical-align: middle;">
</div>
<div class="container"
        style="
        display: inline-block;
        height: 42px;
        width: auto;
        padding: 5px 10px;
        background-color: #fff;">
        <img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" 
            style="
        	height: 100%;
            object-fit: contain;
            vertical-align: middle;">
</div>



&nbsp;

*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

In some cases, you may face a situation where your synchronization is not running, and the following [error message](../Handling-Sync-Issues/) is shown in [Sync Settings Dashboard](../How-to-Open-Sync-Dashboard-%28Adaptive-view%29/):

*MALFORMED_QUERY: Semi join sub-selects are only allowed at the top level WHERE expressions and not in nested WHERE expressions.*

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\contacts-filters-sync-error\error-message.png" style="width:60%;">
</p>

<br><br><br>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\contacts-filters-sync-error\campaign-filter.png" style="width:42.56%; display:inline-block; vertical-align:middle; margin-left:5px; float: right">
</p>

The issue is related to the known [Salesforce API limitation](https://help.salesforce.com/s/articleView?id=sf.c360_a_limits_and_guidelines.htm&type=5), which does not allow using the query with specific items. Usually, such queries are generated when the Salesforce Contacts List View with the Filter by Campaign Name is used in your organization.

&nbsp;

&nbsp;

***

&nbsp;

## How to address the issue

To resolve the described above synchronization error, you need to change the filter (sync scope) for [down-syncing contacts from Salesforce to your mail client](../Synchronization-of-Contacts/) in Sync settings.

!!! warning "Important"
    Depending on your subscription plan, the appearance of your Sync Settings page may be different. Below you can find the troubleshooting steps described for the **New** and **Legacy** Sync Settings pages. Proceed with the steps according to the appearance of your Sync Setting page:
    
    * [New Sync Settings page](#steps_for_the_new_sync_settings_page)
    * [Legacy Sync Settings page](#steps_for_the_legacy_sync_settings_page)

&nbsp;

### Steps for the [new Sync Settings page](../Configuring-Activities-Synchronization-Settings-rg/)

<p style="margin-left:5%">  
<br>
<b>1.</b> Open {{ product_name }}, click <b>Menu</b> and go to <b>Open {{ company_name }} in browser</b>
</p>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\missing-add-sequence-button\settings.png" style="width:22.08%; display:inline-block; vertical-align:middle; margin-left:10px; float: right">
</p>

<p style="margin-left:5%">
<br>
<b>2.</b> Click on your profile picture in the upper right-hand side corner, then go to <b>Settings</b> > <b>Sync section</b>
<br><br><br><br>
</p>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\contacts-filters-sync-error\contact-card.gif" style="width:50%; display:inline-block; vertical-align:middle; margin-left:5px; float: right">
</p>

<p style="margin-left:5%">  
<b>3.</b> On the opened Sync Settings page, find the <a href=../Configuring-Activities-Synchronization-Settings-rg/#contacts_saving>Contacts card</a> and click <b>Customize scope</b>
<br><br><br>
<b>4.</b> In the drop-down list, choose the desired <i>Custom Salesforce view</i> to synchronize only contacts available in the selected Salesforce view
<br><br><br>
<b>5.</b> Click <b>Apply</b> to save the changes
</p>

&nbsp;

&nbsp;

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\contacts-filters-sync-error\start.png" style="width:16.53%; display:inline-block; vertical-align:middle; margin-left:15px; float: right">
</p>

Once the Contact Filter configuration is done, you need to Enable or Force synchronization to check if the issue is resolved.

&nbsp;

***

&nbsp;

### Steps for the [legacy Sync Settings page](../Configuring-Activities-Synchronization-Settings/)

<p style="margin-left:5%">  
<br>
<b>1.</b> Open {{ product_name }}, click <b>Menu</b> and go to <b>Sync Settings</b>
<br><br>
<b>2.</b> On the opened <a href=../How-to-Open-Sync-Dashboard-%28Adaptive-view%29/>Sync Dashboard page</a>, go to <b>Sync Setting</b> > <b>Filters</b>
<br><br>
</p>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\contacts-filters-sync-error\custom-view.gif" style="width:38.06%; display:inline-block; vertical-align:middle; margin-left:12px; float: right">
</p>

<p style="margin-left:5%">  
<b>3.</b> Find the Contacts card and click <b>Customize</b> in the bottom right corner of the card
<br><br><br>
<b>4.</b> Switch to the <b>Custom view</b> option
<br><br><br>
<b>5.</b> In the drop-down list, choose the desired <i>Salesforce contact view</i> to synchronize only contacts available in the selected Salesforce view
<br><br><br>
<b>6.</b> Click <b>Save</b> to apply the changes
</p>

&nbsp;

&nbsp;

Once the Contact Filter configuration is done, you need to Enable or [Force synchronization](../How-to-Open-Sync-Dashboard-%28Adaptive-view%29/#force_rges_sync) to check if the issue is resolved.

&nbsp;

***

&nbsp;

## If the issue still persists

If the troubleshooting steps described above have not resolved the synchronization issue, contact [{{ company_name }} support team](mailto:support@revenuegrid.com) for additional investigation and describe the steps you completed.