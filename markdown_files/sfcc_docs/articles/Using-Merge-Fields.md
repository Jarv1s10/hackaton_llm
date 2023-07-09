---
title: Personalize your automated outreach with Merge Fields
description: Using Merge Fields️ while creating steps, templates and signature
---

  
# Using Merge Fields️ while creating steps, templates and signatures

<p style="font-size:15px"><i>3 min read - updated few hours ago</i> </p>
<!-- ShareThis BEGIN -->
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis -->

<iframe src="https://player.vimeo.com/video/382438694" width="853" height="505" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>


While creating a mass-sent messages in Revenue Grid, make use of powerful rationalization feature — Merge Fields. It automatically inserts recipient-specific piece of data to email and SMS types of steps. 

<p style="margin-left:2%;">Merge field feature is available when:</p>
<p style="margin-left:4%;"> 
 - Adding a step to a Sequence<br>
 - Adding emails to CC field (because you can merge an email type of a field)
 - Building a template<br>
 - Building a signature<br>
 - Building an unsubscribe text<br>
</p>
<hr>
For example this is how merge-fielded email will look when you build it, and how your recipient will see it:
<img src="../../assets/images/Sequences/merge-field-example.png" style="width: 750px; height: 240px;"/>

<hr>

## Insert a merge field

In order to insert a merge-field value: <br>
<p style="margin-left:2%;">1. Put a cursor where auto-inserted value should appear in the message</p>
<p style="margin-left:2%;">2. Type <b>&lcub;&lcub;</b> to see the drop-down with available variables you can choose from. Alternatively use <b>&lcub;&lcub; &rcub;&rcub;</b> icon on the editor bar.
<br>
 (insert <a href="https://help.salesforce.com/articleView?id=cpq_merge_fields.htm&type=5">merge fields</a>) on the text editor toolbar</p>
<p style="margin-left:2%;">3. Choose what recipient-specific value you want to auto-insert into a mass email. 
</p>
<p>The value gets retrieved from Salesforce (recipient-specific data) or Revenue Grid (sender-specific data such as signature, campaign unsubscribe link, and more).
</p>

  *Commonly used merge-field examples:* Lead/Contact Salutation, Full name and Company name, [RE Sequence](../Sequences/) starter's (Owner's) name and [RE email signature](../Settings/#signatures), [sequence unsubscribe link](../Settings/#the_unsubscribe_section), etc.

<br>
<div class="admonition hint">
<p class="admonition-title">Note</p>
<p>When you use &lcub;&lcub;Sender Phone Number&rcub;&rcub; type of a merge field, Revenue Grid will pull sender's mobile number if available. In case if Mobile field is not populated, then it will show number set in Phone field.</p>
</div>

<hr>

## Troubleshoot broken merge fields

<p> <img src="../../assets/images/faq/merge_preview.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;">
 To check a merge field's validity, you need to switch the editor to <b>Preview mode</b> (use tabs below the editor). Then, choose a recipient from "To:" field drop-down (if you haven't added recipients to the sequence yet, then "To:" field will show John Doe as a placeholder) whom you want to preview the end result for. In preview mode, invalid merge fields get highlighted with red color.
</p>

While processing an email type of a Step, Revenue Grid checks whether all merge field's values are available. Some may not be available due to empty values in Salesforce, wrong syntactic, no API access etc. If a value is missing for a specific prospect, then an automated email containing it will not be sent to the prospect. Instead, it will be moved to [Action Center](../Planner/)'s To-Dos tab and hang on there until handled manually.  

The best practice to fix it, is to populate the missing field (highlighted red) on the recipients' file in Salesforce. Otherwise, remove the merge field tag from the message.
<br>
<hr>

## Use If-Then-Else logic to replace missing fields with alternative values
<br>
While personalizing a mass message, you should merge in a field from Salesforce. When a field is blank for a certain prospect though, utilize if-then-else expression.

<b>Example:</b>

Expected result: "Dear John...", or when name field is blank, simply "Dear Customer...".
<br><br>
Regular expression: "Dear &lcub;&lcub;Name&rcub;&rcub;..." which will cause <i>Merge Field Issue</i> in cases when <i>Name</i> field is blank for a prospect. Go to the Action Center's To-do tab to fix such issue manually. Until you fix the issue, a prospect will hang on there and will not proceed to the next step of a Sequence.
<br><br>
Smart expression: "Dear &lcub;&lcub;#if Name&rcub;&rcub;&lcub;&lcub;Name&rcub;&rcub;&lcub;&lcub;#else&rcub;&rcub;Customer&lcub;&lcub;/if&rcub;&rcub;"
<br><br>

