---
title: User level settings of Revenue Grid
description: Learn how to configure Revenue Grid user level settings for maximum performance
---



# General Settings of Revenue Grid

<p style="font-size:15px"><i>8 min read - updated few hours ago</i> </p>
<!-- ShareThis BEGIN -->
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis -->
<br>

<p> <img src="../../assets/images/01122022/opensettings.png" style="margin-left:15px;  float: right; width: 25%; height: 25%;">Settings page is used to view and adjust the basic parameters of user activities in Revenue Grid (RG).<br>
<br>
To access Revenue Grid Settings, click the Settings icon in the top right corner of the RG interface.<br>
<br>
Now more detailed about every of the tabs.<br><br>
</p>
<br>
<hr>


<p> <img src="../../assets/images/07272022/4.png" style="margin-right:15px;  float: right; width: 40%; height: 40%;">
Go to Setting → <b>My account</b> subtab. It indicates current RG user's display name and email address. You can't change it, since it's being pulled from your CRM and email accounts.
<br><br>
<br><br><br>
</p>
<hr>

## Sequences settings

On the Sequences tab, you can configure the General, Signature, Merge fields, Editor and Blocklist settings.

### Update role

<p><img src="../../assets/images/2302/role.png" style="margin-right:15px; margin-left:15px; float: right; width: 50%;">
</p>
Specify what is your role in terms of sequences - admin or user.
<br><br><br><br><br>

### Configure notifications

<p><img src="../../assets/images/2302/notifications.png" style="margin-right:15px; margin-left:15px; float: right; width: 50%;"></p>

In the <b>Notifications</b> section you can select the rules for receiving notifications. 
<br><br>
When the <b>Place all undelivered email reports into notifications</b> checkbox is unselected, no undelivered emails will be shown in the Action Center, though still will be counted as Bounced in a <a href="../Analytics/"><i>Sequence's</i> statistics</a>. When the checkbox is selected, you will find undelivered emails in the Notifications tab of the Action Center.  
<br><br>
The <b>Receive daily sequence digest</b> checkbox controls whether you receive daily sequence's digest to your email or not. If the checkbox is selected, but you still don't receive the digest, it means the digest option is turned off for your organization. Contact you Revenue Grid Signal manager.


<br><br><br><br>

### Set numbers for sending SMS and making voice calls

<p><img src="../../assets/images/2302/phone.png" style="margin-right:15px; margin-left:15px; float: right; width: 50%;">
In addition, when <a href="../admin-settings/#select_sms_and_call_provider">Admin level SMS setting is set</a>, you can choose a single number from the <b>SMS number</b> dropdown list or enter a new phone number manually. This number will be reserved for executing SMS type of steps only of your sequences.
<br><br>
Similarly, you can choose a single number from <b>Voice number</b> dropdown list or enter a new phone number manually. This number will be reserved for executing call type of steps only of your sequences.
<br>

</p>
<br>

### Specify country and time zone for scheduling steps

<p><img src="../../assets/images/2302/sending.png" style="margin-right:15px; margin-left:15px;  float: right; width: 50%;"></p>
<p>
In the <b>Sending</b> section, you can specify the <b>Default country code</b>. The specified country's calendar is used when planning Sequence steps for Recipients with no specified country to schedule steps only on business days.
<br><br>
Also, here, you can select the <b>Default time zone</b> to be used when planning Sequence steps for Recipients with no specified time zone. 
</p>

<br><br><br>

### Pause/start sequences-related activity

<p><img src="../../assets/images/2302/pause-start.gif" style="margin-right:15px; margin-left:15px;  float: right; width: 50%;"></p>
In the <b>Sequences activity</b> section you can manage all your user sequence activities - <b>pause</b> and <b>restart</b> them on specified dates. These settings are especially useful when you need to temporarily stop sending sequences, for example, while you are on a vacation.

<br><br>
<hr>
 
 
### Manage signatures

