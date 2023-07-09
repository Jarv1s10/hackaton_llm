---
description: Step-by-step guidance on how to troubleshoot the "Add-In Could Not Be Started" issue and other issues
---
# Add-In Troubleshooting: *Add-In Could Not Be Started* and Other Issues  
  

*5 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

If you successfully [installed the Add-In](../How-to-Install-and-Run-the-Solution-all-configurations/) and [configured your corporate firewall to let {{ product_name }} traffic through](../Overcoming-Firewall-Issues/), yet on trying to open it in MS Outlook you get an error notification "*ADD-IN ERROR. This add-in could not be started. Close this dialog to ignore the problem or click "Restart" to try again*", that might be caused an issue with [{{ product_name }}](../Introduction/) rendering. This article describes the ways to resolve the issue. The solutions are only applicable for MS Outlook Desktop for Windows. 

![](../assets/images/Using-SmartCloud-Connect/How-To-s/Troubleshooting/add-in-error.png)

&nbsp;

&nbsp;

### Solution 1: Refresh Microsoft Browser Configuration

The error may occur with various Add-Ins / plugins installed in MS Outlook Desktop for Windows. The below guidelines are official ones provided by Microsoft.  

The first step is to determine the versions of Windows OS and MS Outlook that you are using. These versions define  which native Microsoft browser is used to render MS Outlook Add-Ins; that might be MS Edge or MS Internet Explorer.

