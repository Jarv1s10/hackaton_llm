# Cloud for Customer SSI Add-In Settings

!!! note "Note"
    End users' permissions to modify Cloud for Customer SSI settings are defined in your Org settings. Several Add-In settings can only be modified by [Key Users](https://www.sap.com/documents/2018/10/febc12f6-227d-0010-87a3-c30de2ffd8ff.html)

&nbsp;

Cloud for Customer SSI is a highly customizable tool; it is designed to meet the needs of different categories of users following different workflows. Profile Settings management is an advanced Cloud for Customer SSI feature that enables the end users to manage and fine-tune Cloud for Customer SSI Add-In's behavior: what objects and activities will be handled by the Add-In and how specific fields will be processed. Also refer to [this article](../Customization-Settings-Sync/) for information on Cloud for Customer SSI Synchronization Settings.

!!! note "Note"
    After making any adjustments in the settings, make sure to click the **Save** button in the upper right corner of the tab to save and apply them

&nbsp;

A [Key User](https://www.sap.com/documents/2018/10/febc12f6-227d-0010-87a3-c30de2ffd8ff.html) can adjust profile settings for any user in an Org or modify a Profile template used by group of users via the "Groupware settings" tab. Ordinary users can use their "Add-In Settings" tab to adjust some aspects of their individual configurations.

Profile templates managed by the Key users are essentially sets of function adjustments specific to groups of users with different roles in the CRM; the Templates contain more settings than individual Profiles.



<details><summary> >>> Click to see screenshots <<< </summary>
<p><img src="..\..\assets\images\Profiles\prof-templ-addin-1.png">
<br>
<br>
<img src="..\..\assets\images\Profiles\prof-templ-addin-23.png">
<br>
<br>
<img src="..\..\assets\images\Profiles\prof-templ-addin-4.png">
</p></details>

&nbsp;



The following fine tuning controls are available in [Cloud for Customer SSI Profile settings](../How-to-Open-Your-C4C-SSI-Settings-Profile/) > **Add-In Settings** tab



!!! note "Note"
    Via the *Groupware settings* pane, [SAP C4C Key Users](https://www.sap.com/documents/2018/10/febc12f6-227d-0010-87a3-c30de2ffd8ff.html) can modify Profile settings for any user in their organization, or configure Profile templates applied for pre-set groups of users.  
    Individual users' Cloud for Customer SSI settings can be adjusted by the regular users via the pane *User settings*; the Key users can access and re-adjust these settings as well

&nbsp;

**I.** **Select which object types should be handled and displayed by Cloud for Customer SSI Add-In**
Toggle the checkbox to enable or disable object and activity types processing by Cloud for Customer SSI

![](../assets/images/Profiles/enable_objects.png)

&nbsp;

**II.** **Define which record fields will be displayed, edited, and searched via the Add-In**

!!! note "Note"
    The field settings described below are available for every enabled object or activity type

**1\.** What fields should be listed in record cards' Basic View (not expanded card) for users' reference  

![](../assets/images/Profiles/basic_view.png)

The number of displayed fields is limited to four. Click on picklists and select fields you want to be displayed on Basic card view.

&nbsp;

**2\.** What fields will be available in record cards' Detailed View (fully expanded record card) for users' reference and editing.  

![](../assets/images/Profiles/detailed_view.png)

&nbsp;

To add a field, click **✚ Add Field to Detailed View** at the top of an object's Detailed View tab and select a field from the picklist. To remove a field, click the **x** icon next to it.

![](../assets/images/Profiles/add-remove.png)

&nbsp;

Note that some fields are impossible to remove, so  the **x** icon is grayed out for them.  

&nbsp;

Additionally, in this tab you can rearrange the order in which fields will be listed in the card, by drag-and-dropping them.


![](../assets/images/Profiles/field_order.png)&nbsp;

&nbsp;

Additionally, in this tab you can manage several attributes for each field displayed in Detailed card view:

 ![](../assets/images/Profiles/field_settings.png)

&nbsp;

- **Read Only**: whether a field's value can be modified  
- **Required**: whether a field is mandatory to fill  
- **Display on Create**: whether a field should be included in the object creation dialog  
- **Display on Record**: whether a field should be included in the "Save in SAP C4C" dialog  



&nbsp;

The **Settings** tab contains fields and checkboxes that define nuances of user interactions with objects performed via the Add-In: search, creation, and editing.

![](../assets/images/Profiles/settings_.png)


- **Sort By**: Set what field should be used for sorting records of a specific type  
- **Search By**: Specify what fields' values should be browsed on user-initiated search  
- **Allow Create**: Define whether the users should be allowed to create objects of this type  
- **Allow Update**: Define whether the users should be allowed to modify objects of this type  

&nbsp;

&nbsp;
