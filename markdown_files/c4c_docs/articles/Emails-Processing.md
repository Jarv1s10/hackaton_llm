# How E-Mails Are Processed by SSI

There are three ways to get an e-mail saved from your MS Outlook Desktop / On the Web or Gmail mailbox to SAP C4C:  

**1\.** Manual (selective) saving via SAP C4C Add-In  

**2\.** Semi-automatic saving via dedicated folder  

**3\.** Automatic items saving with auto-save  

All these ways to save an e-mail are described in this article.

&nbsp;
&nbsp;

### 1. User-defined ("selective" or "manual") saving

You can save an e-mail or calendar item linked to an existing or [new created](../Create-Records/) Cloud for Customer object. To do that:

- [Open Cloud for Customer SSI Sidebar](../How-to-Open-C4C-SSI-Sidebar/)  

- Select/create an e-mail or open a meeting/appointment in MS Outlook, Outlook.office.com, or the SSI Chrome Extension for Gmail

- In Cloud for Customer SSI Sidebar, click **Save this E-Mail** at the bottom of the relevant object's expanded card.

- (optionally) modify the item's Subject on saving, if you want to name the matching SAP C4C record differently.

!!! tip "Tip"
    In addition, there is an optional possibility to edit a saved e-mail's Body before it's conveyed to SAP C4C

- Click **Add** 

![](../assets/images/Article1/save-email-dialog.png)

&nbsp;

#### Read mode and Compose mode in MS Exchange / Office 365

- If the message is opened in **Read mode**, that is selected in the *Inbox* or *Sent* folder, or the custom added *SAP e-mails* folder (e-mails from any other folders are **not** processed by SSI), it will be saved in SAP Cloud for Customer directly, following the regular pattern.
- If the message is opened in **Compose mode** (that is, it is a new message created by clicking **New e-mail**, **Reply**, or **Forward** in MS Outlook/Office 365/Gmail), saving it in SAP C4C is not possible until you enable synchronization, or, as a workaround, you could save  the message and move it to the **Sent** MS Outlook folder and then open it in Read mode and save it.  
  Note that in SSI Chrome Extension for Gmail e-mails saved in Compose mode are handled in the same manner as in Read mode, the save date/time set according to the date/time when the Extension's Sidebar was opened to save the e-mail.

&nbsp;

&nbsp;

* * *

#### Saving files attached to e-mails in SAP C4C

In the same *"Save an E-Mail to SAP C4C"* dialog, you can mark files attached to the e-mail which you want to save in SAP C4C along with it:

![](../assets/images/Article1/save-email-attachment.png)

&nbsp;

&nbsp;

* * *

### 2\. Semi-automatic saving via dedicated folder

To quickly save an e-mail in SAP C4C by [Synchronization](../C4C-SSI-Sync-Overview/), you can make use of either of the following methods:

- Drag-and-drop the e-mail to the dedicated *SAP E-Mails* MS Outlook folder

![](../assets/images/Start/dedicated_folder.png)

&nbsp;

or

- Right-click on the e-mail item and assign it the custom *SAP Cloud for Customer SSI* category

![](../assets/images/Start/custom_category.png)

&nbsp;

!!! note "Note"
    E-mails saved this way will be created in SAP Cloud for Customer on the following sync session, that is within 1-30 minutes after saving. E-mails will be auto-linked to a single relevant Contact or Individual Customer. See the point (**3**) below to learn how linking is performed

&nbsp;

&nbsp;

* * *

### 3\. Automatic saving with Auto-save

If the corresponding [Sync setting](../Customization-Settings-Sync/#ii_e-mails_sync_options) is enabled, all new incoming/outgoing e-mails from/to addresses already registered in SAP C4C will be saved in SAP C4C automatically, auto-linked to a single relevant Contact, Account, or Individual Customer. The following pattern is applied on retrieval of related object(s) to be linked:

- The sender's and recipients' addresses are retrieved from the *To*, *CC*, and *From* fields of the e-mail
- The addresses are matched with Contact and Individual Customer records available in your SAP Cloud for Customers  
- The saved e-mail gets linked to the first matching record found (a single one)
- If no matching records are found for some e-mail addresses, the are still registered in the saved unlinked e-mail object's *Recipients* field

&nbsp;

#### E-mail categories which do **not** get auto-saved when Auto-saving is enabled:

**A\.** In-org e-mails. In addition, if opened for such e-mails the Sidebar displays a notification *"Nothing to save in SAP Cloud for Customer"*  

<details><summary>>>> Click to see a screenshot <<<</summary>
<p>
    <img src="..\..\assets\images\Initial_Search\internal-notification.png">
</p>
</details>


**B\.** E-mails from/to addresses or domains [blocklisted from syncing](../blocklist/) on the Org level or individual level. In addition, if opened for such e-mails the Sidebar displays a notification *"Nothing to save in SAP Cloud for Customer"*  

**C\.** E-mails placed into any other folders of your e-mail client but *Inbox*, *Sent*, or the custom *SAP E&#8209;Mails* one  

**D\.** Service e-mails (see below)  





&nbsp;

* * *

&nbsp;

### The Add-In / Chrome Extension does not work with Service e-mails

Service e-mail messages cannot be saved in Cloud for Customer or processed in any way, so the Add-In / Chrome Extension cannot be opened for the following kinds of e-mails:

*   [MS Outlook message read receipts](http://support.office.com/en-us/article/add-and-request-read-receipts-and-delivery-notifications-a34bf70a-4c2c-4461-b2a1-12e4a7a92141)  
*   MS Outlook calendar item acceptance / declining / update notifications  
*   MS Outlook delivery failure notifications  

When an e-mail of this kind is selected in MS Outlook Desktop or On the Web, the button **View Context of SAP Cloud for Customer** becomes disabled and the Sidebar cannot be opened.

