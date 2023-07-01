---
description: Revenue Grid discontinues the support of RG Email Sidebar in Internet Explorer and the older versions of Outlook, which used Internet Explorer to render add-ins
---
# Internet Explorer End of Support  
  

*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

Starting from June 2022, [Microsoft ceased support and updates of the Internet Explorer 11 desktop application](https://docs.microsoft.com/en-us/lifecycle/announcements/internet-explorer-11-end-of-support) on most versions of Windows 10 and encouraged its customers to move to other browsers. For this reason, we also discontinue the possibility to run {{ product_name }} in Outlook on the Web ([Office.com](https://office.com)/[Outlook.com](https://outlook.com)) opened in the Internet Explorer browser. Refer to [this article](../Supported-Email-Services/#browsers) for the list of compatible web browsers.

Since the older Desktop versions of MS Outlook use Internet Explorer 11 engine to render embedded add-ins in its interface, it will be **impossible to run {{ product_name }}** on these versions of MS Outlook. Refer to this Microsoft help article for more information about [browsers used by Office Add-ins](https://learn.microsoft.com/en-us/office/dev/add-ins/concepts/browsers-used-by-office-web-add-ins).
    
We recommend that our customers migrate from Internet Explorer-rendering versions to the newest versions of MS Office products that use other browsers (MS Edge, MS Edge Chromium or user’s default browser) to ensure {{ product_name }} functioning.   

<br>
!!! tip "Tip"  
    Refer to [this Microsoft article](https://learn.microsoft.com/en-us/office/dev/add-ins/concepts/browsers-used-by-office-web-add-ins#microsoft-365-subscription-versions-of-office-on-windows) for Microsoft 365 subscription versions of Office on Windows
<br>
  
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



&nbsp;

