---
description: How to auto-crop (clip) the previous message in the email body 
---
# Auto-Cropping (Clipping) of Previous Messages in Email Body  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

By default every new message in an email correspondence thread contains quoted bodies of all previous messages in the thread along with email signatures. If you do not want to save this extra data in Salesforce as part of the latest received or sent email message, {{ product_name }} offers the *Email auto-cropping* option. It works for MS Exchange, Office 365, and Gmail emails.

To use this option, you should get it enabled for your implementation of {{ product_name }} by sending us a corresponding request to [our Support team](mailto:support@revenuegrid.com)

After the setting has been enabled this way, a corresponding checkbox **Crop previous messages in thread** will be added to the "Save this email to Salesforce" dialog:

![](../assets/images/Configuration-&-Settings/User-Settings/Auto-Cropping-of-Previous-Messages-in-Email-Body/cropping.png)

&nbsp;

Please note that this checkbox cannot be used together with the [Auto-save all emails in this thread](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_email_threads) setting.



!!! warning "Important"
    Auto-cropping cannot be performed properly in the following cases:
    1. if the subject of an email in the thread was changed in Compose mode
    2. when fragments of previous messages were copied and pasted into an email
    3. if the email that you are replying to was deleted from MS Exchange / Office 365 before you saved the reply in Salesforce or all message in a thread were deleted

&#160;
 &#160;

