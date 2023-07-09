# SSI Add-In View Problems in Microsoft Outlook 2013

&nbsp;

&nbsp;

**[ This article is work-in-progress ]**

&nbsp;

&nbsp;

## Symptoms

SAP Cloud for Customer Server-Side Integration Add-In has different views in MS Outlook 2013 and MS Outlook 2016. In MS Outlook 2013, the SSI Add-In button **isn't available** in the ribbon as well as a sidebar.

In MS Outlook 2013, Add-In is located in a custom pane only, but users expect to see the Add-In button in the ribbon and use the sidebar.

This is how users may use Add-In in **MS Exchange 2013** (Outlook Web Access).

<p>
<img src= "..\..\assets\images\add-in-view-problem\1.png">
</p>

&nbsp;

&nbsp;

In **MS Outlook 2016**, Add-In is available from the ribbon and as a sidebar, as we got used.

<p>
<img src= "..\..\assets\images\add-in-view-problem\2.png">
</p>

&nbsp;

* * *

&nbsp;


## Causes

The root cause is the **absence of MS Outlook 2013 updates** (thus, it is not an SSI Add-In issue).

To show the SSI Add-In button in the ribbon and allow the use of the sidebar, MS Outlook 2013 should support **Add-In commands**. MS Outlook Add-In commands provide ways to initiate specific Add-In actions from the ribbon by adding buttons or drop-down menus. This lets users access Add-Ins in a simple, intuitive, and unobtrusive way – users will have an Add-In button in the ribbon and may use the sidebar.

&nbsp;

* * *

&nbsp;

## Resolution

It is necessary to install a few updates for MS Outlook to address the current situation.

Listed updates will enable [Add-in commands for Outlook](https://learn.microsoft.com/en-us/office/dev/add-ins/outlook/add-in-commands-for-outlook?tabs=xmlmanifest):

* [March 8, 2016 security update for Outlook](https://support.microsoft.com/en-us/topic/ms16-029-description-of-the-security-update-for-outlook-2013-march-8-2016-3d61acd7-3dc6-b9f4-3a1b-5f1f5321d109)  
* [March 8, 2016 security update for Office (KB3114816)](https://support.microsoft.com/en-us/topic/march-8-2016-update-for-office-2013-kb3114816-3d3eb171-78c2-0e61-62a2-85723bc4bcc0)  
* [March 8, 2016 security update for Office (KB3114828)](https://support.microsoft.com/en-us/topic/march-8-2016-update-for-office-2013-kb3114828-54437016-d1e0-7aac-dbb7-4ecfbd57f5f0)  

&nbsp;

!!! warning "Important"
    It is strongly recommended to keep MS Office up-to-date with the most recent updates installed to avoid described issues in the future

&nbsp;

&nbsp;