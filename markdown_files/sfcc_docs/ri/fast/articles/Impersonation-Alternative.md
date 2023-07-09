---
description: The detailed guide on Exchange Impersonation setup special scenarios for hybrid environments
---
# Impersonation Setup: Hybrid Scenarios  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*7 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

_**[the article is work-in-progress] **_

&nbsp;

&nbsp;

This guide is intended for Exchange Impersonation setup special scenarios for hybrid environments, where the typical scenarios for [Office 365](../Impersonation-O365/) or [MS Exchange](../Set-up-An-Impersonation-Service-Account/) cannot be applied.

&nbsp;

Enabling MS Exchange Impersonation for the end users consists of three stages:   

**I.** Configure a Service Account and Apply it for {{ short_name }} end users as described in this article, Method 1  

**II.** Verify the Configuration as described in this article  

**III.** Configure Exchange Impersonation in {{ product_name }} Admin panel ([described in a separate KB article](../Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/))  

&nbsp;

&nbsp;

## **Step I: Configure a Service Account and Apply it for {{ short_name }} end users** 

!!! note "Note"
    There are three methods how to set up Impersonation, Method 1 described in a [dedicated article](../Impersonation-O365/) is the recommended one, while Methods 2 and 3 in this article are only used in specific configurations

&nbsp;

&nbsp;

### Setup Method #2 (alternative): via RBAC

Requirements to configure Exchange Impersonation in your Org:

