# How to Resolve SSI Synchronization Issues



&nbsp;

When using [SSI Sync Engine](../C4C-SSI-Sync-Overview/) to synchronize data between your mailbox and SAP Cloud for Customer, sometimes you may encounter certain sync issues. [SSI Sync dashboard](../Synchronization-Dashboard/) includes a dedicated tab that allows to monitor these issues for troubleshooting.

&nbsp;

!!! warning "Important"
    Do not confuse synchronization **issue** and synchronization **error**, when synchronization becomes completely non-functional and no records can be synchronized
    
&nbsp;

*   **Issues.** Synchronization issues are logged in the tab when SSI Sync encounters conflicts between synchronized data sources or due to less obvious reasons. Every issue's log usually includes a sync error code or notification returned by SAP Cloud for Customer and indicates the source of the error.

<p>
<img src= "..\..\assets\images\Sync-Issues\574d8ac5c6979138ff609d3c.png">
</p>

&nbsp;

*   **Account credentials changed.** These issues occurs if your MS Exchange / Office 365 / Gmail or SAP Cloud for Customer login credentials were changed and SSI can no longer access your data. See the section describing [credentials renewing](../Sync-Issues-Troubleshooting/#renewing_cloud_for_customer_or_mail_data_access_credentials) below for more information  

<p>
<img src= "..\..\assets\images\Sync-Issues\574d8c559033605108fde741.png">
</p>

&nbsp;

&nbsp;

Detailed information about each Sync issue can be found [on the Dashboard](../Synchronization-Dashboard/) and Issues pages. If your local Admin cannot resolve the issue locally, you can get [our Support Team](https://support.sap.com/en/contact-us.html)'s assistance. Provide our Support Team with a detailed description of the issue, including error codes and screenshots, so they can start troubleshooting without delay. 

<p>
<img src= "..\..\assets\images\Sync-Issues\3.png">
</p>

&nbsp;

In addition, for the cases when SSI is unable to access your mailbox or SAP Cloud for Customer data or if data syncing fails 10 times consecutively, SSI can be configured to send the Key Users / Admins a notification e-mail informing them about the need for action to resolve the issue and resume data syncing.

&nbsp;



In case a persistent Sync access issue occurs, for example, due to Sync misconfiguration, you may need to revoke the mailbox data access token. After that, [re-activate Sync for the mailbox](../How-to-Configure-User/).

&nbsp;

* * *

&nbsp;

## How to Investigate Synchronization Issues

A synchronization issue occurs when SSI is unable to synchronize data between SAP Cloud for Customer and Microsoft Exchange / Office 365 or Gmail due to a reason on either side. In many cases, these issues are caused by incomplete data availability on e-mail server side, e.g. missing Contact key fields values, like Last name, or by specific SAP Cloud for Customer rules that may prevent users from editing or deleting objects of certain types.

&nbsp;

When a Sync issue occurs, SSI notifies the concerned users in the following ways:

*   In MS Outlook, the item for which a Sync issue occurred is assigned two custom categories: a red *“Sync Error”* category and a white category providing extra details  

<details>
<summary>>>> Click to see a screenshot <<<</summary>
    <p>
        <img src="..\..\assets\images\Sync-Issues\5832fc42903360645bfa6a98.png">
    </p>
</details>

&nbsp;

In Gmail mail client, the item for which a Sync issue occurred is assigned a custom label "*SAP E-Mails/Sync Error*" for e-mails or a red marker for events.

<details>
<summary>>>> Click to see a screenshot <<<</summary>
    <p>
        Label "<em>SAP E-Mails/Sync Error</em>" for e-mails with sync issues:
    </p>
    <p>
        <img src="..\..\assets\images\Sync-Issues\gmail-error-category.png">
    </p>
    <br>
    <br>
    <p>
        Red marker for events with sync issues:
    </p>
    <p>
        <img src="..\..\assets\images\Sync-Issues\event-error-category.png">
    </p>
</details>

&nbsp;

*   Information about logged sync issues is displayed on the **Issues** tab of the [SSI Sync Dashboard](../Synchronization-Dashboard/). To view issues encountered with a certain handled item type, click on an item type (e.g. Contact, Accounts, Tasks, E-Mails, etc.)

<p>
<img src= "..\..\assets\images\Sync-Issues\5.png">
</p>

&nbsp;

!!! tip "Tip" 
    You can also instantly view the item involved in the issue by clicking the *SAP Cloud for Customer* or *Exchange* icon on the issue block

* All SSI Sync issues also [get logged in SSI Admin panel](../How-to-Configure-Admin/) for monitoring and resolution by the Key Users  

&nbsp;

&nbsp;

## How to resolve a synchronization issue

*   If the issue occurred because a required field was left empty, fill in the missing details in the [Save dialog](../Save-Dialog/)   
*   For cases when an issue cannot be resolved on your own or by local admin, it is recommended to contact our [technical support](https://support.sap.com/en/contact-us.html). Send a detailed description of the issue, including error codes and screenshots, so the support team can investigate the issue and help you without delay

&nbsp;

* * *

&nbsp;

### Renewing SAP Cloud for Customer or Mail data access credentials

If MS Exchange / Office 365 / Gmail access credentials expire or get changed, SSI can no longer synchronize user data. After that happens, affected end users or the Key Users managing them receive a notification e-mail with instructions how to re-activate SSI Sync Engine. In addition, a corresponding notification appears in the users' individual [SSI Dashboard](../Synchronization-Dashboard/).  

To renew e-mail data access for SSI Sync Engine, follow the steps provided in [this article](../Synchronization-Dashboard/). 

&nbsp;

&nbsp;
