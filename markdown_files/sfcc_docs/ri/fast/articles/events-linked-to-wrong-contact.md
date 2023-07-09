--- 

description: Learn how to address an issue where events created using Book Me link are linked to a wrong Contact in Salesforce 

--- 

# Events Created with Book Me Feature are Linked to a Wrong Contact in Salesforce 

*4 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;
 

{{ short_company_name }} Email Grid offers [Share Calendar Availability (Book me)](https://docs.revenuegrid.com/ri/fast/articles/Sharing-Calendar-Availability-%28Adaptive-view%29) feature that allows parsing your and your colleagues’ availability periods based on MS Exchange / Office 365 calendar data to be sent to your contacts to negotiate a meeting time convenient for all participants involved. 

If you have faced an issue where calendar items created using [Book me](https://docs.revenuegrid.com/ri/fast/articles/Sharing-Calendar-Availability-%28Adaptive-view%29) feature are not saved to the relevant Contacts in Salesforce as expected, follow the instructions provided below in this article to handle this issue. 

Two possible manifestations of this issue: 

* After a Book Me link is sent to the Recipient and the time slot is selected, the event on the Organizer’s Salesforce calendar is linked to a wrong Contact in Salesforce.  

* When an Organizer schedules a meeting with a new Contact whose email address has not been saved in Salesforce yet, a new Contact record is created in the CRM, however the newly created Contact is not linked to the relevant Event record. 


This issue may occur due to specific saving patterns of custom properties in *Salesforce records* field on the *Linked records* tab during the generation of Book Me links. 

&nbsp;
 ***
 

## How to address this issue in existing meetings 

You can troubleshoot this issue in the meetings that have already been scheduled and synced to Salesforce in two ways: 

**1\.1\.** Find the necessary event on your Outlook calendar 

**1\.2\.** Click **Edit** and open {{ product_name }} 

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\event-linked-to-wrong-contact\event-edit-outlook.png" style="width:70%">
</p>

<br>

**1\.3\.** Click **Event is saved** to see the event details 

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\event-linked-to-wrong-contact\event-is-saved2.png" style="width:50%">
</p>

<br>

**1\.4\.** In the *Name* field, specify the Contact record to be linked with the meeting  

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\event-linked-to-wrong-contact\name-field.png" style="width:50%">
</p>

<br>

**1\.5\.** Click **Save** to apply the changes 

**1\.6\.** After the next sync session, the changes will be reflected in Salesforce 

 
&nbsp;

Alternatively, to link the existing meeting with the relevant contact:  

<br>

**2\.1\.** Find the necessary event on your Outlook calendar 

**2\.2\.** Click **Edit** and open {{ product_name }} 

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\event-linked-to-wrong-contact\event-edit-outlook.png" style="width:70%">
</p>

<br>

**2\.3\.** Find the *Contact* tab and click on it to see the relevant contact record 

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\event-linked-to-wrong-contact\contact1.png" style="width:50%">
</p>

<br>

**2\.4\.** Click on the arrow on the Contact card to view the detailed object card

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\event-linked-to-wrong-contact\contact0.png" style="width:50%">
</p>

<br>

**2\.5\.** Make sure that the *Name* field is prefilled with the relevant Contact's name

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\event-linked-to-wrong-contact\contact2.png" style="width:50%">
</p>

<br>

**2\.6\.** Click **Save event** to link the meeting with the relevant contact 

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\event-linked-to-wrong-contact\contact3.png" style="width:50%">
</p>

<br>

**2\.7\.** After the next sync session, the changes will be reflected in Salesforce 

 &nbsp;
 ***

## How to prevent this issue in future 

There are two ways to prevent such issues in future and ensure that the created events are linked to the right Contact record in Salesforce: 

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\event-linked-to-wrong-contact\link-both.png" style="width:50%; display:inline-block; vertical-align:middle; margin-left:1px;float: right; margin-top:1rem;"></p>
&nbsp;

* When creating a [Book Me link](https://docs.revenuegrid.com/ri/fast/articles/Sharing-Calendar-Availability-%28Adaptive-view%29/#to_initiate_a_meeting_by_sharing_your_availability_periods_with_business_contacts), **specify both** *Salesforce record* and *Lead* or *Contact* on the Linked records tab. In this way, the created meeting will be correctly linked to the selected records in Salesforce 


<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\event-linked-to-wrong-contact\link-none.png" style="width:50%; display:inline-block; vertical-align:middle; margin-left:1px;float: right; margin-top:1rem;"></p>
&nbsp;

* When creating a [Book Me link](https://docs.revenuegrid.com/ri/fast/articles/Sharing-Calendar-Availability-%28Adaptive-view%29/#to_initiate_a_meeting_by_sharing_your_availability_periods_with_business_contacts), **do NOT specify** *Salesforce record*, *Lead* or *Contact* on the Linked records tab. Leave these fields empty to ensure that the Contact/Lead is automatically recognized and the relevant Contact/Lead and related Salesforce account is linked to the event 

