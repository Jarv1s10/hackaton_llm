---
description: How to manage licenses for users in your org
---
# Managing Licenses for the Users  
  

<i>For users of the Email Sidebar on:</i><br><br>
<span style="color: #e74125;font-size: 17px;font-weight: 700;line-height: 30px;padding: 0px 10px;outline: none;border-radius: 2px;text-decoration: none;background-color: #fff;display: inline-block;border: 0px solid #000;transition: .3s all;width: auto;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="display: inline-block;vertical-align: middle;height: 32px;object-fit: contain;"></span><span style="color: #e74125;font-size: 17px;font-weight: 700;line-height: 30px;padding: 0px 10px;outline: none;border-radius: 2px;text-decoration: none;background-color: #fff;display: inline-block;border: 0px solid #000;transition: .3s all;width: auto;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="display: inline-block;vertical-align: middle;height: 32px;object-fit: contain;"></span><span style="color: #e74125;font-size: 17px;font-weight: 700;line-height: 30px;padding: 0px 10px;outline: none;border-radius: 0px;text-decoration: none;background-color: #fff;display: inline-block;border: 0px solid #000;transition: .3s all;width: auto;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="display: inline-block;vertical-align: middle;height: 32px;object-fit: contain;"></span> 

&nbsp;

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

To use {{ product_name }} Admin panel, special access permissions are required. To request the permissions for your organization, [contact {{ company_name }} support team by email](mailto:support@revenuegrid.com). Admin panel provides tools for managing end users and some of its key settings it includes duplicate {{ product_name }} [Customization](../Customization-Settings-Explained/) and [Sync](../Configuring-Activities-Synchronization-Settings/) settings on Admin level

&nbsp;

## Managing Licenses in the new Admin Panel

!!! warning "Important"
    In March 2023 release, the new Admin Panel was introduced. The support of the old Admin Panel will be ceased soon, thus we strongly encourage that our customers switch to the new Admin Panel.

&nbsp;

Managing Licenses (previously known as *Plans*) is only available to assigned {{ short_company_name }} Administrators; to access these actions you first need to [log in to the Administration Panel](../How-to-Log-In-to-the-Admin-Panel/), and then select the **Licenses** tab under Administration on the left-hand side panel.

<img src="..\..\assets\images\new-admin-panel\licenses\licenses.png" class="minimized">
&nbsp;

Different **Licenses** are provided for different user groups and include specific settings (e.g., the sync interval in seconds) for different synchronization customization sets.

A License can be assigned to the user on user creation. Later the assigned License can be changed when editing the User, see the [article on Managing Users](../Managing-Users-via-the-Solution-s-Admin-Panel/).


!!! note "Note"
    No modifications are possible on the Licenses tab, there you can only view Licenses details


<br><br>

### **Licenses List View**

On the **Licenses** tab, you can view the following columns:
<img src="..\..\assets\images\new-admin-panel\licenses\columns.png">
<br>

• **Name**. Displays a list of existing plans and their names

• **External ID**. Displays External Ids of Plans

• **Synchronization Interval** (in seconds). The standard synchronization interval is 30 minutes, and incremental synchronization is expected to last about 30 seconds per user. Sync interval cannot be adjusted by regular Users. If you need to have your sync interval changed, please consult us to [our Support team](mailto:support@revenuegrid.com)  

• **Active**. Displays the status of Plans that can be set true or false

• **Description**. Displays descriptions of Plans


&nbsp;

You can sort the table by each column's value. Click on the column name to sort ascending or sort descending.

<br>

<img src="..\..\assets\images\new-admin-panel\licenses\filter.png" style="width:40%; display:inline-block; vertical-align:middle; margin-left:10px; float: right">
In the **Filter by** box, you can select what licenses to display – active or inactive. Click on the X icon to clear the filter.

<br><br><br>


<img src="..\..\assets\images\new-admin-panel\licenses\columns-filter.png" style="width:40%; display:inline-block; vertical-align:middle; margin-left:10px; float: right">

Click the <img src="..\..\assets\images\new-admin-panel\licenses\tune-normal.svg" style="display:inline-block; vertical-align:middle; margin:1px; object-fit:contain;"> icon on the right to add or remove columns displayed on the Licenses tab.

<br><br><br><br><br>

<img src="..\..\assets\images\new-admin-panel\licenses\search.png" style="width:40%; display:inline-block; vertical-align:middle; margin-left:10px; float: right">
Use search box to quickly find the license you need.

<br><br>

!!! note "Note"
    No bulk actions with Licenses are supported. However, Licenses parameters can be exported to/imported from a file


<br>
<hr>
<br>

## Manage Plans in the legacy Admin Panel

!!! warning "Important"
    In March 2023 release, the new Admin Panel was introduced. The support of the legacy Admin Panel will be ceased soon, thus we strongly encourage that our customers switch to the new Admin Panel.
<br>

!!! warning "Important"
    To use {{ product_name }} Admin panel, special access permissions are required. To request the permissions for your organization, [contact {{ company_name }} support team by email](mailto:support@revenuegrid.com). Admin panel provides tools for managing end users and some of its key settings it includes duplicate {{ product_name }} [Customization](../Customization-Settings-Explained/) and [Sync](../Configuring-Activities-Synchronization-Settings/) settings on Admin level

Managing Plans is only available to assigned {{ product_name }} Administrators; to access these actions you first need to [log in to the Administration Panel](../How-to-Log-In-to-the-Admin-Panel/), and then select the **Plans** tab on the panel.

Different **Plans** are provided for different user groups and include specific settings (e.g., the sync interval in seconds) for different synchronization customization sets.

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b39fd1b0428630abc0b9f99.png" class="minimized">
</p>

&nbsp;

!!! note "Note"
    No modifications are possible on the Plans tab, there you can only view Plan details

A Plan can be assigned to the user on user creation. Later the assigned Plan can be changed when editing the User, see the [article on Managing Users](../Managing-Users-via-the-Solution-s-Admin-Panel/).

#### **Plans List View**

On the **Plans** tab, you can view the following fields:

• **ID**. The column is hidden by default

• **Name**. Displays a list of existing plans and their names

• **External ID**. Displays External Ids of Plans

• **Synchronization Interval In Seconds**. The standard synchronization interval is 30 minutes, and incremental synchronization is expected to last about 30 seconds per user. Sync interval cannot be adjusted by regular Users. If you need to have your sync interval changed, please consult us to [our Support team](mailto:support@revenuegrid.com)  

• **Active**. Displays the status of Plans that can be set true or false

• **Description**. Displays descriptions of Plans

A filter by each column can be applied to the list. To do that, click the **Expand more** icon next to a column name and select the action you need:

• **Sort Ascending**

• **Sort Descending**

• **Remove Sort**

• **Hide Column**

Click the ☰ (**Menu**) icon on the right to add or remove columns; you can also clear all filters by selecting the **Clear All Filters** item in this menu.

!!! note "Note"
    No bulk actions with Plans are supported. However, Plans parameters can be exported to/imported from a file



&#160;
 &#160;

