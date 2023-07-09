---
description: Guide on using Salesforce email templates via the RG Email Sidebar
---
# How to Use Salesforce Email Templates via the Sidebar  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*3 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

## Email reply templates

[Salesforce email templates](http://help.salesforce.com/articleView?id=email_templates_lightning_parent.htm&type=5) help you effectively increase the speed of composing typical responses for the customers. With {{ product_name }} Add-In / Chrome Extension you can use both popular Salesforce message templates and customized Lightning Experience email templates to initiate and maintain business correspondence. In addition to that, {{ product_name }} will automatically populate the template you chose with key data retrieved from a relevant Salesforce record or the email's body and signature. The templates can be easily customized in Salesforce according to your specific needs.

To compose a message based on a Salesforce email template in {{ product_name }} opened MS Outlook on the Web or Desktop:  

**1\.** Compose a new message by clicking **New email** or **Reply** or select a message you want to respond to in MS Outlook Desktop or On the Web version  

**2\.** At the bottom of {{ product_name }}, click **More...** > **Templates**  

   ![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5bad1c51042863158cc6d3c8.png)

&nbsp;

**3\.** In the **Email Templates** dialog that appears, populate the necessary fields:  

   ![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5bb790f82c7d3a04dd5b5834.png)

&nbsp;

   **3\.1.** In the **Template folder** field, select a customly created Salesforce templates folder or leave the default folder _All templates_.  
   **3\.2.** In the **Template name** field, select the Salesforce or Lightning Experience email template to use  


_Standard Salesforce templates selection:_

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5bb79725042863158cc71d49.png)

&nbsp;

   **3\.3.** In the **Recipient record** field, select the contact or lead to whom the email message is addressed. The record's data will be autofilled in the template's *{ }* merge fields    
   **3\.4.** In the **Related to record** field, select a record you want to link it with in Salesforce (for example, a support case or opportunity). The record's data will be autofilled in the template's *{ }* merge fields   

**4\.** Click **Insert** to put the text of the template into a message you created or compose a new email based on selected template  

!!! tip "Tip"
    In the latest {{ product_name }} updates recently used templates are stored for quick selection

&nbsp;

* * *

&nbsp;

## Custom Meeting Scheduler templates

In the latest {{ product_name }} updates you can customize HTML layout and text content of standard messages used for organizing meetings via {{ short_name }}'s [Send meeting Time slots](../How-to-Send-Meeting-Time-Slots-(Adaptive-view)/) and [Share calendar availability (Book me)](../Sharing-Calendar-Availability-(Adaptive-view)/) features. There are three [Salesforce templates](https://help.salesforce.com/articleView?id=email_templates_lightning_parent.htm&type=5) involved:

**1\.** the message containing suggested time slots link(s)  
**2\.** the message containing the parsed availability spans table link  
**3\.** the notification sent out after a time slot was selected  

&nbsp;
&nbsp;

### **To create a custom template:**

- follow the steps provided in [this Salesforce help article](https://help.salesforce.com/articleView?id=creating_custom_html_email_templates.htm&type=5) - *Custom (without using Letterhead)*  

- make sure to include the following parameters into the HTML template you create: 
  - for template type 1 (time slots):  
    - *{!Duration}* meeting duration that is set in *Send meeting time slots* step 1  
    - *{!TimeSlots}* the list of meeting time slots URLs selected in *Send meeting time slots* step 2
    - *{!TimeZone}* meeting organizer's time zone  

  - for template type 2 (availability spans)  
    - *{!BookingURL}* link to the parsed availability spans table generated by Meeting Scheduler  

  - for template type 3 (notification sent out to the attendee(s))  
    - *{!Title}* meeting title (subject) srting  
    - *{!Description}* meeting description (body)  
    - *{!Date}* meeting date string; the US time format is used, e.g. "June 15"  
    - *{!DateTime}* the date and time string, as in the default notification  
    - *{!Invitees}* list of email addresses of the attendees  
    - *{!Location}* the location string  

- send your created custom templates' *unique names* to [{{ company_name }} support team](mailto:support@revenuegrid.com) and we will enable them for your Org  



&#160;
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
