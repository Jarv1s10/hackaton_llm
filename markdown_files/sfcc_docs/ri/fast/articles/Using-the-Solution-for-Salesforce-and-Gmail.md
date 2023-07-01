---
description: Complete guide on using RG Email Sidebar with Gmail and Google workspace via the Chrome extension
---
# Using the Solution with Gmail and Google Workspace via the Chrome Extension  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*8 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

### Using the Extension's Sidebar

The Extension's Sidebar in Gmail web interface is mostly identical to [its rendition in MS Outlook](../Introduction/); it includes the same set of controls and information fields with the same functions. Therefore, you may refer to the guides on using {{ short_name }} Outlook Add-In ([guide 1](../Introduction/), [guide 2](../All-User-Actions-in-Add-In-Sidebar/)) to learn how to work with the Chrome Extension.  

!!! tip "Tip"
    Similarly, [Customization](../Customization-Settings-Explained/) and [Synchronization](../Configuring-Activities-Synchronization-Settings/) advanced settings of the Chrome Extension mostly mirror ones available for the MS Outlook Add-In

&nbsp;

After the Gmail extension has been configured, as soon as you sign in to your Gmail box the {{ product_name }} Extension can be opened in the pane on the right-hand side of the page opened in Chrome browser.

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\583300e9903360645bfa6acf.png" class="minimized">
</p></details>



&nbsp;

To show or hide the Extension's Sidebar, click the **Salesforce** icon in the toolbox on the right-hand side of Gmail or Google Calendar UI.

&nbsp;

Via the Sidebar, you can directly interact with Salesforce when:  

*   Viewing an email message: Inbox, Sent Mail, or any other folder
*   Composing a new email message
*   Viewing or creating an Event in Google Calendar

&nbsp;

&nbsp;

## Via the Chrome Extension you can perform the following actions:



&nbsp;

### Saving Emails in Salesforce

!!! warning "Important"
    Please note that the Extension does **not** process email messages marked with checkbox ticks in Gmail interface, instead it requires actually opening every email to process them

&nbsp;

There are three ways to save an email from Gmail Inbox or Sent folders to Salesforce:

**A\.** Using the **Save** button in the Extension's panel (direct/manual saving)

* Select an email from Gmail Inbox or Sent folder or compose a new message
* Mark Contact(s), Account(s), or other related Salesforce objects to be associated with the email in the Extension's Sidebar
* Click **Save** in {{ product_name }} Extension's window
* the [*Save this email to Salesforce* dialog](../Save-Email-Dialog/) will appear

&nbsp;

In this dialog, you can set several aspects how the email will be saved in Salesforce:

