---
hide_feedback_form: 1
description: Latest Release Notes for RG Email Sidebar and knowledge base updates
---
# What's New?

<h2>Productivity Package & Activity Capture: Latest Release Notes</h2>

<p style="font-size:15px"><i>3 min read</i></font></p>
<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

***

!!! note "Note"
    Also see [this {{ company_name }} Docs article](https://docs.revenuegrid.com/articles/release-notes/) for full {{ company_name }} solution release notes
&nbsp;   


&nbsp; 
***
###  2305 Release notes

*Released on: June 3, 2023* (Fast prod environment)

&nbsp;

#### 2305 New features and improvements    

**1. Auto-select specific file types in the Save dialog** 

Implemented the possibility to automatically preselect specific file types for saving to Salesforce in the Add-In's Save dialog. A new field **Preselect the attachment file types in Save dialog** is added to the Sidebar customization under *Attachments autoselection in Save dialog*.   

<a href="../Customization-Settings-Explained/#attachments_auto-selection" target="_blank">Learn more about files preselection setup...</a>

<img src="..\..\assets\images\Release-notes\2305\preselect.png">

<br><br>

**2. Remove any email addresses and domains from the blocklist** 

Changed the default mechanism for deleting email addresses and domains from the blocklist. Previously, it was impossible to remove the common and internal email domains from the blocklist. Now, such email domains can be removed from the blocklist if necessary.

<a href="../Blocklisting-Email-Addresses-and-Domains/#blocklist_special_considerations" target="_blank">Learn more about the altered deletion mechanism...</a> 

<br><br>

**3. Apply mass actions on the Users page in the new Admin Panel [admin level]**  

All mass actions are now available on the Users tab in the new Admin Panel. When any mass action is in progress, do not close or leave the page because it will cancel the mass action.   
  
<a href="../Customization-Settings-Explained/#attachments_auto-selection" target="_blank">Learn more about managing users in the Admin Panel...</a>

<img src="..\..\assets\images\Release-notes\2305\all-mass-actions.png">

  <br><br>

**4. Specify allowed authentication methods for Revenue Grid [admin level]** 

Ensured that on the login page, end users see only the authentication methods that are configured for their tenant by their admin.  

<br><br>

*The update also includes several minor bugfixes, UX/UI improvements, as well as customer-specific updates.*

<br>

&nbsp; 
***
###  2304 Release notes

*Released on: May 6, 2023* (Fast prod environment)

&nbsp;

#### 2304 New features and improvements    

**1. Login with Salesforce Experience Cloud account** 

Expanded the list of supported Salesforce Experience Cloud domains to facilitate login with this service and ensure seamless integration with RG products. Now, the supported Customer/Partner Community domains are: *force.com, salesforce.com, siteforce.com, my.site.com*.

[Learn more about supported Salesforce editions...](../Supported-Salesforce-Editions/)  

  <br><br>

**2. Connect with your Salesforce Experience Cloud account on the My connectivity page** 

Added the possibility to connect to Salesforce with a Salesforce Experience Cloud account on the *My connectivity* page.   

[Learn more about using My connectivity page...](../Partner-Community-Authorization/#log_in_with_your_customer_partner_community_from_revenue_grid_sync_settings_for_add-in-only_users)

  <br><br>

**3. Automatically save emails in a thread in your Gmail mailbox**  

Implemented the support of auto-saving of emails in a thread for Gmail users. With this functionality, Gmail users can auto-save entire user-selected email communication threads to Salesforce.   
  
[Learn more about using this feature...](../Save-All-Emails-in-a-Thread/)

  <br><br>

**4. Save the event reference number to a designated Salesforce field** 

Implemented an on-demand possibility to save the event reference information (Organizer's email, required attendees, optional attendees, event reference number, original event description) in a designated Salesforce field. By default, this info is saved in the event *Description* field. To change the saving pattern for reference information, submit a corresponding request to [Revenue Grid support team](mailto:support@revenuegrid.com).  

<br><br>  

**6. Save the phone number entered on the Booking Confirmation page to Salesforce**  

Ensured the possibility of saving the Phone number entered by the Book Me link recipient on the *Booking Confirmation* page to the *Phone* field on the auto-created/existing Contact record in Salesforce. 

This functionality is implemented with a new admin-level setting *CalendarAvailabilityAttendeePhoneFieldName* where admins can specify the Salesforce field for saving the phone number entered on the *Booking Confirmation* page. To request this feature, submit a corresponding request to [Revenue Grid support team](mailto:support@revenuegrid.com). 


<br><br>

#### 2304 Bugfixes

**1.** Addressed an issue where the "Event is not saved" status was displayed in the Add-In after users clicked the Save button to save an event to Salesforce. Now, the correct event-saving status is displayed in all cases.  

**2.** Fixed an interface issue with the Hungarian localization where the text on some labels and buttons did not match the design.  

**3.** Ensured that the fields intended for numeric values are correctly checked for the number of characters limitation in the Save dialog in the Add-In.  

**4.** Improved interaction with the Booking confirmation page by ensuring that when a user tries to book a time slot that another user has already booked, and it is not possible to select another slot on this day due to reaching the daily limit of Book Me meetings in the Organizer's calendar, the user will see the corresponding notification with a hint for further actions.   


&nbsp;

*The update also includes several minor bugfixes, UX/UI improvements, as well as customer-specific updates.*

<br>

&nbsp; 
***
###  2303 Release notes

*Released on: April 1, 2023* (Fast prod environment)

&nbsp;

#### 2303 New features and improvements    


** 1. Manage users in the new Admin Panel**

<img src="..\..\assets\images\Release-notes\2303\admin-panel.png" style="width:40%; display:inline-block; vertical-align:middle; margin-left:10px; float: right">
The new Admin Panel is now introduced for all customers. The support of the legacy Admin Panel will be ceased soon, thus we encourage that our customers switch to using the new Admin Panel. 

Read more about <a href="../Managing-Users-via-the-Solution-s-Admin-Panel/" target="_blank">how to manage users in the new Admin Panel...</a>
<br><br><br>

**2. Open the new Sync Settings page from the Add-In's menu**

New Sync Settings page is now available to the prevailing majority of {{ company_name }} users. Click on the Menu icon in the Sidebar and select Sync Settings to open the new page. 

Learn more about <a href="../Configuring-Activities-Synchronization-Settings-rg/" target="_blank">using the new Sync Settings page...</a>

<img src="..\..\assets\images\Release-notes\2303\sync.png" class="minimized">

<br><br>

**3. Limit the number of Book Me meetings per day**

Improved the Book me defaults page: ensured that users can limit the number of Book Me meetings per day in the new field *Maximum allowed events per day for this type of event*. Set the number of Book Me meetings that can be scheduled per day in the corresponding field.

Learn more about <a href="../Sharing-Calendar-Availability-%28Adaptive-view%29/#managing_book_me_defaults" target="_blank">the Book me defaults page...</a>

<img src="..\..\assets\images\Release-notes\2303\max.png" style="width:60%;">

<br><br>

**4. Open the relevant flagged signal from the Sidebar**

Ensured that when users click on the View button on the *New flagged signal* notification in the Sidebar, the corresponding signal page is opened. Previously, the Signals Feed would open. 

Read more about <a href="https://docs.revenuegrid.com/ri/fast/articles/revenue-signals/" target="_blank">Signals in the Sidebar...</a>  

<br><br>  


#### 2303 Bugfixes

**1\.** Add-In layout fix, ensured that notifications are displayed in the Sidebar as designed when its width is around 500 px. 

**2\.** Calendar sharing stability fix: ensured that time slots are displayed correctly for users in -6, -7, -8, etc., time zones. 

**3\.** Removed the unnecessary spaces in the Start and End date/time on the Booking page.  


&nbsp;

*The update also includes several minor bugfixes, UX/UI improvements, as well as customer-specific updates.*

&nbsp;

&nbsp; 

***
###  2302 Release notes

*Released on: February 24, 2023* (Fast prod environment)

&nbsp;

&nbsp;

#### 2302 New features and improvements    


**1. Customize the Booking Confirmation page**  

Implemented customization of the Booking Confirmation page. Now, you can adjust the appearance of the Booking Confirmation page, add necessary elements (pick lists, checkboxes, custom fields, etc.) and make them required or optional. This functionality is managed using the admin setting *BookMeCustomFields*.  

<br><br>  

**2. Sync meetings booked using the Bookings with me feature** 

Implemented seamless syncing of meetings booked with the <a href="https://support.microsoft.com/en-us/office/bookings-with-me-setup-and-sharing-ad2e28c4-4abd-45c7-9439-27a789d254a2" target="_blank">Bookings with me</a> feature in MS Outlook to Salesforce. Previously, syncing of such meetings was not supported.  

<br><br>     

**3. Change the connected Salesforce account by logging out**  

Ensured that when users log out from {{ product_name }}, they can relog in into the Add-In using another Salesforce account and the same mailbox. Previously, such a scenario was impossible without changing the <a href="../change-salesforce-creds/" target="_blank">connected Salesforce account credentials on the Sync Settings page</a>.  

<br><br>    

**4. Select a preferred localization for the new Sync Settings page** 

Implemented the support of localizations for the new {{ company_name }} user interface available for the Add-In users. Now, the following settings pages will be displayed in the language of a user's browser: My Connectivity, Sync, Book me defaults, Raw settings, Profiles, Users, Licenses, Sidebar, etc.  

<a href="../localization/" target="_blank">Learn more about the Add-In's localization</a>  

<br><br>    

**5. Export/import sync settings** 

Implemented the possibility for admins to export/import sync settings for Profiles, Users, Licenses, and Global from/to a file.  

<br><br>    

**6. Improved user registration flow**   

Fine-tuned user registration flow in the Sidebar: now, after clicking on the Continue with Salesforce button (previously, Sign in with Salesforce) on the Add-In's start, a new user will be automatically created and signed in to the Add-In. Previously, new users would face an error in such a scenario.  

<br><br>  

#### 2302 Bugfixes

**1\.**  Booking Confirmation page layout fix: ensured that the time zone and time information are displayed as designed irrelative of the length of the time zone name.  

**2\.** Add-In performance fix: significantly reduced the time of inserting big email templates.  

&nbsp;

*The update also includes several minor bugfixes, UX/UI improvements, as well as customer-specific updates.*

&nbsp;


&nbsp; 
***
###  2301 Release notes

*Released on: January 28, 2023* (Fast prod environment)

&nbsp;

#### 2301 New features and improvements    

**1\.** **See the most important signals right in {{ product_name }}**

<p><img src="..\..\assets\images\Release-notes\2301\flagged-signal.png" style="width:50%; display:inline-block; vertical-align:middle; margin-left:5px;float: right" class="minimized"></p>
Now, you don't have to switch between the emails/events to see the related important (flagged) signals, because they will pop-up as notifications in the Sidebar on their due date.  

When the signal notification appears, you can open the related object in {{ product_name }}, open the {{ company_name }} Signals feed in the web browser, or dismiss the signal. 

Learn more about [using signals in the Sidebar](https://docs.revenuegrid.com/ri/fast/articles/revenue-signals/)

<br><br> 

**2\.** **Easier data filling-in for meeting attendees**  

Now, when a recipient submits their data (email address, name, phone number, and notes) on the Booking Confirmation page at least once, the data is saved in the local browser storage, and if the recipient opens another Book Me/Time Slots link from the same organization, the relevant fields will be automatically prefilled on the Booking Confirmation page.  
The recipient’s information is updated in the local browser storage every time the recipient changes any field values. 

<br><br>  

**3\.** **Made the Reminder and Engagement features available for customers using MS Graph app-only access** 

Added the Mail.Send permission to all shared environments to ensure that the Reminder and Engagement (Sequences) features are supported for customers who use MS Graph app-only access. 
  
Learn more about using [stale-thread reminders](../Stale-Thread-Reminder/) and [Engagement panel](../How-to-Use-the-Solution-s-Engagement-Panel/)

<br><br>  

**4\.** **Implemented a new logic for event attendees syncing enabled on request**

Per the specific customer's request, implemented a 2-way sync of event attendees: when an attendee is deleted in Salesforce, it is deleted in Exchange. This functionality is controlled by a new setting "ServiceEventTrackDeletedAttendees" (default value "0", disabled, "1" - enabled). To request this functionality, submit a corresponding request to our support team. 

Learn more about other [special admin/global settings](../Special-Admin-Panel-Settings/).

&nbsp;


#### 2301 Bugfixes

**1\.** Ensured that the required field "Last name" is highlighted with the red color on the Contact creation page if this field is empty.

**2\.** Resolved an issue that caused endless object card loading after updating the "Description" field on an object card in Quick View and saving the changes. 

&nbsp;

*The update also includes several minor bugfixes, UX/UI improvements, as well as customer-specific updates.*

&nbsp;

***

###  2212 Release notes

*Released on: December 24, 2022* (Fast prod environment)

&nbsp;

#### 2212 New features and improvements    

**1\.** **The Smart Description feature for Tasks is now available for MS Graph users**

We implemented the support of the Smart Description feature for Tasks synchronization for the users of MS Graph. Learn more about using this feature in [this article](../Using-the-Smart-Description-Feature/).
 
<br><br>
**2\.** **Create a calendar item with a MS Teams meeting link right from Salesforce** 

Per the specific customer's requirement, improved the flow of down-syncing the calendar items created in Salesforce with the selected custom *"Create online MS Teams meeting"* checkbox. Now, when such calendar items are saved from Salesforce to MS Outlook calendar, a corresponding calendar item will be created in the user's mail server calendar with an automatically generated link to an MS Teams meeting.
 
 
<br><br>
**3\.** **Added one more scenario for saving emails subject to blocklist exceptions** 

Fine-tuned the email saving via the Add-In: ensured proper email saving if there is at least one non-blocklisted address / domain in a sent / received email, no email address of the sender / recipient is saved to Salesforce as a Lead or Contact, or cannot be associated with any Business record in Salesforce. Learn more about <a href="../Special-Admin-Panel-Settings/#:~:text=%C2%B6-,SalesforceEmailAutoTrackMode,-(default%20value%20%3D%20%E2%80%9C0">strategies used on “not for syncing” blocklist applied on saved emails linking</a>

<br><br>
**4\.** **Expanded the list of Salesforce Partner Communities that can work with {{ short_company_name }} products** 

Per the potential customer's request, we expanded the list of supported Salesforce Partner Community domains to facilitate login with this service and ensure the seamless integration with {{ short_company_name }} products. Due to specific security limitation, companies that would like to work with {{ company_name }} products through Salesforce Partner Community domains, they must send a corresponding request to [{{ short_company_name }} Support Team](mailto:support@revenuegrid.com). Read more about [Customer / Partner Community environment integration specifics](https://docs.revenuegrid.com/ri/fast/articles/Partner-Community-Integration/)

<br><br>
**5\.** **Implemented support of more Salesforce fields for MS Graph users** 

Per the customer's requirement, implemented the support of the *"Profession"* field for MS Graph users and its proper saving to Salesforce.

&nbsp;

&nbsp;


#### 2212 Bugfixes

**1\.** Resolved an issue with logging in to the Add-In with Partner Community link. Now, users of Salesforce Partner Community can seamlessly log in with the Sidebar as expected in such cases.

**2\.** Fixed the cause of the misleading notifications *"Something went wrong. Please refresh the page"* and *"Oops... Something went wrong"* displayed when an admin force started a sync session for a user whose previous sync session was still in progress. Now, a relevant message is displayed in such a scenario.

**3\.** Fixed an issue where the links to Sync Settings and Customization pages opened from MS Outlook running on the Edge Chromium browser or Outlook on the Web in this browser would open in a cropped browser window.


&nbsp;

*The update also includes several minor bugfixes, UX/UI improvements, as well as customer-specific updates.*

&nbsp;

***
###  2211 Release notes

*Released on: November 26, 2022* (Fast prod environment)

&nbsp;

#### 2211 New features and improvements    

**1\.** **Synchronize any folder from your mailbox**

By default, {{ short_company_name }} Sync Engine synchronizes only the emails from the Inbox and Sent folders. But per the specific customer's requirement, we implemented the synchronization of the mailbox Archive folder to Salesforce by adding a new parameter "SyncArchiveFolder" to the setting "ExchAdditionalEmailFolders". You can request the synchronization of the emails from other mailbox folders by submitting a corresponding request to the {{ short_company_name }} Support team.
 
<br><br>
**2\.** **Handle sync issues in the new {{ short_company_name }} Admin panel interface** 

Improved the handling of sync issues by adding this feature in the new {{ company_name }} Admin panel interface. Now, the admins can address any user-specific sync issues in Settings > Administration > Users.

Note that this feature is not yet available to the Add-In-only users.

<p><img src="..\..\assets\images\Release-notes\2211\sync-issues.png" class="minimized"></p>
 
 
<br><br>
**3\.** **Admin panel improvement: more convenient filtering of sync issues** 

Ensured that admins can reset the specific settings within a tenant or organization, reapply them globally for all users, and allow users to modify the settings that were applied globally from the Administration panel in {{ company_name }}.

Note that this feature is not yet available to the Add-In-only users.

&nbsp;

&nbsp;


#### 2211 Bugfixes

**1\.** A Time Slots reliability fix: ensured that users can remove the selected time slots on the booking confirmation page opened on a mobile device.

**2\.** Improved the notifications in the new Administration panel in {{ company_name }}, so now they are more meaningful and user-friendly.


&nbsp;

*The update also includes several minor bugfixes, UX/UI improvements, as well as customer-specific updates.*

&nbsp;
***

###  2210 Release notes

*Released on: October 29, 2022* (Fast prod environment)

&nbsp;

#### 2210 New features and improvements    

**1\.** **New Sync Settings page**

Finished updating the interface of the Sync Settings page to ensure even better usability and convenience. 

For now, the updated Sync Settings page is accessible only from the Revenue Grip web platform. Please, note that the updated Sync Settings page is not yet available to the Add-In-only users. 
[Learn more...](../Configuring-Activities-Synchronization-Settings-rg/)


<p><img src="../../assets/images/Release-notes/2210/new-sync-settings.png" style="width:90%" class="minimized"></p>
 
<br><br>
**2\.** **Select the date and time for your reminders** 

<p><img src="..\..\assets\images\Release-notes\2210\reminder.gif" style="width:35%; display:inline-block; vertical-align:middle; margin-left:1px;float: right" class="minimized"></p>

Now, you can select not only the date when you would like to get a stale thread reminder but also the preferred time for it to pop up. 

 
<br><br><br><br><br><br><br><br><br><br><br><br>
**3\.** **Admin panel improvement: more convenient filtering of sync issues** 

Added the possibility of filtering the relevant events on the Sync Issues list by their Start date. Now, {{ short_name }} Admins can add the Start date column using the drop-down filter menu "Columns" and filter the sync issues accordingly in the admin panel. 

 
<br><br>
**4\.** **Auto-create new Contacts in Salesforce with the pre-filled phone number** 

We added the possibility to auto-create new Contacts in Salesforce with a phone number field prefilled with the phone number provided by the invitee on the Book Me confirmation page.  

 
<br><br>
**5\.** **Historical syncing of emails and calendar items from/to free email domains** 

By default, all free email domains are blocklisted from auto-syncing and records auto-creation, but we implemented an on-demand possibility to run the [historical synchronization](../Historical-Sync-%26-Timezones-Matching/) of the emails and calendar items sent from/to free email domains (gmail.com, yahoo.com, etc.). You can request this feature by submitting a corresponding request to the [{{ short_company_name }} Support team](mailto:support@revenuegrid.com). 


&nbsp;

&nbsp;


#### 2210 Bugfixes

**1\.** Time Slots booking page fix in MS Outlook 2013: ensured that empty slots are displayed as designed

**2\.** Addressed the cause of an issue where the expected time of the next sync session was calculated with 1-minute inaccuracy. Ensured that the correct expected time of the next sync session is displayed


&nbsp;

*The update also includes several minor bugfixes, UX/UI improvements, as well as customer-specific updates.*

&nbsp;
***
###  2209 Release notes

*Released on: October 1, 2022* (Fast prod environment)

&nbsp;

#### 2209 New features and improvements    

<br>
**1\.** **Saving of attached files has become even easier**


<p><img src="..\..\assets\images\Release-notes\2209\attachments.gif" style="width:50%; display:inline-block; vertical-align:middle; margin-left:1px;float: right; margin-top:1rem;"></p>

<br>
Improved the saving of attachments to Salesforce in {{ product_name }}. We removed the "Add file" button in the end of the new item creation page. Instead, now the attachments can be saved by selecting the necessary files on the "Attachments" section at the top of the page 


&nbsp;
&nbsp;
&nbsp;

<br><br><br>

**2\.** **Submit your feedback about {{ product_name }}**


<p><img src="..\..\assets\images\Release-notes\2209\feedback.gif" style="width:50%; display:inline-block; vertical-align:middle; margin-left:1px;float: right; margin-top:1rem;"></p>

<br>
You can effortlessly submit your feedback about {{ product_name }} with two mouse clicks right in the Add-In. Currently, users can report a problem or suggest a new feature by selecting the corresponding option "Give Feedback" on the Add-In's menu



&nbsp;
<br><br><br><br><br><br>

**3\.** **Saving all-day private events in Salesforce**

Added the possibility to save all-day private Google calendar items in Salesforce. 

In the out-of-the-box version of {{ product_name }}, [autosaving of calendar items marked as private](../Saving-Calendar-Items-in-Salesforce-%28Adaptive-view%29/#saving_private_calendar_items) in Salesforce is not supported. However, customers can request private calendar items autosaving if their flow requires that by submitting a corresponding request to [our support team](mailto:support@revenuegrid.com)



&nbsp;

**4\.** **Default location prefilling on booking link creation page**

Improved the usability of Book Me/Time Slots booking by implementing the prefilling of the default rooms on the link creation page. Now, users can set a default location on the *Manage Book Me defaults* page and it will always be automatically preselected in the *Location* field on creating new Book Me / Time Slots links. 

&nbsp;

**5\.** **On-demand possibility to hide Customization and Sync Settings pages**

Per the customer's request, we implemented a possibility to disable the access to sync settings and customization for the customer's employees. With this setting enabled, all the buttons and links leading to Customization and Sync Settings pages are hidden from the Add-In's interface, and the users cannot access them and change any Book Me/ Time Slots and other objects' defaults, etc. 

To request the enabling of this on-demand feature for your organization, contact [{{ company_name }} support team by email](mailto:support@revenuegrid.com)


&nbsp;

&nbsp;


#### 2209 Bugfixes

**1\.** Time Slots booking page fix in MS Outlook 2013: ensured that empty slots are displayed as designed

**2\.** Addressed the cause of an issue where the expected time of the next sync session was calculated with 1-minute inaccuracy. Ensured that the correct expected time of the next sync session is displayed



&nbsp;

*The update also includes several minor bugfixes, UX/UI improvements, as well as customer-specific updates.*
&nbsp;

***

###  2208 Release notes

*Released on: September 3, 2022* (Fast prod environment)

&nbsp;

#### 2208 New features and improvements    


**1\.** **See when the next sync session will run**

We ensured the possibility to see when to expect the applied changes and new objects to be synced in Salesforce. Refer to [this article](../How-the-Solution-Works-and-What-It-Syncs/) for more detailed information about {{ company_name }} sync engine and syncing patterns.

<p><img src="..\..\assets\images\Release-notes\2208\next-sync-will-run-in-not-saved.png" style="width:50%; display:inline-block; vertical-align:middle; margin-left:1px;float: right; margin-top:1rem;"></p>
&nbsp;

* To see when the next sync session will run, select any email, open {{ product_name }}, and hover over the Information icon in the Add-In next to the "*Email isn't saved*" status to see the estimated time when the next sync will take place


&nbsp;

<p><img src="..\..\assets\images\Release-notes\2208\next-sync-will-run-in-saved.png" style="width:50%; display:inline-block; vertical-align:middle; margin-left:1px;float: right; margin-top:1rem;"></p>
&nbsp;

* If the email is already saved, hover over the Information icon in the Add-In next to the "*Email is saved*" status to see the approximate time of the next sync session and the objects to which the Email/Event will be saved in Salesforce (e.g., Lead, Opportunity, Contact)

&nbsp;
&nbsp;
&nbsp;

**2\.** **Link Outlook categories with Salesforce field values**

Per the customer’s request, we implemented the on-demand possibility to link Outlook categories with Salesforce field values. With this feature enabled, the fields on Salesforce objects (events, emails, contacts, and tasks) are set based on the categories assigned in Outlook and vice versa. This feature is available upon request. To enable this feature for your org, contact [{{ short_company_name }} Support team](mailto:support@revenuegrid.com).

&nbsp;


**3\.** **Change the status of a deleted event instead of removing it from Salesforce** 

We implemented an on-demand possibility to preserve in Salesforce the calendar items if they are deleted or canceled in Outlook. With this feature enabled, if a calendar item is deleted or canceled in Outlook, it is still preserved in Salesforce with the status "*Cancelled*," and the cancellation reason changes to "*Customer Cancelled*". In this way, it is possible to keep track of all events, including the deleted ones.

&nbsp;

**4\.** **Track unanswered emails with reminders and signals**

Improved the tracking of unanswered emails: now, if you set a [reminder for an email thread](../Stale-Thread-Reminder/), additionally, a signal is automatically created. On the due date, you will get an email notification reminding you to follow up on an unanswered email in this email thread, as well as a signal in the {{ product_name }} to ensure that this action is not omitted or missed. Learn more about [Revenue Signals] and how to [manage them in the Add-In].

&nbsp;

**5\.** **Blocklisting is now available in the new {{ short_company_name }} Settings interface**

{{ company_name }} offers an automatic saving of Emails, Meetings/Appointments, and Contacts in Salesforce. To prevent the saving of items not intended to be saved in Salesforce, you can add the email addresses or email domains to Blocklist either in [{{ product_name }}](../Blocklisting-Email-Addresses-and-Domains/) or right on the {{ company_name }} Settings web page.

<details><summary>Click to see an animation</summary>
<p><img src="..\..\assets\images\Release-notes\2208\blocklisting-new-rg-settings.gif" class="minimized"></p>
</details>
&nbsp;

&nbsp;

**6\.**  **Linking Rules page added to the new {{ short_company_name }} Settings page**

Previously [linking rules](../Configuring-Activities-Synchronization-Settings/#linking_to_opportunities) were only available in the {{ product_name }}. In this release, this feature has been added to the new Settings interface in {{ company_name }} web platform to ensure even more convenient Opportunities linking.

<details><summary>Click to see an animation</summary>
<p><img src="..\..\assets\images\Release-notes\2208\linking-rules-new-rg-interface.gif" class="minimized"></p>
</details>
&nbsp;

&nbsp;


#### 2208 Bugfixes

**1\.** Fixed a spontaneous issue where on adding time slots for generating a link for sharing calendar availability, the selected slots in the calendar would appear displaced. Now the selected slots are always displayed as designed

**2\.** Fixed an issue where it was impossible to create a Signal with the Due date from the past. Now, Signals can be seamlessly created with any dates from the past and future

**3\.** Another improvement of the Book Me/ Time Slots feature UI/UX: now when all slots in the provided time span are occupied, the relevant notification is displayed to the invitee

&nbsp;

*The update also includes several minor bugfixes, UX/UI improvements, as well as customer-specific updates.*


&nbsp;
***
&nbsp;

###  2207 Release notes

*Released on: July 30, 2022* (Fast prod environment)

&nbsp;

##### 2207 New features and improvements    

**1\.** Per the customer's request, we added the possibility to control who receives notifications about sync errors. Now, admins can exclude end-users from the list of recipients so they don't get excessive/unnecessary notifications      
  
  
**2\.** Improved the design and usability of the *General* tab on the {{ short_company_name }} Sync Settings page: now users can conveniently manage the synchronization of different items (turn on/off, see the sync direction, etc.) on one page  

<details><summary> >>> Click to see a screenshot <<< </summary> 
<p><img src="..\..\assets\images\Release-notes\sync-settings-general.png" class="minimized"></p>
</details>
&nbsp;

**3\.** Improvement of {{ company_name }} Settings use convenience: now all relevant information about sync issues is available in one place – on the *Issues* tab in {{ short_company_name }} Sync Settings. The users can see the first occurrence date for a specific issue, object type, sync direction, object name, error message and easily contact the {{ short_company_name }} support team with the *"Help me resolve this issue"* button  

<details><summary> >>> Click to see a screenshot <<< </summary>  
<p><img src="..\..\assets\images\Release-notes\sync-settings-issues.png" class="minimized"></p>
</details>
&nbsp;

**4\.** Added the possibility to create new Signals right from {{ product_name }} without the need to switch between email service and {{ short_company_name }} interfaces. On the *New Signal* page, users can specify the Signal's title, due date, related object, owner, and description. [Learn more…]( ../revenue-signals/#create_a_new_signal_from_rg_email_sidebar)  

<details><summary> >>> Click to see a screenshot <<< </summary>  
<p><img src="..\..\assets\images\Release-notes\new-signal.png"style="width: 50%; height: 70%;"></p>
</details>
&nbsp;
  
**5\.** Implemented the possibility to see when each user synchronized last time to improve the mass synchronization processes and troubleshooting. Now, in the Admin panel, {{ short_name }} Admins can add the Last Synchronization Session column using the drop-down filter menu *"Columns"* on the *"Users"* tab and sort the relevant events on the Sync Issues list by their Last Synchronization Session.  
  
<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Release-notes\last-sync-session.png"></p>
</details>
&nbsp;

**6\.** Per the customer's request, we implemented the possibility to distinguish between synced inbound and outbound emails. Now synchronized inbound emails are marked with *"In"* in the email subject, while synchronized outbound emails are marked with *"Out"* in the email subject

&nbsp;

##### 2207 Bugfixes

**1\.** Ensured that Customization errors are now automatically resolved 5 min after they occurred. Now, the user does not necessarily need to take any manual actions to proceed using {{ product_name }}    
  
**2\.** Minor Book Me, Time Slots fields improvement: ensured that on the first click on Save to SF Record, Save to Lead, or Contact fields, the forms are displayed as designed    
  
**3\.** Fixed the issue where Book Me/ Time Slots feature wouldn't support America/Fort_Wayne time zone. Now, sharing calendar availability feature works as expected with all time zones


*The update also includes several minor bugfixes, UX/UI improvements, as well as customer-specific updates.*

&nbsp;

&nbsp;

###  2206 Release notes

*Released on: July 2, 2022* (Fast prod environment)

&nbsp;

##### 2206 New features and improvements    

**1\.** Per customers' requests, we implemented support for Salesforce Lightning templates use in {{ product_name }}. Now, after clicking on the “Templates” button in the Sidebar, the users can choose what templates to see in the field “Template folder”: Salesforce Classic message templates or Lightning Experience email templates. [Learn more about using email templates in {{ product_name }}](../Using-Salesforce-Templates/) 

**2\.**  Implemented the possibility to manage {{ company_name }} Signals through {{ product_name }}. Now, the relevant Signals are displayed in {{ product_name }} for emails/events in read/compose modes, and users can manage them right from their email service client (mark a signal as Done/Dismissed, copy the signal link, open in Salesforce). Learn more about [using Revenue Signals right from your {{ product_name }} interface](../revenue-signals/)

**3\.** Per the customer's requirement, we implemented "SQL Server Always Encrypted" for both Add-In and Sync data transfers to encrypt secrets with a key possessed by the customer      

**4\.** Per the customer’s request, we improved Admin panel Sync issues troubleshooting by adding the possibility to track the date when a particular event Sync issue first occurred 

**5\.** We implemented the possibility to filter the relevant events on the Sync Issues list by their Start date. Now, in the Admin panel, {{ short_name }} Admins can add the Start date column using the drop-down filter menu "Columns"    

  
&nbsp;

##### 2206 Bugfixes

**1\.** Improved the look of the Book Me/Time Slots dialogs by adding field borders to *Attendees (required)*, *Attendees (optional)*, and *Slots* fields    

**2\.** A minor Sidebar consistency UX fix: ensured that the “Inserting…” loader notification disappears as expected after an email template is inserted    

**3\.** Fixed the issue where after automatic log out from the [Chrome extension](../Chrome-Extension-Intro/), the users were requested to log in back to Google for multiple times and grant the required permissions

**4\.** Fixed an issue where it was impossible to insert Salesforce email templates which have no Subjects into emails; we ensured that Lightning Experience email templates without subjects can be inserted, as designed


*The update also includes several minor bugfixes, UX/UI improvements, as well as customer-specific updates.*

&nbsp;

&nbsp;

###  2205 Release notes

*Released on: June 4, 2022* (Fast prod environment)

&nbsp;

##### 2205 New features and improvements    

**1\.** Per a potential customer's request, we implemented the possibility to auto-sync items located in custom mailbox folders/subfolders, all subfolders of the Inbox folder. [Learn more...](../Saving-Emails-in-Salesforce-1.-Function-Overview/#under_the_hood_mechanisms_and_special_patterns_applied_on_emails_saving/)   

**2\.** A minor backend improvement for the Book Me feature: we extended Book Me confirmation notification with additional fields *ServerSyncUserId*; Notes; *Location*; *OrganizerTimeZone*; Phone. [Learn more...](../Sharing-Calendar-Availability-%28Adaptive-view%29/)

**3\.** Per the customer's requirement, we implemented an advanced records search mechanism, where [Search By](../Using-the-Search-by-List-Customization-Setting/) may be used for a combination of fields (tags)      

**4\.** Per the customer's requirement, we implemented the following [search system](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-(Adaptive-view)/) improvements: added the function Search by object type and the button *Show more*. [Learn more...](../Using-the-Search-by-List-Customization-Setting/)  

**5\.** An [Auto-save all emails in a thread](../Save-All-Emails-in-a-Thread/) feature improvement based on customers feedback: implemented passing of special values from email fields populated by the users in Save dialog to all subsequent synced emails. [Learn more...](../Save-All-Emails-in-a-Thread/#specific_use_nuances)

**6\.** [Sync Settings](../Configuring-Activities-Synchronization-Settings/) > My Connectivity page improvement: to ensure that the users react to Sync connectivity loss, now the page shows a "Status: Lost" icon in the main menu if a Sync Connectivity problem occurred    

**7\.** Per a customer's requirement, now when the ["Disregard organizer's calendar" checkbox is selected in the Book Me dialogue](../Sharing-Calendar-Availability-(Adaptive-view)/), any meetings booked by link recipient(s) will be marked in the Organizer's calendar as Free    

**8\.** Based on a customer's request, we implemented support for [Gmail box aliases](https://support.google.com/a/answer/33327?hl=en), now {{ short_name }} recognizes them and processes relevant data seamlessly

  

&nbsp;

##### 2205 Bugfixes

**1\.** Recurring Salesfoce Events syncing consistency fix: ensured that the "Can't find specified timezone" error no longer occurs on handling Events set in the newly added Salesforce timezones    

**2\.** Fixed a Sidebar UX consistency issue, where the [Reminder section](../Stale-Thread-Reminder/) was collapsed by default and its preferred state was not remembered. Now it works as designed    

**3\.** Ensured that Gmail box aliases are handled as expected for {{ short_name }} users connected via [Google Impersonated Access](../Gmail-Service-Account/)


*The update also includes several minor bugfixes, UX/UI improvements, as well as customer-specific updates.*

&nbsp;

&nbsp;


###  2204 Release notes

*Released on: April 30, 2022* (Fast prod environment)

&nbsp;

##### 2204 New features and improvements

**1\.** Due to a change in Google resources access permissions system, it is no longer possible to exclude any access types from {{ short_name }} permissions granting. The corresponding permissions dialog was adjusted accordingly [Learn more...](../How-to-Set-Up-the-Chrome-Extension-for-Salesforce-and-Gmail/#2_sign_in_to_gmail_and_grant_rg_email_sidebar_permission_to_work_with_your_gmail_and_google_calendar_data)

**2\.** To improve involved APIs' performance, we implemented automatic clean up of engagement tracking logs in the DB after a certain period. [Learn more...](../How-to-Use-the-Solution-s-Engagement-Panel/#engagement_data_logging_in_salesforce)

**3\.** As a part of the overall Sync Settings overhaul, we changed the design of the Sync control buttons, making them more streamlined

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sync-Settings\sync-buttons-upd.png" class="minimized">
</p></details>


**4\.** Another Book Me functional improvement based a customer's request, we implemented an optional possibility to make the system treat Tentative slots as Free instead of Occupied. This mechanics is managed Org-wide or for individual users, via the global setting *ShowTentativAsBusy*. [Learn more...](../Sharing-Calendar-Availability-%28Adaptive-view%29/)

**5\.** We made [{{ short_name }} Customizations](../Managing-Email-Sidebar-Customizations/) management smoother, by implementing seamless Customization saving and pushing, no Add-In restart is required anymore

&nbsp;

##### 2204 Bugfixes

**1\.** Fixed an issue with timezones recognition for synchronized recurring Salesforce events that was causing an error "*Can`t find specified timezone:*"

**2\.** We improved the compatibility of [{{ short_name }} for Gmail](../Using-the-Solution-for-Salesforce-and-Gmail/) with Mixmax and Boomerang extensions installed in Chrome to ensure flawless workflow 

**3\.** Ensured that notification pop up headers for *Success*, *Warning*, *Error*, *Info* are also translated into other languages, as expected

*The update also includes several minor bugfixes, UX/UI improvements, as well as customer-specific updates.*

&nbsp;

&nbsp;


### 2203 Release notes

*Released on: April 11, 2022* (Fast prod environment)

&nbsp;

##### 2203 New features and improvements

**1\.** Based on a customer's request, we implemented the possibility to configure {{ short_company_name }} Meeting Scheduler scenarios (Book Me, Time Slots) integration with custom-built external applications via dedicated APIs. [Learn more...](../Scheduler-API-Endpoints/)  

**2\.** Per the customers' requests, we implemented [mass pushing of a Customization](../Managing-Email-Sidebar-Customizations/#pushing_your_customization_to_other_users_in_your_salesforce_org) by the Admin on the Org level, so new provisioned end users also get it right away. We've also added an extra informative dialog with a mass push confirmation request  

**3\.** Implemented an optional "Only work with Calendar items" {{ product_name }} usage scenario 

&nbsp;

##### 2203 Bugfixes

**1\.** Implemented the missing connectivity type ["Impersonated access"](../Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/) for "E-mail configuration" >"My connectivity" on the updated [Sync settings page](../Configuring-Activities-Synchronization-Settings/)

**2\.** Also ensured that error notifications on the updated "My Connectivity" page include error codes information from connected systems, whenever they are retrieved

**3\.** Ensured that the preferred expanded/collapsed state of Book Me / Time Slots dialogs' fields is saved and applied each time the users open the dialogs  

**4\.** Another UI improvement of the updated "My Connectivity" page: ensured that the page's widgets move down on page scaling  

*The update also includes several minor bugfixes, UX/UI improvements, as well as customer-specific updates.*

&nbsp;

&nbsp;

### 2202 (Spring 2022) Release notes

*Released on: March 19, 2022* (Fast prod environment)

Also includes [2111 HF1 and HF2 improvements and bugfixes](../Release-Notes/#2111_hf1_and_hf2_release_notes).  

&nbsp;

#### 2202 New features and Improvements

**1\.** Added new controls to open [{{ company_name }}](https://docs.revenuegrid.com/) settings from Email Sidebar: A. Instead of the old Customization page, the button "Customization" now leads to {{ short_company_name }} settings; B. renamed the button "Open {{ company_name }}" to "Open {{ company_name }} in browser"; C. made the "Open {{ company_name }} in browser" button always available  

**2\.** Sync Engine Email Server connectivity settings tab was moved to {{ company_name }} environment, as a tab "My connectivity". It has the same functions for O365 (OAuth), Gmail (OAuth), Exchange (credentials entry dialog), the look was redesigned to boost usability. MS Exchange logon config dialog as well as Impersonation status have also been moved to a dedicated tab on {{ company_name }} settings web page  

**3\.** We've enhanced the design of Email Sidebar pop-up notifications, making them look more sleek. In addition, now it is possible to copy notification texts to find error solutions online  

**4\.** Per a customer's request, implemented optional strict CRM records search on Emails capturing: retrieval of "equals" results only instead or "similar" results for linking, managed by global settings *SearchMode*, *SearchCase*  

**5\.** We've extended {{ short_company_name }} API capabilities to allow creating meetings with attendees in addition to appointments over API. [Learn more...](../Scheduler-API-Endpoints/)  

**6\.** Per a customer's request, re-arranged Book Me generation dialog fields, increasing the feature's user friendliness  

**7\.** Book me dialog improvement: based on customers' feedback, made the name of the checkbox used to exclude parsing of organizer's calendar more intuitive ("Disregard organizer's calendar") and improved the tooltip; also changed its location in the dialog  

**8\.** Implemented an optional setting that allows disabling meeting notes/invitee phone sync entered at the Booking page to the resulting Event, to meet specific customers' requirements  

**9\.** Based on the customers' requests, we implemented support for more phone number formats in the Sidebar, ensuring that formats with less than 12 digits like European ones also get processed correctly  

&nbsp;

&nbsp;

#### 2202 Bugfixes

**1\.** Fixed a specific issue where a pre-defined status "Completed" was not assigned to Tasks created via "Log a Call'. Now that is performed as designed  

**2\.** Fixed an issue where the "MS Teams" location item was available in the Time Slots / Book Me dialog for users who do not have MS Graph connectivity and thus cannot use it. Now it's no longer present there

**3\.** Fixed an issue where an incorrect domain name was shown in the [*Suggested New Records* section](../Create-New-Records/#the_suggested_records_tab) for selected emails. Now a relevant domain name is displayed there, as designed

*The update also includes several minor bugfixes, UX/UI improvements, as well as customer-specific updates.*

&nbsp;

&nbsp;

### 2111 HF1 and HF2 Release notes

*Released on: January 30, 2022* (Fast prod environment)

&nbsp;

##### 2111 HF1 and HF2 New features and improvements

**1\.** In Book Me and Time Slots dialogs, the *MS Teams* item for Teams meeting room links auto-generation is now readily available, at the top of the Location picklist. Only available for O365 MS Graph connectivity or Hybrid connectivity. [Learn more...](../How-to-Send-Meeting-Time-Slots-%28Adaptive-view%29/#ms_teams_integration_on_location_selection)

**2\.** Based on the customers' requests, we've re-introduced the image previewing feature in [attachments handling dialogs](../Attachments-Handling-%28Basic%29/#saving_email_attachments). To preview an image attached to an email: click the **👁** (Preview) icon next to it

**3\.** Based on the customers' requests, we implemented support for more phone number formats in the Sidebar, ensuring that formats with less than 12 digits like European ones also get processed correctly

**4\.** Implemented a setting that allows disabling meeting notes and invitee's Phone # conveying to an Event created with Book Me or Time Slots, to meet specific customers' requirements

&nbsp;

##### 2111 HF1 and HF2 Bugfixes

**1\.** Fixed a specific issue where a pre-defined status "Completed" was not assigned to Tasks created via [Log a Call](../Log-A-Call/#how_to_log_a_call_in_salesforce). Now that is performed as designed

**2\.** Fixed the cause of an issue where the Status field did not get prefilled for new Tasks according to special *DefaultsForCreate* settings

&nbsp;

&nbsp;

### 2111 (Winter 2022) Release notes

*Released on: December 4, 2021* (Fast prod environment)

&nbsp;



**Note:** this major release also includes 2108 HF1 and HF2 improvements, see their descriptions in the section underneath

#### 2111 New features and Improvements

Also see a video summary: <https://vimeo.com/652890150>



##### Meeting Scheduler (Book Me, Time Slots) improvements

**1\.** Per a customer's request, we optimized the layout of Book Me generation dialog fields, increasing the feature's user friendliness. [Learn more...](../Sharing-Calendar-Availability-%28Adaptive-view%29/#then_fill_in_the_optional_meeting_parameters_hidden_under_the_advanced_options_tab)

**2\.** We've further improved Book Me availability loading performance through backend optimization. We've also removed the Switch to Old View button from the Booking Page

**3\.** Another Booking page improvement: now Book Me link recipients (invitees) have the possibility to choose their preferred meeting Duration among several alternatives. There are up to 3 duration options specified by the organizer, the shortest option is default. [Learn more...](../Sharing-Calendar-Availability-%28Adaptive-view%29/#setting_alternative_meeting_durations)

**4\.** Next Book Me feature improvement: implemented an optional possibility to allow Book Me link recipients to [invite additional attendees to booked meetings](../Sharing-Calendar-Availability-%28Adaptive-view%29/#then_fill_in_the_optional_meeting_parameters_hidden_under_the_advanced_options_tab), by listing their email addresses during slot selection. This is required by some customers' business communication flows. The setting that manages this feature was put in [Add-In Customization settings](../Customization-Settings-Explained/)

**5\.** Time Slots Booking page got redesigned. We made it simpler and more straight-forward

**6\.** Another important Book Me feature improvement. For different reasons, some companies require to set Book me links' lifespan; we implemented this possibility as a [Special Admin setting](../Special-Admin-Panel-Settings/#extra_configuration_settings) *BookMeLinkExpirationPeriod*

**7\.** Per a customer's request, implemented an optional possibility to exclude own availability from parsing on Book Me links generation. [Learn more...](../Sharing-Calendar-Availability-(Adaptive-view)/)

**8\.** MS Teams integration improvement for Book Me / Time Slots: implemented the possibility to auto-generate Teams meeting room links for meetings initiated via {{ short_name }} Meeting Scheduler. Now it also works for Office 365 mailboxes configured via hybrid [MS Graph](../MS-Graph/)-[Exchange Web Services](../Working-With-EWS/) connectivity 

**9\.** {{ short_name }} Meeting Scheduler consistency improvement for coworkers' calendars displaying: ensured that internal attendees' working hours are indicated on the Booking page

**10\.** A minor Book Me dialog user friendliness improvement: re-worked Attendees list functioning to match Time Slots Attendees list  

**11\.** Starting on December 1 we've replaced the list of {{ product_name }} IPs which customers should whitelist in their corporate firewall to run the solution. [Learn More...](../Overcoming-Firewall-Issues/#november_2021_revenue_grid_resources_ip_update) 

&nbsp;

##### Other improvements

**1\.** Conditional un-syncing: to meet certain CRM calendars capture flow requirements, implemented the following optional configurable Calendars sync feature: depending on the value in a specific Event field, the Event gets un-synced from email client's calendar but remains in Salesforce. The feature is managed by the special setting *SalesforceEventUnsyncConditions*. See the description in [this article](../Special-Admin-Panel-Settings/#conditional_events_un-syncing). A sample use case: after a Case gets closed, its associated Event's status is changed to ‘vacated’ and the Sync Engine removes the matching item from end users' mailbox calendars

**2\.** The following language localizations are planned to be added in mid-December 2021: 

- Italian 
- Korean (South Korea)
- Portuguese (Portugal)
- Chinese (traditional)
- Czech

**3\.** A minor "Save Event" dialog usability improvement for {{ short_name }} MS Outlook Add-In: implemented relevant Account pre-selection in the ["Save Event" dialog](../Save-Email-Dialog/#save_event_dialog) if the Save button was clicked on a specific Contact in the [Sidebar](../Introduction/)

**4\.** Added {{ company_name }} animated logo to [{{ short_name }} Outlook Add-In's](../Introduction/) loading screen

**5\.** {{ short_name }} Admin panel users management got enhanced with several more bulk config actions . [Learn more...](../Managing-Users-via-the-Solution-s-Admin-Panel/#actions_with_users)

&nbsp;

&nbsp;

##### 2111 Bugfixes

**1\.** Fixed an issue where the notification regarding Customization update was not displayed in the Sidebar after Customization saving. Now the notification is displayed as expected

**2\.** Improved the performance of [initial data parsing](../Initial-Search-and-Applied-Record-Filters/) by the Add-In: implemented parallel search by emails and Account search

**3\.** Fixed an issue where [Book Me](../Sharing-Calendar-Availability-%28Adaptive-view%29/) / [Time Slots](../How-to-Send-Meeting-Time-Slots-%28Adaptive-view%29/) could not be used via [Delegated calendar access](../Using-MS-Outlook-Delegated-Calendars/). Now Delegates with "Can Edit" rights can create Book Me / Time Slots links for calendar Delegators, as designed

**4\.** Ensured that the *field Importance* setting on Customization page is processed correctly on settings saving

**5\.** Boosted the performance of Engagement grouped clicks/opens backend data handling for [{{ company_name }} Sequences](https://docs.revenuegrid.com/articles/about-sequences/)

*The update also includes several minor bugfixes, UX/UI improvements, as well as customer-specific updates.*

&nbsp;

* * *

&nbsp;

### {{ product_name }} 2108 (Fall 2021) Release notes



#### 2108 Hotfix 2

*Released on: November 1, 2021* (Fast prod environment)

##### 2108 Hotfix 2 New features and improvements

**1\.** Based on several requests, we increased the expiration date for [generated Time Slots links](../How-to-Send-Meeting-Time-Slots-(Adaptive-view)/) from 14 days to 60 days after generation date, for all users





##### 2108 Hotfix 2 Bugfixes

**1\.** Fixed a localization issue, where translations were not applied for some card headers in [{{ product_name }}](../Introduction/)

**2\.** Ensured that [Sync engine](../Synchronization-Engine-An-Overview/) no longer stops on attempting to process 20000 new Contacts within Sync scope

&nbsp;



#### 2108 Hotfix 1

*Released on: October 6, 2021* (Fast prod environment)

##### 2108 Hotfix 1 Bugfixes

**1\.** Resolved an encoding issue with {{ short_company_name }} Sync Engine where special German language characters got corrupt on emails saving via [{{ short_company_name }} Sync](../Synchronization-Engine-An-Overview/)  

**2\.** [Sidebar UI/UX](../Introduction/) consistency fix: resolved an issue where the "Event will be saved" notification was displayed in {{ short_company_name }} Sidebar's header instead of "Event is saved" after performing any search action  

**3\.** Add-In Danish localization: discovered several missing component translations and added them



&nbsp;

&nbsp;

#### 2108 New features and Improvements

*Released on: September 04, 2021*  (Fast prod environment)

**1\.** Added support for [Tasks and Contacts syncing](../Onboarding-Tasks/) over [MS Graph connection](../MS-Graph/) for Office 365 accounts 

**2\.** Implemented support for [mass Sync activation](../Mass-Deployment-of-the-Add-In-Office-365/) via [Impersonating service account](../Impersonation-O365/) for [MS Graph connection](../MS-Graph/). [This article](../Impersonation-Graph/) contains instructions on how to confiture it  

**3\.** Implemented an [Add-In Customization option](../Customization-Settings-Explained/) for marking specific object fields as "*Force Required*". A Force Required field is handled as mandatory for filling in when [creating](../Create-New-Records/) or [modifying items via {{ short_company_name }} Sidebar](../All-User-Actions-in-Add-In-Sidebar/). See [this article](../Customization-Settings-Explained/#mark_fields_as_force_required) for more information 

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\User-Settings\Customization\Force-Required.png" class="minimized">
</p></details>


&nbsp;

**4\.** Implemented an optional possibility to up-sync MS Exchange [resource rooms](https://docs.microsoft.com/en-us/microsoft-365/admin/manage/room-and-equipment-mailboxes?view=o365-worldwide) calendars as Salesforce [conference rooms (public calendars)](https://help.salesforce.com/s/articleView?id=sf.customize_groupcal.htm&type=5&language=en_US)  

**5\.** Implemented [User Sync settings](../Configuring-Activities-Synchronization-Settings/) or [{{ company_name }} Admin panel](../How-to-Log-In-to-the-Admin-Panel/) logging in over [Gmail OAuth 2.0](https://developers.google.com/identity/sign-in/web/sign-in) besides standard logging in over [Salesforce OAuth 2.0](https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_flows.htm&type=5) or [Exchange/Office 365 OAuth 2.0](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow) 

**6\.** Added a [Global setting](../Special-Admin-Panel-Settings/#extra_configuration_settings) for optional disabling of email Body field saving to Salesforce for at all email saving scenarios, for special business flows that exclude email Bodies saving to Salesforce  

**7\.** [Book Me](../Sharing-Calendar-Availability-(Adaptive-view)/) / [Time Slots](../How-to-Send-Meeting-Time-Slots-(Adaptive-view)/) usability improvement: per several customers' requests, implemented the possibility to configure default values to be auto-filled in Book me and Time Slots dialogs. See [this article](../How-to-Send-Meeting-Time-Slots-%28Adaptive-view%29/#time_slots_dialog_auto-filling) for details    

**8\.** Now Book me and Time Slots can also be configured to be used in [delegated access calendars](../Using-MS-Outlook-Delegated-Calendars/) and other scenarios with [granted Editor permissions](https://support.microsoft.com/en-us/office/allow-someone-else-to-manage-your-mail-and-calendar-41c40c04-3bd1-4d22-963a-28eafec25926)  

**9\.** Another Time Slots / Book Me improvement: ensured that meeting Organizer can get invitees' meeting detailing Notes and optionally their Phone numbers entered in [the Booking page](../Sharing-Calendar-Availability-%28Adaptive-view%29/#how_to_book_a_slot_recipient_side) in generated confirmation email, by adding two dedicated fields to the Booking page. See [this article](../Sharing-Calendar-Availability-%28Adaptive-view%29/#the_extra_fields_phone_number_and_notes) for complete information  

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sharing-Calendar-Availability-(Adaptive-view)\extra-fields.png">
</p></details>

&nbsp;

**10\.** Meeting Scheduler Booking page performance got improved; now [the Booking page](../Time-Slots-Gmail/#how_to_book_a_slot_recipient_side) loads and refreshes considerably faster  

**11\.** Added an optional possibility to prevent email server-originating updates to be applied for *Read only* Salesforce Events by [{{ short_name }} Sync engine](../Synchronization-Engine-An-Overview/)  

**12\.** Improved loading screens and notifications displayed on product [Customization settings](../Customization-Settings-Explained/) updates  

**13\.** Now Meeting Scheduler features (Book Me and Time Slots) can be used for [MS Exchange / Office 365 Shared calendars](https://docs.microsoft.com/en-us/outlook/troubleshoot/calendaring/how-to-share-calendar-and-contacts#outlook). See [this article](../How-to-Send-Meeting-Time-Slots-%28Adaptive-view%29/#shared_calendars_compatibility) for details

**14\.** Implemented an optional possibility to get new created Salesforce Events instantly down-synchronized to email client's calendar. See [this article](../Synchronization-Engine-An-Overview/#salesforce_calendar_email_client_calendar_insta-sync) for complete information.

&nbsp;

&nbsp;

#### 2108 Bugfixes

**1\.** Ensured that [Sync engine](../Synchronization-Engine-An-Overview/) no longer fails on attempting to [process](../Synchronization-of-Contacts/) over 20000 Contacts within Sync scope

**2\.** Fixed a [Sidebar](../Introduction/) issue in Outlook on the Web, where info bar notification was not displayed after "Quick Save" icon clicking. Now Quick Save status is displayed as designed  

**3\.** [Sync re-activation](../Authorizing-Sync-Engine-to-Work-with-Your-Data/) use friendliness fix: ensured that [Sync engine](../Synchronization-Engine-An-Overview/) gets started automatically after its re-activation via the "Provide access to  Office 365" dialog in the [Sidebar](../Introduction/)



*The update also includes several minor bugfixes, UX/UI improvements, as well as customer-specific updates.*

&nbsp;

* * *

&nbsp;

### {{ product_name }} 2105 (Summer 2021) Release notes

&nbsp;

#### 2105 Hotfix 1

*Released on: July 4, 2021*  (Fast prod environment)

&nbsp;

##### 2105 Hotfix 1 New features and Improvements

**1\.** Added a unique optional possibility to link multiple [Business Records](https://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) to Events saved in Salesforce [via {{ product_name }}](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/); this multilinking function is not available in Salesforce out-of-the-box.  
This feature requires [{{ company_name }} Salesforce managed package installation](../Admin-Managed-Package/) and can be enabled upon request  

**2\.** [Time Slots](../How-to-Send-Meeting-Time-Slots-(Adaptive-view)/) / [Book Me](../Sharing-Calendar-Availability-(Adaptive-view)/) usability improvement: ensured that meeting Organizers see any special Notes added by the invitees who accepted the meeting in the resulting calendar notification's *Description*  

&nbsp;

*The update also includes several minor bugfixes, UX/UI improvements, as well as customer-specific updates.*

&nbsp;

&nbsp;

#### 2105 Major update

*Released on: May 29, 2021*  (Fast prod environment)

&nbsp;

#### 2105 New features and Improvements



**1\.** Add-In loading and operations boost: improved different Add-In functions performance by  excluding pre-loading of extra properties and functions:  

- Add-In loading speed was increased by over 25%
- Different non-core [Add-In functions](../Introduction/) (route components) are now loaded on-demand: Add-In cache selectively loads features when they are required by the user  

&nbsp;
**2\.**  A [Google Calendar Sync](../Using-the-Solution-for-Salesforce-and-Gmail/#syncing_calendar_events_in_salesforce) improvement. We implemented 2-way synchronization of recurring Google calendar Event series. Their syncing can be performed [via color-coding](../Using-the-Solution-for-Salesforce-and-Gmail/#syncing_calendar_events_in_salesforce) or [via Save button](../Save-Email-Dialog/) or [by Autosync](../Configuring-Activities-Synchronization-Settings/#automatic_syncing_of_calendar_items_events_autosharing); syncing a single event in a series syncs the entire series.  
*Limitations:* [same as in MS Exchange](../Calendars-Syncing-Exceptions/); the maximum number of synced occurrences is defined by [Salesforce limits](https://help.salesforce.com/articleView?id=000338790&type=1&mode=1). Private Google Events cannot be synced in general  

**3\.** Implemented {{ product_name }} localization in Danish. Earlier also added Japanese and Chinese (Simplified). See [this article](../Introduction/#ri_user_interface_localizations) for the full list of supported {{ short_name }} UI languages  

**4\.** [Revenue Engage email campaigns](https://revenuegrid.com/product/email-campaign-salesforce/) building improvement: implemented a [{{ company_name }} template](https://docs.revenuegrid.com/articles/Templates/) selector in the Sidebar displayed next to campaign emails; the selector also applies templates to Email bodies in Compose / Reply  mode in MS Outlook. In addition, users' [pre-configured Salesforce templates](https://help.salesforce.com/articleView?id=sf.email_create_a_template.htm&type=5) can be automatically added to {{ company_name }} templates pool upon request                                  

**5\.** Based on several customers' requests, implemented the optional possibility to auto-fill a pre-set text in the Body (Description) field in [Time Slots](../How-to-Send-Meeting-Time-Slots-(Adaptive-view)/) / [Book Me](../Sharing-Calendar-Availability-(Adaptive-view)/) creation dialogs  

**6\.** Per a customer's request, implemented the optional possibility to get [new created Contacts'](../Create-New-Records/) *Address* field prefilled based on associated Account's Address  

**7\.** We've implemented notifications on pending {{ short_name }} Add-In updates which recommend the end users to restart the Add-In to apply an update 

<u>Regular update:</u>  

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Features\update-addin.png">
</p></details>

&nbsp;

<u>Specific update:</u>
Required to use a specific [Add-In function](../Introduction/), e.g. [Smart Actions](../All-User-Actions-in-Add-In-Sidebar/#smart_actions) or [Engagement tracking](../Tracking-Customer-Engagement-with-Magic-Pixel-(Adaptive-view)/)   

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Features\update-section.png">
</p></details>
&nbsp;

**8\.** [{{ short_name }} Admin panel Users management](../Managing-Users-via-the-Solution-s-Admin-Panel/) improvement: implemented optional auto-deletion of inactive users from {{ product_name }} database, based on *Inactive user* criteria – users that did not open the Add-In and had no Sync sessions over a set period of  time (6 months by default). The mechanism can be enabled [upon request](mailto:support@revenuegrid.com)  

**9\.** Per a customer's request, implemented optional auto-deletion of users from {{ short_name }} database as soon as they get removed from the customer's [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/). This feature only works for Orgs with [MS Graph connection](../MS-Graph/). It can be enabled [upon request](mailto:support@revenuegrid.com)   

&nbsp;

&nbsp;

#### 2105 Bugfixes

**1\.** [Book Me](../Sharing-Calendar-Availability-(Adaptive-view)/) and [Time Slots](../How-to-Send-Meeting-Time-Slots-(Adaptive-view)/) consistency fix: ensured that "Working elsewhere" and "Tentative" calendar item statuses are rendered as "Free" for Time Slots and Book Me, as expected  

**2\.** Fixed several issues with [Book Me](../Sharing-Calendar-Availability-(Adaptive-view)/) and [Time Slots](../How-to-Send-Meeting-Time-Slots-(Adaptive-view)/) dialogs and the Booking page, improving their usability  

**3\.** Fixed localStorage detection for Internet Explorer 11 browser to ensure smooth Add-In running in this browser  

**4\.** [Outlook for Android implementation](../Using-on-iPhone/): fixed a Sidebar UI issue where the calendar selector control on date fields did not work as expected, making the fields hard to fill in. Now it works all right

&nbsp;

*The update also includes several minor bugfixes, UX/UI improvements, as well as customer-specific updates.*

&nbsp;

&nbsp;

* * *

&nbsp;

&nbsp;

### {{ product_name }} 2102 (Spring 2021) Release notes

&nbsp;

#### 2102 Hotfix 1 and Hotfix 2

&nbsp;

##### 2102 HF1-2 Bugfixes

**1\.** [Time Slots](../How-to-Send-Meeting-Time-Slots-%28Adaptive-view%29/) booking page consistency fix: ensured that the time slot that corresponds to the time link recipients click in a time slots invitation email is selected in the Booking page table, as expected  

**2\.** A minor UX fix for Book Me and Time Slots: ensured that the invitation link does not get inserted twice if the Finish button is double-clicked  

**3\.** Fixed an issue where an incorrect file size (0.00 Bytes) was displayed for the [.eml (email copy) file attachment](../Attachments-Handling-(Basic)/#the_default_attachment_eml_copy_of_an_email) in the Sidebar. Now valid file sizes are displayed  

*The update also includes several minor bugfixes, UX/UI improvements, as well as customer-specific updates.*

&nbsp;

&nbsp;

#### 2102 major update

##### 2102 Improvements and new features

Video summary:

<details><summary> >>> Click to see the video <<< </summary>
<p><iframe src="https://player.vimeo.com/video/514472857" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
</p></details>


&nbsp;


**1\.** [Save dialog](../Save-Email-Dialog/) usability improvement: based on the customers' requests, implemented the possibility to select or unselect all retrieved related records with a single click on items saving  

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Working-with-Activities\select-all.png">
</p></details>
&nbsp;

**2\.** Implemented an optional possibility to delete Events synced in Salesforce by [{{ short_name }} Sync engine](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/). This function allows the users to easily remove an item synced to Salesforce by mistake, also in bulk.
To remove a synced calendar item from Salesforce: assign it the custom *"Salesforce Unsync"* category in MS Outlook and wait for the next [Sync session](../Synchronization-Engine-An-Overview/)


<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Unsync-Event\unsync-owa.png">
</p></details>
&nbsp;

**3\.** Per a customer's request, implemented the possibility to interact with [Salesforce Lightning Scheduler](https://www.salesforce.com/products/platform/products/lightning-scheduler/) via {{ company_name }}. See the video <https://youtu.be/D6betOrxAwo> to learn how to use this feature. Also see the [tech background article](../Lightning-Scheduler-API/)



**4\.** Another convenience of use Sidebar interface improvement: added a quick save button to records' flashcards (headers) displayed in {{ product_name }}, so now it is possible to save an email with a record with a single click, without expanding a record's card. See [this article](../All-User-Actions-in-Add-In-Sidebar/#quick_save_to_a_record) for details  

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Getting-Started\First-Steps\Using-Adaptive-View\quick-save.png">
</p></details>

&nbsp;

**5\.** Implemented the premium Stale Thread Reminder communication enhancement feature. See [this article](../Stale-Thread-Reminder/) for complete information  

&nbsp;

**6\.** Implemented the possibility to [synchronize](../Synchronization-Engine-An-Overview/) [Google Tasks](https://support.google.com/tasks/answer/7675772?co=GENIE.Platform%3DDesktop&hl=en) between Gmail and Salesforce using {{ short_name }} Sync. See [this article](../Using-the-Solution-for-Salesforce-and-Gmail/#syncing_tasks_between_google_and_salesforce) for more information    

&nbsp;

**7\.** Redesigned [{{ short_name }} Meeting Scheduler](../Sharing-Calendar-Availability-%28Adaptive-view%29/)'s booking webpage to boost its usability; now the page is also easier to use on mobile devices

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sharing-Calendar-Availability-(Adaptive-view)\booking-new-view.png" class="minimized">
</p></details>

&nbsp;

**8\.** MS Exchange Delegated access extended support: per several customers' requests, implemented support for both emails and calendars handling via Delegated access, via [{{ company_name }} Web (Cloud) as well as Desktop implementations](../Desktop-MSI-and-Cloud-Web-Implementations-Comparison/). Presently, the feature only works over [EWS](../Working-With-EWS/), but not [MS Graph](../MS-Graph/)

**9\.** [Book Me feature](../Sharing-Calendar-Availability-(Adaptive-view)/) improvement: per several customers' requests, implemented the possibility to add time spans (buffers) between subsequent meetings organized using Book Me. 
This allows the organizer to take a short break and get prepared between the meetings. The span's duration is set via a picklist in [Book Me generation dialog](../Sharing-Calendar-Availability-%28Adaptive-view%29/#then_fill_in_the_optional_meeting_parameters_hidden_under_the_advanced_options_tab)

&nbsp;

&nbsp;

##### 2102 Bugfixes

**1\.** Fixed a rare issue that caused a false error notification *"Something went wrong. Attachments not saved."* to appear under specific circumstances upon saving two or more attached files in Salesforce, even though the attachments were saved successfully   

**2\.** ["Mark as SPAM"](../Context-Specific-Actions/) usability fix for calendar items: the button's tooltip and notification were revised to make them more clear; also added extra notifications to clarify the flow  

**3\.** Increased {{ product_name }} navigation user friendliness by adjusting the logic how the Back button works in several dialogs    

**4\.** Fixed an issue where the records search field became unclickable in the Sidebar  

*The update also includes several minor bugfixes, UX/UI improvements, as well as customer-specific updates.*

&nbsp;

* * *

&nbsp;

### {{ product_name }} 2011 HF2 (Fall 2020) Release notes

*Release date: February 1, 2020*

&nbsp;

#### 2011 HF2 Improvements and new features

**1\.** Book Me dialog improvement: added the item *"None"* for the [Minimal Time Span field](../Sharing-Calendar-Availability-(Adaptive-view)/#then_fill_in_the_optional_meeting_parameters_hidden_under_the_advanced_options_tab), making it easy to remove the necessity of a time span between booked meetings  

**2\.** Added the Stale Thread reminder feature for [{{ company_name }} integration](https://docs.revenuegrid.com/articles/release-notes/). See [this article](../Stale-Thread-Reminder/) for more information

&nbsp;

#### 2011 HF2 Bugfixes

**1\.** A  minor Book Me consistency fix: ensured that multiple booking of the same calendar slot by several invitees is no longer possible in case several invitees open the link at the same time

**2\.** A minor [Customization settings](../Customization-Settings-Explained/) application consistency fix: ensured that pinning of "Suggested new records" in customization settings leads to the tab's pinning in {{ short_company_name }} Sidebar





*The update also includes several minor bugfixes, UX/UI improvements, as well as customer-specific updates.*

&nbsp;

&nbsp;

### {{ product_name }} 2011 HF1 (Fall 2020) Release notes

*Release date: January 4, 2020*

&nbsp;

#### 2011 HF1 Improvements and new features

**1\.** Save dialog usability improvement: based on the customers' requests,  implemented the possibility to select or unselect all retrieved related  records with a single click on items saving.

**2\.** [Save dialog](../Save-Email-Dialog/) usability improvement: based on the customers' requests, implemented the possibility to select or unselect all [retrieved related records](../Save-Email-Dialog/#save_email_dialog) with a single checkbox click in the Save dialog.  

**3\.**  Implemented an optional possibility to [auto-save emails](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_emails_emails_autosharing) in Salesforce independently, without [auto-creating People records](../Synchronization-Engine-An-Overview/#automatic_creation_of_contacts_or_leads_by_rg_email_sidebar_autoresolving) or linking them to  Business records; also added a corresponding [Global setting](../Special-Admin-Panel-Settings/#extra_configuration_settings)  *SalesforceEmailAutoTrackIncludingNotShared* to manage this function.

**4\.** "Stale Thread Reminder" [{{ company_name }}](https://docs.revenuegrid.com/) integration feature was implemented. See [this article](../Stale-Thread-Reminder/) for more details.



&nbsp;

*The update also includes several minor bugfixes, UX/UI improvements, as well as customer-specific updates.*

&nbsp;

### {{ product_name }} 2011 (Fall 2020) Release notes

*Release date: December 5, 2020*

&nbsp;

#### 2011 Improvements and new features

**1\.** Now the end users can check out [future product features Roadmap](https://portal.productboard.com/ymxffqium9zmspudbn3gcjlt/tabs/1-in-development) by opening the Sidebar's Main menu > About screen.

**2\.** Implemented the possibility to [log in to {{ company_name }}](../How-to-Install-and-Run-the-Solution-for-Office-365-Mailboxes/#ii_rg_email_sidebar_logon) using [O365 OAuth 2.0](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow). This applies to both end user accounts and the Admin panel.

**3\.** Max security [O365 OAuth 2.0](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow) is now also used as the only method for [Exchange Impersonation service accounts](../Impersonation-O365/) data access authorizing for Office 365 mailboxes. All existing customers who use such Impersonation accounts must [re-authorize the access using O365 OAuth](../Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/#service_account_authorization_via_office_365_oauth). This switching was required because the old Impersonated access authorization method with login and password creds entry will be disabled by Microsoft in 2021.

**4\.** [{{ company_name }}](https://docs.revenuegrid.com/) integration improvement: implemented Signals widget embedding into {{ short_company_name }} Sidebar as a [Smart Action](../All-User-Actions-in-Add-In-Sidebar/#smart_actions). It works as a link to {{ company_name }} Signals page.

**5\.** Per several customers' requests, the text of the [Customization push](../Managing-Email-Sidebar-Customizations/#pushing_your_customization_to_other_users_in_your_salesforce_org) notification was updated, making it clearer.

**6\.** Implemented a number of [MS Graph connectivity](../MS-Graph/) improvements and bugfixes, incl. [syncing of recurring Meetings and Appointments series](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#synchronizing_series_of_recurring_items) and [saving attached files](../Attachments-Handling-(Basic)/).

**7\.** Removed the "Sign in with Login/Password" option from the [Sync settings sign in page](../How-to-Open-Sync-Dashboard-(Adaptive-view)/), since now secure Salesforce OAuth authorization is now used instead for all end users.

**8\.** A minor [Book Me links generation](../Sharing-Calendar-Availability-(Adaptive-view)/) use convenience improvement: now  generated Book Me hyperlinks can be inserted behind any words, phrases,  or sentences highlighted by the user in composed email's body. The feature works in MS Outlook for Windows or Mac and Outlook on the Web, the Web (Cloud) implementation only.

**9\.** Book Me / Time Slots time zone selector improvement: now popular time zones can be found quickly by their abbreviation, e.g. *HST/HDT; AKDT;  AKST; PDT; MST/MDT; CDT; CST; EDT; AST; SST; ChST; EST*

**10\.** Optimized the Add-In's initial loading, by excluding some excessive startup jobs.




&nbsp;

&nbsp;

#### 2011 Bugfixes

**1\.** Sidebar data refresh consistency improvement: fixed a configuration-specific issue where {{ short_company_name }} Sidebar displayed Salesforce context data for a previously selected email instead of the actual one's.

**2\.** Fixed a rare issue that prevented saving of attached files along with emails due to a timeout in Salesforce.

**3\.** Fixed a seldom occurring issue where the "Log a Call" dialog wasn't opened in the Sidebar on icon clicking, instead freezing the Sidebar with the status "Initializing..."



*The update also includes several minor bugfixes, UX/UI improvements, as well as customer-specific updates.*

&nbsp;

&nbsp;





* * *

&nbsp;

&nbsp;

### {{ product_name }} 2008 (Summer 2020) Hotfix 2 Release notes

*Release date: October 5 2020*

#### Improvements and new features

**1\.** {{ short_name }} [Sign Up Wizard page](../User-Registration-Wizard/) was re-designed for extra usability.  

**2\.** Implemented the possibility to edit the fields of already saved [Enhanced Email messages](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-%28Adaptive-view%29/#11_emails_saved_as_emailmessages_vs_emails_saved_as_tasks) via the Sidebar: SFDC records linked to the email (*Related To*): both [WhatID People Records and WhoID Business Records](https://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/), *Subject*, *Body*, and other key ones. In this scenario, the email gets deleted and then re-created in Salesforce. 

**3\.** The text of the [customization push](../Managing-Email-Sidebar-Customizations/#pushing_your_customization_to_other_users_in_your_salesforce_org) notification was updated, to make it more clear.  

***The update also includes several minor bugfixes and UX/UI improvements.***

&nbsp;

#### Bugfixes

**1\.** Fixed a rare issue where an operation timeout error prevented attached files saving via the Add-In.

**2\.** Fixed a minor UI issue where the number of related Opportunities was not indicated on Account detailed card's Related tab.

&nbsp;



* * *

&nbsp;

### {{ product_name }} 2008 (Summer 2020) Release notes: notable improvements and fixes

&nbsp;

#### Improvements and new features

**1\.** Implemented [MS Graph secure API](https://docs.microsoft.com/en-us/graph/overview) support for working with MS Office 365 data. Presently, this mechanism is optionally applied for several Enterprise customers. See [this article](../MS-Graph/) for complete information.

**2\.** Implemented an optional possibility to log in into {{ product_name }} using [Office 365 OAuth 2.0](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow) instead of Salesforce OAuth. It can be used for both end user accounts and the [Admin panel](../How-to-Log-In-to-the-Admin-Panel/). Presently, it's available for big Enterprise customers.

**3\.** Made the Book Me/Time Slots selection dialog more mobile-friendly; now clicking on the "Suggested time slots" link summons a "Confirm a meeting" pop-up dialog instead of opening the calendar table.

**4\.** Ensured automatic force-stopping of sync sessions if Sync was stuck for a specified number of days, by implementing a corresponding mechanism.

&nbsp;


&nbsp;

#### Notable fixes

**1\.** Fixed an issue where under specific circumstances emails belonging to a selected thread got auto-saved linked to the User instead of a relevant Opportunity. Now linking works as designed.

**2\.** Fixed a specific issue where the Save dialog did not list related records if the "Save email..." button was clicked too quickly after dialog opening.

**3\.**  Fixed an issue where all-day Events downsynced from Salesforce to Gmail calendar were converted into 5pm-5pm Events instead of 12pm - 12pm ones. Now all-day events downsyncing works as designed.



***The update also includes several less significant bugfixes, back end and front end performance optimizations, minor UX/UI tweaks, etc.***



&nbsp;
&nbsp;

### Knowledge Base updates

&nbsp;

#### New articles

- [A collection of {{ company_name }} video tutorials](../Video-Guides/)
- [Using {{ product_name }} with MS Graph](../MS-Graph/) 
- [How to configure MS Exchange meeting Room lists to make the Rooms usable in {{ short_name }} Meeting Scheduler](../Rooms-List/)


&nbsp;

#### Updated articles

- [Emails saving as EmailMessage (Enhanced email) vs. Emails saving as Tasks](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-%28Adaptive-view%29/#11_emails_saved_as_emailmessages_vs_emails_saved_as_tasks)

- [Global and Contextual default search filters' parameters explained](../Customization-Settings-Explained/#default_rg_email_sidebar_filters)

- [Managing Organizations, Email access type configuration](../Managing-Organizations-via-the-Admin-Panel/#activity_this_subtab_displays_system_activities_for_the_current_organization)

- [How to activate {{ short_name }} Sync](../Authorizing-Sync-Engine-to-Work-with-Your-Data/)

- [Optional editing of an Email's body on saving](../Save-Email-Dialog/#editing_saved_emails_body)

- [How to configure a Gmail service account](../Gmail-Service-Account/)
&nbsp;
&nbsp;
* * *

&#160;
### {{ product_name }} 2005 (Spring 2020) + Hotfix 1 Release notes

&nbsp;

#### Improvements and new features

&nbsp;

##### User interface/user experience improvements and Rebranding

**1\.** Due to development of a [new products line](https://docs.revenuegrid.com/) and marketing focus expansion

- Solution got rebranded to *{{ company_name }}*. Now that includes all [components of the Add-In and the Sync Engine](../AddIn-vs-Sync-Functions/)  
- [{{ company_name }} revenue intelligence platform](https://docs.revenuegrid.com/) got rebranded to *Revenue Engage*  
- Invisible.io got rebranded to *RevenueGrid.com*  

Product users are not affected by the rebranding in any way, it's the same use conditions, the same set of functions, plus an updated interface and extra features.

&nbsp;

**2\.** {{ product_name }} [Sidebar user interface](../Introduction/) got tweaked, the following controls were slightly moved or changed for increased usability

- The key controls layout in the header was updated as follows. This results in a better compatibility with mobile devices

![](../assets/images/Using-SmartCloud-Connect/new_header.png)
&nbsp;

- Navigation was improved by adding Sidebar screen/card names and moving the navigation controls to the top of the Sidebar
![](../assets/images/Using-SmartCloud-Connect/navigate.png)
&nbsp;
-  Similarly, the **Cancel** and **Save/Create** buttons and the **Show only important fields** checkbox previously put at the bottom of various dialogs have been relocated to the Sidebar's header
![](../assets/images/Using-SmartCloud-Connect/buttons_header.png)

&nbsp;

-   The **Menu** icon was moved to the left-hand side of the header and the Menu is now implemented as a dedicated screen instead of a dialog, so it's easy to use on mobile devices

&nbsp;

**3\.** Released an advanced Salesforce managed package that ensures maximum {{ product_name }} integration with Salesforce. The package also includes essential visual components elements (Salesforce Canvas panes), for the best use experience it should be installed for all {{ short_name }} users in an Org by the local Salesforce Admin, along with the older [Invisible Suite package](../Admin-Managed-Package/). More information [here](../Admin-Managed-Package/).

&nbsp;

**4\.** Implemented several new convenient {{ short_name }} customization settings: *Notify when email is opened*, *Hide Chatter*, *Do not allow attaching .EML files to objects*, *Do not allow to work with email templates*, *Do not allow to search objects in LinkedIn*, *Support Case Assignment Rules*, *Support Lead Assignment Rules*, *Edit email body in Save dialog*. See [this article](../Customization-Settings-Explained/#2_application_settings) for more information.

&nbsp;

**5\.** {{ product_name }} Classic view has been discontinued as obsolete for all end users. See [this article](../All-User-Actions-in-Add-In-Sidebar/) to learn how to use {{ short_name }} Adaptive view.

&nbsp;

**6\.** (Desktop MSI implementation only) A drag and drop signature-to-contact  processing mechanism was implemented; it allows to quickly populate a  new Contact's fields by selecting the signature of an email and then  dropping it into {{ product_name }}. What fields can be extracted  based on a signature: 
  *First/Last name  
  Address  
  Title  
  Email  
  Phones (if multiple - assign according to Contact's phone fields)  
  Account*  

&nbsp;

**7\.** [User-initiated records search](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-(Adaptive-view)/) via [{{ product_name }}](../Introduction/) got improved: now when viewing search results the users also see secondary record fields besides the Name field; this helps to identify different records with identical names.

&nbsp;

**8\.** [Revenue Engage integration] Implemented a setting *RevenueGridConfiguration* that allows to enable or disable [Revenue Engage](https://docs.revenuegrid.com/) access controls in [{{ product_name }}](../Introduction/).

&nbsp;

**9\.** Implemented an optional "Edit email on saving" feature available for big Enterprise {{ short_name }} customers which is managed via Customization settings. The feature allows editing saved emails' bodies (Description) in the Saved dialog,  for example to remove sensitive information. Limitations: *1.* only emails  saved in [Read mode](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#2_when_revenue_grid_sync_is_not_active), *2.* does not support HTML formatting, *3.* unavailable for  Enhanced Emails, i.e. only Task descriptions can be edited. In addition, Email bodies exceeding the field's limit (32k characters by default) get auto-truncated.

&nbsp;

**10\.** Implemented an optional possibility to track and save emails from/to a secondary email address used by a contact, based on a corresponding custom secondary email field added in Salesforce.

&nbsp;

**11\.** The automatic email notification "Action required - Sync suspended" was improved to make it more informative for the recipients. Now it includes specific required action steps and illustrations.

&nbsp;

**12\.** [Save email/Save event](../Save-Email-Dialog/) flow improvement based on a customer's request: now previously selected or already linked related objects are also  pre-selected when an item gets saved with another record retrieved via {{ product_name }} search.

&nbsp;

**13\.** A minor improvement of the [Save Email/Save Event dialog](../Save-Email-Dialog/), now clicking on a related record's header in the dialog toggles the checkbox which manages record linking.

&nbsp;

**14\.** Another [Save email/Save event](../Save-Email-Dialog/) dialog's usability improvement, now the Linked  Records selector uses the convenient clear/select checkboxes logic instead of the "Remove" button.

&nbsp;

**15\.** Another [Save email/Save event dialog](../Save-Email-Dialog/) user friendliness improvement: updated the labels related to records linking selector to make them more informative.

&nbsp;

**16\.** Updated the labels in {{ product_name }} [Synchronization settings](../Configuring-Activities-Synchronization-Settings/), improving their informativity.

&nbsp;

**17\.** Implemented the possibility to differentiate between emails saved by the users via the Save button ([Read and Compose modes](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#2_when_revenue_grid_sync_is_not_active)) and emails auto-saved by {{ short_name }} Sync engine, using a custom Salesforce field *AddInEmail*.

&nbsp;

**18\.** The Save email/Save event button was disabled in {{ product_name }} for all [Delegated calendar access scenarios](../Using-MS-Outlook-Delegated-Calendars/) in the [Web (Cloud) {{ short_company_name }} implementation](../Desktop-MSI-and-Cloud-Web-Implementations-Comparison/).

&nbsp;

**19\.** All references to SpringCM document management system in {{ product_name }} and its documentation have been changed to DocuSign, due to SpringCM rebranding.

&nbsp;

**20\.** Ensured automatic force-stopping of sync sessions if they were stuck for a certain number of days, by implementing a corresponding mechanism.

&nbsp;

##### Chrome Extension for Gmail improvements


&nbsp;

**1\.** Gmail Calendar events handling improvement: implemented the possibility to set default Gmail events' reminders over {{ company_name }} Sync.

&nbsp;

**2\.** Gmail calendar handling improvement: based on the customers' feedback, we implemented the possibility to assign different colors for [colorcoding Events to be synced](../Using-the-Solution-for-Salesforce-and-Gmail/#syncing_calendar_events_in_salesforce) by {{ product_name }}. Also note that the color-marking way to sync Gmail calendar event is now disabled by default and it can be enabled by request.

&nbsp;

&nbsp;

##### Engagement tracking panel improvements

&nbsp;

**1\.** Added displaying of minutes in Engagement tracking details to allow the users to know specific time when the email was opened by a recipient. Also changed the label and the font of notifications counter.

&nbsp;

**2\.** Engagement tracking panel improvement: now it is possible to reset the new engagement notifications counter by *Ctrl* pressing  + double-clicking the Engagement tracking icon in the Sidebar's bottom toolbar.

&nbsp;

**3\.** Another Engagement panel improvement: implemented an optional possibility to auto-pin (mark as important) in Engagement panel all external (not in-org) emails with auto-inserted tracking code. The new Customization setting used to manage that is "Notify when email is opened".



&nbsp;

* * *

&nbsp;

#### Notable fixes

&nbsp;

**1\.** Fixed an issue that occurred in configurations which use Person Accounts, resulting in a Sync issue "Can not select a person account".

&nbsp;

**2\.** Fixed an issue with processing of user-defined "Email domains blacklisted from syncing" values involving aliases (with [+] in the address). Now they are handled as designed.

&nbsp;

**3\.** Fixed an issue where an incorrect set of objects was linked to a saved email or event after extra objects to link were added using search in the Saved email/Save event dialog. Now only specifically selected objects from search are linked.

&nbsp;

**4\.** Fixed an issue that prevented {{ short_company_name }} Sidebar logon with Salesforce creds for some of end users (the "SimpleWebClient concurrent use" exception).

&nbsp;

**5\.** Fixed an issue where some labels and messages in various {{ product_name }} components remained in English after switching to another localization. Now they are translated.

&nbsp;

**6\.** Fixed an issue where the bottom item in the related records search results list of the Save email/Save event dialog was sometimes not displayed.

&nbsp;

**7\.** Fixed a specific issue where the latest clicked Opportunity was  displayed in the "Related to" field of the clones for emails after  saving the email link to various objects.

&nbsp;

**8\.** Fixed an issue where Salesforce all-day events were synchronized as 5pm - 5pm events in Gmail calendar. Now they are synced as proper Gmail all-day events.





***The update also included a number of other less significant bugfixes, back end and front end performance optimizations, minor UX/UI tweaks, etc.***

&nbsp;

* * *

&nbsp;

### 2002 Hotfix 1 Release Notes

&nbsp;

#### Improvements and new features

**1\.** Due to development of a [new products line](https://docs.revenuegrid.com/) and marketing focus expansion

- Solution gets rebranded to *{{ company_name }}*  
- Invisible.io gets rebranded to *RevenueGrid.com*  

Product users are not affected by the rebranding in any way, it's the same use conditions, the same set of functions, plus a slightly updated interface and extra features.

**2\.** We added a related records selection mechanism implemented as checkboxes to the [Save Email/Save Event dialog](../Save-Email-Dialog/); it works in the same manner as the checkboxes removed from the [Sidebar](../Introduction/)'s home screen.

![](../assets/images/Using-SmartCloud-Connect/How-To-s/Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/dialog_checkboxes.png)

&nbsp;

**3\.** Implemented an additional [Customization setting](../Customization-Settings-Explained/#2_application_settings) that regulates [Engagement notifications](../How-to-Use-SCC-Engagement-Panel-%28Adaptive-view%29/#to_view_collected_tracking_information_in_the_engagement_panel) displaying for emails to external (not in-org) contacts  with auto-inserted tracking code; the setting is called "Notify when email is opened". When it is enabled, notifications in SCC Sidebar's  bottom toolbar will be displayed when the tracking code is triggered by the recipients of all such emails, as if they were marked as Important in the Engagement panel by the user.

**4\.** Improved wording in several [Save Email/Save Event dialogs'](../Save-Email-Dialog/) fields labels.



&nbsp;

&#160;

