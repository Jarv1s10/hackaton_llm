---
description: Detailed overview of Admin panel login procedure
---
# How to Log In to the Admin Panel  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*5 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;
!!! warning "Important"
    In March 2023 release, the new Admin Panel was introduced. The support of the legacy Admin Panel will be ceased soon, thus we strongly encourage that our customers switch to the new Admin Panel. This article contains two sections:  
    • [How to log in to the new Admin Panel](../Managing-Organizations-via-the-Admin-Panel/#how_to_log_in_to_the_new_admin_panel)  
    • [How to log in to the legacy Admin Panel](../Managing-Organizations-via-the-Admin-Panel/#how_to_log_in_to_the_lagacy_admin_panel)

To use {{ product_name }} Admin panel, special access permissions are required. To request the permissions for your organization, [contact {{ company_name }} support team by email](mailto:support@revenuegrid.com). Admin panel provides tools for managing end users and some of its key settings it includes duplicate {{ product_name }} [Customization](../Customization-Settings-Explained/) and [Sync](../Configuring-Activities-Synchronization-Settings/) settings on Admin level.


&nbsp;

## How to log in to the new Admin Panel

{{ short_company_name }} Administration panel is the advanced setup page that enables local product administrators to configure, manage, and monitor the Users and Profiles. The Admin panel contains the following tabs:

- **[Profiles](../Managing-Organizations-via-the-Admin-Panel/).** Displays the Profiles page, where you can view a list of profiles and can manage what profiles are authorized to use specific {{ company_name }} product packages

- **[Users](../Managing-Users-via-the-Solution-s-Admin-Panel/).** Displays the Users page, where you can view the list of users and manage what users are authorized to use specific {{ company_name }} product packages, user-specific settings, activity, etc.

- **[Licenses](../Managing-Plans-for-the-Users/).** Displays the Licenses page where you can view the list of licenses and manage users' configurations


<br>

Currently four Admin panel options are implemented. Admins can log in to the Administration panel with 

<img src="..\..\assets\images\new-admin-panel\login\login.png" style="width:30%; display:inline-block; vertical-align:middle; margin-left:10px; float: right">

* [Salesforce](../How-to-Log-In-to-the-Admin-Panel/#admin_panel_login_with_salesfoce)

* [Salesforce Sandbox](../How-to-Log-In-to-the-Admin-Panel/#admin_panel_login_with_salesfoce_sandbox)

* [Office 365](../How-to-Log-In-to-the-Admin-Panel/#admin_panel_login_with_microsoft_oauth_office_365_or_microsoft_365)

* [Google](../How-to-Log-In-to-the-Admin-Panel/#admin_panel_login_with_gmail_oauth) 


&nbsp;

* * *

&nbsp;

#### **Admin panel login with Salesfoce**

**1\.** Open the Admin panel access URL provided by [{{ company_name }} Support Team](mailto:suport@revenuegrid.com) in your web browser

<img src="..\..\assets\images\new-admin-panel\login\sf.png" style="width:30%; display:inline-block; vertical-align:middle; margin-left:10px; float: right">

**2\.** On the login page that opens, select **Continue with Salesforce**

<br>

**3\.** Enter your authorized Admin login account or enter the login credentials in the [Salesforce OAuth window](https://help.salesforce.com/articleView?id=remoteaccess_authenticate_overview.htm) that appears

<img src="..\..\assets\images\new-admin-panel\login\sf-auth2.png" style="width:60%;">

&nbsp;

**3\.** If your Admin login credentials are correct, you will log to {{ company_name }} Administration Panel

&nbsp;
* * *
&nbsp;

#### **Admin panel login with Salesfoce Sandbox**

**1\.** Open the Admin panel access URL provided by [{{ company_name }} Support Team](mailto:suport@revenuegrid.com) in your web browser

<img src="..\..\assets\images\new-admin-panel\login\sandbox.png" style="width:30%; display:inline-block; vertical-align:middle; margin-left:10px; float: right">

**2\.** On the login page that opens, select Continue with Salesforce Sandbox

<br>

**3\.** Enter your authorized Admin login account or enter the login credentials in the [Salesforce OAuth window](https://help.salesforce.com/articleView?id=remoteaccess_authenticate_overview.htm) that appears

<img src="..\..\assets\images\new-admin-panel\login\sandbox-auth.png" style="width:60%;">

&nbsp;

**3\.** If your Admin login credentials are correct, you will log to {{ company_name }} Administration Panel


&nbsp;
* * *
&nbsp;


#### Admin panel login with Microsoft OAuth (Office 365 or Microsoft 365)

[MS Office 365 OAuth](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow) authentication method can be used to access {{ short_name }} Admin panel, if configured.

To log in over MS OAuth:

**1\.** Open the Admin panel access link provided by [{{ company_name }} Support Team](mailto:suport@revenuegrid.com) in your web browser

<img src="..\..\assets\images\new-admin-panel\login\office.png" style="width:30%; display:inline-block; vertical-align:middle; margin-left:10px; float: right">

**2\.** Click on the **Sign in with Office 365** option

<br>

**3\.** Select {{ short_company_name }} Admin's account or enter the login credentials in the O365 OAuth dialog that appears. Don't worry, this authorization will be used exclusively to log in to the Admin panel

<img src="..\..\assets\images\Install-and-Run\SyncAuth\oauth.png" style="width:60%">

<br>

**4\.** This is normally required on the initial login. O365 will request specific access permissions for {{ company_name }}. This data access is fully secured by [{{ short_company_name }} data privacy and security guarantees](../Privacy-and-Security/), it is **never** used for any activities not initiated by you.  
Click **Accept** in the dialog to finalize authorization

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\How-to-Log-in-to-SmartCloud-Connect-Administration-Panel\o365-permissions.png">
</p></details>

<br>

**5\.** If your Admin login credentials are correct, you will log to {{ company_name }} Administration Panel

&nbsp;
* * *
&nbsp;

#### Admin panel login with Gmail OAuth


[Gmail OAuth](https://developers.google.com/gmail/api/auth/about-auth) authentication method can also be used to access {{ short_name }} Admin panel, if configured.

To log in over Google OAuth:  

**1\.** Open the Admin panel access link provided by [{{ company_name }} Support Team](mailto:suport@revenuegrid.com) in your web browser  

<p><img src="..\..\assets\images\new-admin-panel\login\gmail.png" style="width:30%; display:inline-block; vertical-align:middle; margin-left:10px; float: right">
</p>

**2\.** Click on the **Sign in with Google** option  

<br>

**3\.** Select the {{ short_company_name }} Admin account or enter login credentials in the Google OAuth dialog that appears. Don't worry, this authorization will be used exclusively to log in to the Admin panel

<img src="..\..\assets\images\new-admin-panel\login\gmail2.png" style="width:60%;">

&nbsp;

**4\.** Next, Google will notify you about specific access permissions granted for {{ company_name }}. This data access is fully secured by [{{ short_company_name }} data privacy and security guarantees](../Privacy-and-Security/), it is **never** used for any activities not initiated by you.  

<details><summary> >>> Click to see list of required permissions <<< </summary>
<p>

<b>The standard set of 10 permissions that {{ company_name }} obtains for every Gmail user on provisioning. See <a href="../How-to-Set-Up-the-Chrome-Extension-for-Salesforce-and-Gmail/#2_sign_in_to_gmail_and_grant_revenue_inbox_permission_to_work_with_your_gmail_and_google_calendar_data">this article</a> for more details.</b><br>
<br>
<ul>
<li>See, edit, create, and delete all of your Google Drive files</li>
<li>See, create, and delete its own configuration data in your Google Drive</li>
<li>See, edit, download, and permanently delete your contacts</li>
<li>See, edit, share, and permanently delete all the calendars you can access using Google Calendar</li>
<li>See and edit your email labels</li>
<li>Manage drafts and send emails</li>
<li>Read, compose, and send emails from your Gmail account</li>
<li>Associate you with your personal info on Google</li>
<li>See your personal info, including any personal info you've made publicly available</li>
<li>See your primary Google Account email address</li>
</ul>
</details>

&nbsp;

Click **Continue** in the dialog to finalize authorization.

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\How-to-Log-in-to-SmartCloud-Connect-Administration-Panel\gmail-continue.png" style="width:70%">
</p>

<br>

**5\.** If your Admin login credentials are correct, you will log to {{ company_name }} Administration Panel


<br>
<hr>
<br>

## How to log in to the legacy Admin panel

{{ short_company_name }} Administration panel is the advanced setup page that enables local product administrators to configure, manage, and monitor the Users and Profiles. The Admin panel contains the following tabs:

- **[ROI Study/Health Status](../Return-on-Investment-ROI-Usage-Efficiency-and-User-Setup-Status-Tools/).** {{ product_name }} return on investment, use efficiency, and product setup status monitoring tools

- **[Organizations](../Managing-Organizations-via-the-Admin-Panel/).** Displays the Organizations page where you can view a list of organizations and manage what organizations are authorized to use the {{ product_name }}

- **[Users](../Managing-Users-via-the-Solution-s-Admin-Panel/).** Displays the Users page, where you can view the list of users and manage what users are authorized to use the Add-In / Chrome Extension and [{{ company_name }} Synchronization](../Synchronization-Engine-An-Overview/)

- **[Plans](../Managing-Plans-for-the-Users/).** Displays the Plans page where you can view the list of plans and manage users' configurations

- **Activity**. In the latest {{ product_name }} updates Admin panel also includes the Activity tab that lists all activities performed in the Admin panel by every user with Admin permissions. The tab is very useful for rolling back unwanted changes or defining who did what changes in Admin settings

- **[Global settings](../Special-Admin-Panel-Settings/).** This page is normally managed by {{ company_name }} CSM team and is not displayed for local Admins. On this tab you can view and adjust a number of specific {{ product_name }} settings


&nbsp;

* * *

&nbsp;

#### **Admin panel ordinary login**

**1\.** Open the Admin panel access URL provided by {{ company_name }} in your web browser


&nbsp;

**2\.** Do either of the following, depending on the configured authorization system

- The default login procedure: click **Log In with Salesforce** and enter your authorized Admin login credentials in the [Salesforce OAuth window](https://help.salesforce.com/articleView?id=remoteaccess_authenticate_overview.htm) that appears
- The alternative custom login procedure: enter your **Login** (email address), **Password**, and the **Instance** (if required) provided by {{ company_name }} and then click **Log In**

<p>
    <img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/How-to-Log-in-to-SmartCloud-Connect-Administration-Panel/1.png">
</p>

&nbsp;

**3\.** If your Admin login credentials are correct, you will see the [ROI Study](../Return-on-Investment-ROI-Usage-Efficiency-and-User-Setup-Status-Tools/) of the Administration Panel upon logging in to it


<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\How-to-Log-in-to-SmartCloud-Connect-Administration-Panel\3.png" class="minimized">
</p>

&nbsp;
* * *
&nbsp;

#### Admin panel login with Salesforce Single Sign-On

In case you don't want to enter your admin panel login credentials directly and instead use secure [Salesforce SSO](http://trailhead.salesforce.com/en/modules/identity_login/units/identity_login_sso) login. This is the default logon method:  

**1\.** On the Admin panel login page: click on **SSO** in the lower right corner, then enter your company's Salesforce Org link in the corresponding field below and click **Log In**  

<p><img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5babc9792c7d3a04dd5afff8.png">
</p>



&nbsp;

**2\.** A standard Salesforce OAuth window will appear. In it, you can either select a previously saved account or enter your Salesforce user login and password:  

<p><img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5babcd122c7d3a04dd5b0020.png">
</p>


&nbsp;

**3\.** Click **Log In** and {{ product_name }} admin panel will be opened in a new browser tab

&nbsp;
* * *

&nbsp;

#### Admin panel login with Microsoft OAuth (Office 365 or Microsoft 365)

[MS Office 365 OAuth](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow) authentication method can be used to access {{ short_name }} Admin panel, if configured.

To log in over MS OAuth:
**1\.** Open the Admin panel access link provided by [{{ company_name }} Support Team](mailto:suport@revenuegrid.com)  
**2\.** Click **Log in with Microsoft** in the login dialog  

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\How-to-Log-in-to-SmartCloud-Connect-Administration-Panel\1.png">
</p>

&nbsp;

**3\.** Select {{ short_name }} Admin's account or enter the login credentials in the O365 OAuth dialog that appears. Don't worry, this authorization will be used exclusively to log in to the Admin panel

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Install-and-Run\SyncAuth\oauth.png">
</p></details>

&nbsp;

**4\.** This is normally required on the initial login. O365 will request specific access permissions for {{ product_name }}. This data access is fully secured by [{{ short_name }} data privacy and security guarantees](../Privacy-and-Security/), it is **never** used for any activities not initiated by you.  
Click **Accept** in the dialog to finalize authorization

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\How-to-Log-in-to-SmartCloud-Connect-Administration-Panel\o365-permissions.png">
</p></details>

&nbsp;
Several seconds later you will see the Admin panel's user interface.

&nbsp;
* * *
&nbsp;

#### Admin panel login with Gmail OAuth


[Gmail OAuth](https://developers.google.com/gmail/api/auth/about-auth) authentication method can also be used to access {{ short_name }} Admin panel, if configured.

To log in over Google OAuth:  
**1\.** Open the Admin panel access link provided by [{{ company_name }} Support Team](mailto:suport@revenuegrid.com)  
**2\.** Click **Log in with Google** in the login dialog  

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\How-to-Log-in-to-SmartCloud-Connect-Administration-Panel\1.png">
</p>

&nbsp;

**3\.** Select {{ short_name }} Admin account or enter login credentials in the Google OAuth dialog that appears. Don't worry, this authorization will be used exclusively to log in to the Admin panel

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\How-to-Log-in-to-SmartCloud-Connect-Administration-Panel\gmail-oauth.png">
</p>

&nbsp;

**4\.** Next, Google will notify you about specific access permissions granted for {{ product_name }}. This data access is fully secured by [{{ short_name }} data privacy and security guarantees](../Privacy-and-Security/), it is **never** used for any activities not initiated by you.  

<details><summary> >>> Click to see permissions detailing and screenshots <<< </summary>
<p>

<b>The standard set of 11 permissions that {{ product_name }} obtains for every Gmail user on provisioning. See <a href="../How-to-Set-Up-the-Chrome-Extension-for-Salesforce-and-Gmail/#2_sign_in_to_gmail_and_grant_revenue_inbox_permission_to_work_with_your_gmail_and_google_calendar_data">this article</a> for more details.</b><br>
<br>
<ul>
<li>See, edit, create, and delete all of your Google Drive files</li>
<li>See, create, and delete its own configuration data in your Google Drive</li>
<li>See, edit, download, and permanently delete your contacts</li>
<li>See, edit, share, and permanently delete all the calendars you can access using Google Calendar</li>
<li>See and edit your email labels</li>
<li>Manage drafts and send emails</li>
<li>Read, compose, and send emails from your Gmail account</li>
<li>Associate you with your personal info on Google</li>
<li>Create, edit, organize, and delete all your tasks</li>
<li>See your personal info, including any personal info you've made publicly available</li>
<li>See your primary Google Account email address</li>
</ul>
<br>
<br><br><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\How-to-Log-in-to-SmartCloud-Connect-Administration-Panel\gmail-permissions1.png">
<br>
<br><br><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\How-to-Log-in-to-SmartCloud-Connect-Administration-Panel\gmail-permissions2.png">

</p></details>

&nbsp;

Click **Continue** in the dialog to finalize authorization.

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\How-to-Log-in-to-SmartCloud-Connect-Administration-Panel\gmail-continue.png">
</p>

&nbsp;
Several seconds later you will see the Admin panel's user interface.





&#160;
 &#160;


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
<div class="banners banner-2">
  <img src="../../assets/images/banners/banner-2.svg" style="width: 100%; height: 100%;">
  <a class="button" href="https://revenuegrid.com/request-demo/?utm_source=kb_rg&utm_medium=referral&utm_campaign=eac_demo&utm_content=banner" target="_blank">Book a free demo</a>
</div>
