---
description: Frequently Asked Questions (FAQs) about Revenue Grid for Salesforce
---
<script>
function setClipboard(value) {
    var tempInput = document.createElement("input");
    tempInput.style = "position: absolute; left: -1000px; top: -1000px";
    tempInput.value = value;
    document.body.appendChild(tempInput);
    tempInput.select();
    document.execCommand("copy");
    document.body.removeChild(tempInput);
}
</script>
<style>
.button {
  position: relative;
  background-color: #ffffff; 
  border: none;
  font-size: 15px;
  color: #AAAAAA;
  padding: 6px;
  text-align: center;
  -webkit-transition-duration: 0.6s; /* Safari */
  transition-duration: 0.6s;
  text-decoration: none;
  overflow: hidden;
  cursor: pointer;
  display: flex;
  color: teal;
}

.button img {
    width: 1rem;
    margin-left: 5px;
    width: 15px;
    margin-top: 2px;
}

.button:after {
  content: "";
  background: #90DDD0;
  display: block;
  position: absolute;
  padding-top: 600%;
  padding-left: 350%;
  margin-left: -20px!important;
  margin-top: -120%;
  opacity: 0;
  transition: all 0.9s
}

.button:active:after {
  padding: 0;
  margin: 0;
  opacity: 5;
  transition: 0s
}

div.a { text-indent: 30px; }
div.b { text-indent: 50px; }

</style>

