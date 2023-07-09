---
title: Frequently asked questions
description: The most commonly asked questions about Revenue Grid products
---
<script>
function setClipboard(value) {
    var tempInput = document.createElement("input");
    tempInput.style = "position: absolute; left: -1000px; top: -1000px";
    tempInput.value = value;
    document.body.appendChild(tempInput);
    tempInput.select();
    document.execCommand("copy");
    document.body.removeChild(tempInput);
}
</script>
<style>
.button {
  position: relative;
  background-color: #ffffff; 
  border: none;
  font-size: 15px;
  color: #AAAAAA;
  padding: 6px;
  text-align: center;
  -webkit-transition-duration: 0.6s; /* Safari */
  transition-duration: 0.6s;
  text-decoration: none;
  overflow: hidden;
  cursor: pointer;
  display: flex;
  color: teal;
}

.button img {
    width: 1rem;
    margin-left: 5px;
    width: 15px;
    margin-top: 2px;
}

.button:after {
  content: "";
  background: #90DDD0;
  display: block;
  position: absolute;
  padding-top: 600%;
  padding-left: 350%;
  margin-left: -20px!important;
  margin-top: -120%;
  opacity: 0;
  transition: all 0.9s
}

.button:active:after {
  padding: 0;
  margin: 0;
  opacity: 5;
  transition: 0s
}

div.a { text-indent: 30px; }
div.b { text-indent: 50px; }

</style>

<p><img src="../../assets/images/faq/question2.png" style="margin-left:15px;  float: right; width: 30%; height: 30%;"></p>

# Made of the most often<br>asked questions we get from you!

<br><br>

<!-----------------------------BIG----------------------------------->
<!-----------------------------BIG----------------------------------->

### 1\. How to add a prospect to a Sequence?

<p>There are a couple of ways to do that, on <a href="../Recipients/">Sequences' Recipients tab</a> or via  the  <a href="../Sidebar/#sequence_widget">Sidebar Widget</a>.</p>
<hr>
<p><b>On Sequences' Recipients tab</b>, to which you get from Sequences→<i>Click on a sequence you want to add a recipient to</i>→Recipients tab</p>

<p style="margin-left:2%;">1. Click <img src="../../assets/images/faq/add_recipients_button.png" style="display: inline-block;vertical-align: middle;width: 95px;margin-left: 1px;height: 65px;object-fit: contain;"> button in the upper right-hand corner</p>

<p style="margin-left:2%;">
    <img src="../../assets/images/08052021/add_recipients_from.png" style="margin-left:15px;  float: right; width: 25%;">
    2. Then in the appeared drop-down menu; choose where do you want to add recipients from
</p>

<p style="margin-left:4%;">
You may add:
<br>
• all contacts from a certain Salesforce view<br>  
• handpicked contacts from a certain Salesforce view<br> 
• prospects from <a href="../People/">Audience page</a>, who have been imported to Revenue Grid earlier<br> 
• <a href="../import-recipients-from-csv/">import from a CSV file</a> from your local computer</p> 
<br><br>

<hr></hr>

<p><b>Via the Sidebar Widget</b>, which you open by clicking<img src="../../assets/images/faq/open_sidebar.png" style="display: inline-block;vertical-align: middle;width: 35px;margin-left: 1px;height: 35px;object-fit: contain;"> on the right-hand side in the Action Center or on the Audience pages. Once opened, you'll see Sequence Widget on the bottom of the sidebar. Click <img src="../../assets/images/faq/add_seq.png" style="display: inline-block;vertical-align: middle;width: 25px;margin-left: 1px;height: 25px;object-fit: contain;"> in order to choose an existing Sequence from the opened dialog box and click <img src="../../assets/images/faq/add_but.png" style="display: inline-block;vertical-align: middle;width: 75px;margin-left: 1px;height: 55px;object-fit: contain;"></p>
<p style="margin-left:9%;">
<img src="../../assets/images/faq/widget.png" style="float: left; width: 265px; height: 180px;">
<img src="../../assets/images/faq/add_seq2.png" style=" width: 265px; height: 180px;">
</p>
<br>

<button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/articles/FAQ/#1_how_to_add_a_prospect_to_a_sequence')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
<!-----------------------------BIG----------------------------------->
<!-----------------------------BIG----------------------------------->

### 2\. How to pause a Sequence for a specific prospect?

There are multiple ways to pause a sequence for a recipient. One of the ways is to perform this action on Audience page.
<p>1. Go to Audience page</p>
<p>2. Search the prospect(s) who you want to stop a Sequence for</p>
<p>3. If it is a single prospect, then click <img src="../../assets/images/faq/more_icon.png" style="display: inline-block;vertical-align: middle;width: 25px;margin-left: 1px;height: 25px;object-fit: contain;"> icon and click Pause; if you are trying to pause a sequence for several prospects, then  you will have to perform <a href="../People/#mass_and_single_prospect_actions">Mass action</a>: Select the checkboxes and click <img src="../../assets/images/faq/more_icon.png" style="display: inline-block;vertical-align: middle;width: 25px;margin-left: 1px;height: 25px;object-fit: contain;"> icon appeared in the upper right corner of the page, and click Pause</p>
<br>
Also there is a similar way to pause a sequence for prospect(s) on the Recipients tab of a Sequence and via the <a href="../Sidebar/#sequence_widget">Email Sidebar</a>
<br><br>

<button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/articles/FAQ/#2_how_to_pause_a_sequence_for_a_specific_prospect')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
<!-----------------------------BIG----------------------------------->
<!-----------------------------BIG----------------------------------->

### 3\. How to use Merge Fields?

<p style="margin-left:2%;">
    <img src="../../assets/images/faq/merge_insert3.gif" style="margin-left:15px;  float: right; width: 145px; height: 135px;">
    1. Put a cursor where you want an auto-inserted value to appear in your message in a text editor
    <br><br>
    2. Then type "&lcub;&lcub;" so a drop-down with values appears
    <br><br>
    3. Choose a desired one by clicking on it or type the value
</p>
<br><br><br>
Alternative way...
<br><br>
<p style="margin-left:2%;">
    <img src="../../assets/images/faq/mergedrop2.png" style="margin-left:15px;  float: right; width: 385px; height: 205px;">
    1. Put a cursor where you want a value to appear
    <br><br>
    2. Instead of typing "&lcub;&lcub;", use  <img src="../../assets/images/faq/mergeicon.png" style="display: inline-block;vertical-align: middle;width: 35px;margin-left: 1px;height: 35px;object-fit: contain;"> icon on the toolbar of the text editor
    <br><br>
    3. Choose a desired one by clicking on it
