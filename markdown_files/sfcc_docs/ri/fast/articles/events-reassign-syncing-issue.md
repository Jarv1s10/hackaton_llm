---
description: Learn how to resolve the issue when events are not synced from Salesforce to Microsoft Outlook till they are reassigned on the Salesforce side
---

# Events Synchronization Problem when Syncing from Salesforce to MS Outlook Calendar

*1 min read*

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

User can face the events synchronization issue when they create a new event in Salesforce, and it does not get synced to their MS Outlook Calendar. However, once User1, who created the event, assigns it to User2 on the Salesforce side, then such event syncs to the User2 MS Outlook Calendar.  

The described synchronization problem may occur when the organization uses Salesforce Impersonation for connection to {{ product_name }} and the dedicated Salesforce Service Account **does not have admin rights** in Salesforce.

&nbsp;

!!! warning "Important"
    **Salesforce Service Account** should be used only for **Salesforce Impersonation** operation. It should not be involved in any activities on the Salesforce side and should not be linked to any mailbox accounts. This user must have admin rights in the Salesforce system

&nbsp;

To resolve the given events synchronization problem, the organization should provide the Salesforce Service Account with the **System Administrator rights** in Salesforce, including the corresponding license and user profile.

<p>
<img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\events-reassign-syncing-issue\1.png">
</p>

&nbsp;

&nbsp;

***

&nbsp;

&nbsp;

**Refer to related articles describing Impersonation configuring:**

* [How to Configure Impersonation to Deploy the Solution [MS Exchange On-Premises]](../Set-up-An-Impersonation-Service-Account/)

* [How to Set Up Sync via Impersonation & Configure User Mailboxes](../Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/)

* [How to Configure Impersonation to Deploy the Solution [Office 365]](../Impersonation-O365/)

* [How to Configure App-Only Access to Deploy the Solution via MS Graph Connection [Office 365]](../Impersonation-Graph/)

* [Impersonation Setup: Hybrid Scenarios](../Impersonation-Alternative/)

&nbsp;