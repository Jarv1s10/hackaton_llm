---
title: Handling duplicate records
description: Guide to handling duplicate records when importing prospects from Salesforce and when importing from a CSV file
---



# Automatic handling duplicate records

<p style="font-size:15px"><i>2 min read - updated few hours ago</i> </p>
<!-- ShareThis BEGIN -->
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis -->
<br>

## Handling duplicate records when importing prospects from Salesforce</a> 

These include any prospects from Salesforce, whether from views, reports, or campaigns.
<br><br>
When importing a prospect that already exists in Revenue Grid and had been imported from Salesforce (such <a href="../prospect-profile/">prospects have <img src="../../assets/images/People/contact.svg" style="display: inline-block;vertical-align: middle;width: 25px;margin-left: 1px;height: 25px;object-fit: contain;"> or <img src="../../assets/images/People/lead.svg" style="display: inline-block;vertical-align: middle;width: 25px;margin-left: 1px;height: 25px;object-fit: contain;"> icons</a>), the record in Revenue Grid will be updated with the version coming from Salesforce. And the prospect will be added to a sequence if importing on the <a href="../Recipients/">Recipients tabs</a>. Owner of the record in Revenue Grid will be updated with the user who is importing the record.
<br><br>
When importing a prospect that already exists in Revenue Grid and had been imported from a CSV file (such <a href="../prospect-profile/">prospects have no icon</a> next to their photo), the record in Revenue Grid will be updated with the version coming from Salesforce, <b>but leaving existing values of fields that are blank in Salesforce untouched</b>. In other words, it will blend data. And the prospect will be added to a sequence if importing on the <a href="../Recipients/">Recipients tabs</a>. Owner of the record in Revenue Grid will be updated with the user who is importing the record.
<br>
<hr>

## Handling duplicate records when importing from a CSV file 

### Prospect already exists and you are the prospect owner

If a prospect who is being imported, already exists (matched email) in Revenue Grid and had been imported (matched email) from a CSV file or punched in manually using the <a href="../Recipients/#where_i_can_add_recipients_from">Add a new prospect</a> button (such <a href="../prospect-profile/">prospects have no icon next to their photo</a>), <b>and you are the owner</b> of the prospect, the prospect's information will be overwritten by the currently uploaded file (and the prospect will be added to a sequence if imported on the <a href="../Recipients/">Recipients tabs</a>.)
<br>

### Prospect already exists and you are NOT the prospect owner

If a prospect who is being imported, already exists (matched email) in Revenue Grid and had been imported (matched email) from a CSV file or punched in manually using the <a href="../Recipients/#where_i_can_add_recipients_from">Add a new prospect</a> button (such <a href="../prospect-profile/">prospects have no icon next to their photo</a>), <b>and you are <b>NOT</b> the owner</b> of the prospect, the prospect's information will <b>NOT</b> be overwritten by the currently uploaded file. (and the prospect will <b>NOT</b> be added to a sequence if imported on the <a href="../Recipients/">Recipients tabs</a>.)
<br>


### Prospect already exists and is linked to a Salesforce record

If a prospect who is being imported, already exists (matched email) in Revenue Grid with <a href="../prospect-profile/"><img src="../../assets/images/People/contact.svg" style="display: inline-block;vertical-align: middle;width: 25px;margin-left: 1px;height: 25px;object-fit: contain;"> or <img src="../../assets/images/People/lead.svg" style="display: inline-block;vertical-align: middle;width: 25px;margin-left: 1px;height: 25px;object-fit: contain;"> icons</a>,, the prospect's information will <b>NOT</b> be overwritten by the currently uploaded file (and the prospect will <b>NOT</b> be added to a sequence if imported on the <a href="../Recipients/">Recipients tabs</a>). It doesn't matter whether you are or are not the owner of the prospect.
<br><br>
If there are more than one prospects with the same email in the same CSV file, then while importing each next record updates the preceding one, unless some of the required fields are blank.
<br> <br>
<hr>
## Adding a single prospect via <a href="../Recipients/#where_i_can_add_recipients_from">Add a new prospect</a> feature
 
In this case, even if such prospect (matched email) already exists in Revenue Grid, the newly added prospect will still be added to Revenue Grid and you will end up with two records with the same email.

<br>






