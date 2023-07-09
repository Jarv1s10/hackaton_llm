---
description: Correct handling of MS Exchange Aliases on Processing Emails and Calendar Items using RG Email Sidebar
---
# Handling of MS Exchange Aliases on Processing Emails and Calendar Items  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

Many sales reps and other professionals commonly use [Email aliases](https://support.microsoft.com/en-my/help/12407/microsoft-account-how-to-manage-aliases) in their business correspondence, which results in different email addresses being used for communicating with different contacts. Additionally, this concerns their business meeting activities carried out over MS Outlook calendar as much as their email communication.

{{ product_name }} supports [Gmail / Google Workspace email alliases](https://support.google.com/a/answer/33327?hl=en) handling. {{ short_name }} ensures their recognition, seamless processing of the relevant data and synchronization with Salesforce.

An MS Exchange mailbox user may have up to 3 email aliases retrieved from the server plus an extra address specified in one's Salesforce account, if it differs from them. Thus, up to 4 aliases.

{{ product_name }} manages your and your colleagues' (other users in your Salesforce org) MS Exchange / Office 365 aliases automatically, so you do not need to worry about matching your own and your colleagues' email address aliases set in Salesforce records with addresses used in your communication threads or registered as scheduled meetings' [Attendees](../Calendar-Items-Sync-Special-Patterns-Attendees-Lists,-Private-Items,-Item-Unsharing-and-Deletion/#attendees_lists). The lists of active aliases are retrieved from your MS Exchange / Office 365 on [{{ product_name }} activation](../User-Registration-Wizard/#step_2_mail) or when you [change your email credentials](../How-to-Change-Email-Address-in-Your-Product-Account-Office-365/); it gets automatically updated once a week.

At the same time, please note that when your business contacts are added to your CRM via {{ short_name }}, every record is based on one specific email address. Therefore, any alias email addresses used by your contacts will be viewed by {{ short_name }} as new [unresolved](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-(Adaptive-view)/#the_new_records_tab) entities - however, the Add-In will display [related records](../Initial-Search-and-Applied-Record-Filters/#related_records_retrieval_pattern) based on data in the email's signature and the email domain.



&#160;
 &#160;

