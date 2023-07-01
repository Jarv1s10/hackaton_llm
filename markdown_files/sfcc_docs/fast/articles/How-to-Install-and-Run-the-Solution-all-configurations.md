---
description: Detailed instruction on how to install and run the solution (all MS Exchange / Office 365 configurations)
---
# How to Install and Run the Solution (all MS Exchange / Office 365 configurations)  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>
<div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*7 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! tip "Tip"
    Also see [this {{ company_name }} blog article](https://revenuegrid.com/blog/salesforce-outlook-integration/) for an overview of solution installation procedures

&nbsp;

!!! note "Note"
    If you are a local administrator rolling out {{ product_name }} for multiple users in your organization, you can make use of [Add-in mass deployment procedures](../Mass-Deployment-of-the-Add-In-Office-365/)

&nbsp;

&nbsp;

## I. {{ product_name }} Add-In Installation

You can install {{ company_name }} Email Sidebar Add-in in your MS Exchange / Office 365 mailbox using one of the following ways:

* [Install the Add-in via Outlook on the desktop](#install_the_add-in_via_outlook_on_the_desktop)

* [Install the Add-in via Outlook on the Web](#install_the_add-in_via_outlook_on_the_web)

&nbsp;

### Install the Add-in via Outlook on the desktop

!!! tip "Tip"
    Also, refer to [this Microsoft article](https://support.office.com/en-us/article/get-an-office-add-in-for-outlook-1ee261f9-49bf-4ba6-b3e2-2ba7bcab64c8) describing add-ins installation via Outlook on the desktop

<br>

<p>
    <img src="..\..\assets\images\Install-and-Run\all-config\get-addin-1.png" style="width:39.38%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
    <b>1.</b> Open your MS Outlook for Desktop, go to <i>Home</i> tab, and click <b>Get Add-ins</b> in MS Outlook ribbon
</p>

<br><br><br><br>

<p>
    <img src="..\..\assets\images\Install-and-Run\all-config\get-addin-2.png" style="width:41.49%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
    <b>2.</b> MS Outlook Add-in management window will be opened. In the <i>Search add-ins</i> box on the right-hand side, type <i>"{{ company_name }}"</i> and select <b>{{ company_name }} for Salesforce</b>
</p>

<br><br><br>

<p style="margin-left:2%">
    <b>3.</b> In the next window that appears, click <b>Add</b>
</p>

<p><img src="..\..\assets\images\Install-and-Run\all-config\get-addin-3.png">
</p>

<br><br>

<p>
    <img src="..\..\assets\images\Install-and-Run\all-config\rg-ribbon.png" style="width:39.25%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

You will see {{ product_name }} icons added to MS Outlook ribbon.

Next, you need to [log in to {{ product_name }}](#ii_rg_email_sidebar_logon).

<br><br><br>

Alternatively, follow the steps below describing the **Add-in installation via Outlook on the Web**.

&nbsp;

&nbsp;

### Install the Add-in via Outlook on the Web

!!! tip "Tip"
    Also, refer to [this Microsoft article](https://support.microsoft.com/en-us/office/using-add-ins-in-outlook-on-the-web-8f2ce816-5df4-44a5-958c-f7f9d6dabdce) describing using add-ins in Outlook on the Web

<br>

<p style="margin-left:2%">
    <b>1.</b> Log in to <a href=https://outlook.live.com/owa/>Outlook on the Web</a> with your credentials
    <br><br>
</p>

<p>
    <img src="..\..\assets\images\Install-and-Run\all-config\more-actions.png" style="width:20.99%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
    <b>2.</b> Select any email message and click the <b>•••</b> (More actions) icon in the upper right corner of the message
    <br><br>
</p>

<p>
    <img src="..\..\assets\images\Install-and-Run\all-config\get-addins.png" style="width:23.77%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
    <b>3.</b> In the menu that appears, scroll down and click <b>Get Add-ins</b>
    <br><br><br>
</p>

<p>
    <img src="..\..\assets\images\Install-and-Run\all-config\get-addin-2.png" style="width:41.49%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
    <b>4.</b> Add-ins for Outlook window will be opened. In the <i>Search add-ins</i> box on the right-hand side, type <i>"{{ company_name }}"</i> and select <b>{{ company_name }} for Salesforce</b>
</p>

<br><br><br>

<p style="margin-left:2%">
    <b>5.</b> In the next window that appears, click <b>Add</b>
</p>

<p><img src="..\..\assets\images\Install-and-Run\all-config\get-addin-3.png">
</p>

<br>

{{ product_name }} Add-in is added to your mailbox. Next, you need to [log in to {{ product_name }}](#ii_rg_email_sidebar_logon).

&nbsp;

!!! tip "Tip"
    Also note that {{ product_name }} for Salesforce (the [Web (Cloud) implementation](../Desktop-MSI-and-Cloud-Web-Implementations-Comparison/)) can also be installed from an .XML Outlook Add-in manifest file or URL provided by your local {{ short_name }} Admin or RevenueGrid.com, refer to [this article](../How-to-Install-the-Add-In-from-an-XML-Manifest-File-or-URL/) for more information
	
&nbsp;

!!! note "Note"
    After you install the Add-in for an email account, it becomes available in MS Outlook running on other configurations and devices compatible with Outlook on the Web, Outlook for Mac, iOS, or Android with the same account logged in
	
&nbsp;

!!! warning "Important"
    Before using {{ product_name }} in MS Outlook Desktop on Windows, please make sure that you have the latest version of MS Edge installed, since it is used to render {{ product_name }} in MS Outlook

&nbsp;
* * *
&nbsp;

## II. {{ product_name }} Logon

!!! note "Note"
    {{ short_name }} logging in is not instant: depending on the number of email messages in your mailbox and items in your calendar it may take several minutes to log in, since on logging in {{ short_name }} needs to [match](../Initial-Search-and-Applied-Record-Filters/) all your existing correspondence and calendar items with your Salesforce records. That is only performed once per account

&nbsp;

### **1\.** Open the Sidebar

<p>
    <img src="..\..\assets\images\Install-and-Run\all-config\rg-open-ribbon.png" style="width:39.25%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
    Open the <a href=../Introduction/>Sidebar</a> for a selected, opened or new email message in MS Outlook Desktop by clicking the <b>Open {{ company_name }}</b> button in the ribbon.
    <br><br>
    See <a href=../Open-in-Outlook-Web/>this article</a> to learn how to open the Sidebar in MS Outlook on the Web.
</p>
<br><br>

### **2\.** Logging on to {{ product_name }}

<!--!!! note "??? Note"
    Note that your data transferred via {{ product_name }} as well as your service access credentials are secured and are **never** shared or stored anywhere, according to {{ company_name }} [Privacy and Security principles](../Privacy-and-Security/).-->

<p>
    <img src="..\..\assets\images\Install-and-Run\all-config\connect-to-sf.png" style="width:39.64%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
There are three available options to log in to {{ product_name }}. Choose one of the following options to connect to Salesforce account and proceed with the steps described below:
</p>

* [Connect to Salesforce](#connect_to_salesforce_login)
* [Connect to Salesforce Sandbox](#connect_to_salesforce_sandbox_login)
* [My Customer/Partner Community login](#my_customerpartner_community_login)

&nbsp;

!!! tip "Tip"
    This step can also be performed for multiple end users in bulk, by the [local {{ short_name }} Admin](../How-to-Log-In-to-the-Admin-Panel/). See [this article](../Set-up-Salesforce-Auth/) for more information

&nbsp;

&nbsp;

#### Connect to Salesforce login

<p>
    <img src="..\..\assets\images\Install-and-Run\all-config\login-sf.png" style="width:35.94%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
<b>1.</b> Click the <b>Connect to Salesforce</b> button. A browser window with Salesforce <a href=http://help.salesforce.com/articleView?id=remoteaccess_authenticate_overview.htm>OAuth</a> page will be opened
</p>
<br>

<p>
    <img src="..\..\assets\images\Install-and-Run\all-config\login-sf-2.png" style="width:50.2%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
<br>
<b>2.</b> Enter your Salesforce credentials on the page or select a previously saved account’s username and click <b>Log In</b>
</p>
<br><br><br><br><br><br><br><br>

!!! note "Note"
    In the screenshot above, a standard Salesforce login window is shown. Note that this OAuth window may look different depending on your Salesforce configuration

<br>

<p>
    <img src="..\..\assets\images\Install-and-Run\all-config\sf-access.png" style="width:50.22%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
<br>
<b>3.</b> Next, click <b>Allow</b> to grant {{ company_name }} Email Sidebar permissions to work with your Salesforce data
</p>

<br><br><br><br><br><br><br><br><br>

<!--
!!! note "Note"
    At this point you may also need to confirm this access via [Salesforce two-factor authentication](https://help.salesforce.com/articleView?id=security_overview_2fa.htm&type=5)
-->

&nbsp;

&nbsp;

#### Connect to Salesforce Sandbox login

!!! tip "Tip"
    Salesforce Sandbox is an isolated environment with Salesforce data used for CRM system tests, learning how to use Salesforce, or experimenting with its features. Refer to [this article](http://help.salesforce.com/articleView?id=create_test_instance.htm) for more information

<br>
<p>
    <img src="..\..\assets\images\Install-and-Run\all-config\login-sf-sb.png" style="width:35.94%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
<b>1.</b> Click the <b>Connect to Salesforce Sandbox</b> button. A browser window with Salesforce <a href=http://help.salesforce.com/articleView?id=remoteaccess_authenticate_overview.htm>OAuth</a> page will be opened
</p>
<br>

<p>
    <img src="..\..\assets\images\Install-and-Run\all-config\login-sf-sb-2.png" style="width:50.22%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
<br>
<b>2.</b> Enter your Salesforce Sandbox credentials on the page and click <b>Log In to Sandbox</b>
</p>
<br><br><br><br><br><br><br><br><br>

<p>
    <img src="..\..\assets\images\Install-and-Run\all-config\sf-access.png" style="width:50.2%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
<br>
<b>3.</b> Next, click <b>Allow</b> to grant {{ company_name }} Email Sidebar permissions to work with your Salesforce data
</p>

<br><br><br><br><br><br><br><br><br>

&nbsp;

&nbsp;

#### My Customer/Partner Community login

<p>
    <img src="..\..\assets\images\Install-and-Run\all-config\more.gif" style="width:37.14%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

To log in with your Salesforce Customer/Partner Community, click **More v** to show this login option.

<br>

<!--
!!! note "Note"
    ??? This logon method is also used to log in with [Single Sign-On (SSO)](http://help.salesforce.com/articleView?id=sso_about.htm) (the recommended method), if it is configured in your Org. Besides, in some configurations OAuth 2.0 and SSO authentication methods are combined; OAuth 1.0 protocol is not supported by {{ product_name }}

&nbsp;-->

<p>
    <img src="..\..\assets\images\Install-and-Run\all-config\login-partner.png" style="width:35.94%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
<b>1.</b> Click the <b>My Customer/Partner Community</b> button
</p>
<br><br>

<p>
    <img src="..\..\assets\images\Install-and-Run\all-config\login-partner-2.png" style="width:39.64%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
<b>2.</b> Enter your community access URL or your special access link in the box and click <b>My Customer/Partner Community</b> below the box
</p>
<br><br><br><br><br>

<p>
    <img src="..\..\assets\images\Install-and-Run\all-config\login-partner-3.png" style="width:50.22%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
<br>
<b>3.</b> On the opened Salesforce <a href=http://help.salesforce.com/articleView?id=remoteaccess_authenticate_overview.htm>OAuth</a> page, enter your community login credentials or select a previously saved account’s username and click <b>Log In</b>
<br><br><br><br><br><br><br><br><br>
</p>

!!! note "Note"
    In the screenshot above, a standard Salesforce login window is shown. Note that this OAuth window may look different depending on your Salesforce configuration
    
<br>

<p>
    <img src="..\..\assets\images\Install-and-Run\all-config\sf-access.png" style="width:50.22%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
<br>
<b>4.</b> Next, click <b>Allow</b> to grant {{ company_name }} Email Sidebar permissions to work with your Salesforce data
<br><br><br><br><br><br><br><br><br><br>
</p>

<br>

<!--
??? In the latest {{ product_name }} updates logging on will be followed by a dialog window for authorizing [{{ short_name }} Add-In's](../Desktop-MSI-and-Cloud-Web-Implementations-Comparison/) access to MS Exchange data, this way allowing to skip setup stage [*3: Activate {{ company_name }} synchronization*](#3_activate_revenue_grid_synchronization) (see below).
-->
&nbsp;

&nbsp;

### **3.** Activate {{ company_name }} synchronization

Once you log in to {{ product_name }} with your Salesforce account, you need to set up [{{ short_company_name }} synchronization](../Synchronization-Engine-An-Overview/) by authorizing it to access your MS Exchange / Office 365 data. Proceed with the steps according to the email service you are using:

* [Activate {{ short_name }} Sync for MS Exchange](#activate_rges_sync_for_ms_exchange)

* [Activate {{ short_name }} Sync for Office 365](#activate_rges_sync_for_office_365)

<br>

If you skip this setup step, you can still run and use {{ product_name }}, except for [the key functions carried out by {{ short_name }} Sync](../AddIn-vs-Sync-Functions/).

!!! warning "Important"
    If you are using several different mailboxes for your correspondence (not [aliases](https://support.office.com/en-us/article/add-or-remove-an-email-alias-in-outlook-com-459b1989-356d-40fa-a689-8f285b13f1f2)), make sure to authorize [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/) for the same mailbox as one for which you installed the [Add-in](../Introduction/), otherwise the [Sync engine functions](../AddIn-vs-Sync-Functions/) will work incorrectly even though {{ short_name }} Sync will appear to be running

&nbsp;

&nbsp;

#### Activate {{ short_name }} Sync for MS Exchange

<p>
    <img src="..\..\assets\images\Install-and-Run\all-config\exch-login.png" style="width:45.72%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
    <br>
    After connecting to your Salesforce account, {{ product_name }} will ask you to connect to your Exchange account to enable {{ short_name }} Sync engine.
</p>
<p style="margin-left:4%">
    <br>
    Enter your Exchange mailbox's Login and Password and click <b>Connect to Exchange</b>
</p>
<p style="margin-left:2%">
    <br>
    In some configurations, you may also need to enter a valid <a href=https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/start-using-web-services-in-exchange>Exchange Web Services link</a> specific to your company's Exchange configuration. To do that, click <b>More v</b> icon and paste the EWS link provided by your local Exchange Admin into the field.
    <br><br><br>
</p>

After access has been authorized, [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/) will start running every 30 minutes 24/7 for this email account.

&nbsp;

&nbsp;

#### Activate {{ short_name }} Sync for Office 365

<p>
    <img src="..\..\assets\images\Install-and-Run\all-config\o365-login.png" style="width:45.72%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
    <br>
    After connecting to your Salesforce account, {{ product_name }} will ask you to connect to your Office 365 account to enable {{ short_name }} Sync engine.
</p>

<p style="margin-left:4%">
    <br>
    <b>1.</b> Click the <b>Connect to Office 365</b> button. A browser window with Office 365 login page will be opened
    <br><br><br><br><br><br>
</p>

<p>
    <img src="..\..\assets\images\Install-and-Run\all-config\o365-sign-in.png" style="width:52.87%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:4%">
    <br>
    <b>2.</b> Enter your Office 365 login credentials in the O365 <a href=https://oauth.net/2/>OAuth 2.0</a> dialog or pick an account from the list when available
    <br><br><br><br><br><br><br><br>
</p>

<p>
    <img src="..\..\assets\images\Install-and-Run\all-config\o365-perm.png" style="width:52.87%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
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

!!! note "Note"
    You may update both Exchange and Salesforce accounts in sync settings at any point later. Refer to [this article](../Renewing-Exchange-and-Salesforce-Account-Credentials/) to learn how

&nbsp;

!!! tip "Tip"
    Refer to [this article](../Historical-Sync-&-Timezones-Matching/) to learn what emails and calendar items you have in MS Exchange / Office 365 will be auto-saved in Salesforce if you enable the corresponding settings ([calendar items auto-saving](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#meeting_appointment_autosaving), [emails auto-saving](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_emails_emails_autosharing)) after setting up {{ company_name }} synchronization

&nbsp;

&nbsp;
* * *
&nbsp;

## III. (Admins only) Install the Managed package in Salesforce

To enable the full scope of features offered by {{ product_name }} several minor adjustments must be made in your Salesforce Org's configuration; installing the [{{ company_name }} managed package](../Admin-Managed-Package/) allows to accomplish that quickly and effortlessly. Follow the above link for complete information about the package.

&nbsp;

!!! note "Note"
    {{ product_name }} is based on the following fundamental principle: one email account is connected to a single Salesforce account. Therefore, no more than one business email account can be connected to a Salesforce account; for the same reason, several Salesforce accounts cannot be connected to a single email account via {{ short_name }}.  
    However, if such scenario is required, as a workaround you can set up your email accounts each connected to a separate Salesforce account within the same Org.  
    Also note that {{ short_name }} can automatically [recognize and match different MS Exchange / Office 365 aliases](../MS-Exchange-Aliases-Handling/) used for the same email account

&nbsp;

&nbsp;

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