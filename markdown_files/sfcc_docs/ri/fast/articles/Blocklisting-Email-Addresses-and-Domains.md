---
description: How to blocklist specific email addresses and domains in RGES Add-In
---
# Blocklisting Email Addresses and Domains in {{ short_name }} Add-In  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! warning "Important"
    This individual user-defined blocklist and the [corporate blocklist](../Special-Admin-Panel-Settings/#emails_domains_blocklisted_from_sync) managed by the [local admin](../How-to-Log-In-to-the-Admin-Panel/) or by our [Support team](mailto:support@revenuegrid.com) are complementary (additive). That is, both these not-to-be-saved by sync blocklists are applied when {{ product_name }} processes your emails

&nbsp;


!!! warning "Important"
    Please note that if you change the **Email Domains blocklisted From Syncing** list, for the changes to be applied you must [log out from {{ product_name }}](../How-to-Change-Email-Address-in-Your-Product-Account-Office-365/) and then [re-log in](../How-to-Install-and-Run-the-Solution-all-configurations/#ii_rg_email_sidebar_logon)

&nbsp;

If you do **not** want email messages and calendar items from/to certain addresses or domains to be saved with Salesforce, e.g. personal or in-company ones, you can add them to the blocklist. {{ product_name }} will never save emails from/to these addresses and domains in Salesforce automatically; however, you still can [save them selectivey via the Sidebar](../How-to-Save-Internal-or-Blacklisted-Emails-in-Salesforce-%28Adaptive-view%29/). {{ product_name }} Add-In also applies these addresses on [initial search filtering](../Initial-Search-and-Applied-Record-Filters/#internal_emails_corporate_domains_and_the_blocklist), thus also excluding them from [parsing in the Sidebar](../All-User-Actions-in-Add-In-Sidebar/#4_viewing_details_instantly). 

The blocklist is also applied on [MS Outlook meetings](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/) and [Gmail events](../Using-the-Solution-for-Salesforce-and-Gmail/#syncing_calendar_events_in_salesforce) saving and [auto-saving](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#meeting_appointment_autosaving) in Salesforce. By default, MS Outlook Meetings or Gmail events which have only blocklisted addresses/domains among their invitees will **not** be autosaveable in Salesforce. Another way to prevent saving of a calendar item is to [mark it as Private](../Calendar-Items-Sync-Special-Patterns-Attendees-Lists,-Private-Items,-Item-Unsharing-and-Deletion/#private_calendar_items).

If there is at least one non-blocklisted address/domain among the invitees, the calendar item will be autosaveable in Salesforce, linked to the corresponding Lead or Contact.  
At that, there is also an option available for Enterprise {{ short_name }} customers that allows saving calendar items which have no Lead or Contact to link it to, see the details about the *SalesforceEventAutoTrackIncludingNotShared* setting in [this article](../Special-Admin-Panel-Settings/#extra_configuration_settings).

!!! tip "Tip"
    Also see [this article](../Special-Admin-Panel-Settings/#auto-saving_and_blocklist_intersections) for detailed information on auto-saving flow options and blocklist intersections

&nbsp;

To add both email addresses and domains to the not-to-be-saved-by-sync blocklist, in the **Misc. Settings** block, **Email Domains blocklisted From Syncing** box, specify all addresses or domains you want to exclude from [auto-syncing in Salesforce](../Synchronization-Engine-An-Overview/). Note that the list does not support the [wildcards](https://www.computerhope.com/jargon/w/wildcard.htm).

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b10f4610428632c466a6ad6.png)

&nbsp;

Also, a special global setting blocklists all free email services (e.g., *gmail.com*, *outlook.com*, etc.) from syncing by default, so you don’t need to add all of them to the Blocklist. To change or customize this setting, contact our [support team](mailto:support@revenuegrid.com).

!!! note "Note"
    Both Emails and Meetings invitations received from addresses belonging to specified domains will not be automatically synced in Salesforce

&nbsp; 

!!! warning "Important"
    If an email is received from multiple senders, and only certain email addresses are in the blocklist, the email will still be linked to registered senders who are not blocklisted

&nbsp;

## Blocklisting email addresses in the Sidebar

Additionally, {{ product_name }} enables you to blocklist specific email addresses right form the [Sidebar](../Introduction/). To do that, select an email from/to an address to be blocklisted from sync and click the **Do Not Sync** button on [the **Suggested new records** tab](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-(Adaptive-view)/#the_new_records_tab) displayed in the Sidebar.

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b10f4ac0428632c466a6adb.png)

<br>

## Blocklist special considerations

If your company uses several internal email domains (e.g., *successteam.com*, *success.team*, *successteam.io*) and you as an admin need to ensure that users won’t be able to remove these email domains or specific email addresses from the blocklist, you can request our support team to disable the setting *ServiceItemsDeletedFromAutoTrackBlackList*. 

If this setting is disabled, it will be impossible for admin to manually remove any internal email domain in the *ServiceAutoTrackBlackList* setting: on refreshing the Settings page, the deleted email domain will be restored in the Blocklist.  The same happens when a user removes internal domain(s) from their individual Blocklist in {{ short_company_name }} Sync Settings, the deleted domain(s) reappear in the Blocklist after some time. 


&#160;
 &#160;

