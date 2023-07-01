---
description: Trobleshooting: learn how to resolve the "Need Admin Approval" error
---
# How to Resolve the *Need Admin Approval* Error  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*4 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

The "Need Admin Approval" error may occur when a regular user attempts to get authenticated in {{ product_name }} with one's Office 365 credentials in the OAuth window:

![](../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Admin-Approval/admin-approval1.png)

&nbsp;

!!! warning "Important"
    There is also an important server-side prerequisite to be clarified with your local Admin or [{{ short_name }} Support team](mailto:support@revenuegrid.com). To be able to authenticate access, your company's Office 365 server must have a [valid MPN ID from Microsoft](https://docs.microsoft.com/en-us/partner-center/mpn-create-a-partner-center-account). If no MPN ID is configured, {{ product_name }} App might be regarded as *unverified* and for this reason it will not be listed among access consent Apps in Admin settings. If that is the case, contact [{{ short_name }} Support team](mailto:support@revenuegrid.com) with a corresponding request







&nbsp;

### What causes the error

The error is caused by User permission settings in corporate [MS Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/); specifically, the option “*User can consent to apps accessing company data on their behalf*” is set to "*No*", along with its derivative setting for accessing the groups' data. 

These settings can be found in **All services** -> **Enterprise applications** -> **User settings** in MS Azure Active Directory.

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Admin-Approval\admin-approval2.png" class="minimized">
</p></details>

&nbsp;



&nbsp;
&nbsp;

### Problem solutions

&nbsp;

#### Method 1

##### Step 1: Grant Admin Consent for {{ product_name }}

**1\.** Log in to MS Azure AD <https://portal.azure.com> with Admin credentials  
**2\.** Go to **Enterprise Applications**  
**3\.** Select **All Applications**  
**4\.** Type "*{{ company_name }}*" in the search field to find the App and select it   

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Admin-Approval\admin-approval3.png" class="minimized">
</p></details>

&nbsp;