<p><img src="../../assets/images/07272022/5.png" style="margin-right:15px; margin-left:15px;  float: right; width: 40%; height: 40%;">
Go to <b>Signature</b> subtab. Here you can set up signatures which will be used in your RG emails. Use <i>Primary signature</i> or <i>Secondary signature</i> Signature types of <a href="../Using-Merge-Fields/">RG merge field</a> in order to add these signatures to Sequences' steps.
<br><br>
You can set up 2 different signatures, <i>Primary</i> and <i>Secondary</i>. They can be used in various cases, e.g. intended for prospects who speak different languages, or when you want your replies and new threads signed differently. 
</p>
<br><br><br>
<p><img src="../../assets/images/2302/auto-insert-rule.gif" style="margin-right:15px; margin-left:15px;  float: right; width: 40%; height: 40%;"></p>
Using the <b>Auto-insertion rule</b> drop-down list, you can specify when to use one or another signature:
<br><br><br><br>
<p style="margin-left:4%;">
<ul>
<li><b>Add primary signature to sequence emails</b> – select this option if you want the signature to be automatically added to all email type of steps sent by Sequences.</li><br>
<li><b>Add primary signature only to the 1st email in every new thread</b> – select this option if you want the signature to be used only in "New thread" type of email Steps, rather than in "Reply". You choose the type when <a href="../Create-new-sequence/#email_type_of_a_step">adding or editing an email type of a step</a>.</li><br>
<li><b>Add primary signature to the 1st email and secondary to all next emails</b> – select this option if you want the Secondary signature to be added to every email sent in a Sequence starting from the second step. With this option selected, the primary signature is automatically added only to the first email.</li><br>
<li><b>Do not add signature</b> – select this option if you do <b>not</b> want any signature to be automatically added to sequences' emails.</li>
</ul>
</p>


<br>
<div style="margin-left:2%;"; class="admonition hint">
<p class="admonition-title">Auto inserted Signature</p>
<p>Keep in mind that based on selected preferences of auto-adding a signature to sequence emails, you will see a special tag <i>&lcub;&lcub;Auto inserted Signature&rcub;&rcub;</i> in the email body editor when creating or editing <i>an email type of step</i>.
<br><br>
When there is &lcub;&lcub;Auto inserted Signature&rcub;&rcub;, then Primary nor Secondary signature merge fields will not appear when you try to add them manually.
</p>
</div>

<p style="margin-left:2%;">
<img src="../../assets/images/10082021/sign-new.png" style="display: inline-block;vertical-align: middle;width: 100%;margin-left: 1px;height: 100%;object-fit: contain;">
</p>

<p style="margin-left:5%;"> 
• Make use of the standard formatting tools located above the body field to format the signature 
<br><br>
• You can import a signature from a preferred HTML editor or from your MS Outlook/Office 365/Gmail. In order to create such signatures, switch the Source code (HTML) mode by clicking the <i>Source</i> on the bottom of the editor, and paste the preferred signature into it.</p>

<p  style="margin-left:5%;">  • <img src="../../assets/images/Settings/addlink.png" style="display: inline-block;vertical-align: middle;width: 25px;margin-left: 1px;height: 25px;object-fit: contain;"> Add URLs into the signature and define how the URLs will be displayed and opened. If you need to remove an URL (unlink), click on the URL placement word or phrase and then click the <img src="../../assets/images/Steps/unlink.png" style="display: inline-block;vertical-align: middle;width: 23px;margin-left: 1px;height: 23px;object-fit: contain;"> (Unlink) icon on the right-hand side of the text editing bar. </p>
<p  style="margin-left:5%;"><img src="../../assets/images/Settings/signunsub.png" style="margin-left:15px;  float: right; width: 125px; height: 200px;">
• <img src="../../assets/images/Settings/mergefield.png" style="display: inline-block;vertical-align: middle;width: 27px;margin-left: 1px;height: 27px;object-fit: contain;"> Use Revenue Grid <a href="../Using-Merge-Fields/">merge fields</a> to add recipient- or campaign-specific data into your signature. 
⚠️Now through Merge Fields, you can add a pre-made <a href="../Settings/#unsubscribe_links">Unsubscribe Links</a> directly to your signature and when adding a signature to your email, the unsubscribe link will be added within.
<br><br>
• Paste an image inline from clipboard
</p>





