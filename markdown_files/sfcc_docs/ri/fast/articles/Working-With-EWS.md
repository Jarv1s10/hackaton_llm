---
description: Learn how to work with MS Exchange EWS
---
# How the Solution Works with MS Exchange EWS  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*4 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

{{ product_name }} is designed to run concurrently with other processes engaging a mail server's [Exchange Web Services (EWS)](https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/start-using-web-services-in-exchange) and provides the customers with the necessary controls regulating EWS access by {{ product_name }}. 

&nbsp; 

### What EWS access control tools allow:

#### **Different [deployment](../Email-Integration-Full-Deployment-Scenarios/) options**

{{ product_name }} supports Multi-Tenant, Single-Tenant, and On-Premise scenarios.

   - These scenarios imply various levels of data and configuration isolation between tenants: logical isolation for Multi-tenant instances, physical isolation for Single-tenant instances, of full customer control for On-premise deployments
  - As a best use practice, Multi-tenant deployment is recommended as the most cost-efficient one for an average customer, also providing a solid level of security. Other options should be considered if specific security requirements prohibit Multi-tenant operation in your Org

&nbsp;

#### **IP Address restrictions: {{ product_name }} operates via a fixed set of IP addresses**

The customers using corporate firewall IP address restrictions for Salesforce or MS Exchange servers connection need to allow-list specific IP addresses used by {{ product_name }}.

 - Such whitelisting is complementary, it does not block any existing server traffic  

  - See more details on configuring IP restrictions and the list of IP addresses used in Multi-tenant environments [here](../Overcoming-Firewall-Issues/)  

   - For Single-tenant configurations a specific list is communicated during {{ product_name }} deployment  

  - As a best practice, such configuration should be added over the current customer configuration, to prevent interfering with existing traffic  

&nbsp;

#### **Filtering {{ product_name }} EWS traffic {{ product_name }}**

Filtering can be configured to use a pre-set UserAgent header on every EWS call made to the customer's MS Exchange server. Such configuration allows traffic filtering on multiple levels:

  - On MS Exchange / Office 365 side: using MS Exchange controls, as documented [here](https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/how-to-control-access-to-ews-in-exchange)

     - This configuration control allows additive listing of allow-listed applications, and if used by in a customer's Org it may be extended to include traffic from/to {{ product_name }}

  - By a stateful firewall which can block HTTPS traffic
    - As in the above case, a custom rule can be built based on an added UserAgent HTTP header to allow {{ product_name }}-originated EWS traffic pass through, in addition to any other allowed traffic
    
  - The value of the UserAgent header for all EWS traffic can be set as requested by a customer

  - As a best practice, customers who already implemented EWS traffic filtering using one of the above approaches should consider extending their configuration to allow {{ product_name }} EWS traffic

&nbsp;

#### **Allow EWS Access for a specific list of mailboxes only**

In some configurations, {{ product_name }} can use [Exchange Impersonation](../Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/) and communicate with MS Exchange server through [pre-configured Service Accounts](../Impersonation-O365/). 

 - If EWS are not used in any other way in a customer's configuration, then only specific mail accounts which need EWS access may be enabled to access them, in particular an [Impersonating account](../Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/) set up for {{ product_name }}
  - Refer to [this Microsoft article](https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/controlling-client-application-access-to-ews-in-exchange#impersonation-and-ews-access-management) for details on enabling EWS access
  - Note that certain {{ product_name }} functions may be not supported for this configuration (e.g. the [Add-In](../Introduction/) will not be available, refer to [this article](../AddIn-vs-Sync-Functions/) for more information), [contact our CSM team](mailto:support@revenuegrid.com) for details

&nbsp;

##### Best practices configuration flow

- Choose the {{ product_name }} deployment model that suits your Org's needs
- Decide whether {{ product_name }} IP address filtering shall be configured in your Org
- Decide whether {{ product_name }} EWS traffic filtering shall be configured in your Org
- Decide which user [authentication model](../Email-Integration-Full-Deployment-Scenarios/) shall be used in your organization: whether the end users will sign in to MS Exchange or Office 365 themselves, whether [Exchange Impersonation](../Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/) and [Service accounts](../Impersonation-O365/) will be used, and whether the {{ short_name }} [Outlook Add-In](../Introduction/) will be used; depending on that EWS access may be allowed only for a [Service account](../Impersonation-O365/) authenticating a list of end users

 &nbsp;

#### Admin consent permissions for EWS

EWS connection allows to establish MS Exchange or O365 (With Exchange Online) servers access to all data types at once: Emails, Calendar, Tasks, Contacts. The permissions set is called *EWS.AccessAsUser.All*; in contrast to [MS Graph O365 access](../MS-Graph/) EWS does <u>not</u> have a technical possibility to limit access to specific data types.  

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\API_permissions.png" class="minimized">
</p></details>

&nbsp;

!!! note "Note"
    Also see [this FAQ entry](../Frequently-Asked-Questions/#28_what_administrative_permissions_admin_consent_does_revenue_inbox_have_is_it_possible_to_limit_this_app_to_specific_users_or_groups_of_users_in_our_company) for more information and [this article](../Need-Admin-Approval/) to learn how to resolve the "Need Admin Approval" error


&nbsp;

!!! tip "Tip"
    Customized data type specific access to mailboxes on O365 servers is available over MS Graph connection. See [this article](../MS-Graph/) for details

&#160;
 &#160;

