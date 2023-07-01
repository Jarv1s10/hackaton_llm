---
description: RG Email Sidebar full deployment scenarios for multiple end users
---
# Email Integration Full Deployment Scenarios  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*3 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

Setting up {{ short_name }} [Add-In](../Introduction/) and [Synchronization](../Synchronization-Engine-An-Overview/) for multiple end users is a standard procedure performed by the local mail server Admin and [Salesforce/{{ short_name }} admin](../How-to-Log-In-to-the-Admin-Panel/).  
The following scenarios can be applied to deploy {{ product_name }}  

!!! note "Note"
    {{ product_name }} is **not** a standalone application: it is installed in MS Outlook Desktop, Web, or Mobile implementation as an Add-In, or in the Chrome browser as a browser Extension for Gmail

&nbsp;

!!! tip "Tip"
    {{ product_name }} can also be installed in a private corporate Azure cloud on back end, if that is required by the company's security requirements. [Contact our CSM team](mailto:support@revenuegrid.com) for more information about this possibility. The deployment procedures used in such scenario are identical to the regular ones used for RevenueGrid Azure servers deployment

&nbsp;

### Scenarios for MS Exchange or Office 365 mail accounts via {{ short_name }} Outlook Add-In

&nbsp;

!!! tip "Tip"
    Also see [this article](../Managing-Organizations-via-the-Admin-Panel/#configuring_connection_type_for_an_organization) to learn about all mail server connectivity types compatible with {{ product_name }}

&nbsp;

| Deployment scenario                                          | Required Admin actions*****                                  | Required User actions<br />([Registration wizard](https://revenuegrid.com/csm-wizard/) recommended) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **A.** Full {{ short_name }} deployment for all users by the Admin, except for individual Add-In logon: see the scenario F below (involves [Impersonated Access](../Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/), thus not suitable for all configurations) | 1. [Set up an Impersonating service account in MS Exchange](https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/how-to-configure-impersonation)<br />2. Mass-deploy the Add-In for all end users in [MS Exchange](../Mass-Deployment-of-the-Add-In-MS-Exchange/) or [Office 365](../Mass-Deployment-of-the-Add-In-Office-365/) via [Impersonating account](../Impersonation-O365/). {{ short_name }} Sync will be auto-activated on the users' first logon to the Add-In | [Log on to the Add-In in MS Outlook/Office.com](../How-to-Install-and-Run-the-Solution-for-Office-365-Mailboxes/#ii_smartcloud_connect_logon) |
| **B.** Only Add-In mass deployment by the Admin              | 1. Mass-deploy the Add-In for all end users in [MS Exchange](../Mass-Deployment-of-the-Add-In-MS-Exchange/) or [Office 365](../Mass-Deployment-of-the-Add-In-Office-365/) (without Impersonating account). In this case {{ short_name }} Sync is [to be activated by the end users](../Authorizing-Sync-Engine-to-Work-with-Your-Data/) | 1. [Log on to the Add-In](../How-to-Install-and-Run-the-Solution-for-Office-365-Mailboxes/#ii_smartcloud_connect_logon)<br />2. [Activate {{ short_name }} Sync](../Authorizing-Sync-Engine-to-Work-with-Your-Data/) |
| **C.** Only {{ short_name }} Sync activation, through Impersonated account | 1. [Set up an Impersonated service account in MS Exchange / Office 365](https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/how-to-configure-impersonation)<br />2. [Set up mailbox access in {{ short_name }} admin panel](../Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/#configuring_mailbox_access_for_scc_sync) | 1. [Install the Add-In](../How-to-Install-and-Run-the-Solution-for-Office-365-Mailboxes/#i_install_smartcloud_connect_add-in_via_installation_wizard)<br />2. [Log on the the Add-In](../How-to-Install-and-Run-the-Solution-for-Office-365-Mailboxes/#ii_smartcloud_connect_logon) |
| **D.** Full installation by individual end users             | No special Admin actions save for *****                      | 1. [Install the Add-In](../How-to-Install-and-Run-the-Solution-for-Office-365-Mailboxes/#i_install_smartcloud_connect_add-in_via_installation_wizard)<br />2. [Log on to the Add-In](../How-to-Install-and-Run-the-Solution-for-Office-365-Mailboxes/#ii_smartcloud_connect_logon)<br />3. [Activate {{ short_name }} Sync](../Authorizing-Sync-Engine-to-Work-with-Your-Data/) |
| **F.** Automatic {{ product_name }} logon using a Salesforce service account | Create a dedicated Salesforce account with special permissions and configure it to impersonate {{ short_name }} users' accounts. See [this article](../Set-up-Salesforce-Auth/) for details. | 1. [Install the Add-In](../How-to-Install-and-Run-the-Solution-for-Office-365-Mailboxes/#i_install_smartcloud_connect_add-in_via_installation_wizard)<br />2. [Activate {{ short_name }} Sync](../Authorizing-Sync-Engine-to-Work-with-Your-Data/) via the Sidebar |

***** there are two additional local Admin actions to be performed for every listed scenario:  
❍ [ensure that the Add-In's connections are not blocked by the corporate firewall](../Overcoming-Firewall-Issues/) and  
❍ [install the {{ company_name }} managed package in Salesforce to ensure maximum interaction efficiency](../Admin-Managed-Package/)

&nbsp;

* * *

&nbsp;

&nbsp;

### Scenarios for Gmail account via [{{ short_name }} Chrome Extension](../Chrome-Extension-Intro/)

**[this section is work-in-progress]**

| Deployment scenario                                          | Required Admin actions*****                                  | Required User actions<br />([Registration wizard](https://revenuegrid.com/csm-wizard/) recommended) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **A.** Full {{ short_name }} deployment for all users by the Admin, except for individual Extension logon (involves [Impersonated Access](../Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/))<br  />Can only be performed for Windows OS, using [MS Active directory](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview) | **1\.** [Mass-install the Chrome Extension](../Chrome-Extension-Mass-Deployment/) for all end users<br />**2\.** [Configure a service Gmail account and mass-sign in to Salesforce for all end users through it](../Gmail-Users-Mass-Provisioning/)<br /> | Login to the corporate Gmail / Google Workspace (G Suite) account in Chrome Browser |
| **B.** The Chrome Extension is deployed for all users by the Admin.<br />Using Google native procedures or MS Active Directory | [Using Google native procedures](https://support.google.com/chrome/a/answer/6306504?hl=en)<br />[Using MS Active Directory means](../Chrome-Extension-Mass-Deployment/)<br /> | **1\.** Login to the corporate Gmail / Google Workspace (G Suite) account in Chrome Browser<br />**2\.** [Sign in to the Chrome Extension](../How-to-Set-Up-the-Chrome-Extension-for-Salesforce-and-Gmail/#2_sign_in_to_gmail_and_grant_smartcloud_connect_permission_to_work_with_your_gmail_and_google_calendar_data)<br /> |
| **C.** [Chrome Extension's Synchronization](../Synchronization-Engine-An-Overview/) is mass-activated by the Admin | [Configure a service Gmail account and mass-sign in to Salesforce for all end users through it](../Gmail-Users-Mass-Provisioning/)<br /> | **1\.** [Install the Chrome Extension](../How-to-Set-Up-the-Chrome-Extension-for-Salesforce-and-Gmail/)<br />**2\.** Login to the corporate Gmail / Google Workspace (G Suite) account in Chrome Browser<br /> |

&nbsp;

***** there are two additional local Admin actions to be performed for every listed scenario:  
❍ [Ensure that the Extension's connections are not blocked by the corporate firewall](../Overcoming-Firewall-Issues/) and  
❍ [Install the {{ company_name }} managed package in Salesforce to ensure maximum interaction efficiency](../Admin-Managed-Package/)



&#160;
 &#160;