<p> <img src="../../assets/images/Sequences/if-merge.gif" style="margin-left:15px;  float: right; width: 70%; height: 70%;">
The most convenient way to use the smart expression is, type the "#" symbol, and choose the value you want to insert.
<br>
</p>
<br>
<hr>

## Awesome Merge Field options: 

<b>Part of the day</b> merge field: Say you start your outreach with a greeting like "Good &lcub;&lcub;part_of_the_day&rcub;&rcub;", Revenue Grid will pull a value among "morning", "afternoon", or "evening" depending on when exactly the email is being sent off taking into consideration the recipient's time zone:

* "morning" – from 12 AM to 12 PM
* "afternoon" – from 12 PM to 4 PM
* "evening" – from 4 PM to 12 AM

<br>
<b>Last step day</b> merge field: Use this merge field when you want to refer to the previous outreach within a sequence. It works best with Follow-up type of steps. Case use: You have an email type of a step which has been executed on the previous Thursday. The next step in the sequence can have this merge field and look like "I emailed you on &lcub;&lcub;last_step_day&rcub;&rcub;, but never heard back." The recipient will see this: "I emailed you on Thursday, but never heard back."<br>
Note that <b>Last step day</b> merge field will work only if the previous step was executed.

<br>
<b>Book me link</b> merge field: Adds personal Book me link to the email. Depending on <a href="../Settings-of-Sequences/#sending">whose behalf the sequence is being run</a>, you can add &lcub;&lcub;Owner BookMe Text&rcub;&rcub; or &lcub;&lcub;Sender BookMe Text&rcub;&rcub;. Go to settings to <a href="../Settings/#bookme_text">set up your personal Book me link</a>.
<br>
<hr>

## Extra BookMe and Unsubscribe links

<p> <img src="../../assets/images/10082021/extra-book-me-link.png" style="margin-left:15px;  float: right; width: 70%; height: 70%;">
You can add extra book me or unsubscribe links to your email steps. Those links will be associated with the sequence, for complex link tracking and performance measurements.
</p>
<br><br><br><br><br><br><br><br><br><br>
<hr>

## Available Merge Field values

<b>Possible recipient-specific values pulled from Salesforce</b>

|||      |      |
| ---- | ---- | ---- | ---- |
|	First Name	|	Mailing City	|	Photo URL	|	Lead Source	|
|	Last Name	|	Mailing State/Province	|	Clean Status	|	Status	|
|	Full Name	|	Mailing Zip/Postal Code	|	Level	|	Industry	|
|	Title	|	Mailing Country	|	Languages	|	Rating	|
|	LinkedIn	|	Mailing Latitude	|	Deleted	|	Annual Revenue	|
|	Phone Number	|	Mailing Longitude	|	Salutation	|	Employees	|
|	Skype	|	Mailing Geocode Accuracy	|	Company	|	Converted	|
|	Building	|	Business Phone	|	Street	|	Converted Date	|
|	Apartment	|	Business Fax	|	City	|	Unread By Owner	|
|	Zip	|	Home Phone	|	State/Province	|	Created Date	|
|	TimeZone	|	Other Phone	|	Zip/Postal Code	|	Last Modified Date	|
|	Other Street	|	Asst. Phone	|	Country	|	System Modstamp	|
|	Other City	|	Department	|	Latitude	|	Last Activity	|
|	Other State/Province	|	Assistant's Name	|	Longitude	|	Last Viewed Date	|
|	Other Zip/Postal Code	|	Birth date	|	Geocode Accuracy	|	Last Referenced Date	|
|	Other Country	|	Contact Description	|	Phone	|	Company D-U-N-S Number	|
|	Other Latitude	|	Last Stay-in-Touch Request Date	|	Mobile Phone	|	Email Bounced Reason	|
|	Other Longitude	|	Last Stay-in-Touch Save Date	|	Fax	|	Email Bounced Date	|
|	Other Geocode Accuracy	|	Is Email Bounced	|	Email	|	Current Generator(s)	|
|	Mailing Street	|	Data.com Key	|	Website	| Prospect owner email		|
|	SIC Code	|	Product Interest	|	Primary	|		|
|	Number of Locations	|	Jigsaw Contact ID	|	Description	|		|