See [this Microsoft article](https://docs.microsoft.com/en-us/office/dev/add-ins/concepts/browsers-used-by-office-web-add-ins) to find out which one is used in your system based on your Windows version and Office package version combination. Users running the latest Windows 10 and Microsoft 365 Office updates typically have their Add-Ins rendered by MS Edge.



&nbsp;

#### If your system uses MS Edge

Sometimes the error is caused by [MS Desktop App Web Viewer](https://appsource.microsoft.com/en-us/product/office/WA104295828?tab=Overview) getting corrupt. Take the steps below to re-install this module.  

**1\.** Close all MS Office apps running in your system, including MS Outlook  
**2\.** Run the following cmdlet in Windows PowerShell or command line on your PC, with Admin permissions:  

```
powershell Add-AppxPackage -register -disable {Windows folder on system disk path e.g. 'C:\Windows\'}\SystemApps\Microsoft.Win32WebViewHost_cw5n1h2txyewy\AppxManifest.xml
```

**3\.** Run MS Outlook and try [opening {{ short_name }} Add-In](../How-to-Install-and-Run-the-Solution-all-configurations/#1_open_the_sidebar) to see if the issue was resolved  

&nbsp;

&nbsp;

&nbsp;

#### If none of Microsoft Add-Ins work or Sidebar controls become unclickable (WebView2 runtime)

The issue where important [Sidebar elements](../Introduction/) become unclickable, e.g. the *Save* or *Create* button, has a technical cause on Microsoft Outlook side. Specifically, due to the ongoing Microsoft transition from old MS Edge to [Chromium MS Edge](https://support.microsoft.com/en-us/microsoft-edge/download-the-new-microsoft-edge-based-on-chromium-0f4a3dd7-55df-60f5-739f-00010dba52cf) some MS Outlook for Windows versions have an interface frames rendering issue with MS Edge. Microsoft is planning to roll out a complete solution in a [future MS Windows update](https://blogs.windows.com/msedgedev/2020/10/19/edge-webview2-general-availability/).

An official workaround [provided by Microsoft](https://developer.microsoft.com/en-us/office/blogs/office-add-ins-community-call-february-10-2021/):  

!!! note "Note"
    The workaround works only for Windows 10 and Office 365 or Microsoft 365 package version *16.0.13530.20424* or newer. See [this Microsoft article](https://support.microsoft.com/en-us/office/about-office-what-version-of-office-am-i-using-932788b8-a3ce-44bf-bb09-e334518b8b19) to learn how to check what version you have

&nbsp;

**1\.** Close MS Outlook  
**2\.** Close MS Edge browser windows, if any are opened  
**3\.** Download [*MS Edge Webview2 runtime*](https://docs.microsoft.com/en-us/microsoft-edge/webview2/) from this location: <https://go.microsoft.com/fwlink/p/?LinkId=2124703>   

If this package does not work in your configuration, install an alternative version. Browse [this Microsoft resource](https://developer.microsoft.com/en-us/microsoft-edge/webview2/#download-section) for versions compatible with different MS Edge builds and x86, x64, or arm64 architecture.  

&nbsp;

**4\.** Open your Downloads folder and [install Webview2 on your Windows system](https://docs.microsoft.com/en-us/deployoffice/webview2-install#webview2-runtime-installation). The runtime's security and stability are guaranteed by Microsoft, see [this article](https://developer.microsoft.com/en-us/microsoft-365/blogs/understanding-office-add-ins-runtime/) for complete information on Webview2  
**5\.** Launch MS Outlook and check if {{ product_name }} Add-In can be opened and [key Sidebar controls](../Introduction/) are clickable   

&nbsp;

&nbsp;

&nbsp;

#### If that does not help

- Get the latest Windows 10 updates
- Get the latest Microsoft 365 / Office package updates
- [Install MS Edge Chromium](https://support.microsoft.com/en-us/microsoft-edge/download-the-new-microsoft-edge-based-on-chromium-0f4a3dd7-55df-60f5-739f-00010dba52cf); in some configurations that might be required to prevent [Win32WebViewHost.exe issues](https://github.com/OfficeDev/office-js/issues/1620)

&nbsp;

* * *

&nbsp;

#### If your system uses Internet Explorer

Since Microsoft stopped supporting the [Internet Explorer 11 desktop application](https://docs.microsoft.com/en-us/lifecycle/announcements/internet-explorer-11-end-of-support) on most versions of Windows 10, {{ company_name }} discontinued support of {{ product_name }} for Internet Explorer and older MS Outlook versions that use the Internet Explorer browser to render add-ins. 


Since the older Desktop versions of MS Outlook use Internet Explorer 11 engine to render embedded add-ins in its interface, it will be **impossible to run {{ product_name }}** on these versions of MS Outlook. Refer to this Microsoft help article for more information about [browsers used by Office Add-ins](https://learn.microsoft.com/en-us/office/dev/add-ins/concepts/browsers-used-by-office-web-add-ins).    
  
We recommend that our customers migrate from Internet Explorer-rendering versions to the newest versions of MS Office products that use other browsers (MS Edge, MS Edge Chromium or user’s default browser) to ensure {{ product_name }} functioning.    
  
Make sure that you are using an MS Outlook version that is included in the following MS Office builds:    
  
**1\.** For customers the Desktop MS Office versions set up via [MS Office Click-to-Run installation]( https://docs.microsoft.com/en-us/office/troubleshoot/office-suite-issues/office-click-to-run-installation):    
  
* *Microsoft Edge with WebView1: Microsoft 365 ver.16.0.11629 or later and Microsoft 365 version older than 16.0.13530.20424*  
  
* *Microsoft Edge with WebView2: Microsoft 365 ver.16.0.13530.20424 or later with [additionally installed WebView2]( https://docs.microsoft.com/en-us/office/dev/add-ins/concepts/browsers-used-by-office-web-add-ins#:~:text=On%20Windows%20versions%20prior%20to%20Windows%2011%2C%20the%20WebView2%20control%20must%20be%20installed%20so%20that%20Office%20can%20embed%20it.)*

**2\.** For customers using the Desktop MS Office versions set up via a [Windows Installer (MSI) package](https://docs.microsoft.com/en-us/windows/win32/msi/windows-installer-portal):    
  
* *Microsoft Edge with WebView2: Office 2021 or later*

&nbsp;


If you are using an MS Office build **older than 16.0.11629** or version **older than Office 2021**, you should consider upgrading to the latest versions from the list above. Additionally, make sure that you run Windows 10 build 1903 or newer. If it's older, we recommend you to upgrade your Windows system to the latest build.

!!! tip "Tip"
    Refer to [this Microsoft article]( https://support.microsoft.com/en-us/office/about-office-what-version-of-office-am-i-using-932788b8-a3ce-44bf-bb09-e334518b8b19) to find out what version of MS Office you are using.   
    To find out which version of Windows operating system you are running, consult [this Microsoft guide](https://support.microsoft.com/en-us/windows/which-version-of-windows-operating-system-am-i-running-628bec99-476a-2c13-5296-9dd081cdd808)



&nbsp;
&nbsp;

### Contact {{ company_name }} Support

If none of the above listed solutions resolves the issue, [contact our Support team](mailto:support@revenuegrid.com) for further assistance.

&nbsp;

*Also see the following articles:*  

["Browser version is not supported" troubleshooting](../Browser-Version-Troubleshooting/)

[{{ product_name }} mass deployment scenarios](../Email-Integration-Full-Deployment-Scenarios/)

[How {{ product_name }} works with EWS](../Working-With-EWS/)

[Microsoft Consent framework](https://docs.microsoft.com/en-us/azure/active-directory/develop/consent-framework)  

[Microsoft App Consent Experience](https://docs.microsoft.com/en-us/azure/active-directory/develop/application-consent-experience)  


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
<div class="banners banner-2">
  <img src="../../assets/images/banners/banner-2.svg" style="width: 100%; height: 100%;">
  <a class="button" href="https://revenuegrid.com/request-demo/?utm_source=kb_rg&utm_medium=referral&utm_campaign=eac_demo&utm_content=banner" target="_blank">Book a free demo</a>
</div>