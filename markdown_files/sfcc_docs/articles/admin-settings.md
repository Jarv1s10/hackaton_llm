---
title: Admin level settings of Revenue Grid
description: Complete guide to Revenue Grid Platform settings: all features explained
---



# Admin level settings

**[admin level article]**

<p style="font-size:15px"><i>8 min read</i> </p>
<!-- ShareThis BEGIN -->
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis -->
<br>

<p> <img src="../../assets/images/01122022/opensettings.png" style="margin-left:15px;  float: right; width: 25%; height: 25%;">Admin settings page is used to view and adjust the company-wide parameters for users in Revenue Grid (RG).<br>
<br>
To access Revenue Grid Settings, click the Settings icon in the top right corner of the RG interface.<br>
<br>
Now more detailed about every of the tabs.
</p>
<br>

<div class="admonition attention">
<p class="admonition-title">Important</p>
<p>These tabs are editable only by users with Admin rights and changes get applied to all RG users company wide.</p>
</div>
<br>
<hr>

## Control what to sync with Salesforce

<p> <img src="../../assets/images/Settings/salesforce.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;"></p>
Go to Settings → Platform settings → **Sequences** → **General**.  

* Control automatic synchronization of all activities generated by sequences with Salesforce.  
* Allow creating Salesforce campaigns for each sequence.  
* Enable automatic import of recipients into Revenue Grid from Salesforce email send out widget.<br>

<br><br>
<hr>

## Allow upload and export from/to CSV

<p> <img src="../../assets/images/Settings/import.png" style="margin-left:15px;  float: right; width: 50%;">
Go to Settings → Platform settings → <b>Sequences</b> → <b>General</b>.  <br><br>

These check-boxes enable option to upload and download prospects from/to a CSV file on the <a href="../Recipients/#export_recipients_to_a_csv_file">Recipients tab</a> of a Sequence, as well as on the <a href="../People/#export_prospects_to_a_csv_file">Audience tab</a>.

</p>
<br><br><br><br>
<hr>

## Configure default contry code and time zone for sending

Go to Settings → Platform settings → <b>Sequences</b> → <b>General</b>.

In the **Sending** section, specify the default country code and time zone which will be used for sending out steps for prospects with no country and time zone specified.

<img src="../../assets/images/Settings/sending.png" style="margin-left:15px;  float: right; width: 50%;">
**Default country code** - the country whose calendar that must be used when planning Sequence steps for recipients with no specified country to schedule steps only on business days.

**Default time zone** - the time zone that must be used when planning Sequence steps for recipients with no specified time zone.

<br><br>
<hr>

## Set up auto-dismissal of items in the Action Center

<img src="../../assets/images/Settings/auto-dismiss.png" style="margin-left:15px;  float: right; width: 50%;"><br>

You can set up auto-dismissal of notifications about **auto-replies**, **calls** and **misc**. to-do items in the Action Center.  

<br><br>

Auto-dismissal affects **all existing** and **future items** for which auto-dismissal is enabled. After enabling auto-dismissal for specific items, all active sequences paused due to these item types will **continue** with the next steps for all relevant users.    

You must specify the delay for auto-dismissing to ensure that your colleagues have enough time to review and process the notifications and to-do items in their Action. The delay can vary from <b>1</b> to <b>999</b> days. 

!!! warning "Important"
    Enabling auto-dismissal will affect all users. 
    
    Before enabling auto-dismissal, ask your colleagues that work with sequences to **review** their Action Center notifications. This will prevent renewing sequences that were stopped for a long time, outdated or irrelevant sequences

<br><br>
<hr>

## Set company-wide defaults for sequences

Go to Settings → Platform settings → Sequences → **Defaults**. 

<img src="../../assets/images/Settings/defaults2.png" style="margin-left:15px;  float: right; width: 50%;">

Here, you can configure default settings and auto-replies and OOTO handling settings for all newly created sequences. All new sequences will inherit the default settings unless the sequence owner changes these settings for a specific sequence on the <a href="../Settings-of-Sequences/">Sequence Settings</a> page. Settings on the sequence level override the default organization-wide settings specified by admins. 


<b>Map sequence stage change on person status</b> is used to update a recipient's <a href="../Prospect-Statuses/">Person Status</a> once <a href="../Sequences-Stages/">Sequence Stage</a> changes.<br>

<b>Don't pause sequence upon response from the prospect</b> controls whether a Sequence pauses for the recipient when one replies. Normally, when a Sequence sends an email and a recipient replies to it, then the Sequence won't proceed to the next step for that recipient until you process his/her reply manually on the <a href="../Planner/">Action Center</a>.<br>

