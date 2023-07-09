---
description: Learn how to manage users via the Solution's Admin Panel
---
# Managing Users via the Solution's Admin Panel  
  

<i>For users of the Email Sidebar on:</i><br><br>
<span style="color: #e74125;font-size: 17px;font-weight: 700;line-height: 30px;padding: 0px 10px;outline: none;border-radius: 2px;text-decoration: none;background-color: #fff;display: inline-block;border: 0px solid #000;transition: .3s all;width: auto;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="display: inline-block;vertical-align: middle;height: 32px;object-fit: contain;"></span><span style="color: #e74125;font-size: 17px;font-weight: 700;line-height: 30px;padding: 0px 10px;outline: none;border-radius: 2px;text-decoration: none;background-color: #fff;display: inline-block;border: 0px solid #000;transition: .3s all;width: auto;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="display: inline-block;vertical-align: middle;height: 32px;object-fit: contain;"></span><span style="color: #e74125;font-size: 17px;font-weight: 700;line-height: 30px;padding: 0px 10px;outline: none;border-radius: 0px;text-decoration: none;background-color: #fff;display: inline-block;border: 0px solid #000;transition: .3s all;width: auto;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="display: inline-block;vertical-align: middle;height: 32px;object-fit: contain;"></span> 

&nbsp;

