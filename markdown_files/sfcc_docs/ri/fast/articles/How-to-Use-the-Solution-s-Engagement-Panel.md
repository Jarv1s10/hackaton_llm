---
description: The principles of working with the RGES Engagement panel
---
# How to Use the Solution's Engagement Panel  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*9 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

In the latest {{ short_name }} updates the [Magic Pixel customer engagement tracking feature](../Tracking-Customer-Engagement-with-Magic-Pixel-(Adaptive-view)/) was revamped into a full-fledged Engagement panel.

!!! warning "Important"
    An inserted Magic Pixel tracking code is displayed at composed email Body's [first or the last line](../How-to-Use-SCC-Engagement-Panel-%28Adaptive-view%29/#tracking_code_insertion_to_the_first_line) as a blinking dot in MS Outlook Desktop or as a blank line in MS Outlook on the Web, make sure not to delete it when your edit the email or tracking will **not** be performed 

&nbsp;

This tool allows you to monitor engagement of your business contacts with your emails. After you send an email with the tracking code (the "Magic Pixel") inserted, the following data is collected and conveyed to you in real-time mode via {{ short_name }} Engagement Panel:

- **Date and time** (in your timezone) when the email is opened by the recipient(s)
- **Country / state, city** - approximate geolocation where the email was opened. To see it, you need to hover the cursor over the <img src="../../assets/images/Using-SmartCloud-Connect/How-To-s/Engagement-Panel/location_pin.png" style="display: inline-block;vertical-align: middle;width: 18px;margin-left: 1px;height: 14px;object-fit: contain;"> icon
- **Device type** from which the email was opened (desktop or mobile device)

&nbsp;

The renewed Engagement panel has the following improvements:

