---
description: Learn how to uninstall all product components from your system
---
# How to Uninstall All Product Components from Your System


<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>
<div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

If you want to stop using {{ product_name }}, you need to:

1.  Remove the {{ product_name }} Add-In from your email application
2.  Stop the sync process in {{ product_name }}

Your account will be automatically deactivated approximately one month after you perform the steps below. If you want to have your account deactivated, please send a corresponding request to [our Support team](mailto:support@revenuegrid.com).

!!! tip "Tip"
    Also refer to [this FAQ entry](../Frequently-Asked-Questions/#13_dedicated_salesforce_emails_salesforce_tasks_salesforce_contacts_folders_or_categories_in_email_client_created_by_rges_sync_engine) for detailed information on custom folders and categories associated with {{ product_name }}

&nbsp;

#### Removing the {{ product_name }} Add-In (Web/Cloud implementation)

To remove the {{ product_name }} Add-In from Microsoft Outlook for Windows, do the following:

1.  Click **File** and then click **Manage Add-ins**.
2.  In the list, select **{{ product_name }} for Salesforce** and click the **Minus** (Uninstall) button  

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5832fd7d903360645bfa6aa3.png" class="minimized">
</p>

&nbsp;

To remove the {{ product_name }} Add-In from Microsoft Outlook for Mac, do the following:

1.  Click **Manage Apps** in the upper right corner of the window
2.  In the list, select **{{ product_name }} for Salesforce** and click the **Minus** (Uninstall) button

&nbsp;

To remove the {{ product_name }} Add-In from Office 365, do the following:

1.  In Mail, in the **Settings** menu, click **Manage add-ins**
2.  Select the “My add-ins” category, find **{{ product_name }} for Salesforce** and turn off the switch

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5832fd9fc697916f5d053175.png" class="minimized">
</p>

&nbsp;

&nbsp;

#### Uninstalling {{ product_name }} Add-In (Desktop/MSI implementation)

Removing the Add-In installed from an MSI package (please refer to the corresponding section of [this article](../How-to-Install-and-Run-the-Solution-all-configurations/) for more information) follows the regular procedure of uninstalling Windows applications:

1\. Press **⊞ Win+R** to open the Run dialog;   
2\. Enter _appwiz.cpl_ in the dialog to open Windows Programs and features;  
3\. Type _smart_ in the Search Programs and Features search bar on the right-hand side;  
4\. Right-click on _{{ product_name }} for Salesforce.com Add-In_ and select **Uninstall**.

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b759d640428631d7a8a0e69.png" class="minimized">
</p>

Please note that MS Outlook should be closed when the Add-In is being uninstalled.

&nbsp;

&nbsp;

#### Stopping Synchronization

Note that if you do not stop {{ short_name }} synchronization after removing the Add-In, your emails and events will still be synchronized between your MS Exchange and Salesforce, according to the patterns you previously had, including the custom Salesforce categories. To suspend {{ company_name }} synchronization, do the following:

<p style="margin-left:4%">
    <br>
    <b>1.</b> Open the {{ product_name }} Add-In in MS Outlook Desktop or On the Web version
    <br><br>
</p>

<p>
    <img src="..\..\assets\images\Install-and-Run\uninstall\sync-settings.png" style="width:27.49%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:4%">
    <br>
    <b>2.</b> Click the <b>&#x2630; Menu</b> button in {{ product_name }} and select <b>Sync settings</b>
    <br><br><br><br>
</p>

<p style="margin-left:4%">
    <b>3.</b> Click &#10073;&#10073; <b>Pause</b> on the <b>General</b> tab of the <a href="../Configuring-Activities-Synchronization-Settings-rg/">new Sync Settings page</a>, or on the Dashboard of the <a href="../Configuring-Activities-Synchronization-Settings/">legacy Sync Settings page</a> (depending on the appearance of your Sync Settings page)
</p>

<p>
    <img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5832fdbc903360645bfa6aac.png" style="width:47%; display:inline-block; vertical-align:middle; margin-left:7px; float: right">
    <br><br><br>
    <img src="..\..\assets\images\Install-and-Run\uninstall\pause.png" style="width:52%; display:inline-block; vertical-align:middle; float: left">
    <br><br><br><br><br><br><br><br>
</p>

&nbsp;

&nbsp;

#### Full Sync Engine Disabling

{{ short_name }} sync component can be completely disabled by the [local admin](../How-to-Log-In-to-the-Admin-Panel/) (for Enterprise implementations) or by request sent to [our Support team](mailto:support@revenuegrid.com). Sync also gets auto-disabled if you change or remove your [access authentication credentials](../Authorizing-Sync-Engine-to-Work-with-Your-Data/); in this case synchronization will carry out ten MS Exchange connection attempts. If all of them fail, you will get a corresponding automatic warning notification by email; later, all your customization and synchronization settings will be reset to default and the custom Salesforce Emails, Salesforce Tasks, Salesforce Contacts folders will be removed from MS Outlook (the Add-In will not be removed automatically).


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
