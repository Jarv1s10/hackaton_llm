---
description: Learn how to handle the issue when the Revenue Grid Managed Package for Salesforce installation failed
---

# Managed Package Installation Failed with the *This Package Can't be Installed* Error

*1 min read*

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

While installing the [{{ company_name }} Managed Package](../Admin-Managed-Package/), you may face the issue when you are redirected to the installation status page or receive an email notification with the following error details:

*(Update_Custom_Setting-8) get_tenant_url (Action) – We can't find an action with the name and action type that you specified*

&nbsp;

<details><summary> >>> Click to see screenshots <<< </summary>
<br>
<p><b>Installation status page</b>
<img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\managed-package-installation-failed\1.png">
</p>
<br>
<br>
<br>
<p><b>Email notification</b>
<img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\managed-package-installation-failed\2.png">
</p>
</details>


&nbsp;

This problem occurs on installing the managed package to [**Salesforce Professional Edition**](https://help.salesforce.com/s/articleView?id=sf.overview_edition.htm&type=5). This Salesforce edition does not include the [**Web Services API** component](https://www.salesforce.com/content/dam/web/en_us/www/documents/pricing/DS_SalesCloud_EdCompare.pdf) that is necessary for the {{ company_name }} Solution to make the callout and populate the custom setting automatically. However, this component can be enabled by Salesforce for an additional fee.

&nbsp;

***

&nbsp;

## How to handle the issue

To handle the problem, make sure that you are using the Salesforce Professional Edition. Refer to [this Salesforce Help article](https://help.salesforce.com/s/articleView?id=sf.overview_finding_edition.htm&type=5) to find out which edition you are using.

The {{ company_name }} Managed Package can operate without the **Web Services API** component, therefore, a separate managed package version was explicitly developed for Salesforce Professional Edition users.

&nbsp;

**You can get the latest version of the managed package for Salesforce Professional Edition here:**  
<https://login.salesforce.com/packaging/installPackage.apexp?p0=04t1P0000006KNH>

&nbsp;

***

&nbsp;

## If the issue still persist

If the installation of the managed package version for Salesforce Professional Edition failed too, the problem requires additional investigation by our [support team](mailto:support@revenuegrid.com). The support team may ask you to check and provide the following details:

* [Check the Salesforce edition](https://help.salesforce.com/s/articleView?id=sf.overview_finding_edition.htm&type=5) you are using

* Try to run the managed package installation using the **System Administrator** profile user

* Go to **Setup** > **Deployment Status: View Details** page and check additional details of the unsuccessful installation attempt

&nbsp;

&nbsp;