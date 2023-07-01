# Handling of MS Exchange / Office 365 Contacts

[Cloud for Customer SSI Sync](../C4C-SSI-Sync-Overview/) can synchronize your MS Exchange / Office 365 contacts in SAP C4C as:

- SAP Accounts  

- SAP Contacts  

- SAP Individual Customers  

Contacts synchronization is a two-sided process, so your SAP C4C items will be continuously mirrored in your MS Exchange / Office 365, and vice versa, on Cloud for Customer SSI sync sessions.

Contacts are synchronized with SAP C4C via the dedicated folder or category in MS Exchange / Office 365.

!!! tip "Tip"
    If you you want to create a new synchronized Contact in MS Exchange / Office 365, you can just create it directly in a custom SAP contacts folder and it will be synced

&nbsp;

#### To synchronize a Contact via Dedicated folders

1\. Click on the Contact you want to sync with SAP C4C

2\. Drag-and-drop it to the corresponding folder in the leftmost pane, under **My Contacts**, so it will be synced as an Account, a Contact, or an Individual Customer

![](../assets/images/Sync-Contacts/folders.png)

&nbsp;

&nbsp;

#### To synchronize a Contact via Custom Categories

1\. Right-click on the Contact you want to sync with SAP C4C

2\. Select **Categorize > {SAP Cloud for Customer SSI, Account, or Individual Customer}**

*SAP Cloud for Customer SSI* category assigning results in the item's syncing as a SAP C4C Contact.

![](../assets/images/Sync-Contacts/category.png)

&nbsp;

On the following sync session the contact(s) marked this way will be automatically moved to the corresponding folder in the left pane and synchronized with SAP C4C.

!!! note "Note"
    Please disregard the custom categories *Error in SAP Cloud for Customer SSI* and *Visit*, these are used for syncing calendar items

&nbsp;

**Deleting a Contact in Exchange/Office 365**

If you remove an already synchronized Contact/Account/Individual Customer from the corresponding MS Outlook folder or delete it:

- if *Keep {SAP object type} Read Only* is disabled for this object type in [Profile Sync settings](../Customization-Settings-Sync/#iv_adjust_synchronization_patterns_applied_for_saved_objects_and_activities) – the object gets deleted from SAP C4C as well, on the following sync session
- if *Keep {SAP object type} Read Only* is enabled for this object type in [Profile Sync Settings](../Customization-Settings-Sync/#iv_adjust_synchronization_patterns_applied_for_saved_objects_and_activities) – the object gets automatically re-created in the corresponding MS Outlook folder on the following sync session, retrieved from SAP C4C. Please note that if you sync a contact with this feature enabled, this contact will be removed from your MS Exchange / Office 365 account.

 &nbsp;

**Adding a Contact in SAP C4C**

When a new Contact is added in SAP C4C and it is visible within the set view (see above), it appears in the **SAP C4C Contacts** folder in Outlook after the next synchronization.  

&nbsp;

**Modifying a Contact in SAP C4C**

When an existing Contact is modified in SAP C4C and it belongs to the set list view (see above), the corresponding contact in the *SAP C4C Contacts* folder in MS Exchange / Office 365 gets updated, on the following sync session.

&nbsp;

**Deleting a Contact in SAP C4C**

When a synced Contact is deleted in SAP C4C, the corresponding contact in the *SAP C4C Contacts* folder in MS Exchange / Office 365 gets deleted as well, on the following sync session.

&nbsp;

#### Special Patterns Applied on Contacts Processing

When a Contact is created and synchronized from MS Outlook to  SAP C4C, the following pattern is applied in order to find a relevant  Account to link this Contact to:

*1\.* The value of the Contact’s *Company* field is used to search for relevant Account(s) in SAP C4C.

*2\.* If an Account with exact *Company* field matching is found – the Account is used for Contact linking. In case there are several Accounts found, one with the earliest creation date is used.

*3\.* If there is no direct match, the *Company* field’s value is searched for among sub-strings of Account names in SAP C4C, and if there is only one matching Account found, it is used to link the Contact to. If no relevant Account is found this way, see point 4.

*4\.* If no matches with the *Company* field’s value are found among Account names in SAP C4C, a Contact with empty Account association is attempted to be created in SAP C4C.