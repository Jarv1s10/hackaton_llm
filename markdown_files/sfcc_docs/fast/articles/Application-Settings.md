---
description: Detailed overview of application settings in RG Email Sidebar Customization Settings
---
# Application Settings in {{ short_name }} Customization Settings  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*3 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! tip "Tip"  
    See [this article](../Customization-Settings-Explained/) for more detailed overview of {{ product_name }} Customization Settings  
  
Using the controls in the right pane of Customization page you can adjust the following settings defining various aspects of the Add-In's/Chrome Extension's behavior:  

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b1f91272c7d3a0fa9a2e0d0.png)

&nbsp;

*   **Auto-insert Engagement Tracking code (MagicPixel) into composed emails**. Select this checkbox to have [email tracking](../How-to-Use-the-Solution-s-Engagement-Panel/) automatically enabled for all emails you compose and send to external recipients  
*   **Notify when email is opened**. Another setting related to [Engagement panel](../How-to-Use-the-Solution-s-Engagement-Panel/); when enabled, notifications in the Sidebar's bottom toolbar will be displayed when the tracking code is triggered by the recipients of all such emails, as if they were marked as important (pinned) in the Engagement panel by the user  



!!! note "Note"
    The Magic Pixel tracking code only gets auto-inserted into emails if your {{ product_name }} Add-In / Chrome Extension is opened when you create a new email; if it's closed when you compose an email, the tracking code will not be inserted


*   **Do not load related objects lists**. If you select this checkbox, {{ product_name }} will not display related objects in the Sidebar  
*   **Include internal emails into search results**. By default, {{ product_name }} does not display objects related to [internal emails](../Initial-Search-and-Applied-Record-Filters/#internal_emails_corporate_domains_and_the_blocklist). Select this checkbox to allow {{ product_name }} to search for internal email addresses in Salesforce and display all objects related to the opened internal email  
*   **Hide Chatter**. Toggle this setting to show or hide [Chatter access button](../Using-Chatter/) in [{{ product_name }}](../Introduction/)  
*   **Do not allow sharing email message in Chatter feed**. Select this checkbox if you do not want to get auto-generated Salesforce Chatter notifications about emails and attachments processed by {{ product_name }}  
*   **Do not allow attaching .EML files to objects**. This setting defines whether you are allowed to save email messages converted to .eml files with Salesforce objects. See [this article](../Attachments-Handling-%28Basic%29/#the_default_attachment_eml_copy_of_an_email) for more information  
*   **Do not allow to work with email templates**. This setting manages [the possibility to use Salesforce email templates](../Using-Salesforce-Templates/) from {{ product_name }}  
*   **Do not allow to search objects in LinkedIn**. This setting manages the possibility to search an Account or Contact in LinkedIn from {{ product_name }}  
*   **Support Case Assignment Rules**. Enable this setting if you want to have the ability to assign Support Cases in queues via {{ product_name }} using Case Assignment Rules, in order to assign Cases to your colleagues according to you preferences  
*   **Support Lead Assignment Rules**. Enable this setting if you want to have the ability to assign Leads in queues via {{ product_name }} using Lead Assignment Rules, in order to assign Leads to your colleagues according to you preferences  

&nbsp;

&nbsp;


The next block of settings manages several aspects of [saving emails as activities in Salesforce](../Saving-Emails-in-Salesforce-1.-Function-Overview/):

*   **Do not select "Auto-save in thread" by default**. This setting makes the **Auto-save all emails in this thread** checkbox in the **Record email as activity to Salesforce** dialog unchecked by default, so you will need to select this box specifically for those messages you consider worth adding to the relevant correspondence thread in Salesforce. This implies performing an extra action on email processing, but allows saving some storage space in your Org

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5bace2e3042863158cc6d0ed.png)

&nbsp;

!!! note "Note"
    In case [Auto-Save Emails in Threads synchronization setting](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_email_threads) is enabled and this box is selected, when you save an email by clicking the **Save** button, the **Auto-save new emails within this thread** checkbox will still be unselected by default and you will have to manually select it to auto-track the thread in Salesforce

&nbsp;

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5babb4f6042863158cc6c6f3.png)

&nbsp;

* **Edit email body in Save dialog**. See [this article](../Save-Email-Dialog/#editing_saved_emails_body) for complete information about this setting


&#160;
 &#160;

