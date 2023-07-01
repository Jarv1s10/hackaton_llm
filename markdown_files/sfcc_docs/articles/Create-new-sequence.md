---
title: Step-by-step guide to creating a sequence in Revenue Grid
description: Learn how to create and edit sequences in Revenue Grid 
---

  


# Step by step guide to create and to launch your first <i>Sequence</i>

<p style="font-size:15px"><i>6 min read - updated few hours ago</i> </p>
<!-- ShareThis BEGIN -->
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis -->
<iframe title="vimeo-player" src="https://player.vimeo.com/video/379264540" width="853" height="505" frameborder="0" allowfullscreen></iframe>
------

In order to set up and launch a Sequence in Revenue Grid, first you need to create an empty Sequence, then add recipients and *Steps* to it, and finally <i>Activate</i> it.



### Create a new Sequence

Follow these steps to create a new *Sequence*.

1. Go to Sequences page through the left-hand side navigational bar

2. Click <img src="../../assets/images/faq/create_sequence.png" style="display: inline-block;vertical-align: middle;width: 100px;margin-left: 1px;height: 60px;object-fit: contain;">  button in the top right-hand corner

3. Fill out the form

<p style="margin-left:5%;"> <img src="../../assets/images/01122022/newseq1.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;">
<b>a.</b> Name your sequence.
<br><br>
<b>b.</b> Sharing the sequence.<br></p>
<p style="margin-left:9%;">
<i>• Private</i> - the sequence will be visible only to you.<br><br>
<i>• Shared</i> - visible(read-only) to everyone in your company. Your colleagues can view Steps, <a href="../Analytics/">Statistics</a>, <a href="../Settings-of-Sequences/">Settings of the Sequence</a>, and <b>clone</b> it.<br><br>
<i>• Multi-owner</i> - You can assign a different sender per every single step. Thus, you cadence will appear to recipients as a group of people of your company is reaching out to the prospect. All owners of all steps will be added to CC to every step, so the recipient sees all senders every time the sequence email is received. Only admins can create multi-owner sequences.<br><br>
</p>

<div style="margin-left:9%;" class="admonition important">
<p class="admonition-title">Note</p>
<p>Admin level users always have full access to all Sequences. More about access rights <a href="../Access-rights/">here</a></p>
</div>

<p style="margin-left:5%;">
<b>c.</b> Add tags to the sequence for easier classification and search through.
<br>
</p>

<p style="margin-left:5%;">
<b>d.</b> Email are being sent on behalf of - the emails will be sent out to recipients:<br>
</p>
<p style="margin-left:9%;">
 • from your email address as an owner of a <b>Private</b> sequence;<br>
 • from email address of your <i>delegator</i> when you are a delegatee. Read more about delegation of tasks <a href="../Delegation/">here</a>;<br>
 • from email address of owner of the recipients record in Salesforce when you choose <b>Shared</b> sequence;
</p>

<div style="margin-left:9%;" class="admonition important" style="margin-left:5%;">
<p class="admonition-title">Important</p>
<p>You cannot change this setting later.</p>
</div>

<p style="margin-left:9%;"><i>Send on behalf of the sequence owner</i>  -</p>
<p style="margin-left:12%;">
• all emails will be sent from your mailbox with your <a href="../Settings/#signatures">signature</a> and <a href="../Settings/#unsubscribe_links">unsubscribe text</a>
<br>
• all related <a href="../to-dos/">to-do</a> items will appear on your <a href="../Planner/">Action Center</a> page<br>
• all prospects' replies/auto-replies will appear in your mailbox<br>

<p style="margin-left:9%;"><i>Send on behalf of the prospect owner</i> setting -</p>
<p style="margin-left:12%;">
• all emails will be sent out from prospect’s owner (listed in Salesforce) mailbox with the owner's signature and unsubscribe text<br>
• all related <a href="../to-dos/">to-do</a> items will appear on the prospect owner’s <a href="../Planner/">Action Center</a><br>
• all prospects’ replies/auto-replies will appear in prospect owner’s mailbox<br><br>
In case if an ownership changes in Salesforce, a new to-do item labeled as <a href="../to-dos/#owner_change">Owner change</a> will appear on prospect’s previous owner’s To-do tab on the Action Center.<br>
</p>



