# Add-In Troubleshooting: "Add-In Could Not Be Started" and Other Issues

&nbsp;

If SSI was successfully installed for and allow-listed in the corporate firewall to let SSI traffic through, yet an error notification "*ADD-IN ERROR. This add-in could not be started. Close this dialog to ignore the problem or click "Restart" to try again*" appears on opening the Add-In in MS Outlook, that might be caused an issue with [Sidebar](../Introduction/) rendering. This article describes the ways to resolve the issue. The solutions are only applicable for MS Outlook Desktop for Windows. 

![](../assets/images/Troubleshooting/add-in-error.png)

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

**3\.** Run MS Outlook and try [opening SSI Add-In](../How-to-Open-C4C-SSI-Sidebar/) to see if the issue was resolved  

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
**5\.** Launch MS Outlook and check if SSI Add-In can be opened and [the key Sidebar controls](../Introduction/) are clickable   

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

In older versions of MS Windows and MS Outlook, Internet Explorer is used to render Outlook Add-Ins. There are several possible solutions for Internet Explorer:  

&nbsp;

#### Check your Internet Explorer

Make sure that you have the latest version of Internet Explorer installed, as described in [this Microsoft article](https://support.microsoft.com/en-us/topic/run-the-latest-version-of-internet-explorer-11-ea628df4-50ce-8019-f9f4-468e39685cea).

If needed, re-activate Internet Explorer in your Windows system:

**1\.** Press the **Windows key + R**, type *control* and press Enter   
**2\.** Click **Programs**  
**3\.** Click **Programs and Features**  
**4\.** Select **Turn Windows features on or off**  
**5\.** Select the checkbox next to *Internet Explorer 11*  
**6\.** Reboot Windows to apply the changes, then check if the issue was resolved

&nbsp;
&nbsp;

##### Fix Internet Explorer Settings, if they got corrupt

**1\.** Press the **Windows key + R**, type *inetcpl.cpl* and press Enter to open Internet Explorer's *Internet Options*  
**2\.** Open the tab **Advanced**   
**3\.** Click **Reset** under **Reset Internet Explorer Settings**  
**4\.** Click **Reset** under **Are you sure you want to reset all Internet Explorer settings?**  
**5\.** As soon as the changes are applied, click **Close** and then **OK**  
**6\.** Reboot your Windows to apply changes, then check if the issue was resolved  

&nbsp;
&nbsp;

##### Install System Updates

To get maximum performance and compatibility, all SSI users are recommended to upgrade to Windows 10 build *1903 or above* and Microsoft 365 / Office package version *16.013530* or above.

&nbsp;
&nbsp;

##### Enable Protected Mode in Internet Explorer

In case upgrading is not an option, you can try enabling *Protected mode* in MS Internet Explorer. To do that:

**1\.** Close MS Outlook and any web browsers you use  
**2\.** Press the **Windows key + R**, type *inetcpl.cpl* and press Enter to open Internet Explorer's **Internet Options**  
**3\.** Open the **Security** tab  
**4\.** Click **Internet Sites zone**  
**5\.** Select the checkbox **Enable Protected Mode**  
**6\.** Click **OK**  
**7\.** Restart MS Internet Explorer and Outlook  
**8\.** See if you can open the Add-In in MS Outlook now  
**9\.** If the issue persists, reboot your PC and try again    

&nbsp;

&nbsp;

##### Add SSI resources to Trusted Sites

If the issue persists after enabling *Protected mode*:

**1\.** Press the **Windows key + R**, type *inetcpl.cpl* and press Enter to open Internet Explorer's **Internet Options**  
**2\.** Open the **Security** tab  
**3\.** Select **Trusted sites** under available zones  
**4\.** Click the button **Sites**  
**5\.** Add *\*\.invisiblesolutions.com* to the list  
**6\.** Restart MS Outlook and see if you can open the SSI Add-In now  



&nbsp;
&nbsp;

### Contact SAP Support

If none of the above listed solutions resolves the issue, [contact SAP Support](https://support.sap.com/en/contact-us.html) for further assistance.

&nbsp;

*Also see the following articles:*  

["Browser version is not supported" troubleshooting](../Browser-Version-Troubleshooting/)

[Microsoft Consent framework](https://docs.microsoft.com/en-us/azure/active-directory/develop/consent-framework)  

[Microsoft App Consent Experience](https://docs.microsoft.com/en-us/azure/active-directory/develop/application-consent-experience)  





&#160;
 &#160;

