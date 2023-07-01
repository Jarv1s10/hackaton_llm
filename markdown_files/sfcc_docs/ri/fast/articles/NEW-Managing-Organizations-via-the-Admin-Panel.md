---
description: Using RGES Admin panel, you can create, edit, define special sync settings, configure connection type for Organizations
---
# Managing Organizations via the Admin Panel  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*9 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! warning "Important"
    To use {{ product_name }} Admin panel, special access permissions are required. To request the permissions for your organization, [contact {{ company_name }} support team by email](mailto:support@revenuegrid.com). Admin panel provides tools for managing end users and some of its key settings it includes duplicate {{ product_name }} [Customization](../Customization-Settings-Explained/) and [Sync](../Configuring-Activities-Synchronization-Settings/) settings on Admin level

&nbsp;

In {{ product_name }} Administration Panel context, an Organization is a group of Users with shared basic settings which cooperate in a shared Salesforce space.

The **Organizations** tab of [Administration Panel](../How-to-Log-In-to-the-Admin-Panel/) provides mechanisms for defining synchronization configuration for an Organization. 

!!! note "Note"
    In the current implementation there is no way to limit the access rights for Admin Users, so an assigned Admin User can manage users in all Organizations locally 

&nbsp;

#### **Organizations List View**

On the **Organizations** tab, you can see the following columns:  

*   **ID** (this column is hidden by default)
*   **Name**
*   **Mailbox Access Type**
*   **Synchronization Status**
*   **Actions**

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b4355cd2c7d3a099f2e514a.png" class="minimized">
</p>

&nbsp;

A filter by each column can be applied to the list. To do that, click the **Expand more** icon next to a column name and select the action you need:

*   **Sort Ascending**
*   **Sort Descending**
*   **Remove Sort**
*   **Hide Column**

Click the ☰  (**Menu**) icon on the right to add or remove columns; you can also clear all filters by selecting the **Clear All Filters** item in this menu.  
Note that no bulk actions can be performed on Organizations.

If [synchronization](../Synchronization-Engine-An-Overview/) is enabled and running, organization info on the list is displayed in black font color. If synchronization is [not set up](../Email-Integration-Full-Deployment-Scenarios/) or is [suspended](../Handling-Sync-Issues/) for the whole Organization – it is displayed in red font color.

Via the **Organizations** tab you can perform the following tasks:  

*   **Create Organizations**
*   **View and edit Organizations' details**
*   **Delete Organizations**  

&nbsp;

&nbsp;

#### **Creating Organizations**

To create an organization:  

**1\.** Go to the **Organizations** tab  

**2\.** In the upper right corner of the page, click **New**  

**3\.** Do the following:   

&nbsp; &nbsp; &nbsp; &nbsp;**3\.1.** Fill in the **Name** field  
&nbsp; &nbsp; &nbsp; &nbsp;**3\.2.** Fill in the **External Id** field (the value becomes read-only and cannot be changed later)  
&nbsp; &nbsp; &nbsp; &nbsp;**3\.3.** From the **Mail Access Type** picklist, select the access type used for the organization:   

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b1f8d6f2c7d3a0fa9a2e0a8.png" class="minimized">
</p>

&nbsp;

4\. Click **Save** in the upper right corner to complete Org creation 

&nbsp;

&nbsp;

#### **Editing Organizations**

To modify an organization:

**1\.** Go to the **Organizations** tab  

**2\.** To edit or view an Organization, select one from the list; the following detailed information will appear:  

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b1f8e032c7d3a0fa9a2e0b2.png" class="minimized">
</p>

&nbsp;

**3\.** Edit the necessary Org parameters  
**4\.** Click **Save**    

&nbsp;
&nbsp;

#### **Viewing Organization Subtabs**

There are the following subtabs on the **Organizations** tab which contain relevant sets of actions. 

!!! note "Note"
    The columns in the subtabs can be added or removed via the columns actions picklist summoned by clicking the ☰ (**Menu**) icon

&nbsp;
&nbsp;

#### **Users** – the subtab displays the list of users which belong to the organization

The subtab includes a number of columns (these can be added or removed via the menu summoned by clicking the ☰  (**Menu**) icon).

