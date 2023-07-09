---
description: Detailed guidance on configuring Impersonation to deploy RG Email Sidebar [MS Exchange On-Premises]
---
# How to Configure Impersonation to Deploy the Solution [MS Exchange On-Premises]  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*9 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! tip "Tip"
    Refer to [this article](../Impersonation-O365/) to learn how to set up Impersonation in case your company uses an Office 365 mail server or to [this article](../Impersonation-Alternative/) for [Hybrid mail servers](https://docs.microsoft.com/en-us/exchange/exchange-hybrid)

&nbsp;

!!! note "Note"
    All configuration activities described in this article are typical actions performed for an Impersonation service account via Exchange Admin portal secured by Microsoft. On {{ product_name }} side, data processing privacy and security are guaranteed by the [applicable {{ company_name }} policies](https://revenuegrid.com/privacy-policy/)

&nbsp;

Also see the following articles to learn more about MS Exchange Impersonation:

- [MS Exchange Impersonation overview](https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange)
- [How Impersonation is used for {{ product_name }} deployment](../Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/)





&nbsp;

Enabling MS Exchange Impersonation in {{ product_name }} consists of three Stages:  

**I.** Create a Service Account and Apply it for {{ short_name }} end users [[described in this section](../Set-up-An-Impersonation-Service-Account/#stage_i_configure_a_service_account_and_apply_it_for_rges_end_users)]   

&nbsp;

**II.** Verify the Configuration [[described in this section](../Set-up-An-Impersonation-Service-Account/#stage_ii_verify_the_configuration)]   

&nbsp;

**III.** Configure Exchange Impersonation in {{ product_name }}'s Admin panel [[described in a dedicated KB article](../Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/)]  

&nbsp;

<iframe src="https://player.vimeo.com/video/447501654" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>

&nbsp;





## Stage I: Configure a Service Account and Apply it for {{ short_name }} End Users

In order to set up an Exchange Impersonation account via [Exchange Admin Center](https://docs.microsoft.com/en-us/exchange/exchange-admin-center), follow the steps below.  

&nbsp;

### Setup via Exchange Admin Center [main method]

&nbsp;

In order to set up an Exchange Impersonation account via [Exchange Admin Center](https://docs.microsoft.com/en-us/exchange/exchange-admin-center), follow the steps below.


&nbsp;

#### 1. Create a Service Account

&nbsp;

First, you need to create a Service email account. It must to be a dedicated mailbox used <u>only</u> as an Impersonating service account for {{ product_name }}, it should have no other functions. The Impersonating service account requires a [dedicated MS Exchange / Office 365 mailbox license](https://docs.microsoft.com/en-us/microsoft-365/admin/manage/assign-licenses-to-users?view=o365-worldwide) [E1, E3, E5, Business Basic or Business Standard](https://docs.microsoft.com/en-us/office365/servicedescriptions/exchange-online-service-description/exchange-online-service-description) and does **not** require an extra {{ product_name }} license.  
Please register the Service Account with the name *MasterImpersonation* to make it easy to find later for testing or troubleshooting.  

Follow the steps described in [this Microsoft article](https://docs.microsoft.com/en-us/exchange/recipients/create-user-mailboxes?view=exchserver-2019#create-user-mailboxes) to create a Service mail account.

&nbsp;

&nbsp;

#### 2\. Create a Group that Includes All {{ short_name }} End Users' accounts

Depending on your Org's configuration, you may use **A)** a [Distribution group](https://learn.microsoft.com/en-us/exchange/recipients/distribution-groups?view=exchserver-2019) or **B)** a [Security group list](https://learn.microsoft.com/en-us/exchange/recipients/mail-enabled-security-groups?view=exchserver-2019).

&nbsp;



##### A. To create a Distribution group

**2\.A.1.** Log in to your corporate [Exchange Admin Center](https://docs.microsoft.com/en-us/exchange/exchange-admin-center) with Admin credentials and select the tab **Exchange** in the upper left corner

Exchange Admin portal link: <https://admin.microsoft.com/Adminportal/Home> 

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\selection.png">
</p></details> 


&nbsp;

**2\.A.2.** Select **recipients** in the navigation pane on the left and then click **groups** in the right-hand pane

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex1a.png" class="minimized">
</p></details>


&nbsp;



**2\.A.3.** Create a group: click on the **+** (Add) icon and select **Distribution group**

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex2a.png" class="minimized">
</p></details>


&nbsp;



**2\.A.4.** Enter a **Display name** *RIapplicationGroup* and an **Alias** *RIAG* to easily identify the group later

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex3a.png" class="minimized">
</p></details>


&nbsp;

**2\.A.5.** Next, assign the Impersonation account as a group owner:

- Click the **+** (Add) icon under *Owners:*

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex3extra.png" class="minimized">
</p></details>
&nbsp;
- In the dialog that appears, use the **🔍** icon to find the *MasterImpersonation* account you created earlier and then **add - >** it to group owners


&nbsp;

**2\.A.6.** After that, add {{ product_name }} user accounts to the group:

- Scroll down and make sure that the checkbox *Add group owners as members* is selected  

- Click the **+** (Add) icon under *Members:*

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex4a.png" class="minimized">
</p></details>


- In the dialog that appears, use the **🔍** icon to find {{ product_name }} end users and then **add - >** them to the group members list

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex5a.png"><br><br><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex6a.png">
</p></details>


&nbsp;

- Add all en users to the group in the same manner and click **OK**

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex7a.png">
</p></details>


&nbsp;

**2\.A.7.** Set the following recommended group membership rules:

- *Approval to join the group.* **Closed: Members can be added only by the group owners.**   
- *Choose whether the group is open to leave.* **Closed: Members can be removed only by the group owners.**  

- After that, Apply the changes in the Distribution group by clicking **Save** at the bottom  

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex8a.png" class="minimized">
</p></details>
&nbsp;

&nbsp;
&nbsp;

**Alternatively, if you prefer using a Security group instead**

&nbsp;

##### B. To create a Security group

**2\.B.1.** Log in to your corporate [Exchange Admin Center](https://docs.microsoft.com/en-us/exchange/exchange-admin-center) with Admin credentials and select the tab **Exchange** in the upper left corner

Exchange Admin portal link: <https://admin.microsoft.com/Adminportal/Home> 

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\selection.png">
</p></details> 


&nbsp;

**2\.B.2.** Select **recipients** in the navigation pane on the left and then click **groups** in the right-hand pane

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex1a.png" class="minimized">
</p></details>


&nbsp;



**2\.B.3.** Create a group: click on the **+** (Add) icon and select **Security group**

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex2asg.png" class="minimized">
</p></details>

&nbsp;


**2\.B.4.** Enter a **Display name** *RIapplicationGroup* and an **Alias** *RISG* to easily identify the group later

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex3asg.png" class="minimized">
</p></details>


&nbsp;

**2\.B.5.** Next, assign the Impersonation account as a group owner:

- Click the **+** (Add) icon under *Owners:*

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex3extrasg.png" class="minimized">
</p></details>
&nbsp;
- In the dialog that appears, use the **🔍** icon to find the *MasterImpersonation* account you created earlier and then **add - >** it to group owners


&nbsp;


**2\.B.6.** After that, add {{ product_name }} user accounts to the group:

- Scroll down and make sure that the checkbox *Add group owners as members* is selected  

 <details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex4asg.png" class="minimized">
</p></details>

&nbsp;

- Click the **+** (Add) icon under *Members:*

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex4asg.png" class="minimized">
</p></details>
&nbsp;

- In the dialog that appears, use the **🔍** icon to find {{ product_name }} end users and then **add - >** them to the group members list

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex5a.png"><br><br><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex6a.png">
</p></details>


&nbsp;
- Add all end users to the group in the same manner and click **OK**

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex7a.png">
</p></details>

&nbsp;

**2\.B.7.** Enable the recommended group joining policy setting *Owner approval is required* by selecting a corresponding checkbox  

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\4sgrule.png" class="minimized">
</p></details>

&nbsp;

**2\.B.8.** Apply the changes in the Security group by clicking **Save** at the bottom  

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex8asg.png" class="minimized">
</p></details>
&nbsp;


&nbsp;





#### 3\. Set the Users Group and Apply Impersonation  

&nbsp;

##### If you configured a Distribution group (see point **2.A.** above)

**3\.A.1.** [Run Exchange Management Shell](https://docs.microsoft.com/en-us/PowerShell/exchange/exchange-server/open-the-exchange-management-shell?view=exchange-ps) as Administrator

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex21.png" class="minimized">
</p></details>

&nbsp;

**3\.A.2.** Enter the following lines in Exchange Management Shell console one by one:

```
$groupidentity = $(Get-DistributionGroup RIAG).Identity.DistinguishedName  
```
&nbsp;
```
New-ManagementScope -Name:"RIusersScope" -RecipientRestrictionFilter "MemberOfGroup -eq '$groupidentity'"
```
&nbsp;


<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex22.png" class="minimized">
</p></details>

&nbsp;

**3\.A.3.** Next, return to [Exchange Admin Center](https://docs.microsoft.com/en-us/exchange/exchange-admin-center) and open the **permissions** tab in the navigation pane on the left, then click the **+** (Add) icon in the header of the right pane

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex23.png" class="minimized">
</p></details>

&nbsp;



**3\.A.4.** In the *New role group* dialog that appears, enter a role group's **Name**, then select the *RIusersScope* group that you configured on Step **3.2**. in the **Write scope** field

!!! tip "Tip"
    If you leave the *Default* Write scope, Impersonation will be applied for all users in the Org.

&nbsp;

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex24.png">
</p></details>

&nbsp;



**3\.A.5.** Next, click the **+** (Add) button under *Roles:*

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex25.png">
</p></details>


&nbsp;

**3\.A.6.** In the *Select a Role* dialog that appears, select **ApplicationImpersonation** in the pane on the left, then click the **add - >** button underneath and click **OK** at the bottom

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex26.png">
</p></details>


&nbsp;



**3\.A.7.** Now you should enable the impersonation account to perform its role. To do that:

- Next, click the **+** (Add) button under *Members:*

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex29.png">
</p></details>
&nbsp;

- In the *Select Members* dialog that appears: click the **🔍** (Search) icon and find **MasterImpersonation** account; select it and click the **add - >** button underneath, then click **OK** at the bottom  

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex27.png">
</p></details>

&nbsp;

**3\.A.8.** Finally, click the **Save** button at the bottom of the *New role group* dialog to apply the changes

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex28.png">
</p></details>


&nbsp;

***Alternatively,***

&nbsp;

##### If you configured a Distribution group (see point **2.B.** above)



&nbsp;
**3\.B.1.** [Run Exchange Management Shell](https://docs.microsoft.com/en-us/PowerShell/exchange/exchange-server/open-the-exchange-management-shell?view=exchange-ps) as Administrator

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex21.png" class="minimized">
</p></details>

&nbsp;

**3\.B.2.** Enter the following lines in Exchange Management Shell console one by one:

```
$groupidentity = $(Get-Group RISG).DistinguishedName  
```
&nbsp;
```
New-ManagementScope -Name:"RIusersScope" -RecipientRestrictionFilter "MemberOfGroup -eq '$groupidentity'"
```

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\1sgcmd.png" class="minimized"><br><br><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\2sgcmd.png" class="minimized">
</p></details>


&nbsp;

**3\.B.3.** Next, return to [Exchange Admin Center](https://docs.microsoft.com/en-us/exchange/exchange-admin-center) and open the **permissions** tab in the navigation pane on the left, then click the **+** (Add) icon in the header of the right pane

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex23.png" class="minimized">
</p></details>

&nbsp;



**3\.B.4.** In the *New role group* dialog that appears, enter a role group's **Name**, then select the *RIusersScope* group that you configured on Step **3.2**. in the **Write scope** field

!!! tip "Tip"
    If you leave the *Default* Write scope, Impersonation will be applied for all users in the Org.

&nbsp;

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex24.png">
</p></details>

&nbsp;


**3\.B.5.** Next, click the **+** (Add) button under *Roles:*

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex25.png">
</p></details>


&nbsp;

**3\.B.6.** In the *Select a Role* dialog that appears, select **ApplicationImpersonation** in the pane on the left, then click the **add - >** button underneath and click **OK** at the bottom

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex26.png">
</p></details>
&nbsp;


**3\.B.7.**  Now you should enable the impersonation account to perform its role. To do that:

- Click the **+** (Add) button under *Members:*

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex29.png">
</p></details>

&nbsp;

- In the *Select Members* dialog that appears: click the **🔍** (Search) icon and find the account **MasterImpersonation**; click the **add - >** button underneath, then click **OK** at the bottom

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex27.png">
</p></details>

&nbsp;

**3\.B.8.** Finally, click the **Save** button at the bottom of the *New role group* dialog to apply the changes

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\ex28.png">
</p></details>
* * *

&nbsp;

&nbsp;

## Stage II: Verify the Configuration

&nbsp;

Next, you need to test the configured Impersonating account using the official tool [Microsoft Remote Connectivity Analyzer](https://techcommunity.microsoft.com/t5/exchange-team-blog/what-8217-s-new-with-microsoft-remote-connectivity-analyzer-a/ba-p/597652):

**1\.** Open Microsoft Remote Connectivity Analyzer via the link <https://testconnectivity.microsoft.com>   
**2\.** Open the tab **Exchange Server** in the navigation pane and select **Service Account Access** in the pane on the right   

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\test.png" class="minimized">
</p></details> 


&nbsp;

**3\.** Fill in the details for connecting to an end user account:  

**4\.** **Target Mailbox email address**: enter email address of any {{ short_name }} user managed by the configured Impersonation account   

**5\.** **Service Account User Name (Domain\User name or UPN)**: enter the account's name using the *{domain}\\{user name}* or *{user}@{domain}* format  

**6\.** The **Password** field: enter the service account's password  

!!! note "Note"
    Security of tested account's credentials entered in the dialog is guaranteed by Microsoft

&nbsp;

**7\.** Incase your configuration has a custom [Exchange Web Services URL](https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/start-using-web-services-in-exchange), select **Specify Exchange Web Services URL** and enter your corporate EWS URL.
Otherwise, select **Use Autodiscover to detect server settings** to let the tool auto-determine the URL

**8\.** Next, select **Test predefined folder** and leave the default value *Inbox* in the box below  

**9\.** Select **Use Exchange Impersonation** and under **Impersonated user** enter the same email address of a {{ short_name }} user managed by the configured Impersonation account    

**10\.** In the field **Impersonated user identified**, leave the default value *SmtpAddress*  

**11\.** If that is required in your configuration, select **Ignore Trust for SSL**  

**12\.** Read and confirm the “**I understand and must ...**” section; enter the CAPTCHA and click **Verify** to prove that you are not a robot  

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Setting-Up-Impersonated-Access-in-SmartCloud-Connect-and-Configuring-Mailbox-Access-for-Organizations-and-Users\test2.png" class="minimized">
</p></details> 


&nbsp;

**13\.** Click **Perform test** at the bottom of the dialog and check the test results to see if the configured Impersonated account works

&nbsp;

&nbsp;

* * *

&nbsp;

&nbsp;

## Stage III: Configure Exchange Impersonation in {{ product_name }} Admin panel

After creating a service account, proceed to [the steps provided in this article](../Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/) to configure the [Sync Engine](../Synchronization-Engine-An-Overview/) to operate via this account.


&#160;

&nbsp;

