# How to Resolve the "This add-in has been disabled to help keep you safe" Error


&nbsp;

The issue manifests in the following manner: you see the following notification on SSI Add-In opening in [MS Outlook on the Web](https://en.wikipedia.org/wiki/Outlook_on_the_web) for MS Exchange On Premises, e.g. *outlook.office.com*, and cannot proceed.

Opening SSI Add-in in Outlook on the Web results in the following error message:

*This add-in has been disabled to help keep you safe. To continue using the  add-in, validate that this item is hosted in a trusted domain or open it in the Office desktop app.*

![](..\assets\images\Troubleshooting\addin-keep-safe.png)

&nbsp;

This error is caused by a security update implemented by Microsoft.

To resolve the issue:  

Update your MS Exchange mail server with the latest Security Updates that were released after October 13, 2020. All later updates include the changes required for the Add-In to start normally.  

See [this Microsoft article](
https://support.microsoft.com/en-us/help/4581424/description-of-the-security-update-for-exchange-server-october-2020) for more information.



&nbsp;

&nbsp;

*Also see the following articles:*  

["Need Admin Approval" troubleshooting](../Need-Admin-Approval/)

[Microsoft Consent framework](https://docs.microsoft.com/en-us/azure/active-directory/develop/consent-framework)  

[Microsoft App Consent Experience](https://docs.microsoft.com/en-us/azure/active-directory/develop/application-consent-experience)  



&nbsp;

&nbsp;