&nbsp;&nbsp;&nbsp;&nbsp;**1\.** Using the *Search Salesforce records* field, select [People and Business Salesforce object(s)](https://www.forcetalks.com/salesforce-topic/what-is-the-difference-between-whoid-and-whatid-how-can-we-associate-the-task-with-the-salesforce-opportunity-using-whatid) to be linked to the email in Salesforce via the [*Related To* field](https://trailhead.salesforce.com/en/content/learn/modules/data_modeling/object_relationships) of the resulting Task or EmailMessage items  
&nbsp;&nbsp;&nbsp;&nbsp;**2\.** (optional) Select [email attachments](../Attachments-Handling-(Basic)/) to be stored in Salesforce along with the message  
&nbsp;&nbsp;&nbsp;&nbsp;**3\.** (optional) Modify the Subject for the matching Task/Email message created in Salesforce  
&nbsp;&nbsp;&nbsp;&nbsp;**4\.** Set the [Priority](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_task.htm) for the Task/Email message  
&nbsp;&nbsp;&nbsp;&nbsp;**5\.** Set the [Status](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_emailmessage.htm) for the Task/Email message (set to *Completed* by default)  



!!! note "Note"
    Unlike [saving emails in compose mode in MS Outlook](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/) which is only performed by [{{ company_name }} synchronization](../Synchronization-Engine-An-Overview/), with the Chrome Extension Gmail / Google Workspace (G Suite) messages can be saved in Salesforce directly and immediately using the **Save** button at any point in email Read as well as Compose mode

&nbsp;

!!! tip "Tip"
    Note that when an email is saved via {{ short_name }}, the resulting *Task* object's completion date/time or *EmailMessage* object's Sent date/time, are set based on the date/time then the Chrome Extension's Sidebar was <u>opened</u> in Gmail to process this email 

&nbsp;

**B\.** By moving (or dragging-and-dropping) the email you need to save in Salesforce to the custom *Salesforce Emails* folder. This [folder/label](https://hiverhq.com/blog/gmail-labels/) is created and set as the marker for item auto-saving in Salesforce by {{ company_name }} synchronization

<details><summary>>>> Click to see an animation <<<</summary>
<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Gmail\move_to_folder.gif" class="minimized">
</p>
</details>


&nbsp;

**C\.** By assigning the email the blue *Salesforce Emails* label

<details><summary>>>> Click to see an animation <<<</summary>
<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Gmail\assign_label.gif" class="minimized">
</p>
</details>



&nbsp;

The other custom label/Gmail subfolder added to your mailbox on {{ product_name }} installation is *Tracked successfully*; this label/subfolder marks emails and calendar items which have already been successfully saved in Salesforce via {{ product_name }}.

!!! warning "Important"
    In the cases 2 and 3 email saving is performed by [{{ company_name }} synchronization](../Synchronization-Engine-An-Overview/), that is, not instantly but on the following sync session (within 1-30 minutes). The Task/Email Message object created this way will be automatically linked to primary [related objects](../Initial-Search-and-Applied-Record-Filters/#related_records_retrieval_pattern) retrieved by {{ product_name }} [initial search](../Initial-Search-and-Applied-Record-Filters/)

&nbsp;

&nbsp;

#### Saving Archived emails

[Archieved Gmail messages](http://howto.husd.k12.ca.us/kb/google-apps/what-does-archiving-mean-in-gmail) can be saved in Salesforce via [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/) just like any other email messages, but assigning them the Salesforce emails label or clicking the Save button.

&nbsp;

* * *

&nbsp;

### Syncing Calendar Events in Salesforce

!!! note "Note"
    Google Calendar Events saving is performed on the following [sync session](../Synchronization-Engine-An-Overview/); it may take between 1 and 30 minutes for a saved Event to appear in Salesforce

&nbsp;

Syncing Google calendar Events in Salesforce can be done in three ways:  

**1\.** Using the **Save** button in the Extension's panel (immediate/manual saving)

&nbsp;&nbsp;&nbsp;&nbsp;**1\.1.** Open the calendar event you want to sync with your Salesforce calendar  

&nbsp;&nbsp;&nbsp;&nbsp;**1\.2.** [Search](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-(Adaptive-view)/) [People and Business Salesforce objects](https://www.forcetalks.com/salesforce-topic/what-is-the-difference-between-whoid-and-whatid-how-can-we-associate-the-task-with-the-salesforce-opportunity-using-whatid) and mark the checkboxes next to their names in the Extension. If no relevant objects exists, [create them](../Create-New-Records/)  

&nbsp;&nbsp;&nbsp;&nbsp;**1\.3.** Click **Save** at the top of {{ product_name }} Extension's Sidebar. The [*Save this event to Salesforce* dialog](../Save-Email-Dialog/#save_event_dialog) will appear  

&nbsp;&nbsp;&nbsp;&nbsp;**1\.4.** Add [People or Business records](https://www.forcetalks.com/salesforce-topic/what-is-the-difference-between-whoid-and-whatid-how-can-we-associate-the-task-with-the-salesforce-opportunity-using-whatid) to be [linked](https://trailhead.salesforce.com/en/content/learn/modules/data_modeling/object_relationships) to the resulting Salesforce Event using the *Search Salesforce records* field  
&nbsp;

**2\.** {{ product_name }} can be set up to save all Calendar events automatically on [synchronization sessions](../Synchronization-Engine-An-Overview/). Please refer to [this article](../Configuring-Activities-Synchronization-Settings/#automatic_syncing_of_calendar_items_events_autosharing) for detailed information on these settings.

In the cases ( **2** ) and ( **3** ) the Event object created this way will be automatically linked to primary [related objects](../Initial-Search-and-Applied-Record-Filters/#related_records_retrieval_pattern) retrieved by {{ product_name }} [initial search](../Initial-Search-and-Applied-Record-Filters/).

!!! tip "Tip"
    To exclude an email message or event from being synced in Salesforce, you can add its email address to [sync blocklist](../Configuring-Activities-Synchronization-Settings/#blocklisting_emails_and_domains) in [synchronization settings](../How-to-Open-Sync-Dashboard-(Adaptive-view)/)
&nbsp;

**3\.** Color-coding (only available by request)

!!! warning "Important"
    In the latest Extension updates, this syncing method is disabled by default and it can be enabled exclusively upon request sent to our [Customer Success Managers team](mailto:support@revenuegrid.com).  
    Along with the request you should specify what color(s) you want to use for color-marking Gmail calendar events to be synced with Salesforce. The available colors are: *Tomato*, *Tangerine*, *Banana*, *Basil*, *Sage*, *Peacock*, *Blueberry*, *Lavender*, *Grape*, *Flamingo*, *Graphite*. That is required to prevent confusion of colorcoding patterns already in place within a company.  
    In addition, you can define the time range for Events syncing (by default that is 15 days in the past from the actual date). Search *GoogleCalendarLastActivityTimeSpan* in [this article](../Special-Admin-Panel-Settings/#extra_configuration_settings) for more information.



By marking the event with the chosen color; color marking is not to be confused with [Gmail labels](https://hiverhq.com/blog/gmail-labels/).

Note that after you set up {{ product_name }}, *Blueberry* is set as the marker for events saving in Salesforce by {{ company_name }} synchronization, unless another color is configured.  

<details><summary>>>> Click to see an animation <<<</summary>
<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Gmail\color_coded.gif" class="minimized">
</p>
</details>



&nbsp;
&nbsp;

#### Events handling features presently unavailable in {{ product_name }} Chrome Extension

Several [calendar items handling mechanics](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/) available in {{ product_name }} MS Outlook Desktop or On the Web version Sidebar are presently not implemented in the Chrome Extension:  

- No auto-saving of files attached to events: Attached files saving can only be performed [using the **Save** button](../Save-Email-Dialog/)  
- Setting special Event reminders is unavailable  
- Only Event organizers (but not the in-org attendees) can save Events using color-coding (see point (**2**) above)  

&nbsp;

* * *

&nbsp;

### Syncing Contacts between Gmail and Salesforce

!!! tip "Tip"
    Also see [this article](../Synchronization-of-Contacts/) to learn more about syncing of Contacts

&nbsp;

You can sync a Gmail Contact in Salesforce in the following way:

By assigning the Contact you need to sync in Salesforce the custom *Salesforce Contacts* label. This custom Gmail [folder/label](https://hiverhq.com/blog/gmail-labels/) is added to Gmail on [sync activation](../How-to-Set-Up-the-Chrome-Extension-for-Salesforce-and-Gmail/#2_sign_in_to_gmail_and_grant_rg_email_sidebar_permission_to_work_with_your_gmail_and_google_calendar_data) and is then used as the marker for Contacts syncing in Salesforce by [{{ short_name }} sync engine](../Synchronization-Engine-An-Overview/).  

<details><summary>>>> Click to see an animation <<<</summary>
<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Gmail\label_contact.gif" class="minimized">
</p>
</details>


&nbsp;

In addition to that, your business Contacts existing in Salesforce get [down-synced](../Special-Sync-Options-Save-Events-As-Other-&-One-Way-Sync/#one-way_synchronization) to Gmail, as auto-created Gmail contacts. 

&nbsp;

* * *

&nbsp;

### Syncing Tasks between Google and Salesforce

!!! tip "Tip"
    Presently, syncing of recurring Task series is not supported in either direction, only a single Task from a series gets synced per attempt

&nbsp;

{{ short_name }} Chrome Extension also allows to easily synchronize [Google Tasks](https://support.google.com/tasks/answer/7675772?co=GENIE.Platform%3DDesktop&hl=en) in Salesforce using the custom *Salesforce tasks* list auto-created in Gmail by {{ short_name }} Sync engine. To sync a task:  

**1\.** Open the needed task in Gmail

**2\.** Add the Task to the custom *Salesforce tasks* list. See [this Google article](https://support.google.com/a/users/answer/9310236?hl=en) to learn how to add a Task to a List.  
You may also assign several Tasks in bulk this way

**3\.** Now the Task will be automatically synced to Salesforce on the following [Sync session](../Synchronization-Engine-An-Overview/) within 1 - 30 minutes, depending on the current Sync period

Also see [this article](../Object-Fields-Mapping-Patterns/#google_tasks) to learn how Google Tasks fields are matched with Salesforce Tasks fields.

&nbsp;

* * *

&nbsp;

### Searching for and creating Salesforce objects via the Extension

You can search for or create Salesforce objects in the Extension in the same ways as in {{ product_name }} MS Outlook Desktop or On the Web version Add-In. Please refer to [this article](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-(Adaptive-view)/#searching_for_existing_salesforce_records_and_creating_new_records_in_smartcloud_connect) for detailed information on these functions.

For information on how to install the {{ product_name }} extension in your Chrome browser, refer to the article [Signing Up with {{ product_name }} for Salesforce and Gmail](../How-to-Set-Up-the-Chrome-Extension-for-Salesforce-and-Gmail/).

&nbsp;

* * *

&nbsp;

#### How to refresh the Sidebar

To refresh the Chrome Extension Sidebar's user interface and the data displayed in it, for example after [importing](../Managing-Email-Sidebar-Customizations/) or [adjusting](../Customization-Settings-Explained/) the Extension's Customization settings:

**1\.** Click on the **☰** (Menu) icon in the Sidebar  

**2\.** Select **Refresh** in the Menu  

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Gmail\refresh.png">
</p></details>


&nbsp;

* * *

&nbsp;

#### Differences between the Exchange/Office 365 Add-In implementation and the Chrome Extension for Gmail

* The Extension does **not** require setting up [mailbox access authorization](../Authorizing-Sync-Engine-to-Work-with-Your-Data/) or [additional sync access authorization](../Authorizing-Sync-Engine-to-Work-with-Your-Data/) in {{ short_name }} Sync settings

* The Extension does **not** require additional Gmail signing-in to access the [Sync settings page](../Configuring-Activities-Synchronization-Settings/)

* Presently, the Extension only supports the following [{{ short_name }} Smart Actions](../All-User-Actions-in-Add-In-Sidebar/#smart_actions):  
  [Book Me (Calendar Availability)](../Sharing-Calendar-Availability-(Adaptive-view)/), [Time slots](../How-to-Send-Meeting-Time-Slots-(Adaptive-view)/), [Engagement panel](../How-to-Use-the-Solution-s-Engagement-Panel/) (only [auto-insertion](../How-to-Use-the-Solution-s-Engagement-Panel/#to_insert_the_tracking_code_formerly_magic_pixel_into_an_email_message) of the tracking code is supported, and it is inserted only while the Extensions [Sidebar](../Introduction/) is opened), [Salesforce Templates](../Using-Salesforce-Templates/), [Observations](../Using-Salesforce-Templates/), [Reports](https://trailhead.salesforce.com/en/content/learn/modules/reports_dashboards/reports_dashboards_overview)


* Presently, the Extension does not support [automatic saving of all emails in a communication thread](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_email_threads)
* The Extension can save emails in Compose mode immediately in Salesforce, independently from [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/); the resulting Salesforce Task's or EmailMessage's Date and time field are set to the Date and time when the Sidebar was opened to save it
* [Smart description](../Using-the-Smart-Description-Feature/) is not supported
* No [saving in Salesforce](../Attachments-Handling-(Basic)/) of [inline attachments](https://www.quora.com/Whats-the-difference-between-attaching-and-embedding-images-in-Gmail) (also not supported in the Exchange/Office 365 Add-In implementation). However, the Chrome Extension can save in Salesforce files sent as [Google drive links](https://support.google.com/mail/answer/2487407?co=GENIE.Platform%3DDesktop&hl=en) 
* No ["default attachment"](../Attachments-Handling-(Basic)/#use_cases) (an email's exact copy in *.eml* format) saving available
* [Calendar events instant-sync](../Synchronization-Engine-An-Overview/#instant_sync_of_calendar_items) from Google calendar to Salesforce is not supported; however, the insant sync of events from Salesforce to Google calendar is supported



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