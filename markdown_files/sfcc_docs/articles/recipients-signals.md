---
description: Assignees selection strategies for Revenue Signals
---

# Select Assignees for Revenue Signals

**[ This is the article for Signals managers]** 

&nbsp;

*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

The assignees for most of Revenue Signals are predefined based on their relationship to Salesforce objects or activities (events, emails); however, some Signals feature advanced assignees configuration options (e.g. [Chosen conditions met for the Salesforce object](https://docs.revenuegrid.com/ri/fast/articles/signals-settings-and-parameters/#1_chosen_conditions_met_for_the_salesforce_object)) when Revenue Grid admins can select the assignees who are to receive a specific Signal.  

<br>

So far, four assignees selection options are implemented for such Signals: 

<br>
<!--<img src="../../assets/images/2301/assignees.png"  style="width: 45%; float: right;margin-left:2%;"/> -->
**Assignees are selected based on the Salesforce relationship:** 

**1.** The signal notification is sent to the user who is the Salesforce **object owner**. 

<br>
**Assignees are selected based on custom preferences:**  

**2.** The signal notification is sent to the **manager** of the user who is the Salesforce object owner. 

**3.** The signal notification is sent to a **list of RG users**. 

<br>
**Assignees are selected based on custom assignees template:**  

**4.** The signal notification is sent to the **users specified in the Json format in the field Custom assignees template**. 


The JSON example of the custom assignees template for selecting the Salesforce opportunity owner, Salesforce opportunity owner's manager and all Signals managers, and excepting the users specified in the list of their IDs: 

```
{ 
    "include": [ 
        { 
            "type": "SalesforceRelationshipSelectorRule", 
            "objectType": "Opportunity", 
            "relationship": "OwnerId" 
        }, 
        { 
            "type": "SalesforceRelationshipSelectorRule", 
            "objectType": "Opportunity", 
            "relationship": "Owner.ManagerId" 
        }, 
        { 
            "type": "ManagersSelectorRule" 
        } 
    ], 

    "exclude": [ 
        { 
            "type": "UserIdsSelectorRule", 
            "userIds": ["<specified-user-ids>"] 
        } 
    ] 
} 

```