<b>Pause sequence and create a To-Do item on reply from the same company</b>  pauses all upcoming outreaches to all recipients belonging to the same company once a reply from at least one person from that company is received. This switch button can be enabled only if *Don't pause sequence upon response from the prospect* is disabled.<br>

<b>Schedule newly added steps for the previously unresponsive recipients</b> is used to start reaching out, with additionally added steps, to those of prospects who had been <b>Unresponsive</b>, and the prospects' status will go back to <b>Approaching</b>.<br>

<br>

### Auto-replies and OOTO processing rules

<img src="../../assets/images/Settings/ooto.png" style="margin-left:15px;  float: right; width: 50%;">

Set the rule for handling of <b>Out of the Office</b> (OOTO) and other automatic responses:<br><br>

**Place all auto-replies to <a href="../Notifications/">Notifications</a> for manual processing** - enable if users must process every auto-reply manually, e.g. to reschedule a sequence step<br>    
**Ignore auto-replies and continue sequence** - enable if sequences must proceed disregarding the auto-replies<br>
**Ignore auto-replies and add additional delay {Days} before next step** - enable if sequences must proceed disregarding the auto-replies but with automatic increase of the interval between steps by a set number of days<br><br>

<hr>

## Company-wide default signatures, unsubscribe and BookMe text   

<p> <img src="../../assets/images/10072022/default-signatures.png" class="minimized" style="margin-left:15px;  float: right; width: 55%; height: 40%;">
Go to Setting → Platform settings → Sequences  → <b>Merge fields</b> to change company-wide default signatures, unsubscribe and BookMe text that are being used in Sequence emails. 
<br><br>Here Admins can set the default Primary and Secondary signatures which will be applied company-wide. By enabling/disabling the switch button below, the Admins can allow the end users to override the default signatures and modify the signatures.
</p>
<br><br>

<p> <img src="../../assets/images/10072022/rules.png" style="margin-left:15px;  float: right; width: 45%; height: 40%;">
On this page, Admins can also change the auto-inserting rules for default signatures: do not insert them or select a specific inserting pattern. 
</p>

<br><br><br>

<img src="../../assets/images/Settings/force-reset.png" style="margin-left:15px;  float: right; width: 30%; height: 40%;">
By clicking the **Force reset users' signature settings** button, you will reset all users’ signatures the default signature. 


<br><br>
 
### Set company-wide unsubscribe link 

<p> <img src="../../assets/images/07272022/9.png" style="margin-left:15px;  float: right; width: 55%; height: 40%;">
On the Unsubscribe subtab, Admins set company-wide standard for unsubscribe text.

By enabling/disabling the switch button, the Admins can allow the end users to override the default unsubscribe text and modify it. Also, here they can configure auto-insertion rule for unsubscribe text.
</p>
<br><br><br>
 

### Set company-wide BookMe link 

<p> <img src="../../assets/images/10072022/bookme.png" style="margin-left:15px;  float: right; width: 55%; height: 40%;">
On the BookMe subtab, Admins set company-wide standard for BookMe text that is inserted by the end users in their Sequence emails. 

By enabling/disabling the switch button, the Admins can allow the end users to override the default BookMe text and modify it. 

</p>
<br><br><br><br><br><br>

<hr>

## Status updates

<p> <img src="../../assets/images/11072021/eloqua.png" style="margin-left:15px;  float: right; width: 40%; height: 50%;">
Go to Setting → Platform Settings → Sequences → <b>Status updates</b> subtab.

Upload a CSV file to synchronize Opt-In / Opt-Out statuses.<br>

</p>
<br><br><br><br><br><br><br><br><br><br>
<hr>

## Select SMS and call provider

Go to Setting → Platform Settings → Sequences → <b>SMS & Calls</b> subtab. 

Available SMS & calls providers:

<img src="../../assets/images/12022021/sms-and-calls.png" style="margin-left:15px;  float: right; width: 40%;">

* <a href="https://www.twilio.com/" target="_blank">Twilio</a>. Detailed Twilio setup guide in <a href="../twilio/" target="_blank">this article</a>.

* <a href="https://www.ringcentral.com/" target="_blank">Ring Central</a>

* <a href="https://aircall.io/" target="_blank">Aircall</a>. Detailed Aircall setup guide in <a href="../aircall-setup/" target="_blank">this article</a>.

* <a href="ttps://360smsapp.com/" target="_blank">SMS 360</a>

<br><br><br>


<img src="../../assets/images/12022021/phone-settings.png" style="margin-left:15px;  float: right; width: 50%;">
When this Admin level setting is in place, every user will be able to choose a single number from a pool of available to them numbers on their Settings → Personal settings → Sequences → General → **Phone settings**. Or admin can set phone settings for each user manually.

<br><br>

