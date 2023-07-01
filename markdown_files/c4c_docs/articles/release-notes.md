# What's New?

<h2>SAP Cloud for Customer Server-Side Integration:<br>
Latest Release Notes and Knowledge Base Updates </h2>

&nbsp;

### 2304 Release notes

*Released on: April 22, 2023*

&nbsp;

#### 2304 New features and improvements   

**1\.** **Improved the logic of Location data synchronization for Visits**

Improved the general logic of syncing Location data for cases when there are two Location fields for Visit in SAP Cloud for Customer and only one Location field in the mail client calendar. Moreover, if both Location fields in SAP are filled, after sync, both locations will appear in an event Location field in the mail calendar divided by delimiter "**/-/-/**".

Also, ensured that no updates are sent out to the attendees when SSI Sync makes system changes to the event, e.g. adds a delimiter.

<br><br>

**2\.** **Improved "Keep Accounts Read-Only" feature**

Improved the behavior of the "Keep Accounts Read-Only" feature. Now, ensured that no Accounts and their related objects created in MS Outlook get affected by synchronization when the feature is enabled. Previously, SSI Sync could make changes to these records in Outlook to reflect only relevant data from SAP Cloud for Customer.

<br><br>

**3\.** **Optimized implementation of activity sharing process**

Improved system implementation of activity sharing. Now, the linking algorithm is more clear, allowing to resolve and link activity participants without additional or unexpected difficulties.

<br><br>

#### 2304 Bugfixes

**1\.** Ensured that SSI Chrome extension icon do not disappear from the side panel when opening event details in Google Calendar. Previously, SSI icon may be unavailable on the event details dialog after some Google updates.

**2\.** Ensured that the invitation/update is sent out automatically to all meeting attendees in Exchange when you add a new attendee to the corresponding event in SAP Cloud for Customer.

**3\.** Fixed the color of the "SAP Cloud for Customer" category in MS Outlook, ensuring it is green. Previously, an update of some Exchange versions affected the color range and changed the "SAP Cloud for Customer" category color to dark olive.

**4\.** Required Subject field behavior fix: ensured that if the Subject field is required and not filled with data, you are unable to create and save a Ticket via Add-In.

&nbsp;

*The update also includes several minor bugfixes, UX/UI improvements, as well as customer-specific updates.*

&nbsp;

&nbsp;

***

###  2303 Release notes

*Released on: March 18, 2023*

&nbsp;

#### 2303 New features and improvements   

**1\.** **Improved authorization flow to SAP Chrome Extension for Gmail**

Implemented seamless [login process to SAP Chrome extension for Gmail](../set-up-for-gmail/#ssi_google_chrome_extension_setup). Previously, you needed manually copy the TenantURL and paste it into the Chrome extension. Now, during authorization in [User Settings](../How-to-Configure-User/), the system detects your current TenantURL and automatically sets it for your SAP Chrome extension for Gmail.

<div class="admonition warning">
    <p class="admonition-title">Important</p>
    <p>
        <img src="..\..\assets\images\release-notes\2303\accept.png" style="width:53%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
    </p>
    <p>
        Once your SAP Cloud for Customer for Gmail extension is updated to version <b>2302.12.0.51</b>, it will be disabled.<br>
        To re-enable it, accept the additional permissions to read and change your data on all <i>ondemand.com</i> and <i>saphybriscloud.com</i> sites.
    </p>
    <p>
        Note that this affects only already active SSI users
    </p>
</div>

<br><br>

**2\.** **Improved functionality of "Saving this item to SAP..." dialog**

<p><img src="..\..\assets\images\release-notes\2303\save-dialog.png" style="width:37%; display:inline-block; vertical-align:middle; margin-left:15px; float: right"></p>

Now, while saving calendar items via the Add-In, you can select only the record types available in the drop-down list (manual entering is no longer available). This improvement ensures that the relevant event record type will be saved to the SAP Cloud for Customer.

<br><br><br>

#### 2303 Bugfixes

**1\.** Ensured that the Account field is prefilled on a New Phone Call card in the Add-In when creating a record via **Contact card** > <b>&middot;&middot;&middot;&middot;</b> (More) icon > **New Phone Call**.

**2\.** E-mail attachment saving fix: ensured that while saving an e-mail with only one file attached, Add-In handles and saves the attachment to SAP as expected.

&nbsp;

*The update also includes several minor bugfixes, UX/UI improvements, as well as customer-specific updates.*

&nbsp;

&nbsp;

***

###  2302 Release notes

*Released on: February 18, 2023*

&nbsp;

#### 2302 New features and improvements    

**1\.** **Polish and Italian localizations added to Server-Side Integration**

Now, Server-Side Integration supports Polish and Italian user interface localizations in the product. See the full list of available languages and learn more about [SSI localization configuring](../configuring-localization/).

<br><br>

**2\.** **Select where to save attachments in SAP Cloud for Customer**

<p><img src="..\..\assets\images\release-notes\2302\save-att-options.png" style="width:34.88%; display:inline-block; vertical-align:middle; margin-left:5px; float: right"></p>

Now, while saving e-mail with attachments to SAP via the Add-In, you have one extra option where to save the attached files. The new option allows you to save attachments to both the selected SAP object and e-mail in addition to saving only to the SAP object or only to the e-mail.

<br><br>

**3\.** **Pin the Lead object card in the Add-In**

<p><img src="..\..\assets\images\release-notes\2302\pin-lead.png" style="width:39.25%; display:inline-block; vertical-align:middle; margin-left:5px; float: right"></p>

We implemented the possibility to pin the Lead object card in the Add-In to have it at hand and save time on searching for necessary Lead object.

<br><br>

**4\.** **Automatic prefilling of day/time fields for SAP objects in the Add-In**

<p><img src="..\..\assets\images\release-notes\2302\date-time-prefill.png" style="width:36.34%; display:inline-block; vertical-align:middle; margin-left:5px; float: right"></p>

We improved the prefilling of day/time fields for Appointments, Visits, Phone Calls, and Tasks in the Add-In with day and time data according to the user’s calendar time zone. Note that this feature is implemented only for *Start*, *End*, and *Due* date/time fields.

<br><br>

**5\.** **Auto-provisioning users in SAP Cloud for Customer by the e-mail domain name**

We implemented the functionality to auto-provision users by the e-mail domain name. Now, Admins can specify a particular domain name to auto-provision SAP Cloud for Customer users with the same e-mail domain name.

Learn more about [configuring SSI by Admin](../How-to-Configure-Admin/)

<br><br>

#### 2302 Bugfixes

**1\.** Ensured that all Add-In's buttons translations are displayed according to the selected SSI localization.

**2\.** Improved a message shown to users when they save events via the Add-In. Now, the message provides more information on the saving process: "*This item will be saved to SAP at the next synchronization. Please save and close it before synchronization so that the item is linked to selected objects.*"

**3\.** Resolved an issue where the buttons **Blocklist this person** and **Blocklist this e-mail domain** were enabled for the already blocklisted Contacts. Now, these buttons are inactive (greyed out) if a person or domain is in the blocklist.

&nbsp;

*The update also includes several minor bugfixes, UX/UI improvements, as well as customer-specific updates.*

&nbsp;

&nbsp;