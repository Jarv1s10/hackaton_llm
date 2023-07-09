---
description: Detailed information on how to solve the issue with incorrect time displayed in Book Me selection table when opened by a recipient
---
# Incorrect Time Displayed in Book Me Selection Table Opened by a Recipient  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*3 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! tip "Tip"
    Refer to [this article]( ../Sharing-Calendar-Availability-(Adaptive-view)/) for detailed information on using the Book Me feature in {{ product_name }} for Salesforce and Gmail  

&nbsp;

The Book Me (Share Calendar Availability) function allows sharing available periods based on your Google calendar data with your business contacts to schedule a meeting for a time slot convenient for all parties. The rendered availability table with available time slots is generated and sent to the recipient(s) via a Book Me URL.    

If a recipient of the generated Book Me link notifies you that the table displays a wrong time, to resolve the issue you should check your time zone settings; this issue may occur due to the discrepancies between your actual time zone and one set in MS Outlook.    

!!! warning "Important"
    The sent Book Me link is **not** updated automatically you change the time zone. After adjusting the time zone settings, you should [invalidate the previously sent Book Me Link](../Invalidate-Book-Me/) that displayed a wrong time and [create a new Book Me link for the recipient(s)](../Sharing-Calendar-Availability-%28Adaptive-view%29/#to_initiate_a_meeting_by_sharing_your_availability_periods_with_business_contacts).    

&nbsp;

## How to change Time zone settings in Outlook on the Web

To check and if necessary change your time zone:    

**1\.**	Open MS Outlook on the Web (outlook.com, outlook.office.com, outlook.live.com) and log in to the relevant Outlook account, if needed    

**2\.**	After that click on the Gear ⚙ (Settings) button in the upper right corner of MS Outlook main window  

![](../assets/images/Using-SmartCloud-Connect/How-To-s/Troubleshooting/Book-Me-Link-Time-Zone/time_zone_owa_1.png)    

&nbsp;

**3\.**	In the Settings window that opens, find the item **View all Outlook settings** at the bottom and click on it    

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\Book-Me-Link-Time-Zone\time_zone_owa_2.png" class="minimized"></p>

&nbsp;

**4\.** Next, click **Calendar** (1) > **View** (2). Under the *Calendar Appearance* category, you'll find the field "*The current time zone for your meeting hours is*" (3) with the current Time zone settings  

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\Book-Me-Link-Time-Zone\time_zone_owa_3.png" class="minimized"></p>

&nbsp;

**5\.** If your MS Outlook time zone does not match your actual time zone, scroll down to the *Time Zones* category, then select the correct time zone in the drop-down list or start typing the name of time zone location in the **Display my calendar in time zone** field    

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\Book-Me-Link-Time-Zone\time_zone_owa_4.png" class="minimized"></p>

&nbsp;

**6\.** Click **Save** in the bottom right corner of the Settings window to apply the changes

<details><summary> >>> Click to see an animation <<< </summary>
<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\Book-Me-Link-Time-Zone\time-zone-owa.gif" class="minimized">
</p></details>

&nbsp;

* * *
&nbsp;  

## How to change Time zone settings in Outlook Desktop

&nbsp;

To check and if necessary change your time zone:   

**1\.** Launch Outlook Desktop. Click on the **File** tab in the top left corner    

![](../assets/images/Using-SmartCloud-Connect/How-To-s/Troubleshooting/Book-Me-Link-Time-Zone/time_zone_desktop_1.png)    

&nbsp;

**2\.** Select **Options** at the bottom of the menu   

![](../assets/images/Using-SmartCloud-Connect/How-To-s/Troubleshooting/Book-Me-Link-Time-Zone/time_zone_desktop_2.png)  

&nbsp;

**3\.** In the Settings window that opens, click **Calendar** (1). Under the *Time Zone* (2) category, check your current Time zone settings (3)    

&nbsp;

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\Book-Me-Link-Time-Zone\time_zone_desktop_3.png" class="minimized"></p>

&nbsp;

**4\.** If your MS Outlook time zone does not match your actual time zone, select the proper time zone in the drop-down list    

**5\.** Click **OK** at the bottom of the Settings window to apply the changes    

<details><summary> >>> Click to see an animation <<< </summary>
<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\Book-Me-Link-Time-Zone\time_zone_desktop.gif" class="minimized">
</p></details>

&nbsp;

!!! warning "Important"
    The Time zone settings in Outlook Desktop are synchronized with the overall Windows Time settings. Do not adjust them in case your Windows Time settings are correct   
    Also note that adjusting the Primary time zone in Outlook results in Windows Time settings auto-changing    

&nbsp;

See [this article]( https://support.microsoft.com/en-us/office/add-remove-or-change-time-zones-5ab3e10e-5a6c-46af-ab48-156fedf70c04#ID0EBBD=Windows_(newer_versions)) for more information on how to add, remove, or change time zones in MS Outlook.  

&nbsp;



&nbsp;  



&#160;
 &#160;


