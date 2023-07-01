---
description: Detailed overview of historical synchronization Historical synchronization and time zones matching in Salesforce
---
# Historical Sync and Time Zone Matching  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*4 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

Historical synchronization means inclusion of existing MS Outlook emails and events into {{ product_name }} [sync scope](../Synchronization-Engine-An-Overview/) on the first start of {{ company_name }} synchronization.

#### Existing *events* synchronization (historical sync) on {{ company_name }} sync activation

After you a) [install {{ product_name }}](../How-to-Install-and-Run-the-Solution-all-configurations/), b) [set up synchronization](../Authorizing-Sync-Engine-to-Work-with-Your-Data/), and c) enable [meetings/appointments auto-syncing](../Configuring-Activities-Synchronization-Settings/#automatic_syncing_of_calendar_items_events_autosharing), only those MS Outlook and Salesforce calendar items which are created *after* sync activation will be automatically synchronized between Exchange and Salesforce. Thus, the following categories of calendar items will **not** be auto-saved:

- Any calendar items, including ones scheduled for any time after {{ company_name }} sync initial activation but created before it
- Series of recurring calendar items created before initial sync activation, including events scheduled to occur 

Synchronization of such existing individual or recurring calendar items from MS Outlook can be initiated by the user - by assigning them the custom *Salesforce* category in MS Outlook, or using the *Save* button in the Sidebar.

!!! note "Note"
    Please also note that {{ company_name }} synchronization will **not** down-sync to MS Exchange / Office 365 your Salesforce calendar items which existed prior to sync initial activation

&nbsp;

!!! tip "Tip"
    If the existing events are too many to manually mark all of them for saving in Salesforce through category assigning, you can order their inclusion into {{ company_name }} synchronization scope as a separate custom service, by request sent to [our Sales team](mailto:sales@revenuegrid.com)



#### Existing emails saving (historical sync) on {{ company_name }} sync activation

After you a) [install {{ product_name }}](../How-to-Install-and-Run-the-Solution-all-configurations/), b) [set up synchronization](../Authorizing-Sync-Engine-to-Work-with-Your-Data/), and c) enable [emails auto-syncing](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_emails_emails_autosharing), {{ product_name }} will auto-sync in Salesforce all your emails from/to non-[blocklisted/internal addresses/domains](../Initial-Search-and-Applied-Record-Filters/#internal_emails_corporate_domains_and_the_blocklist) sent or received within 6 days in the past from sync activation date.

!!! tip "Tip"
    By default, only the emails in the Inbox and Sent folders are auto-saved. If you need to save the emails from other folders/subfolders (custom folders, archive, etc.) and adjust the sync scope inclusion time span according to your needs submit a corresponding request sent to our [Support team](mailto:support@revenuegrid.com)

<br>
If you do not want to use auto-sharing for bulk syncing of your existing emails, you can initiate synchronization of only selected previously existing emails from MS Outlook, by assigning them the custom *Salesforce* category in MS Outlook, moving them to the *Salesforce emails* folder, or using the *Save* button in the Sidebar.


!!! warning "Important"
    By default, all free email domains are blocklisted from auto-syncing and records auto-creation. If you need to save the existing the emails and calendar items sent from/to free email domains (gmail.com, yahoo.com, etc.), submit a corresponding request to the [{{ short_company_name }} Support team](mailto:support@revenuegrid.com)

&nbsp;

* * *

&nbsp;

#### Times Zones Matching

The general principle how {{ product_name }} [syncs calendar items](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/) is [integrating](../Object-Fields-Mapping-Patterns/) [MS Outlook calendar items processing mechanisms](https://support.office.com/en-us/article/introduction-to-the-outlook-calendar-d94c5203-77c7-48ec-90a5-2e2bc10bd6f8) and [Salesforce calendar events handling](https://help.salesforce.com/articleView?id=events_and_calendars.htm&type=5), also matching their corresponding time zone-defined  offsets.
Additionally, when generating the [time slots selection](../How-to-Send-Meeting-Time-Slots-(Adaptive-view)/) or [calendar availability booking](../Sharing-Calendar-Availability-(Adaptive-view)/) page, {{ product_name }} reads the actual time zone values in recipients' browsers and adjusts the scheduling table accordingly; a selector of other time zones is also included in the scheduling page.

##### Issues with uncommon time zones handling

Due to a discrepancy between the sets of time zones available in [MS Exchange](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/default-time-zones) and [Salesforce](https://help.salesforce.com/articleView?id=admin_supported_timezone.htm&type=5), some less common time zones cannot be matched properly on {{ product_name }} calendar items synchronization. This results in [synchronization issues](../Handling-Sync-Issues/) of the following kind: *Can't match specified timezone: 'Greenland Standard Time' ({occurrence id})*. If you encounter these issues, it is recommended to switch to a nearest matching commonly used time zone when working with {{ product_name }}, if possible.

A detailed list of known problematic time zones:

| MS Exchange/Windows time zone                                | Salesforce time zone         | Status    | Details                                                      |
| ------------------------------------------------------------ | ---------------------------- | --------- | ------------------------------------------------------------ |
| Aus Central W. Standard Time - (UTC+08:45) Eucla             | n/a                          | different |                                                              |
| Central Brazilian Standard Time - (UTC-04:00) Cuiaba         | America/Santiago             | compliant | unmatched DS period from Feb to May and ST start from Aug to Nov |
| Cuba Standard Time - (UTC-05:00) Havana                      | America/Indiana/Indianapolis | similar   | small unmatched period from 0:00AM up to 2:00AM for DS and ST start |
| Dateline Standard Time - (UTC-12:00) International Date Line West | n/a                          | different |                                                              |
| E. Europe Standard Time - (UTC+02:00) Chisinau               | Europe/Athens                | similar   | small unmatched period from 2:00AM to 3:00AM for DS start and from 3:00AM to 4:00AM for ST start |
| Easter Island Standard Time - (UTC-06:00) Easter Island      | America/Mexico_City          | compliant | matching is almost impossible - DS and ST switching is opposite |
| Greenland Standard Time - (UTC-03:00) Greenland              | America/Sao_Paulo            | compliant | matching is almost impossible - DS and ST switching is opposite |
| Jordan Standard Time - (UTC+02:00) Amman                     | Asia/Beirut                  | compliant | small unmatched period - several days on DS and ST start     |
| Kamchatka Standard Time - (UTC+12:00) Petropavlovsk-Kamchatsky - Old | Pacific/Auckland             | compliant | large unmatched period for DS start from Mar to Apr and ST start from Sep to Oct |
| Mid-Atlantic Standard Time - (UTC-02:00) Mid-Atlantic - Old  | n/a                          | different |                                                              |
| Morocco Standard Time - (UTC+00:00) Casablanca               | Africa/Casablanca            | identical | unmatched period from May to Jun in DS (floating ST for Ramadan) |
| North Korea Standard Time - (UTC+09:00) Pyongyang            | n/a                          | different |                                                              |
| Paraguay Standard Time - (UTC-04:00) Asuncion                | America/Santiago             | compliant | very large unmatched period for DS start from Mar to May and ST start from Aug to Oct |
| Saint Pierre Standard Time - (UTC-03:00) Saint Pierre and Miquelon | America/Sao_Paulo            | compliant | matching is almost impossible - DS and ST switching is opposite |
| Samoa Standard Time - (UTC+13:00) Samoa                      | n/a                          | different |                                                              |
| Sao Tome Standard Time - (UTC+01:00) Sao Tome                | n/a                          | different |                                                              |
| Syria Standard Time - (UTC+02:00) Damascus                   | Asia/Beirut                  | compliant | small unmatched period for several days for DS and ST start  |
| Turks And Caicos Standard Time - (UTC-05:00) Turks and Caicos | America/Indiana/Indianapolis | compliant | large unmatched period for DS start from Jun to Mar          |
| West Bank Standard Time - (UTC+02:00) Gaza, Hebron           | Asia/Beirut                  | similar   | small unmatched period is only one day long for DS and ST start |

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