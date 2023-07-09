---
description: Learn how to use app-only access to 
---
# How to Deploy the Solution via App-Only Access for MS Graph [Office 365]  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*6 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! tip "Tip"
    See [this article](../Impersonation-O365/) if your company uses an Office 365 mail server over [Exchange Web Services](../Working-With-EWS/) instead of MS Graph. Or [this article](../Set-up-An-Impersonation-Service-Account/) in case your company uses an MS Exchange On Premises mail server, or [this article](../Impersonation-Alternative/) for [Hybrid mail server deployment options](https://docs.microsoft.com/en-us/exchange/exchange-hybrid)

&nbsp;

!!! note "Note"
    Privacy and security of any data access and handling associated with {{ product_name }} deployment procedures are guaranteed by the [applicable {{ company_name }} policies](https://revenuegrid.com/privacy-policy/)

&nbsp;

{{ product_name }} can connect to MS Office 365 mail accounts over [app-only access](https://learn.microsoft.com/en-us/azure/active-directory/develop/app-only-access-primer) for MS Graph, as a more up-to-date and versatile alternative to [Exchange Web Services](../Working-With-EWS/). See [this article](../MS-Graph/) for complete information on using app-only access. Unlike the Impersonation deployment scenarios (see the links in the *Tip* above), this connection type does **not** require [configuring an Impersonation service account](../Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/).

&nbsp;

For MS Graph app-only-access connection type, a special Profile-wide mass deployment procedure is used. Follow the instructions below to deploy the solution over app-only access. 

&nbsp;

&nbsp;

## The procedure consists of three Stages

Most steps are performed in [{{ short_company_name }} Admin panel](../How-to-Log-In-to-the-Admin-Panel/), except for the Admin consent permissions prerequisite configured in [Microsoft Office 365 Admin center](https://docs.microsoft.com/en-us/microsoft-365/admin/admin-overview/about-the-admin-center?view=o365-worldwide) and {{ short_company_name }} access limiting to specific user accounts.

&nbsp;

**Stage 1.** Create a Profile with [app-only access](../Managing-Organizations-via-the-Admin-Panel/#configuring_connection_type_for_an_organization) via [{{ short_name }} Admin panel](../Managing-Organizations-via-the-Admin-Panel/) or convert an existing Office 365 Org to this connection type [described in this section](#stage_1_create_an_ms_graph_impersonation_org_via_rges_admin_panel_or_switch_users_to_ms_graph_connection)

&nbsp;

**Stage 2.** Grant [permissions consent](https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#for_ms_graph_o365_server_connection) via mail server Admin account [described in this section](#stage_2_grant_permissions_consent_by_mail_server_admin_account)

&nbsp;

**Stage 3.** Verify the Configuration [described in this section](#stage_3_verify_the_connectivity)   

&nbsp;

&nbsp;

## Stage 1: Create an MS Graph app-only access Org via {{ short_name }} Admin panel or switch users to MS Graph connection

&nbsp;

To authorize {{ company_name }} access to end users' mail data over MS Graph, the local mail server Admin should:  

**1\.1.** [Log in to {{ short_name }} Admin panel](../Managing-Organizations-via-the-Admin-Panel/) with Admin credentials. You will see the default Org's tab upon logging in

**1\.2.** Create an Organization as described in [this article](../Managing-Organizations-via-the-Admin-Panel/#creating_organizations):

- In the upper right corner of the Organizations tab, click **New**  
- Fill in the **Name** field for the Org
- Fill in the **External Id** field (the value becomes read-only and cannot be changed later)

**1\.3.** Click **Save** in the upper right corner to complete Org creation

**1\.4.** [Move existing Office 365 user accounts to this Org](../Managing-Users-via-the-Solution-s-Admin-Panel/#moving_users_between_organizations) or [provision new {{ short_name }} users](../User-Registration-Wizard/) within it

&nbsp;

&nbsp;

### To Switch a User to MS Graph Connection in Admin panel

Alternatively, in case {{ product_name }} was originally deployed for the users over another connection type and you want to switch them to MS Graph, this possibility is implemented via [{{ short_name }} Admin panel](../How-to-Log-In-to-the-Admin-Panel/). To do that, follow the steps below:  

**1\.** [Log in to {{ short_name }} Admin panel](../Managing-Organizations-via-the-Admin-Panel/) with Admin credentials. You will see the default Org's tab upon logging in

**2\.** Open [the subtab **Users**](../Managing-Users-via-the-Solution-s-Admin-Panel/)

**3\.** Click on the user that you want to switch to MS Graph

**4\.** Click the **⚙** (Actions Menu) icon in the upper right corner of the tab and select **Check Mailbox Connectivity** in the picklist

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\MS-Graph\switch-1.png" class="minimized">
</p>
&nbsp;

If the user presently belongs to an [MS Graph app-only access Org](../Managing-Organizations-via-the-Admin-Panel/#configuring_connection_type_for_an_organization), this action results in user switching to MS Graph app-only access connection.

You will see a Sync Error line *Cancelled* under user account details and if you click on it a notification about connectivity type switching being carried out will appear.

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\MS-Graph\connection-switch.png">
</p>

&nbsp;

Connection type swtiching will be completed after the following successful [{{ short_name }} sync session](../Synchronization-Engine-An-Overview/). You may [Force Synchronization from the user's page](../Managing-Users-via-the-Solution-s-Admin-Panel/#actions_with_users) to expedite that.

As soon as switching is complete for the user, the indication **Mailbox Status** will change to *Initialized*.


&nbsp;

* * *

&nbsp;

## Stage 2: Grant permissions consent by mail server Admin account

&nbsp;

On Microsoft 356 Admin Center Side, the {{ product_name }} App requires the following set of access consent permissions. See [this Microsoft article](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/grant-admin-consent) for complete information an app permissions configuring.

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\MS-Graph\permissions-graph.png" class="minimized">
</p>

&nbsp;

To authorize {{ product_name }} access to end users' mail data over MS Graph, the local mail server Admin should do the following:  

**2\.1.** [Log in to {{ short_company_name }} Admin panel](../Managing-Organizations-via-the-Admin-Panel/) with Admin credentials. 

**2\.2.** Find the necessary profile and open [the **Connectivity** subtab](../Managing-Organizations-via-the-Admin-Panel/)

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\MS-Graph\email-config.png" class="minimized">
</p>

&nbsp;

**2\.3.** Click the button **Microsoft 365 OAuth (Graph API)**

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\MS-Graph\grant-permissions.png" class="minimized">
</p>

&nbsp;

**2\.4.** A [standard Office 365 OAuth window](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-v2-protocols) will appear. Select Microsoft 365 Admin's account or enter the login credentials in the dialog. Don't worry, this authorization will be used exclusively to grant the access permissions for MS Graph app-only access

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Install-and-Run\SyncAuth\oauth.png">
</p></details>




**2\.5.** Next, you will see the Permissions authorization dialog

On {{ product_name }} side, the set of permissions is individually configured for every Enterprise customer's Org by [our Support team](mailto:support@revenuegrid.com). Each permission is required to provide a [specific {{ product_name }} function](../Introduction/#key_revenue_inbox_features), so if some permissions are not granted the corresponding features become unavailable

<details><summary> >>> Click to see the full permissions list and a screenshot <<< </summary>
<p><b>The complete list of permissions</b>
<br>
<br>
<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\MS-Graph\permissions-rg.png">
</p></details>
&nbsp;

Click **Accept** in the bottom right corner of the dialog to grant the permissions.

If everything went well, you will see a notification *"Signed in successfully"*, then will read *Impersonation status: Authorized* in the Email Configuration tab.



&nbsp;

&nbsp;

### {{ short_name }} App Access Limiting to Specific User Accounts (optional)

In many configurations {{ short_name }} mailbox data access granted over app-only access must be limited to a specific group of entitled users. That is accomplished using Blacklist and Whitelist settings.

Follow the steps below to set the exact list of entitled users. Based on [this Microsoft article](https://docs.microsoft.com/en-us/graph/auth-limit-mailbox-access).

&nbsp;

**Configure ApplicationAccessPolicy**

To configure an application access policy and limit the scope of application permissions:

**1\.** Connect to Exchange Online PowerShell. For details, see [Connect to Exchange Online PowerShell](https://docs.microsoft.com/en-us/powershell/exchange/exchange-online/connect-to-exchange-online-powershell/connect-to-exchange-online-powershell?view=exchange-ps&preserve-view=true)

**2\.** Identify the app’s client ID and a mail-enabled security group to restrict the app’s access to

   - Identify the app’s application (client) ID in the [Azure app registration portal](https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationsListBlade)
   - Create a new mail-enabled security group or use an existing one and identify the email address for the group

**3\.** Create an application access policy

   Run the following command, replacing the arguments for **AppId**, **PolicyScopeGroupId**, and **Description**

  

```
New-ApplicationAccessPolicy -AppId e7e4dbfc-046f-4074-9b3b-2ae8f144f59b -PolicyScopeGroupId EvenUsers@contoso.com -AccessRight RestrictAccess -Description "Restrict this app to members of distribution group EvenUsers."
```

**4\.** Test the newly created application access policy.

Run the following command, replacing the arguments for **Identity** and **AppId**.

```
Test-ApplicationAccessPolicy -Identity user1@contoso.com -AppId e7e4dbfc-046-4074-9b3b-2ae8f144f59b 
```

   The output of this command will indicate whether the app has access to User1’s mailbox.

That the changes to app access policies can take up to 30 minutes to get applied in Microsoft Graph REST API calls.


&nbsp;

* * *


&nbsp;

## Stage 3: Verify the Connectivity

&nbsp;

**3\.1.** [Log in to {{ short_name }} Admin panel](../Managing-Organizations-via-the-Admin-Panel/) with Admin credentials. You will see the default Org's tab upon logging in

**3\.2.** Open [the subtab **Email configuration**](../Managing-Organizations-via-the-Admin-Panel/)

**3\.3.** Click **Check Users Exchange Impersonated Access** in the upper right corner of the tab

As soon as you click on this button, all user accounts moved to the MS Graph app-only access Org get automatically re-configured to work over app-only access connection.

If everything was configured correctly, you will see a green indication that app-only connection connection of all users in the Org was successful:

*Status: Success*
*Check Results: connected successfully*



&nbsp;

&nbsp;