</p>
<br><br><br>

<hr></hr>

<p>Preview the result</p>
<p style="margin-left:2%;">
    <img src="../../assets/images/faq/send-test.gif" style="margin-left:15px;  float: right; width: 50%; height: 50%;">
    In order to preview a message, you should first switch the editor to the preview mode.
    <br><br><br>
</p>
<br>

<hr></hr>

<div class="admonition warning">
    <p class="admonition-title">Additional info</p>
    <p><img src="../../assets/images/faq/merge_preview.png" style="margin-left:15px;  float: right;  width:30%; height: 30%;"> While previewing, merged values will be highlighted: Yellow indicates that relevant data was retrieved successfully; Red indicates that relevant data is not populated in Salesforce for this prospect.</p>
    <br><br>
    <p><img src="../../assets/images/faq/merge_issue.png" style="margin-left:15px;  float: right; width:285px; height: 205px;"> When it's red, meaning not able to fill the value, the automated email will not be sent out and the sequence for this prospect will be paused. In order to let you know about the issue, RG will notify you on <a href="../to-dos/">Action Center's To-Do tab</a> so you resolve the issue either by editing body of your message manually (e.g. removing the merge field tag) or by populating the value in Salesforce so RG can pick it up.</p>
</div>

<p>Commonly used merge fields are: Lead/Contact name, company name, RG Sequence owner name as well as your email signature and unsubscribe link.</p>
<br>
<button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/articles/FAQ/#3_how_to_use_merge_fields')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
<!-----------------------------BIG----------------------------------->
<!-----------------------------BIG----------------------------------->

### 4\. How to insert a signature into an email?

You can add a pre-made signature via one of the Merge Fields tags.
<br>
<p style="margin-left:2%;">
    <img src="../../assets/images/faq/add_sign.gif" style="margin-left:15px;  float: right; width: 145px; height: 135px;">
    1. Put a cursor where you want a signature to appear in the text  (whether when replying from the Action Center or creating an email type of a step)
    <br><br>
    2. Type "&lcub;&lcub;"
    <br><br>
    3. In the appeared drop-down choose 'User signature' or 'User Secondary signature', depending which signature you want to use. Refer to <a href="../Settings/#signatures">this article</a> for details.
</p>
<div  class="admonition hint">
    <p class="admonition-title">&lcub;&lcub;Auto inserted Signature&rcub;&rcub; merge field tag</p>
    <p>Keep in mind that based on selected preferences of auto-adding a signature to sequence emails in  <a href="../Settings/#signatures">signature settings</a>, you may see a special tag, <i>&lcub;&lcub;Auto inserted Signature&rcub;&rcub;</i>, in the email body editor when creating or editing <i>an email type of step</i>.</p>
</div>
<br>
<p>Preview the result</p>
<p style="margin-left:2%;">
    <img src="../../assets/images/faq/send-test.gif" style="margin-left:15px;  float: right; width: 50%; height: 50%;">
    Merge field tag will be replaced with one of pre-made signatures saved in Settings→Signature tab. In order to preview a message, you should first switch the editor to the preview mode.
</p>
<br><br>

<button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/articles/FAQ/#4_how_to_insert_a_signature_into_an_email')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
<!-----------------------------BIG----------------------------------->
<!-----------------------------BIG----------------------------------->

### 5\. How to Opt-out a recipient from a sequence's outreaches?

<p>There are a couple of ways to do that, on <a href="../Recipients/">Sequences' Recipients tab</a> or via the <a href="../Sidebar/#sequence_widget">Sidebar Widget</a> or on the <a href="../People/#contactlead_profile">recipient's profile page</a>.</p> 
<br>
<b>On Sequences' Recipients tab</b>
<br>
<p style="margin-left:2%;">
    1. Go to Sequences page→<i>Sequence name</i>→Recipients tab
    <br><br>
    2. Select a checkbox next to a recipient who you want to opt-out
    <br><br>
    3. Click the appeared <img src="../../assets/images/faq/more_icon.png" style="display: inline-block;vertical-align: middle;width: 25px;margin-left: 1px;height: 25px;object-fit: contain;">  icon on the upper right-hand side, and choose Opt-out
</p>
<br>
<p><b>Via the Sidebar Widget</b></p>
<p style="margin-left:2%;">
    <img src="../../assets/images/faq/opt-out.png" style="margin-left:15px;  float: right; width: 185px; height: 245px;">
    1. Open the sidebar by clicking<img src="../../assets/images/faq/open_sidebar.png" style="display: inline-block;vertical-align: middle;width: 35px;margin-left: 1px;height: 35px;object-fit: contain;"> on the right-hand side in the Action Center or Recipient's profile pages. <br>
    <p style="margin-left:5%;">
        <i>Once opened, you'll see Sequence Widget on the bottom of the sidebar, where all sequences a recipient is engaged into will be listed</i>
    </p>
</p> 
<br>
<br>
<p style="margin-left:2%;">
    2. Click <img src="../../assets/images/faq/more_icon2.png" style="display: inline-block;vertical-align: middle;width: 25px;margin-left: 1px;height: 25px;object-fit: contain;"> next to a sequence which you want to opt-out a recipient from
    <br><br>
    3. Choose Opt-out from the menu
</p>
<br>
<p><b>On the recipient's profile page</b> - this opts out a prospect from all sequence he/she is engaged into.</p>
<br>
<p style="margin-left:2%;">
    <img src="../../assets/images/faq/profile.png" style="margin-left:15px;  float: right; width: 285px; height: 200px;">
    1. Go to recipients profile by clicking on prospect's name wherever it is clickable: in the Action Center page, Recipients tab of the Sequence, or on the Audience page
    <br><br>
    2. Click Opt-out in the Overview area
</p>
<br><br>

<button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/articles/FAQ/#5_how_to_opt-out_a_recipient_from_a_sequences_outreaches')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
<!-----------------------------BIG----------------------------------->
<!-----------------------------BIG----------------------------------->

### 6\. How Revenue Grid acts when a CC-ed recipient replies to my email?

