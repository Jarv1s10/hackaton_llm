---
description: Troubleshooting: How to address Revenue Grid sync and iPhone/iPad contacts app issue
---
# {{ company_name }} Sync and iPhone / iPad Contacts App Issue
  

<div class="container" style="display: inline-block; height: 42px; width: auto; padding: 1px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/mobile-icon.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! note "Note"
    This issue is specific to iOS and does not occur on devices using Android, MacOS, or Windows OS

If you do either of the following:

- [activate {{ short_name }} sync](../Authorizing-Sync-Engine-to-Work-with-Your-Data/) for a corporate MS Exchange / Office 365 account which is already logged in MS Outlook Mobile on your iPhone/iPad

- log on to your corporate email account with enabled [{{ company_name }} Synchronization](../Synchronization-Engine-An-Overview/) in MS Outlook Mobile on your iPhone/iPad  

that may result in new contacts (phone numbers, email addresses, etc.) you add to the iPhone getting transferred into your Salesforce Org.  
The cause of this behavior is how the default Contacts iOS app handles new contacts: by default, this app is saving new contacts you add to the iPhone with the set Default Account, also auto-selecting all custom categories (Groups) available in this email account to be assigned to them on saving, including the [custom Salesforce category tracked by {{ short_name }} sync](../Synchronization-of-Contacts/#syncing_a_contact_using_the_custom_salesforce_category).  
Thus, if your corporate MS Exchange / Office 365 email account with active {{ short_name }} Sync is set as Default on your iPhone, these contacts will subsequently be auto-saved in your Salesforce Org, as that is the pattern of Contacts handling by {{ short_name }} sync.



To prevent that, make sure that another email account is set as default one in your iPhone instead of the corporate email account synced with Salesforce:

1. Open **iPhone Settings**
2. Select **Contacts**
3. Tap **Default Account**
4. Select a personal account instead of the MS Exchange / Office 365 corporate one

<details><summary>>>> Expand to see the Steps <<<</summary>
<p>
    <div style="text-align:center"><b>(1)</b></b><img src="..\..\assets\images\Using-SmartCloud-Connect\iOS\defaultacc1.png" alt="" width="400"> <br>   <div style="text-align:center"><b>(2)</b><img src="..\..\assets\images\Using-SmartCloud-Connect\iOS\defaultacc2.png" alt="" width="400">  
    </p>
   </details>


&#160;
 &#160;

