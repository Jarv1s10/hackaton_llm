---
description: Learn how to manage Tasks via the Solution (Tasks Sync)
---
# Managing Tasks via the Solution (Tasks Sync)  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*3 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

[{{ company_name }} synchronization](../Synchronization-Engine-An-Overview/) ensures continuous background syncing of your work Tasks between MS Exchange / Office 365 and Salesforce. Once [activated](../Authorizing-Sync-Engine-to-Work-with-Your-Data/), {{ short_name }} synchronization runs every 30 minutes on server side.

!!! tip "Tip"
    Refer to [this article](../Object-Fields-Mapping-Patterns/#ms_outlook_tasks) to learn how MS Exchange / Office 365 Task item fields are matched with [Salesforce Tasks](https://help.salesforce.com/articleView?id=tasks.htm&type=5) by {{ short_name }}.  
    Also refer to [this article](../Choosing-What-to-Synchronize/) for more details on configuring objects synchronization

&nbsp;

With {{ product_name }}, you can save and update your work tasks in Salesforce right from your preferred mail client. Task reminders are synced along with them - so you will not miss any important ones. Selective automatic synchronizing of Tasks with Salesforce offered by {{ product_name }} is highly useful for jobs reporting and coordination.

After [{{ short_company_name }} sync is set up](../Authorizing-Sync-Engine-to-Work-with-Your-Data/), to enable Tasks down-syncing from Salesforce to your mail client, go to the **Sync Settings** page (see the article [Opening the Dashboard](../How-to-Open-Sync-Dashboard-(Adaptive-view)/)), on the General subtab, enable the **Sync my Salesforce tasks** switch button in the Tasks block:

<p><img src="..\..\assets\images\Configuration-&-Settings\User-Settings\contacts-sync\tasks-sync.png">
</p>

&nbsp;

Note that your Tasks existing in MS Exchange / Office 365 prior to {{ short_name }} sync activation will **not** be synced with Salesforce, unless you specifically select them to be synced using either one of the methods described below:

&nbsp;
&nbsp;

#### Saving a Task in Salesforce

You can save an MS Exchange / Office 365 Task in Salesforce in one of the following ways:

*   By assigning the task the custom *Salesforce* category. In this case on the following sync session the task will be saved in Salesforce and automatically moved to the *Salesforce Tasks* folder
*   By moving the task to the dedicated *Salesforce Tasks* folder. On the following sync session the task will be saved in Salesforce and automatically assigned the *Salesforce* category. As long as the task stays in the folder, any changes made to it will be conveyed to its matching Task object in Salesforce

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/582db73e903360645bfa502b.png)

&nbsp;

!!! note "Note"
    If the Salesforce category is unassigned after an item was moved to the dedicated Salesforce folder and synchronized with Salesforce, {{ short_name }} sync will automatically restore the category on this item on the following sync session – items will remain synced if you just unassign the custom category from them but leave them in the dedicated folder.
    In the opposite case, if a synchronized item is removed from the dedicated Salesforce folder to be unsynced, {{ short_name }} sync will automatically remove the custom category from this item in MS Outlook on the following sync session

!!! note "Note"
    Your personal Tasks located in the default *Tasks* folder or other folders in MS Exchange / Office 365 will **not** get saved in Salesforce. Only the Tasks assigned the *Salesforce* category or moved to the *Salesforce Tasks* folder will get saved


&nbsp;
&nbsp;

#### Editing a Salesforce Task via {{ product_name }}

You can edit a Salesforce task via {{ short_name }} in one of the following ways:

*   In [{{ product_name }}](../All-User-Actions-in-Add-In-Sidebar/), expand a related record's card, select the *Related* tab and expand the necessary Task under *Open activities*

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/582db7dec697916f5d0516af.png)

&nbsp;

*   Alternatively, find the needed Task among *Open activities* right on the Sidebar's home screen

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/582db7dec697916f5d0516af2.png)

&nbsp;

* * *

&nbsp;

#### Opening a Task directly in Salesforce

To open a task in Salesforce, do the following:

1.  Find the necessary Task in {{ product_name }} using either of the ways described in the previous section
2.  Click the Cloud icon or the <img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/open_in_sf.png" style="display: inline-block;vertical-align: middle;width: 18px;margin-left: 1px;height: 14px;object-fit: contain;"> icon next to the Task's header; the Task will be opened in Salesforce in your browser

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/cloud_icon.png)

&nbsp;

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/582db90f903360645bfa5043.png)

&nbsp;

!!! note "Note"
    Changes made to a task via {{ product_name }} are conveyed to Salesforce immediately and do not require [{{ short_name }} sync to be active](../How-to-Open-Sync-Dashboard-(Adaptive-view)/), while changes made to tasks in email client will appear in Salesforce only after the following [sync session](../Synchronization-Engine-An-Overview/)

&nbsp;

* * *

&nbsp;

#### Tasks Syncing Limitations via [MS Graph](../MS-Graph/)

Tasks syncing via MS Graph has the following limitations:  

- Recurring Tasks syncing is not supported
- No deleted Tasks processing via MS Graph
- Private Tasks do not get synced
- Categories are not supported
- Migration from MS Graph Tasks to EWS Tasks cannot be carried out

If [Impersonation over MS Graph](../Impersonation-Graph/) is used to mass-deploy the solution for end users, Tasks Syncing is completely unavailable.

&#160;