*9 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! warning "Important"
    In March 2023 release, the new Admin Panel was introduced. The support of the legacy Admin Panel will be ceased soon, thus we strongly encourage that our customers switch to the new Admin Panel. This article contains two sections:  
    • [Managing Users in the new Admin Panel](../Managing-Users-via-the-Solution-s-Admin-Panel/#managing_users_in_new_admin_panel)  
    • [Managing Users in the legacy Admin Panel](../Managing-Users-via-the-Solution-s-Admin-Panel/#managing_users_in_the_legacy_admin_panel)

To use {{ product_name }} Admin panel, special access permissions are required. To request the permissions for your organization, [contact {{ company_name }} support team by email](mailto:support@revenuegrid.com).  Admin panel provides tools for managing end users and some of its key settings it includes duplicate {{ product_name }} [Customization](../Customization-Settings-Explained/) and [Sync](../Configuring-Activities-Synchronization-Settings/) settings on Admin level

&nbsp;

## Managing Users in the new Admin Panel

&nbsp;

Managing users in only available to assigned {{ product_name }} Administrators; to access these settings and actions you first need to  [log in to Administration panel](../How-to-Log-In-to-the-Admin-Panel/).

&nbsp;

#### **Editing Users**

To edit a user:

**1\.** Go to the **Users** tab of the Administration Panel  

**2\.** In the users list, click the user you want to edit. The page with user details will appear

<img src="..\..\assets\images\new-admin-panel\users\user.png" class="minimized">

**3\.** Edit the necessary fields: **Name**, **Email**, **Profile**, **License**, **Description**, and other user settings, or view the necessary informaion: User ID, Synchronization Status, Effective Synchronization Status, Mailbox Status, Last synchronization session

**4\.** Click **Save**  

&nbsp;

* * *

&nbsp;

#### **Actions with Users**

To understand the actions you may perform on the **Users** tab, see the descriptions of User actions Menu items below. All these can be performed individually or in bulk for a group of selected {{ short_name }} users. Note the action *Install Sidebar*, it is handy to mass-install [MS Outlook Add-In](../Introduction/) after [{{ short_name }} Sync Engine was configured](../Authorizing-Sync-Engine-to-Work-with-Your-Data/).

To open the Actions menu, select any user and click on the three dots menu on the left. 

<p><img src="..\..\assets\images\new-admin-panel\users\actions.png" class="minimized">
</p>

!!! note "Note"
    If you don't see the Actions column, try scrolling the page to the right and check whether this column is selected for display.

**Delete**. Delete a user. Please note that Users with initialized mailbox cannot be deleted

**Force delete**. Delete a user, users with initialized mailbox can be deleted this way

**Reset mailbox**. Request {{ product_name }} to remove user customization and keep synchronization disabled. Once synchronization is enabled again, the first synchronization attempt will apply the customization to the user’s mailbox

**Re-initialize mailbox**. Request {{ product_name }} to refresh mailbox data access for the user. Re-initializing is performed to resolve errors which affected data parsing consistency in the mailbox

**Check settings**. Use this action allows to verify if the Sync Engine is properly set up and to jump start it after fixing errors

**Check CRM connectivity**.  the connection to Salesforce tenant under these user credentials can be established

**Check mailbox connectivity**. the connection to Exchange under this user credentials can be established

**Enable synchronization**. Enable synchronization for a User, if it was disabled

**Disable synchronization**. Suspend synchronization for a user. If synchronization is suspended for an ordinary User, it can be resumed from the Sync Dashboard

**Force synchronization**. Standard synchronization interval is set to 30 minutes. A user can manually trigger synchronization outside of the standard sync schedule by clicking the Force Synchronization action, but no sooner than 1 minute after the last attempt to trigger it. This is done to avoid service overload in case of multiple consecutive “Force Synchronization” requests
		
**Install Sidebar**. Run this action to easily install {{ short_name }} Add-In for MS Outlook for the user's account. That is only viable if the Sync Engine was authorized to work with the user's mail server data

**Remove Sidebar**. Run this action to uninstall {{ short_name }} Add-In for MS Outlook from this user account

**Reset Sidebar customization**. Resets the user's Customization settings to the default state configured by the Admin or {{ short_name }} Support Team

&nbsp;

&nbsp;

#### Managing Users’ Sync Status

By default, synchronization is disabled for new added User accounts until the initial configuration is completed for them. In the list on the Users tab, admins can see users for whom sync is enabled or disabled by changing the sorting of the Synchronization status column.

!!! note "Note"
    Synchronization may also get [suspended automatically due to errors](../Handling-Sync-Issues/)

&nbsp;

You can change the sync status for several Users at the same time: select the corresponding checkboxes in the left-most column, then click the **three dots** icon in the upper right corner of the page and from the drop-down menu select **Enable Synchronization** or **Disable Synchronization**.

<p><img src="..\..\assets\images\new-admin-panel\users\bulk-actions.png" class="minimized">
</p>

&nbsp;

The corresponding notification (action successful or failed) will appear in the bottom left corner of the page.

<p><img src="..\..\assets\images\new-admin-panel\users\sync-enabled.png" style="width:40%;">
</p>

&nbsp;

!!! note "Note"
    If the sync status is disabled for an Profile, synchronization will not run for any of its users no matter what individual sync status they have

&nbsp;

All available mass actions:

* Reset mailbox
* Enable synchronization
* Disable synchronization
* Delete
* Force delete
* Change organization
* Change plan
* Reset sidebar customization

&nbsp;
<hr>
&nbsp;

### **Viewing User Subtabs**

You can view the tabs containing detailed information about a specific user when you click on the needed user's name on the list. The User details page will open.

The following tabs are shown on every User details page.

<br>

#### Connectivity

Displays email configuration set up for this user.

You can edit the user’s name and mailbox settings that were specified during the provisioning process or defined by the profile to which the user belongs.

<p><img src="..\..\assets\images\new-admin-panel\users\connectivity.png">
</p>

If Exchange Direct access is selected:

• You can change the login credentials for the user: SMTP email address, Exchange account name (can be different from SMTP email address), and password  

• With Office 365 authentication: 
    ◦ Cannot update or access User’s OAUTH2 tokens 
    ◦ Can change user back to login/password authentication scheme 
    ◦ Can delete a stored Refresh Token for Ordinary User 
    
    
If Exchange Impersonated access is selected:

• You can change only SMTP email address, as other parameters come through Org configuration
• Office 365 OAUTH scenario is also supported 
• Users are not allowed to change their SMTP email address (to prevent connecting to another user's mailbox) 

&nbsp;

#### All available Mailbox access types in Email Configuration

<p><img src="..\..\assets\images\new-admin-panel\users\mailbox-type.gif" style="width:70%">
</p>

&nbsp;

See [this article](../Managing-Organizations-via-the-Admin-Panel/#configuring_connection_type_for_an_organization) for complete information on each connection type.


<br><br>

#### Statistics

Displays the list of synchronization sessions of the selected user. To download a session’s log, click the Download Log icon in the Actions column

<p><img src="..\..\assets\images\new-admin-panel\users\statistics.png">
</p>


<br><br>

#### Sync Issues

Displays a list of issues from last synchronization session.

Synchronization issues are caused by modification operations from mail server storage to Salesforce or vice versa.

<p><img src="..\..\assets\images\new-admin-panel\users\sync-issues.png">
</p>

<br><br>

#### Activity</strong>
			
Displays system activities for the selected user.
<br>
For each activity, you can see the following information: 
			
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Date and time when the activity occurred 
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• An email address of the user that initiated the activity&nbsp; &nbsp;&nbsp; 
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• A type of the activity&nbsp; &nbsp;&nbsp; 
<br><br>
To download an activity-related log, in the **Actions** column, click on the Download icon.

To copy the activity-related details, in the **Details** column, click on the Copy icon.

<p><img src="..\..\assets\images\new-admin-panel\users\activity.png">
</p>


<br><br>
Possible activities are: 
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• User is added
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• User is removed
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• User synchronization is disabled
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• User synchronization is disabled due to authorization error
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• User synchronization is disabled due to throttling error
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• User synchronization is disabled due to other error
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• User synchronization is enabled
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• User Customization is reapplied
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• User Profile is changed
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• User Synchronization is disabled, Customization is uninstalled 
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• User License assigned event.
			

<br><br>

#### **Customization**

Displays the Sidebar customization settings for the selected user.

<p><img src="..\..\assets\images\new-admin-panel\users\customization.png">
</p>
<br><br>

#### **Defining Individual Synchronization Settings for a User or a Group of Users**

It is possible to push predefined synchronization settings to groups of users and individual users within an Org, or to all users of an Org; the users can be allowed or disallowed to adjust these settings. If you need to preset customized sync settings to different users in your Org, send us a corresponding request to [our Support team](mailto:support@revenuegrid.com)

&nbsp;

&nbsp;

#### **How to Get Users' Sync IDs**

To get a user's Sync ID, which is used in specific configuration scenarios and [API scenarios](https://docs.revenuegrid.com/ri/fast/articles/Lightning-Scheduler-API/):

<img src="..\..\assets\images\new-admin-panel\users\user-id.png" style="width:40%; display:inline-block; vertical-align:middle; margin-left:10px; float: right" class="minimized">

**1\.** On the Users tab, click on the needed user in the users list to open their details page  

**2\.** On the Details page, find the **User ID field** with an alphanumeric value

**3\.** Copy this value, it is the user Sync Id that you need

<br><br><br><br><br>

!!! tip "Tip"
    Alternatively, if the User ID field field is empty. After opening the User's Details page, see the URL in the address line of your browser. The link contains an alphanumeric value between the segments */users/* and */details*    
  
    For example, *4e8a3d12-fa32-4d92-9170-74cac44a1530*  <br> <img src="..\..\assets\images\new-admin-panel\users\user-id-url.png" class="minimized">


&nbsp;
<hr>

&nbsp;

#### **Moving Users Between Profiles**

Profile is assigned for each user during the provisioning process. Otherwise, Users are automatically assigned to the default Profile. You can also change the Profile to which Users are assigned later after provisioning is complete.

!!! note "Note"
    When assigning Users to other Profiles, be aware that the new Profile may use a different mailbox access type or Microsoft Exchange Server impersonation settings. As a result, {{ product_name }}'s ability to access the User's mailbox may be affected

&nbsp;

To assign a User to another Profile:   

<p><img src="..\..\assets\images\new-admin-panel\users\profile.png" style="width:40%; display:inline-block; vertical-align:middle; margin-left:10px; float: right" class="minimized">
</p>

**1\.** On the **Users** tab of the Administration Panel, click on the user you want to assign another Profile to

**2\.** On the **Details** page, select the Profile that you want to assign the User to

**3\.** Click **Save**  

&nbsp;

&nbsp;

<hr>
&nbsp;


#### How to delete users

To delete a user:  

**1\.** Go to the **Users**  tab of the Administration Panel  

**2\.** From the list of users, pick the user you want to delete and click the **Force delete** icon

<p><img src="..\..\assets\images\new-admin-panel\users\delete-users.png" class="minimized">
</p>

&nbsp;

**3\.**  In the confirmation dialog that appears, click **Delete**

<p><img src="..\..\assets\images\new-admin-panel\users\delete-conf.png" style="width:60%;">
</p>

&nbsp;

Once a User is deleted via the Administration Panel, they cannot access and use any {{ company_name }} product.
&nbsp;



<br>
<hr>
<br>

## Managing Users in the legacy Admin Panel

!!! warning "Important"
    In March 2023 release, the new Admin Panel was introduced. The support of the old Admin Panel will be ceased soon, thus we strongly encourage that our customers switch to the new Admin Panel.

!!! warning "Important"
    To use {{ product_name }} Admin panel, special access permissions are required. To request the permissions for your organization, [contact {{ company_name }} support team by email](mailto:support@revenuegrid.com).  Admin panel provides tools for managing end users and some of its key settings it includes duplicate {{ product_name }} [Customization](../Customization-Settings-Explained/) and [Sync](../Configuring-Activities-Synchronization-Settings/) settings on Admin level

&nbsp;

Managing users in only available to assigned {{ product_name }} Administrators; to access these settings and actions you first need to  [log in to Administration panel](../How-to-Log-In-to-the-Admin-Panel/).

&nbsp;

#### **Editing Users**

To edit a user:

**1\.** Go to the **Users** tab of the Administration Panel  

**2\.** In the users list, click the user you want to edit or the **Edit** icon next to the user. The page with user details will appear

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b30bc3e2c7d3a0fa9a36523.png" class="minimized">
</p>

**3\.** Edit the necessary fields: **Name**, **Organization**, **Plan**, or **E-Mail**  

**4\.** Click **Save**  

&nbsp;

* * *

&nbsp;

#### **Actions with Users**

To understand the actions you may perform in the **Users** tab, see the descriptions of User actions Menu items below. All these can be performed individually or in bulk for a group of selected {{ short_name }} users. Note the action *Install {{ product_name }} for Salesforce for Microsoft Outlook*, it is handy to mass-install [MS Outlook Add-In](../Introduction/) after [{{ short_name }} Sync Engine was configured](../Authorizing-Sync-Engine-to-Work-with-Your-Data/).

<details><summary> >>> Click to see how to open the Menu <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\actions-menu.png">
</p></details>



&nbsp;

<table class="table-bordered">
	<tbody>
	<tr>
		<td>
			<p>
				<img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b3f6da50428630abc0bc6a0.png" alt="" style="float: left; margin: 0px 10px 10px 0px;">
			</p>
		</td>
		<td>
			<strong>Edit User</strong>. Open and edit a User
		</td>
	</tr>
	<tr>
		<td>
			<p>
				<img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b30c64d2c7d3a0fa9a36596.png" alt="" style="float: left; margin: 0px 10px 10px 0px;">
			</p>
		</td>
		<td>
			<strong>Delete</strong>. Delete a User. Please note that Users with initialized mailbox cannot be deleted
		</td>
	</tr>
	<tr>
		<td>
		</td>
		<td>
			<strong>Force Delete</strong>. Delete a user, users with initialized mailbox can be deleted this way
		</td>
	</tr>
	<tr>
		<td>
			<p>
				<img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b3f6e042c7d3a099f2e3fb0.png" alt="" style="float: left; margin: 0px 10px 10px 0px;">
			</p>
		</td>
		<td>
			<strong>Enable Synchronization</strong>. Enable synchronization for a User, if it was disabled
		</td>
	</tr>
	<tr>
		<td>
			<p>
				<img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b3f6e232c7d3a099f2e3fb1.png" alt="" style="float: left; margin: 0px 10px 10px 0px;">
			</p>
		</td>
		<td>
			<strong>Disable Synchronization</strong>. Suspend synchronization for a user.&nbsp;If synchronization is suspended for an ordinary User, it can be resumed from the Sync Dashboard
		</td>
	</tr>
	<tr>
		<td>
			<p>
				<img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b3f6e552c7d3a099f2e3fb7.png" alt="" style="float: left; margin: 0px 10px 10px 0px;">
			</p>
		</td>
		<td>
			<strong>Force Synchronization</strong>. Standard synchronization interval is set to 30 minutes. A user can manually trigger synchronization outside of the standard sync schedule by clicking the Force Synchronization action, but no sooner than 1 minute after the last attempt to trigger it. This is done to avoid service overload in case of multiple consecutive “Force Synchronization” requests
		</td>
	</tr>
	<tr>
		<td>
			<p>
				<img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b3f6e682c7d3a099f2e3fb9.png" alt="" style="float: left; margin: 0px 10px 10px 0px;">
			</p>
		</td>
		<td>
			<strong>Reset Mailbox</strong>. Request {{ product_name }} to remove user customization and keep synchronization disabled.&nbsp;Once synchronization is enabled again, the first synchronization attempt will apply the customization to the user’s mailbox<br>
		</td>
	</tr>
	<tr>
		<td>
		</td>
		<td>
			<strong>Re-initialize User's Mailbox</strong>. Request {{ product_name }} to refresh mailbox data access for the user. Re-initializing is performed to resolve errors which affected&nbsp; data parsing consistency in the mailbox<br>
		</td>
	</tr>
    <tr>
		<td>
		</td>
		<td>
			<strong>Check Settings</strong>. Use this action allows to verify if the Sync Engine is properly set up and to jump start it after fixing errors<br>
		</td>
	</tr>    
	<tr>
		<td>
		</td>
		<td>
			<strong>Check CRM Connectivity</strong>. Read [this article]f the connection to Salesforce&nbsp;tenant under these user credentials can be established<br>
		</td>
	</tr>
	<tr>
		<td>
		</td>
		<td>
			<strong>Check Mailbox Connectivity</strong>. Read [this article]f the connection to Exchange under this user credentials can be established
		</td>
	</tr>
    	<tr>
		<td>
		</td>
		<td>
			<strong>Install {{ product_name }} for Salesforce for Microsoft Outlook</strong>. Run this action to easilt install {{ short_name }} Add-In for MS Outlook for the user's account. That is ony viable if the Sync Engine was authorized to work with the user's mail server data
		</td>
	</tr>    
    <tr>
		<td>
		</td>
		<td>
			<strong>Check Add-In Status</strong>. Run this action to find out if {{ short_name }} Add-In for MS Outlook is installed for this user account
		</td>
	</tr>  
    <tr>
		<td>
		</td>
		<td>
			<strong>Remove Add-In</strong>. Run this action to uninstall {{ short_name }} Add-In for MS Outlook from this user account
		</td>
	</tr>     
	<tr>
		<td>
		</td>
		<td>
			<strong>Reset Add-In Customization</strong>. Resets the user's Customization settings to the default state configured by the Admin or {{ short_name }} Support Team
		</td>
	</tr>
	</tbody>
	</table>


&nbsp;

&nbsp;

#### Managing Users’ Sync Status

By default, synchronization is disabled for new added User accounts until the initial configuration is completed for them. In the list on the Users tab, the Users for which sync is enabled are shown in black font color, while the Users for which it is disabled are shown in red font color.

!!! note "Note"
    Synchronization may also get [suspended automatically due to errors](../Handling-Sync-Issues/)

&nbsp;

You can change the sync status for several Users at the same time: mark the corresponding boxes in the left-most column, then click the **Settings** icon in the upper right corner of the page and from the drop-down menu select **Enable Synchronization** or **Disable Synchronization**.

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b3a189f0428630abc0ba04e.png)

&nbsp;

The corresponding notification (action successful or failed) will appear in the bottom left corner of the page.

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b3a18de2c7d3a0fa9a3aead.png)

&nbsp;

!!! note "Note"
    If the sync status is disabled for an Organization, synchronization will not run for any of its users no matter what individual sync status they have

&nbsp;

&nbsp;

#### **Viewing User Subtabs**

You can view the tabs containing detailed information about a specific user when you select the needed user from the list or click the **Edit** icon. The User details page will open.

The following tabs are shown on every User details page.

<table class="table-bordered">
	<tbody>
	<tr>
		<td>
			<p>
				<strong>Statistics </strong>
			</p>
			<p>
				<img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b30e0ec0428632c466b49c9.png">
			</p>
		</td>
		<td>
			<strong></strong>
			<p>
				 Displays the list of synchronization sessions of the selected user. To see more details, click the&nbsp;icon to open the job under&nbsp;Actions. A session description and details open on a new page. To download a session’s log, select the Download Log icon from the Actions
			</p>
		</td>
	</tr>
	<tr>
		<td>
			<strong>Issues</strong>
		</td>
		<td>
			 Displays a list of issues from last synchronization session 
			<br>
			 Synchronization issues are caused by modifications operations from Exchange Storage to Salesforce or vice versa 
			<br>
		</td>
	</tr>
	<tr>
		<td>
			<p>
				<strong>Activity</strong>
			</p>
		</td>
		<td>
			 Displays system activities for the selected user 
			<br>
			 For each activity, you can see the following information: 
			<br>
			 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Date and time when the activity occurred 
			<br>
			 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• An email address of the user that initiated the activity&nbsp; &nbsp;&nbsp; 
			<br>
			 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• A type of the activity&nbsp; &nbsp;&nbsp; 
			<br>
			 To download an activity-related log, under&nbsp;Actions, choose the appropriate icon. Possible activities are: 
			<br>
			 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Employee is Added&nbsp; &nbsp;&nbsp; 
			<br>
			 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Employee is Removed&nbsp; &nbsp;&nbsp; 
			<br>
			 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Employee Synchronization is Disabled&nbsp; &nbsp;&nbsp; 
			<br>
			 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Employee Synchronization is Disabled Due to Authorization Error&nbsp; &nbsp;&nbsp; 
			<br>
			 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Employee Synchronization is Disabled Due to Throttling Error&nbsp; &nbsp;&nbsp; 
			<br>
			 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Employee Synchronization is Disabled Due to Other Error&nbsp; &nbsp;&nbsp; 
			<br>
			 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Employee Synchronization is Enabled&nbsp; &nbsp;&nbsp; 
			<br>
			 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Employee Customization is Reapplied&nbsp; &nbsp;&nbsp; 
			<br>
			 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Employee Organization is Changed&nbsp; &nbsp;&nbsp; 
			<br>
			 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Employee Synchronization is Disabled, Customization is Uninstalled 
			<br>
			 &nbsp; &nbsp; &nbsp; &nbsp; •&nbsp;Employee Plan Assigned Event.&nbsp; &nbsp;&nbsp; 
			<br>
		</td>
	</tr>
	<tr>
		<td>
			<p>
				<strong>Salesforce Configuration </strong>
			</p>
		</td>
		<td>
			<strong></strong>
			<p>
				 Displays the field for Salesforce instance URL where you configure users’ access to Salesforce
			</p>
		</td>
	</tr>
	<tr>
		<td>
			<p>
				<strong>Email Configuration</strong>
			</p>
		</td>
		<td>
			 Displays email configuration set up for this user 
			<br>
			 You can edit the user’s name and mailbox settings that were specified during the provisioning process or defined by the organization to which the user belongs 
			<br>
			<strong>If Exchange Direct access is selected:</strong><br>
			 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • You can change the login credentials for the user: SMTP email address, Exchange account name (can be different from SMTP email address), and password 
			<br>
			 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • With Office 365 authentication: 
			<br>
			 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ◦&nbsp;Cannot update or access User’s OAUTH2 tokens 
			<br>
			 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ◦&nbsp;Can change user back to login/password authentication scheme 
			<br>
			 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ◦&nbsp;Can delete a stored Refresh Token for Ordinary User 
			<br>
			<strong>If Exchange Impersonated access is selected:</strong><br>
			 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• You can change only SMTP email address, as other parameters come through Org configuration&nbsp; &nbsp;&nbsp; 
			<br>
			 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Office 365 OAUTH scenario is also supported 
			<br>
			 &nbsp; &nbsp; &nbsp; &nbsp; • Users are not allowed to change their SMTP email address (to prevent connecting to another user's mailbox) 
			<br>
		</td>
	</tr>
	</tbody>
	</table>

&nbsp;

#### All available Mailbox access types in Email Configuration

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/mailbox-access.png" class="minimized">
</p>

&nbsp;

See [this article](../Managing-Organizations-via-the-Admin-Panel/#configuring_connection_type_for_an_organization) for complete information on each connection type.

&nbsp;

#### **Defining Individual Synchronization Settings for a User or a Group of Users**

In the latest {{ product_name }} updates it is possible to push pre-defined synchronization settings to groups of users and individual users within an Org, or to all users of an Org; the users can be allowed or disallowed to adjust these settings. If you need to preset customized sync settings to different users in your Org, send us a corresponding request to [our Support team](mailto:support@revenuegrid.com)

&nbsp;

&nbsp;

#### **How to Get Users' Sync IDs**

To get a user's Sync ID, which is used in specific configuration scenarios and [API scenarios](https://docs.revenuegrid.com/ri/fast/articles/Lightning-Scheduler-API/):

**1\.** On the Users tab, click on the needed user in the users list to open their settings page  

**2\.** See the URL in the address line of your browser. The link contains an alphanumeric value between the segments */users/* and */edit*  

For example, *2b34d5dc-9019-4f88-a724-c1426e93a522*

**3\.** Copy this value, it is the user Sync Id that you need



&nbsp;

&nbsp;

#### **Moving Users Between Organizations**

Organization is assigned for each user during the provisioning process. Otherwise, Users are automatically assigned to the default Organization. You can also change the Organization to which Users are assigned later after provisioning is complete.

!!! note "Note"
    when assigning Users to other Organizations, be aware that the new Organization may use a different mailbox access typ e or Microsoft Exchange Server impersonation settings. As a result, {{ product_name }}'s ability to access the User's mailbox may be affected

&nbsp;

To assign a User to another Organization, do the following:   

**1\.** On the **Users** tab of the Administration Panel, select the end users you want to move to another Organization  

**2\.** From the **Organization** picklist, select the Organization that you want to move the User to

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b30ea292c7d3a0fa9a3669a.png" class="minimized">
</p>

&nbsp;

**3\.** Click **Save**  

**4\.** If the following pop-up appears,  click **Yes** or **Cancel** to proceed

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b30dfb30428632c466b49c1.png)

&nbsp;

&nbsp;

#### Deleting Users

To delete a user:  

**1\.** Go to the **Users**  tab of the Administration Panel  

**2\.** From the list of users, pick the user you want to delete and click the **Delete** icon

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b30e8a20428632c466b49fe.png" class="minimized">
</p>

&nbsp;

**3\.**  In the confirmation dialog that appears, click **Delete**

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b30e0552c7d3a0fa9a36650.png)

&nbsp;
Once a User is deleted via the Administration Panel, they cannot access and use {{ product_name }} Add-In / Chrome Extension.
&nbsp;



&#160;
 &#160;