<p style="margin-left:5%;">
<b>e.</b> Schedule defines a time frame within which you want your outreaches to get sent out. You can create <a href="../Settings/#schedules">a custom schedules</a> to fit into any imaginable timing.
<br><br>
<b>f.</b> Choose time zone.


<br><br>
<b>g.</b> Email address to be used for sending the emails to prospects. You can custom map another email address for your outreaches. It doesn't have to be primary work email only. In the current version, to custom map another email you have to contact us. We would love to help.


<br><br>
<b>h.</b> Phone number to be used for SMS types of steps of the sequence being created. <a href="../admin-settings/#select_sms_and_call_provider">Read more about how to set up SMS sending.</a>
<br><br>


<b>i.</b> In the Salesforce View and Campaign drop-down, select if you'd like a lead view or a contact view get created in Salesforce automatically along with the sequence. The name of the view will be identical to the Sequence's name. 
<br><br>
You can use this view to gather prospects form campaigns and reports. The view will be linked with the Sequence, and recipients who get added to the view will be down-synced to the list of recipients of the Sequence seamlessly. 
<br><br>
Once such Sequence is created, you won't be able to add recipients to it on the <a href="../Create-new-sequence/#adding_recipients_to_a_sequence">Recipients tab</a> manually. The only channel through which recipients get into the Sequence is via the automatically created <a href="../Settings-of-Sequences/#automatically_updated_views">Salesforce view/campaign</a>. 
<br>
</p>
<!-- Outdated Extra step
<p style="margin-left:9%;">
<b>Extra step on the Salesforce side:</b> Once such sequence is created, you will find a new view in Salesforce. Now you have to go to the <i>Leads</i> or <i>Contacts</i> tab, click on the newly created View, and set for e.g. a campaign to the <i>"Filter by Campaign name"</i> field; then remove the pre-defined "REMOVE_THIS_FILTER" filter.
<img src="../../assets/images/Sequences/sfilter.png" style="width: 50%; height: 50%;"/>

</p>-->
</p></p>

4. Click <img src="../../assets/images/faq/create_but.png" style="display: inline-block;vertical-align: middle;width: 90px;margin-left: 1px;height: 60px;object-fit: contain;"> and your sequence is ready. Next you should add [recipients](../Recipients), create steps and then you may activate it


<div class="admonition important">
<p class="admonition-title">Note</p>
<p style="font-size:16px">You can skip some of the parameters while creating a sequence, and set them up or change in the <a href="../Settings-of-Sequences/">Settings of the sequence later</a>.</p>
</div>

<hr>



### Adding recipients to a Sequence

<p><img src="../../assets/images/08052021/add_recipients_from.png" style="margin-left:15px;  float: right; width: 25%; height: 25%;">
In order to add recipients to a sequence, please go to <a href="../Recipients/">Recipients tab</a>.

<p style="margin-left:2%;">
1. Click <img src="../../assets/images/faq/add_recipients_button.png" style="display: inline-block;vertical-align: middle;width: 90px;margin-left: 1px;height: 60px;object-fit: contain;"> button in the top right-hand corner.<br>
2. In the appeared drop-down menu, choose where do you want to pull recipients from:</p>

<p style="margin-left:9%;">

• <i>Salesforce views</i> - follow the dialog box and import all the prospects within a certain Salesforce List view.<br><br>
</p>
<div class="admonition caution" style="margin-left:9%;">
<p class="admonition-title">Note</p>
<p>Select the "Auto-sync selected views every hour" checkbox so Revenue Grid checks the chosen Salesforce view for new contacts/leads and if any, then pulls them into the Sequence seamlessly. The newly added contacts/leads will be engaged starting from Step 1. <br><br>

