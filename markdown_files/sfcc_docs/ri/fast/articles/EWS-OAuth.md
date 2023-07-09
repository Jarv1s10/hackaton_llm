---
description: Learn how to authorize mailbox data access via O365 OAuth for EWS
---
# How to Authorize Mailbox Data Access via O365 OAuth for EWS  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

[MS Office 365 OAuth](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow) authentication method can be used to [authorize {{ short_name }} Sync to access end users' Office 365 mail](../Authorizing-Sync-Engine-to-Work-with-Your-Data/) data over [EWS connection](../Working-With-EWS/).  
This method is also the only way to authorize an [Exchange Impersonation service account](../Impersonation-O365/) for Office 365 mailboxes, since the old Impersonated access authorization method with login and password creds entry will be removed by Microsoft in 2021. 

&nbsp;

### Users data access authorization by {{ short_name }} via OAuth 2.0

You need to activate [{{ company_name }} Synchronization](../Synchronization-Engine-An-Overview/) in the following cases:

- on the first start, if {{ short_name }} Sync was not [mass-activated by the local Admin](../Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/), for example in case [mass deployment](../Email-Integration-Full-Deployment-Scenarios/) through [Exchange Impersonation](../Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/) cannot be used in your company's configuration for any reason  
- if {{ short_name }} Sync's mailbox access expired or your mailbox password was changed

&nbsp;

!!! tip "Tip"
    In the latest {{ product_name }} updates the users are [prompted to enable {{ short_name }} Sync for Office 365 on the first {{ product_name }} logon](../How-to-Install-and-Run-the-Solution-for-Office-365-Mailboxes/#ii_smartcloud_connect_logon)

&nbsp;

Follow the steps below to do that:  

**1.** In [{{ product_name }}](../Introduction/#introduction_to_smartcoud_connect), click the **☰** (**Menu**) button in the upper left corner and select **Set up sync** (or **Sync settings**) in the Menu that appears

![](../assets/images/Using-SmartCloud-Connect/How-To-s/Sync-Settings/sync_setup.png)

&nbsp;

**2\.** Enter your Office 365 login credentials in the O365 [OAuth 2.0](https://oauth.net/2/) dialog that appears



![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b6b2a3d2c7d3a03f89d7bba.png)

&nbsp;

Next, Office 365 will request your confirmation; click **Accept** in this dialog to complete Sync activation. Your email data accessed by {{ company_name }} Sync engine remains all secure and private, under our [Privacy & Security principles](../Privacy-and-Security/).

![](../assets/images/Install-and-Run/permissions_requested.png)

&nbsp;

After access has been authorized, [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/) will start running every 30 minutes 24/7 for this email account. 

!!! tip "Tip"
    Should you encounter the "Need Admin Approval" error in this dialog, refer to [this article](../Need-Admin-Approval/) to learn how to resolve it

&nbsp;

&nbsp;







&nbsp;

