---
description: Add-In troubleshooting: what to do if the icon grayed out or no icon is displayed
---
# Add-In Troubleshooting: Icon Grayed Out or No Icon Displayed  
  

*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

### {{ product_name }} Icon Grayed Out

This issue concerns the [Desktop implementation](../Desktop-MSI-and-Cloud-Web-Implementations-Comparison/) of {{ product_name }} for Salesforce in MS Outlook for Windows. It manifests as {{ short_name }} icons in MS Outlook ribbon being replaced by a grayed out icon:

![](../assets/images/Using-SmartCloud-Connect/How-To-s/Troubleshooting/placeholders.png)

&nbsp;

The cause of the issue is your proxy auto-configuration script's error or custom proxy settings used on your system.

It occurs when [WPAD](https://manuals.gfi.com/en/webmon11/content/administrator/topics/gettingstarted/configuringwpad.htm?cshid=UsingWPAD) (Web Proxy Autodiscovery Protocol) is configured but cannot be resolved by the Add-In. 

Steps to resolve the issue:

**1\.** Find {{ short_name }} log files following [this instruction](../Troubleshooting-Product-Desktop-MSI-Implementation/)  

**2\.** Read [this article]f the General log contains the following repetitive error

```[ERROR] [connector_site]: [11:08:41.292001],<T6064>,{first chance exception}: class http::basic_error: Unable to find appropriate proxy for https://sfdc-live-desktop-invisible.azurewebsites.net/Desktop/GetUpdateInfo?Emails=******&ExplicitDomainName=&ProductVersion=1.101.0.0&PackageVersion= The proxy auto-configuration script could not be downloaded```  

**3\.** Check with the local IT Admin if there are custom proxy settings used on your system  

**4\.** [Open Windows Settings](https://www.digitalcitizen.life/introducing-windows-10-ways-open-settings) > select **Internet Options** > **Connections** tab > **LAN Settings**  

<p><img src="../../assets/images/Using-SmartCloud-Connect/How-To-s/Troubleshooting/lan_settings.png" class="minimized">
</p>

&nbsp;

**5\.** Make sure that that both boxes are cleared under "Automatic configuration"  

**6\.** Restart MS Outlook and see if the icons are displayed properly now

If that does not help, send the Add-In's logs to [our Support team](mailto:support@revenuegrid.com) for further investigation.

&nbsp;

&nbsp;

### {{ product_name }} Icon is not Displayed in the Ribbon

If you [installed {{ short_name }} Add-In successfully](../How-to-Install-and-Run-the-Solution-for-Office-365-Mailboxes/) and its icons [cannot be found in MS Outlook Desktop ribbon](https://support.microsoft.com/en-us/office/video-customize-the-ribbon-9ce81e05-ecc1-4142-a3e3-1298b37a59c6), but it is [available in MS Outlook on the Web](../Open-in-Outlook-Web/), then you probably [activated MS Outlook mode *Work offline*](https://support.microsoft.com/en-us/office/work-offline-in-outlook-f3a1251c-6dd5-4208-aef9-7c8c9522d633).  

To resolve the issue, please [switch MS Outlook back to *Online mode*](https://support.microsoft.com/en-us/office/switch-from-working-offline-to-online-2460e4a8-16c7-47fc-b204-b1549275aac9) and see if the {{ short_name }} icons appear in the ribbon.





&#160;
 &#160;