•     Administrative credentials for the server PC that is running Exchange 2013 - 2019 with the [Client Access server role](https://techcommunity.microsoft.com/t5/exchange-team-blog/exchange-2013-client-access-server-role/ba-p/596493)

•     Domain Administrator credentials, or credentials for another account type with the permission to create and assign roles and scopes

•     Remote [Exchange PowerShell](https://docs.microsoft.com/en-us/PowerShell/exchange/exchange-server/exchange-management-shell?view=exchange-ps) installed on the computer from which you will run the setup commands



&nbsp;

Microsoft Exchange Server 2010-2019 uses [Role-Based Access Control (RBAC)](https://docs.microsoft.com/en-us/exchange/permissions-exo/permissions-exo) to assign permissions to accounts. You can use the **New-ManagementRoleAssignment** Exchange Management Shell cmdlet to assign the **ApplicationImpersonation** role to users in the organization.

!!! tip "Tip"
    Also refer to [this Microsoft help](https://docs.microsoft.com/en-us/exchange/understanding-management-role-scope-filters-exchange-2013-help?redirectedfrom=MSDN) article for complete information on account Roles 

&nbsp;

When you assign the **ApplicationImpersonation** role, use the following parameters of the **New-ManagementRoleAssignment** cmdlet:

• **Name** - The friendly name of the role assignment. Each time you assign a role, an entry is made in the RBAC roles list. You can verify role assignments by using the Get-ManagementRoleAssignment cmdlet. 

• **Role** - The RBAC role to assign. When you set up Exchange Impersonation, you assign the ApplicationImpersonation role.

• **User** - The impersonating mail account. 

• **CustomRecipientScope** - The scope of users that the impersonating user can impersonate. The impersonating user will only be allowed to impersonate other users within a specified scope. If no scope is specified, the user is granted the ApplicationImpersonation role over all users in an organization. You can create custom management scopes using the New-ManagementScope cmdlet.

&nbsp;

&nbsp;

**To configure Exchange Impersonation for a [shared mailbox](https://docs.microsoft.com/en-us/exchange/collaboration/shared-mailboxes/shared-mailboxes?view=exchserver-2019) (aliases)**

**1\.**    Create a [shared mailbox](https://docs.microsoft.com/en-us/exchange/collaboration/shared-mailboxes/shared-mailboxes?view=exchserver-2019). If there is already a shared mailbox in your Exchange, skip this step

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\shared-mailbox.png" class="minimized">
</p></details> 



&nbsp;

**2\.** Open [Exchange Management Shell](https://docs.microsoft.com/en-us/PowerShell/exchange/exchange-server/open-the-exchange-management-shell?view=exchange-ps)

&nbsp;

**3\.** Run the **New-ManagementScope** [cmdlet](https://docs.microsoft.com/en-us/exchange/collaboration/shared-mailboxes/shared-mailboxes?view=exchserver-2019) to create a scope for which the impersonation role should be assigned. If the scope was set earlier, you can skip this step. The following example shows how to create a management scope for a specific group; you can create ManagementScope only via PowerShell.

*New-ManagementScope -Name:scopeName -RecipientRestrictionFilter:{Recipients Filter}*

The *RecipientRestrictionFilter* parameter of the **New-ManagementScope** [cmdlet](https://docs.microsoft.com/en-us/exchange/collaboration/shared-mailboxes/shared-mailboxes?view=exchserver-2019) defines the mailboxes in the scope. You can use properties of the **Identity** object to create the filter. 

&nbsp;

The following command is used to set a filter that defines the scope of mailbox aliases beginning with "sharedmail":

```New-ManagementScope -Name SharedScopeAlias -RecipientRestrictionFilter {email alias, e.g. 'sharedmail*'}```

&nbsp;

**4\.** Run the **New-ManagementRoleAssignment** [cmdlet](https://docs.microsoft.com/en-us/exchange/collaboration/shared-mailboxes/shared-mailboxes?view=exchserver-2019) to add the impersonating permissions for the mailboxes within the scope set at step ( **3** ). The following command is used to enable the service account to impersonate all users in this scope

*New-ManagementRoleAssignment -Name:{Impersonation Assignment Name} -Role:ApplicationImpersonation -User:{Service Account} -CustomRecipientWriteScope:{Scope Name}*

&nbsp;

*For example:*

``` New-ManagementRoleAssignment –Name "impersonation" –Role:ApplicationImpersonation –User "ImpersonatedAcc" –CustomRecipientWriteScope "SharedScopeAlias"```

&nbsp;

Alternatively, if your [{{ product_name }} deployment scenario](../Email-Integration-Full-Deployment-Scenarios/) requires that, you can assign the Impersonation service account for all user accounts. To do that:

Run the **New-ManagementRoleAssignment** [cmdlet](https://docs.microsoft.com/en-us/PowerShell/scripting/developer/cmdlet/cmdlet-overview?view=PowerShell-6) to add impersonating permissions to the specified mail account. The following command is used to configure Exchange Impersonation enabling a service account to impersonate *all* users in an Org:  

*New-ManagementRoleAssignment -Name:{impersonationAssignmentName} -Role:ApplicationImpersonation -User:{ServiceAccount}*


&nbsp;

*For example:*

 ```New-ManagementRoleAssignment -Name "impersonationrole" -Role:ApplicationImpersonation -User "ImpersonatingAcc"```

&nbsp;

&nbsp;

### **To configure the management scope (via PowerShell):**

Granting impersonation access to a limited set of Exchange users is more complex than granting access to all users in an Org. In Exchange this requires creation of a Management Scope which identifies the users that Impersonation will apply to. Management scopes bound to a group use the full distinguished name of the distribution group. 

**1\.**  
```$UserCredential = Get-Credential```  

&nbsp;

**2\.**  
```$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri https://outlook.office365.com/PowerShell-liveid/ -Credential $UserCredential -Authentication Basic -AllowRedirection```  

&nbsp;

**3\.**  
```Import-PSSession $Session```  

&nbsp;

**4\.** Read [this article]he current Management Scopes:  
  ```Get-ManagementScope | fl```

&nbsp;

**5\.** Next, we need to get the distinguished name of the group we are  going to use, for example (using an especially createds O365 accounts group):  
  ```$Group = Get-Group "ManagementScopeO365Group"```

&nbsp;

**6\.** Now get the distinguished name of the group, as we will need it for the next command  
  ```$Group.DistinguishedName```

&nbsp;
You will see the folllowing PowerShell output:  

*CN=ManagementScopeO365Group_XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX,OU=YourServer.onmicrosoft.com,OU=Microsoft Exchange Hosted Organizations,DC=NAMPR01A003,DC=prod,DC=outlook,DC=com*

&nbsp;

**7\.** Create a New Management Scope:  

```
New-ManagementScope –Name "OnePlaceMailServiceAccount"  –RecipientRestrictionFilter {MemberofGroup -eq  "your-distinguished-group-value-here"}
```


In a sample case:

```
 New-ManagementScope –Name "YourServiceAccount"  –RecipientRestrictionFilter {MemberofGroup -eq  "CN=ManagementScopeO365Group_  XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX,OU=YourServer.onmicrosoft.com,OU=Microsoft Exchange Hosted  Organizations,DC=NAMPR01A003,DC=prod,DC=outlook,DC=com"}
```

&nbsp;
**8\.** Now that we have defined a new Management Scope, we like to use by running the following command which will list out all the users that  are included in this Management Scope. This should be the users that you have added to the distribution group.  
  ```$myMS = (Get-ManagementScope | Where-Object Name -eq "YourServiceAccount")```

&nbsp;
**9\.** Enter
  ```Get-Recipient -RecipientPreviewFilter $myMS.RecipientFilter```



*Name        RecipientType*  

&nbsp;

*admin       UserMailbox*  

*CSM_Test01  UserMailbox*  

*CSM_Test02  UserMailbox* 

&nbsp;


&nbsp;
* * *

&nbsp;

&nbsp;

### Setup Method #3 (alternative): via PowerShell


This guide is based on this [Microsoft help article](https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/how-to-configure-impersonation).

There are two ways to configure a MS Exchange Impersonated account:

**I.** Using [PowerShell Exchange Management cmdlets](https://docs.microsoft.com/en-us/PowerShell/scripting/developer/cmdlet/cmdlet-overview?view=PowerShell-6):  
•	Works in Exchange 2016 - 2019 as well as Office 365  
•	Provides the maximum level of account control  

&nbsp;or

**II.** Using [Exchange Admin Center Web UI](https://docs.microsoft.com/en-us/exchange/exchange-admin-center)
•	Works in Exchange 2016 - 2019 as well as in Office 365  
•	The easier way to go; however, allows configuring Impersonation only for **all** users in an Org  

&nbsp;

&nbsp;

#### Set up Impersonation in Office 365 with [Exchange Online](https://docs.microsoft.com/en-us/exchange/exchange-online) using [Exchange PowerShell](https://docs.microsoft.com/en-us/PowerShell/exchange/exchange-server/exchange-management-shell)

**Prerequisites:**

* Administrative credentials for the Exchange server  
* Domain Administrator credentials, or other credentials with the permission to create and assign roles and scopes  
* Exchange management tools installed on the computer from which you will run the commands  
  

&nbsp;

&nbsp;

**To configure impersonation for all Exchange users in an Org:**

If you are familiar with the Windows PowerShell commands and you want  to know how to grant application impersonation rights in Office 365  using PowerShell. below steps will show how you can easily give  impersonation rights to all office 365 users of your organization with the following commands:

**1\.** Open Exchange Management Shell and click **All Programs** from the Start menu > **Microsoft Exchange Server**  

&nbsp;

**2\.** Run the **New-ManagementRoleAssignment cmdlet** to  configure the impersonation permission to the required user. The  following example will show you how to grant Application impersonation  to enable a service account to impersonate all other users in an  organization.  

```
New-ManagementRoleAssignment -name:impersonationAssignmentName -Role:ApplicationImpersonation -User:serviceAccount
```

&nbsp;

&nbsp;



To assign the application impersonation role for the specific users or groups of users, you need to run the following commands.

**1\.** **Open the Exchange Management Shell** > Choose **All Programs** from the Start menu > **Microsoft Exchange Server**.  

&nbsp;

**2\.** Run the **New-ManagementScope cmdlet** to create a  scope to which the impersonation role can be assigned. You can skip this  step if an existing scope is available. The following example shows how  to create a management scope for a specific group.  

```
New-ManagementScope -Name:scopeName -RecipientRestrictionFilter:recipientFilter
```

&nbsp;

**3\.** Run the **New-ManagementRoleAssignment cmdlet** to configure the permission to impersonate the users of the specified scope.

```
New-ManagementRoleAssignment -Name:impersonationAssignmentName  -Role:ApplicationImpersonation -User:serviceAccount  -CustomRecipientWriteScope:scopeName
```

&nbsp;
<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\cloud_migration.png" class="minimized">
</p></details>

&nbsp;

* * *

&nbsp;



## Step II: Verify the Configuration



Next, you need to test the configured Impersonating account using [Microsoft Remote Connectivity Analyzer](https://techcommunity.microsoft.com/t5/exchange-team-blog/what-8217-s-new-with-microsoft-remote-connectivity-analyzer-a/ba-p/597652) online tools:

**1\.** Open the link <https://testconnectivity.microsoft.com>  
**2\.** Select **Service Account Access (Developers)**  

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\test.png" class="minimized">
</p>


&nbsp;

**3\.** Fill in the details for connecting to the service account:

**4\.** **Target Mailbox address**: enter the service account's email address

**5\.** **Service Account user name**: enter the account's name using the *{domain}\\{user name}* or *{user}@{domain}* format

**6\.** **Service Account password** and **Confirm password** fields: enter the service account's password two times

!!! note "Note"
    Security of tested account's credentials entered is guaranteed by Microsoft

&nbsp;

**7\.** If you are using an [Exchange Web Services URL](https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/start-using-web-services-in-exchange), click on “**Specify Exchange Web Services URL**” and enter the URL, otherwise MS Remote Connectivity Analyzer will try to discover your EWS URL automatically

**8\.** In the **Test predefined folder** field, leave the default value (*“Inbox”*)

**9\.** Select **Use Exchange Impersonation** and under **Impersonated user** enter the email address of any user from the impersonated emails list

**10\.** If necessary in your configuration, select **Ignore Trust for SSL**

**11\.** Read and confirm the “**I understand ...**” section and enter the CAPTCHA to verify that you're not a robot 

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\test2.png" class="minimized">
</p></details> 


&nbsp;

**12\.** Click **Perform test** and check the test results to see if the Impersonated account works




&nbsp;

* * *

&#160;

### Step III: Configure Impersonation in {{ product_name }} Admin panel

Next, proceed to [the steps provided in this article](../Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/) to configure {{ short_name }} [Sync Engine](../Synchronization-Engine-An-Overview/) to operate via the Impersonation account.

&nbsp;
&#160;


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
      margin-top: -100px;
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
<div class="banners banner-3">
  <img src="../../assets/images/banners/banner-3.svg" style="width: 100%; height: 100%;">
  <a class="button" href="https://revenuegrid.com/sign-up/?utm_source=kb_rg&utm_medium=referral&utm_campaign=eac&utm_content=banner" target="_blank">Try {{ company_name }} for free</a>
</div>