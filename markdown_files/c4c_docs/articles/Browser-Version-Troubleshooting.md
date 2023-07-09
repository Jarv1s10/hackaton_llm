# How to Resolve the "Browser version is not supported" Error



&nbsp;

The issue manifests in the following manner: you see the following notification on SSI Add-In opening in MS Outlook and cannot proceed. The issue may occur in Windows 8, Windows 8.1, Windows 10

*Sorry, we couldn't load the app because your browser version is not supported. Click here for a list of supported browser versions.*

![](..\assets\images\Troubleshooting\browser-version.png)

&nbsp;

The error is caused by MS Outlook Add-Ins rendering general requirements.

To resolve the issue, follow the steps below:  

**1\.** Determine what browser is used by your MS Outlook to render Add-Ins, as described in [this Microsoft article](https://docs.microsoft.com/en-us/office/dev/add-ins/concepts/browsers-used-by-office-web-add-ins)   

**2\.** Make sure the required browser is installed. For example, if you had Internet Explorer uninstalled you can restore it through **Control Panel** -> **Programs** -> **Programs and Features**  -> **Turn Windows Features on and off** -> check the box **Internet Explorer 11** and click OK  -> restart your Windows  
Or, if Microsoft Edge is required, follow [this link](https://www.microsoft.com/en-ca/windows/microsoft-edge) to install it.  

**3\.** Make sure the required browser is updated. See [this Microsoft article](https://support.microsoft.com/en-ca/help/4028118/windows-run-the-latest-version-of-internet-explorer-11) to lean how to update Internet Explorer 11.  

**4\.** If installing and updating the required browser does not help, repair your MS Office installation as described in [this Microsoft article](https://support.microsoft.com/en-us/office/repair-an-office-application-7821d4b6-7c1d-4205-aa0e-a6b40c5bb88b?ocmsassetid=ha010357402&correlationid=4f778651-f3e5-454e-bdd7-d4d0816784a0&ui=en-us&rs=en-us&ad=us), restart your Windows and check if the issue persists



&nbsp;

&nbsp;

*Also see the following articles:*  

["Need Admin Approval" troubleshooting](../Need-Admin-Approval/)


[Microsoft Consent framework](https://docs.microsoft.com/en-us/azure/active-directory/develop/consent-framework)  

[Microsoft App Consent Experience](https://docs.microsoft.com/en-us/azure/active-directory/develop/application-consent-experience)  



&nbsp;

&nbsp;