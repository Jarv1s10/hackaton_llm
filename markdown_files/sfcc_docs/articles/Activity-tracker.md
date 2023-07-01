---
title: Revenue Gird, a glimpse to under the hood
description: Revenue Grid activity tracker explained: metadata processing for enhancing your sales performance
---


  

# Invisible activity tracker plays a crucial, cross-functional role under the hood

<p style="font-size:15px"><i>1 min read - updated few hours ago</i> </p>
<!-- ShareThis BEGIN -->
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis -->

Real time sales guidance mechanisms of Revenue Grid are backed up by metadata which is being collected, parsed, indexed and stored on the secured servers. Metadata includes details of email correspondence and calendar items company wide. 
<br><br>
Once such activity is detected, it gets parsed, categorized and matched to information stored in Salesforce.
<br><br>
Such implementation is carried out via <a href="https://developers.google.com/gmail/api">Gmail API</a>, <a href="https://developers.google.com/calendar">Calendar API</a>, <a href="https://developers.google.com/drive">Drive API</a> for Gmail inboxes; and via <a href="https://docs.microsoft.com/en-us/office/dev/add-ins/outlook/web-services">Exchange Web Services (EWS)</a> for MS Exchange and Office 365 inboxes.
<br><br>
###Values in Revenue Grid interface derived from Activity Tracker



<p><img src="../../assets/images/Activity-tracker/cap1.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;"/>
While reviewing <a href="../Pipeline-visibility/">Pipeline Visibility</a> and <a href="../Account-visibility/">All Accounts dashboard</a>, the count of sent/received emails, conducted meetings, people involved total, as well as the most recent touch details are possible due to the Activity Tracker running on the background.
</p>
<br>
<p><img src="../../assets/images/guided/newchart.png" style="margin-left:15px;  float: right; width: 60%; height: 60%;"/>
People Intelligence charts on the <a href="../Opportunity-details/">Opportunities 360</a> and <a href="../Account-details/">Account details</a> tabs, which show who from your company have been in touch with each of representatives of an opportunity is possible because of the Activity Tracker.<br><br>
</p>
<br>
<p><img src="../../assets/images/Activity-tracker/cap3.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;"/>
Activity trend charts on the <a href="../Opportunity-details/">Opportunities 360</a> and <a href="../Account-details/">Account details</a> tabs, which show all meetings and email scattered on a timeline is being drawn based on records captured by the Activity Tracker.<br><br><br><br>
</p>

<br>
<p><img src="../../assets/images/guided/last-f-touch.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;"/>
Engagement highlight blocks on the <a href="../Opportunity-details/">Opportunities 360</a> and <a href="../Account-details/">Account details</a> tabs, which consolidate pieces of information such as the first and the last touches, certain types of "What's Next" values are also being drawn based on records captured by the Activity Tracker.
</p>
<br>
<p><img src="../../assets/images/guided/signals1.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;"/>
Many <a href="../Signals/">Signals</a> are being triggered based on conditions captured by the Activity Tracker. For example a signal notifying that a meeting follow up has been sent out by a Sales Rep; or Activity Summary Signals, which gather and send summary of executed actions on regular basis. 
</p>

<br><br><br>
<p><img src="../../assets/images/08052021/team12.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;"/>
Number of sent/received emails and conducted meetings per employee on the <a href="../team-coaching/">Team tab</a> gets reflected based on records captured by the the Activity Tracker. 
</p>
<br><br><br><br><br><br><br><br><br>
<div class="admonition important">
<p class="admonition-title">Streaming data vs Activity Tracking</p>
<p style="font-size:16px">While ability to see an indication that there has been a certain number of emails is possible due to the Activity Tracking component. Whereas being able to drill deeper and actually read context of an email with just a click, gets carried out by streaming the context right from employee's inbox. No data is stored anywhere else.</p>
</div>










