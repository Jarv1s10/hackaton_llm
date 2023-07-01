---
description: The complete guide to RG Email Sidebar supported email servers
---
# Supported Email Servers  
  

*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

{{ product_name }} is compatible with the following email servers. Please click on an Email server to learn more:

*   [Microsoft Office 365 (with Exchange Online plan)](../Supported-Email-Clients-for-Microsoft-Office-365-(with-Exchange-Online-plan)/)
*   [Microsoft Exchange 2016, 2019](../Supported-Email-Clients-for-Microsoft-Exchange-2013,-2016/)
*   [Gmail](../Supported-Email-Clients-for-Gmail/), via [{{ product_name }} Chrome Extension](../Using-the-Solution-for-Salesforce-and-Gmail/)
*   Other email servers using POP/IMAP and SMTP protocols - only via the [Desktop (MSI) implementation of {{ product_name }}](../How-to-Install-and-Run-the-Desktop-MSI-implementation-MS-Outlook/) (no special compatibility guaranteed)

!!! note "Note"
    Pay attention that starting from June 2022, [Microsoft ceased support and updates of the Internet Explorer 11 desktop application](https://learn.microsoft.com/en-us/lifecycle/announcements/internet-explorer-11-end-of-support) on most versions of Windows 10 and encouraged its customers to move to other browsers. Since the MS Outlook 2013 for desktop uses Internet Explorer 11 engine to render embedded add-ins in its interface, it will be impossible to run {{ product_name }} on this version of MS Outlook. Learn more in [this {{ short_company_name }} article](https://docs.revenuegrid.com/ri/fast/articles/internet-explorer-end-of-support/)

&nbsp;

!!! warning "Important"
    {{ product_name }} interacts with MS Exchange servers over [Exchange web services (EWS)](https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/start-using-web-services-in-exchange), so an essential prerequisite for using the tool is that EWS are enabled on your Exchange server. Refer to [this Microsoft connectivity test page](https://testconnectivity.microsoft.com/) to check your EWS connectivity: on this page, open the **Exchange Server** tab and run  
    **1.** *Exchange ActiveSync* test  
    **2.** *Exchange ActiveSync Autodiscover* test  
    **3.** *Synchronization, Notification, Availability, and Automatic Replies* test     


&nbsp;

***

&nbsp;

## Microsoft Office 365

Please find the list of compatible email clients below. Note, it's recommended to update your email client to the latest version for the best experience with {{ product_name }}.  

&nbsp;


<table>
<tbody>
<tr>
	<td>
		<strong> Email Client </strong>
	</td>
	<td>
		<strong>Supports <a href="https://docs.revenuegrid.com/ri/fast/articles/Synchronization-Engine-An-Overview/">Sync Engine</a></strong>
	</td>
	<td>
		<strong> Supports <a href="https://docs.revenuegrid.com/ri/fast/articles/Introduction/">Add-In</a> </strong>
	</td>
</tr>
<tr>
	<td>
		 Microsoft Outlook 2016, 2019 for Windows
	</td>
	<td>
		 Yes
	</td>
	<td>
		 Yes+Pin*
	</td>
</tr>
<tr>
	<td>
		 Microsoft Outlook 2016, 2019 for Mac
	</td>
	<td>
		 Yes
	</td>
	<td>
		 Yes
	</td>
</tr>
<tr>
	<td valign="top">
		Outlook on the web (Outlook.com)
		<br>
	</td>
	<td valign="top">
		Yes
	</td>
	<td valign="top">
		Yes
	</td>
</tr>
<tr>
	<td>
		 Outlook app for 
		<a href="http://itunes.apple.com/us/app/microsoft-outlook-email-and-calendar/id951937596">iOS</a> or <a href="http://play.google.com/store/apps/details?id=com.microsoft.office.outlook&amp;hl=en">Android</a>
	</td>
	<td>
		 Yes
	</td>
	<td>
		 Yes
	</td>
</tr>
<tr>
	<td>
		 Any other desktop or mobile client&nbsp;&nbsp; 
		<br>
		 that can be connected to&nbsp;Microsoft Exchange&nbsp;&nbsp; 
		<br>
		 and supports folders and/or categories, e.g. 
		<a href="http://support.apple.com/mail">iOS Mail app</a>
	</td>
	<td>
		 Yes
	</td>
	<td>
		 No
	</td>
</tr>
</tbody>
</table>
**\* What 'Yes+Pin' means?** Sidebar Add-In [can be 'pinned'](../Sidebar-Pinning/), so you do not need to reopen it each time browsing different emails or meetings in your email client. Please note, *Outlook 2016* one-time purchase version and older Outlook versions do not support {{ product_name }} pinning. Only *Exchange 2016* and newer Exchange versions support {{ short_name }} pinning

&nbsp;

* * *

&nbsp;

## MS Exchange 2016, 2019

!!! note "Note"
    Pay attention that starting from June 2022, [Microsoft ceased support and updates of the Internet Explorer 11 desktop application](https://learn.microsoft.com/en-us/lifecycle/announcements/internet-explorer-11-end-of-support) on most versions of Windows 10 and encouraged its customers to move to other browsers. Since the MS Outlook 2013 for desktop uses Internet Explorer 11 engine to render embedded add-ins in its interface, it will be impossible to run {{ product_name }} on this version of MS Outlook. Learn more in [this {{ short_company_name }} article](https://docs.revenuegrid.com/ri/fast/articles/internet-explorer-end-of-support/) 

&nbsp;

<table>
<tbody>
<tr>
	<td>
		<strong>Email Client</strong>
	</td>
	<td>
		<strong>Supports <a href="https://docs.revenuegrid.com/ri/fast/articles/Synchronization-Engine-An-Overview/">Sync Engine</a></strong>
	</td>
	<td>
		<strong> Supports <a href="https://docs.revenuegrid.com/ri/fast/articles/Introduction/">Add-In</a> </strong>
	</td>
</tr>
<tr>
	<td>
		 Microsoft Outlook 2016, 2019 for Windows
	</td>
	<td>
		 Yes
	</td>
	<td>
		 Yes+Pin*
	</td>
</tr>
<tr>
	<td>
		 Microsoft Outlook 2016, 2019 for Mac
	</td>
	<td>
		 Yes
	</td>
	<td>
		 Yes
	</td>
</tr>
<tr>
	<td>
		<a href="http://itunes.apple.com/us/app/microsoft-outlook-email-and-calendar/id951937596itunes.apple.com/us/app/microsoft-outlook-email-and-calendar/id951937596">Outlook app for iOS</a>, <a href="http://play.google.com/store/apps/details?id=com.microsoft.office.outlook&amp;hl=en">Outlook app for Android</a>
	</td>
	<td>
		 Yes**
	</td>
	<td>
		 No**
	</td>
</tr>
<tr>
	<td>
		 Any other desktop or mobile client&nbsp; 
		<br>
		 that can be connected to&nbsp;Microsoft Exchange&nbsp; 
		<br>
		 and supports folders and/or categories, e.g. 
		<a href="http://support.apple.com/mail">iOS Mail App</a>
	</td>
	<td>
		 Yes
	</td>
	<td>
		 No
	</td>
</tr>
</tbody>
</table>

**\* What 'Yes+Pin' means?** Sidebar Add-In [can be 'pinned'](../Sidebar-Pinning/), so you do not need to reopen it each time browsing different emails or meetings in your email client. Please note, *Outlook 2016* one-time purchase version and older Outlook versions do not support {{ product_name }} pinning. Only *Exchange 2016* and newer Exchange versions support {{ short_name }} pinning

**\*\*** Presently, due to [a limitation in MS Outlook Mobile](https://docs.microsoft.com/en-us/outlook/add-ins/outlook-mobile-addins), in MS Outlook for Android/iOS the Add-In can be used with Office 365/Office.com accounts only. However, your data can be exchanged with Salesforce using [{{ short_name }} sync](../Synchronization-Engine-An-Overview/) (through [auto-syncing](../Configuring-Activities-Synchronization-Settings/#automatic_syncing_of_calendar_items_events_autosharing) or [the custom "Salesforce Emails" folder](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#3_besides_using_the_save_button_emails_saving_can_be_performed_in_4_more_easy_ways)).

&nbsp;



* * *
&nbsp;

Browsers
--------

Since {{ product_name }} is a cloud solution, if used in Office.com/Outlook.com, it can run in a browser. Please check browser's compatibility and update your browser to the latest version for the best experience with {{ product_name }}.

<table>
<tbody>
<tr>
	<td>
		<strong> Browser</strong>
	</td>
	<td>
		<strong> Support</strong>
	</td>
</tr>
<tr>
	<td>
		 Chrome & Chromium-based
	</td>
	<td>
		 Full
	</td>
</tr>
<tr>
	<td>
		 Safari (Including iOS version)
	</td>
	<td>
		 Full
	</td>
</tr>
<tr>
	<td>
		 Android Mobile browser
	</td>
	<td>
		 Full
	</td>
</tr>
<tr>
	<td>
		 MS Edge
	</td>
	<td>
		 Compatible
	</td>
</tr>
<tr>
	<td>
		 Firefox
	</td>
	<td>
		 Compatible
	</td>
</tr>
<tr>
	<td>
		 Opera
	</td>
	<td>
		 Compatible
	</td>
</tr>
<tr>
	<td>
		 Internet Explorer 11, 10, 9 or lower
	</td>
	<td>
		 No
	</td>
</tr>
</tbody>
</table>
&nbsp;

!!! note "Note"
    If your email client is Microsoft Outlook for Windows, please make sure the latest version of MS Edge is installed in your system because it is used to render the Sidebar in Outlook

&nbsp;
* * *
&nbsp;

Supported Email Clients for Gmail 
--------

{{ product_name }} can work with Gmail and G Guite servers only through the dedicated [Chrome Browser Extension](https://chrome.google.com/webstore/detail/revenue-inbox-for-salesfo/agfekjndkedoakoeahndfnjilkifbicn?hl=en) that is added to Gmail / Google Workspace (G Suite) web interface. See [this article](../Chrome-Extension-Intro/) for more information.

{{ short_name }} for Salesforce and Gmail supports the [Sync Engine](../Synchronization-Engine-An-Overview/) and Add-Inn pinning. You can effectively run {{ short_name }} on tablet devices, but please note that the Extension’s rendering is not specifically optimized for using it on mobile phone screens.

The prerequisites to use the {{ short_company_name }} Chrome Extension for Salesforce and Gmail:  

- The latest update of Google Chrome or a Chromium based browser available for your operating system  
- A corporate Gmail / Google Workspace (G Suite) account  
- A Salesforce account  
- Internet connection  

&nbsp;
* * *
&nbsp;

Internet Explorer End of Support 
--------

Since Microsoft stopped supporting the [Internet Explorer 11 desktop application](https://docs.microsoft.com/en-us/lifecycle/announcements/internet-explorer-11-end-of-support) on most versions of Windows 10, {{ company_name }} discontinued support of {{ product_name }} for Internet Explorer and older MS Outlook versions that use the Internet Explorer browser to render add-ins. 


To ensure maximum performance and compatibility, all {{ short_name }} users are recommended to upgrade to Windows 10 build *1903 or above* and Microsoft 365 / Office package version *16.0.11629 or above*.


!!! tip "Tip"
    Refer to [this {{ company_name }} article](../internet-explorer-end-of-support/) to learn more about the MS Outlook versions which are not supported anymore and possible upgrading.   

&nbsp;

&nbsp;



&nbsp;