!!! note "Note"
    The application may be absent from the list, in case none of the users registered consent for the App previously. If  this is the case, see [Method 2](../Need-Admin-Approval/#method_2) from this article

&nbsp;

&nbsp;

##### Step 2: Grant Admin consent

After the Step 1 is complete, proceed to the following setup actions:

**1\.** Open the **Permissions** tab and click **Grant Admin consent for %CompanyName%**  
<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Admin-Approval\admin-approval4.png" class="minimized">
</p></details>
&nbsp;

**2\.** Log in with O365 Admin credentials and click **Accept** in the *Permissions requested* dialog that appears
<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Admin-Approval\admin-approval5.png">
</p></details>

&nbsp;

!!! note "Note"
    {{ product_name }} accesses and handles the end users' email and CRM data in a most secure and private manner, according to our [Privacy and Security guarantees](https://revenuegrid.com/privacy-policy/), so approving this data access is safe

&nbsp;

**3\.** Refresh the page with Permissions for the application you've just registered consent for  
**4\.** The list of consent permissions will be displayed in the *Admin Consent* tab on the *Applications* page   

<details><summary> >>> Click to see the list of permissions <<< </summary>
<p><table>
<thead>
<tr>
<th>API Name</th>
<th>Claim value</th>
<th>Permission</th>
<th>Type</th>
<th>Granted through</th>
<th>Granted by</th>
</tr>
</thead>
<tbody>
<tr>
<td>Microsoft Graph</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Microsoft Graph</td>
<td>profile</td>
<td>View users’ basic profile</td>
<td>Delegated</td>
<td>Admin consent</td>
<td>An administrator</td>
</tr>
<tr>
<td>Microsoft Graph</td>
<td>email</td>
<td>View users’ email address</td>
<td>Delegated</td>
<td>Admin consent</td>
<td>An administrator</td>
</tr>
<tr>
<td>Microsoft Graph</td>
<td>Calendars.ReadWrite</td>
<td>Have full access to user  calendars</td>
<td>Delegated</td>
<td>Admin consent</td>
<td>An administrator</td>
</tr>
<tr>
<td>Microsoft Graph</td>
<td>Mail.ReadWrite</td>
<td>Read and write access to user mail</td>
<td>Delegated</td>
<td>Admin consent</td>
<td>An administrator</td>
</tr>
<tr>
<td>Microsoft Graph</td>
<td>User.ReadEtasic.All</td>
<td>Read all users’ basic profiles</td>
<td>Delegated</td>
<td>Admin consent</td>
<td>An administrator</td>
</tr>
<tr>
<td>Microsoft Graph</td>
<td>User.Read</td>
<td>Sign in and read user profile</td>
<td>Delegated</td>
<td>Admin consent</td>
<td>An administrator</td>
</tr>
<tr>
<td>Microsoft Graph</td>
<td>MailboxSettings.ReadWrite</td>
<td>Read and write user mailbox settings</td>
<td>Delegated</td>
<td>Admin consent</td>
<td>An administrator</td>
</tr>
<tr>
<td>Microsoft Graph</td>
<td>offline access</td>
<td>Maintain  access to data you have given it access to</td>
<td>Delegated</td>
<td>Admin consent</td>
<td>An  administrator</td>
</tr>
<tr>
<td>Office 365 Exchange  Online</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Office 365  Exchange Online</td>
<td>EWS.AccessAsUser.All</td>
<td>Access mailboxes as the signed-in user via Exchange Web Services</td>
<td>Delegated</td>
<td>Admin consent</td>
<td>An administrator</td>
</tr>
</tbody>
</table>
</p></details>



&nbsp;

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Admin-Approval\admin-approval6.png" class="minimized">
</p></details>

&nbsp;

After that, individual users should open {{ product_name }}, click the **☰** (Menu) button in its upper left corner and select **Sync settings** or **Set up sync**

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Admin-Approval\set-up1.png" style="width: 45%; height: 45%;">
</p></details>

&nbsp;

The final setup action required from the end users is to grant access to their mailbox data when prompted in the O365 OAuth dialog. As soon as it is granted, they can start using [all {{ product_name }} functions](../AddIn-vs-Sync-Functions/).

&nbsp;

* * *

&nbsp;

#### Method 2

There is also another way to resolve the issue: the local Office 365 Admin can register consent for the App on the initial logon. This method requires the O365 Admin to be [provisioned as a {{ product_name }} user](../Managing-Users-via-the-Solution-s-Admin-Panel/).

Setup actions to be performed by the Admin:

**1\.** Log in to {{ product_name }} with Salesforce credentials registered for the Admin's account  
**2\.** Press on the **☰** (Menu) button in the upper left corner of the Sidebar  
**3\.** Select **Set up sync** in the menu    

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Admin-Approval\set-upalt.png">
</p></details>
&nbsp;



**4\.** Next, Log in with O365 Admin credentials in the O365 OAuth dialog that appears     



**5\.** In the following "*Permissions Requested*" dialog window: select the checkbox **Consent on behalf of your organization**  and click **Accept**

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Admin-Approval\admin-approval7.png" class="minimized">
</p></details>
&nbsp;

Authorization is successful, a "*Signed in successfully*" notification will appear. Now the consent to use the App has been granted for the whole Org and all end users in it are allowed to perform O365 data access authorization for {{ product_name }}.

&nbsp;

*An optional extra Step*

In case the O365 Admin does not intend to use the App, the corresponding user can be removed from {{ product_name }} via [{{ short_name }} Admin panel](../How-to-Log-In-to-the-Admin-Panel/). To do that:  
**1\.** Log into {{ short_company_name }} Amin UI with admin credentials  
**2\.** Click the **Gear** (Settings) icon in the upper right corner of the page opened  
**3\.** Select **Force Delete **  

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Admin-Approval\admin-approval8.png" style="width: 70%; height: 70%;">
</p></details>

&nbsp;

After that check that O365 Admin user's email address was removed from [{{ product_name }} users list](../Managing-Users-via-the-Solution-s-Admin-Panel/).

&nbsp;

* * *

&nbsp;

### Method 3

Another option is to allow the end users to register consent for Apps on their own.

!!! note "Note"
    If this method is used, the end users will be able to register consent for any third party Apps; for some enterprises such setup might contradict general Office Apps security policies

&nbsp;

**1\.** Log in to Azure AD using Admin credentials  
**2\.** Go to **Enterprise applications** -> **User settings **  
**3\.** Switch the setting “*User can consent to apps accessing company data on their behalf*” to **Yes ** 

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Admin-Approval\admin-approval9.png" class="minimized">
</p></details>

&nbsp;

Enabling of the setting “*User can consent to apps accessing company data for the groups they own*” is optional.

&nbsp;

&nbsp;

*Also see the following articles:*  

[{{ product_name }} mass deployment scenarios](../Email-Integration-Full-Deployment-Scenarios/)

[How {{ product_name }} works with EWS](../Working-With-EWS/)

[Microsoft Consent framework](https://docs.microsoft.com/en-us/azure/active-directory/develop/consent-framework)  

[Microsoft App Consent Experience](https://docs.microsoft.com/en-us/azure/active-directory/develop/application-consent-experience)  


<br>

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


