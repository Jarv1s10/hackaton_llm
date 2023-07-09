---
title: TO-DO items for you to handle for uninterrupted sales engagement
description: Learn how to handle tasks on the To Do tab to ensure uninterrupted sales engagement
---

  
# To-dos tab of the Action Center

<p style="font-size:15px"><i>3 min read - updated few hours ago</i> </p>
<!-- ShareThis BEGIN -->
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis -->


<iframe src="https://player.vimeo.com/video/386988687" width="853" height="505" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>

##Types of To-do items:

#### Review and Submit an email

This happens when you select "Review email before sending" while creating your email type of a Step. Your option are "Send as planned", "Send now" or "Reschedule".
    
<br>

#### Colleague's Reply

<p> <img src="../../assets/images/Planner/todo-colrep.png" style="margin-left:15px;  float: right; width: 40%; height: 40%;">
This happens when you have more than one representative of a same company in a sequence (identified by domain name of recipients email), and one of them replies. There is a control called "Create task on reply from same company" <a href="../Settings-of-Sequences/#details">Setting of a Sequence</a> to detect such occurrences. Here on the To-dos tab you can choose how you want to process replies from colleagues. You may *Finish* a *Sequence* for the contact with standard options: "Not Interested", "Success" or "Opt out". Alternatively you may *Dismiss* the fact that a colleague replied and then a *Sequence* will continue as planned.
<br><br>
When there are more than one colleague in other sequences, Select the "Apply to all colleagues from the same company" checkbox. It will prevent all communication with the company while you are proceeding with the prospect who replied.
</p>
<br>

#### Make a Call

<p><img src="../../assets/images/09272022/12.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;"/>
When recipients reach a phone call type of a step, it appears here in To-dos for you to make the call. 
The cell phone number of the recipient will be pulled from Salesforce. In case the field is blank, you can type in the number. Manually typed in numbers won't be saved to Salesforce.
<br><br>
As a prerequisite, your Revenue Grid has to be <a href="../admin-settings/#select_sms_and_call_provider">set up with one of the providers</a>.
<br><br>
</p><br>

<p> <img src="../../assets/images/09272022/13.png" style="margin-left:15px;  float: right; width: 30%; height: 30%;">
By clicking <i>Log</i>, you'll be prompted to confirm the outcome of it in the popped up dialog box and choose how to proceed from here. Use <i>Comment</i> text editor to log a conversation if needed.
</p>

<br><br><br><br><br>

<p> <img src="../../assets/images/09272022/14.png" style="margin-left:15px;  float: right; width: 40%; height: 40%;">
If <i>Move to another step</i> is chosen, select which step to place the Call item to from the dropdown. You can't place the item to the past step.
</p>

<br><br><br><br><br>

<br>
<div class="admonition hint">
<p class="admonition-title">Logging calls in Salesforce</p>
<p> Once logged, the call will appear in Salesforce on the prospect's record after the next Revenue Grid Synchronization session. Subject of the call will be "Successful call", "Voice mail" or "No Reply" depending on what you choose as Result of the call above.

<img src="../../assets/images/Planner/logged-to-sfdc.png" style="width: 450px; height: 270px;"/>
</p>
</div>
<br><br>
<p style="margin-left:5%;"> <img src="../../assets/images/Planner/greenicon.png" style="margin-left:15px;  float: right; width: 40%; height: 40%;">
Refer to the color of the icon of the item, to get an idea right away if it is good time to call now. When it's green, it means it's a working day and working hour on the prospect's side.
<br>
</p>
<br>
<p style="margin-left:5%;"> <img src="../../assets/images/Planner/reschedule.png" style="margin-left:15px;  float: right; width: 30%; height: 30%;">
Alternatively, you may reschedule a step for the recipient by Pencil icon.
</p>

<br><br><br><br>

#### Send SMS

When a recipient reaches SMS type of a step, which is marked as "Review and personalize this step", it appears here in *To-dos* for you to log SMS or to reschedule a step using Pencil icon.

<img src="../../assets/images/Planner/logsms.png" style="width: 80%; height: 80%;"/>

<p style="margin-left:10%;"> Additional actions: </p>
<p style="margin-left:12%;"> <i>Remove from sequence</i> - unlist the recipient from the sequence at once</p>
<p style="margin-left:12%;"> <i>Skip</i> - Skips current step and instead, executes the following step on current step's schedule</p>
<p style="margin-left:12%;"> <i>Mute</i> - Mutes this step and proceeds to the following step without changes in the following steps' schedule</p>
<p style="margin-left:12%;"> <i>Finish</i>  options - mark the recipient with a corresponding Person Status and take the recipient to the finish of the sequence</p>
<br>
<div class="admonition hint">
<p class="admonition-title">When logged here, it also gets saved in SFDC automatically</p>
<p> Once logged, the SMS will appear in Salesforce on the prospect's record after the next Revenue Grid Synchronization session. 

<img src="../../assets/images/Planner/logged-to-sfdc-sms.png" style="width: 450px; height: 270px; "/>
</p>
</div>
<br>

#### Log a Misc. type of a step

When a recipient reaches to a Misc. type of a step within a Sequence, you get a new To-do item to execute and log the action.
<img src="../../assets/images/Planner/miscsteplog.png" style="width: 100%; height: 100%;"/>
<br>
<div class="admonition hint">
<p class="admonition-title">An action logged here, gets saved in SFDC as well</p>
<p>Once a Misc. type of a step gets processed in the Action Center, the action gets logged to SFDC as a completed task.

<img src="../../assets/images/Planner/logged-to-sfdc-misc.png" style="width: 450px; height: 270px;"/>

</p>
</div>


<br>
#### Merge Field issue

<p> <img src="../../assets/images/Planner/todo-mfissue.png" style="margin-left:15px;  float: right; width: 40%; height: 40%;">This happens when you merge a field which is not populated in Salesforce, so Revenue Grid cannot auto-insert it into your email. Edit your message by removing the merge field or populate that field in Salesforce manually. Until you resolve the issue, a sequence for this prospect will be on hold.
</p><br>
<br>

#### Owner Change	 

<p> <img src="../../assets/images/Planner/todo-ownerchange.png" style="margin-left:15px;  float: right; width: 40%; height: 40%;"> When a recipient's owner changes in Salesforce, such item appears on the previous owner's To-do tab. A sequence will be paused for the recipient, until the previous owner decides how to proceed. The previous owner may *Finish* a *Sequence* for the contact with standard options: "Not Interested", "Success" or "Opt out"; or else, click *Continue sequence* button to proceed with the Sequence as planned. 
</p>
<br>
#### Lead conversion

<p> <img src="../../assets/images/Planner/todo-leadconv.png" style="margin-left:15px;  float: right; width: 40%; height: 40%;">
When a recipients is a Lead in Salesforce, and he/she has been converted to a Contact in Salesforce, all sequences the recipient is engaged into will get paused for him/her and you will receive a new To-do item where you have to choose how to proceed: Finish the sequence with standard options (Success, Not interested, Opt-out), or Dismiss the item so the engagement will go on per sequence's order.
</p>
<br>

#### Error sending

<p> <img src="../../assets/images/Planner/todo-sendingerr.png" style="margin-left:15px;  float: right; width: 40%; height: 40%;">
One of the reasons you may see this is blank value in the Email field for the recipient. Double check in CRM, and if it persists, then contact us at support@revenuegrid.com.</p>


<br><br><br><br>








