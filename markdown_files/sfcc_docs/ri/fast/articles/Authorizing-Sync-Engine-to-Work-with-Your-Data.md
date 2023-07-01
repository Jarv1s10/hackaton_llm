---
description: How to authorize the Sync Engine to work with your data (Sync Activation) 
---
# Authorizing Sync Engine to Work with Your Data (Sync Activation)  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>
<div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*3 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

This article describes in which cases you need to activate [{{ company_name }} Synchronization](../Synchronization-Engine-An-Overview/) and instructions on authorizing the Sync Engine to work with your data.

!!! tip "Tip"
    Many customers ensure that {{ company_name }} Sync is mass-activated for the end users by the local Admin, so no extra setup actions are required. See this article for more information on [{{ short_name }} mass deployment scenarios](../Email-Integration-Full-Deployment-Scenarios/)

<br><br>

Users need to **activate [{{ short_company_name }} Synchronization](../Synchronization-Engine-An-Overview/)** in the following cases:

- on the first start via [the corresponding dialog](../How-to-Install-and-Run-the-Solution-for-Office-365-Mailboxes/#ii_rg_email_sidebar_logon), if {{ short_name }} Sync was not [mass-activated by the local Admin](../Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/), for example, because [Impersonated access](../Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/) cannot be used in your mail client configuration

- in case {{ short_name }} Sync's mailbox authorization expired or your mailbox password [was changed](../Renewing-Exchange-and-Salesforce-Account-Credentials/)

- if you notice that [{{ product_name }} functions performed by {{ short_name }} Sync](../AddIn-vs-Sync-Functions/) are **not** carried out, and Sync is not  [paused](../How-to-Open-Sync-Dashboard-(Adaptive-view)/#pause_and_resume_rg_sync) or [suspended due to an error](../Handling-Sync-Issues/)

- [the corresponding dialog](../How-to-Install-and-Run-the-Solution-for-Office-365-Mailboxes/#ii_rg_email_sidebar_logon) also appears automatically in the [Sidebar](../Introduction/) if 6 consequential [{{ short_name }} synchronization](../Synchronization-Engine-An-Overview/) attempts get rejected by your email server

!!! note
    If Sync activation is skipped, a number of [key {{ product_name }} features performed by {{ short_name }} Synchronization](../AddIn-vs-Sync-Functions/) will be unavailable

<br><br>

If {{ short_name }} Sync stops [due to an error](../Handling-Sync-Issues/), the end users or the Admin user get an automatic email notification with instructions how to re-enable it:

<p><img src="..\..\assets\images\Install-and-Run\SyncAuth\sync-email.png"></p>

&nbsp;

!!! warning "Important"
    If you are using several different email boxes for your correspondence (not [aliases](https://support.office.com/en-us/article/add-or-remove-an-email-alias-in-outlook-com-459b1989-356d-40fa-a689-8f285b13f1f2)), make sure to authorize [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/) data access for the same email box as one for which you installed the [Add-In](../Introduction/), otherwise the [Sync engine functions](../AddIn-vs-Sync-Functions/) will work incorrectly even though {{ short_name }} Sync will appear to be running

&nbsp;

&nbsp;
***
&nbsp;

## Activate {{ short_name }} Sync for MS Exchange

<p>
    <img src="..\..\assets\images\Install-and-Run\SyncAuth\new_dialog.png" style="width:45.72%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
    <br>
    To activate (reactivate) your {{ short_name }} Sync engine for MS Exchange:
    <br><br>
</p>

<ul style="margin-left:4%">
    <li>Enter your Exchange mailbox's Login and Password and click <b>Connect to Exchange</b></li>
</ul>

<p style="margin-left:2%">
    <br>
    In some configurations, you may also need to enter a valid <a href=https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/start-using-web-services-in-exchange>Exchange Web Services link</a> specific to your company's Exchange configuration. To do that, click <b>More v</b> icon and paste the EWS link provided by your local Exchange Admin into the field.
    <br><br><br><br>
</p>

After access has been authorized, [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/) will start running every 30 minutes 24/7 for this email account.

<br>

Also, refer to these instructions if you want to [**pause** the synchronization](../How-to-Open-Sync-Dashboard-(Adaptive-view)/#pause_and_resume_rg_sync) or completely [**disable** {{ short_name }} Sync Engine](../Uninstalling-All-Product-Components/#full_sync_engine_disabling).

!!! tip
    You may update both mailbox and Salesforce accounts in sync settings at any point later. Refer to [this article](../Renewing-Exchange-and-Salesforce-Account-Credentials/) to learn how

&nbsp;
***
&nbsp;

## Activate {{ short_name }} Sync for Office 365

<p>
    <img src="..\..\assets\images\Install-and-Run\SyncAuth\o365-login.png" style="width:45.72%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
    <br>
     To activate (reactivate) your {{ short_name }} Sync engine for Office 365:
</p>

<p style="margin-left:4%">
    <br>
    <b>1.</b> Click the <b>Connect to Office 365</b> button. A browser window with Office 365 login page will be opened
    <br><br><br><br><br><br><br><br>
</p>

<p>
    <img src="..\..\assets\images\Install-and-Run\SyncAuth\o365-sign-in.png" style="width:52.87%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:4%">
    <br>
    <b>2.</b> Enter your Office 365 login credentials in the O365 <a href=https://oauth.net/2/>OAuth 2.0</a> dialog or pick an account from the list when available
    <br><br><br><br><br><br><br><br>
</p>

<p>
    <img src="..\..\assets\images\Install-and-Run\SyncAuth\o365-perm.png" style="width:52.87%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:4%">
    <br>
    <b>3.</b> Next, click <b>Accept</b> to grant {{ company_name }} Email Sidebar permissions to work with your Office 365 data<br><br>
    Note, that you may not see this dialog if permissions were granted earlier by you or your admin.
    <br><br><br><br><br><br><br><br><br><br><br><br>
</p>

After access has been authorized, [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/) will start running every 30 minutes 24/7 for this email account.

<br>

Also, refer to these instructions if you want to <a href="../How-to-Open-Sync-Dashboard-(Adaptive-view)/#pause_and_resume_rg_sync" target="_blank"><b>pause</b> the synchronization</a> or completely <a href="../Uninstalling-All-Product-Components/#full_sync_engine_disabling" target="_blank"><b>disable</b> {{ short_name }} Sync Engine</a>.

!!! tip
    You may update both mailbox and Salesforce accounts in sync settings at any point later. Refer to [this article](../Renewing-Exchange-and-Salesforce-Account-Credentials/) to learn how

&nbsp;
***
&nbsp;

## Activate {{ short_name }} Sync for Gmail

See <a href="../How-to-Set-Up-the-Chrome-Extension-for-Salesforce-and-Gmail/#2_sign_in_to_gmail_and_grant_rg_email_sidebar_permission_to_work_with_your_gmail_and_google_calendar_data" target="_blank">this article</a> to learn how to activate {{ company_name }} Sync for Gmail / Google Workspace (G Suite) mailboxes.