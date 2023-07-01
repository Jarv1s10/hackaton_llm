---
title: Twilio setup
description: Learn how to setup Twilio SMS and voice calls for your Revenue Grid
---



# How to setup Twilio SMS and voice calls for your Revenue Grid

<p style="font-size:15px"><i>2 min read - updated few hours ago</i> </p>
<!-- ShareThis BEGIN -->
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis -->



<br>


<h2>Follow these steps in order to set up Twilio as your provider of SMS and Voice calls from Revenue Grid or Salesforce interface.</h2>

1. Create and log in to your Twilio account.
<p style="margin-left:2%;"> <img src="../../assets/images/12022021/twil0.png" style="margin-left:15px;  float: right; width: 65%; height: 65%;"/>
Go to <a href="https://www.twilio.com/">https://www.twilio.com/</a> and create a free account, you won't need to pay until you are ready to top up your balance.
<br><br>
On the home page of the Twilio profile, you should see <b>Account SID</b> and <b>Auth Token</b>. You are going to need it on Step 7 coming shortly below.
</p>

<br>

2. Create TwilML App.
<p style="margin-left:2%;"> <img src="../../assets/images/12022021/twil2.png" style="margin-left:15px;  float: right; width: 35%; height: 35%;">
Then proceed to TwilML Apps tab, and click <b>Create new TwilML App</b>
</p> 
<br><br><br><br><br><br><br><br><br><br>


3. Continue creating TwilML App.
<p style="margin-left:2%;"> <img src="../../assets/images/12022021/twil3.png" style="margin-left:15px;  float: right; width: 75%; height: 75%;">
<b>Voice Request URL</b> field has to be populated with this URL.<br>Replace [Your Tenant Name] in the URL with the name of your tenant, otherwise the setup won't go further.<br><br>

</p>

<div class="admonition important" style="margin-left:7%;">
<p class="admonition-title" >Voice Request URL</p>
<p style="font-size:16px; margin-left:2%;"><i>https://[Your Tenant Name]-drip.revenuegrid.com/api/v1.0/communication/twilio/voiceCallback</i></font><br><br>
Example of the URL for Stark Media: <i>https://starkmedia-drip.revenuegrid.com/api/v1.0/communication/twilio/voiceCallback</i></font>
</p>
</div>




<br>
  

4. Complete creating TwilML App.
<p style="margin-left:2%;"> <img src="../../assets/images/12022021/twil4.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;">
Click <b>Save</b> and you should see <b>SID</b> of your TwilML App on the screen. You are going to need this value on Step 7 below.<br><br>
If the value doesn't appear on the screen, that means Twilio hasn't accepted the URL. Contact us for further review.



</p>

<br><br><br><br>


5. Add new numbers to your Twilio account to use it from Revenue Grid.
<p style="margin-left:2%;"> <img src="../../assets/images/12022021/twil5.png" style="margin-left:15px;  float: right; width: 60%; height: 60%;">
You can purchase numbers which Sales team can set up for their individual Revenue Grid profiles.<br><br>
Keep in mind that if you purchase a number for SMS sending, you'll be able to use such number for Voice calling out of Revenue Grid as well.<br><br>

</p>

<br><br>

6. Add Sales team members' existing mobile phone numbers (if they want to) for calling out of Revenue Grid.<br>
<p style="margin-left:2%;"> <img src="../../assets/images/12022021/twil6.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;">
Go to <b>Phone numbers → Manage → Verified Caller IDs</b>.<br><br>
</p>
<br><br>
<p style="margin-left:2%;"> <img src="../../assets/images/12022021/twil7.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;">
Click <b>Add a new Caller ID</b>, to enter the number and verify. After the setup is done. Every individual Revenue Grid user will be able to pick his/her number and use it from Revenue Grid, see below.

</p>


<br><br><br><br><br><br><br><br>


7. Proceed to the Revenue Grid side for the final steps of the setup.
<p style="margin-left:2%;"> <img src="../../assets/images/12022021/sms-and-calls.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;">
Go to Revenue Grid Admin Settings → SMS & Calls.
<br><br>
On this subtab, you have to populate <b>Account SID</b> and <b>Token</b> fields with the values taken from Step 1 mentioned above.<br><br>
Also, populate the <b>Voice application SID</b> field with the value from Step 4 mentioned above.<br><br>
Click <b>Save</b>.
</p>
<br><br><br>
8. Assign numbers to individual users in Revenue Grid.
<p style="margin-left:2%;"><img src="../../assets/images/07082021/settings-account.png" style="margin-left:15px;  float: right; width: 45%; height: 45%;">
You are almost done. Now, users have to go to their Revenue Grid personal settings, and pick available numbers from the corresponding drop-down, whether it's meant to be for SMS or Voice calls.<br><br>
Every number is being used only by one user.<br><br>
If a Revenue Grid user provided his/her own phone number for the verification on Step 6, then this is where the user can pick his/her own number and start outreach.<br><br>
Admins can set this personal level setting for <a href="../admin-settings/#manage_all_users">every Revenue Grid user</a> as well.
</p>

<br><br><br>
And that's it, folks. Now Revenue Grid will use the corresponding number when users <a href="../to-dos/#send_sms">send SMS messages</a> and <a href="../to-dos/#make_a_call">conduct Voice calls</a> from the Action Center, or from the <a href="../sfdc-widgets/#dial_out"><b>Dial out</b> widget in your Salesforce interface</a>.


<br><br>