*   **Name**
*   **E-Mail for Notifications**
*   **Organization**
*   **Plan**
*   **Account Logon**
*   **Synchronization Disabled**
*   **Mailbox Status**
*   **Created On**
*   **Actions**. The following actions are available:

<table class="table-bordered">
<tbody>
<tr>
	<td>
		<p>
			<img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b3f6da50428630abc0bc6a0.png" alt="" style="float: left; margin: 0px 10px 10px 0px;">
		</p>
	</td>
	<td>
		<span style="color:#333333"><strong>Edit User</strong>. Access and edit the User.</span>
	</td>
</tr>
<tr>
	<td>
		<p>
			<span style="color:#333333"><img alt="" src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b30c64d2c7d3a0fa9a36596.png" style="float:left; margin:0px 10px 10px 0px"></span>
		</p>
	</td>
	<td>
		<span style="color:#333333"><strong>Delete</strong>. Delete the User. Please note that Users with initialized mailbox cannot be deleted.</span>
	</td>
</tr>
<tr>
	<td>
		<p>
			<img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b3f6e042c7d3a099f2e3fb0.png" alt="" style="float: left; margin: 0px 10px 10px 0px;">
		</p>
	</td>
	<td>
		<span style="color:#333333"><strong>Enable Synchronization</strong>. Enable synchronization for a User.</span>
	</td>
</tr>
<tr>
	<td>
		<p>
			<img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b3f6e232c7d3a099f2e3fb1.png" alt="" style="float: left; margin: 0px 10px 10px 0px;">
		</p>
	</td>
	<td>
		<span style="color:#333333"><strong>Disable Synchronization</strong>. Suspend synchronization for the user.&nbsp;If the synchronization is suspended for an ordinary User, it can be resumed from the User Dashboard.</span>
	</td>
</tr>
<tr>
	<td>
		<p>
			<img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b3f6e552c7d3a099f2e3fb7.png" alt="" style="float: left; margin: 0px 10px 10px 0px;">
		</p>
	</td>
	<td>
		<span style="color:#333333"><strong>Force Synchronization</strong>. Standard synchronization interval is set to 30 minutes. The user can manually trigger synchronization outside of the standard sync schedule by selecting the Force Synchronization action, but no sooner than 1 minute after the last attempt to trigger a sync. This is done to avoid service overload in case of multiple consecutive “Force sync” requests.</span>
	</td>
</tr>
<tr>
	<td>
		<p>
			<img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b3f6e682c7d3a099f2e3fb9.png" alt="" style="float: left; margin: 0px 10px 10px 0px;">
		</p>
	</td>
	<td>
		<span style="color:#333333"><strong>Reset Mailbox</strong>. Request {{ product_name }} to remove user customization and keep synchronization disabled.&nbsp;Once synchronization is enabled again, the first synchronization attempt will apply customization to the user’s mailbox.</span>
	</td>
</tr>
<tr>
	<td>
		<p>
			<span style="color:#333333"><img alt="" src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b30f6fd2c7d3a0fa9a3674d.png" style="float:left; margin:0px 10px 10px 0px"></span>
		</p>
	</td>
	<td>
		<span style="color:#333333"><strong>Check User's Exchange Impersonated Access</strong>. Appears if Exchange Impersonation is set up for a user; initiates a check of impersonated mailbox access.</span>
	</td>
</tr>
    </tbody>
</table>


*   **Disabled Due To An Error** (hidden by default)
*   **Updated On** (hidden by default)

&nbsp;

&nbsp;
#### **Defining Special Synchronization Settings for an Org**

In the latest {{ product_name }} updates it is possible to push specific [synchronization settings](../Configuring-Activities-Synchronization-Settings/) to all users of an Org, or to groups of users and individual users within an Org; the users can be allowed or disallowed to adjust these settings. If you need to preset individual sync settings to different users in your Org, send us a corresponding request to [our Support team](mailto:support@revenuegrid.com).
&nbsp;

#### **Statistics** – the subtab displays statistics about the last synchronization session for each User in the Organization

You can check all the details about the item you need by clicking it or the **Open Job** icon under the **Actions** column. 
The subtab has the following columns that can be added or removed via the menu summoned by clicking the ☰ (**Menu**) icon:

* **Job ID** (hidden by default)

* **User**

* **Synchronization Start Date**

* **Synchronization End Date**

