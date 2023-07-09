---
title: Settings of a sequence explained
description: Learn how to use the Settings tab to set up a Sequence’s specific parameters
---

  
# Settings of a Sequence

<p style="font-size:15px"><i>5 min read</i> </p>
<!-- ShareThis BEGIN -->
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis -->



Use the **Settings** tab to set up a Sequence's specific parameters.

### General

<img src="../../assets/images/08232021/seq-set1.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;">
**Sequence name** - you can rename the sequence.

**Priority** - select the priority for your sequence:

* <img src="..\..\assets\images\04042023\priority-high.png" style="display:inline-block; vertical-align:middle; margin:1px; object-fit:contain;">**High**: Steps will be scheduled for the earliest possible time.  

* <img src="..\..\assets\images\04042023\sort-asc.png" style="display:inline-block; vertical-align:middle; margin:1px; object-fit:contain;">**Normal**: Steps will be scheduled in the usual order **after** high-priority ones. 

* <img src="..\..\assets\images\04042023\remove.png" style="display:inline-block; vertical-align:middle; margin:1px; object-fit:contain;">**Low**: Steps will be scheduled **after** normal and high-priority ones. 

!!! tip "Tip"
    However, the <b>Run now</b> action overrides all priority settings and configured schedules
    
<br>

**Delivery Schedule** - select one of preset <a href="../Settings/#schedules">delivery schedules</a>.<br>

**Sharing** - change the Sequence's sharing permissions: <br>
<p style="margin-left:5%;">
• <b>Private</b>: Only you and admins can modify this sequence and add prospects to it. <br>
• <b>Shared</b>: Everyone in your team can add prospects to this sequence. Only you and admins can modify it.<br>
• <b>Multi-owned</b>: Everyone can add prospects to this sequence. Only admins can create and modify such a sequence. 
</p>



!!! tip "Tip"
    Admins always can view, select, edit and clone all sequences regardless of settings mentioned above
<br><br>

<hr>
### Sending

<img src="../../assets/images/01122022/seq-set2.png" style="margin-left:15px;  float: right; width: 35%; height: 35%;">

In **Default country code**, specify the country whose calendar will be used for executing the steps for recipients who have no country specified in Salesforce.<br>

In **Default time zone**, specify the time zone which will be used for executing the steps for recipients who have no time zone specified in Salesforce.<br>

In the <b>Send on behalf of</b> drop-down, you can choose from whose inbox a sequence will send out emails to the recipients. 
</p>
<p style="margin-left:5%;">
○ <b>Prospect's owner</b> - the recipients will receive emails from whoever is listed as their owner in Salesforce, no matter who runs the sequence.
<br><br>
○ <b>Sequence's owner</b> - the recipient will get an email from whoever runs the sequence. 
</p>


**Email address to be used** for sending the emails to prospects. You can custom map another email address for your outreaches. It doesn't have to be primary work email only. In the current version, to custom map another email you have to contact us. We would love to help.
<br>

**Phone number to be used for SMS** types of steps of the sequence being created.
<br><br>


<hr>

### Details

<img src="../../assets/images/08232021/seq-set3.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;">

<b>Start sequence on the date</b> starts a sequence on a certain date, at certain time.<br>

<b>Pause sequence on the date</b> hard stops a sequence on a certain date, at certain time.<br>

<br><br><br>

!!! tip "Tip"
    Alternatively, you can set the start and pause dates by clicking on the three dots icon on the necessary sequence in the list of Sequences and selecting **Set sequence dates**
<br>

<b>Map sequence stage change on person status</b> is used to update a recipient's <a href="../Prospect-Statuses/">Person Status</a> once <a href="../Sequences-Stages/">Sequence Stage</a> changes.<br>

<b>Don't pause sequence upon response from the prospect</b> controls whether a Sequence pauses for the recipient when one replies. Normally, when a Sequence sends an email and a recipient replies to it, then the Sequence won't proceed to the next step for that recipient until you process his/her reply manually on the <a href="../Planner/">Action Center</a>.<br>

<b>Pause sequence and create a To-Do item on reply from the same company</b>  pauses all upcoming outreaches to all recipients belonging to the same company once a reply from at least one person from that company is received. This switch button can be enabled only if *Don't pause sequence upon response from the prospect* is disabled.<br>

<b>Schedule newly added steps for the previously unresponsive recipients</b> is used to start reaching out, with additionally added steps, to those of prospects who had been <b>Unresponsive</b>, and the prospects' status will go back to <b>Approaching</b>.<br>

<b>Automatically add unsubscribe text at the end of every sequence email</b> is used to add usubscribe link to each sequence email.


</p>
<br><br>
<hr>
### Unsubscribe configuration

<p style="margin-left:5%;"> <img src="../../assets/images/08232021/seq-set4.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;">

Customize unsubscribe link to match specific campaign needs. Customize supplementary text using text editing toolbar. In order to insert the actual unsubscribe link, please select a word or a phrase and then click <img src="../../assets/images/08232021/unsub.png" style="display: inline-block;vertical-align: middle;width: 25px;margin-left: 1px;height: 25px;object-fit: contain;"> Unsubscribe Link icon. 
<br><br>
Use <a href="../Using-Merge-Fields/">merge fields</a> in order to append the unsubscribe message to the end of your outreaches.


</p>
<br><br>
<hr>
###  Auto responses and OOTO processing rule 

<img src="../../assets/images/08232021/seq-set5.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;">

Set the rule for handling of <b>Out of the Office</b> (OOTO) and other automatic responses:<br><br>

<br>
**Place all auto-replies to <a href="../Notifications/">Notifications</a> for manual processing** - used if you prefer to process every auto-reply manually, e.g. to reschedule a Sequence step<br><br>    
**Ignore auto-replies and continue sequence** - enable if you want to proceed with the Sequence disregarding the auto-replies<br><br>
**Ignore auto-replies and add additional delay {Days} before next step** - enable if you want to proceed with the Sequence disregarding the auto-replies but with automatic increase of the interval between steps by a set number of days<br><br>


</p>
<br><br>
<hr>
### Automatically updated views 

<p style="margin-left:5%;"> <img src="../../assets/images/08232021/seq-set6.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;">

Salesforce views which you used to import recipients to the sequence. When new contacts/leads get added to the view in Salesforce, Revenue Grid will pull them into the Sequence seamlessly and outreaches to the newly added recipients will start from the first step according to Sequence's schedule.

</p>


<br><br>
<hr>
### Sequence Notes

<p style="margin-left:5%;"> <img src="../../assets/images/06192022/2.png" style="margin-left:15px;  float: right; width: 70%; height: 70%;">

Leave notes for future references. 


</p>
<br><br><br><br><br><br>