Please note that this function works <b>only</b> if the Sequence is not started or active. In case the Sequence is paused, the system won’t upload any new prospects.<br><br>

In order to turn automatic updating list of recipients off, go to <a href="../Settings-of-Sequences/#automatically_updated_views">settings of your sequence</a> and control it in "Automatically updated views" section.<br><br></p>
</div>

<p style="margin-left:9%;">
• <i>Records from views</i> - follow the dialog box and handpick recipients from a view.<br><br>
• <i>Reports</i> or <i>Campaigns</i> - follow the dialog box and import all the prospects within a certain Salesforce report.  <br><br>
• <i>Records from reports</i> or <i>campaigns</i> - follow the dialog box and handpick recipients from a report.<br><br>
</p>
<div class="admonition caution" style="margin-left:9%;">
<p class="admonition-title">Note</p>
<p>All types of Reports are importable into Revenue Grid, with a condition that the report has Contact or Lead ID column.</p>
</div>

<p style="margin-left:9%;">
<i>• Existing prospects</i> - from Revenue Grid's <a href="../People/">Audience</a> page, from among those who have been imported from Salesforce earlier<br><br>
<i>• Add new recipient</i> - a punched into a single-recipient-form, when you need to add a prospect quickly and directly to Revenue Grid.<br><br>
<i>• CSV</i> - import prospects from an uploaded file from your computer. Refer to <a href="../import-recipients-from-csv/">this article</a> describing that step by step<br><br>
</p></p>

<div class="admonition tip">
<p class="admonition-title">Hint</p>
<p>You may always add more recipients later even after activating a sequence. Those recipients who get added later will be reached out according to sequence's schedule starting from the 1st step of the Sequence, no matter on what steps other recipients are at that moment. </p>
</div>

<p>
<img src="../../assets/images/07202022/6.png"  style="width: 50%; height: 50%;float: right;margin-left:2%;"/> 
Once upload of the recipient is done, you can review how many have left off and other details regarding the recipients being upload.
</p>
<br><br><br><br><br><br>


------



### Adding and editing *Steps* to/of a Sequence

Whether to an empty or to an existing sequence, adding *Steps* is very easy and straightforward. 

<p style="margin-left:2%;">1. On the <a href="../Overview/">Overview</a> tab, click <img src="../../assets/images/faq/add-step.png" style="display: inline-block;vertical-align: middle;width: 100px;margin-left: 1px;height: 60px;object-fit: contain;"> in the top right-hand corner

<p style="margin-left:2%;"> <img src="../../assets/images/Sequences/newstep.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;">2. In the appeared prompt, choose type of the step. It may be an email, a phone call, a text message, a miscellaneous type of a step, or a signal<br><br>
</p>

<p style="margin-left:2%;">3. <i>Schedule idle</i> section with "Days" and "Hours" fields. Here you choose how long you want a step which is being added to wait after the previous step gets executed. <br><br>
Read here <a href="../Create-new-sequence/#create_immediate_follow-up_step">how to create same day follow up email type of a step</a>.<br>
<br>

</p>

<p style="margin-left:2%;">4. Click <i>Next</i> to start building your Steps
</p></p>
Depending on what type of a step you choose, you have slightly different editors:

------

### Adding *Steps* with a customized schedule

<p style="margin-left:2%;"> <img src="../../assets/images/12262022/custom-schedule.gif"  style="width: 50%; float: right;margin-left:2%;" class="minimized"/> 
By default, when you create a new step within a sequence, the sequence schedule is applied to the step that is being created. You can select a custom schedule for specific step.
<br><br>
This feature is especially useful if you want to schedule specific step types at specific times. For example, if you would like the Call steps to be scheduled from 8 am to 12 pm, you can create a corresponding schedule and set it for a specific step. 
</p>



------

#### Email type of a step