<br><br>
<hr>
## Manage merge fields

Go to Setting → <b>Merge fields</b> subtab to set personal Unsubscribe and Book me link.<br>

###Unsubscribe text
To keep Revenue Grid's automated email sequences non-obtrusive, messages sent via the platform must include an unsubscribe link for the prospects. The unsubscribe text and link can be customized to match specific campaign needs.
<br><br>
Unique unsubscribe URLs are automatically generated by Revenue Grid for every created Sequence, as <a href="../Using-Merge-Fields/">
specific merge fields</a>.
<br><br>
To set the unsubscribe section to be used in your emails:

<p style="margin-left:2%;">1. Open the <b>Merge Fields</b> tab on the Settings page</p>

<p style="margin-left:2%;">2. In the Unsubscribe text area, click on the text field and enter the line to surround the unsubscribe link, e.g. <i>"Click this link to unsubscribe from our offers</i></p>

<p style="margin-left:2%;">3. Highlight the URL placement word or phrase with the cursor (e.g. <i>"this link"</i>) and then click the <img src="../../assets/images/Steps/insert_url.png" style="display: inline-block;vertical-align: middle;width: 18px;margin-left: 1px;height: 14px;object-fit: contain;"> icon on the right-hand side of the text editing bar.

If you decide to remove the URL (unlink), click on the URL placement word or phrase and then click the <img src="../../assets/images/Steps/unlink.png" style="display: inline-block;vertical-align: middle;width: 18px;margin-left: 1px;height: 14px;object-fit: contain;"> (Unlink) icon on the right-hand side of the text editing bar. The hyperlink will be removed.</p>

<p style="margin-left:2%;">6. Then <b>Save</b> in the <b>Unsubscribe text</b> tab.</p>

Now the unsubscribe section is ready to be inserted into your RG emails, as &lcub;&lcub;UnsubscribeText&rcub;&rcub; <a href="../Using-Merge-Fields/">merge fields</a>. Alternatively, you can insert the "bare" unsubscribe link, as &lcub;&lcub;UnsubscribeLink&rcub;&rcub; merge field.
<br>

<p><img src="../../assets/images/Settings/unsubscr-dial.png" style="margin-left:15px;  float: right; width: 320px; height: 100px;">
After a prospect clicks the Unsubscribe link in an email, he/she will be prompted to confirm this action on the unsubscribe page opened in ones' browser.</p>

<div class="admonition hint">
<p class="admonition-title">Note</p>
<p style="font-size:16px">
If the unsubscribe section is not set up by a user, Revenue Grid will be using one defined by Admin. In addition, Sequence-specific unsubscribe sections can be used according to the campaign's requirements: for example, for emails sent out to prospects who speak a different language.</p>
</div>
<br><br>

### BookMe text

The 'Book me' text gets configured here, and it will be used when:<br>
<p style="margin-left:5%;">
• A sequence, which has recipients you own in SFDC, is being run <a href="../Settings-of-Sequences/#sending">on behalf of</a> prospect's owner, and the &lcub;&lcub;Owner BookMe Text&rcub;&rcub; merge field is being used. 
<br>
• You run a sequence <a href="../Settings-of-Sequences/#sending">on behalf of</a> sequence owner, and you use the &lcub;&lcub;Sender BookMe Text&rcub;&rcub; merge field.
</p>
<br><br>
In order to set your Book me text, go to Settings → Merge Fields.
<br>
<p style="margin-left:2%;">1. Open the <b>Merge Fields</b> tab on the Settings page</p>

