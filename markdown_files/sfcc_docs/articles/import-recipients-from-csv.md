---
title: Importing prospects from a CSV file
description: Detailed guide on importing prospects from a CSV file
---



# Import recipients from a CSV file

<p style="font-size:15px"><i>3 min read</i> </p>
<!-- ShareThis BEGIN -->
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis -->
<br>


<div class="admonition hint">
<p class="admonition-title">Note</p>
<p style="font-size:16px">In order to enable the feature to upload prospects from a CSV file, your Revenue Grid Admin must enable it in <a href="../admin-settings/#allow_upload_and_export_fromto_csv">the Import/Export tab of the settings</a>.</p>
</div>


In order to add recipients from a CSV file to a sequence, first make sure your CSV file is in the right format and has all necessary columns in place, spelled and deliminated correctly. Then, you can upload it to Revenue Grid: directly on the [*Recipients*](../Recipients) tab of a particular sequence, or to the main pool of prospects on the [*Audience*](../People) page.
<br>


Prospects imported from a CSV file have **no icon next to their logo** in Revenue Grid (if they are not linked to any Salesforce records), while prospects imported from Salesforce will be marked with <img src="../../assets/images/People/contact.svg" style="display: inline-block;vertical-align: middle;width: 25px;margin-left: 1px;height: 25px;object-fit: contain;"> Salesforce Contact and <img src="../../assets/images/People/lead.svg" style="display: inline-block;vertical-align: middle;width: 25px;margin-left: 1px;height: 25px;object-fit: contain;"> Salesforce Lead icons.

Prospects imported from Salesforce and CSV will remain in Revenue Grid until they are manually deleted. 

<hr>

###CSV file format

These are the headers of the columns which should match exactly like in the template. 
<img src="../../assets/images/Sequences/csv-format.png" style="width: 740px; height: 105px;">
<a href="../../assets/images/Sequences/template.csv">Download template</a><br>
<b>Required columns: email, firstName, lastName</b><br>
<b>Optional columns: all the rest</b>

<img src="../../assets/images/Sequences/csv-format2.png" style="width: 540px; height: 105px;">

In the example above, second prospect in the list won't be uploaded to Revenue Grid because of missing value in one of the required columns.
<br><br>
Make sure you double check your CSV file opened in MS Excel or in any other supported CSV file editor.
<br>

<hr>
###Importing prospects to Revenue Grid from CSV file

You can import recipients directly into one of your sequences, or to the Audience page to the major pool of prospects in Revenue Grid.
<br>

<p style="margin-left:2%;"><img src="../../assets/images/08052021/add_recipients_from.png" style="margin-left:15px;  float: right; width: 25%; height: 25%;"> 1. Click <img src="../../assets/images/faq/add_recipients_button.png" style="display: inline-block;vertical-align: middle;width: 90px;margin-left: 1px;height: 60px;object-fit: contain;"> button in the top right-hand corner, and choose "CSV"</p>
<br><br><br><br>
<p style="margin-left:2%;">2. In the appeared dialog box, choose a file or drag-and-drop it to the gray area. </p>

<img src="../../assets/images/Sequences/import-csv1.png" style="width: 750px; height: 450px;"/>
<p style="margin-left:4%;">
Once a file is chosen, <b>Preview</b> area will parse first two rows from your CSV file. There may be a case when you would get error messages. </p>

<p style="margin-left:4%;"><img src="../../assets/images/Sequences/import-preview.png" style="margin-left:15px;  float: right; width: 250px; height: 50px;">
Missing mandatory column - means at least one header of the required columns is missing or mistyped. Please open your CSV file on your computer via MS Excel or any other supported editor and make sure that required headers all properly delimited and look good.<br><br>
No relevant data - means the chosen file is empty.
</p>
<br><br>
<p style="margin-left:2%;">3. Choose values in the <i>Character Code</i> and <i>Values Separated By</i> drop-downs and click "Import".</p>

<img src="../../assets/images/07202022/6.png" style="width: 50%; height: 50%;"/>

<p style="margin-left:4%;">
<i>Total</i> - how many rows have been found in the file (besides the header row)<br>
<i>Created</i> - how many prospects have been successfully imported<br>
<i>Matched existing</i> - how many prospects match already existing prospects with the same email<br>
<i>Failed</i> - how many prospects had blank at least one value in required fields<br>
<i>Added to sequence</i> (this appears only when you importing into a sequence on the <a href="../Recipients/">Recipients tab</a>, as opposed to on the Audience page) - it equals to number of <i>Created</i> prospects, and shows how many prospects have been added to the sequence<br>
</p>
<br>
<hr>
What happens when I have duplicated prospects? Refer to <a href="../handling-duplicate-records/">this article for details on how Revenue Grid handles duplicates while importing prospects</a>. 




<br>






