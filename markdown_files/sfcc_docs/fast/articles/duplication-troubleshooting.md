---
description: Unexpected sync behavior: what to do if RG Email Sidebar creates multiple copies of the same calendar event
---
# Troubleshooting Events Duplication in Salesforce


<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>
<div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

<br>

*5 min read*

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

The creation of multiple copies of the same calendar event in [sync sessions](../Synchronization-Engine-An-Overview/) usually indicates that besides {{ product_name }}, there is other software transferring data between your email service and Salesforce API, causing data transfer conflicts with {{ short_name }}.

When you are using {{ product_name }}, there should be no other software running that performs data transfer between your email service and [Salesforce API](http://trailhead.salesforce.com/modules/api_basics/units/api_basics_overview) (e.g., *Salesforce Lightning Sync*, *Salesforce Inbox*, *Salesforce for Outlook*, *Einstein Activity Capture*, etc.) Running different MS Exchange – Salesforce sync applications simultaneously will cause sync conflicts and items duplication. If you encounter this kind of unexpected behavior, please check that with your Salesforce admin or, if you are a Salesforce admin, check for such software in the following places:
 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1\.** Salesforce Setup > Apps > App Manager
 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2\.** [Connected Apps](https://help.salesforce.com/articleView?id=connected_app_overview.htm&type=5)
 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**3\.** [Salesforce Login History](https://help.salesforce.com/articleView?id=users_login_history.htm&type=5)

&nbsp;

After you find apps which cause sync conflicts, please refer to [this Salesforce Help article](https://help.salesforce.com/s/articleView?id=sf.exchange_sync_sfo_sync_conflict.htm&type=5) or to the step-by-step guide to learn how to disable them. Please also note that apps which use Salesforce API and do **not** exchange data between Salesforce and MS Exchange / Office 365 / Gmail will **not** cause sync conflicts.

Before removing any duplicates created in Salesforce, it's necessary to disable the app causing this issue to ensure that the duplication stops.

&nbsp;
***

## Disable Lightning Sync for Outlook users

<br>
**1\.** Switch to Lightning Experience as described in [this Salesforce article](https://help.salesforce.com/articleView?id=000337767&type=1&mode=1)
<br><br>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\duplication-troubleshooting\open-setup.png" style="width:50%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<br>
**2\.** Click the **Gear** (Setup Menu) icon in the upper right corner of the page and open [Salesforce Setup](https://help.salesforce.com/articleView?id=basics_nav_setup.htm&type=0)
<br><br><br><br><br><br>

**3\.** In the *Quick Search* field in the upper left corner, type "*Sync*" to quickly find the necessary setting  

<br>
**4\.** Select the option  **Outlook Integration and Sync**

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\duplication-troubleshooting\outlook-integr.png" class="minimized" style="width:95%">
</p>

<br><br>
**5\.** Next, on the *Outlook Integration And Lightning Sync*, disable the Lightning Sync switch button

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\duplication-troubleshooting\outlook-integr-off.png" class="minimized" style="width:95%">
</p>

<br>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\duplication-troubleshooting\sync-settings.png" style="width:27.49%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

**6\.** After that, open {{ product_name }} in MS Outlook, click the <b>☰&nbsp;Menu</b> button in the upper left corner of the Add-In's interface, and select **Sync Settings**

<br><br>

!!! warning "Important"
    Depending on your subscription plan, the appearance of your Sync Settings page may be different. Below you can find the steps described for the **New** and **Legacy** Sync Settings pages. Proceed with the steps according to the appearance of your Sync Setting page

<br>

**Steps for the [new Sync Settings page](../Configuring-Activities-Synchronization-Settings-rg/)**

<br>
**7\.** On the opened Sync Settings page, go to the *Issues* tab, find the events duplicates in the list, and remove them

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\duplication-troubleshooting\issues.png">
</p>

<br><br>

**8\.** Go back to the *General* tab and click the **Force sync** button

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\duplication-troubleshooting\force.png">
</p>

<br><br>

**Steps for the [legacy Sync Settings page](../Configuring-Activities-Synchronization-Settings/)**

<br>
**7\.** On the opened Sync Settings page, click on the *Issues* section, then go to **Events** to see the list of all events duplicates and remove them

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\duplication-troubleshooting\issues-events-old.png" class="minimized" style="width:95%">
</p>

<br>
**8\.** Go back to the *Dashboard* section and click the **Force sync** button

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\duplication-troubleshooting\force-sync-old.png" class="minimized" style="width:95%">
</p>

&nbsp;

***

## Disable Lightning Sync for Gmail users

<br>
**1\.** Switch to Lightning Experience as described in [this Salesforce article](https://help.salesforce.com/articleView?id=000337767&type=1&mode=1)   
<br><br>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\duplication-troubleshooting\open-setup.png" style="width:50%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<br>
**2\.** Click the **Gear** (Setup Menu) icon in the upper right corner of the page and open [Salesforce Setup](https://help.salesforce.com/articleView?id=basics_nav_setup.htm&type=0)
<br><br><br><br><br><br>

**3\.** In the *Quick Search* field in the upper left corner, type "*Sync*" to quickly find the necessary setting  

<br>
**4\.** Select the option  **Gmail Integration and Sync**  

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\duplication-troubleshooting\gmail-integr.png" class="minimized" style="width:95%">
</p>

<br>
**5\.** Next, on the *Gmail Integration And Lightning Sync*, disable the Lightning Sync switch button  

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\duplication-troubleshooting\gmail-integr-off.png" class="minimized" style="width:95%">
</p>

<br>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\duplication-troubleshooting\sync-settings.png" style="width:27.49%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

**6\.** After that, open {{ product_name }} in Gmail, click the <b>☰&nbsp;Menu</b> button in the upper left corner of the Add-In's interface, and select **Sync Settings**

<br><br>

!!! warning "Important"
    Depending on your subscription plan, the appearance of your Sync Settings page may be different. Below you can find the steps described for the **New** and **Legacy** Sync Settings pages. Proceed with the steps according to the appearance of your Sync Setting page

<br>

**Steps for the [new Sync Settings page](../Configuring-Activities-Synchronization-Settings-rg/)**

<br>
**7\.** On the opened Sync Settings page, go to the *Issues* tab, find the events duplicates in the list, and remove them

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\duplication-troubleshooting\issues.png">
</p>

<br><br>

**8\.** Go back to the *General* tab and click the **Force sync** button

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\duplication-troubleshooting\force.png">
</p>

<br><br>

**Steps for the [legacy Sync Settings page](../Configuring-Activities-Synchronization-Settings/)**

<br>
**7\.** On the opened Sync Settings page, click on the *Issues* section, then go to **Events** to see the list of all events duplicates and remove them

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\duplication-troubleshooting\issues-events-old.png" class="minimized" style="width:95%">
</p>

<br>
**8\.** Go back to the *Dashboard* section and click the **Force sync** button

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\duplication-troubleshooting\force-sync-old.png" class="minimized" style="width:95%">
</p>

&nbsp;

***

## Disable Einstein Activity Capture  

<br>
**1\.** Switch to Lightning Experience as described in [this Salesforce article](https://help.salesforce.com/articleView?id=000337767&type=1&mode=1)   
<br><br>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\duplication-troubleshooting\open-setup.png" style="width:50%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<br>
**2\.** Click the **Gear** (Setup Menu) icon in the upper right corner of the page and open [Salesforce Setup](https://help.salesforce.com/articleView?id=basics_nav_setup.htm&type=0)
<br><br><br><br><br><br>

**3\.** In the *Quick Search* field in the upper left corner, type "*Einstein*" to quickly find the necessary setting  

<br>
**4\.** Select the option  **Settings**  

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\duplication-troubleshooting\einstein.png" class="minimized" style="width:95%">
</p>

<br><br>
**5\.** On the *Settings* tab, disable Einstein Activity Capture  

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\duplication-troubleshooting\einstein-off.png" class="minimized" style="width:95%">
</p>

<br>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\duplication-troubleshooting\sync-settings.png" style="width:27.49%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

**6\.** After that, open {{ product_name }} in your email service, click the <b>☰&nbsp;Menu</b> button in the upper left corner of the Add-In's interface, and select **Sync Settings**

<br><br>

!!! warning "Important"
    Depending on your subscription plan, the appearance of your Sync Settings page may be different. Below you can find the steps described for the **New** and **Legacy** Sync Settings pages. Proceed with the steps according to the appearance of your Sync Setting page

<br>

**Steps for the [new Sync Settings page](../Configuring-Activities-Synchronization-Settings-rg/)**

<br>
**7\.** On the opened Sync Settings page, go to the *Issues* tab, find the events duplicates in the list, and remove them

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\duplication-troubleshooting\issues.png">
</p>

<br><br>

**8\.** Go back to the *General* tab and click the **Force sync** button

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\duplication-troubleshooting\force.png">
</p>

<br><br>

**Steps for the [legacy Sync Settings page](../Configuring-Activities-Synchronization-Settings/)**

<br>
**7\.** On the opened Sync Settings page, click on the *Issues* section, then go to **Events** to see the list of all events duplicates and remove them

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\duplication-troubleshooting\issues-events-old.png" class="minimized" style="width:95%">
</p>

<br>
**8\.** Go back to the *Dashboard* section and click the **Force sync** button

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\duplication-troubleshooting\force-sync-old.png" class="minimized" style="width:95%">
</p>