A lot depends on who has been added to CC field: 
<p style="margin-left:4%;">- a main recipient's colleague who is also enrolled into the same sequence</p>
<p style="margin-left:4%;">- anybody else</p>
<br>
In case if you receive an email from CC-ed recipient, who is a main recipient's colleague and also enrolled into the same sequence: 
<p style="margin-left:2%;"> Such email appears on the Notification tab in the Action Center, which you may reply to or dismiss. Meanwhile for your main recipient, 'Colleague’s Reply' item gets created on To-dos tab in the Action Center. Such item pauses a sequence for the main recipient until processed manually.</p>
<br>
In case if you CC-ed anybody else: 
<p style="margin-left:2%;">Such reply, even if it's an auto-reply or a bounce, will appear on Notification tab in the Action Center and a sequence for the main recipient will not be paused.</p>
<br>
<div class="admonition warning">
    <p class="admonition-title">Important</p>
    <p>Select 'Pause sequence and create a To-Do item on reply from the same company' checkbox in Sequence's Settings in order to intercept such occurrences. </p>
</div>
<br>

<button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/articles/FAQ/#6_how_revenue_grid_acts_when_a_cc-ed_recipient_replies_to_my_email')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
<!-----------------------------BIG----------------------------------->
<!-----------------------------BIG----------------------------------->

### 7\. What is Person Status in Revenue Grid?

As soon as imported to Revenue Grid, every prospect gets assigned to "Just added" status and then changes depending on prospect's behavior within a <i>Sequence</i>. Person status helps to identify on what stage a prospect currently is. Some status changes are automatic, while others initiated by Revenue Grid user.
<br><br>
For example, status lifecycle may develop from "Just added"→"Not contacted"→"Approaching"→"Success". For detailed information about every status, <a href="../Prospect-Statuses/"> refer to this article</a>
<br><br>
When a prospect’s status changes in Revenue Grid, it may get reflected in Salesforce according to custom mapping.
<br><br>

<button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/articles/FAQ/#7_what_is_person_status_in_revenue_grid')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
<!-----------------------------BIG----------------------------------->
<!-----------------------------BIG----------------------------------->

### 8\. How to add an unsubscribe link to an email?

In the text editor, whether when creating an email type of a step or when creating a template, do following:
<br>
<p style="margin-left:2%;">1. Put a cursor to the end of your email where usually unsubscribe links appear</p>
<p style="margin-left:2%;">2. Type "&lcub;&lcub;" so a drop-down with Merge Field values appear</p>
<p style="margin-left:2%;">3. Choose "Unsubscribe Text"</p>
<br>
The Merge Field tag will be replaced with a premade unsubscribe text which you can add/edit in <i>Settings→Unsubscribe</i>
<br>
<hr>
<p><b>Preview the result when creating an email type of a step</b></p>
<p style="margin-left:2%;">
    <p><img src="../../assets/images/faq/send-test.gif" style="margin-left:15px;  float: right; width: 50%; height: 50%;">
    In order to preview a message, you should first switch the editor  to the preview mode.</p>
</p>
<br><br><br><br>

<button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/articles/FAQ/#8_how_to_add_an_unsubscribe_link_to_an_email')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
<!-----------------------------BIG----------------------------------->
<!-----------------------------BIG----------------------------------->

### 9\. How to add targeted recipients to a Sequence from Salesforce report?

Easy! Revenue Grid supports Salesforce reports of any type that have Contact/Lead ID column in it.
<br><br>
Go to <a href="../Recipients/">Recipients tab</a> of your Sequence and select "Report" from "Add recipients" drop-down. 
<br><br>
Follow the dialog that show you Salesforce reports you have access to, and pull the recipients in.
<br><br>
<a href="../Recipients/#where_i_can_add_recipients_from">Refer to these articles for detailed guides on how to import recipients from different sources.</a>
<br><br>

<button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/articles/FAQ/#9_how_to_add_targeted_recipients_to_a_sequence_from_salesforce_report')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
<!-----------------------------BIG----------------------------------->
<!-----------------------------BIG----------------------------------->

### 10\. What data get synchronized from Revenue Grid to Salesforce?

<b>Emails:</b>
<br>
<p style="margin-left:2%;">
    You can have all Revenue Grid incoming and outgoing emails automatically saved to Salesforce as Tasks linked to relevant Contacts or Leads. There are two ways to enable email auto-saving: 
    <br><br>
</p>
<p style="margin-left:2%;">
    <img src="../../assets/images/faq/autosaving.png" style="margin-left:15px;  float: right; width: 300px; height: 150px;" />1. Go to <a href="https://smart.sf.invisiblesolutions.com/ui/#/admin/mailServer/status" target="_blank">Sync settings page</a> via the Email Sidebar<i> (Settings Dashboard will be opened in a new Web browser tab)</i> → Detailed Settings → ...and enable the switch button next to 'ENABLE AUTO-SAVING' in <i>ACTIVITIES SYNC SETTINGS</i> section. <a href="https://docs.revenuegrid.com/ri/fast/articles/Configuring-Activities-Synchronization-Settings/" target="_blank">Refer to this article for more information about sync settings </a>
    <br><br>
    2. Alternatively, you can have emails auto-saved automatically if such feature is requested during Revenue Grid implementation.
</p>
<div class="admonition hint">
    <p class="admonition-title">Hint</p>
    <p>Auto-saving happens along with the next synchronization session. By default every 30 minutes unless manually forced on the Sync Settings Dashboard.</p>
</div>
<br>
<hr>
<b>Calls:</b>
<p style="margin-left:2%;">
    <img src="../../assets/images/Planner/logged-to-sfdc.png" style="margin-left:15px;  float: right; width: 450px; height: 270px;">
    By default, all calls which get logged on <a href="../to-dos/">To-do tab</a> in the Action Center get created in Salesforce during the next Revenue Grid Synchronization session.
</p>
<br><br><br><br><br>

<button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/articles/FAQ/#10_what_data_get_synchronized_from_revenue_grid_to_salesforce')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
<!-----------------------------BIG----------------------------------->
<!-----------------------------BIG----------------------------------->

### 11\. Scenarios when targeted contacts forward your email to someone else

Roles:
<br>
<p style="margin-left:5%;">
    1. Revenue Grid user from whose inbox the sequence is sending emails. See sequence level setting called <a href="../Create-new-sequence/#create_a_new_sequence">Email are being sent on behalf of</a> for more details<br>
    2. Jim is being engaged by your sequence. <br>
    3. Tom has never been in any of sequences of anyone in your organization. <br>
    4. Megan have been engaged by other sequences, thus listed on Revenue Grid <a href="../People/">Audience</a> page
    <br>
