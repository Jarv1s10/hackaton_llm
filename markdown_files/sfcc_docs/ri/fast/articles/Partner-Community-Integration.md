---
description: Learn the specifics of Revenue Grid integration with Salesforce Customer / Partner Community Environments.
---
# {{ company_name }} Integration with Salesforce Customer / Partner Community Environments  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*3 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

## Customer / Partner Community environment integration specifics

&nbsp;

!!! tip "Tip"
    Also see [this article](../Partner-Community-Authorization/) to learn how to log in to a Salesforce Customer / Partner Community environment
&nbsp;

!!! warning "Important"
    {{ company_name }} supports only the following Salesforce Experience Cloud subdomains: <u>force.com</u>, <u>salesforce.com</u>, <u>siteforce.com</u>, <u>my.site.com</u>


&nbsp;

[{{ short_name }} Add-In](../Introduction/) and [Sync engine](../Synchronization-Engine-An-Overview/) provide a special possibility to capture CRM data for [Salesforce Customer / Partner Community environments](https://help.salesforce.com/s/articleView?id=000335630&type=1) integrated with different MS Exchange or Google mail instances, i.e. authorized mail servers used by company's partners or customers entitled to access specific segment of a shared CRM environment. 

This is organized in the same secure and Salesforce config specific manner as for corporate infrastructures which include several dedicated email servers/domains, e.g. ones used by different branches of a company. Each {{ short_company_name }} backend unit is a multi-tenant entity, hosting multiple company entities as dedicated tenants and end user groups. Within this infrastructure, each tenant‘s and each user’s data is securely isolated from the rest and no unauthorized data access is possible. On new Customer / Partner Community users provisioning in the system, a HMAC-based server-to-server authentication scheme with request signing via a secret shared between the sender and the recipient is applied, along with protection from replay attacks involving a nonce value and timestamps, ensuring that provisioning requests are performed only by an entitled authorized party and this access is spoofing-proof. 

No user data or access credentials are consistently stored or anyhow exposed to disclosing within {{ short_name }} infrastructure, the system leverages Salesforce and Exchange/O365 or Google native data access authorization methods via individual users OAuth and other token types instead of access credentials.  

For all such scenarios, in-org, different branch, or customer / partner community, users' data handling is performed in an isolated targeted manner that always observes the [access rules set for individual users or groups of users in Salesforce](https://help.salesforce.com/s/articleView?id=sf.perm_sets_overview.htm&type=5). When a provisioned customer / partner user gets [server-side Sync activated](../Authorizing-Sync-Engine-to-Work-with-Your-Data/) and [logs in to {{ short_name }} Add-In](../How-to-Install-and-Run-the-Solution-all-configurations/#ii_rg_email_sidebar_logon), their access to the shared Salesforce environment is authorized via OAuth 2.0 or [another supported mechanism](../Managing-Organizations-via-the-Admin-Panel/#configuring_connection_type_for_an_organization) and in this environment {{ short_name }} has the same data viewing and editing permissions scope as the user has when they open their Salesforce account in a browser. A single email account is connected to a single designated Salesforce account and the system ensures that no unauthorized data access, modification, leakage, or hijacking is possible.  

The data that a customer/partner community user may capture in Salesforce from their MS Exchange mailbox is defined by [{{ short_name }}'s selective or automated capturing mechanisms](../How-the-Solution-Works-and-What-It-Syncs/) and [Sync settings](../Configuring-Activities-Synchronization-Settings/) as well as the actual write/edit permissions on the Salesforce side.

Also note that {{ short_name }} can work with up to 4 email aliases available for configured end users' MS Exchange mailbox. See [this article](../MS-Exchange-Aliases-Handling/) for more information. 

The below diagram illustrates the backend architecture of individual users' data processing in the {{ short_name }} system.

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src= "..\..\assets\images\Using-SmartCloud-Connect\How-It-Works\Sync-Community\auth-community.png" class="minimized">
</p></details> 

&nbsp;

&nbsp;

&nbsp;

## Lightning Scheduler integration specifics

&nbsp;

!!! tip "Tip"
    Also see [this article](../Partner-Community-Authorization/) to learn how to configure Lightning Scheduler integration for {{ short_name }}

&nbsp;

For {{ short_name }} [integration with Salesforce Lightning Scheduler](../Lightning-Scheduler-API/), data processing also follows the same principles of security and isolation. The data being transferred for Lightning Scheduler integration purposes is solely the Free/Occupied slots information from the user's calendar, no other details are read or transferred.  
Even though Lightning Scheduler integration config involves a Salesforce Admin user account for connectivity authorization, calendar data transfers are carried out on the same "single MS Exchange mail account ↔ single associated Salesforce account" basis, ensuring that no unauthorized data access, modification, leakage, or hijacking is possible. This is also true for Customer / Partner Community Lightning Scheduler usage with {{ product_name }}. 



&nbsp;

&nbsp;

