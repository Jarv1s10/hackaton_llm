---
description: Learn about configuring Collaborative Forecasts in Salesforce
---

# Collaborative Forecasts in Salesforce

*4 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

[Collaborative Forecasts](https://help.salesforce.com/s/articleView?id=sf.forecasts3_setup_intro.htm&type=5) is the Salesforce functionality that enables the sales team to plan and predict their sales process and sales results.   

Turning on and configuring Collaborative Forecasts in Salesforce is an essential prerequisite for using Revenue Grid forecasts and reports, which are built upon the relevant data retrieved from Salesforce. 

!!! note "Note"
    It’s recommended to enable Collaborative Forecasts in Salesforce. But even if they are not enabled in Salesforce, you will see the related reports. However, the Quota will not be displayed in the reports. 
    <br>

 <hr>

## 1. Turn on Collaborative Forecasts 

<p style="margin-left:7%">
<b>1.1.</b> Switch to Lightning Experience as described in <a href="https://help.salesforce.com/s/articleView?language=en_US&id=000337767&mode=1&type=1" target="_blank">this article</a>
<br><br>
<img src="..\..\assets\images\intelligence-package\collaborative-forecasts\gear.png" style="width: 30%; float: right;margin-left:2%; margin-right: 10%;">
<b>1.2.</b> Click the <b>Gear</b> (Setup Menu) icon in the upper right corner of the page to open <a href="https://help.salesforce.com/articleView?id=basics_nav_setup.htm&type=0" target="_blank">Salesforce Setup menu</a> 
<br><br><br><br><br><br>
<img src="..\..\assets\images\intelligence-package\collaborative-forecasts\forecasts-settings.png" style="width: 30%; float: right;margin-left:2%; margin-right: 10%;">
<br>
<b>1.3.</b> In the <i>Quick Search</i> box in the upper left corner, type <i>"Forecasts Settings"</i> to quickly find the necessary tab
<br><br>
<b>1.4.</b> Select <b>Forecast Settings</b>  
<br><br><br><br><br><br>
<b>1.5.</b> If the <b>Enable Forecast</b> switch button is disabled, turn it on, so it's "<i>Active</i>"
<br><br>
<img src="..\..\assets\images\intelligence-package\collaborative-forecasts\active.png">
<br>
<br><br>
</p>

!!! note "Note"
    After you turn on the Enable Forecast switch button, the forecast called *Opportunity Revenue* will automatically appear on the list *Available Forecast Types*. This forecast is enough to get Revenue Grid's functionality running. Refer to [this Salesforce article](https://help.salesforce.com/s/articleView?id=sf.forecasts3_enabling_data_sources.htm&type=5) for more information about forecast types and their configuration. 


<hr>


## 2. Select Collaborative Forecast Rollup 

You can select between two collaborative forecasts rollup options: 
<p style="margin-left:5%">
    <b>Single forecast category rollups</b> combine the opportunities within each forecast category into separate forecasts for each category. It's a default rollup method. 
<br>
    <b>Cumulative forecast rollups</b> combine opportunities from multiple forecast categories into cumulative forecast categories. 
</p>

!!! tip "Tip"
    Salesforce-recommended rollup method is the **cumulative rollup** . You can read more about the collaborative forecasts roll-up methods in [this Salesforce article](https://help.salesforce.com/s/articleView?id=sf.forecasts3_cumulative_columns_overview.htm&type=5)
<br>

To select the necessary collaborative forecasts rollup option:

<p style="margin-left:7%">
    <b>3.1.</b> On the  <i>Forecasts Settings</i> page, find the section <b>Manage Forecast Rollups</b>
        <br><br>
    <b>3.2.</b> Click <b>Edit</b>
        <br><br>
    <b>3.3.</b> Select the preferred forecast rollup method 
    <br><br>
        <img src="..\..\assets\images\intelligence-package\collaborative-forecasts\3.3.png" class="minimized" >
    <br>
</p>

!!! warning "Important" 
    Switching from one rollup method to another **deletes** adjustments for all active forecast types. 
    
<hr>

## 3. Set the default date range  

The default date range is the date range for displaying the forecasts grid on the forecasts page. Refer to [this Salesforce article](https://help.salesforce.com/s/articleView?id=sf.forecasts3_defining_forecasts_range.htm&type=5) for more detailed information about the date range. 

!!! tip "Tip"
    The **default date range must be set to Quarter** to ensure that users' quotas are correctly displayed in Revenue Grid. If *Forecast period* is set to *Quarter*, Revenue Grid will **not** be able to retrieve the data necessary for reporting and forecasting 

<p style="margin-left:7%"> 
    <b>4.1.</b> On the <i>Forecasts Settings</i> page, find the section <b>Choose a Default Date Range</b>
        <br><br>
    <b>4.2.</b> Click <b>Edit</b> 
        <br><br>
    <b>4.3.</b> Specify the preferred
 </p>
 <ul style="margin-left:12%">
        <li>Forecast period</li>
        <li>Starting On</li>
        <li>Extending For</li>
 </ul>
 <p style="margin-left:7%"> 
    <b>4.4.</b> Click <b>Save</b> to apply the changes 
    <br><br>
        <img src="..\..\assets\images\intelligence-package\collaborative-forecasts\4.3.png" class="minimized">
        <br>
</p>
 
 
