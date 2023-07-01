---
description: How to renew Exchange / Office 365 / Gmail and Salesforce access credentials
---
# Renewing Exchange / Office 365 / Gmail and Salesforce Access Credentials  
  

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

If your mailbox or Salesforce credentials get changed or expire, {{ short_name }} will no longer be able to work with your data. However, you can easily renew your Salesforce and/or MS Exchange authorization to let {{ product_name }} regain access to your mailbox and/or CRM data.

&nbsp;

## Microsoft Access Tokens Expiration Explained

!!! tip "Tip"
    See [this Microsoft article](https://docs.microsoft.com/en-us/azure/active-directory/develop/refresh-tokens) for complete information on refresh tokens

&nbsp;

When an [access token](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-configurable-token-lifetimes#access-tokens) expires, MS Office clients use a valid [refresh token](https://docs.microsoft.com/en-us/azure/active-directory/develop/refresh-tokens) to obtain a new access token. This exchange succeeds if the user's initial authentication is still valid.  
By default, refresh tokens are valid for 90 days; however, with continuous use they can remain valid until [revoked](../Revoke-Token/).  

Refresh tokens can get auto-invalidated in the following cases:  

- User's password has changed since the refresh token was issued

- If the local Exchange/O365 Admin [applies conditional access policies](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/howto-conditional-access-session-lifetime) that restrict access to the resource the user is trying to access 

&nbsp;

* * *

&nbsp;

## All data access renewal actions are performed in Sync Settings

&nbsp;

To open {{ product_name }} Sync Settings from the Sidebar:  

**1\.**  Open the {{ product_name }} Add-In / Chrome Extension in MS Outlook Desktop or On the Web version or Gmail

**2\.**  Click the **☰** **Menu** button in {{ product_name }} Add-In / Chrome Extension and select **Sync settings** or **Set up Sync** to [activate {{ short_name }} Sync Engine first](../Authorizing-Sync-Engine-to-Work-with-Your-Data/)   

<details><summary> >>> Click to see an animation <<< </summary>
<p><img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5b9134712c7d3a03f89e85c5.gif" style="width: 45%; height: 45%;">
</p></details>

&nbsp;

!!! warning "Important"
    Depending on your license, the appearance of your Sync Settings page may be different. Below you can find instructions on how to renew access credentials on the **Legacy** and **New** Sync Settings pages. Proceed with the steps according to the appearance of your Sync Setting page:

    * [New Sync Settings page](#new_sync_settings_page)

    * [Legacy Sync Settings page](#legacy_sync_settings_page)

<br>

## New Sync Settings page

This section includes access renewal steps on the [new Sync Settings page](../Configuring-Activities-Synchronization-Settings-rg/) for the following mailbox accounts and Salesforce:

* [Microsoft Office 365](#refreshing_rges_ms_office_365_access)
* [Microsoft Exchange](#refreshing_rges_ms_exchange_access)
* [Google Workspace](#refreshing_rges_gmail_access)
* [Salesforce](#refreshing_rges_salesforce_access)

<br>
<hr>
<br>

### Refreshing {{ short_name }} MS Office 365 access

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\renew-access-credentials\my-connectivity.png" style="width:35%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
    <br>
    <b>1.</b> On the opened Personal Settings page, go to <b>My connectivity</b>
    <br><br><br><br><br><br>
</p>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\renew-access-credentials\email-config-365.png" style="width:43%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
    <b>2.</b> Find the <b>Email configuration</b> tab and:
</p>

<ul style="margin-left:4%">
    <li>click <b>Refresh</b> and log in with your account credentials in the Microsoft Online OAuth window that appears to refresh your access</li>
    <p>or</p>
    <li>click <b>Change</b> to use other login credentials or change the mailbox access type</li>
</ul>
<br>

If you have clicked **Change**, you need to select the **mailbox access type** and sign in with your credentials in the login window that appears.

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\renew-access-credentials\mailbox-types.png">
</p>

!!! note "Note"
    If your admin has restricted some mailbox access type(s), you may see only one or two options available instead of all three

&nbsp;
***
&nbsp;

### Refreshing {{ short_name }} MS Exchange access

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\renew-access-credentials\my-connectivity.png" style="width:35%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
    <br>
    <b>1.</b> On the opened Sync Settings page, go to <b>My connectivity</b> under <b>Personal Settings</b>
    <br><br><br><br><br><br>
</p>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\renew-access-credentials\email-config-exch.png" style="width:43%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
    <br>
    <b>2.</b> Find the <b>Email configuration</b> tab and click <b>Refresh</b> to start the credentials renewing process
    <br><br><br><br><br><br><br>
</p>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\renew-access-credentials\exch-login.png" style="width:45%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
    <br>
    <b>3.</b> Enter your MS Exchange password and click <b>Connect</b> to refresh the MS Exchange access token or update the password
    <br><br><br><br><br><br><br><br>
</p>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\renew-access-credentials\exch-advanced.png" style="width:45%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<ul style="margin-left:4%">
    <li>Note that under <b>Advanced Setup</b> you can also specify a new <a href=http://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/start-using-web-services-in-exchange>EWS</a> configuration URL for your mailbox</li>
</ul>

<br><br><br><br><br><br><br>

If you need to use other login account credentials or change the **mailbox access type**:

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\renew-access-credentials\exch-change.png" style="width:43%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

* Click **Change** on the Email configuration tab

<br><br><br><br><br><br>

* Select the relevant **mailbox access type**

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\renew-access-credentials\mailbox-types.png">
    <br>
</p>

* Enter your account credentials in the login window that appears

&nbsp;

!!! note "Note"
    If your admin has restricted some mailbox access type(s), you may see only one or two options available instead of all three

&nbsp;
***
&nbsp;

### Refreshing {{ short_name }} Gmail access

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\renew-access-credentials\my-connectivity.png" style="width:35%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
    <br>
    <b>1.</b> On the opened Sync Settings page, go to <b>My connectivity</b> under <b>Personal Settings</b>
    <br><br><br><br><br><br>
</p>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\renew-access-credentials\email-config-google.png" style="width:43%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
    <b>2.</b> Find the <b>Email configuration</b> tab and:
</p>

<ul style="margin-left:4%">
    <li>click <b>Refresh</b> and log in your account credentials in the Google OAuth window that appears to refresh your access</li>
    <p>or</p>
    <li>click <b>Change</b> to use other login credentials or change the mailbox access type</li>
</ul>
<br>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\renew-access-credentials\google-accesses.png" style="width:48%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
    <br>
    <b>3.</b> In the following dialog window, click <b>Continue</b> to re-authorize {{ short_name }} access to your Google data
    <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
</p>

If you have clicked **Change**, you need to select the **mailbox access type** and sign in with your credentials in the login window that appears.

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\renew-access-credentials\mailbox-types.png">
</p>

!!! note "Note"
    If your admin has restricted some mailbox access type(s), you may see only one or two options available instead of all three

&nbsp;
***
&nbsp;

### Refreshing {{ short_name }} Salesforce access

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\renew-access-credentials\my-connectivity.png" style="width:35%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
    <br>
    <b>1.</b> On the opened Sync Settings page, go to <b>My connectivity</b> under <b>Personal Settings</b>
    <br><br><br><br><br><br>
</p>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\renew-access-credentials\crm.png" style="width:52%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
    <b>2.</b> Find the <b>CRM</b> tab and:
</p>

<ul style="margin-left:4%">
    <li>click <b>Refresh</b> and log in with your Salesforce credentials in the Salesforce OAuth window that appears to refresh your access</li>
    <p>or</p>
    <li>click <b>Change</b> to use a different Salesforce access type</li>
</ul>
<br>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\renew-access-credentials\sf-types.png" style="width:50.9%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p>
    <br>
    If you have clicked <b>Change</b>, then you need to select the <b>Salesforce access type</b> and sign in with your account credentials in the login window that appears.
    <br><br><br><br><br><br>
</p>

&nbsp;

&nbsp;

***

&nbsp;


## Legacy Sync Settings page

This section includes access renewal steps on the legacy Sync Settings page for the following mailbox accounts and Salesforce:

* [Microsoft Office 365](#refreshing_rges_ms_office_365_access_1)
* [Microsoft Exchange](#refreshing_rges_ms_exchange_access_1)
* [Google Workspace](#refreshing_rges_gmail_access_1)
* [Salesforce](#refreshing_rges_salesforce_access_1)

&nbsp;

### Refreshing {{ short_name }} MS Office 365 access

**1\.** On the [{{ short_name }} Sync Dashboard](../How-to-Open-Sync-Dashboard-(Adaptive-view)/) page, go to **Sync settings**(1) > **E-Mail Configuration**(2) in the navigation pane on the left

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b915c5d2c7d3a03f89e87fd.png" class="minimized">
</p>

&nbsp;

**2\.** To refresh your MS Office 365 authorization: click **Refresh** (1) and enter your login credentials in the Microsoft Online OAuth window that appears  

**or**    

To use other login credentials or update your MS Office 365 access password if it was changed, click **Change** (2) next to *Change E-Mail Account or Server*   

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b915fed2c7d3a03f89e8837.png" class="minimized">
</p>

&nbsp;

**3\.** Enter your login credentials in the corresponding fields of the [OAuth](https://en.wikipedia.org/wiki/OAuth) window that appears

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b6b2a3d2c7d3a03f89d7bba.png">
</p>

&nbsp;

* * *

&nbsp;

### Refreshing {{ short_name }} MS Exchange access

**1\.** On the [{{ short_name }} Sync Dashboard](../How-to-Open-Sync-Dashboard-(Adaptive-view)/) page, go to **Sync settings** > **E-Mail Configuration** in the navigation pane on the left   

**2\.** To refresh MS Exchange access token, click **Refresh** in {{ short_name }} Sync Dashboard window that appears

<p><img src="../../assets/images/Install-and-Run/refresh_exchange.png" class="minimized">
</p>

&nbsp;

 **or**
 
&nbsp;

To use other login credentials or update your MS Exchange mailbox access password if it was changed, click **Change** next to _Change E-Mail Account or Server_, select **Microsoft Exchange, Outlook.com or unsure** and enter the new mailbox login credentials in the following window.

Note that here you can also specify a new [EWS](http://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/start-using-web-services-in-exchange) configuration URL for your mailbox.

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b6b2ad82c7d3a03f89d7bc1.png" class="minimized">
</p>

&nbsp;

* * *

&nbsp;

### Refreshing {{ short_name }} Gmail access

**1\.** On the [{{ short_name }} Sync Dashboard](../How-to-Open-Sync-Dashboard-(Adaptive-view)/) page, go to **Sync Settings** > **E-Mail Configuration** in the navigation pane on the left

**2\.** Сlick **Refresh** to refresh an expired access token or update the password

<p><img src="../../assets/images/Using-SmartCloud-Connect/How-To-s/Gmail/refresh_change.png" class="minimized">
</p>

&nbsp;

**3\.** Enter your Gmail login credentials in the Gmail OAuth window that appears  

**4\.** In the following dialog window, click **Allow** to re-authorize {{ short_name }} access to your Gmail data  

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Gmail\chrome_allow.png" class="minimized">
</p></details>

&nbsp;

* * *

&nbsp;

### Refreshing {{ short_name }} Salesforce access

**1\.** On the [{{ short_name }} Sync Dashboard](../How-to-Open-Sync-Dashboard-(Adaptive-view)/) page, go to **Sync settings**(1) > **CRM**(2) in the navigation pane on the left

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b915a782c7d3a03f89e87e0.png" class="minimized">
</p>

&nbsp;

**2\.** To update the Salesforce login token: click **Refresh** under Salesforce Access on the right-hand side if you need

**or**    

To use different Salesforce login credentials or update your password: click **Change** next to *Change Salesforce account*

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b9159382c7d3a03f89e87d2.png" class="minimized">
</p>

&nbsp;

**3\.** Enter your Salesforce login credentials or select a previously saved account from among Saved Usernames in Salesforce OAuth window that appears

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b913e520428631d7a8ac762.png">
</p>


