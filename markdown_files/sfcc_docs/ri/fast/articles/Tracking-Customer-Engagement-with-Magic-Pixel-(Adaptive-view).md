---
description: Learn how to properly track email opens with Tracking Code
---
# Tracking Email Opens with Tracking Code  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*4 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

{{ product_name }} offers an email opening tracking feature called _Tracking Code / Magic Pixel_ or _Email Opens Statistics_. This feature allows you to monitor contacts engagement by tracking the time, location, and device type used to open an email you have sent.  
The feature is based on inserting a special tracking code into composed email message Body, displayed as a blinking pixel in MS Outlook Desktop or a blank line in MS Outlook on the Web. When the recipients open the message in their email clients, the code is triggered; it collects the opening time, device type, and approximate location data and passes this information directly to your {{ product_name }} Add-In.  

!!! tip "Tip"
    The feature is also available in [{{ short_name }} for Salesforce and Gmail Chrome Extension](../Using-the-Solution-for-Salesforce-and-Gmail/). The only essential difference is that in the Chrome Extension the only way to add the tracking code is by [enabling its automatic insertion into all composed emails](../Tracking-Customer-Engagement-with-Magic-Pixel-(Adaptive-view)/#tracking_all_sent_emails) via {{ short_name }} Customization settings.  
At the same time, if the recipients have a Gmail / Google Workspace (G Suite) box, their approximate Location cannot be retrieved



&nbsp;

#### **To insert the Magic Pixel object (tracking code) into an email message:**

!!! note "Note"
    An inserted Magic Pixel tracking code is displayed at composed email Body's [first or the last line](../How-to-Use-SCC-Engagement-Panel-%28Adaptive-view%29/#tracking_code_insertion_to_the_first_line) as a blinking dot in MS Outlook Desktop or as a blank line in MS Outlook on the Web, make sure not to delete it when your edit the email or tracking will **not** be performed  

&nbsp;

**1\.** Create a new message in MS Outlook on the Web or Desktop by clicking **New Email**, **Reply/Reply All**, or **Forward**  
**2\.** Insert the magic pixel object into the message in one of the following ways, depending on your email client:   

&nbsp; &nbsp; &nbsp; &nbsp;**2.1.** In MS Outlook Desktop: click the **Magic wand** icon (**Track Email Opens**) next to the Open {{ product_name }} button in MS Outlook ribbon (only displayed for messages opened in Compose mode).  
Once the tracking object is inserted, you will see a confirmation line above the message. Note that the magic pixel object will reserve some space in the first line of the message.  

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b6ac45c0428631d7a89c287.png" class="minimized">
</p>

&nbsp;

&nbsp; &nbsp; &nbsp; &nbsp;**2.2.** In Outlook on the Web: [expand **{{ product_name }} icon > **](../Open-in-Outlook-Web/) and select **Track Email Opens** in the drop-down menu.  

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b6ac49d2c7d3a03f89d7709.png" class="minimized">
</p>

&nbsp;

Once the object is inserted, you will see a confirmation line above the message. Note that the tracking code object reserves the entire first line of the message in Outlook on the Web (Outlook.live.com / Outlook.office.com).  

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b6ac4ea0428631d7a89c28d.png" class="minimized">
</p>

&nbsp;
&nbsp;

#### **To view collected email opens information**

*   In MS Outlook Desktop: open the relevant message and click the **Email opens** icon in **Smart Actions** bottom toolbar in {{ product_name }}

*   In Outlook on the Web (Outlook.com, Outlook.office.com): open the related message and [expand **{{ product_name }} >**](../Open-in-Outlook-Web/), select **Open {{ product_name }}** from the drop-down menu, then click the **Emails Opens** icon in **Smart Actions** bottom toolbar in {{ product_name }}

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b6ac5312c7d3a03f89d7714.png)

&nbsp;

Refer to [this article](../How-to-Use-the-Solution-s-Engagement-Panel/) to learn how to work with engagement tracking results in Engagement panel.

&nbsp;
&nbsp;

#### Tracking All Sent Emails

{{ product_name }} allows automatically inserting the tracking code into all emails you are sending (excluding ones sent to [internal/blocklisted addresses](../Initial-Search-and-Applied-Record-Filters/)). To enable this option, enter [{{ product_name }} Customization page](../Customization-Settings-Explained/) and select the **Auto-insert MagicPixel into all composed email messages** checkbox under **Other settings**, **Application settings** on the right-hand side of the page and then click **Save** in the slide-down panel at the top of the page to apply the customization setting.  

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b6ac8990428631d7a89c2be.png" class="minimized">
</p>

&nbsp;

!!! warning "Important"
    Note that *every* opening by different recipients of the email message with tracking code from different devices is registered and then displayed in the Add-In, unless one of described below limitations applies

&nbsp;
&nbsp;

#### Tracking Code / Email Opens Statistics Limitations

*   The engagement tracking data for every email open or link click is stored in {{ short_name }} Engagement panel only for 90 days
*   Magic Pixel is a tiny object that is inserted at the beginning of the first line of your email message. If you delete it, the tracking code will not be sent to the recipient and {{ product_name }} will not track the email’s opening. Please make sure to keep the magic pixel object intact  
*   Tracking code cannot be inserted into a plain text message; also, it will not be triggered if the recipient’s mailbox is configured to view messages as plain text  
*   The feature uses the recipient’s IP address to identify their approximate location; the IP cannot be determined if the recipient is using a VPN or proxy connection, a firewall, or other privacy and security measures which block IP address capturing. For the same reason in some cases the approximate location retrieved via Magic Pixel is not accurate  
*   If the IP address of the device on which the email is opened and the sender’s IP address are identical, email opening will not be registered and the location will not be logged  
*   If the recipient is using Gmail email service, no data about their location can be collected, so _GMAIL_ will be indicated in the Location field  
*   Some email clients may block images inserted inline into email messages, including the pixel that {{ product_name }} uses to track email opens. For example, Microsoft Outlook (desktop) will not allow magic pixel to trigger unless the recipient allows downloading inline images via the “*Click here to download pictures. To help protect your privacy, Outlook prevented automatic download of some pictures in this message*” dialog  

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
<div class="banners banner-2">
  <img src="../../assets/images/banners/banner-2.svg" style="width: 100%; height: 100%;">
  <a class="button" href="https://revenuegrid.com/request-demo/?utm_source=kb_rg&utm_medium=referral&utm_campaign=eac_demo&utm_content=banner" target="_blank">Book a free demo</a>
</div>
