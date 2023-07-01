---
description: Learn how RG Email Sidebar works and what it syncs
---
# How the Solution Works and What It Syncs  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*3 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! tip "Tip"
    Besides serving as a Mailbox ↔ Salesforce integration tool, {{ product_name }} is an integral part of the premium [revenue intelligence](https://revenuegrid.com/blog/what-is-guided-selling/) platform [{{ company_name }}](https://revenuegrid.com). Check [this article](https://docs.revenuegrid.com/) for more information

&nbsp;

{{ product_name }} is a cloud application that performs two-way synchronization of data between your Salesforce account and Exchange mailbox and gives you access to Salesforce data right from your email client. After you create a {{ product_name }} account using a simple [registration wizard](../User-Registration-Wizard/) and install [the MS Outlook Desktop or On the Web version Add-In](../How-to-Install-and-Run-the-Solution-all-configurations/) or [the Chrome Extension](../How-to-Set-Up-the-Chrome-Extension-for-Salesforce-and-Gmail/), {{ product_name }} will customize your mailbox by adding the required custom folders/labels, add its [Sidebar](../All-User-Actions-in-Add-In-Sidebar/), and start [synchronizing your records](../Synchronization-Engine-An-Overview/) on server-side. The specifics of using the {{ product_name }} Chrome Extension for Gmail are explained in [this article](../Using-the-Solution-for-Salesforce-and-Gmail/).



![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b2a77d82c7d3a0fa9a3394f.png)

&nbsp;

The data that [{{ company_name }} synchronizes](../Synchronization-Engine-An-Overview/) includes:

*   **[Contacts.](../Synchronization-of-Contacts/)** In Outlook, {{ product_name }} creates a new contact folder named *Salesforce Contacts* where you can find your Salesforce contacts. To synchronize a newly created contact with Salesforce, assign it the *Salesforce* category or move it to the *Salesforce Contacts* folder
*   **[Calendar items.](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/)** Your Salesforce and Outlook calendars are in sync. To save a new meeting or appointment in Salesforce, assign it the “Salesforce” category in Outlook or save it using the Outlook Add-In or Chrome Extension
*   **[Tasks.](../Synchronization-of-Tasks/)** As with contacts, {{ product_name }} creates a new task folder named “Salesforce Tasks” in which you can find your tasks. By adding a new or moving an existing task to this folder, or assigning a task the custom “Salesforce” category in MS Outlook Desktop or On the Web version, you can quickly save it in Salesforce
*   **[Emails](../Saving-Emails-in-Salesforce-1.-Function-Overview/) and [Email Attachments](../Attachments-Handling-(Basic)/).** {{ product_name }} creates a new folder named “Salesforce Emails” in your mailbox. Moving your emails to this folder will save them as completed tasks with Salesforce. Email attachments are also saved to Salesforce as attachments to the completed task

Synchronization runs in the background (server-to-server) 24x7, one sync session every 30 minutes; the interval is defined by the set [service plan](../Managing-Plans-for-the-Users/).

&nbsp;

<iframe src="https://player.vimeo.com/video/473922580" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>

&nbsp;
&nbsp;

* * *

&nbsp;

### Advanced Features Which Require [Sync Engine](../Synchronization-Engine-An-Overview/) to Be Running

After you [set up](../Authorizing-Sync-Engine-to-Work-with-Your-Data/) MS Exchange-Salesforce synchronization performed by {{ product_name }}, you will unlock the following essential {{ product_name }} features:

* Meeting Scheduler: [Send meeting time slots](../How-to-Send-Meeting-Time-Slots-(Adaptive-view)/), [Share calendar availability](../Sharing-Calendar-Availability-(Adaptive-view)/)
* [Engagement Panel](../How-to-Use-the-Solution-s-Engagement-Panel/)
* [Saving email messages to Salesforce in Compose mode](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/)
* [Saving calendar items to Salesforce](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/)
* [Bidirectional syncing of calendars](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/)
* Email or calendar item auto-saving or saving in Salesforce of all emails in a thread, as well as all other possibilities managed in [Synchronization settings](../Configuring-Activities-Synchronization-Settings/)

&nbsp;

!!! warning "Important"
    Note that when you are using {{ product_name }} there should be no other software running that performs data transfer between MS Exchange and [Salesforce API](http://trailhead.salesforce.com/modules/api_basics/units/api_basics_overview) (e.g. Salesforce Lightning sync, Salesforce Inbox, Salesforce for Outlook, etc.) Running different MS Exchange – Salesforce sync applications simultaneously will cause sync conflicts and items duplication. If you encounter this kind of unexpected behavior, please check that with your Salesforce admin or, if you are a Salesforce admin, check for such software in the following places:  
    <br>
    ●   [Salesforce Setup](http://help.salesforce.com/articleView?id=basics_nav_setup.htm) > Apps > App Manager  
    ●   [Connected Apps](http://help.salesforce.com/articleView?id=connected_app_overview.htm&type=5)  
    ●   [Salesforce Login History](http://help.salesforce.com/articleView?id=users_login_history.htm&type=5)  
    <br>
    After you find apps which cause conflicts, please refer to [this Salesforce help article](https://dreamevent.secure.force.com/articleView?id=connected_app_delete.htm&type=5) to learn how to disable them.Please also note that apps which use Salesforce API but **do not** exchange data between Salesforce and MS Exchange will not cause sync conflicts.
    <br><br>
    Learn more about troubleshooting calendar events duplication in [this {{ company_name }} article](../duplication-troubleshooting/)



&#160;
 &#160;