</p>
Scenario 1. 
<p style="margin-left:5%;">
    Jim receives an email generated by the sequence, keeps RG user in To/Cc field and forwards it to Tom.<br>
    Result: RG user gets a new <a href="../Notifications/">Notification</a> or <a href="../Replies/">Reply</a> in the Action Center for Jim, and all sequences Jim is engaged in get paused.
</p>
Scenario 2. 
<p style="margin-left:5%;">
    Jim receives an email generated by the sequence, forwards it to Tom without RG user in To/Cc field. Then Tom adds RG user to To/Cc field and replies to the forwarded email.<br>
    Result: RG user gets a new <a href="../Notifications/">Notification</a> in the Action Center for Jim, and all sequences Jim is engaged in get paused.
</p>
Scenario 3. 
<p style="margin-left:5%;">
    Tom composes a new email, adds RG user to To/Cc field and sends it to Jim and.<br>
    Result: RG user gets a new <a href="../Notifications/">Notification</a> in the Action Center for Jim, and all sequences Jim is engaged in get paused.
</p>
Scenario 4. 
<p style="margin-left:5%;">
    Jim receives an email generated by the sequence, forwards it to Megan without RG user in To/Cc field. Then Megan adding RG user to To/Cc field and replies to the forwarded.<br>
    Result: RG user gets new <a href="../Notifications/">Notifications</a> in the Action Center for Megan and for Jim. All sequences Megan is engaged in get paused.
</p>
Scenario 5. 
<p style="margin-left:5%;">
    Megan composes a new email to RG user, with Jim in To/Cc field.<br>
    Result: RG user gets new <a href="../Notifications/">Notifications</a> in the Action Center for Megan and for Jim. All sequences Jim is engaged in get paused.
</p>
<br>

<button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/articles/FAQ/#11_scenarios_when_targeted_contacts_forward_your_email_to_someone_else')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
<!-----------------------------BIG----------------------------------->
<!-----------------------------BIG----------------------------------->

### 12\. How to use "Send me a test email" functionality?

You can send a test email to yourself in order to eyeball how recipients will see your message.
This function is available when replying to emails in the Action Center, and when <a href="../Create-new-sequence/#email_type_of_a_step">creating an email type of a step</a>.
<br><br>
<b>in the Action Center, when replying to a prospect: </b>
<p>You can always send yourself an email you are preparing for a prospect, just to eyeball how a prospect will see on the other end. Click the more options icon <img src="../../assets/images/Sequences/moreactions.png" style="display: inline-block;vertical-align: middle;width: 30px;margin-left: 1px;height: 30px;object-fit: contain;">, and then "Send me a test email</p>
<img src="../../assets/images/Planner/endtestemail.png" style="width: 90%; height: 100%;"/>
<br>
<b>On the Sequences tab, when creating a new email type of a step: </b>
<br>
<p>
    <img src="../../assets/images/faq/send-test.gif" style="margin-left:15px;  float: right; width: 50%; height: 50%;">
    In order to send a test email, you should first switch the editor to the preview. Once you do that, a clickable button <u>Send me a test email</u> will appear next to Send/Save and Discard buttons under the text editor. Click <u>Send me a test email</u> and you will receive the email within a minute.
</p>
<br>

<button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/articles/FAQ/#12_how_to_use_send_me_a_test_email_functionality')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
<!-----------------------------BIG----------------------------------->
<!-----------------------------BIG----------------------------------->

### 13\. How to deal with bounced contacts?

It happens that once the first step of a sequence gets executed, you receive several bounced replies. One of the reasons you get bounced replies is email addresses have been misspelled in Salesforce. So what to do in that case? The best practice is:
<br>
<p style="margin-left:2%;">
    <img src="../../assets/images/faq/filterbounced.png" style="margin-left:15px;  float: right; width: 205px; height: 231px;">
    1. Go to the original Sequence->Recipients tab, and filter by "Bounced". Now you have a list of exact prospect who have been bounced.</a>
</p>
<br><br><br><br><br>
<p style="margin-left:2%;">
    <img src="../../assets/images/faq/toremove.png" style="margin-left:15px;  float: right; width: 115px; height: 145px;">
    2. Fix their records in Salesforce or remove unneeded once via the More Options <img src="../../assets/images/Sequences/moreactions.png" style="display: inline-block;vertical-align: middle;width: 25px;margin-left: 1px;height: 25px;object-fit: contain;"> icon
</p>
<br><br><br><br>
<p style="margin-left:2%;">
    <img src="../../assets/images/faq/clone.png" style="margin-left:15px;  float: right; width: 205px; height: 145px;">
    3. Clone the original <a href="../Sequences/">Sequence</a> on the Overview tab
</p>
<br><br><br><br><br>
<p style="margin-left:2%;">
    4. Then on the Recipients tab of the original Sequence, select <img src="../../assets/images/faq/select.png" style="display: inline-block;vertical-align: middle;width: 25px;margin-left: 1px;height: 25px;object-fit: contain;"> all prospects who are bounced, then click the More Options icon <img src="../../assets/images/Sequences/moreactions.png" style="display: inline-block;vertical-align: middle;width: 25px;margin-left: 1px;height: 25px;object-fit: contain;"> in the upper right hand corner of the tab, and click Add. In the appeared pop-up, select the cloned sequence. 
    <img src="../../assets/images/faq/addtoseq.png" style="width: 750px; height: 140px;"/>
</p>
<br>

<button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/articles/FAQ/#13_how_to_deal_with_bounced_contacts')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
<!-----------------------------BIG----------------------------------->
<!-----------------------------BIG----------------------------------->

### 14\. How not to get flagged as SPAM when sending emails in bulk?

