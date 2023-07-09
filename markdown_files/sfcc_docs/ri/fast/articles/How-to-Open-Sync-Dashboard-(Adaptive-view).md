---
description: How to set up or customize Revenue Grid sync functioning using Synchronization Dashboard 
---
# How To Open Sync Engine's Dashboard (Sync Settings)  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>
<div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>
<div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*3 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! warning "Important"
    If the Sync settings access page is displayed as a blank window, make sure to disable any adblocking browser extensions (e.g. Adblock Plus or uBlock Origin) for this page and then reload it. This is required because the page uses some scripts which are also used by web ads

&nbsp;

The Sync Settings page is intended to manage the {{ short_company_name }} Sync Engine operation. It is used to set up or customize [{{ company_name }} synchronization functioning](../Synchronization-Engine-An-Overview/) locally, get a detailed overview of your {{ product_name }} usage, and troubleshoot issues. On the Sync settings page, you can:

* [View synchronization statistics and Salesforce / mailbox connection statuses](../Viewing-Synchronization-Statistics-and-Connection-Statuses/)
* [Switch to another Salesforce or mailbox account](../Renewing-Exchange-and-Salesforce-Account-Credentials/)
* Configure activities synchronization on the [new Sync settings page](../Configuring-Activities-Synchronization-Settings-rg/) or the [legacy Sync settings page](../Configuring-Activities-Synchronization-Settings/)
* [Monitor and resolve synchronization issues](../Handling-Sync-Issues/)  

