---
description: Step-by-step instruction on how to resolve the "Browser version is not supported" error
---
# How to Resolve the *Browser Version Is Not Supported* Error  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>
&nbsp;

*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

The issue manifests in the following manner: you see the following notification on {{ short_name }} Add-In opening in MS Outlook and cannot proceed. The issue may occur in Windows 8, Windows 8.1, Windows 10

*Sorry, we couldn't load the app because your browser version is not supported. Click here for a list of supported browser versions.*

<p>
    <img src="../../assets/images/Install-and-Run/browser-version.png">
</p>

&nbsp;

The error is caused by MS Outlook Add-Ins rendering general requirements.

To resolve the issue, follow the steps below:  

**1\.** Determine what browser is used by your MS Outlook to render Add-Ins, as described in [this Microsoft article](https://docs.microsoft.com/en-us/office/dev/add-ins/concepts/browsers-used-by-office-web-add-ins)   

**2\.** Make sure the required browser is installed. For example, if you had Internet Explorer uninstalled you can restore it through **Control Panel** -> **Programs** -> **Programs and Features**  -> **Turn Windows Features on and off** -> check the box **Internet Explorer 11** and click OK  -> restart your Windows  
Or, if Microsoft Edge is required, follow [this link](https://www.microsoft.com/en-ca/windows/microsoft-edge) to install it  

**3\.** Make sure the required browser is updated. See [this Microsoft article](https://support.microsoft.com/en-ca/help/4028118/windows-run-the-latest-version-of-internet-explorer-11) to lean how to update Internet Explorer 11  

**4\.** If installing and updating the required browser does not help, repair your MS Office installation as described in [this Microsoft article](https://support.microsoft.com/en-us/office/repair-an-office-application-7821d4b6-7c1d-4205-aa0e-a6b40c5bb88b?ocmsassetid=ha010357402&correlationid=4f778651-f3e5-454e-bdd7-d4d0816784a0&ui=en-us&rs=en-us&ad=us), restart your Windows and check if the issue persists



&nbsp;

&nbsp;

*Also see the following articles:*  

["Need Admin Approval" troubleshooting](../Need-Admin-Approval/)

[{{ product_name }} mass deployment scenarios](../Email-Integration-Full-Deployment-Scenarios/)

[How {{ product_name }} works with EWS](../Working-With-EWS/)

[Microsoft Consent framework](https://docs.microsoft.com/en-us/azure/active-directory/develop/consent-framework)  

[Microsoft App Consent Experience](https://docs.microsoft.com/en-us/azure/active-directory/develop/application-consent-experience)  



&nbsp;

&nbsp;


