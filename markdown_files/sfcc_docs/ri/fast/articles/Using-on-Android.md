---
description: Guide on using RG Email Sidebar on Android Devices
---
# Using the Solution on Android Devices  
  

<div class="container" style="display: inline-block; height: 42px; width: auto; padding: 1px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/mobile-icon.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*8 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! tip "Tip"
    See [this article](../Using-on-iPhone/) to learn how to use the solution on iPhone devices

&nbsp;

!!! note "Note"
    Presently, due to [a limitation in MS Outlook Mobile](https://docs.microsoft.com/en-us/outlook/add-ins/outlook-mobile-addins), [{{ short_name }} Add-In](../Introduction/) can only be used in MS Outlook for Android or iOS with Office 365 mail accounts, and not with MS Exchange accounts. At that, users' data from MS Exchange accounts can be handled using [{{ company_name }} synchronization](../Synchronization-Engine-An-Overview/), through [auto-saving](../Configuring-Activities-Synchronization-Settings/#automatic_syncing_of_calendar_items_events_autosharing) or the custom "Salesforce" category / folder / list, as described in this article

&nbsp;

{{ product_name }} allows teams to collaborate on-the-go within their Salesforce Orgs, by saving business Contacts, Emails, Calendar events, and Tasks in Salesforce right from personal smartphone or tablet devices with MS Outlook Mobile or On the Web running. Similarly, Contacts and other Salesforce records, Tasks, or Calendar Appointments can be instantly created, updated, or processed via the Sidebar; all additions and changes get automatically mirrored two-way between mail server and Salesforce through server-side [{{ short_name }} Sync Engine](../Synchronization-Engine-An-Overview/). 

If your device has a high enough screen resolution, for example you are using a tablet, you may also effectively use the full rendition of [{{ product_name }}](../Introduction/) in MS Outlook on the Web in a [supported mobile browser](../Frequently-Asked-Questions/#supported_browsers_with_outlook_on_the_web).

&nbsp;

## Handling Business Communication Data from an Android device

To save an Email, Contact, or Task in Salesforce from a mobile device, you may use the basic methods provided by {{ short_name }} Sync Engine or the [Save button](../Save-Email-Dialog/) provided by the mobile rendition of {{ short_name }} [Outlook Add-In](../Introduction/).

&nbsp;

You may also use other [{{ product_name }}](../Introduction/) functions in its mobile rendition on MS Outlook for iOS or Android: create or search Salesforce records, schedule Time Slots or Book Me meetings, etc.

&nbsp;

&nbsp;

### In MS Outlook for Android

You can effectively use {{ product_name }} with [MS Outlook for Android](http://play.google.com/store/apps/details?id=com.microsoft.office.outlook&hl=en). This way you may both easily process your Emails, Calendar items, Contacts, and Tasks via the dedicated Salesforce folder and take a full advantage of [{{ product_name }}](../Introduction/)'s mobile rendition.
&nbp;

Use prerequisites:

- [Install the Add-In](../How-to-Install-and-Run-the-Solution-for-Office-365-Mailboxes/) for your email account

- [Activate {{ short_name }} Sync](../Authorizing-Sync-Engine-to-Work-with-Your-Data/)  

Also refer to [this article](../How-to-Install-the-Solution-using-a-Mobile-Device/) to learn how to install the Add-In via MS Outlook for Android if it wasn't installed.

&nbsp;

&nbsp;

To open [{{ product_name }}](../Introduction/)'s mobile rendition in MS Outlook for Android:  
**1\.** Open a [relevant email](../Saving-Emails-in-Salesforce-1.-Function-Overview/#6_the_add-in_chrome_extension_does_not_work_with_service_emails) in the folders *Inbox* or *Sent*  
**2\.** Tap on the **⋮** (Menu) icon in the upper right corner of the email  
**3\.** Tap on {{ product_name }} logo  

<details><summary>>>> Click to see an animation <<<</summary>
<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Android_screens\open-sidebar.gif">
</p>
</details>

&nbsp;

You will see [{{ product_name }}](../Introduction/), your portal to Salesforce listing [related CRM records](../Viewing-Salesforce-Records-Related-to-your-Email-%28Adaptive-view%29/) and a [number of handy actions](../All-User-Actions-in-Add-In-Sidebar/).

!!! tip "Tip"
    You may also use {{ product_name }} in Outlook on the Web (Outlook.com, Outlook.office.com) opened in your mobile web browser, but the Sidebar's controls are not specifically optimized for lower mobile screen resolutions

&nbsp;

#### Saving Outlook Emails from Android

{{ product_name }} processes to Salesforce <u>only</u> Emails marked this way, this excludes the risks that your personal Emails might get synced there from your mobile.

Emails can be saved in one of the following ways, only in [Read mode](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-%28Adaptive-view%29/):

- using the Save button in the mobile rendition of [{{ product_name }}](../Introduction/)
- using basic Sync Engine means – the custom Salesforce Emails folder

&nbsp;

##### Emails saving via the Save button

This method has the following advantages: you can set what records to link to the saved item in Salesforce and edit the resulting item's key fields Subject, Priority, Status, etc. via [Save dialog](../Save-Email-Dialog/); saving is performed immediately.

To save an email:

**1\.** In MS Outlook Mobile folders Inbox or Sent, select a business email your want to save in Salesforce  

**2\.** Tap the **•••** (Menu) icon on the top and select {{ product_name }} icon  

  <details><summary>>>> Click to see a screenshot <<<</summary>
    <p>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Android_screens\Emails\emails31.png">
    </p>
    </details>

&nbsp;

**3\.** The home screen of the mobile rendition of [{{ product_name }}](../Introduction/) will be opened. Tap the button **Save email** in its upper right corner  

  <details><summary>>>> Click to see a screenshot <<<</summary>
    <p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Android_screens\Emails\emails311.png" style="width: 70%; height: 70%;">
    </p>
    </details>

&nbsp;

**4\.** Pick relevant records to be linked using the Search field or the checkboxes next to suggested records  

  <details><summary>>>> Click to see a screenshot <<<</summary>
    <p>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Android_screens\Emails\emails32.png" style="width: 70%; height: 70%;">
    </p>
    </details>

&nbsp;

Next, optionally modify key fields of the saved item: *Subject*, *Priority*, *Status*, etc.

&nbsp;

**5\.** Tap the **Save** button on the top. As soon as the email is saved you will see a green pop-up notification  

  <details><summary>>>> Click to see a screenshot <<<</summary>
    <p>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Android_screens\Emails\emails33.png" style="width: 70%; height: 70%;">
    </p>
    </details>

&nbsp;

&nbsp;

##### Emails saving via the dedicated folder

If you use either of these three methods, emails get saved on the following [Sync session](../Synchronization-Engine-An-Overview/), that may take from 1 to 30 minutes. As soon as an email from the dedicated folder is saved, it gets the custom "Salesforce Email" category. Feel free to move saved emails back to Inbox or Sent folders from the dedicated folder after they are saved.
If the dedicated folder method is used, emails get saved linked to [auto-retrieved related records](../Initial-Search-and-Applied-Record-Filters/#the_resulting_related_records_list_will_include).

&nbsp;

&nbsp;

**Method 1. Also used for bulk emails processing:** 

Tap on the circles next to needed business emails to select them, then tap the **⋮** (Menu) icon in the upper right corner and select the action **Move to Folder** > **Salesforce Emails** folder

  <details><summary>>>> Click to see a screenshot <<<</summary>
    <p>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Android_screens\Emails\emails21.png">
        <br>
        <br>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Android_screens\Emails\emails11.png">
    </p>
    </details>

&nbsp;

&nbsp;

**Method 2.**

Open the needed business email. Next, tap the **⋮** (Menu) icon in the upper right corner and select the action **Move to Folder**, then tap **Salesforce Emails** 

  <details><summary>>>> Click to see a screenshot <<<</summary>
    <p>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Android_screens\Emails\emails22.png">
        <br>
        <br>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Android_screens\Emails\emails11.png">
    </p>
    </details>

&nbsp;

&nbsp;

**Method 3.** 

After you [configure *Move to folder* for the action Right-swipe on an email in MS Outlook for Android](https://support.microsoft.com/en-us/topic/how-do-i-customize-my-swipe-options-2c66fbb9-09cd-4c97-9f16-1fdad0bb4172):  
Tap, hold and drag the needed business email to the right, then put it into the **Salesforce Emails** folder.

  <details><summary>>>> Click to see the screenshots <<<</summary>
    <p>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Android_screens\Emails\emails10.png">
    <br>
    <br>
    <br>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Android_screens\Emails\emails11.png">
    </p>
    </details>

&nbsp;
***
&nbsp;

#### Syncing Outlook Calendar Items from Android

Since MS Outlook Mobile does not allow custom categories assigning and {{ product_name }} is unavailable for opened calendar items, there are only three options for managing calendar items:  


* [calendar items auto-saving](../Configuring-Activities-Synchronization-Settings/#automatic_syncing_of_calendar_items_events_autosharing) by [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/)  
* events creation via {{ short_name }} Meeting Scheduler: [Time slots](../How-to-Send-Meeting-Time-Slots-(Adaptive-view)/) or [Book me](../Sharing-Calendar-Availability-(Adaptive-view)/)  
* you may also create new Salesforce Events directly using the [+ (Create) button in {{ product_name }}](../Create-New-Records/). At that, any Events created this way will appear in MS Outlook as attendee-less Appointments. See [this article](../Create-New-Event/) for details

In addition, any changes to calendar items created in Salesforce or synced from MS Outlook Desktop or On the Web also get reflected in MS Outlook Mobile calendar.

&nbsp;

&nbsp;

##### Using Meeting Scheduler features from Android

{{ short_name }} Meeting Scheduler features Book Me and Time Slots are also available in the mobile implementation. Meeting invitation links generation dialogs are mostly identical to Desktop implementation, see the following articles for complete information: [Book Me](../Sharing-Calendar-Availability-%28Adaptive-view%29/); [Time Slots](../How-to-Send-Meeting-Time-Slots-%28Adaptive-view%29/).

&nbsp;
***
&nbsp;

#### Syncing Outlook Contacts from Android

{{ product_name }} processes to Salesforce solely the Contacts you marked this way, this excludes the risks that your personal Contacts might get synced there from your mobile.

As long as a Contact is synced, any updates of the Contact on either side get mirrored on the other. To synchronize an MS Outlook Contact with Salesforce, you need to assign it the custom *Salesforce* category:

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Android_screens\contact-swipe.jpg" style="width:45%; display:inline-block; vertical-align:middle; margin-left:10px; float: right">
</p>

<br>

**1\.** Find a business contact that you want to sync in Salesforce in the Contacts list and left-swipe on it  

<br><br><br><br><br><br>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Android_screens\contact-category.jpg" style="width:45%; display:inline-block; vertical-align:middle; margin-left:10px; float: right">
</p>

**2\.** Select the **Salesforce** category to assign  

<br><br>

The Contact will get synced in Salesforce on the following [Sync session](../Synchronization-Engine-An-Overview/) within a span from 1 to 30 minutes.

<br><br><br>

##### To stop syncing a Contact

If you later need to stop syncing a Contact, remove the Salesforce category by right-swiping on it.

&nbsp;
***
&nbsp;

#### Syncing Outlook Tasks in MS To Do App from Android

{{ product_name }} processes to Salesforce <u>only</u> Tasks marked this way, this excludes the risks that your personal Tasks might get synced there from your mobile.

As long as a Task is synced, any updates of the Task on either side get mirrored on the other. To synchronize an MS Outlook Task with Salesforce, you need to assign it to the custom *Salesforce Tasks* list in [Microsoft To Do App](https://play.google.com/store/apps/details?id=com.microsoft.todos&hl=en&gl=US) installed on your mobile:  

<br>

**Method 1: Create a Task in the "Salesforce Tasks" list**

**1\.** Open MS To Do App and open the *Salesforce Tasks* list

  <details><summary>>>> Click to see a screenshot <<<</summary>
    <p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Android_screens\Tasks\tasks30.png">
    </details>
&nbsp;

**2\.** Tap the big **⊕** (Add A Task) button, fill in Task details and then tap **⬆** 

  <details><summary>>>> Click to see the screenshots <<<</summary>
    <p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Android_screens\Tasks\tasks31.png">
    <br>
    <br>
    <br>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Android_screens\Tasks\tasks32.png">
    </p>
    </details>

&nbsp;

The Task you created will get synced in Salesforce on the following [Sync session](../Synchronization-Engine-An-Overview/) within a span from 1 to 30 minutes.

&nbsp;

&nbsp;

**Method 2. Bulk-move several Tasks to the list**

**1\.** Open MS To Do App and open the list that contains the Tasks that you need to sync in Salesforce; long-tap on one of the Tasks and short-tap on any additional Tasks to mark them  

  <details><summary>>>> Click to see a screenshot <<<</summary>
    <p>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Android_screens\Tasks\tasks21.png">
    </p>
    </details>

&nbsp;

**2\.** Tap on the **⋮** (Actions Menu) icon on the top and select **Move**

  <details><summary>>>> Click to see a screenshot <<<</summary>
    <p>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Android_screens\Tasks\tasks22.png">
    </p>
    </details>

&nbsp;

**3\.** Select the list **Salesforce Tasks**  

  <details><summary>>>> Click to see a screenshot <<<</summary>
    <p>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Android_screens\Tasks\tasks23.png">
    </p>
    </details>

&nbsp;

Selected Tasks will get synced in Salesforce on the following [Sync session](../Synchronization-Engine-An-Overview/) within a span from 1 to 30 minutes.

&nbsp;

&nbsp;

##### To stop syncing a Task

If you later need to stop syncing a Task, remove it from the Salesforce Tasks list.

&nbsp;

&nbsp;

* * *

&nbsp;

&nbsp;

#### Using {{ short_name }} Chrome Extension for Gmail on Android

For phone devices, there is only a limited scope of items saving scenarios using {{ product_name }} for Gmail:

##### Saving Emails via the Custom folder/label:

To save an email message in Salesforce, move the message to the "Salesforce Emails" folder.

&nbsp;

&nbsp;

### Usage Limitations on Mobile Devices

When you are using {{ product_name }} in MS Outlook on a mobile device, due to the [peculiarities of the mobile implementation of MS Outlook](http://support.office.com/en-us/article/compare-outlook-for-pc-outlook-on-the-web-and-outlook-for-ios-android-b26a7bf5-0ac7-48ba-97af-984e0645dde5) the solution offers slightly different use patterns than in MS Outlook Desktop devices or Outlook on the Web:

- MS Outlook Mobile implementation does not allow modifying created calendar items; only deleting them to create them anew is possible    
- MS Outlook Mobile implementation does not allow assigning categories to items or removing them; if an item already has an assigned category, the item is highlighted with another color. For this reason it is recommended to [enable automatic syncing of new Appointments and Meetings](../Configuring-Activities-Synchronization-Settings/#automatic_syncing_of_calendar_items_events_autosharing) if you intend to use {{ product_name }} on mobile devices most of the time 
- Since [Compose mode](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/) is not available in MS Outlook Mobile implementation, email saving behavior and the flow of the [Send meeting time slots](../How-to-Send-Meeting-Time-Slots-(Adaptive-view)/) and [Share calendar availability](../Sharing-Calendar-Availability-(Adaptive-view)/) features are more basic; for the latter case pre-defined non-modifiable [Salesforce templates](https://help.salesforce.com/articleView?id=email_templates_lightning_parent.htm&type=5) are used to populate invite emails' bodies   
- Another limitation of the mobile implementation on both iOS and Android is the impossibility to save files attached to emails or calendar items in Salesforce: a *"Something wrong happened. Attachments were not saved"* notification appears if you attempt doing that



&#160;
 &#160;