* **Status**

* **Synchronization Scope**

* **Changes**

* **Issues**

* **Error Category (E Category)**

* **Error Source (E Source)**

* **Message**

* **Exception** (hidden by default)

* **Actions**. The following actions are available:

  <table class="table-bordered">
  	<tbody>
  	<tr>
  		<td>
  			<p>
  				<span style="color:#333333"><img alt="" src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b30fa680428632c466b4aea.png" style="float:left; margin:0px 10px 10px 0px"></span>
  			</p>
  		</td>
  		<td>
  			<span style="color:#333333"><strong>Download Logs</strong>.&nbsp;Click this icon to download the session-related log (in a .zip archive).</span>
  		</td>
  	</tr>
  	<tr>
  		<td>
  			<p>
  				<span style="color:#333333"><img alt="" src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b30e0ec0428632c466b49c9.png" style="float: left; margin: 0px 10px 10px 0px;"></span>
  			</p>
  		</td>
  		<td>
  			<span style="color:#333333"><strong>Open Job</strong>.&nbsp;Select this icon to open a session’s description and details. Read [this article]he corresponding topic for details.</span>
  		</td>
  	</tr>
  	</tbody>
  	</table>

&nbsp;
&nbsp;

#### **Activity**  – this subtab displays system activities for the current organization

To export the data with detailed activities information to a CSV file, click the **Export to CSV** button above the second column. Wait until the file downloads and then you may open it in Microsoft Excel.  

Possible activity types are:

*   **Organization is created**
*   **Organization's synchronization is enabled**
*   **Organization's synchronization is disabled**

The subtab has the following columns that can be added or removed via the menu summoned by clicking the ☰  **Menu** icon:

* **Date**

* **Changed By**

* **Type**

* **Actions**. The following action is available:

  <table class="table-bordered">
  	<tbody>
  	<tr>
  		<td>
  			<p>
  				<span style="color:#333333"><img alt="" src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b30fa680428632c466b4aea.png" style="float: left; margin: 0px 10px 10px 0px;"></span>
  			</p>
  		</td>
  		<td>
  			<span style="color:#333333"><strong>Download Logs</strong>.&nbsp;Click this icon to download the session-related log (in a .zip archive).</span>
  		</td>
  	</tr>
  	</tbody>
  	</table>

*   **Changed By** (ID) (hidden by default)

The **Activity **subtab has the **number of rows to show** box above the **Actions **column. The possible values scope is from 0 to 2000. Entering '0' will display all existing rows for selected Organization; '60' is the default value. After setting a value click the blue **Refresh** button next the box to apply the change.

&nbsp;

**Email Configuration** – displays the type of users' access to mailboxes.

When a new organization is created, specify the type of mailbox access to be used for its users. When the access type is selected and configured, it is applied to all users in the organization. The users can only use the defined type to access their mailboxes.  
When a new Organization is created, specify the type of mailbox access to be used for the Organization’s Users. When the access type is selected and configured, it is applied to all Users in the Organization. The Users can access their mailboxes only using the chosen access type.  
You can edit the user’s name and mailbox settings which were specified during the provisioning process or defined by the organization which the user belongs to.  

&nbsp;

#### Configuring Connection Type for an Organization

!!! tip "Tip"
    Also see [this article](../Email-Integration-Full-Deployment-Scenarios/) for information on all available {{ product_name }} full deployment scenarios 

&nbsp;

As new mailbox compatibilities and deployment scenarios are implemented, more options are added to available **Mailbox Access Type** options:  

- Microsoft Exchange basic authorization (EWS API) - End User logon
- Microsoft Exchange basic authorization (EWS API) - Impersonated logon
- Microsoft 365 OAuth (EWS API) - End User logon
- Microsoft 365 OAuth (Graph API) - End User logon
- Microsoft 365 OAuth (EWS API) - Impersonated logon
- Microsoft 365 OAuth (Graph API) - App-only access logon
- Google Direct Logon
- Google Service Account  

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/access-types.png" class="minimized">
</p>

&nbsp;



##### Microsoft Exchange basic authorization (EWS API) - End User logon

