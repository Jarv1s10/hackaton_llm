---
description: How to save the emails classified as internal/blocklisted in Salesforce using RG Email Sidebar
---
# How to Save Internal or blocklisted Emails in Salesforce  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

Messages [classified as internal/blocklisted](../Initial-Search-and-Applied-Record-Filters/#internal_emails_corporate_domains_and_the_blocklist) aren't saved in Salesforce automatically; however, in the latest {{ product_name }} updates **Save** button in {{ product_name }} is enabled for them. When such message is selected, to indicate why the message cannot be saved in Salesforce there appears a notification under **Smart Actions** bar > **More...**, **Observations** "_Some not important emails were filtered:_" with the list of internal or blocklisted email addresses from the message.

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b71aff12c7d3a03f89da34e.png)

&nbsp;

You can save any messages from/to internal or blocklisted addresses (as well as [unresolved](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-(Adaptive-view)/#the_new_records_tab) (not yet registered in CRM) addresses) in Salesforce using the **Save** button in {{ product_name }}'s header and then filling in the necessary details in the *Save this email to Salesforce* dialog.



!!! note "Note"
    A possible alternative solution is to create a corresponding "people record" in Salesforce (a Contact or Lead), based on the internal email address in question, so {{ product_name }} will work with this email address in the same manner as with non-internal ones, also enabling auto-syncing for it, if the [corresponding option](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_emails_emails_autosharing) is enabled

&#160;
 &#160;

