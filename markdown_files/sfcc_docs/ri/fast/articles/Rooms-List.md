---
description: Learn how to configure Room Lists for MS Exchange meetings over EWS
---
# How to Configure Room Lists for MS Exchange Meetings Over EWS  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

If your Org uses [Exchange Web Services](https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/start-using-web-services-in-exchange) to access email and calendar data, the local MS Exchange Admin should make certain configuration adjustments in order to make [Meeting Room lists](https://docs.microsoft.com/en-us/exchange/recipients/room-mailboxes?view=exchserver-2019) available in {{ product_name }}, e.g. to be used for {{ short_name }}'s' [Book me](../Sharing-Calendar-Availability-(Adaptive-view)/) and [Time Slots](../How-to-Send-Meeting-Time-Slots-(Adaptive-view)/) features.

!!! note "Note"
    If an [impersonating Service account](../Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/) is used for[{{ company_name }} Sync users authorization](../Email-Integration-Full-Deployment-Scenarios/), the Service account must have a mailbox and an Office license assigned to it. If the Service Account does not have a mailbox or license assigned, rooms and resources will not be retrieved in room lists via EWS 

&nbsp;



Then you should configure Room lists, that can only be done via [PowerShell](https://docs.microsoft.com/en-us/powershell/exchange/?view=exchange-ps) for both MS Exchange and Office 365. See [this article](https://technet.microsoft.com/en-us/library/jj984289(v=exchg.160).aspx) to learn how to connect to your Office 365 instance via PowerShell.

After you have connected it, follow the steps below:

1\. Create a [Member Room](https://docs.microsoft.com/en-us/powershell/module/exchange/add-distributiongroupmember?view=exchange-ps). Room resources can be created via <https://portal.office.com/adminportal/home#/ResourceMailbox> or via PowerShell. See [this Microsoft article](https://docs.microsoft.com/en-us/exchange/recipients/room-mailboxes?view=exchserver-2019) for more information  

**2\.** Enter the following cmdlet in PowerShell:  

   ``New-DistributionGroup -Name "{meeting room's name}" -OrganizationalUnit "{your Org's Exchange instance}/Users" -RoomList``

All created Rooms must be included into this list.  

**3\.** Enter another cmdlet in PowerShell:  

​    ``Add-DistributionGroupMember -Identity "{meeting room's name}" -Member Room#``

**4\.** Repeat the step **3** for every room that should be added  

&nbsp;

All meeting Rooms configured this way will become available in {{ product_name }} after the users [re-login into the Add-In](../How-to-Install-and-Run-the-Solution-all-configurations/#ii_rg_email_sidebar_logon)  

&nbsp;

&nbsp;

#### Troubleshooting Resources Availability Over EWS

In case the rooms or other resources are still unavailable in {{ product_name }}, you can troubleshoot the configuration using a free and safe open-source tool [EWS Editor](https://github.com/dseph/EwsEditor/releases/tag/1.21).

**1\.** Connect to your Exchange server via EWS Editor See [this article](https://techcommunity.microsoft.com/t5/exchange/how-to-troubleshoot-ews-connection-issues-using-ews-editor/m-p/1567393) to learn how to do that

**2\.** Open **Tools** > **Meeting rooms...** or another resource category

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Rooms\EWS_editor_2.png">
</p></details>

&nbsp;

**3\.** Read [this article]he rooms' availability in the Room list

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Rooms\EWS_editor_1.png" class="minimized">
</p></details>



&#160;
 &#160;



