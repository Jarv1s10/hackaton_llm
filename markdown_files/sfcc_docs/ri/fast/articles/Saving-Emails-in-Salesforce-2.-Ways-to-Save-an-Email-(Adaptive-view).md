---
description: Detailed overview of the ways to save an email in Salesforce
---
# Ways to Save an Email in Salesforce  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*10 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! tip "Tip"
    Refer to the [first part](../Saving-Emails-in-Salesforce-1.-Function-Overview/) of this article for an overview of {{ product_name }}'s save email function that explains the internal mechanisms involved.  
    Also refer to [this article](../Object-Fields-Mapping-Patterns/#ms_outlook_emails) for detailed information on how fields are matched between MS Exchange / Office 365 and Salesforce objects

&nbsp;

The pattern of email saving in Salesforce depends on how the message is opened MS Outlook: in **Read mode** (an email opened for viewing from the *Inbox*, *Sent* or the *Salesforce Emails*) or in **Compose mode** (email opened in a separate window for composing – as a *New email* created, a *Reply/Reply all* email, or a *Forwarded* one) and on whether [{{ company_name }} Sync](../Synchronization-Engine-An-Overview/) is active, [paused](../How-to-Open-Sync-Dashboard-(Adaptive-view)/#pause_scc_sync) or [suspended for any reason](../Handling-Sync-Issues/).  

!!! warning "Important"
    Please note that {{ product_name }} processes emails only from the *Inbox*, *Sent,* and the custom *Salesforce Emails* folders of your email client. That concerns both [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/) and the Save button in the [Sidebar](../Introduction/)

&nbsp;

!!! tip "Tip"
    After you save an email in Salesforce using the **Save** button or in any other way, you can quickly open the email's detailed card by selecting the email in MS Outlook or Chrome Extension and clicking the **Email is Saved** button in {{ product_name }}'s header

&nbsp;

#### **1\. Saving an Email When {{ company_name }} Synchronization is Active**

After you click the **Save** button (*manual* or *direct* email saving) in the Sidebar in **Compose mode** and [{{ short_name }} Sync is active](../Synchronization-Engine-An-Overview/), the following actions are performed by {{ product_name }}:

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b72c2180428631d7a89f370.png)

&nbsp;
&nbsp;

###&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **1.1.** Emails saved as EmailMessages vs. Emails saved as Tasks

The saving pattern also depends on your Salesforce Org's configuration: whether you use [EmailMessages (Enhanced email feature)](http://help.salesforce.com/articleView?id=emailadmin_enhanced_email_overview.htm) (scenario **A**) or it does not (scenario **B**).

&nbsp;

**A.** If your Org has the [Enhanced email Salesforce feature](http://help.salesforce.com/articleView?id=emailadmin_enhanced_email_overview.htm) enabled and configured in {{ product_name }} Customization settings, the message will be saved in Salesforce as an [Email message](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_emailmessage.htm) Salesforce object rather than a [Task](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_task.htm); its special formatting as well as other html-encoded elements like inline pictures, tables, or diagrams will be saved. See [this article](../Object-Fields-Mapping-Patterns/#ms_outlook_calendar_items) for information on fields matching patterns applied on saving.
When it comes to related records linking, unlike Tasks (see the information below), EmailMessages can be linked to a single [People record](https://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) and to a reasonable number of [Business records](https://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/), unless [emails duplication](../Customization-Settings-Explained/#3_duplicates_for_objects_linking) is enabled in [{{ short_name }} Customization settings](../Customization-Settings-Explained/).  

!!! tip "Tip"
    There is also an option for customers to [edit already saved EmailMessages via the Sidebar](../Saving-Emails-in-Salesforce-1.-Function-Overview/#editing_already_saved_email_messages_via_the_sidebar)

&nbsp;

&nbsp;

**B.** Or, if your Salesforce Org does **not** have the [Enhanced email setting](http://help.salesforce.com/articleView?id=emailadmin_enhanced_email_overview.htm) enabled, the message will be saved as a completed [Salesforce task](https://help.salesforce.com/articleView?id=tasks.htm&type=5) record. In the resulting Salesforce Tasks the key email's elements (the sender’s / recipients’ email addresses, sending date and time, subject, the message body, the sender’s signature) are stored as values in its [corresponding fields](../Object-Fields-Mapping-Patterns/#ms_outlook_emails); the special formatting of message body and its signature is not saved, except for the contained links. The Task’s _Due date_ field is set to the date when the saved email was sent or received. The resulting Task can be linked to several [People records](https://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) and a single [Business record](https://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/), unless [emails duplication](../Customization-Settings-Explained/#3_duplicates_for_objects_linking) is enabled in {{ short_name }} Customization settings.  

&nbsp;

&nbsp;

###&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **1.2.** The "Save this email to Salesforce" dialog will appear



![](../assets/images/Using-SmartCloud-Connect/How-To-s/Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/new_save_email_dialog.png)

&nbsp;

!!! tip "Tip"
    See [this article](../Save-Email-Dialog/) to learn more about the Save dialog


&nbsp;

To proceed with saving, you need to select People records ([WhoId](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/)) and Business records ([WhatId](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/)) to be linked to the resulting Task or EmailMessage in Salesforce under **Linked records** in this dialog.

[{{ short_name }} initial search](../Initial-Search-and-Applied-Record-Filters/) will also list releated or already linked objects if any are found in Salesforce, so you can make the selection quickly. Use the *Search Salesforce records* field to find these objects in Salesforce and select them; to remove a record from the list, click the **x** icon on the right-hand side. If a needed record does not exist in the CRM, you can easily [create it via the Sidebar](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-%28Adaptive-view%29/#creating_new_records_in_salesforce).

To ensure proper linking of saved emails according to your [{{ product_name }} settings](../Customization-Settings-Explained/) and Salesforce configuration, the dialog indicates [if there are conflicts](../Activities-Linking/#linking_via_the_save_dialog).

Next, under **Attachments**, you can select files attached to the email to be saved in Salesforce along with it, including an exact copy of the message in *.eml* format. Refer to [this article](../Attachments-Handling-(Basic)/) for more information. Note that you can also change the files' names on saving, by clicking the **🖉** (Edit) icon next to their names.

!!! note "Note"
    An email attachment cannot be saved in Salesforce in the following cases: **1.** if it exceeds the file size limit in Salesforce – 25 Mb per file; **2.** if the file's extension was not [allow-listed by your local {{ short_name }} Admin](../Special-Admin-Panel-Settings/)

&nbsp;

!!! warning "Important"
    Please note that with [Salesforce Enhanced email](http://help.salesforce.com/articleView?id=000239922&type=1) enabled, due to a technical limitation, when you save an email along with its attachments in Salesforce via {{ product_name }}, the created Email Message object's *HasAttachment* field will not convey accurate status regarding the presence of attachments, so this field/flag should be disregarded

&nbsp;

Finally, you can edit the values in **Other fields**; these are some of the key fields of the corresponding [Task](https://help.salesforce.com/articleView?id=task_fields.htm&type=5) or [EmailMessage](https://help.salesforce.com/articleView?id=000313606&type=1&mode=1) objects created in Salesforce.  
By default, for Task objects you can edit the **Subject**, **Priority**, **Status** (set to *Completed* if you do not prefer to set another value), and for EmailMessage objects you can edit the **Subject** field.  

!!! tip "Tip"
    You can add some more editable fields to the dialog via [{{ product_name }} customization settings](../Customization-Settings-Explained/#8_customizing_detailed_card_view). There you need to select respectively Task or EmailMessage object type and in the object's Detailed view mark the fields you want to edit via the dialog as *Important*

&nbsp;

After populating all necessary fields, click the **Save** button in the bottom right corner of the dialog to save the email in Salesforce.  

As soon as the email gets successfully saved in Salesforce, there appears a success toast notification *"The email was saved in Salesforce and {number of related records} other objects"*, also indicating the number of linked records.



![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b72c7690428631d7a89f398.png)

&nbsp;

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b72d49d0428631d7a89f415.png" class="minimized">
</p>

&nbsp;

!!! tip "Tip"
    Note that emails which you have saved in Salesforce using the [Save button](../Save-Email-Dialog/#save_email_dialog) or any other method are auto-assigned the custom blue *Salesforce* category in MS Outlook, so you can see if you have already processed it. However, that may happen within 1-30 minutes after saving, since that is done by [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/)

&nbsp;

If [{{ short_name }} synchronization](../Synchronization-Engine-An-Overview/) is active, the user-side differences between saving messages in Read mode and Compose mode is the kind of notification you will get (see the screenshots above) and the fact that messages opened in Compose mode will be saved in Salesforce on the following sync session (within 1-30 minutes), unlike messages opened in Read mode, which are saved immediately.

The Salesforce object created when saving an email is logged in {{ product_name }} **Past activities** under the tab **Activity Timeline** and can be opened in Salesforce directly by clicking the blue **Expand** icon next to it.

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b72c8ae2c7d3a03f89dabdc.png)

&nbsp;

&nbsp;

##### Auto-saving All New Email Messages in a Thread

Finally, there is a convenient option that allows saving all new messages in a correspondence thread in Salesforce automatically; refer to [this article](../Save-All-Emails-in-a-Thread/) for complete information.

&nbsp;

&nbsp;

* * *
&nbsp;

&nbsp;

####  **2\. When {{ company_name }} Sync is not Active**

If the **Save** button is clicked and [{{ company_name }} synchronization](../Synchronization-Engine-An-Overview/) is **not active** for any reason:

*   If the message is opened in **Read mode** (only from the *Inbox* and *Sent* folders or the custom added *Salesforce emails* folder, emails from other folders are **not** processed by {{ short_name }}), it will be saved in Salesforce directly, following the regular pattern described earlier. However, note that the blue Salesforce category will not be automatically assigned to the email saved this way in MS Outlook if sync is disabled  
*   If the message is opened in **Compose mode** (that is, it is a new message created by clicking **New email**, **Reply**, or **Forward** in MS Outlook Desktop or On the Web version), saving it in Salesforce is not possible until you enable synchronization, or, as a workaround, you could save the message and move it to the **Sent** MS Outlook folder and then open it in Read mode and save it  

&nbsp;

&nbsp;

* * *
&nbsp;

&nbsp;

#### **3\. Besides using the Save button, emails saving can be performed in 4 more easy ways**

!!! tip "Tip"
    The category/custom folder emails saving method is also handy when you need to save an email from a stationary or mobile device if it goes offline for some periods of time (e.g. when losing wi-fi connection). Items saved this way will be upsynced to Salesforce as soon as Internet connection is available.
    In addition, this option can be effectively used to process multiple items



&nbsp;

Please note that when you use these quick ways to save an email, the email is saved in Salesforce linked to a relevant Contact, Lead, Account, or Opportunity (if enabled in [sync settings](../Configuring-Activities-Synchronization-Settings/#linking_to_opportunities)) object found via [the default Initial search pattern](../Initial-Search-and-Applied-Record-Filters/). That is, it does not allow choosing specific objects to be linked according to user preference, unlike the Save button method described above.

&nbsp;

##### **3.1.** By assigning the **Salesforce** email category

This method only works for emails opened in [Read mode](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-%28Adaptive-view%29/#2_when_revenue_grid_sync_is_not_active) and requires [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/) to be active.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**3.1.1.** In MS Outlook, find the email message you want to save in Salesforce  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**3.1.2.** Right-click the message and select **Categorize** > **Salesforce**. This message category is marked with blue color

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5b72daca0428631d7a89f461.png">
</p></details>


&nbsp;
&nbsp;

##### **3.2.** By moving the email to the **Salesforce Emails** custom folder

This method only works for emails opened in [Read mode](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-%28Adaptive-view%29/#2_when_revenue_grid_sync_is_not_active) and requires [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/) to be active.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**3.2.1.** In MS Outlook, find the email message you want to save in Salesforce.  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**3.2.2.** Drag-and-drop the message to the dedicated **“Salesforce Emails”** folder, or alternatively right-click > Move > Salesforce Emails folder. On the next sync session emails from this folder will be saved in Salesforce and moved to the Sent folder with the Salesforce category assigned.

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5b72ddc20428631d7a89f479.png">
</p></details>



&nbsp;

or  

&nbsp;

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\move-to-folder.png" class="minimized">
</p></details>


&nbsp;

!!! note "Note"
    After an email is put into the *Salesforce Emails* folder (point **3.2**) it is auto-assigned the blue *Salesforce* category to be [processed by {{ short_name }} sync](../Synchronization-Engine-An-Overview/). After it is saved in Salesforce on the following sync session, the email will be automatically moved back to the *Inbox* or *Sent* folder respectively

&nbsp;

&nbsp;

##### **3.3.** Using the "Quick Save to Salesforce" button

There is also a single-click way to save a message in Salesforce using the **Quick Save to Salesforce** button in [MS Outlook Desktop ribbon](https://support.microsoft.com/en-us/office/show-or-hide-the-ribbon-in-office-d946b26e-0c8c-402d-a0f7-c6efa296b527) or [Outlook on the Web context menu](../Open-in-Outlook-Web/#how_to_open_the_sidebar_in_updated_ms_outlook_on_the_web/)

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5b72f2180428631d7a89f589.png" class="minimized">
</p></details>


&nbsp;

When you use the **Quick save to Salesforce** button to save messages in either Read mode or Compose mode and related [People or Business records](https://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) are found in Salesforce, saving is performed by Sync Engine with a 10-20 minute delay, depending on the actual sync interval, connection speed, and the number of related records found. Saving status is displayed as a notification line under email header:

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5b72f7502c7d3a03f89dae50.png" class="minimized">
</p></details>



&nbsp;

To perform quick saving, [{{ short_name }} Sync engine must be running](../Authorizing-Sync-Engine-to-Work-with-Your-Data/).



&nbsp;

In case related records are **not** found after **Quick save to Salesforce** is clicked, there will appear a notification line suggesting to [create a corresponding Salesforce record](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-(Adaptive-view)/) first:

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b72fa1f2c7d3a03f89dae81.png" class="minimized">
</p>

&nbsp;

If you click **Quick save to Salesforce** for a message opened in Compose mode and synchronization is not running, the message will not be saved and there will appear the following error notification line:

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b72fb192c7d3a03f89dae8d.png" class="minimized">
</p>

&nbsp;

In addition, in this case a suggestion to enable synchronization will appear in {{ product_name }} in **Smart Actions** > **More...** > **Observations**:

<details><summary>>>> Click to see a screenshot <<<</summary>
<p>
    <img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5b72fb5e2c7d3a03f89dae91.png">
</p>
</details>

&nbsp;

##### **3.4.** Using the "Quick Save" button on records headers in the Sidebar

See [this article](../All-User-Actions-in-Add-In-Sidebar/#quick_save_to_a_record) to learn how to use this handy saving method.


&#160;
 &#160;


<style>
  .banners {
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .banners a.button {
      background-color: #FFC827;
      color: #2F3341;
      box-shadow: 0 5px 35px rgba(146, 146, 146, 0.2);
      padding: 20px;
      font-family: Graphic, arial;
      font-weight: 600;
      line-height: 24px;
      margin-top: -100px;
      border-radius: 3px;
      cursor: pointer;
      transition: .1s;
  }

  .banners a.button:hover {
    transform: scale(1.05);
  }

  .banners a.button a:hover,
  .banners a.button a:visited {
      color: #2F3341;
  }

  .banner-3 a.button {
    margin-left: 45%;
  }
</style>

<br>
<div class="banners banner-3">
  <img src="../../assets/images/banners/banner-3.svg" style="width: 100%; height: 100%;">
  <a class="button" href="https://revenuegrid.com/sign-up/?utm_source=kb_rg&utm_medium=referral&utm_campaign=eac&utm_content=banner" target="_blank">Try {{ company_name }} for free</a>
</div>