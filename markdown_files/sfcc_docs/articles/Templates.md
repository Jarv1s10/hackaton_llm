---
title: Save time with templates
description: Learn how to manage Revenue Grid (RG) message Templates used for facilitating and automating creation of email Sequence steps
---

  
# How to manage email templates

<p style="font-size:15px"><i>2 min read - updated few hours ago</i> </p>
<!-- ShareThis BEGIN -->
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis -->

<img src="../../assets/images/Templates/temp-mail.png" style="width: 100%; height: 100%;"/>

Revenue Grid (RG) message Templates are used for facilitating and automating creation of email Sequence steps. A template is a typical message used at a single step of an engagement/nurturing campaign.

Every RG user within an Org can contribute templates to a shared template pool, so others will be able to make use of them in their own [Sequences](../Sequences/).

<br><br>
<hr>
### Find the most successful templates

<p> <img src="../../assets/images/07082021/successful-temps.png" style="margin-left:15px;  float: right; width: 40%; height: 40%;">
In order to identify which templates have been the most successful across all sequences, sort the tab by Click, Success, or Reply rates. 
</p>
<br><br><br><br><br><br>



<hr>


### Create a Template

In order to create or edit a template:
<p style="margin-left:2%;">

1. Open the Templates page
<br><br>
2. Click <b>Add template</b>

<img src="../../assets/images/Templates/maintemplate.png" style="width: 550px; height: 270px;"/>

3. Fill in the template's fields:
</p>
<p style="margin-left:5%;">
- <i>Name</i>: enter a unique name used to refer to the template<br><br>
- <i>Sharing</i>: set use permissions<br>
</p>
<p style="margin-left:10%;">
•	<i>Private</i>: visible only to you<br><br>
•	<i>Shared</i> [the default selection]: all users can view(read-only) it and clone this template<br><br>

<div style="margin-left:10%" class="admonition important">
<p class="admonition-title">Note</p>
<p >Admins always can view, select, edit and clone all templates regardless of settings per Template mentioned above</p>
</div>

</p>
<p style="margin-left:10%;">
- <i>Subject</i>: set the email template's Subject line. You may also insert Salesforce and Revenue Grid <a href="../Using-Merge-Fields/">merge fields</a> into it to make it match a specific prospect<br><br>
- Template body: design your email template's text using the standard text editing bar<br><br>
- Use Revenue Grid <a href="../Using-Merge-Fields/">merge fields</a>. It allows personalize a message across companies with the same template. <br><br>
- Add an attachment to your template using  <img src="../../assets/images/Steps/attach.png" style="display: inline-block;vertical-align: middle;width: 3%;margin-left: 1px;height: 3%;object-fit: contain;"> button on the bar.  Supported types:  pdf, doc, docx, xls, xlsx, ppt, pptx, csv, txt, rtf, ods, odt, html, zip, 7z, rar,  mp3, mp4, wma, mpg, flv, avi, jpg, jpeg, png, gif, epub, fb2<br><br>
- Paste an inline image from clipboard or add by using  <img src="../../assets/images/Steps/inline.png" style="display: inline-block;vertical-align: middle;width: 3%;margin-left: 1px;height: 3%;object-fit: contain;"> button on the bar. You may include an image from your local computer or from the Web by pasting in a link. <br><br>
</p>
<p style="margin-left:2%;">
4. Click <b>Save template</b></p>
<br>

<hr>
### Template statistics

<p style="margin-left:2%;"> <img src="../../assets/images/07082021/temp-stat.png" style="margin-left:15px;  float: right; width: 60%; height: 60%;">
Every template has its own statistics to identify how engaging it has been over time.
</p>
<br><br><br><br><br><br>
<hr>
### Edit a Template

There are 2 ways to update a template:
<p style="margin-left:2%;">
On the Templates tab, open a template you'd like to edit. Apply changes in the opened text editor and save the template.
</p>
<p style="margin-left:2%;"> <img src="../../assets/images/Sequences/updatetemplate.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;">
1. Or another way. When <a href="../Create-new-sequence/#email_type_of_a_step">adding a step</a> based on a template, you will have an option to update the used template along with adding the step.
</p>

<div class="admonition danger">
<p class="admonition-title">Important</p>
<p style="font-size:16px">2. Once a <a href="../Templates/">template</a> gets updated, all steps of <i>Sequences</i> which had been built based on the template start using the most recently updated version of the template. Including those emails which are <a href="../to-dos/#review_and_submit_an_email">waiting for a review in the Action Center</a>.</p>
</div>
 <br> 


<hr>
### More hints on Templates

<p><img src="../../assets/images/Templates/hint1.png" style="width: 450px; height: 270px; float: right;"/>
In order to make your email look perfect in inboxes of your recipients, make sure you add a special first line to be displayed in Outlook folder preview:<br><br>
Follow the steps to achieve that:<br></p>
<p style="margin-left:2%;">
1)	Switch the editor to <i>Source</i><br><br>
2)	Add the code line onto the first line of your template:
<br><br>
<img src="../../assets/images/Templates/theline1.png" style="width: 80%; height: 80%;"/>
<br>
Replace the text with yours. The text is hidden in the email body and displayed only as preview in an Inbox folder item.<br>
<br>
Also avoid centered signatures or other elements:
<p style="margin-left:2%;">
There are two elements responsible for alignment in HTML: </p>
<p style="margin-left:5%;">
(a) tag's property align="center"; <br>
(b) style="text-align:center;".</p> 

Please avoid using both when they have different values in the same Template – in this case a browser takes one, while Desktop Outlook takes another one. Use only one of those, or both have to have equal values.
</p>

<hr>
###Utilize templates right in an email client via Revenue Grid Email Sidebar Smart Actions

<iframe title="vimeo-player" src="https://player.vimeo.com/video/554620367" width="640" height="360" frameborder="0" allowfullscreen></iframe>

<hr>
###Favorite Templates

<p> <img src="../../assets/images/02042022/2.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;">
Mark your favorite templates as favorite for quick access when creating <a href="../Create-new-sequence/#email_type_of_a_step">a step for your Sequences</a>.
</p><br>
<img src="../../assets/images/02042022/3.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;">
<br><br><br><br><br>

<hr>
###Clone, view, archive, delete a Templates

<p> <img src="../../assets/images/03092022/templates-actions.png" style="margin-left:15px;  float: right; width: 25%; height: 25%;">
Access more actions you can perform with a template through the menu button on the right-hand side of each template.

</p>
<br><br><br><br><br>

###Who is using a template. Usage information.

<p> <img src="../../assets/images/09272022/11.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;">
This tab shows which sequences has been based on the template, including owners of the sequences for the reference.
</p>
<br><br><br>
<br><br><br>