{{ short_company_name }} synchronization functions and settings are mostly identical for MS Exchange / Office 365 and Gmail accounts, with the exception of several [MS Exchange specific functions](../Using-the-Solution-for-Salesforce-and-Gmail/#differences_between_the_exchangeoffice_365_add-in_implementation_and_the_chrome_extension_for_gmail).

&nbsp;

!!! warning "Important"
    Depending on your product license, the appearance of your Sync Settings page may be different. Below you can find instructions on how to access **New** and **Legacy** Sync Settings pages. Proceed with the steps according to the appearance of your Sync Setting page:
    
    * [How to open the new Sync Settings page](#how_to_open_the_new_sync_settings_page)
    * [How to open the legacy Sync Settings page](#how_to_open_the_legacy_sync_settings_page)

&nbsp;

&nbsp;

## How to open the new Sync Settings page

### Open {{ short_company_name }} Sync Settings

<p style="margin-left:4%">
    <b>1.</b> Open the {{ product_name }} Add-In / Chrome Extension in MS Outlook Desktop or On the Web version or Gmail
    <br><br>
</p>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sync-Settings\sync-settings.png" style="width:27.49%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:4%">
    <b>2.</b> Click the <b>&#x2630; Menu</b> button in {{ product_name }} and select <b>Sync settings</b>, or <b>Set up Sync</b> to <a href=../Authorizing-Sync-Engine-to-Work-with-Your-Data/>activate {{ short_name }} Sync Engine first</a>
    <br><br><br><br>
</p>

Next, you will see the following [{{ short_name }} Sync Settings page](../Configuring-Activities-Synchronization-Settings-rg/) opened in a browser window:

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sync-Settings\sync-page.png" class="minimized">
</p>

&nbsp;

### Force {{ short_company_name }} Sync

To get your data synchronized quickly, you can initiate a sync session ahead of the one-per-30-minutes schedule. To do that:

* Click <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sync-Settings\flash.png" style="width:20px; display:inline-block; vertical-align:middle;">**Force sync** on the **General** tab of Sync Settings

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sync-Settings\force.png">
</p>

&nbsp;

!!! note "Note"
    The Sync session will not be initiated instantly, but within 1-3 minutes. Additionally, please note that  there is a limit on how often Sync forcing can be initiated

&nbsp;

&nbsp;

### Pause and resume {{ short_company_name }} Sync

If you need to pause {{ short_name }} sync for any reason, you can do that on the Sync Settings page as well. To do that: 

* Click &#10073;&#10073; **Pause** on the **General** tab of Sync Settings

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sync-Settings\pause.png">
</p>

!!! note "Note"
    Note that when {{ short_name }} Sync is paused or [suspended due to an error](../Handling-Sync-Issues/), a number of key {{ product_name }} features are unavailable. Please refer to [this table](../AddIn-vs-Sync-Functions/) for more information

<br>

* To resume {{ short_name }} Sync after you have paused it, click &#9658; **Start** on the **General** tab of Sync Settings

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sync-Settings\start.png">
</p>

&nbsp;
***
&nbsp;

## How to open the legacy Sync Settings page

### To open Sync Dashboard:

**1\.**  Open the {{ product_name }} Add-In / Chrome Extension in MS Outlook Desktop or On the Web version or Gmail

**2\.**  Click the **☰** **Menu** button in {{ product_name }} Add-In / Chrome Extension and select **Sync settings**, or **Set up Sync** to [activate {{ short_name }} Sync Engine first](../Authorizing-Sync-Engine-to-Work-with-Your-Data/)   

<details><summary> >>> Click to see an animation <<< </summary>
<p><img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5b9134712c7d3a03f89e85c5.gif"style="width: 40%; height: 50%;">
</p></details>

&nbsp;

**3\.** Next, you may also need to sign in over secure [Salesforce OAuth 2.0](https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_flows.htm&type=5) or [Exchange/Office 365 OAuth 2.0](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow) or [Gmail OAuth 2.0](https://developers.google.com/identity/sign-in/web/sign-in) in a browser page that appears, depending on your {{ short_name }} Org's configuration  

&nbsp;

Next, you will see the following {{ short_name }} Sync Settings page opened in a browser window:

<p>
    <img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\58343ddbc697916f5d053c3c.png" class="minimized">
</p>

&nbsp;

### Force {{ short_name }} Sync

On the Dashboard, to get your data synchronized quickly, you can initiate a sync session ahead of the one-per-30-minutes schedule. To do that:

- Open Sync dashboard
- Click **Force Sync**

![](../assets/images/Using-SmartCloud-Connect/How-To-s/Sync-Settings/force-sync.png)

&nbsp;

!!! note "Note"
    The Sync session will not be initiated instantly, but within 1-3 minutes. Additionally, please note that  there is a limit on how often Sync forcing can be initiated

&nbsp;

&nbsp;

### Pause {{ short_name }} Sync

If you need to pause {{ short_name }} sync for any reason, you can do that from the Dashboard as well. To do that: 

- Open Sync Dashboard
- Click **Pause**

![](../assets/images/Using-SmartCloud-Connect/How-To-s/Sync-Settings/pause-sync.png)

!!! note "Note"
    Note that when {{ short_name }} Sync is paused or [suspended due to an error](../Handling-Sync-Issues/), a number of key {{ product_name }} features are unavailable. Please refer to [this table](../AddIn-vs-Sync-Functions/) for more information


<style>
  .banners {
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .banners a.button {
      background-color: #FFC827;
      color: #2F3341;
      box-shadow: 0 5px 35px rgba(146, 146, 146, 0.2);
      padding: 20px;
      font-family: Graphic, arial;
      font-weight: 600;
      line-height: 24px;
      margin-top: -100px;
      border-radius: 3px;
      cursor: pointer;
      transition: .1s;
  }

  .banners a.button:hover {
    transform: scale(1.05);
  }

  .banners a.button a:hover,
  .banners a.button a:visited {
      color: #2F3341;
  }

  .banner-3 a.button {
    margin-left: 45%;
  }
</style>

<br>
<div class="banners banner-3">
  <img src="../../assets/images/banners/banner-3.svg" style="width: 100%; height: 100%;">
  <a class="button" href="https://revenuegrid.com/sign-up/?utm_source=kb_rg&utm_medium=referral&utm_campaign=eac&utm_content=banner" target="_blank">Try {{ company_name }} for free</a>
</div>