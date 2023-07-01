# Cloud for Customer SSI Synchronization Settings

&nbsp;

!!! note "Note"
    End users' permissions to adjust Cloud for Customer SSI Sync settings are defined in your Org's settings; typically, Sync settings can only be modified by SAP C4C [Key users](https://www.sap.com/documents/2018/10/febc12f6-227d-0010-87a3-c30de2ffd8ff.html)

&nbsp;

Cloud for Customer Server-Side Integration consists of two components, [SSI Outlook Add-In](../Introduction/) / [Chrome Extension for Gmail](../Use-with-Gmail/) and [SSI Sync Engine](../C4C-SSI-Sync-Overview/); both components' specific behavior [can be adjusted](../How-to-Open-Your-C4C-SSI-Settings-Profile/) to match specific workflows peculiar to your business processes.

This article explains Profile settings related to [SSI Sync engine](../C4C-SSI-Sync-Overview/). Also see [this article](../Customization-Settings-Addin/) for information on Cloud for Customer SSI Add-In Settings.

!!! warning "Important"
    After making any adjustments in the settings, make sure to click the **Save** button in the upper right corner of the tab to save/apply them.  
    Note the difference between **A.** saving an updated user settings config (which is applied instantly) and **B.** saving an updated Profile template (can only be modified by [Key users](https://www.sap.com/documents/2016/08/fc8ff4f2-827c-0010-82c7-eda71af511fa.html)). If changes are made in a Profile template, the users get these changes only after the template gets applied for them, individually or in bulk



&nbsp;

!!! note "Note"
    Via the *E-Mail Integration* > *Groupware settings* pane in SAP Cloud for Customer interface, [SAP C4C Key Users](https://www.sap.com/documents/2018/10/febc12f6-227d-0010-87a3-c30de2ffd8ff.html) can [modify Profile settings](../How-to-Open-Your-C4C-SSI-Settings-Profile/) for any user in the organization, or adjust pre-set Profile templates applied for groups of users.  
    Individual SSI settings can be changed by regular users via the pane *E-Mail Integration* > *User settings*; Key users can also adjust other these individual settings, if needed

&nbsp;

The following [Sync engine](../C4C-SSI-Sync-Overview/) fine-tuning controls are available in [Cloud for Customer SSI Profile settings](../How-to-Open-Your-C4C-SSI-Settings-Profile/) > **Sync Settings**:

<details><summary> >>> Click to see screenshots <<< </summary>
<p><img src="..\..\assets\images\Profiles\prof-templ-sync-1.png">
<br>
<img src="..\..\assets\images\Profiles\prof-templ-sync-2.png">
</p></details>

&nbsp;

### **I.** General Sync Settings

![](../assets/images/Profiles/Sync_settings/general.png)

&nbsp;

**1\.** **Remind About Appointments and Visits in**: enable MS Outlook/Gmail Calendar reminders to be added for Appointments/Visits downsynced from SAP C4C as MS Outlook/Gmail calendar items; set reminders triggering interval prior to synced items' occurrence

**2\.** **Remind About Tasks at**: enable MS Outlook/Gmail Calendar reminders to be added for Tasks downsynced from SAP C4C; set task reminders triggering time

**3\.** Attachments handling:

&nbsp;&nbsp;&nbsp;&nbsp;**3\.1.** **Allowed File Extensions for Attachments**: define what file types can be synced in SAP C4C as e-mail/meeting attachments

&nbsp;&nbsp;&nbsp;&nbsp;**3\.2.** **Prohibited File Extensions for Attachments**: define what file types should never be synced in SAP C4C as e-mail/meeting attachments

&nbsp;&nbsp;&nbsp;&nbsp;**3\.3.** **Allowed Attachment Size**: [predefined, cannot be changed] set minimum and maximum file size to be allowed for syncing in SAP C4C, to filter out unneeded attachments like small images from e-mail signatures and save storage space in your SAP C4C org

**4\.** **Default Country** picklist: set the default country of an Account's location used when an Account is auto-created by Cloud for Customer SSI synchronization, for an auto-created new Contact. This "fallback" value is used if Country is a required field for SAP Contacts and an end user specifies an address but leaves the Country field empty, or if a Contact's actual Country cannot be retrieved in SAP.
This value is also useful when your Contacts' companies have multiple offices in different world countries but use the same e-mail domain. 

&nbsp;

### **II.** E-Mails Sync Options

![](../assets/images/Profiles/Sync_settings/email.png)

&nbsp;

**1.** **Enable auto-sharing for e-mail**: all new incoming and outgoing e-mails from/to addresses registered as Contacts or Individual Customers in SAP C4C, except blocklisted or internal addresses/domains, will be auto-saved in SAP C4C.

**2.** **Blocklisted Domains**: list e-mail addresses/domains to be excluded from being auto-saved in SAP C4C, e.g. personal correspondence or internal (in-org correspondence). The e-mail address domain used by the current user is prefilled into this field, unless it's a general use domain.

&nbsp;

&nbsp;

### **III.** Calendar Sync Options

![](../assets/images/Profiles/Sync_settings/event.png)

&nbsp;

**1\.** **Sync private meetings and appointments**: select to enable reserving of time slots in SAP C4C calendar for parsed users' MS Exchange / Office 365 [private](https://support.office.com/en-us/article/make-an-appointment-or-meeting-private-dc3898f0-22f5-45c6-8cc8-b4d4db84111d) meetings and appointments on calendar items auto-syncing. Such meetings/appointments will be added to SAP C4C as placeholder events, revealing no details about them (not even their subjects). If disabled, private meetings and appointments won't be reflected in SAP C4C calendar at all. 

**2\.** **Auto sync meetings**: select to enable automatic MS Exchange / Office 365 meetings synchronization with SAP C4C.

**3\.** **Sync even if there are no linked contacts or individual customers**: this setting manages auto-syncing of meetings whose attendees are not yet registered in SAP C4C (unresolved attendees). If enabled, such meetings will be auto-synchronized, linked to Leads auto-created by Cloud for Customer SSI for the unresolved addresses.

**4\.** **Auto sync appointments**: select to enable automatic MS Exchange / Office 365 appointments synchronization with SAP C4C.

**5\.** **Include private meetings or appointments**: select to enable [private](https://support.office.com/en-us/article/make-an-appointment-or-meeting-private-dc3898f0-22f5-45c6-8cc8-b4d4db84111d) meetings and appointments auto-syncing by Cloud for Customer SSI. Note: if this setting is enabled and setting ( **1** ) is disabled, a sync issue will be logged, since enabling setting ( **1** ) is a prerequisite for ( **4** ).

&nbsp;

&nbsp;

### **IV.** Adjust synchronization patterns applied for saved objects and activities

!!! note "Note"
    Some of these settings are overriden by Key users-configured profile settings and thus cannot be adjusted by regular users

You can adjust synchronization patterns applied for the following objects and activities:

*Contact, Individual Customer, Account, E-Mail, Appointment, Visit, Opportunity, Task*

&nbsp;

#### 1\. **Contact**

![](..\assets\images\Profiles\Sync_settings\contact_settings.png)

&nbsp;

##### ***Contact Settings tab***

**Synchronization filter**: apply a pre-set SAP Cloud for Customer Contacts filter or a user-defined filter, so Cloud for Customer SSI Sync will only handle Contacts satisfying criteria specified in the filter.

**Keep SAP Contacts Read-Only**: allow or disallow modifying Contacts stored in SAP Cloud for Customer via Cloud for Customer SSI Sync.

**Synchronize Home Phone and Address**: enable or disable synchronizing of the fields Home Phone and Address via Cloud for Customer SSI Sync.  

##### ***Contact Smart Description tab***

See the explanation below.  

&nbsp;

#### 2\. **Individual Customer**  

![](..\assets\images\Profiles\Sync_settings\indcustomer_settings.png)

&nbsp;

##### ***Individual Customer Settings tab***

**Synchronization filter**: apply a pre-set SAP C4C Individual Customers filter so Cloud for Customer SSI Sync will only handle Individual Customers satisfying criteria specified in the filter.

**Synchronize Individual Customers**: enable or disable Individual Customers synchronization via Cloud for Customer SSI.  

**Keep Individual Customers Read-Only**: allow or disallow modifying Individual Customers stored in SAP Cloud for Customer via Cloud for Customer SSI Sync.

##### ***Individual Customer Smart Description tab***

See the description below.

&nbsp;

#### 3\. **Account**

![](..\assets\images\Profiles\Sync_settings\account_settings.png)

&nbsp;

##### ***Account Settings tab***

**Synchronization filter**: apply a pre-set SAP C4C Individual Customers filter so Cloud for Customer SSI Sync will only handle Accounts satisfying criteria specified in the filter.  

**Keep Accounts Read-Only**: allow or disallow modifying Individual Customers stored in SAP C4C via Cloud for Customer SSI Sync.  

##### ***Account Smart Description tab***

See the explanation below.

&nbsp;

#### 4\. **E-Mail**

![](..\assets\images\Profiles\Sync_settings\email_settings.png)

&nbsp;

##### ***E-Mail Settings tab***

**Synchronize E-Mail Messages**: enable or disable e-mail messages synchronization via Cloud for Customer SSI.  

**Synchronize E-Mail Attachments**: enable or disable e-mail attachments synchronization via Cloud for Customer SSI.  

&nbsp;

#### 5\. **Appointment**

![](..\assets\images\Profiles\Sync_settings\appointment_settings.png)

&nbsp;

##### ***Appointment Settings tab***  

**Synchronize Appointment Attachments**: enable or disable Appointment attachments synchronization via Cloud for Customer SSI.  

&nbsp;

#### 6\. **Visit**

![](..\assets\images\Profiles\Sync_settings\visit_settings.png)

&nbsp;

##### ***Visit Settings tab***  

**Synchronize Visit Attachments**: enable or disable Visit attachments synchronization via Cloud for Customer SSI.  

&nbsp;

#### 7\. **Task**

![](..\assets\images\Profiles\Sync_settings\task_settings.png)

&nbsp;

##### ***Task Settings tab***

**Synchronize Tasks**: enable or disable Tasks synchronization via Cloud for Customer SSI.   

**Keep Tasks Read-Only**: allow or disallow modifying Tasks stored in SAP Cloud for Customer via Cloud for Customer SSI Sync.

**Synchronize Task Attachments**: enable or disable Task attachments synchronization via Cloud for Customer SSI.

&nbsp;

* * *

&nbsp;

#### The Smart Description tab

This tab is used to set up and manage the Smart description feature available for various object types handled by SSI.

Cloud for Customer SSI can fetch the content of any target field of a SAP C4C object, including [custom ones](https://blogs.sap.com/2016/06/17/points-to-be-noted-before-using-custom-object-builder/), and automatically insert it into a chosen text field of a Visit, Appointment, Contact, or Task item in MS Exchange / Office 365, for example  the *Description* field. This mechanism makes retrieval of needed data from standard as well as custom added fields convenient and flexible, thus unlocking implementation of various custom solutions for smart target SAP C4C data displaying or appending to items’ fields shown in MS Outlook Desktop / On the Web or Gmail.

!!! note "Note"
    Smart description fields values retrieval works only one-way, from SAP C4C to MS Exchange / Office 365 or Gmail, thus any changes you may  make in a text field containing smart description data in your e-mail  client will **not** be up-synced to SAP C4C and instead will be overwritten on the following sync session, replaced by the field’s content fetched from SAP C4C afresh

&nbsp;

An example of the Smart Description feature application is automatic appending a Contact’s *phone number*, *position*, *organization’s address*, or any details contained in a Contact’s non-standard fields, to the Description of a Meeting scheduled with this Contact, to make it more informative and thus faster to process. 

The following delimiter is used to separate appended smart description data from the field’s original content: *++++++++++++++++++++++++++++++++++*

&nbsp;

!!! warning "Important"
    Note that when some informative Smart description details are appended to an external meeting's Description, they will also be seen by the meeting’s attendees, including the external ones, e.g. the customers, so please be considerate about what sensitive information can be included in an item's Smart description

&nbsp;

Similarly, a Task’s or Contact’s fields filling in MS Outlook Desktop / On the Web or Gmail can be enhanced by automatic addition of extra details contained in a relevant objects’ custom fields, while their Notes field can be used by SSI sync for target SAP Cloud for Customer data displaying according to end users’ preferences, in addition to what is displayed in the [Add-In's Sidebar](../Introduction/).  

&nbsp;

&nbsp;

