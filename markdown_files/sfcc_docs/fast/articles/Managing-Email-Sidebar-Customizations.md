---
description: Learn how to push and retrieve customizations to and from your colleagues 
---
# Managing Email Sidebar Customizations  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*5 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

As a {{ product_name }} Admin or user with special permissions, apart from being able to [set up your own customization](../Customization-Settings-Explained/), you can push and retrieve customizations to and from your colleagues. You can push customizations individually or to all {{ product_name }} users in your Salesforce Org.

!!! warning "Important"
    please note that in the latest {{ product_name }} updates customization settings can also be exported to / imported from a _.json_ file. To do that, open [Customization page](../Customization-Settings-Explained/) and click **More**▼ at the top of the page, then select **Import from a file** or **Export to a file**

&nbsp;

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5be03dde2c7d3a01757acad4.png" class="minimized">
</p>

&nbsp;

The older approach which is recommended for {{ product_name }} [mass deployment](../Mass-Deployment-of-the-Add-In-Office-365/) and administration, is pushing/retrieving the settings directly from user to user.

&nbsp;

### Pushing your customization to other users in your Salesforce org

To push your customization to your colleagues, do the following:

**1\.** Click the **Menu** button on the home screen and then click **Customization**

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b080fce0428635ba8b2bd6e.png)

&nbsp;

**2\.** On the **Customization** page, click **Share my customization settings with colleagues**

**3\.** By default, the  **Share my customization settings with colleagues** screen displays all [Salesforce users](https://help.salesforce.com/articleView?id=admin_userprofiles.htm&type=5) that are visible to you based on your permissions. Select the **Only users of {{ product_name }}** checkbox to only display users who logged in to {{ product_name }} with their Salesforce credentials (or users who received a pushed customization at least once)

!!! note "Note"
    Save your customization before pushing it to other users. If you modified your customization without saving it, these changes will not be reflected in the recipient’s Add-In / Chrome Extension

&nbsp;

**4\.** Use the search box to filter by Salesforce User Profiles or by name   

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b0810122c7d3a2f9011eabd.png)

&nbsp;

**5\.** Select the user(s) you want to push your customization to from the list. Tick the **Select all** checkbox to choose all users on the list

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b0810360428635ba8b2bd72.png)

&nbsp;

!!! tip "Tip"
    You can also apply filters to define which users to export a customization to, using to user name, email address, or profile type

&nbsp;

**6\.** Click the button **{Number} Selected users** to push your customization to selected users.
or, to push your customization to all users in your Salesforce org, click **All users in Salesforce org**

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b0810722c7d3a2f9011eac2.png)

&nbsp;

**8\.** Now {{ product_name }} will schedule a customization pushing job. The wait time depends on server load and on the number of users getting the customization and it may take long

!!! tip "Tip"
    You can close the Customization settings window after initiating a customization push, the pushing will be running in the background on server side and you will receive an email notification when it is complete, and the customization recipient(s) will receive a notification in their {{ product_name }} Add-In / Chrome Extension and will be asked to restart Outlook. After Outlook restart, the pushed customization will be fully applied to their Add-In / Chrome Extension

&nbsp; 

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b100a0a0428632c466a6296.png)

&nbsp;

* * *
&nbsp;

### Retrieving a pushed customization

To retrieve existing customizations from your colleagues, do the following:

**1\.** On the **Customization** page, click **Get customization settings from a colleague**  

**2\.** Select the **Only users of {{ product_name }}** checkbox to only view Salesforce users with {{ product_name }} accounts (or users who received a pushed customization at least once)  

**3\.** Use the search box to filter by Salesforce user types or by name or select the user from the list  

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b0810fc0428635ba8b2bd79.png)
&nbsp;

**4\.** Click on a user to retrieve their customization  

!!! note "Note"
    We recommend saving your customization in its current state before retrieving your colleague’s settings - that way you will be able to discard all changes and revert back to your original customization If you accidentally selected a wrong user or if the customization does not suit your needs

&nbsp;

**5\.** Wait while {{ product_name }} updates the settings   

**6\.** Click **Save** in the top-right corner of the page to apply changes  

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b0811390428635ba8b2bd7d.png)

&nbsp;

**7\.** To discard any changes made to your customization, click **Discard changes** _before_ saving. Once the customization is saved, you can only reset to default customization settings  

Once the synchronization is complete, restart Outlook to view the changes.

!!! note "Note"
    Retrieving customizations is not an ongoing process - any further changes the exporter makes to their customization settings will not be reflected in the importer's {{ product_name }} Add-In / Chrome Extension, that is, customization gets imported in its current state and it will not be updated automatically. To use the updated customization, the importer must retrieve it from the **Get customization settings from my colleague** dialog once more

&nbsp;
&nbsp;

### Default Customization Settings

If you have changed some of the above described settings and the resulting Add-In / Chrome Extension behavior does not meet your preferences, you can always revert to the default behavior by clicking the button **Reset to default settings** at the top of Customization page. The default set of settings is defined specifically for your {{ product_name }} implementation by [{{ company_name }}](mailto:support@revenuegrid.com) and [the local Admin](../Special-Admin-Panel-Settings/); during a reset all object-specific and Add-In / Chrome Extension behavior settings are reverted to their default values. User-specified settings can be backed up and recovered from another user in the same organization using the mechanisms described in the above section of this article.  
Also note that the local {{ short_name }} Admin may reset customization settings to default for a group of users. See [this article](../Managing-Users-via-the-Solution-s-Admin-Panel/#actions_with_users) to learn how.

!!! warning "Important"
    After resetting to default settings, make sure to click the **Save** button in the upper right corner of the customization settings window to apply it. Otherwise the retrieved default settings will **not** be applied

&nbsp;

#### Configuring the Default (Initial) Customization

In the latest {{ product_name }} updates the default (initial) set of customization settings can be defined by [the local Admin](../How-to-Log-In-to-the-Admin-Panel/), to be applied right after the Solution is installed or after customization is reset to default by clicking the **Reset to default  settings** button in [Customization page](../Customization-Settings-Explained/) header. This feature enables  quick uniform management of settings for different user categories and  facilitates restoring product functioning after unwanted adjustments  were made in the settings.



&#160;
 &#160;

