# Troubleshooting: Add-In Startup Error On *Loading application data ...*  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

This Add-In error may occur after an end user attempts to log in to {{ short_name }} Add-In, at the screen that reads "Loading application data ...". This error prevents successful Add-In launching.  

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\resource-access.png">
</p>

 &nbsp;

The Correlation ID *b636006a-a181-aa778-7684-etat444c9e46* specified in the notification indicates that a required Microsoft online resource cannot be reached by the Add-In, and for this reason it cannot run.  
The issue is most probably caused by your corporate or individual firewall that blocks the connection to this Microsoft resource. To resolve it, you must allow-list all required resources in your corporate of individual firewall. See [this article](../Overcoming-Firewall-Issues/) for complete information how to do that. In this specific case, it's a JavaScript library on *https://appsforoffice.microsoft.com*.















&nbsp;

&nbsp;



