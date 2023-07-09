---
description: How to troubleshoot the browser issue where the Add-in login redirect page continues endlessly loading without any response
---
# How to Resolve Add-In Login Redirect Page Endless Loading
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container"
        style="
        display: inline-block;
        height: 42px;
        width: 162px;
        padding: 5px 10px;
        background-color: #fff;">
        <img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" 
            style="
        	height: 100%;
            object-fit: contain;
            vertical-align: middle;">
</div>
<div class="container"
        style="
        display: inline-block;
        height: 42px;
        width: 163px;
        padding: 5px 10px;
        background-color: #fff;">
        <img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" 
            style="
        	height: 100%;
            object-fit: contain;
            vertical-align: middle;">
</div>
<div class="container"
        style="
        display: inline-block;
        height: 42px;
        width: auto;
        padding: 5px 10px;
        background-color: #fff;">
        <img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" 
            style="
        	height: 100%;
            object-fit: contain;
            vertical-align: middle;">
</div>

&nbsp;

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\redirect-page-endless-loading\one-moment.png" style="width:36%; display:inline-block; vertical-align:middle; margin-left:5px; float: right">
</p>

If during the [login procedure to {{ short_name }} Add-in](../How-to-Install-and-Run-the-Solution-all-configurations/#2_logging_on_to_rg_email_sidebar), after clicking **Connect to Salesforce** button, the login redirect page is opened in the browser with the "One moment please..." phrase and continues loading without any response, that occurs due to several reasons.

This article describes the reasons for the endless loading of the Add-In login redirect page and possible ways to address this issue.

&nbsp;

***

&nbsp;

## Browser ad-blocking stops the Add-in login page opening

The [ad-blocking](https://en.wikipedia.org/wiki/Ad_blocking) software usually added to the browser as an extension can also block the opening of redirect pages, even those not related to the advertising, like login redirect pages.

If you have an ad-blocking extension in your browser, try to disable or remove it temporarily and perform the login procedure to {{ short_name }} Add-in again.

&nbsp;

***

&nbsp;

## Browser cache issue

Another reason for the endless loading of the Add-In login redirect page is related to the [browser cache](https://www.microsoft.com/en-us/microsoft-365-life-hacks/privacy-and-safety/how-to-clear-cache). The cache is certain information downloaded by your browser intended to improve the browser loading performance, but sometimes the outdated cached data can lead to website loading issues.
<br><br>

To troubleshoot the browser cache issue, try to clear your browser cache and perform the login procedure to {{ short_name }} Add-in again.

Refer to the following articles on clearing the cache in [Google Chrome](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop), [Firefox](https://support.mozilla.org/en-US/kb/how-clear-firefox-cache), [Microsoft Edge](https://support.microsoft.com/en-us/microsoft-edge/view-and-delete-browser-history-in-microsoft-edge-00cf7943-a9e1-975a-a33d-ac10ce454ca4), and [Safari](https://support.apple.com/guide/safari/manage-cookies-sfri11471/mac).

&nbsp;

***

&nbsp;

## Browser settings issue

If the troubleshooting steps described above have not resolved the Add-In login redirect page loading issue, the reason can be related to the browser settings. To verify that the problem is in the current browser, copy the Add-in login redirect page URL and try to open it in a different browser. If the Add-in login page loads successfully in a different browser, it confirms that the issue is related to the initial browser.
<br><br>

To troubleshoot the browser settings issue, try to reset your browser settings to default and perform the login procedure to {{ short_name }} Add-in again.

Refer to the following articles on returning the browser to default settings for [Google Chrome](https://support.google.com/chrome/answer/3296214?hl=en), [Firefox](https://support.mozilla.org/en-US/kb/refresh-firefox-reset-add-ons-and-settings), [Microsoft Edge](https://malwaretips.com/blogs/reset-microsoft-edge/), and [Safari](https://malwaretips.com/blogs/how-to-reset-safari-to-default-settings-mac-guide/).