<b>Possible sender-specific values pulled from Revenue Grid</b>

|    |      |      |
| ---- | ---- | ---- |
|	First Name	|Sender Email|Unsubscribe Text|
|Sender First Name|Sender Title|Unsubscribe Link|
|Sender Last Name|Sender Phone Number|Primary Signature|
|Sender Full Name|Org Name|Secondary Signature|

<div class="admonition hint">
<p class="admonition-title">Note</p>
<p style="font-size:16px">Primary and Secondary signature merge fields are not available when <a href="../Settings/#update_role_set_numbers_for_sending_sms_and_making_voice_calls_log_out">Auto-add signature</a> check-box is selected in Personal Settings.</p>
</div>

<b>Special values</b>

<table data-layout="default">
        <tr>
            <th>
                <p>Values</p>
            </th>
            <th>
                <p>Description</p>
            </th>
            <th>
                <p>Example</p>
            </th>
        </tr>
        <tr>
            <td>
                <p>today</p>
            </td>
            <td>
                <p>Inserts day of the week when an email gets sent out</p>
            </td>
            <td>
                <p>&lcub;&lcub;today&rcub;&rcub; &rarr; Friday</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>tomorrow</p>
            </td>
            <td>
                <p>Inserts the following day of the week when an email gets sent out</p>
            </td>
            <td>
                <p>&lcub;&lcub;tomorrow&rcub;&rcub; &rarr; Saturday</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>days_from_now N</p>
            </td>
            <td>
                <p>Inserts day of the week N days after the email gets sent out</p>
            </td>
            <td>
                <p>&lcub;&lcub;days_from_now 2&rcub;&rcub; &rarr; Sunday</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>weekdays_from_now N</p>
            </td>
            <td>
                <p>Inserts day of the week N workdays after the email gets sent out</p>
            </td>
            <td>
                <p>&lcub;&lcub;weekdays_from_now 2&rcub;&rcub; &rarr; Tuesday</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>part_of_the_day</p>
            </td>
            <td>
                <p>Inserts part of the day when an email gets sent out, considering the recipient&rsquo;s time zone</p>
            </td>
            <td>
                <p>&lcub;&lcub;part_of_the_day&rcub;&rcub; &rarr; morning</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>last_step_day</p>
            </td>
            <td>
                <p>Inserts last step day referring to the previous outreach within a sequence when an email gets sent out</p>
            </td>
            <td>
                <p>&lcub;&lcub;last_step_day&rcub;&rcub; &rarr; Thursday</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Owner BookMe Text</p>
            </td>
            <td>
                <p>Inserts <a href="../Settings/#bookme_text">personal (owner&rsquo;s) Book me link</a> to the email</p>
            </td>
            <td>
                <p>&lcub;&lcub;Owner BookMe Text&rcub;&rcub; &rarr; Book a meeting with me</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Sender BookMe Text</p>
            </td>
            <td>
                <p>Inserts <a href="../Settings/#bookme_text">personal (sender&rsquo;s) Book me link</a> to the email</p>
            </td>
            <td>
                <p>&lcub;&lcub;Sender BookMe Text&rcub;&rcub; &rarr; Book a meeting with me</p>
            </td>
        </tr>
</table>



<style>
  .banners {
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .banners a.button {
      background-color: #FFC827;
      color: #2F3341;
      box-shadow: 0 5px 35px rgba(146, 146, 146, 0.2);
      padding: 20px;
      font-family: Graphic, arial;
      font-weight: 600;
      line-height: 24px;
      margin-top: -80px;
      border-radius: 3px;
      cursor: pointer;
      transition: .1s;
  }

  .banners a.button:hover {
    transform: scale(1.05);
  }

  .banners a.button a:hover,
  .banners a.button a:visited {
      color: #2F3341;
  }

  .banner-3 a.button {
    margin-left: 45%;
  }
</style>

<br>
<div class="banners banner-1">
  <img src="../../assets/images/banners/banner-1.svg" style="width: 100%; height: 100%;">
  <a class="button" href="https://revenuegrid.com/sign-up/?utm_source=kb_rg&utm_medium=referral&utm_campaign=eac&utm_content=banner" target="_blank">Sign up for a free trial</a>
</div>


