---
description: Step-by-step guide on mass deployment of RG Email Sidebar for MS Exchange 2016, 2019
---
# Mass Deployment of the Add-In [MS Exchange 2016, 2019]  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>
&nbsp;

*3 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! tip "Tip"
    Besides rolling out the Solution for the end users, it is highly recommended to install the [{{ company_name }} managed Salesforce app](../Admin-Managed-Package/) in your Org; it will enable the full scope of {{ short_name }} features on the Salesforce side
    Also refer to [this article](../Mass-Deployment-of-the-Add-In-Office-365/) for instructions how to mass deploy the Add-In in Office 365.

&nbsp;

!!! note "Note"
    Pay attention that starting from June 2022, [Microsoft ceased support and updates of the Internet Explorer 11 desktop application](https://learn.microsoft.com/en-us/lifecycle/announcements/internet-explorer-11-end-of-support) on most versions of Windows 10 and encouraged its customers to move to other browsers. Since the MS Outlook 2013 for desktop uses Internet Explorer 11 engine to render embedded add-ins in its interface, it will be impossible to run {{ product_name }} on this version of MS Outlook. Learn more in [this {{ short_company_name }} article](https://docs.revenuegrid.com/ri/fast/articles/internet-explorer-end-of-support/) 

&nbsp;

To mass-deploy {{ product_name }} Add-In for the entitled users in your org, do the following:

!!! tip "Tip"
    Also see [this Microsoft article](https://docs.microsoft.com/en-us/microsoft-365/admin/manage/centralized-deployment-faq?view=o365-worldwide) for information on mass add-ins deployment

&nbsp;

**1\.** Open MS Exchange admin center. Refer to the following articles to find out how to access the Exchange admin center for your organization:

*   [Exchange 2016, 2019](https://technet.microsoft.com/en-us/library/jj150562(v=exchg.160).aspx)

2\. In the Exchange admin center, go to  **Organization **\> **Add-Ins** (Exchange 2016 / 2019) or **Apps** (Exchange 2013)

<p><img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet/docs\assets\57398d2e903360669faf1f0a\images\5894b21b2c7d3a7846309673.png" class="minimized">
</p> 



&nbsp;

**3\.** Click the **+** (Add) button and then choose the source that you want to install {{ product_name }} from. You can install the Add-In from AppSource or from a URL or file location:


<p><img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5894b31e2c7d3a784630967f.png" class="minimized">
</p> 


&nbsp;

*   **Add from AppSource.** At AppSource, find “{{ product_name }} for Salesforce” and click **Add**.
*   **Add from a URL.** In the URL field, enter the full URL for the {{ product_name }} for Salesforce manifest file and click **Install**.
*   **Add from file.** Select **Browse**, navigate to the location of the {{ product_name }} for Salesforce manifest file and click **Next**.

The “{{ product_name }} for Salesforce” Add-In will appear in the list of available apps.

&nbsp;

**4\.** Make {{ product_name }} for Salesforce available to the users in your organization. To do this, in the list of available add-ins, double-click “{{ product_name }} for Salesforce.com”. The  **Edit Add-in settings** dialog box will appear.

<p><img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5894b382dd8c8e73b3e94aa4.png" class="minimized">
</p> 


&nbsp;

**5\.** To make the Add-In available to all users in your organization, select the **Make this app available to users in your organization** checkbox and then select one of the following options:

*   **Optional, enabled by default.** Use this setting to have the {{ short_name }} Add-In enabled by default, allowing the users to disable it if necessary.
*   **Optional, disabled by default.** Use this setting to have the {{ short_name }} Add-In disabled by default, allowing the users to enable it if necessary.
*   **Mandatory, always enabled.** Users can’t disable this app. Use this setting when you do not want to allow your users to turn off the {{ short_name }} Add-In.

Click **Save**.

&nbsp;

**6\.** To verify that the {{ short_name }} Add-In was installed successfully for the user, make sure that the  **Salesforce** ribbon group appeared in the** Home** tab in the user’s MS Outlook.

<p><img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5894b3c1dd8c8e73b3e94aa7.png">
</p>

&nbsp;

* * *

&nbsp;

#### Setting the Default (Initial) Customization

In the latest {{ product_name }} updates the default (initial) set of customization settings can be defined by [local {{ product_name }} Admin](../How-to-Log-In-to-the-Admin-Panel/), to be applied right after the Solution is installed or after customization is reset to default by clicking the **Reset to default  settings** button in Customization page header. This feature enables  quick uniform management of settings for different user categories and  facilitates restoring product functioning after unwanted adjustments  were made in the settings.

&nbsp;
&nbsp;

#### **Defining Individual Synchronization Settings for a User or a Group of Users**

In the latest {{ product_name }} updates it is possible to push pre-defined synchronization settings to groups of users and individual users within an Org, or to all users of an Org; the users can be allowed or disallowed to adjust these settings. If you need to preset customized sync settings to different users in your Org, send us a corresponding request to [our Support team](mailto:support@revenuegrid.com)

&#160;
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