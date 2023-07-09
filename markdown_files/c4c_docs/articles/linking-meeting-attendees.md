# How SSI Links Meeting Attendees when Syncing Appointments and Visits to SAP Cloud for Customer

&nbsp;

&nbsp;

**[ This article is work-in-progress ]**

&nbsp;

&nbsp;

## Linking attendees pattern

When SSI synchronizes an Appointment or Visit from MS Exchange to SAP Cloud for Customer, attendees get linked with SAP Cloud for Customer records according to the sequence described below.

&nbsp;

For each e-mail address from the "To" and "CC" fields of the Exchange event, SSI performs the following:

1. Search for Employee:
    * If Employee is found, consider a match is found and create:
        * Attendee InvolvedParty with this Employee
    * If none Employees are found, search for Contact

&nbsp;

2. Search for Contact:  
    * If just 1 Contact is found (no duplicates with the same e-mail address), consider a match is found and create:
        * Attendee InvolvedParty with this Contact  
        * Account InvolvedParty of this Contact  
        * Contact InvolvedParty  
    * If none Employee or Contact are found, continue search in Individual Customers

&nbsp;

3. Search for Individual Customer:  
    * If just 1 Individual Customer is found (no duplicates with the same e-mail address), consider a match is found and create:  
        * Attendee InvolvedParty with this Individual Customer  
        * Account InvolvedParty with this Individual Customer  

&nbsp;

4. Otherwise, consider that there is "no match"

&nbsp;

When “no match” is detected, the Attendee InvolvedParty record is created, which does not link to any SAP Cloud for Customer record but contains only the person’s e-mail address and name.

&nbsp;

* * *

&nbsp;

### Additional information

The first found Contact and/or Account become(s) Primary for current activity (which makes the Involved Parties list depict now TWO contacts with the same e-mail addresses). The returned list of Contacts is sorted by the most recently created Contact in descending order. This is an internal algorithm that is not indicated in the external API request.

&nbsp;

Note that the Contact/Account Involved Party can also be updated by SAP Cloud for Customer. This depends on party processing configuration in SAP Cloud for Customer (**Business Configuration** > **Activity List** – **All** – **Activities** > **Maintain Involved Parties for Activities**). Primary Account and primary Contact of this Account Involved Parties are added automatically by SAP Cloud for Customer if this is configured.

&nbsp;

&nbsp;