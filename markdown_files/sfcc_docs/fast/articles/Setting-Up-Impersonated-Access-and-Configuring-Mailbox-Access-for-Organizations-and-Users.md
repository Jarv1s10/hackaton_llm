---
description: Learn how to set up sync via Impersonation & configure user mailboxes
---
# How to Set Up Sync via Impersonation & Configure User Mailboxes  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*4 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

[MS Exchange / Office 365 Impersonation](http://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange) is used in scenarios when a single admin service account is used to access and manage many end user accounts, to view or adjust their settings or perform various actions on these accounts' behalf.
In {{ short_name }} setup context, Impersonation allows to automatically [activate {{ company_name }} synchronization](../Authorizing-Sync-Engine-to-Work-with-Your-Data/) for all relevant email accounts in an [Organization](../Managing-Organizations-via-the-Admin-Panel/) in bulk, via an [impersonating MS Exchange service account](../Impersonation-O365/).

!!! note "Note"
    The Impersonation Service email account requires a dedicated MS Exchange / Office 365 mailbox license and does **not** require an additional {{ product_name }} license

&nbsp;

While Impersonation requires performing a sequence of configuration steps on Exchange server side by the local Admin (documented in detail in [this article](../Impersonation-O365/)), it has the following benefits:

- There is no need for every {{ short_name }} user to enter one's Exchange/Office 365 mailbox credentials on {{ product_name }} setup. Instead, multiple users' credentials are set up once, by the local Admin  
- The end users don't need to go to {{ product_name }} settings and [update the access password](../Renewing-Exchange-and-Salesforce-Account-Credentials/) after mailbox password change  
- Mailbox connectivity is established and monitored entirely by the Admin, removing any associated actions from the end users

!!! tip "Tip"
    To check whether an Impersonation service account was configured correctly, open [this Microsoft connectivity tests page](https://testconnectivity.microsoft.com/) and run the test *Service Account Access (Developers)*, as described in [this article](../Impersonation-O365/#step_ii_verify_the_configuration)

&nbsp;

!!! note "Note"
    If an impersonating Service account is used for [{{ company_name }} Sync users authorization](../Email-Integration-Full-Deployment-Scenarios/), the Service account must have a mailbox and a license assigned to it. If the Service Account does not have a mailbox or license assigned, [rooms and other resources](../Rooms-List/) will not be retrieved in {{ product_name }} via EWS 

&nbsp;

&nbsp;

#### Setting up {{ short_name }} Sync for multiple users via Exchange/Office 365 Impersonated Access

**1\.** Open MS Exchange or Office 365 Admin center. Refer to the following articles to learn how to do that:

*   [Office 365](https://support.office.com/en-us/article/about-the-office-365-admin-center-758befc4-0888-4009-9f14-0d147402fd23)
*   [Exchange 2016, 2019](https://technet.microsoft.com/en-us/library/jj150562(v=exchg.160).aspx)

&nbsp;

**2\.** Create an MS Exchange/Office 356 service account and assign it [Impersonation permissions](https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange) using the following step-by-step guides:

* [MS Exchange](../Set-up-An-Impersonation-Service-Account/) 
* [Office 365](../Impersonation-O365/#create_a_service_account_in_office_365)


&nbsp;

**3\.** Set up an Organization containing all relevant user mail accounts:

&nbsp;&nbsp;&nbsp;&nbsp;**3.1\.** [Log in to {{ product_name }} Admin panel](../How-to-Log-In-to-the-Admin-Panel/) (the Admin credentials are provided by [{{ company_name }} support team](mailto:support@invisble.io))

&nbsp;&nbsp;&nbsp;&nbsp;**3.2\.** [Create an Organization in {{ short_name }} Admin panel](../Managing-Organizations-via-the-Admin-Panel/#creating_organizations) [optional; for customers not fully provisioned by {{ company_name }} CSM team]

&nbsp;&nbsp;&nbsp;&nbsp;**3.3\.** [Add all relevant user accounts to the created Organization](../Managing-Organizations-via-the-Admin-Panel/#users_the_subtab_displays_the_list_of_users_which_belong_to_the_organization) [optional; for customers not fully provisioned by {{ company_name }} CSM team]

&nbsp;

**4.** Proceed to the instructions below to bulk-activate [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/) for all relevant email accounts

&nbsp;

&nbsp;

#### Configuring {{ short_name }} Sync Access to User Mailboxes

To bulk-activate or renew {{ short_name }} Sync access for an [Organization](../Managing-Organizations-via-the-Admin-Panel/) consisting of email accounts entitled to use {{ product_name }} for MS Exchange Impersonated access:  

&nbsp;&nbsp;&nbsp;&nbsp;**4.1\.** Go to the [Organizations tab](../Managing-Organizations-via-the-Admin-Panel/) and select the needed Organization, open the **Email Configuration** subtab  

&nbsp;&nbsp;&nbsp;&nbsp;**4.2\.** In the [**Mailbox Access Type** picklist](../Managing-Organizations-via-the-Admin-Panel/#configuring_connection_type_for_an_organization), select **Microsoft Exchange Impersonation** 

&nbsp;&nbsp;&nbsp;&nbsp;**4.3\.** In the *Account Logon* field, enter the [Impersonating account's name (email address)](../Impersonation-O365/)  

&nbsp;&nbsp;&nbsp;&nbsp;**4.4\.** In the *Password* field, enter the [Impersonating account's password](../Impersonation-O365/)  

&nbsp;

**5\.** In the *Exchange Web Services (EWS) URL* field, enter the [EWS URL](https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/start-using-web-services-in-exchange) used in your MS Exchange or click the Magic Wand icon on the right to initiate generating a standard EWS URL, if your Org doesn't use custom ones

&nbsp;

**6\.** Click **Check Users Exchange Impersonated Access** to make sure the procedure was successful, then click **Save**

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5b1e8b030428632c466ac0ab.png" class="minimized">
</p></details>

&nbsp;
&nbsp;

* * *

&nbsp;

#### Service account authorization via Office 365 OAuth

!!! tip "Tip"
     Now this method is the only way to authorize an Exchange Impersonation service account for Office 365 mailboxes, since the old Impersonated access authorization method with login and password creds entry was removed by Microsoft in 2021 

&nbsp;

[MS Office 365 OAuth](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow) authentication method is used to authorize the Service account to work with {{ short_name }} end users' O365 mail data.

To do that:  

&nbsp;&nbsp;&nbsp;&nbsp;**1\.** Go to the [Organizations tab](../Managing-Organizations-via-the-Admin-Panel/) and select the needed Org configured for a group of {{ short_name }} end users. Next, open the subtab **Email Configuration** for the Org  

&nbsp;&nbsp;&nbsp;&nbsp;**2\.** In the [**Mailbox Access Type** picklist](../Managing-Organizations-via-the-Admin-Panel/#configuring_connection_type_for_an_organization), select "*Microsoft 365 OAuth Logon (EWS API) - Impersonated logon*", then click the button **Microsoft 365 OAuth (EWS API)** underneath   

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\o365-oauth.png" class="minimized">
</p></details>

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;**3\.** A standard Office 365 OAuth 2.0 dialog will be opened in a new browser window. In the dialog, enter the [Impersonating account's](../Impersonation-O365/) login credentials and click **Sign In**  

Now {{ product_name }} is authorized to work with mailbox data of all users configured in the Impersonating Service account.



&#160;
 &#160;

