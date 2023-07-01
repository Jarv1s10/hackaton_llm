---
description: Step-by-step guide on setting up the RGES for Chrome extension
---
# How to Set Up the Chrome Extension for Salesforce and Gmail  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*5 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

<iframe src="https://player.vimeo.com/video/447805212" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>

&nbsp;

With [{{ product_name }} for Salesforce and Gmail Chrome browser extension](https://chrome.google.com/webstore/detail/smartcloud-connect-for-sa/agfekjndkedoakoeahndfnjilkifbicn?hl=en), you can access and update any relevant Salesforce data – Emails, Events, Contacts, Tasks, Accounts, etc. right from your Gmail mailbox opened on any device that can run Google Chrome browser. See this article to learn how to use the Extension's [Sidebar interface](../Introduction/).
After installing the extension, please refer to [Using {{ product_name }} for Salesforce and Gmail](../Using-the-Solution-for-Salesforce-and-Gmail/) for information on how to use {{ product_name }} with Gmail.  
{{ short_name }} for Salesforce and Gmail works with both Gmail and [Google Workspace (G Suite)](https://workspace.google.com/). The Chrome Extension's updates get installed automatically, that does not require any actions from the end users.

&nbsp;

!!! tip "Tip"
    A full mass {{ short_name }} deployment scenario for Enterprise Gmail / Google Workspace (G Suite) {{ short_name }} users by [the local Admin](../Managing-Users-via-the-Solution-s-Admin-Panel/) is available for Windows systems. See these articles for details: [Chrome Extension mass deployment via Active Directory](../Chrome-Extension-Mass-Deployment/) and [Gmail Users Mass-Provisioning](../Gmail-Users-Mass-Provisioning/)

&nbsp;

!!! note "Note"
    {{ product_name }} for Salesforce and Gmail is **not** a standalone application, it only works in Gmail web interface opened in Google Chrome or a Chromium-based browser

&nbsp;

&nbsp;



**To start using {{ product_name }} for Salesforce and Gmail, do the following**

### **1.** Add the {{ product_name }} for Salesforce Extension to your Google Chrome


To add the {{ product_name }} for Salesforce Extension to your Chrome or Chromium-based browser:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1.1.**  In the Google Chrome browser, open [this Chrome Web Store link](https://chrome.google.com/webstore/detail/smartcloud-connect-for-sa/agfekjndkedoakoeahndfnjilkifbicn?authuser=4)

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5832ffa4c697916f5d053183.png" class="minimized">
</p></details>


&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1.2.**  Click the button **Add to Chrome**, then click **Add extension** in the confirmation dialog that will appear

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/chrome_add_confirm.png)

&nbsp;
&nbsp;

### **2.** Sign in to Gmail and grant {{ product_name }} permission to work with your Gmail and Google Calendar data

&nbsp;

!!! note "Note"
    Handling of your email/calendar and CRM data by {{ product_name }} Chrome Extension for Gmail is based on the same [set of Privacy and Security principles](../Privacy-and-Security/) as {{ product_name }} Add-In for MS Outlook Desktop or On the Web version

&nbsp;

To grant {{ product_name }} permissions to interact with your Google account, do the following:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **2.1.**  After signing in to Gmail, open the {{ product_name }} Extension by clicking the {{ product_name }} icon in the tab one the right-hand side

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **2.2.**  In the extension's pane, click **Sign in to my Google account**

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\gmail_setup_1-2.png">
</p>


&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2.3.**  The *Choose an account* dialog will appear, select your account in it

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\gmail_setup_3.png">
</p>


&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2.4.**  Provide the Extension access to your Gmail data by ticking **all** nine access items on the list which will appear

&nbsp;

&nbsp;

#### Google Permissions Set

The set of access permissions cannot be adjusted, {{ short_name }} architecture requires all requested permissions to run. The privacy and security of accessed Google data are guaranteed under [{{ product_name }} Privacy and Security policies](https://revenuegrid.com/privacy-policy/).

This nine permissions are required to enable {{ short_name }} to access the relevant types of Google data: Emails, Google Drive files, Calendar, Contacts, Calendar, Tasks, etc.  

!!! warning "Important"
    Each permission is required to perform a [specific {{ short_name }} Chrome Extension (Add-In) or Sync Engine function](../AddIn-vs-Sync-Functions/). In case some of the permissions are not granted, the [Extension (Add-In)](../Introduction/) will be usable except for the affected functions, but the [Sync Engine](../Synchronization-Engine-An-Overview/) will fail with an error "*ISGC-004: Authorization error. Contact your administrator for Google services*". For this reason, please make sure that the full set of permissions is granted

&nbsp;

The complete list of required permissions:  


<details><summary> >>> The complete list of required permissions <<< </summary>
<p>
<b>The standard set of 9 permissions that {{ product_name }} obtains for every Gmail user on provisioning:</b><br>
<br>
<ul>
<li>Associate you with your personal info on Google</li>  
<li>See your primary Google Account email address</li>
<li>See, edit, create, and delete all of your Google Drive files</li>
<li>See, create, and delete its own configuration data in your Google Drive</li>
<li>See, edit, download, and permanently delete your contacts</li>
<li>See, edit, share, and permanently delete all the calendars you can access using Google Calendar</li>
<li>See and edit your email labels</li>
<li>Manage drafts and send emails</li>
<li>Read, compose, and send emails from your Gmail account</li>
</ul>
</p></details>

&nbsp;

<details><summary> >>> Click to see a screenshot <<< </summary>

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Gmail\allow1.png">
</p><br>
     </details>

&nbsp;

Next, you will see the *Login successfully completed!* window and get a notification email "*Security alert: {{ company_name }} was granted access to your Google Account*" as a confirmation.

!!! tip "Tip"
    If, for any reason, you will need to revoke {{ product_name }} extension's access to your Gmail data, you can disable it by going to [Apps connected to your account](https://security.google.com/settings/security/permissions), selecting the extension and then clicking **Remove**

&nbsp;
&nbsp;

### **3.** Authorize the {{ product_name }} Chrome Extension to access your Salesforce data

&nbsp;

To grant the {{ product_name }} Extension permissions to work with your Salesforce data, do the following:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**3.1.**  Open the {{ product_name }} extension by clicking its logo in the toolbar on the right-hand side of your Gmail box interface

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**3.2.** Select **Connect to Salesforce** (to work with your actual Salesforce data).


&nbsp;

Or, if you want to work with [Salesforce Sandbox](https://help.salesforce.com/articleView?id=deploy_sandboxes_intro.htm&type=5) (a copy of your production environment used for testing and development) or a [Customer/Partner Community environment](https://www.salesforce.com/eu/products/community-cloud/overview/), click on **Sign in to Salesforce Sandbox** or **My Customer/Partner Community** respectively.

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **3.3.**  In the [Salesforce SSO](https://help.salesforce.com/articleView?id=sso_about.htm&type=5) Login window that appears, select or enter your Salesforce credentials and click **Log In** (or **Log in to Sandbox**, if you are going to use [Salesforce Sandbox environment](https://help.salesforce.com/s/articleView?id=sf.deploy_sandboxes_intro.htm&type=5))

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\gmail_sf_auth_2.png">
</p>


&nbsp;

You are set to use {{ product_name }} for Salesforce in Gmail. For detailed information on how to use the extension, see [this article](../Using-the-Solution-for-Salesforce-and-Gmail/).

!!! note "Note"
    Unlike {{ product_name }} implementation for [MS Exchange / Office 365/Outlook on the web](../How-to-Install-and-Run-the-Solution-all-configurations/), {{ product_name }} Chrome extension does not require additional email access authorization for [synchronization](../Synchronization-Engine-An-Overview/) to run, so it will be active right after you set up the extension

&nbsp;

* * *

&nbsp;

### How to Remove the Extension from Chrome

Refer to [this Google Chrome Support instruction](https://support.google.com/chromebook/answer/2589434?hl=en) to learn how to remove the extension from your Chrome browser.




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