<hr>

## Control sending capacity and other limits

Go to Settings → Platform Settings → Sequences → <b>Limits</b>. Enforced limits to the number of [RE Sequence emails](../Create-new-sequence/#email_type_of_a_step) sent by RG users.

<b>Number of sequence email/sms touches an RG user can send per day</b>

<p>To prevent SPAM generation, most email services impose a limitation on the number of emails a user (or automated emailing software) can send through a single email account per specific period of time. The applied limit is 1 email sent per 1 minute.
<br><br>
When Revenue Grid sends out emails, both custom written by a user and automated ones, it respects this limitation, observing the one minute minimum interval between sending emails.
<br><br>
The recommended (default) value of this setting is 500 emails; this value approximates the maximum number of emails that can be sent over a standard working day's span with a one minute interval. It is the emails quantity "bandwidth" shared by all email sequences you run in RG.  <br><br>
When the limit is reached, all remaining automated emails have to be postponed to the following day's sending span defined by the Sequence's Schedule, regardless of the step's actual timeline. Therefore, please consider this standard limit of 500 emails/day per RG user when planning your emailing campaigns.
<br><br>
The maximum value that can be set for this parameter is 1000, that is approximately 17 hours of automated emailing per 24 hours. If you do <b>not</b> set a limited daily Schedule for the Sequence (for example to imitate emails sending by a real person)  that is emails sending will be allowed for 24 hours, this increased limit is easily attainable, since the automated emails are sent out by your email server.</p>
<br>



<div class="admonition tip">
<p class="admonition-title">Important</p>
<p>In a realistic common case scenario a single RG user can send out around 100 emails per working day; this number is defined by his/her capability to process the recipient's responses to these emails. However, a informative mass email campaign that requires no specific response can make use from the maximum emailing "bandwidth".   
<br>
	Please note that there is also another factor that defines individual emails dispatching patterns, the *Schedule idle* parameter <a href="../Create-new-sequence/#adding_and_editing_steps_toof_a_sequence">set for Sequence steps</a></p>
</div>

<b>Number of sequence call, misc and signal steps scheduled per day</b>

Set the limit to number of automatic or manual steps of these types that can be scheduled per user per day.

<br>
<b>Sequence touches limit per email domain per day</b>

Set the limit of touches per specific domain to avoid overwhelming a certain company with your outreaches.

<br>
<b>Sequence touches limit per prospect per day</b>

​	The number of RG sequence emails allowed to be sent to a prospect per 24 hours. This parameter is set depending on the essence of the campaign and the target auditory. Normally the maximum number of such emails should not exceed 5, not to get a prospect annoyed. Note that this number does not include extra "custom" emails message composed by a RG user, for example a reaction to a prospect's reply or a follow-up clarifying a previously sent email. This parameter's default value is 5 and the maximum value is 10.


<br>
<b>Sequence touches limit per prospect per week</b>

This parameter is similar to the above one, only it sets the RG sequence emails limit imposed over a period of one week. This parameter's default value is 10 and the maximum value is 20.


<br>

<b>Active sequences per prospect</b>

How many active sequences a user can have at the same time.
<br>


<!--
### Teamwork

Go to Setting → <b>Teamwork</b> subtab. 
<a href="../Access-rights/"><b>Read an extended article describing Admin rights vs regular user rights</b></a>

<p> <img src="../../assets/images/Settings/ownership.png" style="width: 70%; height: 70%;" class="center"></p>


<h4> Allow access to prospects, owned by the other users</h4>


<p style="margin-left:2%;"> When the checkbox is selected: </p>
<p style="margin-left:5%;"> 
•	All regular users have access to leads and contacts owned by other SFDC users for prospect search/import, given that these prospects are visible to them in SFDC <br>
•	All regular users can add all leads and contacts directly to Revenue Grid <a href="../People">Audience</a> page or to Sequences<br>
•	All regular users have access to all all leads and contacts on Audience page, organization wide<br>
•	All regular users can delete their own Prospects only<br>
•	All regular users have access to the <a href="../People/#contactlead_profile">Activity History</a> of all the prospects in Revenue Grid, organization wide<br>
•	drop-down "Emails are being sent on behalf of" becomes enabled (see below)<br>
</p>

<p style="margin-left:2%;"> When the checkbox is cleared: </p>
<p style="margin-left:5%;"> 
•	All regular users can't access leads and contacts they don't own. Not while searching/importing in/from SFDC, not on Revenue Grid <a href="../People">Audience</a> page, nor able to add other users' prospects to sequences.<br>
•	All regular users have access to the <a href="../People/#contactlead_profile">Activity History</a> of only those prospects who have been involved in their sequences at least once
</p>
<div class="admonition hint">
<p class="admonition-title">Note</p>
<p>Regardless of this setting, Admin level users always have full access to all prospects available on Revenue Grid <a href="../People">Audience</a> page, can delete any prospect, as well as see all the items for every prospect in <a href="../People/#contactlead_profile">Activity History</a>.</p>
</div>


<h4> Email is being sent in every sequence on behalf of</h4>

<p style="margin-left:2%;"> <img src="../../assets/images/Settings/new-seq.png" style="margin-left:15px;  float: right; width: 205px; height: 265px;">
In this drop-down, choose default value which will be populated in corresponding field while creating a new sequence.

<br>
Possible values to choose from are:<br></p>
<p style="margin-left:5%;">
•	<i>Prospect's owner</i> -  recipients will receive emails generated by the sequence from whoever is listed as their owners in Salesforce, no matter who runs the sequence<br><br>
•	<i>Sequence owner</i> - recipients will receive emails generated by the sequence from whoever runs the sequence<br>
</p>
-->

<br>
<hr>

## Customize status mapping to Salesforce

Go to Setting → <b>Sequences under Platform Settings</b> → <b>Status mapping</b> subtab. On this tab, Admins can <a href="../Prospect-Statuses/">map Prospect statuses</a> to any value of any field in Salesforce for seamless mirroring, as well as <a href="../Prospect-Statuses/#how_to_create_a_new_custom_prospect_status_and_map_to_a_salesforce_field_boolean_or_pick-list_types">create additional Prospect statuses</a> tailored for any possible business need. Updates on this tab will get applied to all users in an Organization.<br><br>
By default, you get these Person statuses mapped to following values of the selected Salesforce fields (see the picture below).
<img src="../../assets/images/Settings/default-mapping.png" style="width: 100%; height: 100%;"/>
<br><br>
<hr>


## Manage sending schedules 

<iframe src="https://player.vimeo.com/video/380562837" width="853" height="505" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>

Go to Settings → <b>Sequences under Platform Settings</b> → <b>Schedules</b> subtab. On this tab you can create and manage email send-out schedules which you use in [RE Sequence](../Sequences/).
<br>

<p> <img src="../../assets/images/Settings/schedule.png" style="margin-left:15px;  float: right; width: 360px; height: 350px;">
A schedule is a set of specific days of the week and daily time intervals (set in the prospect's Time zone retrieved from Salesforce) used in RG Sequences. Automated emails sent by Revenue Grid will only be dispatched on these days and within these time intervals.
<br>
If you wish to exclude automated emails sending on the dates which are public holidays in the USA, you need to select the checkbox <b>Exclude federal US Holidays</b> in the schedule creation/editing dialog.
</p>
<br><br>

The schedules you select for your [sequence steps](../Sequences/) are overridden by [wait intervals set for individual steps](../Create-new-sequence/#email_type_of_a_step).
For example, if you create a sequence consisting of steps scheduled for every other day of the week except weekends (that is 3 sequence emails per business week) and set the wait interval between the steps to two days, the steps will be performed with a two day long interval (that is 2 sequence emails per business week). At the same, if the schedule implies sending one email per week, a two day long wait interval between steps will be always observed, not affecting the sending schedule. 



<hr>

## Manage signals

<p style="margin-left:2%;"> <img src="../../assets/images/Settings/signal-manager.png" style="margin-left:15px;  float: right; width: 30%; height: 30%;">
Go to Settings → <b>Signals</b> subtab. This setting is available to Managers only. Here you can select which signals to run company-wide. Once a signal is disabled, already generated signals of that type will not disappear from the interface until resolved.
</p>

<br>
<hr>

## Manage all users

<p> <img src="../../assets/images/Settings/users-tab.png" style="margin-left:15px;  float: right; width: 40%; height: 40%;">
Go to Settings → <b>Users</b> subtab. On this tab, Admins can see company-wide Revenue Grid users, their:
<p style="margin-left:5%;">
• Names<br>
• Emails<br>
• Who are their delegates (if any)<br>
• What is their <i>Dial-out and Texting</i> phone numbers (if any) to perform <a href="../Create-new-sequence/#sms_type_of_a_step">SMS</a> and <a href="../Create-new-sequence/#phone_call_type_of_a_step">Phone call</a> types of steps<br> 
• and Role (Admin or a regular User)
</p>
<br>
<p> <img src="../../assets/images/01122022/4.png" style="margin-left:15px;  float: right; width: 40%; height: 40%;">
By clicking on a user, Admins can see their <a href="../Settings/#account">Account tab</a>, where they can set up delegates, select SMS and Voice numbers, grant admin rights, and set up Primary signature.
</p>
</p>
<br><br><br><br><br>










