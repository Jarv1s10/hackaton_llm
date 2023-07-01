---
description: Step-by-step instruction on how to install and run the desktop (.MSI) implementation (MS Outlook 2013, 2016, 2019)
---
# How to Install and Run the Desktop (.MSI) implementation (MS Outlook 2013, 2016, 2019)  
 
 
 
**[the Desktop (.MSI) Implementation  is no longer supported]**

<br>

*[Productivity Package Home page](../../)*

<!--<i>For users of the Email Sidebar on:</i><br><br>-->
<!--<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>-->

<!--&nbsp;-->

<!--*4 min read*  -->

<!-- ShareThis BEGIN --> 
<!--<div class="addthis_inline_share_toolbox"></div>-->
<!-- End ShareThis --> 

<!--&nbsp;-->

<!--### Desktop (.MSI) Planned Deprecation-->

<!--The Desktop (.MSI) implementation for Windows is tied to Internet Explorer 11 engine for [Sidebar](../Introduction/) rendering. For this reason, as soon as Microsoft abandons Internet Explorer 11 according to [their announcement](https://techcommunity.microsoft.com/t5/microsoft-365-blog/microsoft-365-apps-say-farewell-to-internet-explorer-11-and/ba-p/1591666), the Desktop {{ short_name }} implementation will be deprecated.  -->

<!--Therefore, the [standard Web (Cloud) implementation](../How-to-Install-and-Run-the-Solution-for-Office-365-Mailboxes/) will become the only choice.-->

<!--&nbsp;-->

<!--Currently, the Desktop (.MSI) implementation is used exclusively in either of the following cases: **1.** for customized Enterprise {{ short_name }} configurations, **2.** to work with MS Exchange 2013, or **3.** to use {{ product_name }} in a virtual machine environment, e.g. [Citrix XenApp](../How-to-Run-and-Troubleshoot-the-Solution-on-Citrix-XenApp/). This Add-In installation method is only available for MS 2013, 2016, 2019 (Desktop) for Windows. Also refer to [this article](../Desktop-MSI-and-Cloud-Web-Implementations-Comparison/) for a detailed comparison of the two implementations-->

<!--&nbsp;-->

<!--<iframe src="https://player.vimeo.com/video/385513763" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>-->
<!--&nbsp;-->

<!--&nbsp;-->

<!--## I. Download and Install the .MSI distribution package-->

<!--Some customized Enterprise implementations of {{ product_name }} are only available as the Desktop (.MSI) version; their distribution package can only be obtained from our [Support and CSM team](mailto:support@revenuegrid.com).-->

<!--&nbsp;-->


<!--&nbsp; -->

<!--The distribution packages are guaranteed to contain no viruses or other malicious code by {{ company_name }} [Privacy and Security policies](../Privacy-and-Security/).-->


<!--To install the Add-In: run the downloaded .MSI file,  and complete the easy three-step installation process. By default, the {{ product_name }} Add-In will be installed in the '_%systemdisk%\\Users\\%username%\\AppData\\Roaming\\RevenueGrid.com\\{{ product_name }} Add-In_' folder, taking around 28-40 Mb of your HDD space.  -->

<!--Preconditions for installing the .MSI package:-->

<!--- MS Outlook 2013 - 2019 installed on your system-->
<!--- Having admin access permissions on your workstation, including system drive write permissions-->

<!--After you launch the .msi package, MS Outlook will be opened automatically to download updated Add-In installation data, then you will be promoted to close it again, along with some other running apps, to proceed with installation. Close MS Outlook manually, the rest applications manually or automatically.-->

<!--![](../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/close-apps.png)-->



<!--&nbsp;-->

<!--* * *-->

<!--&nbsp;-->

<!--## II. {{ product_name }} Logon-->

<!--!!! warning "Important"-->
<!--    Before using {{ product_name }} in MS Outlook (Desktop) on Windows, please make sure that you have the latest version of MS Edge installed, since it is used to render {{ product_name }} in MS Outlook Desktop-->

<!--After the {{ product_name }} Add-In has been installed in your MS Outlook Desktop or On the Web, you need to open the Sidebar and log on to the Add-In. While on step ( **III** ) the Sign-Up wizard will authorize the Add-In to work with Salesforce and MS Exchange data, at this step similar authentication steps are performed to set up [{{ company_name }} synchronization](../Synchronization-Engine-An-Overview/).-->

<!--### **1\.** To open the Sidebar:-->

<!--- click the **Open {{ product_name }}** button in MS Outlook (Desktop) ribbon-->

<!--![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b6b03020428631d7a89c543.png)-->
<!--&nbsp;-->

<!--### **2\.** Logging on to {{ product_name }}-->

<!--Next, log on to {{ product_name }} using Salesforce OAuth logon:-->

<!--&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2.1.** Click the **Connect to Salesforce** button. The Salesforce [OAuth](http://help.salesforce.com/articleView?id=remoteaccess_authenticate_overview.htm) page will be opened in your browser-->

<!--![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b6b05ce0428631d7a89c563.png)-->
<!--&nbsp;-->
<!--&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2.2.** Enter your Salesforce credentials on the page or select a previously saved account's username and click **Log In**-->

<!--![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b6b07ba2c7d3a03f89d7a23.png)-->
<!--&nbsp;-->
<!--In the screenshot above, a standard Salesforce login window is shown. Note that this OAuth window may look differently, depending on your Salesforce configuration.-->

<!--&nbsp;-->

<!--### **3.** Enable {{ product_name }} [synchronization](../Synchronization-Engine-An-Overview/)-->

<!--Set up {{ company_name }} synchronization by authorizing it to access your MS Exchange / Office 365 data. Please follow the steps described in [this article](../Authorizing-Sync-Engine-to-Work-with-Your-Data/) to do that.-->

<!--!!! warning "Important"-->
<!--    If you are using several different email boxes for your correspondence (not [aliases](https://support.office.com/en-us/article/add-or-remove-an-email-alias-in-outlook-com-459b1989-356d-40fa-a689-8f285b13f1f2)), make sure to authorize [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/) for the same email box as one for which you installed the [Add-In](../Introduction/), otherwise the [Sync engine functions](../AddIn-vs-Sync-Functions/) will work incorrectly even though {{ short_name }} Sync will appear to be running-->

<!--!!! tip "Tip"-->
<!--    Refer to [this article](../Historical-Sync-&-Timezones-Matching/) to learn what emails and calendar items you have in MS Exchange / Office 365 will be auto-saved in Salesforce if you enable the corresponding settings ([calendar items auto-saving](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#meeting_appointment_autosaving), [emails auto-saving](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_emails_emails_autosharing)) after setting up {{ company_name }} synchronization-->

<!--!!! warning "Important"-->
<!--    Please note that if step 3 is skipped, you will be able to run and use {{ product_name }}, except for its functions [performed by {{ short_name }} synchronization](../AddIn-vs-Sync-Functions/), and the Add-In will be suggesting to complete this step in **Observations** (**Smart Actions** bar > **More...**): *Action required! Synchronization component is turned off.* Clicking on the **ENABLE NOW** button will open the [corresponding setup page](../Authorizing-Sync-Engine-to-Work-with-Your-Data/) in your browser-->

<!--![](../assets/images/Getting-Started/First-Steps/desktop_sync_not_enabled.png)-->

<!--&nbsp;-->

<!--!!! note "Note"-->
<!--    If you skip [{{ company_name }} sync](../Synchronization-Engine-An-Overview/) activation, you will not be able to us a number of {{ short_name }} features performed by {{ short_name }} sync. See [this article](../AddIn-vs-Sync-Functions/) for details-->

<!--&nbsp;-->
<!--* * *-->
<!--&nbsp;-->

<!--## **III. (Admins only) Install the managed packages in Salesforce**-->

<!--To enable the full scope of features offered by {{ product_name }} several minor adjustments must be made in your Salesforce Org's configuration; installing the [{{ company_name }} managed package](../Admin-Managed-Package/) and [Invisible Suite managed package](../Admin-Managed-Package/) allows to accomplish that quickly and effortlessly. Follow the above links for complete information about the packages.-->

<!--&nbsp;-->
<!--* * *-->
<!--&nbsp;-->

<!--## Uninstalling the Add-In-->

<!--If you'll need to reinstall or uninstall the Add-In on a workstation, please refer to [this article](../Uninstalling-All-Product-Components/#uninstalling_smartcloud_connect_add-in_desktopmsi_implementation) to learn how to do that.-->

<!--&#160;-->
<!-- &#160;-->


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