Here are a few key recommendations you should follow when sending many emails to avoid getting flagged as spam, whether by spam filters or by recipients.
<br><br>
<b>Recommended</b>
<br>
<p style="margin-left:2%;">
    • Personalized subject and greeting will be considered as a good sign<br>
    • Reputation of a sender grows when a sender sends a sequence of emails with requests to response<br>
    • Add links to body of your email. All the links must be directed to the same domain (doesn't apply to social media outlets)<br>
    <br>
</p>
<b>Not recommended</b><br>
<p style="margin-left:2%;">
    • Sending promo-emails where images prevail text<br>
    • Using link-shortening services (email clients usually consider it as phishing)<br>
    <br>
</p>
<b>Forbidden</b><br>
<p style="margin-left:2%;">
    • Sending attachments in the first email. Attached files can be sent only if there has been a reply to your email<br>
    <br>
</p>
<b>Sender domain security</b><br>
<p style="margin-left:2%;">
    • Comply with Sender Policy Framework (SPF) - an email authentication method. Sender's security on the record indicates the IP and services from which emails are allowed, DKIM and DMARK records in the configuration of your domain for mail.<br><br>
    • <a href="https://support.google.com/a/answer/33786?hl=en">SPF description and recommendations from Google</a><br>
    • <a href="https://support.google.com/a/answer/174124">DKIM description and recommendations from Google</a><br>
    • <a href="https://sendersupport.olc.protection.outlook.com/pm/policies.aspx">General Outlook Recommendations Outlook postmaster</a><br>
</p>
<b>Parameters that indicate level of trust in Office365</b><br>
<p style="margin-left:2%;">
    • <a href="https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/spam-confidence-levels?view=o365-worldwide">SPAM confidence level (SCL) in Exchange Online Protection</a><br>
    • <a href="https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/configure-your-spam-filter-policies?view=o365-worldwide">Configure anti-spam policies in EOP </a><br>
    <br>
    The percentage of spam complaints should not exceed 0.5%
</p>
<b>Rules of email servers regarding Unsubscribe links</b><br>
<p style="margin-left:2%;">
    • Not required in case of one-to-one correspondence<br>
    • It is must have if an email has signs of bulk reach out<br>
    <br>
    For the sender's reputation, it is better if a recipient unsubscribes rather than marks an email as SPAM.<br>
</p>
<br>

<button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/articles/FAQ/#14_how_not_to_get_flagged_as_spam_when_sending_emails_in_bulk')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
<!-----------------------------BIG----------------------------------->
<!-----------------------------BIG----------------------------------->

### 15\. How to import your MS Outlook signature into Revenue Grid?

1. Go to Outlook->File and in the Account Information area, click on the link "Access your account on the Web:"
<img src="../../assets/images/faq/accessontheweb.png" style="width: 500px;"/>
<br>
2. In the opened browser, go to Sent Emails folder and pick any email with your signature in it<br>
3. Select the signature with a cursor and copy it to clipboard (Ctrl+C) <br>
4. Then go to Revenue Grid -> Settings -> Signature, and paste (Ctrl+V) it into one of the text editors: Default or Secondary signature.<br>
<br>
The format of your signature will be preserved when copied from Web page, rather than when copied from desktop version of Outlook.<br>
For more details about Revenue Grid Signatures, <a href="../Settings/#signatures">refer to the article</a>.<br>
<br>

<button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/articles/FAQ/#15_how_to_import_your_ms_outlook_signature_into_revenue_grid')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
<!-----------------------------BIG----------------------------------->
<!-----------------------------BIG----------------------------------->

### 16\. How to pass along your Revenue Grid  Signature to a teammate?

Revenue Grid supports very sophisticated signatures, which you can either build using formatting tools or import from an email client. If you want to pass it along to a teammate so he/she simply changes his/her name and contact details but preserves the format which you have built, then follow the steps to share the signature:<br>
<p style="margin-left:2%;">
    1. Go to Settings -> Signature<br>
    2. Switch the editor to the <i>Source</i> mode on the bottom of the editor<br>
    3. Copy (Ctrl+C) the whole HTML code to clipboard<br>
    4. Send it to a teammate to paste (Ctrl+V) it to the same <i>Source</i> code area of the editor<br>
    <br>
    When a teammate switches back to <i>Edit</i> mode, now the signature appears in the editor area in the exactly same format as yours. What's left is, change name and contact details and click Save.<br>
</p>
For more details about Revenue Grid Signatures, <a href="../Settings/#signatures">refer to the article</a>.<br>
<br>

<button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/articles/FAQ/#16_how_to_pass_along_your_revenue_grid_signature_to_a_teammate')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
<!-----------------------------BIG----------------------------------->
<!-----------------------------BIG----------------------------------->

### 17\. How email opens and link clicks get counted?

There are 5 screens in Revenue Grid which show how many times prospect(s) opened your emails <img src="../../assets/images/faq/opens.png" style="display: inline-block;vertical-align: middle;width: 25px;margin-left: 1px;height: 25px;object-fit: contain;">  and clicked on links <img src="../../assets/images/faq/clicks.png" style="display: inline-block;vertical-align: middle;width: 25px;margin-left: 1px;height: 25px;object-fit: contain;"> which you add to the text of those emails. Here It is explained how exactly email opens and link clicks get counted on every each of the screens.<br>
<br>
1. and 2. <a href="../People/">Audience page</a> / <a href="../People/#contactlead_profile">Prospect profile</a><br>
<p style="margin-left:2%;">
    <img src="../../assets/images/faq/stats.png" style="margin-left:15px;  float: right; width: 140px; height: 230px;">
    This is total count of unique emails that a prospect opened, and total count of unique links that a prospect clicked across all sequences.<br>
    <br>
    <b>Opens</b> if a prospect opened the same email multiple times, then it still counts as one <br>
    <b>Clicks</b>  if an email contains multiple links and a prospect clicked them all, then count of clicks will be higher than count of email opens
</p>
3. Sequence → <a href="../Recipients/">Recipients tab</a><br>
<p style="margin-left:2%;">
    This is count of email opens and link clicks within the sequence. <br>
    <br>
    <b>Opens</b> if a prospect opened the same email multiple times, then it still counts as one <br>
    <b>Clicks</b>  if an email contains multiple links and a prospect clicked them all, then count of clicks will be higher than count of email opens
</p>
4. Sequence → <a href="../Analytics/#metrics">Statistics tab (Metrics)</a> <br>
<p style="margin-left:2%;">
    This is count of unique prospects that opened at least one email, or clicked on at least one link within the sequence.<br>
    <br>
    <b>Opens</b> if a prospect opened all emails of the sequence, then it still counts as one <br>
    <b>Clicks</b>  if a prospect clicked on multiple links within an email, it's still counts as one<br>
    <br>
    <i>The percentage shows relation to number of prospects that were contacted by this sequence. If a prospect was added to the sequence but hasn't been reached out yet, then it doesn't get into calculation of the percentage.</i>
</p>
5. Sequence → <a href="../Analytics/#bar_graph">Statistics tab (Graph)</a><br>
<p style="margin-left:2%;">
    <img src="../../assets/images/faq/graph.png" style="margin-left:15px;  float: right; width: 143px; height: 204px;">This is count of unique prospects who opened an email, clicked a link on a certain step of the sequence. <br>
    <br>
    <b>Clicks</b>  if a prospect clicked on multiple links within an email, it's still counts as one
</p>
<br><br><br>

<button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/articles/FAQ/#17_how_email_opens_and_link_clicks_get_counted')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
<!-----------------------------BIG----------------------------------->
<!-----------------------------BIG----------------------------------->

### 18\. How to create flashy HTML templates?

HTML rich emails can grasp attention of recipients and ignite interest to your product. In Revenue Grid you can create such email type of a step when <a href="../Create-new-sequence/#email_type_of_a_step">building a Sequence</a>, or a template.
<br><br>
As an option, you can use third party HTML email builders like www.beefree.io or www.stripo.email. Such email editors all have <i>export</i> option, for you to import it to the <i>Source</i> tab of Revenue Grid email editor.
<br><br>
Otherwise, you can simply select a part of a web page, copy it, and paste it to the <i>Source</i> tab of Revenue Grid email editor like it is shown on the gif below.
<br><br>
<img src="../../assets/images/faq/kbgif.gif" style="width: 90%; height: 90%;"/>
<br>
Steps to create such template:<br>
<p style="margin-left:2%;">
    1. Go to <a href="../Templates/">Templates</a>, through the left hand side navigation panel<br>
    2. Click  <img src="../../assets/images/faq/addtemp.png" style="display: inline-block;vertical-align: middle;width: 95px;margin-left: 1px;height: 35px;object-fit: contain;"><br>
    3. In the opened text editor, click <i>Source</i> on the bottom of the editor<br>
    4. Paste the copied content from a web page<br>
    5. Switch the editor to the <i>Preview</i> mode to examine the layout<br>
    6. Name the template and choose preferred <a href="../Templates/#create_a_template">Sharing option</a><br>
    7. Click Save<br>
</p>
<br>

<button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/articles/FAQ/#18_how_to_create_flashy_html_templates')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
<!-----------------------------BIG----------------------------------->
<!-----------------------------BIG----------------------------------->

### 19\. How time zones affect timing when a sequence sends out emails?

With Revenue Grid your recipients will never get an email not within business hours of every each of the recipient. There are multiple controls are in place to prevent such occurrence.
<br><br>
First and foremost, every sequence sends every email within hours you specify in <a href="../Settings/#schedules">Schedule</a>. Schedules has nothing to do with time zones yet.
<br><br>
But when another email is getting ready to go out, Revenue Grid first checks prospect's country specified in Salesforce and makes sure to send an email according to <a href="../Settings/#schedules">Schedule</a> in the country's time zone.
<br><br>
If Country field for the recipient is blank in Salesforce, then Revenue Grid will send the email according to preferred <a href="../Settings-of-Sequences/#sending">Sequence's time zone in the settings</a>
<br><br>

<button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/articles/FAQ/#19_how_time_zones_affect_timing_when_a_sequence_sends_out_emails')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
<!-----------------------------BIG----------------------------------->
<!-----------------------------BIG----------------------------------->

### 20\. How to insert "Book me" link into your signature, template or body of an email sent from Revenue Grid?

As you know Revenue Grid offers <a href="https://docs.revenuegrid.com/ri/fast/articles/Sharing-Calendar-Availability-(Adaptive-view)/" target="_blank">the Share Calendar Availability (Book me)</a> feature which allows parsing your available time slots based on your MS Exchange/Office 365 calendar data to be sent to your business contacts. It drastically eases the process of booking a meeting with your business contacts, just add "Book me" link to your email, and let your recipients to choose a time slot suitable for them.
<br><br>
Follow these steps in order to add such link to your signature, template or right to an email sent from Revenue Grid:
<br><br>
1. Open your email in a web browser
<p style="margin-left:4%;">
    For MS Exchange and Office 365 users: from your Desktop Outlook, go to <b>File</b> and click <i>Access this account on the web</i>.
</p>
2. Start composing a new email
<br>
3. Click on Revenue Grid icon, and choose <i>Quick Send Availability</i>
<br>
4.  appeared in the email body text editor
<img src="../../assets/images/faq/copypaste.png" style="width: 350px; height: 250px;"/>
<br>
5. Paste it to wherever you need it in Revenue Grid, whether to your signature, template editor, or to an email when replying from the Action Center.
<img src="../../assets/images/faq/pastethelink.png" style="width: 320px; height: 300px;"/>
<br>

<button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/articles/FAQ/#20_how_to_insert_book_me_link_into_your_signature_template_or_body_of_an_email_sent_from_revenue_grid')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
<!-----------------------------BIG----------------------------------->
<!-----------------------------BIG----------------------------------->

### 21\. How to personalize outreach just for few recipients in a large sequence?

Say you are setting up a new sequence (original). Using "Add recipients" button on the Recipients tab, added a certain number of prospect from SFDC, CSV file or from prospects who have been already imported to Revenue Grid.

While looking through the added prospects, you decide that some of them to get reached out in a different manner rather than the rest, with different email texts or engagement approach.

In this case you need to Move the selected prospects to another Sequence (cloned) and edit steps of the cloned sequence accordingly.

Follow these steps in order to achieve that:<br>

1. Go to <a href="../Overview/">Overview tab</a> of the original Sequence<br>
2. Clone the original Sequence. Once you click "Clone", you will get to the cloned Sequence<br>
3. Go back to the <a href="../Recipients/">Recipients tab</a> of the original Sequence <br>
4. Select checkboxes next to those specific prospect who to get reached out in a different manner<br>     
5. Click the <a href="../Recipients/#mass_and_single_prospect_actions">"More Options"</a> icon appeared in the top right hand side corner of the tab<br>
6. Click "+Add", and choose the cloned Sequence from the drop-down<br>
7. Then right here on the same tab of the original Sequence, select checkboxes next to the same specific prospect again, click the <a href="../Recipients/#mass_and_single_prospect_actions">"More Options"</a> icon appeared in the top right hand side corner of the tab again and choose "Remove from sequence"<br>
8. Now go to the cloned Sequence and edit the steps of the Sequence accordingly<br>
<br>

<button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/articles/FAQ/#21_how_to_personalize_outreach_just_for_few_recipients_in_a_large_sequence')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
<!-----------------------------BIG----------------------------------->
<!-----------------------------BIG----------------------------------->

### 22\. Why is it important to keep a close eye in the Action Center and process all the items appearing on it as soon as possible?

Any given item in the Action Center (a <a href="../Replies/">reply</a>, a <a href="../Notifications/">notification</a>, a <a href="../to-dos/">to-do</a>  type of an item) is dedicated to an individual recipient from one of your sequences. 
<br><br>
The bottom line is, until you handle the appeared item, the recipient will not move forward within a sequence. The sequence will be on pause for this particular recipient. 
<br>
<h4>These types of items in the Action Center <b>pause a sequence for a recipient</b>:</h4>

<h4><a href="../Replies/">on the Replies tab</a></h4>
<p style="margin-left:10%;">☑ Replies to any step of a sequence<br></p>
<h4><a href="../Notifications/">on the Notifications tab</a></h4>
<p style="margin-left:10%;">
    ☑ Notification about Undeliverable emails<br>
    ☑ Autoreplies<br>
    ☑ Standalone emails<br>
    ☑ Meeting invitations<br>
    ☑ Meeting invite response<br>
</p>
<h4><a href="../to-dos/">on the To-dos tab</a></h4>
<p style="margin-left:10%;">
    ☑ Review and Submit an email<br>
    ☑ Colleague's Reply<br>
    ☑ Log a Call<br>
    ☑ Send SMS<br>
    ☑ Log a Misc. type of a step<br>
    ☑ Merge Field issue<br>
    ☑ Owner Change<br>
    ☑ Lead conversion<br>
    ☑ Error sending<br>
</p>
<br>
<div class="admonition example">
    <p class="admonition-title" style="font-size:16px">For example:</p>
    <p style="font-size:16px">
        Say, for a particular recipient, Alex, you have gotten a <a href="../to-dos/#merge_field_issue">Merge Field issue</a> on the <a href="../to-dos/">To-do</a> tab. That means, until you fix it manually, Alex will not receive any following correspondence you had scheduled into the steps of the sequence he is enrolled in.
    </p>
</div>
<br>

<button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/articles/FAQ/#22_why_is_it_important_to_keep_a_close_eye_in_the_action_center_and_process_all_the_items_appearing_on_it_as_soon_as_possible')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
<!-----------------------------BIG----------------------------------->
<!-----------------------------BIG----------------------------------->

### 23\. How to add an unsubscribe link directly to your signature, so you don't have to add it every time to emails or steps manually?

In order to avoid extra time adding an unsubscribe link to every email or step you intend to send out, add it once to your signature. Follow the steps to achieve that:<br>
<p style="margin-left:5%;">
    1. Go to Settings → Signature<br>
    2. Put a cursor where you want an unsubscribe link to appear, usually in the very bottom of a signature.<br>
    3. Click <img src="../../assets/images/faq/mergeicon.png" style="display: inline-block;vertical-align: middle;width: 25px;margin-left: 1px;height: 25px;object-fit: contain;"> Merge Field icon and choose &lcub;&lcub;Unsubscribe Text&rcub;&rcub;<br><br>
    <img src="../../assets/images/faq/unsub-link-in-signature.png" style="width: 750px; height: 250px;"/><br>
    4. Click <img src="../../assets/images/faq/save-button.png" style="display: inline-block;vertical-align: middle;width: 105px;margin-left: 1px;height: 35px;object-fit: contain;"> button so changes get applied<br>
</p>
<br>

<button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/articles/FAQ/#23_how_to_add_an_unsubscribe_link_directly_to_your_signature_so_you_dont_have_to_add_it_every_time_to_emails_or_steps_manually')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
<!-----------------------------BIG----------------------------------->
<!-----------------------------BIG----------------------------------->

### 24\. How to add a person to a sequence right from your email client through Revenue Grid Side panel?

<p>
    <img src="../../assets/images/faq/seq-widget-email-client.gif" style="margin-left:15px; float: right; width: 35%; height: 35%;">
    1. Click on a contact or a lead in the Sidebar to see the pad with details <br>
    2. Switch to Sequences tab<br>
    3. Click 'Add' icon<br>
    4. Select a sequence in the drop-down and click 'Add' button<br>
    <br>
    Note, that if a contact you are trying to add to a sequence hadn't been imported to Revenue Grid at the moment, then on the Sequences tab you can easily import it with just a single click<br><br><a href="../Sidebar/#revenue_inbox_sidebar_opened_in_an_email_client">Read more about controls over Sequences from Revenue Grid Sidepanel</a><br><br><br><br><br><br>
</p>
<br>

<button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/articles/FAQ/#24_how_to_add_a_person_to_a_sequence_right_from_your_email_client_through_revenue_grid_side_panel')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
<!-----------------------------BIG----------------------------------->
<!-----------------------------BIG----------------------------------->

### 25\. How to add a person to a sequence right from SFDC interface?

In order to be able to add a contact or a lead to a sequence right from SFDC interface, you have to set up <a href="../sfdc-widgets/#sales_engagement_widgets">Revenue Grid Sequences widget</a> first.

Once it's set up, it will like this on Contact or Lead screens in SFDC:
<br><br>
<img src="../../assets/images/faq/seq-widget-full.png" style="width: 70%; height: 70%;"/>
<br><br>
For those contacts and leads who have been imported to Revenue Grid, follow these steps to add them to a sequence:
<p style="margin-left:5%;">
    1. Click <img src="../../assets/images/faq/add_seq0.png" style="display: inline-block;vertical-align: middle;width: 25px;margin-left: 1px;height: 25px;object-fit: contain;"> icon<br>
    2. Choose a sequence you want to add to from the drop-down<br>
    3. Click Add button, and as a result, the selected sequence will appear in the widget. Through the widget, you also have certain control over the engagement within the sequence. <a href="../Sidebar/#sequence_widget_in_the_sidebar_opened_in_revenue_grid">Read more here</a>
</p>
<br>
<img src="../../assets/images/faq/adding-thru-widget.png" style="width: 100%; height: 100%;"/><br>
<br>

<button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/articles/FAQ/#25_how_to_add_a_person_to_a_sequence_right_from_sfdc_interface')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
<!-----------------------------BIG----------------------------------->
<!-----------------------------BIG----------------------------------->

### 26\. What happens when you edit a Template?

<!--
<br>
<img src="../../assets/images/faq/seq-widget-full.png" style="width: 70%; height: 70%;"/>
<p style="margin-left:5%;"> 
<br>-->

Be cautious when you edit a <a href="../Templates/">template</a>. Before editing a template, be aware of sequences which have steps built using the template.
<br><br>
When a template gets edited, all steps which the template had been used for will be updated seamlessly. Whether the template-based step is <a href="../Overview/#automatic_vs_manual_type_of_a_step">automatic</a>, then the updated outreach will be carried out in its timely manner; or the template-based step is <a href="../Overview/#automatic_vs_manual_type_of_a_step">manual</a>, then the updated draft will be waiting for you in the Action Center.<br> 

<div class="admonition important">
    <p class="admonition-title">Important</p>
    <p style="font-size:16px">Editing at least one character of a template step, will make the step immune to template edits. Say, you want to build a step based on a template. You pull it in by choosing from the templates drop-down, and then add few extra lines to its text in the editor. In such cases, the step is no more linked to the chosen template, and thus will not be affected if the template gets edited on the <a href="../Templates/">Template</a> tab.</p>
</div>
<br>

<button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/articles/FAQ/#26_what_happens_when_you_edit_a_template')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
<!-----------------------------BIG----------------------------------->
<!-----------------------------BIG----------------------------------->

### 27\. How does the exact time of sending the next email gets calculated?

It all gets figured out by the state of the art algorithm under the hood. Normally, once a user activates a sequence, all its recipients get queued into one stack which shoots emails and SMS one after another within the selected <a href="../Settings/#schedules">delivery schedule</a> and <a href="../Create-new-sequence/#adding_and_editing_steps_toof_a_sequence">Schedule idle</a>. <i>The general bandwidth is 1 email per minute.</i>
<br>
<p>
    <img src="../../assets/images/faq/queue.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;"/>
    But there are cases when a user clicks "Send now" button or schedules a certain email to be sent at a specific time in the Action Center.
</p>
<br><br> 
In such cases, the queue gets shifted and such email cuts the line to get sent out on demand.
<br><br>
Another factor affects queuing is <a href="../Settings/#limits">email bandwidth limits</a>.<br>
<p style="margin-left:5%;">
    For example, if you hit the limit of <i>"Number of sequence touches a RG user can send per day"</i>, then the rest of the steps will be sent out not necessarily on the flowing calendar day, but on the following day within sequence's <a href="../Settings/#schedules">delivery schedule</a>.<br><br>
    ⚠️ And there will be a <a href="../Next-step/#special_indicators">special indicator</a> for queued prospects appearing in the <i>Next step</i> column on the <i>Recipients</i> and <i>Audience</i> tabs.
    <br>
</p>

To sum up, the algorithm considers every email's priority, your and your company's <a href="../Settings/#limits">email bandwidth limits</a> and a <i>Sequence's</i> <a href="../Settings/#schedules">delivery schedule</a>, and as an output, builds the most optimized queue to distribute outreaches.
<br><br>

<button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/articles/FAQ/#27_how_does_the_exact_time_of_sending_the_next_email_gets_calculated')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button></button>

&nbsp;
* * *
&nbsp;
<!-----------------------------BIG----------------------------------->	
<!-----------------------------BIG----------------------------------->


### 28\. How to create a sequence which sends emails only on Thursday?

Say you need a sequence of three emails to get sent on Thursdays only. The first email on the upcoming Thursday, the second on the following Thursday in a week, and the third email on the Thursday coming after that.
<br><br>
Follow these steps in order to set up such a sequence to reach out your prospects only on a certain day of a week.
<br><br>
<p>
    <img src="../../assets/images/faq/spec-schedule.png" style="margin-left:15px;  float: right; width: 40%; height: 40%;">
    1. First, you have to have a <a href="../Settings/#schedules">Delivery Schedule</a> which would be set only to that particular day of the week.
    <p style="margin-left:5%;"> 
        Go to Settings -> Schedule<br>
        Click  <img src="../../assets/images/faq/add-schedule.png" style="display: inline-block;vertical-align: middle;width: 100px;margin-left: 1px;height: 50px;object-fit: contain;"> in the top right-hand corner.<br>
        Create the schedule.<br>
        Read more about <a href="../Settings/#schedules">creating a schedule</a>.
    </p>
</p>
<br><br>
<p>
    <img src="../../assets/images/faq/spec-sch-seq.png" style="margin-left:15px;  float: right; width: 40%; height: 40%;">
    2. Next, make sure you select this schedule when <a href="../Create-new-sequence/#create_a_new_sequence">creating a sequence</a>. <br> 
    <p style="margin-left:5%;">
        Also you can change an existing sequence's delivery schedule on the <a href="../Settings-of-Sequences/#general">Sequence's settings tab</a>.
    </p>
</p>
<br><br><br><br><br><br><br><br><br><br><br>
<p>
    <img src="../../assets/images/faq/idlezero.png" style="margin-left:15px;  float: right; width: 40%; height: 40%;">
    3. Now, it's time to create the 1st steps of the sequence.<br> 
    <p style="margin-left:5%;">
        For the first step, make sure you select 0 days in the <i>Schedule Idle</i> field. That way, the Sequence will start sending the first outreach on the closest upcoming Thursday.<br>
    </p>
</p>
<br><br><br><br><br>
<p>
    <img src="../../assets/images/faq/idlezero2.png" style="margin-left:15px;  float: right; width: 40%; height: 40%;">
    4. When creating the 2nd and the 3rd steps though, it's very important to set 1 day in the <i>Schedule Idle</i> field.<br> 
    <p style="margin-left:5%;">
        If you keep the field at 0, then all 3 emails may get sent out on the same Thursday, and that's what you want to avoid.<br><br>
        You can modify the value even for the existing steps. Just double click the step on the <a href="../Overview/">Overview tab</a> of the sequence, and update the field in <a href="../Create-new-sequence/#email_type_of_a_step">the bottom right-hand corner of the editor</a>.
    </p>
</p>
<br>

<button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/articles/FAQ/#28_how_to_create_a_sequence_which_sends_emails_only_on_thursday')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button></button>

&nbsp;
* * *
&nbsp;
<!-----------------------------BIG----------------------------------->
<!-----------------------------BIG----------------------------------->

### 29\. What folders in an email client get synced with Revenue Grid?

By default, emails only from <i>Inbox</i> and <i>Sent</i> folders of an email client get captured by Revenue Grid.
<br><br>
But by a quick request to our Support team, you can easily have any sub-folder to get synced with Revenue Grid.
<br>

<button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/articles/FAQ/#29_what_folders_in_an_email_client_get_synced_with_revenue_grid')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

<!-----------------------------BIG----------------------------------->
<!-----------------------------BIG----------------------------------->