![](../assets/images/Sequences/emailstep.png)
<br>
<div style="margin-left:5%;" class="admonition attention">
<p class="admonition-title">Multi-owner Sequence</p>
<p style="font-size:16px">
<img src="../../assets/images/07272022/10.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;">
For multi-owner sequences, first choose from whose email address the step will be send out.
<br><br>
Only admins can create Multi Owner Sequence
</p>
</div>

<p style="margin-left:2%;">1. Choose <b>Type</b> in the drop-down. It can be *New thread* or *Reply*<br><br>
2.  <b>Templates</b> drop-down to choose one of pre-made [templates](../Templates)<br><br>
3.  <b>CC</b> field to add emails to send copies of an email to additional people. Each of the following steps inherits CC recipients automatically.<br><br>
4.  <b>Subject</b> of your email<br><br>
5. Sophisticated editor where you type body of your email. It has powerful toolbar to customize you message. Along with standard editing tools some are exceptionally valuable:<br></p>

<p style="margin-left:5%;"><img src="../../assets/images/Sequences/merge-field.png" style="display: inline-block;vertical-align: middle;width: 28px;margin-left: 1px;height: 28px;object-fit: contain;"> <b>Merge field</b> is powerful tool to personalize you message, to add signatures and unsubscribe links and much more. Refer to an article dedicated to capabilities of <a href="../Using-Merge-Fields/">merge field</a></p>

<div style="margin-left:5%;" class="admonition hint">
<p class="admonition-title">Note</p>
<p style="font-size:16px"> 
<img src="../../assets/images/02042022/missing-merge-field.png" style="margin-left:15px; margin-right:15px; float: right; width: 20%; height: 20%;">
When you have Merge Fields, that are not available for any reason (empty values in Salesforce, wrong syntactic, no API access, etc.), the merge field will be red-highlighted in <b>Preview</b>.
</p>
</div>

<div  style="margin-left:5%;" class="admonition hint">
<p class="admonition-title">&lcub;&lcub;Auto inserted Signature&rcub;&rcub; merge field tag</p>
<p style="font-size:16px">Keep in mind that based on selected preferences of auto-adding a signature to sequence emails in  <a href="../Settings/#signatures">signature settings</a>, you may see a special tag, <i>&lcub;&lcub;Auto inserted Signature&rcub;&rcub;</i>, in the email editor when creating or editing <i>an email type of a step</i>.</p>
</div>

<p style="margin-left:5%;"> Besides, you can add links, paste inline images from clipboard or from a link, and add attachments <img src="../../assets/images/Steps/attach.png" style="display: inline-block;vertical-align: middle;width: 3%;margin-left: 1px;height: 3%;object-fit: contain;"> (supported file types are: pdf, doc, docx, xls, xlsx, ppt, pptx, csv, txt, rtf, ods, odt, html, zip, 7z, rar, mp3, mp4, wma, mpg, flv, avi, jpg, jpeg, png, gif, epub, fb2)
</p>


<br><br>
<p style="margin-left:5%;"> <img src="../../assets/images/faq/send-test.png" style="margin-left:15px;  float: right; width: 60%; height: 60%;">
<b>Source code</b> is where you can paste HTML type of an email. Use third party HTML email builders to put together an email which would catch attention, then paste the exported HTML code to source code window.</p>
<br>
<br>
<p style="margin-left:5%;"><b>Preview</b> is to eyeball how your recipients will see your email. Note that once you click on <i>Preview</i>, you will also need to choose a recipient in the "<i>To:</i>" field. If you haven't added recipients to the sequence yet, then "To:" field will show John Doe as a placeholder.<br></p>
<div  style="margin-left:5%;" class="admonition tip">
<p class="admonition-title">Send me a test email</p>

<p> When in <i>Preview</i> mode, <u>Send me a test email</u> button will appear on the bottom of the editor, to send the message to your email address just to examine the look of your email.<br><br></p>
</div>

