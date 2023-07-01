---
description: The behavior of saving enhanced emails to extra (unparsed) objects in Salesforce manually via RG Email Sidebar
---
# Saving an Enhanced Email to the Extra Salesforce Object via {{ product_name }}
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! note "Note"
    This article is applicable only if the Enhanced email Salesforce feature is enabled in your Org's configuration. Refer to [this Salesforce article](https://help.salesforce.com/s/articleView?id=sf.emailadmin_enhanced_email_overview.htm&type=5) for more information about the Enhanced email feature

<br><br>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-It-Works\enhanced-email-saving\linked-records1.png" style="width:42%; display:inline-block; vertical-align:middle; margin-left:2%;float: right">
</p>

Besides the manual and automatic [saving of email messages](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-%28Adaptive-view%29/) to the related [Salesforce objects parsed from the email's](../Initial-Search-and-Applied-Record-Filters/) "To", "CC", and "BCC" fields, body, and signature, {{ product_name }} allows saving email messages to any Salesforce object using the **Linked records** search box in [**Save email** dialog](../Save-Email-Dialog/#save_email_dialog).
Such saving method is characterized with a specific handling of such items on the Salesforce side.

<br><br><br><br>

Saving an [Enhanced email message](https://help.salesforce.com/s/articleView?id=000381944&type=1) manually to the extra (unlinked) Salesforce object results in **adding the object's email address to the "CC" field** of the Enhanced email in Salesforce,

<details>
    <summary>>>> Click to see a screenshot <<<</summary>
    <p>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\How-It-Works\enhanced-email-saving\sf-email.png">
    </p>
</details>

<br>

even if it is absent in the primary email message in MS Exchange / Office 365 / Gmail.

<details>
    <summary>>>> Click to see a screenshot <<<</summary>
    <p>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\How-It-Works\enhanced-email-saving\outlook-email.png">
    </p>
</details>

<br><br><br>

It is an expected behavior and should be considered when saving [Enhanced emails](https://help.salesforce.com/s/articleView?id=000381944&type=1) to the extra Salesforce objects via {{ product_name }}.