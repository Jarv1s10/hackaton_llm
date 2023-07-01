# Troubleshooting: Chrome Extension Startup Errors  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*4 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

The troubleshooting tips listed in this article are specific to [{{ short_name }} Chrome Extension for Gmail](../Using-the-Solution-for-Salesforce-and-Gmail/) implementation.

The errors manifest as the following generic notification "*Sorry, an error occurred ...*" in the Extension's Sidebar after it is opened in Gmail web interface:

<p><img src= "..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\chrome-generic-error.png" style="width: 45%; height: 45%;">
</p>

&nbsp;


The full error notification text:  
*"Sorry, an error occurred, please restart the Sidebar. If the issue persists, contact our Support team for assistance, submit the error ID and the steps that lead to it"*

&nbsp;

In some cases, the error will **not** affect {{ short_name }} Extension's functioning in any way. However, considering that the notification may pop up frequently, you may want to get rid of it.

&nbsp;

## How To Remove The Error Notification


This error may be caused by inaccessibility of your browser's local/session storage. Because of that, {{ short_name }} Chrome Extension cannot save or retrieve the required data from the browser.  

The steps to resolve the issue are similar for the [Chromium-based browsers,](https://en.wikipedia.org/wiki/Chromium_(web_browser)) with several differences in the flow. Please follow the steps below to resolve the issue in Google Chrome and Microsoft Edge web browsers.  

In case the issue persists after suggested steps were performed, please contact [our Support team](mailto:support@revenuegrid.com) by clicking on the link in the Error message.

&nbsp;

### Steps for Google Chrome browser

**1\.** Open Chrome settings, click **Privacy and Security** and open the tab **Cookies and other site data**,  or just open this link: *chrome://settings/cookies*

<details><summary> >>> Click to see screenshots <<< </summary>
<p><img src= "..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\chrome-step1.png">
<br>
<br>
<img src= "..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\chrome-step2.png" class="minimized">
</p></details>  


&nbsp;

**2\.** On the page that opens, make sure that either **Allow all cookies** or **Block third-party cookies in Incognito** is selected. Note that if you select "Block third-party cookies" or "Block all cookies (not recommended)", the following issue will emerge:  

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src= "..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\chrome-step3.png">
</p></details>  

&nbsp;

**3\.** *(Optional)* In case you prefer blocking any third-party cookies by default, on *Step 2* you may select the box **Block third-party cookies**, but then additional configuring is required:  
&nbsp;&nbsp;&nbsp;&nbsp;**3\.1.** Click **Add** next to "*Sites that can always use cookies*" and add *mail.google.com* in the dialog, then make sure that the checkbox **Include third-party cookies on this site** is selected  
&nbsp;&nbsp;&nbsp;&nbsp;**3\.2.** After that, repeat actions from *Step 3.1* for the site *calendar.google.com* to make sure that the issue doesn't occur when you are working with Google Calendar  

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src= "..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\chrome-step4.png">
<br>
<br>
<img src= "..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\chrome-step5.png">
</p></details>  

&nbsp;

After completing these steps, open Gmail or Google Calendar refresh the web page. The issue should be resolved now.

&nbsp;

&nbsp;

&nbsp;

### Steps for MS Edge browser

**1\.** Open browser settings, go to **Cookies and site permissions** and open **Manage and delete cookies and site data**, or just open the link: *edge://settings/content/cookies*  

<details><summary> >>> Click to see screenshots <<< </summary>
<p><img src= "..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\edge-step1.png">
<br>
<br>
<img src= "..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\edge-step2.png" class="minimized">
</p></details>  

&nbsp;

**2\.** On the page that opens, make sure that **Block third-party cookies** is disabled. If this feature is enabled, the same issue will occur

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src= "..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\edge-step3.png">
</p></details>  

&nbsp;

**3\.** *(Optional)* In case you prefer blocking any third-party cookies by default, on *Step 2* you may select the box **Block third-party cookies**, but then additional configuring is required:  
&nbsp;&nbsp;&nbsp;&nbsp; **3\.1.** Click **Add** next to "*Sites that can always use cookies*" and add *mail.google.com* in the dialog, then make sure that the checkbox **Include third-party cookies on this site** is selected  
&nbsp;&nbsp;&nbsp;&nbsp; **3\.2.** After that, repeat actions from *Step 3.1* for the site *calendar.google.com* to make sure that the issue doesn't occur when you are working with Google Calendar  

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src= "..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\edge-step4.png">
<br>
<br>
<img src= "..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\edge-step5.png">
</p></details>  

&nbsp;

After completing these steps, open Gmail or Google Calendar refresh the web page. The issue should be resolved now.  
  
  