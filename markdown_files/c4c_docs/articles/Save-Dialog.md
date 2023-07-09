# The Save E-mail / Save Event Dialog  

&nbsp;

**[The article is  work-in-progress]**  

&nbsp;


!!! tip "Tip"
    If you prefer to save your business communication and meetings in Cloud for Customer automatically or semi-automatically, make use of the [flexible auto-saving options](../Emails-Processing/#3_automatic_saving_with_auto-save) included in SSI

&nbsp;

The Save dialog appears when you select an e-mail or calendar item in MS Outlook Desktop / On the Web / Gmail Inbox or Sent folder and click the Save button in [SSI Sidebar](../Introduction/) in order to get the item saved in SAP Cloud for Customer. Refer to the articles on [saving e-mails](../Emails-Processing/) and [syncing calendar items](../Events-Processing/) for more details.

If the [Save button](../Save-e-mail-dialog/) is used, MS Exchange / Office 365 e-mails are saved directly by [SSI Add-In](../Add-In-vs-Sync/) in [Read mode](../Emails-Processing/#read_mode_and_compose_mode_in_ms_exchange_office_365) or by [SSI sync engine](../C4C-SSI-Sync-Overview/) in [Compose mode](../Emails-Processing/#read_mode_and_compose_mode_in_ms_exchange_office_365). In the latter case e-mails are saved in SAP Cloud for Customer on the following scheduled sync session (within 1 - 30 minutes).

&nbsp;

&nbsp;



- [Open Cloud for Customer SSI Sidebar](../How-to-Open-C4C-SSI-Sidebar/)  
- Select/create an e-mail or open a meeting/appointment in MS Outlook  
- In Cloud for Customer SSI Sidebar, click **Save this E-Mail** (or **Save this Event**) at the bottom of a relevant SAP Cloud for Customer object  
- (optionally) modify the item's Subject on saving, if you want to name the matching SAP Cloud for Customer e-mail object differently  
- Click **Add**  


![](../assets/images/Article1/save-email-dialog.png)

&nbsp;

&nbsp;

### The save e-mail dialog

Via this dialog you can:

- search in Cloud for Customer and select SAP Cloud for Customer records you want to link to the matching activity in  
- set the resulting SAP Cloud for Customer e-mail's parameters and modify its Subject, if necessary  
- mark the attached file(s) you want to [save in SAP Cloud for Customer](../Attachments-Handling/) along with the e-mail, if any; modify the files' names, if necessary  
- define if you want to auto-save in SAP Cloud for Customer future e-mails in the same correspondence thread (the *Auto-save new e-mails within this thread*  checkbox at the bottom). See [this article](../Customization-Settings-Sync/) for more information.

&nbsp;

<!-- image is absent
![](../assets/images/Using-C4C-SSI/How-To-s/Emails-Processing/new_save_email_dialog.png)
-->

&nbsp;

To proceed with saving, you need to select records to be linked to the saved e-mail in SAP Cloud for Customer under **Linked records**  – unless the relevant objects have already been retrieved and added by [SSI initial search](../initial-search-and-applied-filters/). Use the *Search SAP Cloud for Customer records* field to find these objects in SAP Cloud for Customer and select them; to remove an object from the list, clear the checkbox on the right-hand side. 

Note that this field is now unified, used for both these object classes. To ensure proper linking according to your [SSI settings](../Customization-Settings-Addin/) and SAP Cloud for Customer configuration, the dialog indicates it if there are conflicts in linking of selected objects.  

<!-- Need to be investigated and updated
See [this article](../Activities-Linking/) to learn more about linking rules.

You can also select or deselect all auto-retrieved related records using a corresponding checkbox above

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Using-C4C-SSI\How-To-s\Working-with-Activities\select-all.png">
</p></details>
-->

&nbsp;

&nbsp;

After related records to be linked have been selected, you may proceed to handling files attached to the e-mail. In the  **Attachments **section, you can select attachments to be saved in SAP Cloud for Customer along with the e-mail. Note that you can also change the files' names on saving, by clicking the **🖉** (Edit) icon next to their names.

In the list you will also see an extra *.eml* file, it is an exact copy of the e-mail that you can save along with the attachments. Refer to [this article](../Attachments-Handling/) for more information. 

!!! note "Note"
    An e-mail attachment cannot be saved in SAP Cloud for Customer in the following cases:  
    **1.** if it exceeds the file size limit in SAP Cloud for Customer – 25 Mb per file  
    **2.** if the file's extension was not allow-listed in the settings

&nbsp;


&nbsp;

In addition, if [*Automatic Saving of E-Mail Threads*](../Customization-Settings-Sync/#ii_e-mails_sync_options) is enabled in your [SSI Sync settings](../Customization-Settings-Sync/), you can select the **Auto-save new e-mails within this thread** checkbox at the bottom of the dialog to get all future e-mails from/to this correspondent saved in SAP Cloud for Customer automatically, without your involvement.

After populating all necessary fields, click the **Save** button in the bottom right corner of the dialog to save the e-mail in SAP Cloud for Customer.

When the e-mail is successfully saved in SAP Cloud for Customer, a success toast notification pops up.

<!--
![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b72c7690428631d7a89f398.png)  
-->

&nbsp;  

<!--
![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b72d49d0428631d7a89f415.png)  
-->

If [SSI synchronization](../C4C-SSI-Sync-Overview/) is active, the user-side differences between saving messages in Read mode and Compose mode is the kind of notification you will get (see the screenshots above) and the fact that messages opened in Compose mode will be saved in SAP Cloud for Customer on the following sync session (within 1-30 minutes), unlike messages opened in Read mode, which are saved immediately.

The SAP Cloud for Customer object created when saving an e-mail is logged in SSI **Past activities** under the tab **Activity Timeline** and can be opened in SAP Cloud for Customer directly by clicking the blue **Expand** icon next to it.  

<!--
![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b72c8ae2c7d3a03f89dabdc.png)  
-->
&nbsp;

* * *

&nbsp;

### The save event dialog

The *Save this event to SAP Cloud for Customer* dialog appears when you open a sent calendar item in MS Outlook (or Gmail) calendar and click the *Save* button in [SSI Sidebar](../Introduction/). It is used to initiate [the item's synchronization](../Events-Processing/) in SAP Cloud for Customer, linked to relevant records.
&nbsp;

!!! warning "Important"
    Note that calendar items can only be synced with SAP Cloud for Customer after they are sent

&nbsp;

To proceed with saving, you need to select records to be linked to the synced calendar item in SAP Cloud for Customer under **Linked records**, unless the relevant records have already been retrieved and added by [SSI initial search](../initial-search-and-applied-filters/). Use the *Search SAP Cloud for Customer records* field to find these records and select them; to remove an object from the list, click the **x** icon on the right-hand side. 



&#160;
 &#160;
