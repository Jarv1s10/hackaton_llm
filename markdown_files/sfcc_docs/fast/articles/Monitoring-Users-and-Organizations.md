---
description: Learn how to monitor users and organizations sync via the Admin Panel
---
# Monitoring Users and Organizations Sync via the Admin Panel  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*6 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! warning "Important"
    To use {{ product_name }} Admin panel, special access permissions are required. To request the permissions for your organization, [contact {{ company_name }} support team by email](mailto:support@revenuegrid.com). Admin panel provides tools for managing end users and some of its key settings it includes duplicate {{ product_name }} [Customization](../Customization-Settings-Explained/) and [Sync](../Configuring-Activities-Synchronization-Settings/) settings on Admin level

Administration panel includes tools for real-time tracking of synchronization statuses of {{ product_name }} users and organizations to promptly resolve emerging sync issues.

Sync statuses can be monitored and managed by applying different filters, focusing view on list items with certain parameters. The Organizations and Users for which synchronization is enabled are shown in black font color; ones for which it is disabled are shown in red font color.

You can monitor Users’ sync statuses using the following [Administration Panel](../How-to-Log-In-to-the-Admin-Panel/) tools:  

•    Monitoring Organizations' Sync Statuses  
•    Exporting Organizations to CSV  
•    Monitoring Users in Specific Organization  
•    Exporting Users to CSV  
•    Monitoring Synchronization Statistics in Specific Organization  
•    Exporting Synchronization Sessions to CSV  
•    Viewing Synchronization Job Details  
•    Downloading Logs  
•    Monitoring Synchronization Issues for a Specific User

&nbsp;

* * *

&nbsp;

#### Monitoring Organizations' Sync Statuses 

You can apply filters to the list view and monitor the Organizations with enabled or disabled synchronization status.  
To monitor Organizations’ synchronization statuses:  
1\. Go to the **Organizations** page  
2\. In the search box at the top of the **Synchronization Status** column, enter your search criteria, for example, _enabled_. The list will show all Organizations with _enabled_ sync status

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b3a3f3a0428630abc0ba1d1.png" class="minimized">
</p>

&nbsp;

* * *

&nbsp;

#### Exporting Organizations to CSV

You can export the data from the **Organizations** tab list as a CSV file. After you apply necessary filters, export the items as a CSV file with their current view applied; the file is viewable and editable as an Excel document. For example, this way you can export all Organizations with enabled or disabled sync status.  
To export the data to a CSV file, click the **Export to CSV** button above the second column. Wait until the document downloads and then you can open it in MS Excel.

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b3a3f550428630abc0ba1d2.png" class="minimized">
</p>

&nbsp;

* * *

&nbsp;

#### Monitoring Users in a Specific Organization

1\. Go to the **Organizations** tab and open the needed Organization  
2\. On the **Users** subtab, filter Users by their sync status. To do that, enter one of the following search criteria in the search box at the top of the **Synchronization Disabled** column:  
•     **False**. When set to false, synchronization is enabled for a User. These Users are shown in black font color  
•     **True**. When set to true, synchronization is disabled for a User. These Users are shown in red font color

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b3a3f610428630abc0ba1d4.png" class="minimized">
</p>

&nbsp;

* * *

&nbsp;



#### Exporting Users data to CSV

To export the data with Users' sync sessions details to a CSV file, click the **Export to CSV** button above the second column. Wait until the document downloads and then you can open it in MS Excel.

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b3a3f8a0428630abc0ba1d7.png" class="minimized">
</p>

&nbsp;

* * *

&nbsp;

#### Monitoring Synchronization Statistics in a Specific Organization

You can view an Organization's sync sessions on the **Statistics** subtab of the **Organizations** tab. By default, the **Statistics** tab shows the items sorted by their statuses (_finished_ / _errors_) and filtered by errors, so you can view what went wrong with synchronization and needs to be fixed. More details on each unsuccessful sync session are shown in the columns.

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b3a3f992c7d3a0fa9a3b031.png" class="minimized">
</p>

&nbsp;

* * *

&nbsp;

#### Exporting Synchronization Sessions to CSV

To export the data with synchronization sessions details to CSV, click the **Export to CSV** button above the second column. Wait until the document downloads and then you can open it in MS Excel.

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b3a3fa40428630abc0ba1d9.png" class="minimized">
</p>

&nbsp;

* * *

&nbsp;

#### Viewing Synchronization Job Details

You can view synchronization job details for all Users of a specific Organization on the **Statistics** subtab.

!!! note "Note"
    Some columns are hidden by default. To add and view more columns, click the ☰ (Menu) icon on the Statistics subtab and select the columns you need from the picklist

You can view sync job details by clicking the **i** icon in the **Actions** column.

The following columns show sync session details for Users:  
•     **User**.  
•     **Run**. Synchronization time period and date.  
•     **Status**. By default, the statuses are filtered by errors; additional details on the sync session are displayed here.  
•     **Objects** ⏍. A detailed report on synchronized objects. You can copy the values to clipboard by clicking the ⏍ icon.  
•     **Objects**. The number of synchronized objects.  
•     **Changes**. The number of changes after sync completion.  
•     **Failures**. Failures during synchronization.  
•     **Total Changes**. The total number of changes after synchronization.  
•     **Error Source**. Displays the source of error. Possible values: **Unknown** / **Microsoft Exchange** / **Connector**.  
•     **Error Category**. Displays the error category. For example, **caused by authentication issues**.  
•     **Exception** ⏍. You can copy the value to clipboard by clicking the ⏍ icon.  
•     **Issues**. The number of issues detected after sync.  
•     **Conflicts**. The number of conflicts detected after sync.

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b3a3faf0428630abc0ba1da.png)

&nbsp;

* * *

&nbsp;

#### Downloading Logs

In case you need more details on a synchronization session of a specific User (or Organization), you can download the logs.  
To download logs of a specific User, click the ⤓ icon in the **Actions** column (**Statistics** subtab) and wait for the .zip archive with logs to download.

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b3a3fc60428630abc0ba1db.png)

&nbsp;

* * *

&nbsp;

#### Monitoring Synchronization Issues for a Specific User

If sync results for some objects cannot be created, updated, or deleted in Exchange or in Salesforce, a synchronization issue regarding this object will be logged for the User.  
To investigate the sync session issues of a specific User, find the needed User and view the sync status details for this User.  

To view synchronization issues for a specific User:  
1\. Go to the **Users** tab and find the User you want to monitor  
2\. On the **Issues** subtab, you can view the list of issues for this User. The details about the issues are given in the following table:  
•     **Type**. Type of the object that could not be synchronized. The possible types are **E-Mail** or **Appointment**.  
•     **Name**. The name of the object. For example, the **Full name** for Contacts or the **Subject line** for Events.  
•     **Direction**. The direction might be from Exchange to Salesforce or vice versa.  
•     **Operation name**. Create, Update, or Delete.  
•     **Error Code**. The following values are possible:  
​        0 – object is active / success result;  
​        1 – object is locked / an error in the operation;  
​        2 – object is already removed in a storage;  
​        3 – object is inaccessible / updated prematurely in a storage.  
 •     **Error Text**. The error text returned by the instance in which changes are going to be made.

Also, you can view the synchronization issues of a specific User in User Dashboard. For more information, see the **[Handling Issues](../Handling-Sync-Issues/)** article.



&#160;
 &#160;

