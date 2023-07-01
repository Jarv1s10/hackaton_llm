---
description: The mass deployment scenario when the local mail server Admin installs the RGES for Gmail and Salesforce Chrome Extension
---
# Mass Deployment of the Chrome Extension for Gmail  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*6 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

[{{ short_name }} Chrome Extension for Gmail](../Using-the-Solution-for-Salesforce-and-Gmail/) includes [most](../Using-the-Solution-for-Salesforce-and-Gmail/#differences_between_the_exchangeoffice_365_add-in_implementation_and_the_chrome_extension_for_gmail) of [{{ short_name }} Outlook Add-In's and Synchronization features](../AddIn-vs-Sync-Functions/) for Gmail / Google Workspace (G Suite). The Extension can be [installed individually](../How-to-Set-Up-the-Chrome-Extension-for-Salesforce-and-Gmail/) or mass-deployed for all end users by the local mail server Admin.

This article describes the mass deployment scenario where the local mail server Admin installs the [{{ short_name }} for Gmail and Salesforce Chrome Extension](https://chrome.google.com/webstore/detail/smartcloud-connect-for-sa/agfekjndkedoakoeahndfnjilkifbicn?hl=en) for all {{ short_name }} end users in an Org. It is a standard secure [Chrome browser extension](https://developer.chrome.com/extensions) reviewed by Google, and in the enterprise environment it can be mass-deployed for multiple end users using [Microsoft Group Policy](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/policy/group-policy-architecture) mechanisms. This Chrome Extension mass deployment method is only viable in Windows systems, [Windows Active Directory](https://searchwindowsserver.techtarget.com/definition/Active-Directory) environment.

The alternative method for non-Windows systems uses Google's native mechanisms which ensure automatic Extensions installation in Chrome browser after that was enforced for logged in Google accounts by Google Workplace Admin. See [this Google article](https://support.google.com/chrome/a/answer/6306504?hl=en) for complete information.

Besides Extension installation, mass {{ product_name }} for Gmail deployment requires mass Sync activation via a Service account. See [this article](../Gmail-Service-Account/) to learn how to do that.

&nbsp;

To mass-deploy the Chrome Extension using Active Directory, follow the instruction below (based on the [guidelines](https://dennisspan.com/deploying-google-chrome-extensions-using-group-policy/) developed by [Dennis Span](https://dennisspan.com/)).

{{ product_name }} Extension deployment string to be used ([fast prod build](../Using-the-Solution-for-Salesforce-and-Gmail/) installation):   ````agfekjndkedoakoeahndfnjilkifbicn;https://clients2.google.com/service/update2/crx````

&nbsp;

**1\.** Import the [Google Chrome ADMX files](https://support.google.com/chrome/a/answer/187202?hl=en) into your [Active Directory environment](https://searchwindowsserver.techtarget.com/definition/Active-Directory) 

The described method to mass-deploy Chrome extensions is through [Microsoft Group Policy](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/policy/group-policy-architecture). As per [Google](http://www.chromium.org/administrators/frequently-asked-questions): "*For Windows, it is recommended to use Group Policy vs. preferences  files because only Group Policy can be enforced*". An identical statement is  made in the [Chrome Deployment Guide](https://docs.google.com/document/d/1iu6I0MhyrvyS5h5re5ai8RSVO2sYx2gWI4Zk4Tp6fgc/edit#heading=h.q4aguier9n7x): "*Use Windows Group Policies (GPO policies) and cloud policy over preferences when possible. Unlike policies, preferences do not apply to  previous installations of Chrome and are only applied to a single  profile. Policies also override any preferences settings for a feature. Also note that the master_preferences file can be changed and not enforced like group policies can*".

&nbsp;

Google [provides official ADM and ADMX files](https://support.google.com/chrome/a/answer/187202?hl=en) which enable the end users to manage its products. For {{ short_name }} Extension mass deployment, we recommend you to use the [ADMX files](https://cloud.google.com/chrome-enterprise/browser/download/) only and not the ADM files. Before you can use Microsoft Group Policies to mass-deploy the Extension, you first need to import the Google Chrome ADMX files in your [Group Policy Central Store](https://activedirectorypro.com/configure-group-policy-central-store/).
The ADMX files, as well as the ADM language files, (**.ADML*) can be found in the directory *Configuration\admx* of the extracted [Chrome Enterprise Bundle](https://cloud.google.com/chrome-enterprise/browser/download/) archive.

If you are not familiar with the Central Store for Group Policies and require more detailed information, refer to the official Microsoft article [How to create and manage the Central Store for Group Policy Administrative Templates in Windows](https://support.microsoft.com/en-us/help/3087759/how-to-create-and-manage-the-central-store-for-group-policy-administra).

Chrome Enterprise Bundle includes the following six ADMX files:

- *chrome.admx*
- *ChromeUASwitcher.admx*
- *google.admx*
- *GoogleUpdate.admx*
- *LegacyBrowserSupport.admx*
- *PasswordAlert.admx*

The purposes of most of these ADMX files are self-explanatory, except for the ADMX file *google.admx*. This file only has one purpose, which is to set the shared *“Google”* folder in the [Group Policy editor](https://www.tenforums.com/tutorials/79976-open-local-group-policy-editor-windows-10-a.html). This folder ensures that all Google policy settings (for the Chrome browser or other Google products) are grouped under one folder.

![](https://dennisspan.com/wp-content/uploads/2017/07/Deep-dive-automating-and-configuring-Google-Chrome-Google-Chrome-group-policies.jpg)

&nbsp;

The Group Policy Central Store is located on your [domain controllers](https://www.techopedia.com/definition/4193/domain-controller-dc).  
&nbsp;

- The Central Store root path (containing the ADMX files):
  _\\\%LogonServer%\sysvol\\**#DomainName#**\Policies\PolicyDefinitions_

![](https://dennisspan.com/wp-content/uploads/2017/07/Deep-dive-automating-and-configuring-Google-Chrome-Group-Policy-Central-Store.jpg)

&nbsp;

The ADMX files are put in the root of the Store; the language files (**.ADML*), are put in the language-specific subdirectories.

- Central Store subdirectories for the language files:
  _\\\%LogonServer%\sysvol\\**#DomainName#**\Policies\PolicyDefinitions\\**#languagecode-countrycode#**_

Copy the Chrome ADMX files into this folder:

![](https://dennisspan.com/wp-content/uploads/2017/07/Deep-dive-automating-and-configuring-Google-Chrome-Group-Policy-Central-Store-ADMX-files.jpg)

&nbsp;

Copy the English language *.ADML* files into the en-US folder:

![](https://dennisspan.com/wp-content/uploads/2017/07/Deep-dive-automating-and-configuring-Google-Chrome-Group-Policy-Central-Store-ADML-files.jpg)

&nbsp;

!!! note "Note"
    The 2021 updates of {{ product_name }} also include support for several more languages; make sure to copy non-English ADML files for the supported language(s) you will use into their corresponding directories. The [correct directory name for your language](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/available-language-packs-for-windows) can be found in *Configuration\admx* of the unarchived [Chrome Enterprise Bundle](https://cloud.google.com/chrome-enterprise/browser/download/#download)

&nbsp;

Now that you have copied all required files, you can start configuring your settings using a Group Policy editor (such as [Group Policy Management Console](https://docs.microsoft.com/en-us/internet-explorer/ie11-deploy-guide/group-policy-and-group-policy-mgmt-console-ie11)).

In case you do not want to update your Central Store right away, you can first perform some tests by using the local ADMX repository on a server. The local repository of a Windows server is located here: *C:\Windows\PolicyDefinitions*. Apply the same procedure for copying the ADMX and ADML files as for the Central Store. Use the local Group Policy editor to configure your settings (*gpedit.msc*).

!!! warning "Important"
    The future versions of Chrome will feature updated .ADMX and .ADML files included into [Chrome Enterprise Bundle](https://cloud.google.com/chrome-enterprise/browser/download/). Please remember that your Group Policy settings are **not** affected when you update the .ADMX files. Your settings are kept in different files within each individual Group Policy itself: **Registry.pol** contains the Group Policy settings; ***.xml** (e.g. *Files.xml*) contains your Group Policy preferences settings

The path to an individual group policy is as follows:
 \\\%LogonServer%\sysvol\\**#DomainName#**\Policies\\**#PolicyGUID#**

&nbsp;

After configuring your Chrome settings you can check if your Chrome policies are applied by entering *chrome://policy* in Chrome address bar. This will show you all Chrome settings applied for your PC and user.

<p><img src="https://dennisspan.com/wp-content/uploads/2017/07/Deep-dive-automating-and-configuring-Google-Chrome-Chrome-applied-policy-overview.jpg" class="minimized">
</p>

&nbsp;

User settings can be either mandatory or recommended. Mandatory user settings are configured here:  

*User Configuration \ Administrative Templates \ Google \ Google Chrome*  

Recommended user settings are configured here:  

*User Configuration \ Administrative Templates \ Google \ Google Chrome - Default Settings (users can override)*  

On the local server or client, Chrome's computer and user policies are stored in the following [registry keys](https://www.wikihow.com/Use-Regedit):

- *HKEY_CURRENT_USER \ SOFTWARE \ Policies \ Google \ Chrome*
- *HKEY_LOCAL_MACHINE \ SOFTWARE \ Policies \ Google \ Chrome*

&nbsp;

**2\.** To force-install {{ short_name }} for Salesforce and Gmail Chrome Extension, open your [Group Policy Management Console](https://docs.microsoft.com/en-us/internet-explorer/ie11-deploy-guide/group-policy-and-group-policy-mgmt-console-ie11) (dsa.msc) and go to **User Configuration > Administrative Templates > Google > Google Chrome > Extensions**. Fine the setting *Configure the list of force-installed apps and extensions* and enable it.

![](https://dennisspan.com/wp-content/uploads/2017/09/Deploying-Google-Chrome-extensions-using-Group-Policy-Group-Policy-enable-extensions.jpg)

&nbsp;

Click **Show** and enter the string we provided at the beginning of the article into the Value field:

````agfekjndkedoakoeahndfnjilkifbicn;https://clients2.google.com/service/update2/crx````

![](https://dennisspan.com/wp-content/uploads/2017/09/Deploying-Google-Chrome-extensions-using-Group-Policy-Group-Policy-configure-extensions.jpg)

&nbsp;

Now the policy setting is configured. On the next Group Policy refresh the users will automatically get the required extension. To summarize, this policy update will mass-deploy the Extension for all users to whom the Group Policy applies. Extension installation is performed silently, without user interaction.

As mentioned above, after the Extension has been mass-deployed, you can see it in the directory on the users' PCs   *C:\Users\%UserName%\AppData\Local\Google\Chrome\User Data\Default\Extensions*

&nbsp;!!! note "Note"
    Make sure that *Developer mode* is disabled on the Extensions tab of users' Chrome browsers. During the tests, Extensions were not automatically installed with Developer mode enabled

&nbsp;

### Extension removal

If you delete the Extension from the *Configure the list of force-installed apps and extensions* policy setting, the extension is automatically removed from Chrome browser for all users to whom the Group Policy applies.

Future updates of the {{ short_name }} for Salesforce and Gmail Extension are automatically installed through the update URL specified in the Extension's manifest file (https://clients2.google.com/service/update2/crx).

&nbsp;

### {{ short_name }} Extension log on after deployment

After the Extension was deployed, the end users should log on to {{ product_name }} individually via the Extension's [Sidebar](../Introduction/) – see [this article](../How-to-Set-Up-the-Chrome-Extension-for-Salesforce-and-Gmail/#2_sign_in_to_gmail_and_grant_smartcloud_connect_permission_to_work_with_your_gmail_and_google_calendar_data) for more information.



&#160;
 &#160;

