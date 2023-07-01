---
description:
---
# Synchronization Saves Unwanted Emails to Salesforce
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container"
        style="
        display: inline-block;
        height: 42px;
        width: 162px;
        padding: 5px 10px;
        background-color: #fff;">
        <img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" 
            style="
        	height: 100%;
            object-fit: contain;
            vertical-align: middle;">
</div>
<div class="container"
        style="
        display: inline-block;
        height: 42px;
        width: 163px;
        padding: 5px 10px;
        background-color: #fff;">
        <img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" 
            style="
        	height: 100%;
            object-fit: contain;
            vertical-align: middle;">
</div>

&nbsp;

*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

## Unexpected email saving explanation

In some cases, you may face a situation where unwanted emails get saved to Salesforce by [{{ short_company_name }} Sync Engine](../Synchronization-Engine-An-Overview/), even if you save emails only manually via the Add-in and the [auto-saving feature](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_emails_emails_autosharing) is disabled in the [Sync Settings](../Configuring-Activities-Synchronization-Settings/).

&nbsp;

The unexpected email saving to Salesforce can be related to the latest MS Outlook update and related MS Outlook behavior that affects only [**Outlook on the web**](https://www.microsoft.com/en-us/microsoft-365/outlook/web-email-login-for-outlook) and the [**new Outlook for Mac**](https://support.microsoft.com/en-us/office/the-new-outlook-for-mac-6283be54-e74d-434e-babb-b70cefc77439) (not the Legacy Outlook version):

* According to the updated logic, when you reply to or forward an email message with any categories, the **same categories are assigned** to your reply or email that forwards the original one

<br><br>

Therefore, if the original email has a Salesforce category, the new linked email message will also get a Salesforce category, which will trigger [{{ short_company_name }} Sync Engine](../Synchronization-Engine-An-Overview/) to save this email to Salesforce according to the [saving by category functionality](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-%28Adaptive-view%29/#31_by_assigning_the_salesforce_email_category).

That is expected product behavior, so if you save an email to Salesforce, it automatically gets the Salesforce category in Outlook. Then, if you forward this email to your manager within your internal correspondence, the Salesforce category will also be assigned to this internal email, and, as a result, it will be saved to Salesforce.

&nbsp;

***

&nbsp;

## How to handle the unexpected email synchronization

Check and verify that you are using [Outlook on the web](https://www.microsoft.com/en-us/microsoft-365/outlook/web-email-login-for-outlook) or the [new Outlook for Mac](https://support.microsoft.com/en-us/office/the-new-outlook-for-mac-6283be54-e74d-434e-babb-b70cefc77439) to confirm that the unexpected email saving is caused by updated Outlook behavior. Refer to [this Microsoft article](https://support.microsoft.com/en-us/office/what-version-of-outlook-do-i-have-b3a9568c-edb5-42b9-9825-d48d82b2257c#ID0EBBD=macOS) describing how to check the Outlook version.

<br>

As [saving emails by assigning a Salesforce category](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-%28Adaptive-view%29/#31_by_assigning_the_salesforce_email_category) is an expected product behavior, you can do the following actions to prevent unwanted emails from saving to Salesforce:

* Remove the Salesforce category from the email message manually (refer to [this Microsoft guide](https://support.microsoft.com/en-us/office/delete-a-color-category-417b871e-67f0-41b7-b3db-c4ffed19810e?ui=en-us&rs=en-us&ad=us#bkmk_removecategory:~:text=confirm%20the%20deletion.-,Remove%20a%20color%20category%20from%20a%20message%2C%20contact%2C%20calendar%20item%2C%20or%20task,-There%20are%20several) for detailed instructions)

* Move emails to the dedicated folder that is out of {{ short_company_name }} Sync scope