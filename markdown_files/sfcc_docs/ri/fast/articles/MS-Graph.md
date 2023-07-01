---
description: Learn how to use MS Graph Connectivity to Work with O365 Data
---
# Using MS Graph Connectivity to Work with O365 Data  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

[MS Graph secure API](https://docs.microsoft.com/en-us/graph/use-the-api) can be used instead of [Exchange Web Services](https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/start-using-web-services-in-exchange) to work with MS Office 365 data via {{ product_name }}. MS Graph has several benefits over EWS; it is mostly in demand for high-security corporate environments, as it offers configurable [granular data access permissions control](https://docs.microsoft.com/en-us/graph/auth/auth-concepts). It allows to provide focused access *only* to specific Office 365 data types, e.g. Contacts, Tasks, Emails, or Calendar items. The same configured MS Graph data access permissions are applied for both [{{ short_name }} Sync app](../Synchronization-Engine-An-Overview/) and [{{ short_name }} Add-In app](../Introduction/); item types with disabled access permissions remain inaccessible by {{ product_name }}.  
Also see [this Microsoft article](https://docs.microsoft.com/en-us/graph/permissions-reference) to learn more about MS Graph data access control management and security.   

This access type can be enabled for [a specific org](../Managing-Organizations-via-the-Admin-Panel/) or [a specific user in an Org](../Managing-Users-via-the-Solution-s-Admin-Panel/) via [{{ short_name }} Admin panel](../How-to-Log-In-to-the-Admin-Panel/): open the **Organizations** tab > **Mailbox access type** > set to **MS Graph**  

[Server IP whitelisting](../Overcoming-Firewall-Issues/) is also required to work via MS Graph but involves a different set of IPs, you can request the list from [our Support team](mailto:support@revenuegrid.com).

!!! tip "Tip"
    After user switching from another access type or after a new user is initialized: the user must re-login via O365 OAuth 2.0 in order to refresh the access token

&nbsp;

Another special feature of MS Graph is its full data exchange compatibility with other Microsoft 365 apps: MS Teams, MS Office apps, OneNote, etc. For example, {{ product_name }} can be configured to auto-generate MS Teams room links for its Meeting Scheduler features ([Time Slots](../How-to-Send-Meeting-Time-Slots-(Adaptive-view)/), [Book me](../Sharing-Calendar-Availability-(Adaptive-view)/)).

&nbsp;

 &nbsp;

### MS Graph Limitations

As of {{ product_name }} version 2302 (winter 2023), there are several limitations for using the Solution via MS Graph:  

!!! warning "Note"
    **a.** Only Office 365 mailboxes are supported, cannot be used for MS Exchange or Gmail mailboxes   
    **b.** [OAuth 2.0](https://oauth.net/2/) mail data access authorization only   
    **c.** No [saving of all emails in a thread](../Special-Admin-Panel-Settings/#email_threads_auto-sync)   
    **d.** Limited [Smart Description](../Using-the-Smart-Description-Feature/) support (supported for Tasks, Contacts)   
    **e.** Notifications on non-essential meeting updates (including past meetings) made by the organizer get automatically sent out to all attendees   
    **f.** With MS Graph connectivity, localizations into other languages is implemented for all {{ product_name }} components, except for [Sync dashboard](../How-to-Open-Sync-Dashboard-(Adaptive-view)/)   
    **g.** Presently, there are [several limitations with Outlook Tasks syncing](../Synchronization-of-Tasks/#tasks_syncing_limitations_via_ms_graph)  
    **h\.** [Calendar events instant sync](../Synchronization-Engine-An-Overview/#instant_sync_of_calendar_items) from MS Outlook to Salesforce is not supported  
    **i.** [Auto-saving all emails in selected thread](../Save-All-Emails-in-a-Thread/) is currently not supported  
    **j.** Saving of attachments on events is not supported yet


&nbsp;

&nbsp;

