---
description: Step-by-step guide on authorizing sync engine in corporate Office 365 / Azure settings
---
# How to Authorize Sync Engine in Corporate Office 365 / Azure Settings  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

[{{ company_name }} Sync](../Synchronization-Engine-An-Overview/) is ready to be connected to [any supported email server](../Supported-Email-Services/) out of the box. Similarly to [{{ short_name }} Add-In](../Introduction/) [installed for end users' mail accounts](../How-to-Install-and-Run-the-Solution-for-Office-365-Mailboxes/), it is a server app that requires specific server-side permissions to run for individual users. Specifically, security policies configuration established in a company's Office 365 / Azure infrastructure should explicitly allow the app to run; that can be ensured by the local Administrator via [Microsoft 365 Admin center](https://docs.microsoft.com/en-us/microsoft-365/admin/admin-overview/about-the-admin-center?view=o365-worldwide) and [Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/methods-for-assigning-users-and-groups).  

This troubleshooting article addresses the three common issues which may prevent {{ short_name }} Sync engine's functioning on server side.

!!! tip "Tip"
    Also see [this {{ short_name }} FAQ entry](../Frequently-Asked-Questions/#28_my_company_purchased_several_licenses_of_rg_email_sidebar_how_can_i_manage_various_aspects_of_the_solutions_functioning_eg_the_end_users_rges_sync_and_their_access_to_customization_settings_or_adjust_the_under-the-hood_settings) to learn what data access permissions the solution requires to perform its functions

&nbsp;

### I. Check your corporate firewall configuration

See [this article](../Overcoming-Firewall-Issues/) for complete information on how to do that.

&nbsp;

* * *

&nbsp;

### II. Adjust Azure server Enterprise Applications configuration

Steps how to do that:  

**1\.**    Log in to the Azure management portal <https://portal.azure.com> with Admin credentials  

**2\.**    Click on **All services** in the Main menu  

**3\.**    Select the directory you are using for the {{ product_name }} server app  

**4\.**    Click on the **Enterprise applications** tab  

**5\.**    Select the application from the list of applications associated with this directory  

**6\.**    Click the **Properties** tab  

**7\.**    Change the **Enabled for users to sign-in?** toggle to **Yes**  

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/config.png" class="minimized">
</p>

&nbsp;

**8\.** It is also recommended (but not required) to enable the **User assignment required?** toggle; this allows the end users [to authorize {{ company_name }} sync](../Authorizing-Sync-Engine-to-Work-with-Your-Data/) independently from the Admin

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/recommended.png" class="minimized">
</p>

&nbsp;

**9\.**    Click the **Save** button at the top of the page  

**10\.** In addition, check whether the {{ product_name }} application with the ID indicated in the error notification you got is on the list of applications (*added/allow-listed* for the users to be assigned)


 &nbsp;

* * *

&nbsp;

 

### III. To resolve the "You can't access this application" error on users authentication [via a service account](../Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/)

If you get an error notification containing the message "*{{ product_name }} needs permission to access resources in your  organization that only an admin can grant. Please ask an admin to grant  permission to this app before you can use it*" or a status code *AADSTS90094*, you need to adjust your Office 365 settings to allow the end users to sign in to apps like {{ company_name }} Sync.

![](../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/authorization-admin.jpg)

&nbsp;

#### Why does this error occur?

The most common cause is when the end users have no permission to confirm [OAuth](https://oauth.net/2/) consent screens for an application, unless they have Admin rights within your Office 365 tenant. Enterprise apps like {{ product_name }} use OAuth as a more secure way to authorize scoped access to your Office 365 tenant email and calendar data with a username and password. Learn more about service principals and Enterprise app permissions [here](https://support.robinpowered.com/hc/en-us/articles/360000467043).

&nbsp;

&nbsp;

### Additional Microsoft articles for your reference

- [Assign a user or group to an enterprise app in Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/assign-user-or-group-access-portal)
- [How to assign users and groups to an application](https://docs.microsoft.com/en-us/azure/active-directory/application-access-assignment-how-to-add-assignment) 
- [Apps, permissions, and consent in Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/active-directory-apps-permissions-consent#controls) 
- [Assign a user or group to an enterprise app in Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/active-directory-coreapps-assign-user-azure-portal) 



&#160;
&#160;