<p style="margin-left:2%;">6. <b>Review and personalize this step</b> checkbox controls if you want to review an email manually before it gets sent out. If you select this checkbox, then when each of recipients reaches this step according to Sequence's schedule, you get to-do item per each recipient on the <a href="../to-dos/">Action Center's To-do tab</a> where you can <i>Send as planned</i>, <i>Send now</i> or <i>Reschedule</i><img src="../../assets/images/Sequences/resched.png" style="display: inline-block;vertical-align: middle;width: 25px;margin-left: 1px;height: 25px;object-fit: contain;"> 
<br><br><br>
7.  <b>Schedule idle</b> with <i>Days</i> and <i>Hours</i> fields. Here you choose how long you want a step which is being added to wait after a previous step completes.</p>
<p style="margin-left:2%;"> <img src="../../assets/images/Sequences/updatetemplate.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;">
<br><br>
8. At last, click <b>Add step</b>, with or without extra feature - saving the step to the list of Templates for future reuse. In case if you had built the step based on a template, then you'll also have an option not only add the step, but also update the template.</p>
  
<br><br>
</p>
------



#### Phone Call type of a step

When it comes to Phone call type of a step, here is what you have to remember:

<p style="margin-left:2%;">
1.  <i>Call script template</i> drop-down allows you to choose a template script from the same list of <a href="../Templates/">templates</a>
<br><br>
2.  <i>Subject</i> mostly for your own use
<br><br>
3. Toolbar to type and customize your phone call script. Along with standard editing tools, you have exceptionally valuable *Merge field*, a powerful tool to personalize you message, to add signatures and unsubscribe links and much more. Refer to an article dedicated to capabilities of  <a href="../Using-Merge-Fields/">merge field</a>. Also you can add links, paste inline images from clipboard or from a link
<br><br>
4.  <i>Schedule idle</i> - here you choose how long you want a step which is being added to wait after a previous step completes
<br></p>
<p style="margin-left:2%;"> <img src="../../assets/images/Sequences/updatetemplate.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;">
5. At last, click <b>Add step</b>, with or without extra feature - saving the step to the list of Templates for future reuse. In case if you had built the step based on a template, then you'll also have an option not only add the step, but also update the template.</p>
<br>

------



#### SMS type of a step
<p style="margin-left:2%;">
1.  <i>SMS template</i>  drop-down allows you to choose a template from the same list of <a href="../Templates/">templates</a>
<br><br>
2. Text editor for you to type your message
<br><br>
3. <i>Review and personalize this step</i> checkbox controls if you want to review an SMS manually before it gets sent out. If you select this checkbox, then when each of the recipient reaches this step according to Sequence's schedule, <b>you get a separate To-do items per each recipient</b> on the <a href="../to-dos/">Action Center's To-do tab</a>, where you can <i>Send as planned</i>, <i>Send now</i>, <i>Reschedule</i><img src="../../assets/images/Sequences/resched.png" style="display: inline-block;vertical-align: middle;width: 25px;margin-left: 1px;height: 25px;object-fit: contain;">, Skip, Mute etc.
<br><br>
4.  <i>"Schedule idle"</i> with <i>"Days"</i> and <i>"Hours"</i> fields. Here you choose how long you want a step which is being added to wait after a previous step completes<br>
</p>
<p style="margin-left:2%;"> <img src="../../assets/images/Sequences/updatetemplate.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;">
5. At last, click <b>Add step</b>, with or without extra feature - saving the step to the list of Templates for future reuse. In case if you had built the step based on a template, then you'll also have an option not only add the step, but also update the template.</p>


<div class="admonition hint">
<p class="admonition-title">Check SMS sending settings</p>
<p style="font-size:16px">In order to be able to use SMS type of steps: <br>
1. Your company should have a Twilio account<br>
2. Your Admins should connect Twilio account to Revenue Grid in <a href="../Settings/#select_sms_and_call_provider">corresponding settings</a><br>
3. You should go to <a href="../Settings/#account">Settings→Account</a> subtab and choose a number from <i>SMS sender ID</i> drop-down. This number will be reserved only for SMS type of steps ran by you.</p>
</div>
------



