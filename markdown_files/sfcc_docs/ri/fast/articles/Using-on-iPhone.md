---
description: Guide on using RG Email Sidebar on iPhone Devices
---
# Using the Solution on iPhone Devices  
  

<div class="container" style="display: inline-block; height: 42px; width: auto; padding: 1px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/mobile-icon.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*8 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! tip "Tip"
    See [this article](../Using-on-Android/) to learn how to use the solution on Android devices

&nbsp;

!!! note "Note"
    Presently, due to [a limitation in MS Outlook Mobile](https://docs.microsoft.com/en-us/outlook/add-ins/outlook-mobile-addins), [{{ short_name }} Add-In](../Introduction/) can only be used in MS Outlook for Android or iOS with Office 365 mail accounts, and not with MS Exchange accounts. At that, users' data from MS Exchange accounts can be handled using [{{ company_name }} synchronization](../Synchronization-Engine-An-Overview/), through [auto-saving](../Configuring-Activities-Synchronization-Settings/#automatic_syncing_of_calendar_items_events_autosharing) or the custom "Salesforce" category / folder / list, as described in this article

&nbsp;



{{ product_name }} allows teams to collaborate on-the-go within their Salesforce Orgs, by saving business Contacts, Emails, Calendar events, and Tasks in Salesforce right from personal smartphone or tablet devices with MS Outlook Mobile or On the Web running. Similarly, Contacts and other Salesforce records, Tasks, or Calendar Appointments can be instantly created, updated, or processed via the Sidebar; all additions and changes get automatically mirrored two-way between mail server and Salesforce through server-side [{{ short_name }} Sync Engine](../Synchronization-Engine-An-Overview/). 

If your device has a high enough screen resolution, for example you are using a tablet, you may also effectively use the full rendition of [{{ product_name }}](../Introduction/) in MS Outlook on the Web in a [supported mobile browser](../Frequently-Asked-Questions/#supported_browsers_with_outlook_on_the_web).

&nbsp;

## Handling Business Communication Data via an iPhone Device

To save an Email, Contact, or Task in Salesforce from a mobile device, you may use the basic methods provided by {{ short_name }} Sync Engine or the [Save button](../Save-Email-Dialog/) provided by the mobile rendition of {{ short_name }} [Outlook Add-In](../Introduction/).

&nbsp;

You may also use other [{{ product_name }} ](../Introduction/) functions in its mobile rendition on MS Outlook for iOS or Android: create or search Salesforce records, schedule Time Slots or Book Me meetings, etc.

&nbsp;

### In MS Outlook for iOS

Use prerequisites:

- [Install the Add-In](../How-to-Install-and-Run-the-Solution-for-Office-365-Mailboxes/) for your email account
- [Activate {{ short_name }} Sync](../Authorizing-Sync-Engine-to-Work-with-Your-Data/)

Also refer to [this article](../How-to-Install-the-Solution-using-a-Mobile-Device/) to learn how to install the Add-In via MS Outlook for iOS if it wasn't installed.



&nbsp;

#### Saving Outlook Emails from iPhone

{{ product_name }} processes to Salesforce <u>only</u> Emails marked this way, this excludes the risks that your personal Emails might get synced there from your mobile.

Emails can be saved in one of the following ways, only in [Read mode](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-%28Adaptive-view%29/):

- using the Save button in the mobile rendition of [{{ product_name }}](../Introduction/)
- using basic Sync Engine means – the custom *Salesforce Emails* folder

&nbsp;

##### Emails saving via the Save button

This method has the following advantages: you can set what records to link to the saved item in Salesforce and edit the resulting item's key fields *Subject*, *Priority*, *Status*, etc. via [Save dialog](../Save-Email-Dialog/); saving is performed immediately.

To save an email:

**1\.** In MS Outlook Mobile folders Inbox or Sent, select a business email your want to save in Salesforce  

**2\.** Tap the **•••** (Menu) icon on the top and select **Open {{ company_name }}**  

  <details><summary>>>> Click to see a screenshot <<<</summary>
    <p>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\Mobile\iPhone\Emails\emails31.png" style="width: 65%; height: 65%;">
    </p>
    </details>
&nbsp;

**3\.** The home screen of the mobile rendition of [{{ product_name }}](../Introduction/) will be opened. Tap the button **Save email** in its upper right corner  

  <details><summary>>>> Click to see a screenshot <<<</summary>
    <p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\Mobile\iPhone\Emails\emails311.png" style="width: 65%; height: 65%;">
    </p>
    </details>


&nbsp;



**4\.** Pick relevant records to be linked using the Search field or the checkboxes next to suggested records  

  <details><summary>>>> Click to see a screenshot <<<</summary>
    <p>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\Mobile\iPhone\Emails\emails32.png" style="width: 65%; height: 65%;">
    </p>
    </details>

&nbsp;

Next, optionally modify key fields of the saved item: *Subject*, *Priority*, *Status*, etc.

&nbsp;

**5\.** Tap the **Save** button on the top. As soon as the email is saved you will see a green pop-up notification  

  <details><summary>>>> Click to see a screenshot <<<</summary>
    <p>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\Mobile\iPhone\Emails\emails33.png" style="width: 65%; height: 65%;">
    </p>
    </details>


&nbsp;

&nbsp;

##### Emails saving via the dedicated folder

If you use either of these three methods, emails get saved on the following [Sync session](../Synchronization-Engine-An-Overview/), that may take from 1 to 30 minutes. As soon as an email from the dedicated folder is saved, it gets the custom "Salesforce Email" category. Feel free to move saved emails back to Inbox or Sent folders from the dedicated folder after they are saved.
If the dedicated folder method is used, emails get saved linked to [auto-retrieved related records](../Initial-Search-and-Applied-Record-Filters/#the_resulting_related_records_list_will_include).

**Method 1.** 

Tap, hold and drag the needed business email to the right, then put it into the **Salesforce Emails** folder.

  <details><summary>>>> Click to see the screenshots <<<</summary>
    <p>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\Mobile\iPhone\Emails\emails10.png" style="width: 65%; height: 65%;">
    <br>
    <br>
    <br>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\Mobile\iPhone\Emails\emails11.png" style="width: 65%; height: 65%;">
    </p>
    </details>
&nbsp;

&nbsp;

**Method 2. Also used for bulk emails processing:** 

Tap the circle next to the needed business emails to select them, then tap the icon **Move to Folder** in the bottom toolbar and select the **Salesforce Emails** folder.

  <details><summary>>>> Click to see a screenshot <<<</summary>
    <p>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\Mobile\iPhone\Emails\emails21.png" style="width: 65%; height: 65%;">
    </p>
    </details>
&nbsp;

&nbsp;

**Method 3.**
Open the needed business email. Next, tap the **•••** (Menu) icon on the top and select the action **Move to Folder** > **Salesforce Emails** folder.

  <details><summary>>>> Click to see a screenshot <<<</summary>
    <p>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\Mobile\iPhone\Emails\emails22.png" style="width: 65%; height: 65%;">
    </p>
    </details>


&nbsp;

&nbsp;

&nbsp;

#### Syncing Outlook Calendar Items from iPhone

Since MS Outlook Mobile does not allow custom categories assigning and {{ product_name }} is unavailable for opened calendar items, there are only three options for managing calendar items:  


* [calendar items auto-saving](../Configuring-Activities-Synchronization-Settings/#automatic_syncing_of_calendar_items_events_autosharing) by [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/)  
* events creation via {{ short_name }} Meeting Scheduler: [Time slots](../How-to-Send-Meeting-Time-Slots-(Adaptive-view)/) or [Book me](../Sharing-Calendar-Availability-(Adaptive-view)/)  
* you may also create new Salesforce Events directly using the [+ (Create) button in {{ product_name }}](../Create-New-Records/). At that, any Events created this way will appear in MS Outlook as attendee-less Appointments. See [this article](../Create-New-Event/) for details

In addition, any changes to calendar items created in Salesforce or synced from MS Outlook Desktop or On the Web also get reflected in MS Outlook mobile calendar.

&nbsp;

&nbsp;

##### Using Meeting Scheduler features from iPhone

{{ short_name }} Meeting Scheduler features Book Me and Time Slots are also available in the mobile implementation. Meeting invitation links generation dialogs are mostly identical to Desktop implementation, see the following articles for complete information: [Book Me](../Sharing-Calendar-Availability-%28Adaptive-view%29/); [Time Slots](../How-to-Send-Meeting-Time-Slots-%28Adaptive-view%29/).


&nbsp;

&nbsp;

&nbsp;

#### Syncing Outlook Contacts from iPhone

{{ product_name }} processes to Salesforce solely the Contacts you marked this way, this excludes the risks that your personal Contacts might get synced there from your mobile.

As long as a Contact is synced, any updates of the Contact on either side get mirrored on the other. To synchronize an MS Outlook Contact with Salesforce, you need to assign it the custom *Salesforce Contacts* category:

**1\.** Find a business contact that you want to sync in Salesforce in the Contacts list and left-swipe on it  

  <details><summary>>>> Click to see a screenshot <<<</summary>
    <p>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\Mobile\iPhone\Contacts\contacts10.png" style="width: 65%; height: 65%;">
    </p>
    </details>

&nbsp;

**2\.** Select the **Salesforce** category to assign  

  <details><summary>>>> Click to see a screenshot <<<</summary>
    <p>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\Mobile\iPhone\Contacts\contacts11.png" style="width: 65%; height: 65%;">
    </p>
    </details>

&nbsp;

The Contact will get synced in Salesforce on the following [Sync session](../Synchronization-Engine-An-Overview/) within a span from 1 to 30 minutes.



&nbsp;

##### To stop syncing a Contact

If you later need to stop syncing a Contact, remove the Salesforce category by right-swiping on it.

&nbsp;

&nbsp;

&nbsp;

#### Syncing Outlook Tasks in MS To Do App from iPhone

{{ product_name }} processes to Salesforce <u>only</u> Tasks marked this way, this excludes the risks that your personal Tasks might get synced there from your mobile.

As long as a Task is synced, any updates of the Task on either side get mirrored on the other. To synchronize an MS Outlook Task with Salesforce, you need to assign it to the custom *Salesforce Tasks* list in [Microsoft To Do App](https://apps.apple.com/us/app/microsoft-to-do/id1212616790) installed on your mobile:  

**Method 1: Create a Task in the "Salesforce Tasks" list**


**1\.** Open MS To Do App and tap the "Salesforce Tasks" list on its main screen

  <details><summary>>>> Click to see a screenshot <<<</summary>
    <p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\Mobile\iPhone\Tasks\tasks30.png" style="width: 65%; height: 65%;">
    </details>
&nbsp;

**2\.** Tap **Add A Task** at the bottom, fill in Task details and then tap **Done**

  <details><summary>>>> Click to see the screenshots <<<</summary>
    <p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\Mobile\iPhone\Tasks\tasks31.png" style="width: 65%; height: 65%;">
    <br>
    <br>
    <br>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\Mobile\iPhone\Tasks\tasks32.png" style="width: 65%; height: 65%;">
    </p>
    </details>

&nbsp;

The Task you created will get synced in Salesforce on the following [Sync session](../Synchronization-Engine-An-Overview/) within a span from 1 to 30 minutes.

&nbsp;

&nbsp;

**Method 2. Bulk-move several Tasks to the list**

**1\.** Open MS To Do App   

**2\.** Expand the list that contains the Tasks that you need to sync in Salesforce and tap the **•••** (Actions Menu) icon on the top, then select **Edit**

  <details><summary>>>> Click to see a screenshot <<<</summary>
    <p>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\Mobile\iPhone\Tasks\tasks21.png" style="width: 65%; height: 65%;">
    </p>
    </details>

&nbsp;

**3\.** Mark the Tasks you need to sync in Salesforce by tapping the circles next to them, then tap **Move** in the bottom toolbar

  <details><summary>>>> Click to see a screenshot <<<</summary>
    <p>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\Mobile\iPhone\Tasks\tasks22.png" style="width: 65%; height: 65%;">
    </p>
    </details>

&nbsp;

**4\.** Select the list **Salesforce Tasks**  

  <details><summary>>>> Click to see a screenshot <<<</summary>
    <p>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\Mobile\iPhone\Tasks\tasks23.png" style="width: 65%; height: 65%;">
    </p>
    </details>

&nbsp;

Selected Tasks will get synced in Salesforce on the following [Sync session](../Synchronization-Engine-An-Overview/) within a span from 1 to 30 minutes.


&nbsp;

&nbsp;

**Method 3. Move a single Task to the list**

**1\.** Open MS To Do App  

**2\.** Find the Task that you need to sync in Salesforce and right-swipe on it, then tap on the **🢒≡** (List) icon  

  <details><summary>>>> Click to see a screenshot <<<</summary>
    <p>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\Mobile\iPhone\Tasks\tasks11.png" style="width: 65%; height: 65%;">
    </p>
    </details>
&nbsp;

**3\.** Select the *Salesforce Tasks* list to move the Task there

  <details><summary>>>> Click to see the screenshots <<<</summary>
    <p>
        <img src="..\..\assets\images\Using-SmartCloud-Connect\Mobile\iPhone\Tasks\tasks12.png" style="width: 65%; height: 65%;">
    </p>
    </details>

&nbsp;

Selected Tasks will get synced in Salesforce on the following [Sync session](../Synchronization-Engine-An-Overview/) within a span from 1 to 30 minutes.

&nbsp;

##### To stop syncing a Task

If you later need to stop syncing a Task, remove it from the Salesforce Tasks list.

&nbsp;

&nbsp;

* * *

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

