---
description: Step-by-step guide on mass deployment of RG Email Sidebar for Office 365
---
# Mass Deployment of the Add-In [Office 365]  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>
&nbsp;

*6 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! note "Note"
    Refer to [this article](../Mass-Deployment-of-the-Add-In-MS-Exchange/) if you need to mass deploy the Add-In for MS Exchange 2016, 2019 mailboxes

&nbsp;

!!! warning "Important"
    After you install the Add-In for the end users, make sure that {{ short_name }} Sync Engine is activated for them to enable [all product features](../AddIn-vs-Sync-Functions/). That can be done [either individually by each user](../Authorizing-Sync-Engine-to-Work-with-Your-Data/) or [in bulk using Exchange Impersonation](../Impersonation-O365/)

&nbsp;

!!! tip "Tip"
    Besides rolling out the solution for the end users, it is highly recommended to install the [{{ product_name }} Salesforce managed package](../Admin-Managed-Package/) in your Org; it will enable the [full scope of {{ short_name }} features](../Admin-Managed-Package/#package_contents) on the Salesforce side

&nbsp;
&nbsp;

#### Add-In mass deployment

!!! tip "Tip"
    Also see [this Microsoft article](https://docs.microsoft.com/en-us/microsoft-365/admin/manage/centralized-deployment-faq?view=o365-worldwide) for information on mass add-ins deployment

&nbsp;

To install [{{ product_name }} Add-In](../Introduction/) for a group of entitled end users' mail accounts, do the following:

**1\.** Log in to [Office 365 Admin Center](https://docs.microsoft.com/en-us/microsoft-365/admin/admin-overview/about-the-admin-center?view=o365-worldwide) with Admin credentials  

<https://portal.office.com/adminportal/>  

!!! note "Note"
    The Privacy and security of all configuration activities described in this article are guaranteed by the [applicable {{ company_name }} policies](https://revenuegrid.com/privacy-policy/)

&nbsp;

**2\.** Create an MS Exchange Distribution group or Security group as described in [article 1 (Distribution)](../Impersonation-O365/#a_to_create_a_distribution_group) or [article 2 (Security)](../Impersonation-O365/#b_to_create_a_mail-enabled_security_group_instead); the group will include the end business users who entitled to have {{ product_name }} in your company. Note that having such a group allows to easily manage active {{ short_name }} users and mass-activate Sync engine over a [configured Impersonating account](../Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/). The group will be required on the Steps **8.A.5** and **8.B.2** of this guide

&nbsp;

**3\.** In the navigation page on the left, go to **Settings** > **Integrated Apps**   

**4\.** Click the button **Add-Ins** in the upper right corner  

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Mass-Deployment\md2.png" class="minimized">
</p>

&nbsp;

**5\.** Click the button **Deploy Add-In**

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Mass-Deployment\deploy-addin.png" class="minimized">
</p>

&nbsp;

**6\.** Click **Next** in the dialog that appears

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Mass-Deployment\add2.png" class="minimized">
</p>


&nbsp;



**7\.** In the following dialog, select the source you want to install the Add-In from:  

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Mass-Deployment\add1.png" class="minimized">
</p>

&nbsp;

**A.** **Choose from the store**: installation from [Microsoft 365 AppSource](https://appsource.microsoft.com/en-us/marketplace/apps?page=1&country=US&region=ALL&product=office%3Boutlook). This is the recommended way used for typical deployment cases

&nbsp;

**or**  

&nbsp;

**B.** **Upload custom apps**: installation from [a setup URL or Manifest file](../How-to-Install-the-Add-In-from-an-XML-Manifest-File-or-URL/). This method is normally used for custom Enterprise {{ product_name }} implementations deployment 

&nbsp;

&nbsp;

**8\.** The remaining setup steps depend on your selection on the previous Step

&nbsp;

##### If you select option A: Choose from the Store

**8\.A.1.** AppSource home page will be opened in your web browser. Enter "*{{ company_name }}*" in the search field, then click on the Solution's icon in the search results

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Mass-Deployment\appsource.png">
</p>
&nbsp;

**8\.A.2.** Click **Get it now** on the Add-In's page 

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Mass-Deployment\md3.png" class="minimized">
</p> <br> <br>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Mass-Deployment\md4.png" class="minimized">
</p>

&nbsp;

**8\.A.3.** Fill in your contact details to get the Add-In.  
These details are never shared with any third parties, they are used exclusively to establish communication with you by {{ company_name }} CSM or Support Teams

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Mass-Deployment\getapp.png" class="minimized">
</p>

&nbsp;

**8\.A.4.** Read the consent "I give Microsoft permission to use ...", select the checkbox and click **Continue** in the access consent dialog   

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Mass-Deployment\md5.png">
</p>

&nbsp;

!!! note "Note"
    All configuration activities described in this article are typical secure actions performed for {{ product_name }} Add-In installation. Privacy and security of handling of accessed user data are guaranteed by the [applicable {{ company_name }} policies](https://revenuegrid.com/privacy-policy/)

&nbsp;



**8\.A.5.** In the following dialog, make sure that the switch *Is this a test deployment?* is switched to **No**  

Assign users who will get the Add-In installed in their mail accounts: 1. select **Specific users/groups**; 2. in the field below, find and add {{ short_name }} end users one by one or in bulk using the Distribution group or Security group that you created on Step **2.**   

Click **Next** to continue  


<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Mass-Deployment\md6.png" class="minimized">
</p>
&nbsp;

**8\.A.6.** Read the permissions you are granting to {{ product_name }} Add-In and click **Next**

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Mass-Deployment\md7.png" class="minimized">
</p>


&nbsp;

**8\.A.7.** Click **Finish Deployment** in the final dialog  


<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Mass-Deployment\md8.png" class="minimized">
</p>

&nbsp;

The Add-In will be deployed for all assigned users within 12 hours or less. Before the end users start using the Add-In, make sure you have enough activated {{ product_name }} licenses. [Contact our CSM team](mailto:support@revenuegrid.com) directly to address any matters with product licenses



!!! warning "Important"
    Besides deploying the Add-In for the end users, it is important to ensure that its incoming and outgoing connections are **not** blocked by your corporate firewall. Refer to [this article](../Overcoming-Firewall-Issues/) to learn how to do that

&nbsp;

&nbsp;

**Alternatively:**

&nbsp;
&nbsp;

##### If you select option B: Upload custom apps

**8\.B.1.** You may install the Add-In from a customized [Add-In Manifest](../How-to-Install-the-Add-In-from-an-XML-Manifest-File-or-URL/) provided by [our CSM team](mailto:support@revenuegrid.com): from an *.xml* file on your hard drive by clicking **Choose file** or from a web address by entering the URL in the corresponding field. After you select the Manifest, click **Upload** at the bottom  

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Mass-Deployment\add3.png"> <br> <br> 
<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Mass-Deployment\add4.png">
</p></details>

&nbsp;

**8\.B.2.** In the next dialog you should assign users who will get the Add-In installed in their mail accounts: **1.** select **Specific users / groups**; **2.** in the field below, find and add {{ short_name }} end users one by one or in bulk using the Distribution group of Security group that you created on Step **2**.  

In addition to that, define the Add-In's Deployment method. Choose *Fixed* (recommended) if you want {{ product_name }} Add-In's icon to be constantly displayed in the user's MS Outlook ribbon, or choose *Available* if you want {{ product_name }} Add-In to be optionally available in their ribbon, or choose *Optional* if you want to allow the users to remove the Add-In.  

Click **Deploy** at the bottom of the dialog to deploy the Add-In for the entitled users

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Mass-Deployment\add5.png" class="minimized">
</p></details>

&nbsp;

**8\.B.3.** You'll see the deployment in progress screen and then the deployment confirmation dialog; click **Close** in this dialog

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Mass-Deployment\add6.png" class="minimized">
<br> <br>
<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Mass-Deployment\add7.png" class="minimized">
</p></details>

&nbsp;

The Add-In will be deployed for all assigned users within 12 hours or less. Before the end users start using the Add-In, make sure you have enough activated {{ product_name }} licenses. [Contact our CSM team](mailto:support@revenuegrid.com) directly to address any matters with product licenses

!!! warning "Important"
    Besides deploying the Add-In for the end users, it is important to ensure that its incoming and outgoing connections are **not** blocked by your corporate firewall. Refer to [this article](../Overcoming-Firewall-Issues/) to learn how to do that

&nbsp;
&nbsp;

* * *
&nbsp;

#### Setting the Default (Initial) Customization

In the latest {{ product_name }} updates the default (initial) set of customization settings can be defined by [local {{ product_name }} Admin](../How-to-Log-In-to-the-Admin-Panel/), to be applied right after the Solution is installed or after customization is reset to default by clicking the **Reset to default  settings** button in Customization page header. This feature enables  quick uniform management of settings for different user categories and  facilitates restoring product functioning after unwanted adjustments  were made in the settings.

&nbsp;

* * *

&nbsp;

#### **Defining Individual Synchronization Settings for a User or a Group of Users**

In the latest {{ product_name }} updates it is possible to push pre-defined synchronization settings to groups of users and individual users within an Org, or to all users of an Org; the users can be allowed or disallowed to adjust these settings. If you need to preset customized sync settings to different users in your Org, send us a corresponding request to [our CSM team](mailto:support@revenuegrid.com).



&#160;
 &#160;

