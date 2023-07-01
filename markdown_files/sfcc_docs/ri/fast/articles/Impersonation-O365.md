---
description: How to enable MS Exchange Impersonation for the end users
---
# How to Configure Impersonation to Deploy the Solution [Office 365]  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*10 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

 All configuration activities described in this article are typical actions performed for an Impersonation service account via Admin Center secured by Microsoft. On {{ product_name }} side, data processing privacy and security are guaranteed by the [applicable {{ company_name }} policies](https://revenuegrid.com/privacy-policy/)

<br>

Enabling MS Exchange Impersonation for the end users consists of three Stages:   

**Stage I.** [Configure a Service Account and Apply it for {{ short_name }} End Users](../Impersonation-O365/#stage_i_configure_a_service_account_and_apply_it_for_rges_end_users)

**Stage II.** [Verify the Configuration](../Impersonation-O365/#stage_ii_verify_the_configuration)

**Stage III.** Configure Exchange Impersonation in {{ product_name }} Admin panel [[described in a separate KB article](../Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/)]   
&nbsp;


!!! tip "Tip"
    Refer to [this article](../Set-up-An-Impersonation-Service-Account/) to learn how to set up Impersonation in case your company uses an MS Exchange On Premise mail server or to [this article](../Impersonation-Alternative/) for [Hybrid mail server deployment options](https://docs.microsoft.com/en-us/exchange/exchange-hybrid)
&nbsp;


!!! tip "Also see the following articles to learn more about MS Exchange Impersonation:"
    <a href="https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange">MS Exchange Impersonation overview</a><br><br>
    <a href="../Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/">How Impersonation is used for {{ product_name }} deployment</a>
&nbsp;

&nbsp;
<hr>
&nbsp;

## **Stage I: Configure a Service Account and Apply it for {{ short_name }} End Users**

&nbsp;

MS Exchange Impersonation is compatible with Office 365 [with Exchange Online](https://docs.microsoft.com/en-us/exchange/exchange-online). In order to set up Application Impersonation via [Admin Center](https://docs.microsoft.com/en-us/exchange/exchange-admin-center), perform the steps below.  

&nbsp;

### Setup via Admin Center
&nbsp;

#### 1. Create a Service Account

First, you need to create a Service email account. It must be a dedicated mailbox used **only** as an Impersonating service account for {{ product_name }}, it should have no other functions. The Impersonating service account requires a [dedicated MS Exchange / Office 365 mailbox license](https://docs.microsoft.com/en-us/microsoft-365/admin/manage/assign-licenses-to-users?view=o365-worldwide), a Basic plan; it does **not** require any extra {{ product_name }} license.  

Register the Service Account with the name *MasterImpersonation*, so later, it's easy to find for testing or troubleshooting purposes.  

<br><br>

The detailed mail account creation steps (also described in [this Microsoft article](https://docs.microsoft.com/en-us/exchange/recipients/create-user-mailboxes?view=exchserver-2019)):

**1\.1.** Log in to Admin Center at <https://admin.exchange.microsoft.com/> with Admin credentials  

<br>

<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\extra-steps\create-mailbox\active-users.png" style="width: 50%; float: right;margin-left:2%;" class="minimized">
**1\.2.** Open **Users** > **Active users** in the navigation pane on the left, then click **Add a user**  

<br><br><br>

!!! tip "Tip"
    If you don't see the **Users** section in navigation pane on the left, click on the **Show all** option at the end of the list


&nbsp;

**1\.3.** Set up basics for the Service account: 

<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\extra-steps\create-mailbox\create-user.png" style="width: 50%; float: right;margin-left:2%;" class="minimized">  

- Set any **First name** and **Last name**  

- Set the **Display name**: *MasterImpersonation*  

- Set the **Username**: *MasterImpersonation*  

- (*Optional*) select **Automatically create a password** if you want an auto-generated password  

- (*Optional*) select **Send password in email upon completion** and enter a corporate email address you have access to in the field below to receive the auto-generated password

<br><br>

<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\extra-steps\create-mailbox\assign-license.png" style="width: 50%; float: right;margin-left:2%;" class="minimized">
**1\.4.** Select your **Location** and assign an O365 account license to the Service account

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>


<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\extra-steps\create-mailbox\optional-settings.png" style="width: 50%; float: right;margin-left:2%;" class="minimized">
**1\.5.** On the next *Optional settings* screen, leave the default User **Role** and then expand **Profile info** and specify some information to easily identify the account in the future, e.g. *{{ short_company_name }} Master impersonation account*


<br><br><br><br><br><br><br><br>

**1\.6.** Review Service account data you entered and click **Finish adding**

**1\.7.** Click **Close** in the final confirmation window

<br>
The new Service account will shortly become available for further configuration steps.

<br><br>


#### 2\. Create a Group that Includes All {{ short_name }} End Users' accounts

Depending on your Org's configuration, you may use 

**A)** a [Distribution group](https://docs.microsoft.com/en-us/exchange/recipients-in-exchange-online/manage-distribution-groups/manage-distribution-groups) or 

**B)** a [Mail-enabled security group list](https://docs.microsoft.com/en-us/exchange/recipients-in-exchange-online/manage-mail-enabled-security-groups).


<br><br>

##### A. To create a Distribution group

**2\.A.1.** Log in to your Org's [Admin Center](https://docs.microsoft.com/en-us/exchange/exchange-admin-center) with admin credentials. This method is for Office 365 with [Exchange Online](https://docs.microsoft.com/en-us/exchange/exchange-online)

<br>

<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\extra-steps\create-group\add-group.png" style="width: 70%; float: right;margin-left:2%;" class="minimized">
**2\.A.2.** Select **Teams & Groups** > **Active teams & groups** in the navigation pane on the left and then click **Add a group** 

<br><br><br><br>

<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\extra-steps\create-group\distribution.png" style="width: 50%; float: right;margin-left:2%;" class="minimized">
**2\.A.3.** Select **Distribution** under *Choose a group type* and click **Next**


<br><br><br><br><br><br><br><br><br><br>

<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\extra-steps\create-group\name.png" style="width: 50%; float: right;margin-left:2%;" class="minimized">
**2\.A.4.** Set the group's **Name** as *RGDG*, so it's easy to find later, and optionally add a Description

<br><br><br><br><br><br><br><br><br><br>

<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\extra-steps\create-group\owners.png" style="width: 50%; float: right;margin-left:2%;" class="minimized">
**2\.A.5.** On the Assign owners page, click **+ Assign owners** to set the Service account *MasterImpersonation* that you created earlier as the group's Owner. 

When done, click **Next**

<br><br><br><br><br><br><br><br>

<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\extra-steps\create-group\members.png" style="width: 50%; float: right;margin-left:2%;" class="minimized">
**2\.A.6.** On the next window, click **+ Add members**. Add **all** {{ short_name }} end users to the distribution group. 

When done, click **Next**

<br><br><br><br><br><br><br><br>

<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\extra-steps\create-group\email.png" style="width: 50%; float: right;margin-left:2%;" class="minimized">
**2\.A.7.** Specify the group's settings: set its **Email address** and click **Next**

<br><br><br><br><br><br><br><br>


**2\.A.8.** Review the group's configuration and click **Create group**


**2\.A.9.** **Close** the dialog


&nbsp;

If you later need to manage owners or members of the distribution group:

- In **Exchange Admin Center**, open **Recipients** > **Groups** in the navigation pane on the left

- Click the tab **Distribution list** and select the group **RGDG** in the list, then open the tab **Members** and depending on your needs, click **View all and manage owners** or **View all and manage members**, make the necessary changes and click **Save changes**

<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\extra-steps\create-group\rgdg.png" style="width: 100%" class="minimized">

&nbsp;


!!! tip "Related articles:"
    Adding users to a distribution group is also described in <a href="https://docs.microsoft.com/en-us/microsoft-365/admin/email/add-user-or-contact-to-distribution-list?view=o365-worldwide">this Microsoft article</a>

<br> 
<hr>
<br> 

**Alternatively, if you prefer using a Mail-enabled security group instead**

&nbsp;

##### B. To create a Mail-enabled security group

!!! tip "Tip"
    The mail-enabled security group of created this way can also be used for {{ product_name }} mass deployment. Adding new users to this group later results in their automatic inclusion in Impersonation scope and {{ short_name }} Add-In installation for their mail accounts. See [this article](../Mass-Deployment-of-the-Add-In-Office-365/) for details

&nbsp;

**2\.B.1.** Log in to your Org's [Admin Center](https://docs.microsoft.com/en-us/exchange/exchange-admin-center) with admin credentials. This method is for Office 365 with [Exchange Online](https://docs.microsoft.com/en-us/exchange/exchange-online) feature   

&nbsp;

<br>

<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\extra-steps\create-group\add-group.png" style="width: 70%; float: right;margin-left:2%;" class="minimized">
**2\.B.2.** Select **Teams & Groups** > **Active teams & groups** in the navigation pane on the left and then click **Add a group** 

<br><br><br><br>

<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\extra-steps\create-group\mail-security.png" style="width: 50%; float: right;margin-left:2%;" class="minimized">
**2\.B.3.** Select **Mail-enabled security** under *Choose a group type* and click **Next**

<br><br><br><br>


<br><br><br><br><br><br><br><br>

<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\extra-steps\create-group\name-sg.png" style="width: 50%; float: right;margin-left:2%;" class="minimized">
**2\.B.4.** Set the group's **Name** as *RGSG*, so it's easy to find later, and optionally add a Description

<br><br><br><br><br><br><br><br><br><br>

<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\extra-steps\create-group\owners.png" style="width: 50%; float: right;margin-left:2%;" class="minimized">
**2\.B.5.** On the Assign owners page, click **+ Assign owners** to set the Service account *MasterImpersonation* that you created earlier as the group's Owner. 

When done, click **Next**

<br><br><br><br><br><br><br><br>

<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\extra-steps\create-group\members.png" style="width: 50%; float: right;margin-left:2%;" class="minimized">
**2\.B.6.** In the next window, click **+ Add members**. Add **all** {{ short_name }} end users to the group. 

When done, click **Next**

<br><br><br><br><br><br><br><br>

<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\extra-steps\create-group\security-email.png" style="width: 50%; float: right;margin-left:2%;" class="minimized">
**2\.B.7.** Specify the group's settings: set its **Email address** and then ensure that the **Communication** checkbox is unselected and the **Approval** checkbox is selected to ensure maximum security

<br><br><br><br><br><br><br><br>


**2\.B.8.** Review the group's configuration and click **Create group**


**2\.B.9.** **Close** the dialog



&nbsp;

If you later need to manage owners or members of the mail-enabled security group:

- In **Exchange Admin Center**, open **Recipients** > **Groups** in the navigation pane on the left

- Click the tab **Mail-enabled security group** and select the group **RGSG** in the list, then open the tab **Members** and depending on your needs, click **View all and manage owners** or **View all and manage members**, make the necessary changes and click **Save changes**

<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\extra-steps\create-group\rgsg.png" style="width: 90%" class="minimized">



<br><br><br>


#### 3\. Set the Users Group and Apply Impersonation

&nbsp;

**3\.1.** Run Windows PowerShell as Admin and [connect to Exchange Online](https://docs.microsoft.com/en-us/powershell/exchange/connect-to-exchange-online-powershell?view=exchange-ps)  

<br>

**3.1.1** In PowerShell, load the *EXO V2* module by running the following command:  

```
Import-Module ExchangeOnlineManagement 
```

!!! note "Note"
    If the required *ExchangeOnlineManagement* module does not exist then please [follow this link](https://docs.microsoft.com/en-us/powershell/exchange/exchange-online-powershell-v2?view=exchange-ps#install-and-maintain-the-exo-v2-module) to install the EXO V2 module first

&nbsp;
&nbsp;


**3.1.2.** The command that you need to run next uses the below syntax. The parameters in square brackets are optional, they depend on your server's configuration.
<details><summary> >>> Click to see the parameters' description <<< </summary>
<p>
<em>&lt;UPN&gt;</em> is your account in user principal name format (for example, <code>navin@contoso.com</code>).</li>
&nbsp; &nbsp; &nbsp; &nbsp; <li>When you use the <em>ExchangeEnvironmentName</em> parameter, you don't need use the <em>ConnectionUri</em> or <em>AzureADAuthorizationEndPointUrl</em> parameters. For more information, see the parameter descriptions in <a href="https://docs.microsoft.com/en-us/powershell/module/exchange/connect-exchangeonline">Connect-ExchangeOnline</a>.</li>
&nbsp; &nbsp; &nbsp; &nbsp; <li>The <em>DelegatedOrganization</em> parameter specifies the customer organization that you want to manage as an authorized Microsoft Partner. For more information, see <a href="https://docs.microsoft.com/en-us/office365/servicedescriptions/office-365-platform-service-description/partners">Partners</a>.</li>
&nbsp; &nbsp; &nbsp; &nbsp; <li>If you're behind a proxy server, run this command first: <code>$ProxyOptions = New-PSSessionOption -ProxyAccessType &lt;Value&gt;</code>, where &lt;Value&gt; is <code>IEConfig</code>, <code>WinHttpConfig</code>, or <code>AutoDetect</code>. Then, use the <em>PSSessionOption</em> parameter with the value <code>$ProxyOptions</code>. For more information, see <a href="https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-pssessionoption">New-PSSessionOption</a>.</li>
&nbsp; &nbsp; &nbsp; &nbsp;<li>The progress bar is now shown by default, so <code>-ShowProgress $true</code> is no longer required. To hide the progress bar, use this exact syntax: <code>-ShowProgress:$false</code>.</li>

</p></details>


```
Connect-ExchangeOnline -UserPrincipalName <UPN> -ShowProgress $true [-ExchangeEnvironmentName <Value>] [-DelegatedOrganization <String>] [-PSSessionOption $ProxyOptions]
```

&nbsp;
&nbsp;


**3.1.3.** This sample cmdlet connects to Exchange Online PowerShell in a Microsoft 365 / Microsoft 365 GCC organization:

```
Connect-ExchangeOnline -UserPrincipalName navin@contoso.com -ShowProgress $true
```

&nbsp;

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\connect.png" class="minimized">
</p></details>


&nbsp;
&nbsp;


**3\.2.** The next step depends on whether you configured 

**A)** [Distribution group](https://docs.microsoft.com/en-us/exchange/recipients-in-exchange-online/manage-distribution-groups/manage-distribution-groups) or 

**B)** a [Mail-enabled security group list](https://docs.microsoft.com/en-us/exchange/recipients-in-exchange-online/manage-mail-enabled-security-groups) on **Step 2**  

&nbsp;
&nbsp;


##### For case **A** (*Distribution group*)


* Run PowerShell as Admin and enter the following line in PowerShell:

```
$groupidentity = $(Get-DistributionGroup RGDG).DistinguishedName
```

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\scope.png" class="minimized">
</p>
&nbsp;
&nbsp;

* Next, create a [Scope of group members](https://docs.microsoft.com/en-us/exchange/understanding-management-role-scopes-exchange-2013-help) with the name *RGusersScope* by entering the following line:
```
New-ManagementScope -Name:"RGusersScope" -RecipientRestrictionFilter "MemberOfGroup -eq '$groupidentity'"
```
&nbsp;



&nbsp;

##### For case **B** (*Mail-enabled security group*)

* Run PowerShell as Admin and enter the following line in PowerShell:

```
$groupidentity = $(Get-Group RGSG).DistinguishedName
```

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\sg\sg.png" class="minimized">
</p>
&nbsp;
&nbsp;

* Next, create a [Scope of group members](https://docs.microsoft.com/en-us/exchange/understanding-management-role-scopes-exchange-2013-help) with the name *RGusersScope* by entering the following line:

```
New-ManagementScope -Name:"RGusersScope" -RecipientRestrictionFilter "MemberOfGroup -eq '$groupidentity'"
```



<br><br><br>


**3\.3.** After performing the case-specific step **A)** or **B)** above, return to [Exchange Admin Center](https://docs.microsoft.com/en-us/exchange/exchange-admin-center) and open the **Roles** tab and then **Admin Roles** in the navigation pane on the left, then click the **Add role group** button at the top of the right-hand pane

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\role-group.png" class="minimized">
</p>

<br><br><br>


**3\.4.** In the *Add role group* dialog that appears, set the role group’s **Name** as *RGappImpersonation*. After that, in the **Write scope** field select the *RGusersScope* group that you configured on Step **3.2.**

!!! note "Note"
    If you set the *Default* Write scope, Impersonation will be applied for all user accounts in the Org

&nbsp;
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\Name.png" style="width:90%;" class="minimized">
</p>

<br><br><br>


**3\.5.** Next, select **ApplicationImpersonation** under *Roles*:

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\Permission.png" style="width:90%;" class="minimized">
</p>

<br><br><br>

**3\.6.** Set the *MasterImpersonation* Service account created on earlier steps in the field **Members** under *Assign admins* to enable the account to work with mailboxes belonging to the group:

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Impersonation-O365\members.png" style="width:90%;" class="minimized">
</p>

&nbsp;

**3\.7.** Finally, review the configuration and click the **Add role group** button at the bottom of the dialog to finish



&nbsp;

!!! note "Note"
    The above described main method is the recommended one. In case it does not work for any reason in your configuration, refer to the alternative methods provided in [a separate article](../Impersonation-Alternative/)

&nbsp;

&nbsp;

* * *


&nbsp;

## Stage II: Verify the Configuration

&nbsp;

Next, you need to test the configured Impersonating account using the official tool [Microsoft Remote Connectivity Analyzer](https://techcommunity.microsoft.com/t5/exchange-team-blog/what-8217-s-new-with-microsoft-remote-connectivity-analyzer-a/ba-p/597652):

**1\.** Open Microsoft Remote Connectivity Analyzer using the link <https://testconnectivity.microsoft.com>  
&nbsp;
**2\.** Open the tab **Office 365** in the navigation pane and select **Service Account Access** in the pane on the right 

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\testo.png" class="minimized">
</p> 


&nbsp;

**3\.** Fill in the details to connect to an end user account to test connectivity:

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\test2o.png" class="minimized">
</p></details> 
&nbsp;

**4\.** **Target Mailbox email address**: enter email address of any {{ short_name }} user managed by the configured Impersonation account 

**5\.** Leave the default Authentication type: *Modern Authentication (OAuth)*

**6\.** Click **Sign In** and sign in to the user account with its password via [standard O365 OAuth dialog](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-v2-protocols)

!!! note "Note"
    Security of tested account's credentials entered in the dialog is guaranteed by Microsoft

&nbsp;

**7\.** If your configuration has a custom [Exchange Web Services URL](https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/start-using-web-services-in-exchange), select **Specify Exchange Web Services URL** and enter your corporate EWS URL.
Or select the box **Use Autodiscover to detect server settings** to let the tool auto-determine the URL

**8\.** Next, select **Test predefined folder** and leave the default value *Inbox* in the box below

**9\.** Select **Use Exchange Impersonation** and under **Impersonated user** enter the same email address of a {{ short_name }} user managed by the configured Impersonation account    

**10\.** In the field **Impersonated user identified**, leave the default value *SmtpAddress*

**11\.** If that is required in your configuration, select **Ignore Trust for SSL**

**12\.** Leave the default **Service Selection**: *Office 365 (Default)*, select **Ignore Trust for SSL**

**13\.** Read and confirm the “**I understand and I must ...**” section; enter the CAPTCHA and click **Verify** to prove that you are not a robot

**14\.** Finally, click **Perform test** at the bottom of the dialog and check the test results to see if the configured Impersonated account works

&nbsp;

&nbsp;

* * *


&nbsp;

## Stage III: Configure Impersonation in {{ product_name }} Admin panel

&nbsp;

Next, proceed to [the steps provided in this article](../Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/) to configure the [Sync Engine](../Synchronization-Engine-An-Overview/) to operate via the Impersonation account.

&nbsp;

Also see the article [{{ product_name }} mass deployment for Office 365 users](../Mass-Deployment-of-the-Add-In-Office-365/).

&nbsp;

&nbsp;


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