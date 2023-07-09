---
description: Learn how to resolve the "This add-in has been disabled to help keep you safe" error
---
# How to Resolve the *This add-in has been disabled to help keep you safe* Error  


<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*1 min read* 

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div> 
<!-- End ShareThis --> 

&nbsp;

The issue manifests in the following manner: you see the following notification on {{ short_name }} Add-In opening in [MS Outlook on the Web](https://en.wikipedia.org/wiki/Outlook_on_the_web) for MS Exchange On Premises, e.g. *outlook.office.com*, and cannot proceed.

Opening {{ product_name }} Add-in in Outlook on the Web results in the following error message:

*This add-in has been disabled to help keep you safe. To continue using the  add-in, validate that this item is hosted in a trusted domain or open it in the Office desktop app.*

<p>
    <img src="../../assets/images/Install-and-Run/addin-keep-safe.png" class="minimized">
</p>

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

[{{ product_name }} mass deployment scenarios](../Email-Integration-Full-Deployment-Scenarios/)

[How {{ product_name }} works with EWS](../Working-With-EWS/)

[Microsoft Consent framework](https://docs.microsoft.com/en-us/azure/active-directory/develop/consent-framework)  

[Microsoft App Consent Experience](https://docs.microsoft.com/en-us/azure/active-directory/develop/application-consent-experience)  



&nbsp;

&nbsp;