- You can reset the new email opens count indicator on the Engagement panel icon by holding he *Control (Ctrl)* key and double *left-clicking* on the icon
- Implemented an additional [Customization setting](../Customization-Settings-Explained/#2_application_settings) that regulates Engagement notifications displaying for emails to external (not in-org) contacts with auto-inserted tracking code; the setting's name is *Notify when email is opened*. When it is enabled, the red number indicator in {{ product_name }}’s bottom toolbar will be increased when the tracking code is triggered by a recipient of any such email, as if they were marked as Important by the user
- The feature is now also available in [{{ short_name }} for Salesforce and Gmail Chrome Extension](../Using-the-Solution-for-Salesforce-and-Gmail/). The only essential difference is that in the Chrome Extension the only way to add the tracking code is by [enabling its automatic insertion into all composed emails](../Tracking-Customer-Engagement-with-Magic-Pixel-(Adaptive-view)/#tracking_all_sent_emails) via {{ short_name }} Customization settings
- Each email opening is logged in reverse chronological order (the latest openings on top)
- Email openings data is conveniently organized in the Engagement panel as separate expandable communication threads, in which the new emails you send are also logged
- You can mark correspondence threads of especial importance by clicking on the *Pin* 📌 icon next to them to view a notification in the Sidebar's bottom toolbar on email opening. Note that the refresh rate for these notifications is 5 minutes

![](../assets/images/Using-SmartCloud-Connect/How-To-s/Engagement-Panel/notifications.png)

&nbsp;

- Clicking on a thread name in Engagement panel opens the latest email message in this thread
- A search box was implemented on top of Engagement panel, so you can quickly find needed threads by email address, subject, recipient's name and surname
- In addition, in the latest {{ short_name }} updates you can filter engagement data by time period when the tracking code was triggered, by recipients' email domain (company), or by the [Sequence](https://docs.revenuegrid.com/articles/Sequences/) or [Step](https://docs.revenuegrid.com/articles/Create-new-sequence/#adding_and_editing_steps_toof_a_sequence) it belongs to in [{{ company_name }}](https://docs.revenuegrid.com/)

![](../assets/images/Using-SmartCloud-Connect/How-To-s/Engagement-Panel/full_view.png)

&nbsp;

!!! warning "Important"
    If an email containing the tracking code is sent to multiple recipients, there is no technical possibility to detect which one of them opened the email at a specific moment.  
    Also, please note that email openings from your local IP subnet do not get registered in Engagement panel. Therefore, if yourself or colleagues from your office open an email with inserted tracking code, that will not be reflected in the logs.  
    The engagement tracking data for every email open or link click is stored in {{ short_name }} Engagement panel only for 90 days

&nbsp;

* * *

&nbsp;

The feature is based on adding a tiny and secure tracking code snippet into email message body's html. When the recipients open the message in their email clients, the code is triggered; it collects the opening time, device type, and IP location data and passes this information directly to your {{ product_name }} Add-In.



!!! note "Note"
    Note that the Track Email Opens button is only available for emails opened in [Compose mode](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#2_when_smartcloud_connect_sync_is_not_active)

&nbsp;

* * *

&nbsp;

#### **To insert the tracking code (Magic Pixel) into an email message**

**1\.** Create a new message in MS Outlook Desktop or Web by clicking **New Email**, **Reply/Reply All**, or **Forward**  
**2\.** Insert tracking code into the message in one of the following ways, depending on whether you are using MS Outlook Desktop or Web:  

&nbsp;&nbsp;&nbsp;&nbsp;In MS Outlook Desktop: 

- click the *Magic wand* icon (**Track Email Opens**) next to the *Open {{ product_name }}* icon in MS Outlook ribbon  
  Once the tracking object is inserted, you will see a UI-less confirmation line above the message

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b6ac45c0428631d7a89c287.png" class="minimized">
</p>

&nbsp;
or

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp; In Outlook on the Web (outlook.com, outlook.office.com, outlook.live.com):  

##### Tracking code insertion to the first line

**1\.** [Open {{ product_name }}](../Open-in-Outlook-Web/)

**2\.** [Expand {{ product_name }} menu >](../Open-in-Outlook-Web/) and select **Track Email Opens**

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b6ac49d2c7d3a03f89d7709.png" class="minimized">
</p>

&nbsp;

##### Tracking code insertion to the last line

In Outlook on the Web the tracking code can also be inserted to the last line of a composed email. To do that, perform the step *2.* described above, but make sure that {{ product_name }} is closed.



&nbsp;

&nbsp;

After the tracking code is inserted, you will see a UI-less confirmation line above your email.

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b6ac4ea0428631d7a89c28d.png" class="minimized">
</p>

&nbsp;

* * *

&nbsp;

#### To view collected tracking information in the Engagement panel

1. Open [{{ product_name }}](../Introduction/) in MS Outlook on the Web or Desktop
2. Click **Engagement** in the bottom toolbar

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b6ac5312c7d3a03f89d7714.png)

!!! warning "Important"
    Engagement data for a tracking code that was not triggered for over 14 days is excluded from being displayed in the Engagement panel

&nbsp;

After you open the Engagement panel, you will see two major item categories:

- **Pinned emails**, summarizing data about recipients' engagement through email threads in which the tracking code was selectively inserted by {{ short_name }} users, and
- **Other tracked emails**, summarizing data about recipients' engagement through email threads in which the tracking code was inserted automatically

&nbsp;

The numbers you see next to the Engagement icon stand for the number of Pinned (marked as important) threads in which new recipients' engagement actions were registered.

![](../assets/images/Using-SmartCloud-Connect/How-To-s/Engagement-Panel/counter.png)

&nbsp;

**Detailed use cases:**

- for example, if you manually inserted the tracking code into an email communication thread with prospect A and into two more email threads with prospects B and C
- all these threads will be added into the **Pinned emails** category
- if the prospect A opens the email and then email correspondence between you goes back and forth:  
  • the overall engagement updates count will remain 1, regardless of how many emails are sent and received in a pinned thread  
  • you will see a red counter "1" on the Engagement icon, indicating that 1 of the pinned threads had an engagement update   
- If at any point of this communication you view the prospect A's engagement logs, its engagement count will be reset, like it happens with iPhone message notifications, for example. And when the prospect A opens the email thread once again, that be counted as a new engagement update, with a corresponding notification  
- The count will increase to 2 or 3 only if engagement updates are registered in other pinned threads, with the prospects B and C  

&nbsp;

This functionality allows {{ short_name }} users to actively monitor engagement updates in real time for the most important threads; the delay between tracking code triggering by a recipient and notification appearance on the Engagement panel is around 5 minutes.
At that, note that network restrictions on the recipients’ side may block the tracking code's callbacks, thus making precise engagement tracking impossible for some recipients. See the section [Engagement Panel / Email Openings Statistics Limitations](../How-to-Use-the-Solution-s-Engagement-Panel/#engagement_panel_email_openings_statistics_limitations) below for more information.

&nbsp;

&nbsp;

* * *

&nbsp;



#### Tracking All Emails and Meeting Invites You Compose

!!! tip "Tip"
    Only this method can be used in [{{ product_name }} Chrome Extension for Gmail](../Chrome-Extension-Intro/)

{{ product_name }} allows automatically inserting the tracking code into all emails you are sending (excluding ones sent to [internal/blocklisted addresses](../Initial-Search-and-Applied-Record-Filters/)). To enable this option, enter [{{ product_name }} Customization page](../Customization-Settings-Explained/) and select the **Auto-insert MagicPixel into all composed email messages** checkbox under **Other settings**, **Application settings** on the right-hand side of the page and then click **Save** in the slide-down panel at the top of the page to apply the customization setting.

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b6ac8990428631d7a89c2be.png" class="minimized">
</p>

&nbsp;

!!! warning "Important"
    Note that *every* opening by different recipients of the email message with tracking code from different devices is registered and then displayed in the Add-In, unless one of described below limitations applies

&nbsp;

* * *

&nbsp;

#### Engagement Panel / Email Openings Statistics Limitations

*   The tracking code cannot be inserted into a plain text or rich text format message, so in order to be tracked [your email must be in html](https://support.office.com/en-ie/article/change-the-message-format-to-html-rich-text-format-or-plain-text-338a389d-11da-47fe-b693-cf41f792fefa); also, it will not be triggered if the recipient’s mailbox is configured to view received messages as plain text

*   The feature uses the recipient’s IP address to identify their approximate location; the IP cannot be determined if the recipient is using a VPN or proxy connection, a firewall, or other privacy and security measures which block IP address capturing. For the same reason in some cases the approximate location retrieved via tracking code is not accurate

*   If the IP address of the device on which the email is opened and the sender’s IP address are identical, email opening will not be registered and the location will not be logged

*   If a recipient is using Gmail / Google Workspace (G Suite) email client, Outlook.com, or some other public email services, no real information about their location can be collected, so a false location based on [Gmail IP addresses range](https://www.lifewire.com/what-is-the-ip-address-of-google-818153) or [Outlook.com addresses range](https://docs.microsoft.com/en-us/office365/enterprise/urls-and-ip-address-ranges) will be read, indicated as "Gmail" or "Outlook.com"

*   Some email clients may block images inserted inline into email messages, including one used in the tracking code that {{ product_name }} uses to register email opening. For example, MS Outlook (Desktop) will not allow tracking code to trigger unless the recipient allows downloading inline images via the “*Click here to download pictures. To help protect your privacy, Outlook prevented automatic download of some pictures in this message*” dialog

&nbsp;

* * *

&nbsp;

#### Engagement data logging in Salesforce

Sometimes it is handy to have Engagement tracking data indicated in [Tasks](../Object-Fields-Mapping-Patterns/#ms_outlook_emails_ms_exchange_salesforce_sharing) or [EmailMessages](https://help.salesforce.com/articleView?id=emailadmin_enhanced_email_overview.htm&type=5) that match these emails in Salesforce, specifically the date and time of the first and the latest email opens, for instant reference and engagement decision making. {{ product_name }} provides this possibility upon request.  

The custom fields for *First Open* and *Last Open* date and time logging can be added to Salesforce Task or EmailMessage objects either by installing [{{ company_name }} managed package](../Admin-Managed-Package/) or [manually](https://www.forcetalks.com/salesforce-topic/how-to-create-a-custom-field-on-a-standard-salesforce-object/) by your local Salesforce Admin.   

After this function is enabled by our Support team, {{ product_name }} will be logging this Engagement tracking data in Salesforce Tasks or EmailMessages for all emails with inserted tracking code which were sent with [{{ product_name }}](../Introduction/) opened in MS Outlook and saved in Salesforce by {{ product_name }}, these are two essential prerequisites to make this feature work.    

Note that the values in the field *Last Open* get refreshed each time the email is opened from an IP not registered as one used in your Org.


!!! warning "Important"
    Note that to improve involved APIs' performance, the automatic clean up of engagement tracking logs in the DB after a certain period was implemented. 

&nbsp;


&#160;
 &#160;

