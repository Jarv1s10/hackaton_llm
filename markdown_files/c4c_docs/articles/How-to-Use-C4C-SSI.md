# How to Use SAP Cloud for Customer SSI

&nbsp;

<span style="color: #e74125;font-size: 17px;font-weight: 700;line-height: 30px;padding: 0px 10px;outline: none;border-radius: 2px;text-decoration: none;background-color: #fff;display: inline-block;border: 0px solid #000;transition: .3s all;width: auto;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="display: inline-block;vertical-align: middle;height: 32px;object-fit: contain;"></span><span style="color: #e74125;font-size: 17px;font-weight: 700;line-height: 30px;padding: 0px 10px;outline: none;border-radius: 2px;text-decoration: none;background-color: #fff;display: inline-block;border: 0px solid #000;transition: .3s all;width: auto;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="display: inline-block;vertical-align: middle;height: 32px;object-fit: contain;"></span><span style="color: #e74125;font-size: 17px;font-weight: 700;line-height: 30px;padding: 0px 10px;outline: none;border-radius: 0px;text-decoration: none;background-color: #fff;display: inline-block;border: 0px solid #000;transition: .3s all;width: auto;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="display: inline-block;vertical-align: middle;height: 32px;object-fit: contain;"></span> 

&nbsp;

!!! tip "Tip"
    Also refer to [this article](../Emails-Processing/) to learn how to save e-mails via SAP Cloud for Customer SSI and to [this article](../Contacts-Handling/) to learn how to synchronize your contacts

&nbsp;

SAP Cloud for Customer SSI is a cloud solution deployed on customers' e-mail accounts. Its high cross-platform compatibility ensures seamless work with MS Exchange, Office 365, or Gmail accounts. The [local system admin manages the Sync and Add-In](../How-to-Configure-Admin/) components of the solution and can enable both of them for any account.

After a local [Key user](https://www.sap.com/documents/2018/10/febc12f6-227d-0010-87a3-c30de2ffd8ff.html) has [fully mass-deployed](../How-to-Configure-Admin/) the solution for all eligible users:

* [SSI Sync](../C4C-SSI-Sync-Overview/) starts running in the background every 30 minutes 24/7 between the users' Exchange/Office 365 or Gmail account and SAP Cloud for Customer server
* SSI Add-In is added to the users' e-mail account opened in MS Outlook for Windows/Mac/iOS/Android, [Outlook.com](https://outlook.live.com/owa/), or [Office 365](https://outlook.office.com/mail/)
* SSI dedicated Google Chrome Extension is used to run the solution in Gmail boxes and is mostly identical to MS Outlook Add-In in terms of functions

&nbsp;

The first step to start working with SAP Cloud for Customer SSI Add-In is to [open the Sidebar](../How-to-Open-C4C-SSI-Sidebar/) in your MS Outlook Desktop, Outlook on the Web, or the Google Chrome Extension in Gmail.

!!! note "Note"
    SSI requires a constant Internet connection to perform the Add-In’s functions or initiate the Sync Engine’s functions. If no connection is available on a workstation, the Add-In stops working and only initiated earlier or automated Sync engine functions are carried out

&nbsp;

* * *  

&nbsp;

SSI Add-In Sidebar is your direct window to SAP Cloud for Customer. There is a number of actions you can instantly perform through it:

&nbsp;

#### **1\.** Work with SAP Cloud for Customer record cards in the Sidebar

After you select (or compose) an e-mail or meeting in MS Outlook or Gmail, the Sidebar displays SAP Cloud for Customer records related to all registered recipients/senders/attendees engaged in this e-mail or meeting. See [this article](../initial-search-and-applied-filters/) for more information.

Related Contacts and Individual Customers can be viewed in the Sidebar as detailed cards.

Record cards are expanded by default but can be minimized by clicking on their headers and "putting them aside" to free space on the Sidebar's home screen. Minimized cards display only 4 key record fields sufficient for their identification.

In addition, if you refer to a specific record card frequently, you can "pin" it to the top of the Sidebar, by clicking the <img src="../../assets/images/Icons/pin.png" style="display: inline-block;vertical-align: middle;width: 18px;margin-left: 1px;height: 14px;object-fit: contain;"> (Pin) icon in the record's header. To unpin the card, click on the icon again.

![](../assets/images/Start/pin_card.png)

&nbsp;

&nbsp;

#### **2\.** Create a new entry suggestion

If the e-mail address used in a selected e-mail/meeting has not been saved to SAP Cloud for Customer yet, you will see a suggestion to create a SAP Cloud for Customer Contact or Lead based on it.

![](../assets/images/Start/unresolved.png)

&nbsp;

&nbsp;

#### **3\.** Cards' detailed view for instant reference

To open a record's detailed card view, you need to click the **ⅰ Details** button at the bottom of its card.

![](../assets/images/Article1/details.png)

&nbsp;

In the detailed card view, you can easily correct and update the record's fields by clicking the <img src="../../assets/images/Icons/edit.png" style="display: inline-block;vertical-align: middle;width: 18px;margin-left: 1px;height: 14px;object-fit: contain;">&nbsp;(Edit) icon next to the fields.

![](../assets/images/Start/editfields.png)

&nbsp;

Additionally, you can quickly check what SAP Cloud for Customer Activities and Objects ("related records") are associated with a record displayed in the Sidebar. To do that, expand the corresponding category tabs displayed in the record's expanded card. You can also open these records' detailed cards for reference or editing.

![](../assets/images/Article1/related_records.png)

&nbsp;

&nbsp;

#### **4\.** Using the Save button

After a relevant Lead or Contact has been created (or found using [SSI search](../Search-Records/)), you can save an e-mail or a meeting/appointment in SAP Cloud for Customer linked to it. To do that:

- [Open SAP Cloud for Customer SSI Sidebar](../How-to-Open-C4C-SSI-Sidebar/)  
- Select/create an e-mail or open a meeting/appointment in MS Outlook  
- In SSI Sidebar, click **Save this e-mail** (or **Save this Event**) at the bottom of a relevant SAP Cloud for Customer object  
- (Optionally) modify the object's Subject on saving, if you want to name the matching SAP Cloud for Customer e-mail object differently
- Click **Add** to save the e-mail or event  

![](../assets/images/Article1/save-email-dialog.png)

&nbsp;

&nbsp;

#### **5\.** Save files attached to e-mails in SAP Cloud for Customer

In the same *"Save an E-Mail to SAP Cloud for Customer"* dialog, you can select files attached to the e-mail which you want to save in SAP Cloud for Customer along with it.

![](../assets/images/Article1/save-email-attachment.png)

&nbsp;

Additionally, there is the **Attach** button on business records' cards, which can be used to attach files directly to business records.  

![](../assets/images/Start/attach_button.png)

&nbsp;

&nbsp;

#### **6\.** Find your contact on Facebook or LinkedIn, or open it in SAP Cloud for Customer

With SAP Cloud for Customer SSI, you can quickly find your contact's pages on social networks or open its record directly in SAP Cloud for Customer. To do that, use the corresponding controls in the upper right corner of every business object card.

![](../assets/images/Start/fb-li-c4c.png)

&nbsp;

&nbsp;