The typical scenario where the end users enter their Exchange logon credentials in [{{ product_name }}](../Authorizing-Sync-Engine-to-Work-with-Your-Data/#activate_ri_sync_for_ms_exchange) to activate the Sync engine. 

&nbsp; 

##### Microsoft Exchange basic authorization (EWS API) - Impersonated logon

[Microsoft Exchange Impersonation](../Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/) is used to mass-authorize in {{ product_name }} end users with MS Exchange mail accounts via an impersonating service account. Before setting the this access type, you must obtain the [Exchange EWS URL](https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/explore-the-ews-managed-api-ews-and-web-services-in-exchange) and a configured [Impersonating account](../Impersonation-O365/)'s login and password. See [this article](../Set-up-An-Impersonation-Service-Account/) for detailed steps how to configure everything for this access type.

&nbsp;

##### Microsoft 365 OAuth (EWS API) - End User logon

This option is used to authorize in {{ product_name }} end users with Office 365 mail accounts over Office 365 OAuth. See [this article](../Authorizing-Sync-Engine-to-Work-with-Your-Data/#activate_ri_sync_for_office_365) for more information. In the latest product updates it is the default option for bulk O365 users authorization [using a Service account](../Impersonation-O365/).

&nbsp;

##### Microsoft 365 OAuth (Graph API) - End User logon

This option is used to authorize in {{ product_name }} end users with Office 365 mail accounts over [MS Graph](https://docs.microsoft.com/en-us/graph/overview). See [this article](../MS-Graph/) for more information. Also see [this article](../MS-Graph/#ms_graph_limitations) to learn about limitations presently associated with this connection type.

&nbsp;

##### Microsoft 365 OAuth (EWS API) - Impersonated logon

This option is used to mass-authorize in {{ product_name }} end users with Office 365 mail accounts via an [impersonating account](../Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/). To use this access type, you must have mail server and {{ product_name }} Admin account credentials. See [this article](../Impersonation-O365/) for detailed steps how to configure everything for this access type.

&nbsp;

##### Microsoft 365 OAuth (Graph API) - App-only access logon

This option is used to mass-authorize in {{ product_name }} end users with Office 365 mail accounts via app-only access with MS Graph API. To use this access type, you must have mail server and {{ product_name }} Admin account credentials. See [this article](../Impersonation-Graph/) for detailed steps how to configure everything for this access type. Also see [this article](../MS-Graph/#ms_graph_limitations) to learn about limitations presently associated with this connection type.

&nbsp;

##### **Google Direct Logon**

This option is used to authorize in {{ product_name }} end users with Gmail / Google Workspace accounts over Gmail OAuth. The users will need to authorize it individually. See [this article](../How-to-Set-Up-the-Chrome-Extension-for-Salesforce-and-Gmail/) for more information.

&nbsp;

##### **Google Service Account**

This option is used to [mass-authorize in {{ product_name }}](../Gmail-Users-Mass-Provisioning/) end users with Gmail / Google Workspace accounts. See [this article](../Gmail-Service-Account/) for more information.

&nbsp;

&nbsp;

##### {{ company_name }} Compatibility

Presently, due to data access authorization specifics, only connection types *MS Exchange Direct Logon*, *Office 365 OAuth*, *Google Service Account* (partial), and *Google Direct Logon* are supported by the [full {{ company_name }} solution](https://docs.revenuegrid.com/). Via a custom workaround {{ company_name }} is also compatible with MS Graph; in this scenario, {{ company_name }} is configured to run over EWS tokens and {{ company_name }} works over MS Graph.

&nbsp;

* * *

&nbsp;

#### **Deleting Organizations**

Please note that you can delete an Organization only if it has no users with initialized [Exchange Storage](https://docs.microsoft.com/en-us/exchange/plan-and-deploy/deployment-ref/storage-configuration?view=exchserver-2019). If at least one user is initialized, you must delete the user first, and then the Organization. After you delete an Organization, all users that belong to it will be irrecoverably deleted.  
Also note that you cannot delete a default Organization.

To delete an existing organization:  

**1\.** Go to the **Organizations** tab

**2\.** From the list of organizations, select the organization you want to delete, and then click the **Delete** icon

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b1f8f9f0428632c466ac80e.png" class="minimized">
</p>

&nbsp;
**3\.** In the confirmation message that appears, click **Delete**

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b30f01c0428632c466b4a53.png)


&#160;
 &#160;

