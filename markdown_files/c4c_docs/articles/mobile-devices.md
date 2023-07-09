# Using Server-Side Integration on Mobile Devices

&nbsp;

&nbsp;

**[ This article is work-in-progress ]**

&nbsp;

&nbsp;

## General information

Since Server-Side Integration works with the user's MS Exchange mailbox, which can be connected to a mobile device through ActiveSync, the user can partially use some functionality on the mobile device.

User can:

* Access and edit synchronized SAP Cloud for Customer calendar events in a native mobile Calendar application
* Access, edit synchronized SAP Cloud for Customer and create new Contacts, Accounts, and Individual Contacts in a native mobile Contacts application
* Access and edit synchronized SAP Cloud for Customer Tasks in native mobile Reminders application
* Work with Add-In from MS Outlook Mobile application

&nbsp;

* * *

&nbsp;

## Setup MS Exchange account on mobile device

To set up a Microsoft Exchange account on an iOS or Android mobile device or how to install Microsoft Outlook Mobile, follow the Microsoft Support [guidance](https://support.microsoft.com/en-us/office/set-up-office-apps-and-email-on-a-mobile-device-7dabb6cb-0046-40b6-81fe-767e0b1f014f?ui=en-us&rs=en-us&ad=us).

&nbsp;

* * *

&nbsp;

## Using SSI on Android devices

### Open SSI from MS Outlook Mobile

1. Open MS Outlook Mobile App

<p>
<img src= "..\..\assets\images\mobile-devices\android-1.png" style="width: 45%; height: 45%;">
</p>

&nbsp;

2. Open any e-mail from Inbox or Sent items

3. Tap ( &#8942; ) **More** button, as marked on the screenshot below

<p>
<img src= "..\..\assets\images\mobile-devices\android-2.png" style="width: 45%; height: 45%;">
</p>

&nbsp;

4. Tap "SAP" icon to open SSI

<p>
<img src= "..\..\assets\images\mobile-devices\android-3.png" style="width: 45%; height: 45%;">
</p>

&nbsp;

5. You will get the same interface with the same functionality, as in MS Outlook sidebar Add-In

<p>
<img src= "..\..\assets\images\mobile-devices\ios-android-4.png" style="width: 45%; height: 45%;">
</p>

&nbsp;

* * *

&nbsp;

### Work with SAP data through SSI and native Android Apps

#### Contacts

On Android devices, Contacts from a corresponding MS Exchange account can be selected in Contacts App.

<p>
<img src= "..\..\assets\images\mobile-devices\android-contacts-1.png" style="width: 45%; height: 45%;">
</p>

&nbsp;

Shared SAP Cloud for Customer Contacts will have the corresponding labels.

<p>
<img src= "..\..\assets\images\mobile-devices\android-contacts-2.png" style="width: 45%; height: 45%;">
</p>

&nbsp;

&nbsp;

#### Calendar

On Android, SAP Cloud for Customer calendar events will be synchronized into the user’s calendar. On a mobile device, user can edit synchronized events. New events can’t be shared with SAP Cloud for Customer because the native mobile calendar doesn’t work with MS Exchange categories.

In the calendar app interface, it is impossible to distinguish whether a calendar event is synced from SAP Cloud for Customer or not.

As a workaround, user can create an appointment or visit in SSI Add-In through the MS Outlook Mobile app, force sync in the SSI, and, as soon as the sync is completed, the event will appear in the user’s calendar on a mobile device.

&nbsp;

#### E-Mails

User can share e-mails using native mobile apps by moving them into the *SAP E-Mails* folder. After successful sync, the e-mails will be moved back to the Inbox. However, user will not see the status because the native app doesn’t work with MS Exchange categories.

<p>
<img src= "..\..\assets\images\mobile-devices\ios-android-emails.png" style="width: 45%; height: 45%;">
</p>

&nbsp;

***

&nbsp;

## Using SSI on iOS devices

### Open SSI from MS Outlook Mobile

1. Open MS Outlook Mobile App

<p>
<img src= "..\..\assets\images\mobile-devices\ios-1.png" style="width: 45%; height: 45%;">
</p>

&nbsp;

2. Open any e-mail from Inbox or Sent items

3. Tap ( &#8943; ) **More** button, as marked on the screenshot below

<p>
<img src= "..\..\assets\images\mobile-devices\ios-2.png" style="width: 45%; height: 45%;">
</p>

&nbsp;

4. Tap "SAP" icon to open SSI

<p>
<img src= "..\..\assets\images\mobile-devices\ios-3.png" style="width: 45%; height: 45%;">
</p>

&nbsp;

5. You will get the same interface with the same functionality, as in MS Outlook sidebar Add-In

<p>
<img src= "..\..\assets\images\mobile-devices\ios-android-4.png" style="width: 45%; height: 45%;">
</p>

&nbsp;

* * *

&nbsp;

### Work with SAP data through SSI and native iOS Apps

#### Contacts

On iOS, user can access SAP Cloud for Customer Contacts, Accounts, and Individual Customers directly from Contacts App.

1. Open Contacts App on your mobile device
2. Tap "Groups" in the upper left-hand corner

<p>
<img src= "..\..\assets\images\mobile-devices\ios-contacts-1.png" style="width: 45%; height: 45%;">
</p>

&nbsp;

3. Choose your MS Exchange account and select relevant folders

<p>
<img src= "..\..\assets\images\mobile-devices\ios-contacts-2.png" style="width: 45%; height: 45%;">
</p>

&nbsp;

4. Now you can work with SAP Cloud for Customer contacts directly from your mobile device

<p>
<img src= "..\..\assets\images\mobile-devices\ios-contacts-3.png" style="width: 45%; height: 45%;">
</p>

&nbsp;

#### Calendar

On iOS, SAP Cloud for Customer calendar events will be synchronized into the user’s calendar. On a mobile device, user can edit synchronized events. New events can’t be shared with SAP Cloud for Customer because the native mobile calendar doesn’t work with MS Exchange categories.

In the calendar app interface, it is impossible to distinguish whether a calendar event is synced from SAP Cloud for Customer or not.

As a workaround, user can create an appointment or visit in SSI Add-In through the MS Outlook Mobile app, force sync in the SSI, and, as soon as the sync is completed, the event will appear in the user’s calendar on a mobile device.

&nbsp;

#### E-Mails

User can share e-mails using native mobile apps by moving them into the *SAP E-Mails* folder. After successful sync, the e-mails will be moved back to the Inbox. However, user will not see the status because the native app doesn’t work with MS Exchange categories.

<p>
<img src= "..\..\assets\images\mobile-devices\ios-android-emails.png" style="width: 45%; height: 45%;">
</p>

&nbsp;

* * *

&nbsp;

### Add-In localization on iOS devices

The Add-In language in MS Outlook for iOS application is being managed by the device Region settings. You may adjust the Region using the following steps:

1. Go to device **Settings** > **General** > **Language & Region** > **Region**

<p>
<img src= "..\..\assets\images\mobile-devices\ios-localization-1.png" style="width: 45%; height: 45%;">
</p>

&nbsp;

2. Search for the required Region and confirm the Change to the selected region. The MS Outlook app will be restarted automatically, and the Add-In should apply the corresponding language

<p>
<img src= "..\..\assets\images\mobile-devices\ios-localization-2.png" style="width: 45%; height: 45%;">
</p>

&nbsp;

&nbsp;