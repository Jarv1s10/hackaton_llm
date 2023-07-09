---
description: Learn how to monitor synchronization statistics and connection statuses
---
# Monitoring Synchronization Statistics and Connection Statuses  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>
<div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>
<div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

{{ product_name }} logs items synchronization statistics and monitors connection statuses between Salesforce and mail client account. You can analyze this information and perform the necessary follow-up activities if any problems occur.

!!! warning "Important"
    Depending on your product license, the appearance of your Sync Settings page may be different. Below you can find instructions for the **New** and **Legacy** Sync Settings pages. Refer to the chapter according to the appearance of your Sync Setting page:
    
    * [New Sync Settings page](#new_sync_settings_page)
    * [Legacy Sync Settings page](#legacy_sync_settings_page)

&nbsp;

## New Sync Settings page

{{ short_name }} gathers all synchronization statistics and connection statuses data on the **Sync Settings** page:
<br><br>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\sync-status\sync-settings.png" style="width:27.48%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

* To access **Sync Settings**, open {{ product_name }} in your mailbox, click **Menu**, and go to **Sync Settings**

<br><br><br>

On the **General** tab of the Sync Settings page, you can check the *Synchronization status*, *Number of records in a synchronization scope*, *Last session details*, and control sync using the **Force sync** and **Pause** / **Start** buttons.

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\sync-status\general.png">
</p>
<br>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\sync-status\session-details.png" style="width:47.84%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<br>

* Click **Last session details** to view the logged information about the last synchronization. Also, use the **Refresh** button to update the details if another sync session has run recently

<br><br><br><br>

!!! tip "Tip"
    If you discover a sync issue has occurred, refer to [this article](../Handling-Sync-Issues/) to learn how to handle it

<br>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\sync-status\my-connectivity.png" style="width:23.55%; display:inline-block; vertical-align:middle; margin-left:10px;float: right">
</p>

* To check your Salesforce and mail account connection statuses, go to **My connectivity** under Personal setting

<br><br><br><br><br>

On the **My connectivity** page, you can check the *CRM* and *Email* accounts connection statuses. Also, you can refresh connectivity or change accounts using the corresponding **Refresh** or **Change** buttons.

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\sync-status\connection.png">
</p>

!!! tip "Tip"
    <p>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\sync-status\disconnected.png" style="width:27.0%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
    </p>
    If you discover a *Disconnected* status shown on the tab or if you need to change the access account, refer to [this article](../Renewing-Exchange-and-Salesforce-Account-Credentials/) to learn how to renew the credentials

&nbsp;
***
&nbsp;

## Legacy Sync Settings page

To view this information, [go to Sync dashboard page](../How-to-Open-Sync-Dashboard-(Adaptive-view)/#to_open_sync_dashboard). Here you will find:

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5832c9eac697916f5d052f9a.png)

&nbsp;

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5832ca07903360645bfa68bb.png)

&nbsp;

* The statistics of the last synchronization session, including the information about the number of synchronization issues (if any)
* The Salesforce and Microsoft Exchange connection statuses

You can also use the Dashboard control the synchronization process:

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5832ca2cc697916f5d052f9d.png)

&nbsp;

* To stop {{ product_name }} from synchronizing data, click **Pause**
* To force the synchronization to start immediately, click **Force sync**