<p style="margin-left:2%;">2. In the BookMe text area, click on the text field and enter the surrounding text, e.g. <i>"Book a meeting with me"</i>.</p>

<p style="margin-left:2%;">3. Highlight the URL placement word or phrase with the cursor (e.g. <i>"Book a meeting"</i>) and then click the <i>BookMe link</i> icon on the right-hand side of the text editing bar.</p>

<p style="margin-left:2%;">6. Then <b>Save</b>.</p>


Now the Book Me link is ready to be inserted into your RG emails, as &lcub;&lcub;Sender Booking Text&rcub;&rcub; or &lcub;&lcub;Owner BookMe Text&rcub;&rcub;<a href="../Using-Merge-Fields/">merge fields</a>.
<br>


<div class="admonition hint">
<p class="admonition-title">Attention</p>
<p style="font-size:16px">
In order to be able to use such merge field, the <i>CalendarAvailabilityDefaultTimezone</i> setting must be set on any level of settings (User / Org / Global). The value must be in <a href="https://nodatime.org/TimeZones"><i>IANA format</i></a> statistics. 
</p>
</div>

<br><br>
<hr>
<br>

## Add domains not to be imported to Revenue Grid


<p><img src="../../assets/images/Settings/blacklist.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;">
Go to Setting → <b>Import</b> subtab. List email domains which don't need to be imported to Revenue Grid as targeted audience.<br><br>
For example it can be your corporate domains, so emails of your colleagues don't get flown to the Audience tab.</p>
<br><br>
You company domain will be added to the blocklist by default, so not to generate unnecessary communication traffic between colleagues through Revenue Grid. As a result, if you add a colleague to a sequence just to test Sequences, it won't work. Use alternative emails to test sequences.
<hr>



## Change fonts 

<p><img src="../../assets/images/Settings/fontsize.png" style="margin-left:15px;  float: right; width: 30%; height: 30%;">
Go to Setting → <b>Editor</b> subtab. Change default font of the text editors, whether when creating a <i>Step</i> or a <i>Template</i>, replying in the Action Center, etc.
<br><br><br><br>
</p>
<br>
<hr>


## Your email and CRM connections to Revenue Grid

<p> <img src="../../assets/images/03092022/my-connectivity.png" style="margin-left:15px;  float: right; width: 40%; height: 40%;">
On this tab you can renew your Exchange / Office 365 / Gmail and Salesforce access credentials.
<br><br>
Refer to this article for <a href="https://docs.revenuegrid.com/ri/fast/articles/Renewing-Exchange-and-Salesforce-Account-Credentials/">detailed instructions</a>.
</p>
<br><br><br><br><br><br>
<hr>

## Synchronization

<p> <img src="../../assets/images/07272022/sync.png" style="margin-left:15px;  float: right; width: 60%; height: 60%;">
On the <i>Sync</i> tab you can Pause/Resume and Force your email-to-crm synchronization. Normally synchronization happens every 30 minutes, unless you manually force it.
<br>
Refer to this article for <a href="https://docs.revenuegrid.com/ri/fast/articles/Configuring-Activities-Synchronization-Settings-rg/">details</a>.
</p>
<br>
<hr>

## Book me defaults

<p> <img src="../../assets/images/07272022/7.gif" style="margin-left:15px;  float: right; width: 50%; height: 50%;">
On this tab you can set the default values to appear in the Revenue Grid Email Sidebar every time you start creating a Book Me link.
<br><br>
Refer to this article for <a href="https://docs.revenuegrid.com/ri/fast/articles/Sharing-Calendar-Availability-(Adaptive-view)/#managing_book_me_defaults">detailed instructions</a>.
</p>
<br><br><br><br><br><br>
<hr>

## Customization of the Email Sidebar

Refer to this article for <a href="https://docs.revenuegrid.com/ri/fast/articles/Customizing-SmartCloud-Connect-(full-article)/">detailed instructions on customization of the Email Sidebar</a>.











