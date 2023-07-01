---
description: How to investigate and resolve the issue where the Add Sequence button is missing on the RG Lead Sequences widget on some Lead pages in Salesforce
---
# How to Resolve the Missing *Add Sequence* (+) Button on the {{ short_company_name }} Lead Sequences Widget


*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\missing-add-sequence-button\add-button.png" style="width:44.4%; display:inline-block; vertical-align:middle; margin-left:5px; float: right">
</p>

If, while using the Sequences, you face the situation where the **Add Sequence** <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\missing-add-sequence-button\plus.png" style="display:inline-block; vertical-align:middle; margin:1px; object-fit:contain;"> button is missing on the [{{ short_company_name }} Lead Sequences widget](../../../../articles/sfdc-widgets/#sequences_enrolled) on some Lead pages in Salesforce, that could occur due to several reasons.

This article describes the reasons for the **Add Sequence** <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\missing-add-sequence-button\plus.png" style="display:inline-block; vertical-align:middle; margin:1px; object-fit:contain;"> button missing and possible ways to investigate and address this issue.

&nbsp;

***

&nbsp;

## The recipient is opted out from sequences' outreaches

The **Add Sequence** <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\missing-add-sequence-button\plus.png" style="display:inline-block; vertical-align:middle; margin:1px; object-fit:contain;"> button becomes unavailable on the {{ short_company_name }} Lead Sequences widget on the Lead page in Salesforce if the recipient is [opted out from sequences' outreaches](../../../../articles/FAQ/#5_how_to_opt-out_a_recipient_from_a_sequences_outreaches). That is done by design to prevent adding opted-out recipients to sequences.
<br><br>

You can check whether the recipient is opted out on the [recipient's profile page in {{ company_name }}](../../../../articles/prospect-profile/).

To make the **Add Sequence** <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\missing-add-sequence-button\plus.png" style="display:inline-block; vertical-align:middle; margin:1px; object-fit:contain;"> button available on the {{ short_company_name }} Lead Sequences widget on the Lead page, you need to [add the relevant recipient to a Sequence](../../../../articles/FAQ/#1_how_to_add_a_prospect_to_a_sequence) again.

&nbsp;

***

&nbsp;

## The number of active sequences has reached the limit

Another reason the **Add Sequence** <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\missing-add-sequence-button\plus.png" style="display:inline-block; vertical-align:middle; margin:1px; object-fit:contain;"> button may be missing on the {{ short_company_name }} Lead Sequences widget is related to the sequences' limit. If the number of active sequences reaches the limit value, the system blocks the ability to add more sequences and removes the **Add Sequence** <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\missing-add-sequence-button\plus.png" style="display:inline-block; vertical-align:middle; margin:1px; object-fit:contain;"> button from the {{ short_company_name }} Lead Sequences widget.
<br><br>

You can check the limit values set for the sequences on the [**Limits** page in {{ company_name }} settings](../../../../articles/admin-settings/#control_sending_capacity_and_other_limits). However, the Admin rights are required to access and adjust **Sequences' Limits**.
<br><br>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\missing-add-sequence-button\settings.png" style="width:22.08%; display:inline-block; vertical-align:middle; margin-left:10px; float: right">
</p>

To open the [**Limits** page](../../../../articles/admin-settings/#control_sending_capacity_and_other_limits), click the **Settings** icon in the top right corner of the {{ short_company_name }} interface, then go to **Sequences** under **Platform Settings** and select **Limits**.
<br><br>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\missing-add-sequence-button\limits.png">
</p>