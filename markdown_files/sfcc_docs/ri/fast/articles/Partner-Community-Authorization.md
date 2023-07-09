---
description: Step-by-step guidance on how to authorize the solution to work with Salesforce Customer / Partner Community data
---
# How to Authorize the Solution to Work with Salesforce Customer / Partner Community Data  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>
<div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>
<div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*4 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! tip "Tip"
    Also see [this {{ company_name }} blog article](https://revenuegrid.com/blog/salesforce-outlook-integration/) for an overview of solution installation procedures
&nbsp;

!!! warning "Important"
    {{ company_name }} supports only the following Salesforce Experience Cloud subdomains: <i>force.com</i>, <i>salesforce.com</i>, <i>siteforce.com</i>, <i>my.site.com</i>

&nbsp;

{{ product_name }} can be easily configured to work with [Customer / Partner Community data](https://help.salesforce.com/articleView?id=000335630&type=1&mode=1) in Salesforce.

&nbsp;

## Log on with your Customer / Partner Community from the Add-In's logon page

!!! note "Note"
    This logon method is also used to log on with [Single Sign-On (SSO)](http://help.salesforce.com/articleView?id=sso_about.htm) (the recommended method), if it is configured in your Org. Besides, in some configurations OAuth 2.0 and SSO authentication methods are combined; OAuth 1.0 protocol is not supported by {{ product_name }}.

&nbsp;

To log on with your Salesforce Customer/Partner Community:

<br>
<p style="margin-left:5%">
<b>1.</b> On the {{ short_name }} logon page, click <b>More</b>
</p>
<br>

<p style="margin-left:5%"><img src="..\..\assets\images\Configuration-&-Settings\User-Settings\partner-community\partner-com1.png" style="width:35%; display:inline-block; vertical-align:middle; margin-left:1px;float: right">

<b>2.</b> Click <b>My Customer/Partner Community</b>.
</p>
<br><br><br><br><br><br><br>


<p style="margin-left:5%"><img src="..\..\assets\images\Configuration-&-Settings\User-Settings\partner-community\partner-com2.png" style="width:35%; display:inline-block; vertical-align:middle; margin-left:1px; float:right" class="minimized">
<b>3.</b> Enter your community access URL or your special access link in the box and click the button <b>My Customer/Partner Community</b> below the box. Remember to use only <a href="#:~:text=Revenue%20Grid%20supports%20only%20the%20following%20Salesforce%20Experience%20Cloud%20subdomains%3A%20force.com%2C%20salesforce.com%2C%20siteforce.com%2C%20my.site.com">supported subdomains</a>: <i>force.com</i>, <i>salesforce.com</i>, <i>siteforce.com</i>, <i>my.site.com</i>
</p>

<br><br><br>

<p style="margin-left:5%"><img src="..\..\assets\images\Configuration-&-Settings\User-Settings\partner-community\partner-com3.png" style="width:35%; display:inline-block; vertical-align:middle; margin-left:1px; float:right" class="minimized">
<b>4.</b> Enter your community logon credentials or select a previously saved account’s username and click <b>Log In</b> on the community OAuth page that opens in your web browser or perform a Single Sign-On logon according to your <a href="https://en.wikipedia.org/wiki/Single_sign-on">SSO</a> provider's procedure.
</p>

<br><br><br>

<p style="margin-left:5%">
In the screenshot, a standard Salesforce login window is shown. Note that this OAuth window may look differently, depending on your Salesforce configuration.
</p>
<br><br><br>
<p style="margin-left:5%"><img src="..\..\assets\images\Configuration-&-Settings\User-Settings\partner-community\partner-com4.png" style="width:35%; display:inline-block; vertical-align:middle; margin-left:1px;float: right" class="minimized">
<b>5.</b> Next, you need to accept granting {{ product_name }} permissions to work with Salesforce data by clicking <b>Allow</b> in the following dialog window:
</p>

&nbsp;

<br><br><br><br><br><br>
<p style="margin-left:5%">
<b>6.</b> Authorize <a href="../Desktop-MSI-and-Cloud-Web-Implementations-Comparison/">{{ short_name }} Add-In's</a> access to MS Exchange data in the next window
</p>

<br>
<hr>
<br>

##  Log in with your Customer / Partner Community from {{ company_name }} Sync settings (for Add-In-only users)

<br>
Alternative way for Add-In-only users to configure {{ product_name }} is to log in with Customer / Partner Community from {{ company_name }} Sync settings.
<br><br>

To open {{ product_name }} **Sync settings** from the Sidebar:

<p style="margin-left:2%">
    <br>
    <b>1.</b> Open the {{ product_name }} Add-In / Chrome Extension in MS Outlook Desktop or On the Web version or Gmail
</p>

<p>
    <img src="..\..\assets\images\Configuration-&-Settings\User-Settings\partner-community\sync-settings.png" style="width:27.49%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
    <br>
    <b>2.</b> Click the <b>☰ Menu</b> button in {{ product_name }} Add-In / Chrome Extension and select <b>Sync settings</b>
    <br><br><br>
</p>

!!! warning "Important"
    Depending on your subscription plan, the appearance of your Sync Settings page may be different. Below you can find instructions on how to log in with your Customer / Partner Community on the **New** and **Legacy** Sync Settings pages. Proceed with the steps according to the appearance of your Sync Setting page:
    
    * [New Sync Settings page](#steps_for_the_new_sync_settings_page)
    * [Legacy Sync Settings page](#steps_for_the_legacy_sync_settings_page)

&nbsp;

&nbsp;

### Steps for the [new Sync Settings page](../Configuring-Activities-Synchronization-Settings-rg/)

<p>
    <img src="..\..\assets\images\Configuration-&-Settings\User-Settings\partner-community\my-connectivity.png" style="width:24.3%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:4%">
    <br>
    <b>1.</b> On the opened Sync Settings page, go to <b>My connectivity</b> under <b>Personal Settings</b>
    <br><br><br><br><br><br>
</p>

<p>
    <img src="..\..\assets\images\Configuration-&-Settings\User-Settings\partner-community\crm.png" style="width:55%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:4%">
    <br>
    <b>2.</b> Find the <b>CRM</b> tab and click <b>Change</b>
    <br><br><br><br><br><br><br>
</p>

<p>
    <img src="..\..\assets\images\Configuration-&-Settings\User-Settings\partner-community\partner-option1.png" style="width:55%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:4%">
    <br><br>
    <b>3.</b> On the next page, select the <b>Customer / Partner Community</b> login option
    <br><br><br><br><br><br><br><br><br><br>
</p>

<p>
    <img src="..\..\assets\images\Configuration-&-Settings\User-Settings\partner-community\partner-url.png" style="width:44.92%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:4%">
    <b>4.</b> Enter your community access URL or your special access link in the box and click <b>Log in with Customer/Partner Community</b> below the box. Remember to use only <a href="#:~:text=Revenue%20Grid%20supports%20only%20the%20following%20Salesforce%20Experience%20Cloud%20subdomains%3A%20force.com%2C%20salesforce.com%2C%20siteforce.com%2C%20my.site.com">supported subdomains</a>: <i>force.com</i>, <i>salesforce.com</i>, <i>siteforce.com</i>, <i>my.site.com</i>
    <br><br><br>
</p>

<p>
    <img src="..\..\assets\images\Configuration-&-Settings\User-Settings\partner-community\login-partner.png" style="width:50.22%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:4%">
    <br>
    <b>5.</b> On the opened Salesforce <a href=https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_flows.htm&type=5>OAuth</a> page, enter your community login credentials or select a previously saved account’s username and click <b>Log In</b>
    <br><br><br><br><br><br><br><br><br>
</p>

!!! note "Note"
    In the screenshot above, a standard Salesforce login window is shown. Note that this OAuth window may look different depending on your Salesforce configuration

<br>

<p>
    <img src="..\..\assets\images\Configuration-&-Settings\User-Settings\partner-community\sf-access.png" style="width:50.2%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:2%">
    <br>
    <b>6.</b> Next, click <b>Allow</b> to grant {{ company_name }} Email Sidebar permissions to work with your Salesforce data
    <br><br><br><br><br><br><br><br><br><br><br>
</p>

Now you are all set to work with Salesforce Customer / Partner Community data via {{ product_name }}.

&nbsp;
***
&nbsp;

### Steps for the [legacy Sync Settings page](../Configuring-Activities-Synchronization-Settings/)

**1\.** On the opened {{ company_name }} Sync dashboard, select **CRM** in the navigation pane on the left, then click on the circle **Change** in the bottom right corner of the main pane  

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Partner-Community\step1.png" class="minimized">
</p>

&nbsp;

**2\.** Click on the text **CLICK HERE FOR ADVANCED SETUP: ...**


<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Partner-Community\step2.png" class="minimized">
</p>

&nbsp;

**3\.** In the *"Configure Salesforce access"* dialog that appears:


<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Partner-Community\step3.png" class="minimized">
</p>

&nbsp;

**3\.1.** Select **My Customer/Partner Community** on the left  

**3\.2.** Enter the community login URL provided by your Salesforce Admin in the field **Customer/Partner Account Login Url** on the right. Remember to use only <a href="#:~:text=Revenue%20Grid%20supports%20only%20the%20following%20Salesforce%20Experience%20Cloud%20subdomains%3A%20force.com%2C%20salesforce.com%2C%20siteforce.com%2C%20my.site.com">supported subdomains</a>: <i>force.com</i>, <i>salesforce.com</i>, <i>siteforce.com</i>, <i>my.site.com</i>  

!!! note "Note"
    Note that your data transferred via {{ product_name }} as well as your service access credentials and URLs are secured and are **never** shared or stored anywhere, according to {{ company_name }} [Privacy and Security principles](../Privacy-and-Security/)

&nbsp;

**3\.3.** Click on the Salesforce cloud icon  

&nbsp;

**4\.** A standard [Salesforce OAuth](https://help.salesforce.com/articleView?id=sf.remoteaccess_oauth_flows.htm&type=5) window will be opened in your browser.  
To finish setup, log in to the system with your Salesforce credentials  

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Partner-Community\step4.png">
</p>

&nbsp;

**5\.** Next, click <b>Allow</b> to grant {{ company_name }} Email Sidebar permissions to work with your Salesforce data

<p>
    <img src="..\..\assets\images\Configuration-&-Settings\User-Settings\partner-community\sf-access.png">
</p>

&nbsp;

Now you are all set to work with Salesforce Customer / Partner Community data via {{ product_name }}.

&nbsp;