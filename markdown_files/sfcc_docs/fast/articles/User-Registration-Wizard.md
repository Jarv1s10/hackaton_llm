---
description: How to use the Registration Wizard to sign up for a RG Email Sidebar user account 
---
# User Registration Wizard  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*5 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

To sign up for a {{ product_name }} user account, contact [our Support team](mailto:support@revenuegrid.com) for personalized Registration Wizard link and follow the Wizard's steps through {{ short_name }} sign up process.

!!! warning "Important"
    To use the Registration Wizard, make sure that any [adblocking extensions/plugins](https://www.tomsguide.com/round-up/best-adblockers-privacy-extensions) in your web browser are disabled for the Registration Wizard's web page and refresh the page; some scripts used by the wizard are incompatible with adblockers so if you do not disable them you will see a blank page

The wizard consists of the following steps:

[Step 1: Specify your Salesforce account](#step_1_specify_your_salesforce_account)

[Step 2: Specify Your Mailbox Account](#step_2_specify_your_mailbox_account)

[Step 3: Select data you want to synchronize (optional)](#step_3_select_data_you_want_to_synchronize_optional)


&nbsp;

## Step 1: Specify your Salesforce account

&nbsp;

<img src="..\..\assets\images\new-admin-panel\wizard\salesforce.png" style="width:50%; display:inline-block; vertical-align:middle; margin-left:1px;float: right">

To allow {{ company_name }} to work with your Salesforce data, you can log in with:

* [Salesforce account](#connect_with_salesforce_account)

* [Salesforce Experience Cloud account](#connect_with_salesforce_experience_cloud_account)

* [Salesforce Sandbox](#connect_with_salesforce_sandbox)



<br><br><br><br>

### **Connect with Salesforce account**

To authorize {{ product_name }} to work with your Salesforce data:

**1.** Click the Salesforce logo 

<p><img src="..\..\assets\images\new-admin-panel\wizard\sf-access.png" style="width:80%;">
</p>
&nbsp;

**2.** Enter your Salesforce username and password or select your previously logged in Salesforce user account (Saved usernames) in the login.salesforce.com OAuth window that will appear

<p><img src="..\..\assets\images\new-admin-panel\login\sf-auth2.png" style="width:30%;">
</p>

In the screenshot above, a standard Salesforce OAuth window is shown. Note that this window may look differently depending on your Salesforce Org's configuration.

<br>

### **Connect with Salesforce Experience Cloud account**

To log in to your Salesforce Experience Cloud (Customer Community or Partner Community) account:

**1.** Click the **My Customer/Partner Community** option

<p><img src="..\..\assets\images\new-admin-panel\wizard\community-access.png" style="width:50%;">
</p>
&nbsp;

**2.** Enter your community URL. The supported Supported Experience Cloud domains are *force.com, salesforce.com, siteforce.com, my.site.com*

**3.** Enter your community logon credentials or select a previously saved account’s username and click Log In on the community OAuth page 
 
<br>

### **Connect with Salesforce Sandbox**

To log in to [Salesforce Sandbox](http://help.salesforce.com/articleView?id=create_test_instance.htm) (an isolated environment with Salesforce data used for testing, learning how to use the CRM, and experimenting with its features):

**1.** Click the "Salesforce Sandbox" option

<p><img src="..\..\assets\images\new-admin-panel\wizard\sandbox-access.png" style="width:50%">
</p>

**2.** Enter your username and password or select your previously logged in account in the OAuth window



&nbsp;

&nbsp;
***
&nbsp;

## Step 2: Specify Your Mailbox Account


Set your Office 365, MS Exchange / Outlook.com, or Gmail account that will be used with {{ product_name }}. Here, again, either direct authentication with password or [OAuth](http://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/authentication-and-ews-in-exchange#oauth-authentication) is used.

* [Login for Office 365 users](#login_for_office_365_users)

* [Login for Microsoft Exchange users](#login_for_microsoft_exchange_users)

* [Login for Gmail users](#login_for_gmail_users)

<p><img src="..\..\assets\images\new-admin-panel\wizard\email-service.png">
</p>
&nbsp;

!!! note "Note"  
    It's possible that you won't see all three options available if your admin has restricted the email service connection options.
<br>
<br>

#### Login for Office 365 users


To log in to your Office 365 account, click the Office 365 logo and enter your login credentials in the “Sign in to your account” dialog box that appears.  

<p><img src="..\..\assets\images\new-admin-panel\wizard\office-wizard.png" style="width:90%">
</p>

<br><br>

#### Login for Microsoft Exchange users


If you are using an on-premises installation of Microsoft Exchange, or your Exchange server is hosted by a third-party provider, or you are using the Outlook.com mail service, click the circle with Exchange logo and enter the following information:

<p><img src="..\..\assets\images\new-admin-panel\wizard\exchange-wizard.png" style="width:90%">
</p>
&nbsp;

<img src="..\..\assets\images\new-admin-panel\wizard\exchange-creds.png" style="width:50%; display:inline-block; vertical-align:middle; margin-left:1px;float: right">

**1.**    In the **Email** box, enter your email address  

**2.**    In the **Password** box, enter the password for your Exchange account  

**3.**    In some configurations, you may be required to provide your Exchange user name and EWS URL:

* In this case, please enter it in the **User name** box. This name usually consists of your domain name followed by a backslash and your account ID (for example, if your domain is "work" and your Windows account ID is "johndoe," you enter “work\\johndoe”)  

* Usually {{ product_name }} finds the required EWS endpoint URL automatically, but in case it was not found or you need to enter one manually, enter the **Exchange Web Services URL** in the box that appears



<br><br>

#### Login for Gmail users

**1\.** To log in to your Gmail account, click the Google logo and enter your login credentials in the sign in dialog box that appears 

<p><img src="..\..\assets\images\new-admin-panel\wizard\google-wizard.png" style="width:90%">
</p>
&nbsp;

**2\.** On the next page, **grant all permissions** required by {{ company_name }}

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/permissions-google.gif" style="width:50%; display:inline-block; vertical-align:middle; margin-left:1px;float: right; margin-top:1rem;"></p>

<br>
The standard set of 10 permissions that {{ product_name }} obtains for every Gmail user on provisioning:  

* Associate you with your personal info on Google  
* See your personal info, including any personal info you've made publicly available
* See your primary Google Account email address  
* See, edit, create, and delete all of your Google Drive files  
* See, create, and delete its own configuration data in your Google Drive 
* See, edit, download, and permanently delete your contacts  
* See, edit, share, and permanently delete all the calendars you can access using Google Calendar  
* See and edit your email labels

<br><br>
**2\.** Click **Continue** to finish logging in

<br>
!!! warning "Important"
    Please note that the set of permissions cannot be adjusted, {{ product_name }} architecture requires all requested permissions to run. The privacy and security of accessed Google data are guaranteed under [{{ product_name }} Privacy and Security policies](https://revenuegrid.com/privacy-policy/). In case some of the permissions are not granted, the Sync Engine will fail with an error “*ISGC-004: Authorization error. Contact your administrator for Google services*”. For this reason, please make sure that the full set of permissions is granted


After completing registration, {{ short_company_name }} will trigger initial synchronization in the background and install the [{{ product_name }} Add-In](../How-to-Install-and-Run-the-Solution-for-Office-365-Mailboxes/#ii_smartcloud_connect_logon) for the compatible email clients. However you can further customize the scope of the objects that should be synced.



&nbsp;
***
&nbsp;

## Step 3: Select data you want to synchronize (optional)

After completing the wizard steps, you will be redirected to the main {{ company_name }} page. To adjust the selection of record types you want to synchronize:

**1.** Click on your profile photo in the upper right hand corner of the window

**2.** Select **Settings**

**3.** Go to the **Sync** tab

**4.** On the *General* tab, select what record types you want to synchronize – emails, events, tasks, or contacts – by enabling the corresponding switch buttons

!!! tip "Tip"
    Learn more about using Sync settings page and configuring sync settings [in this article](../Configuring-Activities-Synchronization-Settings-rg/)

&nbsp;
<br>

#### Appointments and Tasks

{{ company_name }} synchronizes appointments and tasks that meet the following criteria:

*   of which you are the owner  
*   which are not completed  
*   which occurred over the past two weeks or are scheduled for the future    

&nbsp;

#### Contacts

For contacts, you can click **Customize scope** and select what kind of contacts you want to be synchronized:


*   All available contacts
*   Only my contacts
*   Only contacts from the specified Salesforce view (list views are views you can create in Salesforce which contain a specific set of contacts). {{ product_name }} automatically retrieves the list of views available for your contacts so you can pick one that suits you best

!!! note "Note"
    When using a custom Salesforce view, select a view that includes contacts for which you are the owner. Otherwise, new contacts that you will save from Exchange to Salesforce may later be removed (filtered) from Exchange because they do not belong to the selected view

<br>

**Record Count Limits**  

{{ product_name }} indicates the number of records to be synchronized between your Exchange mailbox and Salesforce. Note that some [{{ product_name }} licenses](https://revenuegrid.com/pricing/) have a limit on the maximum number of synchronized records. Once the limit is reached, {{ product_name }} will limit the number of records retrieved from Salesforce to your MS Exchange.

**Example:** Suppose you have 15,000 contacts in Salesforce and your {{ product_name }} plan allows for up to 10k records sync. If you synchronize only contacts then 10,000 out of 15,000 will be synchronized between Salesforce and Exchange. {{ product_name }} will retrieve the newest 10,000 contacts based on their creation date.




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
      margin-top: -80px;
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
<div class="banners banner-1">
  <img src="../../assets/images/banners/banner-1.svg" style="width: 100%; height: 100%;">
  <a class="button" href="https://revenuegrid.com/sign-up/?utm_source=kb_rg&utm_medium=referral&utm_campaign=eac&utm_content=banner" target="_blank">Sign up for a free trial</a>
</div>