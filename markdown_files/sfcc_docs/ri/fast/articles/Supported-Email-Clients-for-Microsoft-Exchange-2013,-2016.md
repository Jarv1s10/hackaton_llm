---
description: Learn about RG Email Sidebar compatibility with MS Exchange 2016, 2019 Email Clients
---
# Supported Email Clients for MS Exchange 2016, 2019  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

Please find the list of compatible email clients below. Note, it's recommended to update your email client to the latest version for the best experience with {{ product_name }}.

!!! note "Note"
    Pay attention that starting from June 2022, [Microsoft ceased support and updates of the Internet Explorer 11 desktop application](https://learn.microsoft.com/en-us/lifecycle/announcements/internet-explorer-11-end-of-support) on most versions of Windows 10 and encouraged its customers to move to other browsers. Since the MS Outlook 2013 for desktop uses Internet Explorer 11 engine to render embedded add-ins in its interface, it will be impossible to run {{ product_name }} on this version of MS Outlook. Learn more in [this {{ short_company_name }} article](https://docs.revenuegrid.com/ri/fast/articles/internet-explorer-end-of-support/) 
    

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

**\* What 'Yes+Pin' means?** the Add-In’s Sidebar [can be 'pinned'](../Sidebar-Pinning/), that is, set to open automatically for relevant items you select, so you will not need to open it every time when browsing emails or meetings in your email client.  
**\*\*** Presently, due to [a limitation in MS Outlook Mobile](https://docs.microsoft.com/en-us/outlook/add-ins/outlook-mobile-addins), in MS Outlook for Android/iOS the Add-In can be used with Office 365/Office.com accounts only. However, your data can be exchanged with Salesforce using [{{ short_name }} sync](../Synchronization-Engine-An-Overview/) (through [auto-syncing](../Configuring-Activities-Synchronization-Settings/#automatic_syncing_of_calendar_items_events_autosharing) or [the custom "Salesforce Emails" folder](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#3_besides_using_the_save_button_emails_saving_can_be_performed_in_4_more_easy_ways)).

!!! note "Note"
    If your email client is Microsoft Outlook for Windows, please make sure the latest version of MS Edge is installed in your system because it is used to render the Sidebar in Outlook
&nbsp;
* * *
&nbsp;


### Browsers


Since {{ product_name }} is a cloud solution, if used via [Outlook on the Web](https://en.wikipedia.org/wiki/Outlook_on_the_web) it can run in a browser. Please check browser's compatibility and update your browser to the latest version for the best experience with {{ product_name }}.

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
		 Safari (incl. the iOS version)
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


&#160;
 
 
<style>
  .banners {
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .banners a.button {
      background-color: #FFC827;
      color: #2F3341;
      box-shadow: 0 5px 35px rgba(146, 146, 146, 0.2);
      padding: 20px;
      font-family: Graphic, arial;
      font-weight: 600;
      line-height: 24px;
      margin-top: -100px;
      border-radius: 3px;
      cursor: pointer;
      transition: .1s;
  }

  .banners a.button:hover {
    transform: scale(1.05);
  }

  .banners a.button a:hover,
  .banners a.button a:visited {
      color: #2F3341;
  }

  .banner-3 a.button {
    margin-left: 45%;
  }
</style>


<br>
<div class="banners banner-3">
  <img src="../../assets/images/banners/banner-3.svg" style="width: 100%; height: 100%;">
  <a class="button" href="https://revenuegrid.com/sign-up/?utm_source=kb_rg&utm_medium=referral&utm_campaign=eac&utm_content=banner" target="_blank">Try {{ company_name }} for free</a>
</div>

