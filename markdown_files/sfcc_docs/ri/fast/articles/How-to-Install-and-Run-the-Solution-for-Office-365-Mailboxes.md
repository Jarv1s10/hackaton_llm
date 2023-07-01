---
description: How to work with RGES in Office 365 Mailboxes: installation and setup
---
# How to Install and Run the Solution for Office 365 Mailboxes  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*4 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

<iframe src="https://player.vimeo.com/video/381137970" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
&nbsp;

!!! tip "Tip"
    If you are a local administrator rolling out {{ product_name }} for multiple users in your org, you can make use of [Add-In mass deployment mechanisms](../Mass-Deployment-of-the-Add-In-Office-365/)

&nbsp;

For a description of all available installation and logon (Sandbox, Customer/Partner Community, Single Sign-On) options, please refer to [this article](../How-to-Install-and-Run-the-Solution-all-configurations/).

&nbsp;
&nbsp;

## I. Install {{ product_name }} Add-In 
&nbsp;

### 1. Install {{ product_name }} Add-In from MS Outlook for Desktop

{{ product_name }} installation in MS Outlook follows the [standard MS Outlook addin installation steps](https://support.office.com/en-ie/article/get-an-office-add-in-for-outlook-1ee261f9-49bf-4ba6-b3e2-2ba7bcab64c8):

**1\.1\.** Open your MS Outlook for Desktop, go to *Home* tab, and click **Get Add-ins** in MS Outlook ribbon

![](../assets/images/Install-and-Run/get-add-in/get-add-in-1.png)

&nbsp;

**1\.2\.** MS Outlook Add-In management window will be opened. In the *Search add-ins* box on the right-hand side, type *"{{ company_name }}"* and select **{{ company_name }} for Salesforce**

<p><img src="../../assets/images/Install-and-Run/get-add-in/get-add-in-2.png" class="minimized">
</p>

&nbsp;

**1\.3\.** In the next window that appears, click **Add**

<p><img src="../../assets/images/Install-and-Run/get-add-in/get-add-in-3.png" class="minimized">
</p>

&nbsp;

You will see {{ product_name }} icons added to MS Outlook ribbon.

<p><img src="../../assets/images/Install-and-Run/get-add-in/get-add-in-4.png" class="minimized">
</p>

&nbsp;

In addition, corresponding controls are now added to your mail account opened in <https://outlook.com> or <https://outlook.live.com/owa/>. See [this article](../Open-in-Outlook-Web/) for more information.  
  
**1\.4\.** Next, you need to [log on to {{ product_name }}](../How-to-Install-and-Run-the-Solution-for-Office-365-Mailboxes/#ii_rg_email_sidebar_logon)


&nbsp;

*Alternatively, you can install {{ product_name }} Add-In via Installation Wizard following the steps provided below.*
 
### 2. Install {{ product_name }} Add-In via Installation Wizard
 
It is the the recommended way to install the [Cloud (Web) product implementation](../Desktop-MSI-and-Cloud-Web-Implementations-Comparison/) for Office 365 mailboxes, via {{ product_name }} Installation Wizard <https://revenuegrid.com/csm-wizard/>

**2\.1\.** Open the Wizard's page in your web browser and click **Enable for Office 365**   

&nbsp;
<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5b6c73722c7d3a03f89d85db.png" class="minimized">
</p></details>



&nbsp;

**2\.2\.** You will be directed to [{{ product_name }} Add-In's page in Microsoft AppSource](https://appsource.microsoft.com/en-us/product/office/wa200002836?tab=overview).  
On this page, click **GET IT NOW**, then enter email address of the Office 365 account you want to install the Add-In for and sign in via standard O365 login dialog 

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Using-SmartCloud-Connect\get_it_now.png" class="minimized">
<br>    
<br>
<img src="..\..\assets\images\Using-SmartCloud-Connect\login_MS.png">
</p></details>


&nbsp;



**2\.3\.** Select the standard "*I give Microsoft permission ...*" checkbox in the dialog and click **Continue** to grant Microsoft permission to use/share your basic mail account information for {{ product_name }} Add-In

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Using-SmartCloud-Connect\MS_permission.png">
</p></details> 



&nbsp;

**2\.4\.** You will briefly see a redirect window

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Install-and-Run\taking-to-o365.png">
</p></details> 
&nbsp;

Now the Add-In is installed for your mail account.

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Install-and-Run\installed.png" class="minimized">
</p></details> 


&nbsp;

!!! note "Note"
    After you install the Add-In this way, it will also be added to your MS Outlook (desktop) with the corresponding MS Exchange user account logged in

!!! warning "Important"
    Before using the {{ product_name }} Add-In in MS Outlook Desktop on Windows, please make sure that you have the latest version of MS Edge installed, since it is used to render the {{ product_name }}

&nbsp;
* * *
&nbsp;

## II. {{ product_name }} logon

!!! note "Note"
    {{ short_name }} logging on is not instant: depending on the number of email messages in your mailbox and items in your calendar it may take several minutes to log on, since on logging on {{ short_name }} needs to [match](../Initial-Search-and-Applied-Record-Filters/) all your existing correspondence and calendar items with your Salesforce records. That is only performed once per account

Before you start, please make sure that you have an active Salesforce account and an Office 365 account and you got your login credentials for these services at hand.  
After {{ product_name }} Add-In has been installed in your Office 365, you need to [open the Sidebar in MS Outlook](../Open-in-Outlook-Web/) and log on to the Add-In.

**1\.** To open the Sidebar:

*   click the **Open {{ product_name }}** button in MS Outlook Desktop ribbon

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b6b03020428631d7a89c543.png)

&nbsp;

* or, if you are using Outlook on the Web (Outlook.com, Outlook.office.com), refer to [this article](../Open-in-Outlook-Web/) to learn how to open the Sidebar 

&nbsp;
* * *
&nbsp;
**2.** Next, log on to {{ product_name }}:

&nbsp;&nbsp;&nbsp;&nbsp; **2.1.** Click the **Connect to Salesforce** button. A browser window with Salesforce [OAuth](http://help.salesforce.com/articleView?id=remoteaccess_authenticate_overview.htm) page will be opened

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b6b05ce0428631d7a89c563.png)

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp; **2.2.** Enter your Salesforce credentials on the page or select a previously saved account's username and click **Log In**

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b6b07ba2c7d3a03f89d7a23.png)

&nbsp;



In the screenshot above, a standard Salesforce login window is shown. Note that this OAuth window may look differently, depending on your Salesforce configuration.

!!! note "Note"
    At this point you may also need to confirm this access via [Salesforce 2-factor authentication](https://help.salesforce.com/articleView?id=security_overview_2fa.htm&type=5)

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp; **2.3.** Now you need to authorize {{ product_name }} to work with your Salesforce data, by clicking **Allow** in the following dialog window:

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b6c74252c7d3a03f89d85de.png)

&nbsp;

!!! note "Note"
    {{ product_name }} accesses and handles the end users' email and CRM data in a most secure and private manner, according to our [Privacy and Security guarantees](https://revenuegrid.com/privacy-policy/), so allowing this data access is safe 

&nbsp;

**3.** The next setup step to complete before you can use all {{ product_name }} features is to activate [{{ company_name }} synchronization](../Synchronization-Engine-An-Overview/) by authorizing it to access your Office 365 data. 

In the latest {{ product_name }} updates you can easily do that right after your first log on to [{{ product_name }}](../Introduction/), via the following screen:

![](../assets/images/Install-and-Run/o365_creds.png)

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;**3\.1.** Click **Connect to Office 365** 

&nbsp;&nbsp;&nbsp;&nbsp;**3\.2.** Enter your login credentials in the Office 365 login window opened in your browser

!!! warning "Important"
    If you are using several different email boxes for your correspondence (not [aliases](https://support.office.com/en-us/article/add-or-remove-an-email-alias-in-outlook-com-459b1989-356d-40fa-a689-8f285b13f1f2)), make sure to authorize [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/) for the same email box as one for which you installed the [Add-In](../Introduction/), otherwise the [Sync engine functions](../AddIn-vs-Sync-Functions/) will work incorrectly even though {{ short_name }} Sync will appear to be running

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;**3\.3.** Click **Accept** in the Permissions requested dialog. At this point you may need to confirm this access via [Office 365 2-factor verification](https://support.office.com/en-us/article/sign-in-to-office-365-with-2-step-verification-2b856342-170a-438e-9a4f-3c092394d3cb)



<details><summary> >>> Click to see screenshots <<< </summary>
<p><img src="..\..\assets\images\Using-SmartCloud-Connect\login_MS.png"><br><br>
<img src="..\..\assets\images\Install-and-Run\permissions_requested.png">
</p></details> 

&nbsp;

!!! warning "Important"
    Note that if the Sync activation is skipped, a number of [key {{ product_name }} features performed by {{ short_name }} Synchronization](../AddIn-vs-Sync-Functions/) will be unavailable



!!! tip "Tip"
    Refer to [this article](../Historical-Sync-&-Timezones-Matching/) to learn what emails and calendar items you have in MS Exchange / Office 365 will be auto-saved in Salesforce after activating {{ company_name }} synchronization if you enable the corresponding settings ([calendar items auto-saving](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#meeting_appointment_autosaving), [emails auto-saving](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_emails_emails_autosharing))


&nbsp;
* * *
&nbsp;

## III. (Admins only) Install the managed packages in Salesforce

To enable the full scope of features offered by {{ product_name }} several minor adjustments must be made in your Salesforce Org's configuration; installing the [{{ company_name }} managed package](../Admin-Managed-Package/) and [Invisible Suite managed package](../Admin-Managed-Package/) allows to accomplish that quickly and effortlessly. Follow the above links for complete information about the packages.

&#160;
 &#160;