# {{ company_name }} for Salesforce Frequently Asked Questions (FAQs)  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*22 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! tip "Tip"
    Besides serving as a Mailbox ↔ Salesforce integration tool, {{ product_name }} is an integral component of our premium [revenue intelligence](https://revenuegrid.com/blog/what-is-guided-selling/) package [{{ company_name }}](https://revenuegrid.com). Check [this article](https://docs.revenuegrid.com/) for more information

&nbsp;

### 1\. What is {{ product_name }} for Salesforce?

{{ product_name }} is an app for MS Outlook Desktop or On the Web version and Gmail that brings the power of Salesforce right into your mailbox. It is a smart portal embedded into your personal email program, available from inside your email box, calendar, contacts and tasks tabs.

Note that {{ short_name }} is **not** a standalone application: it is installed in MS Outlook Desktop, Web, or Mobile implementation, or in the Chrome browser. {{ product_name }} provides access to Salesforce from MS Outlook Desktop, On the Web and Mobile, or Gmail / Google Workspace (G Suite), conveying all required details about to an email, task, or calendar item in real time. It allows to complete [routine and advanced business communication and CRM tasks](../All-User-Actions-in-Add-In-Sidebar/) with maximum effectiveness without ever leaving your email box to navigate to Salesforce.

Hosted on [secure Microsoft Azure cloud infrastructure](https://docs.microsoft.com/en-us/azure/security/azure-security-infrastructure), {{ product_name }} automatically synchronizes contacts, tasks, calendar items, etc. two-way with Salesforce, also applying [customized filters (views)](https://help.salesforce.com/articleView?id=listviews_parent.htm&type=5), user data access permissions, custom objects, and other peculiarities of your Org's configuration. Owing to [24/7 server-side data synchronization](../Synchronization-Engine-An-Overview/), [all your devices](../Using-on-iPhone/) connected to your mail sever can save data in Salesforce via [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/), and you can view, manage, and update CRM data via {{ product_name }} installed on [a supported platform](../Supported-Email-Clients-for-Microsoft-Exchange-2013,-2016/).

After you [install the Add-In](../How-to-Install-and-Run-the-Solution-for-Office-365-Mailboxes/) and [activate the Sync Engine](../Authorizing-Sync-Engine-to-Work-with-Your-Data/) for an email account, they become available in MS Outlook running on other configurations and devices compatible with Outlook on the Web, Outlook for Mac, iOS, or Android with the same account logged in.

{{ product_name }} is a combination of two [independent yet complementary components](../AddIn-vs-Sync-Functions/) – a server-side [synchronization engine](../Synchronization-Engine-An-Overview/) and a client-side [MS Outlook Add-In / Chrome Extension](../Introduction/) for Salesforce data displaying and conveying user input. The first part provides smart synchronization tools which allows business data to stay up-to-date across all devices capable to connect to a user's MS Exchange, Office 365, or Gmail account; whereas the mail app allows you to process all Salesforce object types including [custom ones](../How-to-Add-A-Custom-Object/), regulated by [a set of customizable parameters](../Customization-Settings-Explained/).

Being a cloud-based solution, {{ product_name }} does **not** require any special security roles or authorizations to be configured in your company's IT infrastructure. Any provisioned {{ short_name }} user in an Org who has an active Salesforce license and an MS Exchange, Office 365, or Gmail account can [set up {{ product_name }}](../Frequently-Asked-Questions/#scc_setup_by_individual_end_users) without involving the local Salesforce and Exchange Admins, using OAuth 2.0 and Single Sign-On mechanisms.

At the same time, if your company's standards require that, the solution can be effectively [mass-deployed for all end users in bulk](../Frequently-Asked-Questions/#bulk_scc_setup_by_local_mailsalesforce_admins) by a local Admin.

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#1_what_is_rg_email_sidebar_for_salesforce')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;

### 2\. On what platforms can I run {{ product_name }} for Salesforce?

{{ product_name }} is a multiplatform cloud solution, you can run it in MS Outlook Desktop or On the Web version on Windows, MacOS, iOS, Android, or in a [supported web browser](../Supported-Email-Clients-for-Microsoft-Exchange-2013,-2016/) on any platform. The full scope of {{ product_name }} features unfolds when it is used with MS Outlook 2013, 2016, 2019 on Windows or MacOS and in Office 365 running in a browser, however the Solution also provides solid and convenient Salesforce interaction when [used on mobile devices](../Using-on-iPhone/).

In addition, it is fully compatible with Gmail mailboxes via [{{ product_name }} Chrome Extension](../Chrome-Extension-Intro/), which you can use in Google Chrome browser or a [Chromium based](https://en.wikipedia.org/wiki/Chromium_(web_browser)) browser running on any supported platform on different kinds of devices.

Note that [{{ short_name }} user interface (Sidebar)](../Introduction/) is rendered identically in all its implementations: the "cloud" implementation in MS Outlook Desktop, [Outlook.com](https://outlook.live.com) and [Office 365](https://outlook.office.com/owa/) as well as in the ["desktop" implementation](../Desktop-MSI-and-Cloud-Web-Implementations-Comparison/). The [Gmaiil implementation](../How-to-Set-Up-the-Chrome-Extension-for-Salesforce-and-Gmail/) (the {{ short_name }} Chrome browser Extension) is also [mostly identical in its look and functions](../Using-the-Solution-for-Salesforce-and-Gmail/#differences_between_the_exchangeoffice_365_add-in_implementation_and_the_chrome_extension_for_gmail).

&nbsp;



#### Essential system requirements for running {{ product_name }}

&nbsp;

| Requirements                            | **Minimum**                                                  | **Recommended**                                              |
| --------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Operating system(s) with version number | Windows 7 or newer<br/>Mac OS X 10.5 or newer                | Windows 11<br/>Mac OS X Catalina                             |
| Hard drive free space                   | 1 Gb                                                         | 5 Gb                                                         |
| RAM                                     | 256 Mb                                                       | 2 Gb                                                         |
| Processor and speed                     | 500 MHz                                                      | 2 GHz                                                        |
| Monitor size                            | 13”                                                          | 17”                                                          |
| LAN speed                               | 1 Mb/s                                                       | 5 Mb/s                                                       |
| Other software                          | Microsoft Outlook 2013 and later<br />or a supported browser (see below) | MS Office 365<br/>MS Outlook 2019<br />or a supported browser (see below) |
| Server-side                             | MS Exchange 2016 or 2019 or Office 365 (with [Exchange Online](https://docs.microsoft.com/en-us/exchange/exchange-online))<br />MS Exchange 2013 has less stability for {{ company_name }} use in [Outlook on the Web](https://en.wikipedia.org/wiki/Outlook_on_the_web), but it runs smoothly in Outlook Desktop/Mobile implementations<br />MS Exchange 2010 is no longer supported | MS Exchange 2019 or Office 365 (with [Exchange Online](https://docs.microsoft.com/en-us/exchange/exchange-online)) |

&nbsp;

&nbsp;

#### Supported browsers (with Outlook on the Web)

&nbsp;

Outlook on the Web:

<https://outlook.com>  
<https://outlook.live.com>   
<https://outlook.office.com/>  
or custom corporate MS Outlook web access URLs



| **Browser**                                                  | **Supported**                                                |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| MS Edge (current and older versions)                         | Compatible<br /> See [this article](../Troubleshooting-Add-In-Could-Not-Be-Started/#if_none_of_microsoft_add-ins_work_or_sidebar_controls_become_unclickable) for MS Edge Chromium use specifics |
| Opera (current and older versions)                           | Compatible                                                   |
| Google Chrome (current and older versions)<br />and Chromium-based browsers | Full support                                                 |
| Firefox                                                      | Compatible                                                   |
| Safari (current and older versions)                          | Full support                                                 |
| MS Internet Explorer                                         | No longer supported due to security obsoletion               |

 <br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#2_on_what_platforms_can_i_run_rg_email_sidebar_for_salesforce')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;

### 3. How can I install the Solution? Is there a trial version to try out?

Refer to the following articles to learn how to install and run {{ product_name }}:

#### {{ short_name }} Setup by individual end users

- In [Office 365](../How-to-Install-and-Run-the-Solution-for-Office-365-Mailboxes/)

- [All configurations on MS Outlook for Windows](../How-to-Install-and-Run-the-Solution-all-configurations/)

- [The Chrome Extension to work with Gmail or Google Workspace (G Suite)](../How-to-Set-Up-the-Chrome-Extension-for-Salesforce-and-Gmail/)

- In [MS Outlook for iOS and Android](../How-to-Install-the-Solution-using-a-Mobile-Device/)

  

&nbsp;

#### Bulk {{ short_name }} Setup by local email/Salesforce Admins

- [All available deployment scenarios](../Email-Integration-Full-Deployment-Scenarios/)
- [Mass {{ short_name }} Add-In deployment in Office 365 in your Org](../Mass-Deployment-of-the-Add-In-Office-365/)
- [Mass {{ short_name }} Add-In deployment in MS Exchange in your Org](../Mass-Deployment-of-the-Add-In-MS-Exchange/)
- [Mass {{ short_name }} Sync authorization in your Org](../Set-up-Salesforce-Auth/)
- [Mass {{ short_name }} Chrome Extension (Gmail / Google Workspace (G Suite)) deployment your Org](../Chrome-Extension-Mass-Deployment/)

&nbsp;

#### {{ product_name }} Trial version

There is a *Trial version* of Email Sidebar available for download here: <https://revenuegrid.com/csm-wizard/>. {{ product_name }} Add-In / Chrome Extension is verified as secure and reliable by both [MS AppSource](https://appsource.microsoft.com/en-US/product/office/wa104379517) and [Chrome Web Store](https://chrome.google.com/webstore/detail/revenue-grid-for-salesfor/agfekjndkedoakoeahndfnjilkifbicn?hl=en). The trial's limitations: this version is identical to the full one, only limited to 14 days of use (extendable by request sent to our [Sales team](mailto:sales@revenuegrid.com)).  
If you don't feel like using your actual Salesforce data or [Salesforce sandbox](https://help.salesforce.com/articleView?id=data_sandbox_create.htm&type=5) to try out {{ product_name }} features, you may [run it with sample data](../Using-the-Add-In-with-Test-Data/).

&nbsp;

#### The free version of {{ product_name }} Add-In

Besides the trial version which you can download via the above link, there is the *Free version*. This version is activated in one of the following cases: if {{ product_name }} [is installed](../How-to-Install-and-Run-the-Solution-all-configurations/) for an email account without [purchasing a license](../Subscription-Plans-&-Pricing/) or if the license of an installed {{ product_name }} copy expires. This version has no access to {{ short_name }} Customization and Synchronization settings, and its [Sync Engine](../Synchronization-Engine-An-Overview/) is suspended.



&nbsp;

#### I've installed {{ product_name }} Add-In and I'm prompted to log in into it. What login and password should I enter? I wasn't provided any special login credentials for {{ short_name }}.

{{ product_name }} login is based on [Salesforce Single Sign-On](https://help.salesforce.com/articleView?id=sso_tips.htm&type=5) authentication, the credentials to be used is your Salesforce login and password; they are entered into the [Salesforce SSO window](https://docs.revenuegrid.com/ri/fast/articles/How-to-Install-and-Run-the-Solution-all-configurations/#2_logging_on_to_revenue_inbox) which is opened in your browser.

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#3_how_can_i_install_the_solution_is_there_a_trial_version_to_try_out')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
### 4\. Is data processed via {{ product_name }} transferred and stored securely? What servers and protocols are used by the Solution?

{{ product_name }} does not store any correspondence or CRM data processed over it, it solely transfers data between your email server and Salesforce over [secure Microsoft Azure protocols](https://docs.microsoft.com/en-us/azure/security/azure-security) with [TLS 1.2](https://www.ssl.com/article/tls-1-3-is-here-to-stay/) encryption; your email service and Salesforce access credentials are not kept in {{ product_name }}, the Solution's interactions with your email server and Salesforce are authorized via [OAuth 2.0](https://help.salesforce.com/articleView?id=remoteaccess_authenticate.htm&type=5) protocol on [{{ product_name }} setup](../How-to-Install-and-Run-the-Solution-all-configurations/). Refer to [this article](../Privacy-and-Security/) for complete information on our Privacy and Security standards. [Secure MS Azure datacenters](https://docs.microsoft.com/en-us/azure/security/fundamentals/overview) involved in data transfer and processing via {{ short_name }} are located on USA East coast, West coast, and in Western Europe. Note that {{ product_name }} servers' location does **not** noticeably affect processed email and CRM data transfer speed regardless of the end users' location, since their mail servers belong to Microsoft Exchange/Office 365 or Gmail infrastructures and all data transfer is carried out on the server side.

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#4_is_data_processed_via_rg_email_sidebar_transferred_and_stored_securely_what_servers_and_protocols_are_used_by_the_solution')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
### 5\. Does the ongoing [{{ company_name }} synchronization](../Synchronization-Engine-An-Overview/) consume much Internet traffic?

Since data exchange is carried out between your email server and Salesforce server while your local email client and the Add-In / Chrome Extension only serve to display data and convey your choices and actions, synchronization does not consume any noticeable amount of your local internet traffic. See [this article](../AddIn-vs-Sync-Functions/) for complete information on {{ short_name }} Sync engine's functions.

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#5_does_the_ongoing_revenue_grid_synchronization_consume_much_internet_traffic')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
### 6\. Does the ongoing {{ company_name }} synchronization generate many [Salesforce API calls](https://support.geckoboard.com/hc/en-us/articles/216804218-I-ve-hit-my-Salesforce-API-request-limit)?

No, the amount of API calls generated by {{ short_name }} is not very significant. {{ product_name }} has [integrated mechanisms](../Salesforce-API-Calls-Limit/) which prevent reaching of the [daily Salesforce API calls limit](https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm).

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#6_does_the_ongoing_revenue_grid_synchronization_generate_many_salesforce_api_calls')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
### 7\. {{ product_name }} creates multiple copies of the same calendar event in on [sync sessions](../Synchronization-Engine-An-Overview/), what should I do to fix that?

This behavior and other kinds of unexpected [sync behavior](../Synchronization-Engine-An-Overview/) usually indicate that there is other software transferring data between your email service and Salesforce API, causing data transfer conflicts with {{ product_name }}.
When you are using {{ product_name }} there should be no other software running that performs data transfer between your email service and [Salesforce API](http://trailhead.salesforce.com/modules/api_basics/units/api_basics_overview) (e.g. *Salesforce Lightning Sync*, *Salesforce Inbox*, *Salesforce for Outlook*, *Einstein Activity Capture*, etc.) Running different MS Exchange – Salesforce sync applications simultaneously will cause sync conflicts and items duplication. If you encounter this kind of unexpected behavior, please check that with your Salesforce admin or, if you are a Salesforce admin, check for such software in the following places:

* **1\.** Salesforce Setup > Apps > App Manager

* **2\.** [Connected Apps](https://help.salesforce.com/articleView?id=connected_app_overview.htm&type=5)

* **3\.** [Salesforce Login History](https://help.salesforce.com/articleView?id=users_login_history.htm&type=5)

After you find apps which cause sync conflicts, please refer to [this Salesforce Help article](https://dreamevent.secure.force.com/articleView?id=connected_app_delete.htm&type=5) to learn how to disable them. Please also note that apps which use Salesforce API and do **not** exchange data between Salesforce and MS Exchange / Office 365/Gmail will **not** cause sync conflicts.

Learn more about troubleshooting calendar events duplication in [this {{ company_name }} article](../duplication-troubleshooting/).

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#7_rg_email_sidebar_creates_multiple_copies_of_the_same_calendar_event_in_on_sync_sessions_what_should_i_do_to_fix_that')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
### 8\. How is {{ product_name }} priced? What subscription plans are available? Are there custom tailored solutions available?

Please refer to [this article](https://revenuegrid.com/pricing/) for detailed information on product plans and pricing. We also offer custom modifications of {{ product_name }} to suit our customers' preferences.  
You may also get {{ short_name }} from MS [AppSource 1](https://store.office.com/en-us/app.aspx?assetid=WA104379517) or [AppSource 2](https://appsource.microsoft.com/en-US/product/office/wa104379517), or the Gmail/Google Workspace implementation in [Google Web Store](https://chrome.google.com/webstore/detail/revenue-grid-for-salesfor/agfekjndkedoakoeahndfnjilkifbicn?hl=en). In addition, please do not hesitate to [contact our Sales Dept directly](mailto:sales@revenuegrid.com) with any questions.

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#8_how_is_rg_email_sidebar_priced_what_subscription_plans_are_available_are_there_custom_tailored_solutions_available')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;

### 9\. We installed the [MS Outlook Add-In](../How-to-Install-and-Run-the-Solution-all-configurations/) / [Chrome Extension](../How-to-Set-Up-the-Chrome-Extension-for-Salesforce-and-Gmail/) and [activated the Sync Engine](../Authorizing-Sync-Engine-to-Work-with-Your-Data/). What is the difference between these two components, what functions do they have?

See [this article](../AddIn-vs-Sync-Functions/) for in-depth information on the two {{ product_name }} components.

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#9_we_installed_the_ms_outlook_add-in_chrome_extension_and_activated_the_sync_engine_what_is_the_difference_between_these_two_components_what_functions_do_they_have')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;

### 10. Can I use the same Salesforce and {{ product_name }} account to process messages from my corporate mail via MS Outlook Add-In and from my Gmail via the [Chrome Extension](../Using-the-Solution-for-Salesforce-and-Gmail/)?

Such use scenarios are only viable if you have two dedicated Salesforce for every mailbox. Email and calendar data capturing processes, including [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/), are always tied to a specific email account. In addition, two {{ product_name }} licenses are required to do that.

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#10_can_i_use_the_same_salesforce_and_rg_email_sidebar_account_to_process_messages_from_my_corporate_mail_via_ms_outlook_add-in_and_from_my_gmail_via_the_chrome_extension')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;

### 11. Things are clear about [creating new Salesforce records](../All-User-Actions-in-Add-In-Sidebar/#2_creating_new_records_on_a_couple_of_mouseclicks), [updating them](../Synchronization-Engine-An-Overview/), [establishing associations among records](../All-User-Actions-in-Add-In-Sidebar/#7_automatedquick_selectionunselection_of_records), and [searching among them](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-(Adaptive-view)/#searching_for_records_in_salesforce_adaptive_view)... how can I delete a Salesforce object via {{ short_name }}?

To prevent unintentional data deletion risks, {{ product_name }} does **not** offer a direct possibility to delete an object from Salesforce, there are only several user-initiated possibilities carried out by [{{ short_name }} Sync engine](../AddIn-vs-Sync-Functions/):

- [Selective Calendar items unsync using the *Unsync* category](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#removing_from_salesforce_calendar_items_synced_by_mistake_salesforce_unsync)
- [Calendar items auto-deletion patterns](../Calendar-Items-Sync-Special-Patterns-Attendees-Lists,-Private-Items,-Item-Unsharing-and-Deletion/)  
- [One-way synchronization scenarios](../Special-Sync-Options-Save-Events-As-Other-&-One-Way-Sync/#one-way_synchronization)  
- Duplicate records merging via the Add-In/Extension, which is based on [Salesforce records merging](https://help.salesforce.com/articleView?id=contacts_merge.htm&type=5)  
- [Already saved Emails modifying in Salesforce](../Save-Email-Dialog/#editing_saved_emails_body)

&nbsp;

As a workaround, to quickly delete an Email, Event, or another object directly from the CRM, you may open it in Salesforce by clicking the <img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/open_in_sf.png" style="display: inline-block;vertical-align: middle;width: 18px;margin-left: 1px;height: 14px;object-fit: contain;"> icon next to [a business or person object](https://www.forcetalks.com/salesforce-topic/what-is-the-difference-between-whoid-and-whatid-how-can-we-associate-the-task-with-the-salesforce-opportunity-using-whatid) related to it in [{{ product_name }}](../All-User-Actions-in-Add-In-Sidebar/#4_viewing_details_instantly) and quickly delete it directly in Salesforce.

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#11_things_are_clear_about_creating_new_salesforce_records_updating_them_establishing_associations_among_records_and_searching_among_them_how_can_i_delete_a_salesforce_object_via_rges')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;

### 12. How does {{ product_name }} match specific fields of MS Exchange/O365 or Google Emails, Calendar items, Tasks, and Contacts with Salesforce objects fields?

Please see the comprehensive information on objects/fields matching patterns in [this article](../Object-Fields-Mapping-Patterns/).

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#12_how_does_rg_email_sidebar_match_specific_fields_of_ms_exchangeo365_or_google_emails_calendar_items_tasks_and_contacts_with_salesforce_objects_fields')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;

### 13. Dedicated Salesforce Emails, Salesforce Tasks, Salesforce Contacts folders or categories in email client created by {{ short_name }} Sync Engine

*What are the "Salesforce Emails", "Salesforce Contacts" folders and the custom "Salesforce", "Salesforce Unsync", "Tracked Successfully", and "Error" categories created in my MS Outlook or Gmail client after [{{ company_name }} synchronization](../Synchronization-Engine-An-Overview/) is [activated](../Authorizing-Sync-Engine-to-Work-with-Your-Data/)? Why do they appear again if I remove them, even though the {{ product_name }} is not opened or the Add-In is [disabled](../Uninstalling-All-Product-Components/)?*

These dedicated folders and custom categories are created in MS Outlook or Gmail on the initial [{{ short_name }} sync session](../Synchronization-Engine-An-Overview/); to get an email, calendar item, contact, or task saved in Salesforce by [{{ short_name }} synchronization](../Synchronization-Engine-An-Overview/), you need to move it to the corresponding custom folder or assign it the custom *Salesforce* category in MS Outlook. See [this article](../Saving-Calendar-Items-in-Salesforce-%28Adaptive-view%29/#custom_salesforce_categories_in_ms_outlook) for complete information.

This items handling mechanic is essential for {{ short_name }} synchronization, that's why these folders and the category are automatically re-created on the following sync session, if they were removed. These folders and the category work completely independently from the Add-In; they also might temporarily disappear after [customization reapplying](../Customization-Settings-Explained/), before synchronization creates them afresh.

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#13_dedicated_salesforce_emails_salesforce_tasks_salesforce_contacts_folders_or_categories_in_email_client_created_by_rges_sync_engine')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
### 14. What onboarding materials / user guides are available for the Solution?

This [Knowledge Base](https://docs.revenuegrid.com/ri/fast/) is the ultimate source of general information as well as specific guidelines, in-depth explanations, and administration instructions for {{ product_name }} for Salesforce. A selection of Knowledge Base articles can be exported to *.docx* or *.pdf* documents for your specific needs, upon request.

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#14_what_onboarding_materials_user_guides_are_available_for_the_solution')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
### 15. Can {{ company_name }} conduct {{ product_name }} use trainings for our company?

Remote trainings as well as onsite trainings can be arranged. Contact our [Support Team](mailto:support@revenuegrid.com) to request product training.

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#15_can_revenue_grid_conduct_rg_email_sidebar_use_trainings_for_our_company')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
### 16. I've added a field to an object in Salesforce and I do not see this field in {{ product_name }}, how to enable it?

To include the new added field into {{ product_name }} processing scope, open [{{ short_name }} Customization page](../Customization-Settings-Explained/) and [enable the added object field via its central pane](../Customization-Settings-Explained/#6_customizing_object_card_appearance_and_behavior). Also note that after you add a new object field in Salesforce, it may take up to 4 hours for the new field to be added to {{ short_name }} Customization central pane; if you want to force this update, click **Save** at the top of Customization page without making any changes - that will initiate refreshing of objects and fields in {{ short_name }} Customization configuration.

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#16_ive_added_a_field_to_an_object_in_salesforce_and_i_do_not_see_this_field_in_rg_email_sidebar_how_to_enable_it')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
### 17. Our Org uses custom Salesforce object(s) and I do not see these objects in {{ product_name }}, how to enable them?

Please refer to [this Knowledge Base article](../How-to-Add-A-Custom-Object/) for complete information on how to add custom objects to {{ short_name }} handling scope.

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#17_our_org_uses_custom_salesforce_objects_and_i_do_not_see_these_objects_in_rg_email_sidebar_how_to_enable_them')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
### 18. I have made adjustments in a calendar item in MS Outlook/Gmail calendar (or in Salesforce), but they did not [get mirrored](../Object-Fields-Mapping-Patterns/#ms_outlook_calendar_items) on the other end. How to fix that?

Calendar items syncing is carried out by [{{ short_name }} Sync Engine](../Synchronization-Engine-An-Overview/) on sync sessions performed on the server side. The regular sync sessions interval is 30 minutes, however, in the latest {{ short_name }} updates [calendar items instant sync](../Synchronization-Engine-An-Overview/#instant_sync_of_calendar_items) was introduced, so extra sync sessions get triggered on calendar items creation, updating, or deletion (if they are marked with the [custom Salesforce category](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#saving_calendar_items_semi-automatically)) – therefore these calendar updates will be synchronized in Salesforce within 1-3 minutes.  

What to check if calendar item update on either side is not reflected on the other:  

- Try [forcing {{ short_name }} sync](../How-to-Open-Sync-Dashboard-(Adaptive-view)/#forcing_scc_sync); make sure that {{ short_name }} sync is [set up](../Authorizing-Sync-Engine-to-Work-with-Your-Data/) and active (not paused or [suspended due to an error](../Handling-Sync-Issues/))  
- Read [this article]hat the calendar item being synced does not belong to the [exceptions which do not get mirror-synced](../Calendar-Items-Sync-Special-Patterns-Attendees-Lists,-Private-Items,-Item-Unsharing-and-Deletion/)  
- Calendar items which {{ short_name }} sync cannot process:  
  • MS Exchange / Office 365 [all-day events](https://support.office.com/en-us/article/create-an-all-day-event-52420de0-8f5a-41b2-a165-070588896c25) which have a duration of over 24 hours ([a Salesforce limitation](https://help.salesforce.com/articleView?id=creating_events_cex.htm&type=5))  
  • Series of recurring all-day events  
  • Calendar items set in [problematic time zones](../Historical-Sync-&-Timezones-Matching/#issues_with_uncommon_time_zones_handling)   
- In addition, refer to [this article](../Calendars-Syncing-Exceptions/) for detailed information on calendars syncing exceptions  
- Finally, there are several [customer-specific one-way synchronization options](../Special-Sync-Options-Save-Events-As-Other-&-One-Way-Sync/#one-way_synchronization) – check with your local Salesforce admin whether that might be the case in your Org  

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#18_i_have_made_adjustments_in_a_calendar_item_in_ms_outlookgmail_calendar_or_in_salesforce_but_they_did_not_get_mirrored_on_the_other_end_how_to_fix_that')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
### 19. I use several email accounts for my business correspondence and I want to connect both of them to my Salesforce account? How can I do that?

{{ product_name }} is based on the following fundamental principle: **one** email account is connected to **one** Salesforce account. Therefore, the above scenario is impossible to implement. For the same reason several Salesforce accounts cannot be connected to a single email account via {{ short_name }}.  
However, if such scenario is required, as a workaround you can set up your email accounts each connected to a separate Salesforce account within the same Org (requires an additional Salesforce and {{ product_name }} license). The same concerns using [{{ short_name }} Chrome Extension for Gmail](../Using-the-Solution-for-Salesforce-and-Gmail/).  
Also note that {{ short_name }} can automatically [recognize and match different MS Exchange / Office 365 alliases](../MS-Exchange-Aliases-Handling/) used for the same email account. 

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#19_i_use_several_email_accounts_for_my_business_correspondence_and_i_want_to_connect_both_of_them_to_my_salesforce_account_how_can_i_do_that')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
### 20. Can I use {{ product_name }} if I use MS Outlook Desktop to work with Gmail emails/events?

This {{ short_name }} use scenario is no longer officially supported. We recommend you to use Gmail / Google Workspace (G Suite) web interface and [{{ short_name }} for Salesforce and Gmail Chrome Extension](../Chrome-Extension-Intro/) instead.

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#20_can_i_use_rg_email_sidebar_if_i_use_ms_outlook_desktop_to_work_with_gmail_emailsevents')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
### 21. A Lead/Contact sometimes responds to an email thread using one's secondary email address (which is also registered in my Salesforce). Is there a way to [save](../Saving-Emails-in-Salesforce-1.-Function-Overview/) these responses in the same thread?

There is no way to get such an email properly saved [automatically](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_emails_emails_autosharing) or [via the dedicated category/folder](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#3_besides_using_the_save_button_emails_saving_can_be_performed_in_4_more_easy_ways); however, you can do that [using the *Save* button](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#1_saving_an_email_when_smartcloud_connect_synchronization_is_active) in [{{ product_name }}](../Introduction/)

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#21_a_leadcontact_sometimes_responds_to_an_email_thread_using_ones_secondary_email_address_which_is_also_registered_in_my_salesforce_is_there_a_way_to_save_these_responses_in_the_same_thread')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;
* * *
&nbsp;
### 22. My mobile device/workstation sometimes loses Internet connection, can I still use {{ product_name }}?

{{ product_name }} collects user input (selections, actions, fields entry and so on) via their email clients – using the [Add-In](../Introduction/) or [Chrome Extension](../Using-the-Solution-for-Salesforce-and-Gmail/), and transferring of that data in real time requires availability of Internet connection.

At that, [{{ short_name }} Sync engine](../Synchronization-Engine-An-Overview/) works on the server side and the mechanisms used for saving items in Salesforce over {{ short_name }} Sync are more fundamental, based on MS Outlook client ↔ MS Exchange / Office 365 server data transfer. If you save an email or calendar item (also an MS Outlook [Task](../Synchronization-of-Tasks/) or [Contact](../Synchronization-of-Contacts/)) from your email client using the custom Salesforce folder or category, the moment your client gets connected to your mail server this item's syncing in Salesforce will be initiated.

This way, you can mark items to be saved while offline and as soon as connection becomes available, their syncing will start. See the following articles to learn how to save items via the dedicated folder/custom category:

[Emails](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/#3_besides_using_the_save_button_emails_saving_can_be_performed_in_4_more_easy_ways)  

[Calendar items](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/#saving_calendar_items_semi-automatically/)  

[On mobile devices](../Using-on-iPhone/)  

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#22_my_mobile_deviceworkstation_sometimes_loses_internet_connection_can_i_still_use_rg_email_sidebar')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;

* * *
&nbsp;
### 23. Why does {{ company_name }} always link saved Activities (emails and calendar items) to an Account?

This mandatory pattern is based on a Salesforce requirement, see Salesforce Help [article 1](https://help.salesforce.com/articleView?id=000336268&type=1&mode=1) and [article 2](https://help.salesforce.com/articleView?id=000336268&type=1&mode=1) for more information. The exception is Tasks, EmailMessages, or Calendar Events linked to a Lead, since Leads require no Salesforce Account registration.

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#23_why_does_revenue_grid_always_link_saved_activities_emails_and_calendar_items_to_an_account')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;

* * *
&nbsp;

### 24. Does {{ company_name }} allow handling items from an [Exchange shared mailbox](https://support.office.com/en-US/article/Open-and-use-a-shared-mailbox-in-Outlook-Web-App-BC127866-42BE-4DE7-92AE-1EF2F787FD5C)?

Yes, most [{{ short_name }} use scenarios](../Introduction/) are supported for Exchange shared mailboxes. See [this article](../Shared-Mailbox/) for more information.

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#24_does_revenue_grid_allow_handling_items_from_an_exchange_shared_mailbox')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;

* * *
&nbsp;

### 25. How to increase the size of [{{ product_name }}](../Introduction/) font and controls to make it more accessible for users with lower vision?

You can "zoom in" the Sidebar the way you zoom in web pages. To do that, click on the Sidebar, press the *Control (Ctrl)* button and scroll up the mouse wheel. All Sidebar components will be expanded and slightly re-arranged.
To accommodate the expanded controls in the Sidebar's pane, you can also stretch the Sidebar sideways: hover the cursor over the left-hand edge of the Sidebar so it looks like this **⇼**, then hold the left mouse button and stretch the Sidebar to the left.
Presently, the zoomed in Sidebar layout is not kept for different selected items.

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#25_how_to_increase_the_size_of_rg_email_sidebar_font_and_controls_to_make_it_more_accessible_for_users_with_lower_vision')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;

* * *

&nbsp;

### 26. I have [activated {{ company_name }} Sync](../Authorizing-Sync-Engine-to-Work-with-Your-Data/), but [Sync engine functions](../AddIn-vs-Sync-Functions/) appear not to be working. 

**1\.** [Check whether Sync is active](../How-to-Open-Sync-Dashboard-(Adaptive-view)/)

**2\.** [Investigate the Issues log for any errors](../Handling-Sync-Issues/) and [resolve their causes](../Sync-Issues-Troubleshooter/)

**3\.** In case Sync has been activated just recently and it appears to be up and running but [Sync functions](../Synchronization-Engine-An-Overview/) are not carried out, check that  it was activated for the same email box as one for which you installed the [Add-In](../Introduction/)

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#26_i_have_activated_revenue_grid_sync_but_sync_engine_functions_appear_not_to_be_working')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;

* * *

&nbsp;

### 27. Can Salesforce data corruption occur under any circumstances when it's handled by {{ product_name }}, e.g. when my Internet connection is unstable?

Data processing and transfer via {{ product_name }} excludes the possibility of data corruption, the only known case of excessive data creation in Salesforce by {{ short_name }} Sync occurs in the situation described in the [entry 7 of this FAQ article](../Frequently-Asked-Questions/#7_rg_email_sidebar_creates_multiple_copies_of_the_same_calendar_event_in_on_sync_sessions_what_should_i_do_to_fix_that).

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#27_can_salesforce_data_corruption_occur_under_any_circumstances_when_its_handled_by_rg_email_sidebar_eg_when_my_internet_connection_is_unstable')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;

* * *

&nbsp;

### 28. My company purchased several licenses of {{ product_name }}. How can I manage various aspects of the Solution's functioning, e.g. the end users' [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/) and their access to [Customization settings](../Customization-Settings-Explained/), or adjust the [under-the-hood settings](../Special-Admin-Panel-Settings/)?

That can be done via [{{ product_name }} Admin panel](../How-to-Log-In-to-the-Admin-Panel/). Admin panel access is available exclusively for [Enterprise {{ short_name }} customers](https://revenuegrid.com/pricing/). To access the panel, check with your local administrator whether they have the access URL and credentials provided to them on product purchase. Or, if you are the administrator or account owner, [send us](mailto:support@revenuegrid.com) a corresponding request to gain the access.

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#28_my_company_purchased_several_licenses_of_rg_email_sidebar_how_can_i_manage_various_aspects_of_the_solutions_functioning_eg_the_end_users_rges_sync_and_their_access_to_customization_settings_or_adjust_the_under-the-hood_settings')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;

* * *

&nbsp;

### 29. What Exchange data access permissions (Admin consent) does {{ product_name }} require? Is it possible to limit this App to be used only by specific users or groups of users in our company?

Yes, the local Admin can selectively deploy the Add-In for everyone or for specific users or groups of users in the company. See [article 1](../Email-Integration-Full-Deployment-Scenarios/) and [article 2](../Mass-Deployment-of-the-Add-In-Office-365/) and [this Microsoft article](https://docs.microsoft.com/en-us/microsoft-365/admin/manage/manage-deployment-of-add-ins?view=o365-worldwide) for details. 

{{ product_name }} can be granted permissions to work with your Org's Exchange data via consent settings applied for:

**A.** For all users in the Org ([Admin consent permissions](https://docs.microsoft.com/en-us/exchange/permissions/permissions?view=exchserver-2019))  
**B.** For individual users to have a choice ([User consent permissions](https://docs.microsoft.com/en-us/microsoft-365/admin/misc/user-consent?view=o365-worldwide))  
**C.** The Admin sets up {{ short_name }} and [enables self-service access](https://docs.microsoft.com/en-us/office365/servicedescriptions/exchange-online-service-description/exchange-online-setup-and-administration#self-service-administration-tools) or assigns the users directly to the application. The Admin can grant consent on behalf of all users in this directory, ensuring that the end users will not be requested to give consent to run {{ product_name }}   

!!! tip "Tip"
    Also see these articles to learn more: [about users provisioning in {{ short_name }} Admin panel](../Managing-Users-via-the-Solution-s-Admin-Panel/) and [about available deployment scenarios](../Email-Integration-Full-Deployment-Scenarios/)

&nbsp;

The following mail server data access permissions settings are required:

&nbsp;

##### For EWS mail server connection

This mail server connection type is currently the default one for both MS Exchange mail servers. See complete information on this connection type in [this article](../Working-With-EWS/). This connection type's limitation is that it does <u>not</u> allow to configure data access permissions in a flexible way: it allows either all user Email, Calendar, Tasks, and Contacts data access for {{ short_name }} or none. Therefore, for this connection type no limited data access deployment options are available to meet special security demands which some Enterprise environments may have. The alternative that includes this possibility is MS Graph connection for O365, see the next FAQ section for details.

*EWS-specific Admin Consent permissions set (EWS.AccessAsUser.All):*

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\API_permissions.png">
</p></details>

&nbsp;

For O365 [with Exchange Online](https://docs.microsoft.com/en-us/exchange/exchange-online) servers, individual end users approve their data access over [O365 OAuth](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow).

&nbsp;

##### For [MS Graph](../MS-Graph/) O365 server connection

MS Graph connection type can be configured to provide access to very different end user data types, ensuring maximum flexibility and security; however, presently, it [does not support  all {{ product_name }} functions](../MS-Graph/#ms_graph_limitations).

*MS Graph Admin Consent permissions*

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\graph_admin.png">
</p></details>
&nbsp;

*MS Graph User Consent permissions*

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\graph_user.png">
</p></details>

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#29_what_exchange_data_access_permissions_admin_consent_does_rg_email_sidebar_require_is_it_possible_to_limit_this_app_to_be_used_only_by_specific_users_or_groups_of_users_in_our_company')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>


&nbsp;

* * *

&nbsp;

### 30. I've opened {{ product_name }} and cannot see the icons Book Me, Time Slots, Engagement, etc. at the bottom. How to fix that?

See [this article](../Manage-Smart-Actions/) to learn how to manage the [Smart Action icons](../All-User-Actions-in-Add-In-Sidebar/#smart_actions) via [{{ short_name }} Customization settings](../Customization-Settings-Explained/).  
Besides that, note that the Book Me and Time Slots actions are not displayed if you select a meeting invite message in Inbox or Sent folders. 

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#30_ive_opened_rg_email_sidebar_and_cannot_see_the_icons_book_me_time_slots_engagement_etc_at_the_bottom_how_to_fix_that')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&#160;

* * *

&#160;

### 31. Does {{ company_name }} allow handling items for an [Exchange Delegated Access use](https://support.microsoft.com/en-us/office/allow-someone-else-to-manage-your-mail-and-calendar-41c40c04-3bd1-4d22-963a-28eafec25926)?

Some use scenarios are supported for MS Exchange Delegate Access configurations. See [this article](../Using-MS-Outlook-Delegated-Calendars/) for more information.

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#31_does_revenue_grid_allow_handling_items_for_an_exchange_delegated_access_use')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;

* * *

&nbsp;

### 32. When I try to authorize {{ company_name }} to access my Office 365 data, I get a "Need Admin Approval" error. How to tackle that?

See [this article](../Need-Admin-Approval/) for instructions how to resolve this issue.

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#32_when_i_try_to_authorize_revenue_grid_to_access_my_office_365_data_i_get_a_need_admin_approval_error_how_to_tackle_that')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;

* * *

&nbsp;

### 33. I [synchronized](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/) an Outlook calendar Meeting / Appointment in Sales by mistake, how can I delete it via {{ product_name }}?

{{ product_name }} can delete Salesforce Events it created to match synced Outlook calendar items. To initiate deletion of a matching Salesforce Event, simple [assign the custom *Salesforce Unsync* category](../Saving-Calendar-Items-in-Salesforce-%28Adaptive-view%29/#removing_from_salesforce_calendar_items_synced_by_mistake) to the item in Outlook calendar. The Salesforce Event will be deleted not immediately but within 1 to 30 minutes on the following [Sync session](../Synchronization-Engine-An-Overview/).

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#33_i_synchronized_an_outlook_calendar_meeting_appointment_in_sales_by_mistake_how_can_i_delete_it_via_rg_email_sidebar')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;

* * *

&nbsp;

### 34. How does {{ product_name }} convey Events created or modified in Salesforce to MS Outlook or Gmail calendar?

Such Events are handled automatically by {{ short_name }} Sync engine. See the following articles for all details:

- [Events "down-syncing" from Salesforce](../Saving-Calendar-Items-in-Salesforce-%28Adaptive-view%29/#events_down-syncing_from_salesforce_to_mail_clients_calendar)
- [General handling principles](../Choosing-What-to-Synchronize/#synchronizing_tasks_and_calendar_events)
- [Specific sync scenarios detailing](../Calendar-Items-Sync-Special-Patterns-Attendees-Lists%2C-Private-Items%2C-Item-Unsharing-and-Deletion/)

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#34_how_does_rg_email_sidebar_convey_events_created_or_modified_in_salesforce_to_ms_outlook_or_gmail_calendar')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;

* * *

&nbsp;

### 35. For security considerations our company uses [Shield Platform Encryption](https://help.salesforce.com/articleView?id=sf.security_pe_concepts.htm&type=5). Can we still use {{ product_name }}?

{{ product_name }} is compatible with some SPE deterministic encryption setups; that depends on what objects get encrypted and what algorithm is applied. Please submit a request with these details to [our CSM team](mailto:support@revenuegrid.com) to find out if your SPE configuration is supported.

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#35_for_security_considerations_our_company_uses_shield_platform_encryption_can_we_still_use_rg_email_sidebar')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;

* * *

&nbsp;

### 36. Some {{ product_name }} elements become completely unclickable in MS Outlook (Desktop) on Windows OS. How to fix that?

The issue where important [Sidebar elements](../Introduction/) become unclickable, e.g. the *Save* or *Create* button, has a technical cause on Microsoft Outlook side. Specifically, due to the ongoing Microsoft transition from the old MS Edge to [Chromium MS Edge](https://support.microsoft.com/en-us/microsoft-edge/download-the-new-microsoft-edge-based-on-chromium-0f4a3dd7-55df-60f5-739f-00010dba52cf) some MS Outlook for Windows versions have an Outlook frames rendering issue with MS Edge. Microsoft is planning to roll out a complete solution in a [future MS Windows update](https://blogs.windows.com/msedgedev/2020/10/19/edge-webview2-general-availability/).

In the meantime, follow the provided steps in [this article](../Troubleshooting-Add-In-Could-Not-Be-Started/#if_none_of_microsoft_add-ins_work_or_sidebar_controls_become_unclickable) to apply an [official workaround provided by Microsoft](https://developer.microsoft.com/en-us/office/blogs/office-add-ins-community-call-february-10-2021/). Also see [this Microsoft article](https://developer.microsoft.com/en-us/microsoft-365/blogs/understanding-office-add-ins-runtime/) for more information.

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#36_some_rg_email_sidebar_elements_become_completely_unclickable_in_ms_outlook_desktop_on_windows_os_how_to_fix_that')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;

* * *

&nbsp;

### 37. What is the purpose of the [Salesforce managed package](https://help.salesforce.com/articleView?id=sf.sharing_apps.htm&type=5) offered by {{ company_name }} to support its solutions? Are these mandatory to install?

There are 3 free [Salesforce managed packages](https://help.salesforce.com/articleView?id=sf.sharing_apps.htm&type=5) that we developed for our customers and keep improving to ensure full {{ company_name }} components compatibility with Salesforce for a seamless integration experience. All managed package updates meet [{{ company_name }} Data Privacy and Security standards](https://revenuegrid.com/privacy-policy/) and [get reviewed by Salesforce AppExchange specialists](https://developer.salesforce.com/docs/atlas.en-us.packagingGuide.meta/packagingGuide/security_review_overview.htm). Each package serves to perform {{ company_name }} functions and expand Salesforce functions.  
Specifically: 

**A\.** The [{{ company_name }} + Revenue Guide managed package](../Admin-Managed-Package/). It is also used to [configure {{ company_name }} widgets](https://docs.revenuegrid.com/articles/sfdc-widgets/#opportunity_and_account_widgets) in Salesforce interface. This package is mandatory to install in a Salesforce Org to use the solutions   

**B\.** The managed package required for [unrolling all Revenue Engage functions](https://docs.revenuegrid.com/articles/engage-mp/). This package is mandatory to install in a Salesforce Org to use Revenue Engage    

**C\.** The obsolete [Invisible Suite package](../Setting-Up-Invisible-Suite-Managed-Package-in-Salesforce/). It is no longer used, except for specific old configurations    

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#37_what_is_the_purpose_of_the_salesforce_managed_package_offered_by_revenue_grid_to_support_its_solutions_are_these_mandatory_to_install')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;

* * *

&nbsp;

### 38. I see {{ company_name }} and {{ company_name }} are ever-evolving, obtaining new features and functions every several months. Where can I check the schedule of solution's feature updates?

We unroll a major update on a monthly basis and a couple of intermediate Hotfix updates in between, see the release notes: [{{ company_name }} all packages](https://docs.revenuegrid.com/articles/release-notes/), [{{ company_name }} Email Sidebar](../Release-Notes/).

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#38_i_see_revenue_grid_and_revenue_grid_are_ever-evolving_obtaining_new_features_and_functions_every_several_months_where_can_i_check_the_schedule_of_solutions_feature_updates')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;

* * *

&nbsp;



### 39\. I want to use {{ company_name }} to work with data from a [Salesforce Customer / Partner Community DB](https://help.salesforce.com/articleView?id=000335630&type=1&mode=1). How can I do that?

See [this article](../Partner-Community-Authorization/) to learn how to configure {{ company_name }} to work with Customer / Partner Community CRM data.

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#39_i_want_to_use_revenue_grid_to_work_with_data_from_a_salesforce_customer_partner_community_db_how_can_i_do_that')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;

* * *

&nbsp;

### 40\. How does {{ short_name }} handle data for [Salesforce Customer / Partner Community](https://help.salesforce.com/articleView?id=000335630&type=1&mode=1) users? Is the flow secure and isolated?

Salesforce Customer / Partner Community users' data handling is performed in an isolated targeted manner that always observes the [access rules set for individual users or groups of users in Salesforce](https://help.salesforce.com/s/articleView?id=sf.perm_sets_overview.htm&type=5). See [this article](../Partner-Community-Integration/) for detailed information about {{ short_name }} data handling for such scenarios.

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#40_how_does_rges_handle_data_for_salesforce_customer_partner_community_users_is_the_flow_secure_and_isolated')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>

&nbsp;

* * *

&nbsp;

### 41\. Why do *Activity Timeline* and other pinned sections in {{ short_name }} Chrome extension not show any data?

<p>
    <img src="..\..\assets\images\faq\41\41.png" style="width:43%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

*Activity Timeline* and object sections are designed to show parsed information from Salesforce after the **email is opened**. Chrome extension has a state when none of the emails are opened (e.g. while viewing *Inbox* or *Sent* folders), but all pinned in <a href="../Customization-Settings-Explained/" target="_blank">Customization settings</a> sections/objects are displayed.

This is the expected behavior, and the information will appear after opening an email as a result of the <a href="../Initial-Search-and-Applied-Record-Filters/" target="_blank">Initial Search</a> process.

<br><button class="button copy-to-clipboard" style="float: right;" onclick="setClipboard('https://docs.revenuegrid.com/ri/fast/articles/Frequently-Asked-Questions/#41_why_do_activity_timeline_and_other_pinned_sections_in_rges_chrome_extension_not_show_any_data')">Copy link to this question<img src="../../assets/images/faq/copy.svg"></button>