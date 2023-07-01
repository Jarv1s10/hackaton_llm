---
description: Detailed guidance on revoking a mailbox access token
---
# How to Revoke a Mailbox Access Token  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

MS Exchange or Office 365 Mailbox access token revoking is sometimes required on [{{ short_name }} Sync Engine troubleshooting](../Handling-Sync-Issues/), specifically if [Sync was misconfigured](../Authorizing-Sync-Engine-to-Work-with-Your-Data/) or a user account was [moved to another {{ short_name }} tenant](../Managing-Users-via-the-Solution-s-Admin-Panel/).
&nbsp;

### To revoke {{ short_name }} Sync access Token for Office 365 mailboxes

!!! note "Note"
    Depending on your MS Office 365 or Exchange configuration, the access token revoking procedure might require contacting your local mail server Admin. See [this Microsoft article](https://docs.microsoft.com/en-us/azure/active-directory/enterprise-users/users-revoke-access) for more information

&nbsp;

**1\.** Open the direct link <https://portal.office.com/account/?ref=MeControl> and log on to O365, if needed   

&nbsp;

**2\.** Select **App permissions** in the navigation pane on the left  

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\revoke-token2.png">
</p>

&nbsp;

**3\.** Click **Revoke** under *Revenue Inbox* the the main pane  

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\revoke-token3.png" class="minimized">
</p>

&nbsp;

**4\.** Log out from {{ short_name }} Add-In and then [log in again](../How-to-Install-and-Run-the-Solution-for-Office-365-Mailboxes/#ii_rg_email_sidebar_logon)  

&nbsp;

Now the access token has been revoked and you need to [activate {{ short_name }} Sync engine afresh](../Authorizing-Sync-Engine-to-Work-with-Your-Data/) providing [all required permissions](https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#29_what_exchange_data_access_permissions_admin_consent_does_rg_email_sidebar_require_is_it_possible_to_limit_this_app_to_be_used_only_by_specific_users_or_groups_of_users_in_our_company) to resume its functioning.

&nbsp;

&nbsp;