#### Misc. type of a step
<p style="margin-left:2%;">
1.  <i>Subject</i> mostly for your own use.
<br><br>
2. Sophisticated editor where you type body of your email. It has powerful toolbar to customize you message. Along with standard editing tools some are exceptionally valuable:
<br></p>

<p style="margin-left:4%;"><img src="../../assets/images/Sequences/merge-field.png" style="display: inline-block;vertical-align: middle;width: 18px;margin-left: 1px;height: 14px;object-fit: contain;"> <i>Merge field</i> is powerful tool to personalize you message, to add signatures and unsubscribe links and much more. Refer to an article dedicated to capabilities of <a href="../Using-Merge-Fields/">merge field</a>. Besides, you can add links, paste inline images from clipboard or from a link</p>
<p style="margin-left:2%;">
3.  <i>"Schedule idle"</i> with <i>"Days"</i> and <i>"Hours"</i> fields. Here you choose how long you want a step which is being added to wait after a previous step completes.
</p>
<p style="margin-left:2%;"> <img src="../../assets/images/Sequences/updatetemplate.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;">
4. At last, click <b>Add step</b>, with or without extra feature - saving the step to the list of Templates for future reuse. In case if you had built the step based on a template, then you'll also have an option not only add the step, but also update the template.</p>

<div class="admonition hint">
<p class="admonition-title">Note</p>
<p>Once a Misc. type of a step gets processed in the Action Center, the action gets logged to SFDC as a completed task.</p>
</div>
<hr>


#### Signal type of a step
<p style="margin-left:2%;">
1.  <i>Subject</i> mostly for your own use.
<br><br>
2. Sophisticated editor where you type body of your email. It has powerful toolbar to customize you message. Along with standard editing tools some are exceptionally valuable:
<br></p>
<p style="margin-left:4%;"><img src="../../assets/images/Sequences/merge-field.png" style="display: inline-block;vertical-align: middle;width: 18px;margin-left: 1px;height: 14px;object-fit: contain;"> <i>Merge field</i> is powerful tool to personalize you message, to add signatures and unsubscribe links and much more. Refer to an article dedicated to capabilities of <a href="../Using-Merge-Fields/">merge field</a>. Besides, you can add links, paste inline images from clipboard or from a link</p>
<p style="margin-left:2%;">
3.  <i>"Schedule idle"</i> with <i>"Days"</i> and <i>"Hours"</i> fields. Here you choose how long you want a step which is being added to wait after a previous step completes.
</p>
<p style="margin-left:2%;"> <img src="../../assets/images/Sequences/updatetemplate.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;">
4. At last, click <b>Add step</b>, with or without extra feature - saving the step to the list of Templates for future reuse. In case if you had built the step based on a template, then you'll also have an option not only add the step, but also update the template.</p>

<div class="admonition hint">
<p class="admonition-title">Note</p>
<p>Once a Signal type of a step gets generated, it will appear on <a href="../Signals/">the Signals tab of the Action Center</a> .</p>
</div>
<hr>



### Create immediate follow-up step

<p style="margin-left:5%;"> <img src="../../assets/images/faq/send-test.png" style="margin-left:15px;  float: right; width: 60%; height: 60%;">
Create 2 email type of steps and place them back to back in a sequence. The first in the list should be your main outreach, while the following step must be your immediate follow up.
Open the second step and make sure <i>Day</i> value in the <i>Schedule idle</i> are is 0.
</p>






<hr>
### Activate the Sequence
<p> <img src="../../assets/images/Sequences/toggle.png" style="margin-left:15px;  float: right; width: 170px; height: 95px;">
And finally, once you finish adding steps, it's time to activate your Sequence. Go to <a href="../Overview/">Overview tab</a> and switch the toggle in the top right-hand corner.</p>








