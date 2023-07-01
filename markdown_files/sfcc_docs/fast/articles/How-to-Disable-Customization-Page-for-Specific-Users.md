---
description: Learn how to revoke access to Customization page for specific users in your organization
---
# How to Disable Customization Page Access for Specific Users  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! warning "Important"
    To use {{ product_name }} Admin panel, special access permissions are required. To request the permissions for your organization, [contact {{ company_name }} support team by email](mailto:support@revenuegrid.com). Admin panel provides tools for managing end users and some of its key settings it includes duplicate {{ product_name }} [Customization](../Customization-Settings-Explained/) and [Sync](../Configuring-Activities-Synchronization-Settings/) settings on Admin level

This procedure duplicates the **Allow customization management** setting from among the [Special settings](../Special-Admin-Panel-Settings/).

To revoke access to [Customization](../How-to-Disable-Customization-Page-for-Specific-Users/) page for specific users in an organization, [log in to Administration panel](../How-to-Log-In-to-the-Admin-Panel/)  and do the following: 

**1\.** Go to the **Organizations** tab and select the necessary organization from the list

**2\.** On selected organization’s page, go to the  **Settings** tab and click **New**

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5be9a5732c7d3a31944dd9b3.png)

&nbsp;

**3\.** Add the  **ServiceAddInDisableCustomization **setting from the list

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5be9a5d404286304a71c272b.png)

&nbsp;

**4\.** In the **Add a New Setting** area that appears, assign the **ServiceAddInDisableCustomization **value to “1”

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5be9a61e04286304a71c272f.png)
&nbsp;
**5\.** Select  **Allow **from the picklist on the right to allow overrides

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5be9a7702c7d3a31944dd9db.png)

**6\.** Click the **Save** icon to save changes  

&nbsp;

* * *

&nbsp;

### Granting Access to [Customization Settings Page](../Customization-Settings-Explained/) for Specific Users

To grant access to certain users within the organization, do the following: 

**1\.** Select the user from the  **Users** tab on the **Organization**’s page  

**2\.** On the  **Settings** tab, click **New**

**3\.** Add the **ServiceAddInDisableCustomization** setting from the picklist:

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5be9a7902c7d3a31944dd9df.png)

&nbsp;

**4\.** In the  **Add a New Setting** area that appears, assign the **ServiceAddInDisableCustomization **value to “0”

**5\.** Click the **Save** icon to save changes

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5be9a7a52c7d3a31944dd9e0.png)

&nbsp;

As a result, the selected user will be able to access the **Customization settings** page, while other users within the same organization will not.

!!! warning "Important"
    Please note that after you change the customization access setting, for the change to be applied the user must [log out](../How-to-Change-Email-Address-in-Your-Product-Account-Office-365/) from one's {{ product_name }} account and then [re-log in](../How-to-Install-and-Run-the-Solution-all-configurations/#ii_rg_email_sidebar_logon)

&#160;
 &#160;

