---
description: Detailed overview of RG Email Sidebar activities synchronization settings
---
# Legacy Sync Settings page: Activities Synchronization Settings Explained  
  
**[legacy Sync Settings page]**

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*4 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! warning "Important"
    Depending on your product license, **the appearance of your Sync Settings page may differ from the one described below**. If you see a different Sync Settings page, refer to [this article](../Configuring-Activities-Synchronization-Settings-rg/).

!!! tip "Tip"
    Some Synchronization features require adding certain auxiliary fields and classes to Salesforce objects; to get them added automatically ask your local Salesforce administrator to install the [{{ company_name }} managed Salesforce app](../Admin-Managed-Package/) in your Org – it will enable the full scope of {{ short_name }} features on the Salesforce side

&nbsp;

{{ product_name }} includes a number of settings that define how Emails, Calendar items, Contacts, or Tasks are processed into Salesforce.

&nbsp;

### To access Sync settings:

**1\.** [Open {{ short_name }} Sync Dashboard](../How-to-Open-Sync-Dashboard-(Adaptive-view)/)  

**2\.** Go to **Sync settings** tab > **Detailed Settings** and see the **Activities Sync Settings** section  

**3\.** Next, you may also need to sign in over secure [Salesforce OAuth 2.0](https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_flows.htm&type=5) or [Exchange/Office 365 OAuth 2.0](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow) or [Gmail OAuth 2.0](https://developers.google.com/identity/sign-in/web/sign-in) in a browser page that appears, depending on your {{ short_name }} Org's configuration





&nbsp;

This article explains all [{{ short_name }} Sync Engine](../Synchronization-Engine-An-Overview/) settings which can be managed by individual users or in bulk by [the Admins](../How-to-Log-In-to-the-Admin-Panel/). The Dashboard's functions and [Sync settings](../Configuring-Activities-Synchronization-Settings/) are mostly identical for MS Exchange / Office 365 and Gmail accounts, with the exception of several [MS Exchange specific functions](../Using-the-Solution-for-Salesforce-and-Gmail/#differences_between_the_exchangeoffice_365_add-in_implementation_and_the_chrome_extension_for_gmail).

&nbsp;

!!! warning "Important"
    Please note that if you adjust the **Auto-Save All Emails in A Thread** sync setting or update the list of **Blocklisted email addresses/domains**; for these changes to be applied you must [log out from {{ short_name }} Add-In](https://docs.revenuegrid.com/ri/fast/assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b3a275f0428630abc0ba0da.png) and then [re-log in](../How-to-Install-and-Run-the-Solution-all-configurations/#ii_rg_email_sidebar_logon)

&nbsp;

* * *

&nbsp;

#### Automatic Saving of Emails (emails autosharing)

!!! tip "Tip"
    Also see [this article](../Special-Admin-Panel-Settings/#auto-saving_and_blocklist_intersections) for detailed information on auto-saving flow options and blocklist intersections

&nbsp;

You can get all relevant (see point **5** in [this article](../Saving-Emails-in-Salesforce-1.-Function-Overview/#under_the_hood_mechanisms_and_special_patterns_applied_on_emails_saving)) incoming and outgoing email messages automatically saved in Salesforce. With automatic saving enabled, your email messages will be automatically saved as Salesforce Tasks or [Email messages](http://help.salesforce.com/articleView?id=emailadmin_enhanced_email_overview.htm&type=5) linked to related Contacts, Leads, and other Salesforce objects retrieved according to [these principles](../Initial-Search-and-Applied-Record-Filters/#the_resulting_related_records_list_will_include). Emails autosaving is performed not immediately but on the following [synchronization session](../Synchronization-Engine-An-Overview/).  


If you receive or send an email from/to an unresolved (not previously registered in Salesforce) Contact or Lead, {{ product_name }} can create a relevant Salesforce automatically to autosave it. See [this article](../Synchronization-Engine-An-Overview/#automatic_creation_of_contacts_or_leads_by_rg_email_sidebar_autoresolving) for more information.

To enable or disable automatic emails saving by {{ short_name }}: in the **Emails** block, toggle the **Enable Auto-Saving **switch button

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/583da1a790336006981741e4.png)

&nbsp;

&nbsp;

##### Inbox Spam Handling Prevention

With enabled Emails auto-saving and set up Leads or Contacts auto-resolving in your cofiguration, {{ product_name }} will process SPAM emails from non-blocklisted email domains which get through to your MS Outlook or Gmail Imbox.

Refer to [this article](../Inbox-SPAM-Handling-in-RG-Email-Sidebar/) for сomplete information on inbox spam handling prevention with {{ product_name }}.

&nbsp;

* * *

&nbsp;

#### Automatic saving of Email Threads

See [this article](../Save-All-Emails-in-a-Thread/) for complete information on how to use this feature.

After you toggle the **Automatic saving of email threads** setting, for the changes to be applied you must [log out from {{ product_name }}](../How-to-Change-Email-Address-in-Your-Product-Account-Office-365/) and then [re-log in](../How-to-Install-and-Run-the-Solution-all-configurations/#ii_rg_email_sidebar_logon).

&nbsp;

To enable this feature: in the *Email Sync Options* section, set the **Auto-Save All Emails In a Thread** switch to Enabled.

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b07f6c62c7d3a2f9011e9be.png)

&nbsp;
&nbsp;

* * *

&nbsp;

#### Linking to Opportunities

You can also have your emails associated not only with contacts and leads, but also with related opportunities. These related opportunities must satisfy all of the following requirements:

*   You are the owner of the opportunity
*   The account associated with the opportunity contains a contact of the person whose email address is specified in the From, To, or CC fields

If several opportunities satisfy these requirements, the email will be saved to the most recent one. If such opportunity was not found, the email will be saved to the account that is associated with the related contact. However, if neither an opportunity nor an associated account were found, the email will not be saved at all. This setting applies only to automatic email/event saving, not to manual saving of events/emails.

To enable the possibility to [link](../Activities-Linking/) saved Emails to Salesforce Opportunities, in the **Misc. Settings** block toggle the **Link to Opportunities** switch button.

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/583da1b390336006981741e5.png)

&nbsp;

* * *

&nbsp;

#### Automatic Syncing of [Calendar Items](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/) (events autosharing)

You can have all your incoming and outgoing Calendar items automatically synced in Salesforce, with specific exceptions listed in [this article](../Calendars-Syncing-Exceptions/). Note that {{ short_name }} will also auto-create new Salesforce records to sync meetings which involve new business contact, see [this article](../Synchronization-Engine-An-Overview/#automatic_creation_of_contacts_or_leads_by_rg_email_sidebar_autoresolving) to learn the details.

With automatic meetings syncing enabled, your meetings will be automatically synced up to your Salesforce calendar and also to the calendars of your colleagues who use {{ product_name }}, if they were invited.

!!! note "Note"
    In the latest product updates, syncing of new Calendar items and their updates can also be performed within several minutes, via [instant syncing](../Synchronization-Engine-An-Overview/#instant_sync_of_calendar_items). This feature can be enabled and configured upon request

&nbsp;

To enable automatic syncing of meetings, toggle the **Enable Meetings Auto-Syncing **switch button.

With automatic syncing of appointments enabled, your appointments will be automatically synced with your Salesforce calendar. To enable automatic saving of appointments, toggle the **Enable Appointments Auto-Syncing **switch button.

![](../assets/images/Configuration-&-Settings/User-Settings/meetings_appointments_as.png)

&nbsp;

* * *

&nbsp;

#### Blocklisting Email Addresses and Domains

{{ product_name }} offers the possibility to **blocklist** email messages and calendar items from/to certain addresses or domains from being saved with Salesforce.

See [this article](../Blocklisting-Email-Addresses-and-Domains/) for more information on **Blocklisting Email Addresses and Domains** with {{ product_name }}.


&nbsp;

* * *

&nbsp;

#### Other Sync Adjustments

Besides above-described regular sync adjustments, {{ product_name }} offers special synchronization settings to meet your company's specific preferences - [syncing calendar items as other object types besides events](../Special-Sync-Options-Save-Events-As-Other-&-One-Way-Sync/#syncing_calendar_events_as_custom_or_standard_salesforce_objects_eg_tasks) and [one-way synchronization options](../Special-Sync-Options-Save-Events-As-Other-&-One-Way-Sync/#one-way_synchronization).


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