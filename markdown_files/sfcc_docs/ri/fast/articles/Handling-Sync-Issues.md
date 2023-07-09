---
description: Detailed overview of synchronization issues and ways to address them
---
# Handling Synchronization Issues  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>
<div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>
<div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*8 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

When using [{{ short_name }} Sync functions](../Synchronization-Engine-An-Overview/), sometimes you may encounter particular mailbox → Salesforce data synchronization issues that can block syncing of certain items or even disable the synchronization completely.

This article provides a detailed overview of how to identify and investigate synchronization issues and ways to address them.

&nbsp;
***
&nbsp;

## Identify synchronization issues

<br>
There are several ways how you can find out that a sync issue has occurred and some data failed to be synchronized between your mailbox and Salesforce.
<br><br>

**1\.** As a first sign of a synchronization issue, {{ product_name }} will mark an affected object in your mailbox with a **custom category**, **label**, or **color** to let you know about it:

<br>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sync-Issues\ms-cat.png" style="width:60%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

* In MS Outlook, the item for which a sync issue occurred is assigned two custom categories: a red "*Sync Error*" category and a white category providing extra details

<br><br><br>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sync-Issues\gmail-labels.png" style="width:43.75%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

* In Gmail mail client, the item for which a sync issue occurred is assigned a custom label "*Sync Error*" or a red marker for calendar items

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sync-Issues\gmail-event-label.png">
</p>

<br><br><br>

**2\.** Another way to identify sync issues is to check the logged data on the **Sync Settings** page. {{ product_name }} logs all occurred synchronization issues and errors in Sync Setting, providing an ability to monitor, investigate, and resolve them efficiently.

&nbsp;

**3\.** In addition, all issues [are also registered in **{{ short_name }} Admin panel**](../Monitoring-Users-and-Organizations/) for monitoring and resolution by the local Admin.

&nbsp;

!!! warning "Important"
    Depending on your license, the appearance of your Sync Settings page may be different. Below you can find information on how to handle synchronization issues on the **New** and **Legacy** Sync Settings pages. Refer to the chapter that corresponds to the appearance of your Sync Setting page:
    
    * [New Sync Settings page](#handling_sync_issues_on_the_new_sync_settings_page)
    * [Legacy Sync Settings page](#handling_sync_issues_on_the_legacy_sync_settings_page)

&nbsp;
***
&nbsp;

## Handling sync issues on the [new Sync Settings page](../Configuring-Activities-Synchronization-Settings-rg/)

&nbsp;

### Investigate synchronization issues

<br>
When {{ short_name }} Sync Engine encounters conflicts between synchronized data sources or is unable to run synchronization to less obvious reasons, all synchronization issues details are reflected in Sync Settings on the **General** and **Issues** tabs.

To conduct an issue investigation, you need to check the logged information, which can include the issue cause description, advice for resolving it, or a [sync error code](../Sync-Issues-Troubleshooter/).

&nbsp;

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sync-Issues\sync-settings.png" style="width:27.48%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

To access **Sync Settings**, open {{ product_name }} in your mailbox, click **Menu**, and go to **Sync Settings**.

<br><br><br>

#### General tab

On the General tab in Sync Settings, you can check the synchronization status, the last sync session details, as well as **sync error messages** if any occurred.

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sync-Issues\auth-error.png">
</p>
<br>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sync-Issues\session-details.png" style="width:49.17%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<br>

* Click **Last session details** to view the logged information about the last synchronization. Also, use the **Refresh** button to update the details if another sync session has run recently.

<br><br><br><br>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sync-Issues\show-details.png" style="width:19.55%; display:inline-block; vertical-align:middle; margin-left:12px;float: right">
</p>

* If there is a sync error message, click **Show details** to see the detailed error description and recommendations on how to address it, when available

<br><br>

#### Issues tab

On the Issues tab, you can find the issue’s log, which usually includes a [sync error code](../Sync-Issues-Troubleshooter/) or notification returned by {{ product_name }} and indicates the source of the error, date and time when the error occurred

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sync-Issues\issues-list.png">
</p>

!!! tip "Tip"
    You can instantly view the Salesforce or MS Exchange / Office 365 / Google record that caused the issue by clicking the mail client or Salesforce icon under **Connectivity**

<br><br>

#### Account credentials changed

When your Salesforce or MS Exchange / Office 365 / Google credentials are changed, {{ product_name }} can no longer access your data, and the corresponding Sync error message appears on the [**General**](#general_tab) tab in Sync Settings.

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sync-Issues\auth-error-details.png">
</p>
<br>

Also, refer to the [Credentials renewing](#renewing_salesforce_or_mail_data_access_credentials) section below for more information.
<br><br>

In addition, for cases when {{ product_name }} is unable to access your Salesforce or mailbox data or when data syncing fails 10 times consecutively, you will receive a **notification email** informing you about the need for action to resolve the issue and resume data syncing.
<br><br>

&nbsp;
***
&nbsp;

### Resolve synchronization issues

Once you investigate the sync issue, you need to follow the handling recommendations described in the issue details. If there are no recommendations, proceed with the following steps to address it:

* If the issue occurred because required data was missing or invalid data was entered into some field, enter or correct the corresponding data

* If the issue occurred due to authorization problems, refer to the [Credentials renewing](#renewing_salesforce_or_mail_data_access_credentials) section below for a solution

* If the issue has an error code, consult [the table of Sync error codes](../Sync-Issues-Troubleshooter/) for a solution

* For the cases when you or your admin cannot resolve an issue locally, it is recommended to contact our [Support and CSM team](mailto:support@revenuegrid.com):

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sync-Issues\support.gif" style="width:32.1%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<p style="margin-left:6%">
    On the Issues tab, click <b>&#8942;</b> (More) icon under <b>Actions</b>, click <b>Chat with support</b>, and send a report to our team. Make sure to include details and screenshots, when applicable.
</p>

&nbsp;

&nbsp;

!!! warning "Important"
    Note that when you are using {{ product_name }} there should be no other software running that performs data transfer between MS Exchange and [Salesforce API](http://trailhead.salesforce.com/modules/api_basics/units/api_basics_overview) (e.g. Salesforce Lightning sync, Salesforce Inbox, Salesforce for Outlook, etc.) Running different MS Exchange – Salesforce sync applications simultaneously will cause sync conflicts and items duplication. If you encounter this kind of unexpected behavior, please check that with your Salesforce admin or, if you are a Salesforce admin, check for such software in the following places:
    
    1. **[Salesforce Setup](http://help.salesforce.com/articleView?id=basics_nav_setup.htm) > Apps > App Manager**  
    2. [Connected Apps](http://help.salesforce.com/articleView?id=connected_app_overview.htm&type=5)  
    3. [Salesforce Login History](http://help.salesforce.com/articleView?id=users_login_history.htm&type=5). After you find apps which cause sync conflicts, please refer to [this Salesforce help article](https://dreamevent.secure.force.com/articleView?id=connected_app_delete.htm&type=5) to learn how to disable them. Please also note that apps which use Salesforce API but do not exchange data between Salesforce and MS Exchange will not cause sync conflicts

&nbsp;

&nbsp;

* * *

&nbsp;

## Handling sync issues on the legacy Sync Settings page

* **Issues.** Synchronization issues are logged in the tab when {{ short_name }} Sync Engine encounters conflicts between synchronized data sources or due to less obvious reasons. Every issue's log usually includes a sync error code or notification returned by {{ product_name }} and indicates the source of the error. Also see [this article](../Sync-Issues-Troubleshooter/) for a table of possible Sync errors  

<p><img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\574d8ac5c6979138ff609d3c.png">
</p>

&nbsp;

* **Account credentials changed.** Occurs if your Salesforce or MS Exchange / Office 365 / Gmail credentials were changed and {{ product_name }} can no longer access your data. See the section below [Credentials renewing](../Handling-Sync-Issues/#renewing_salesforce_or_mail_data_access_credentials) for more information  

<p><img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\574d8c559033605108fde741.png">
</p>

&nbsp;

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sync-Issues\sync-issues.png" class="minimized">
</p>

&nbsp;

Additional information about each Sync issue can be found [in the Dashboard](../How-to-Open-Sync-Dashboard-(Adaptive-view)/). If your local Admin cannot resolve the issue locally, you can get our [Support Team](mailto:support@revenuegrid.com)'s assistance by clicking the **Help me resolve this issue** button under an issue and submitting a detailed description including error codes and screenshots by email.

In addition, for cases when {{ product_name }} is unable to access your Salesforce or mailbox data or when data syncing fails for 10 times consecutively, you will receive a notification email informing about the need for action to resolve the issue and resume data syncing.

&nbsp;

In case a persistent Sync issue occurs, for example due to Sync misconfiguration or [user account switching to another tenant](../Managing-Users-via-the-Solution-s-Admin-Panel/), see [this article](../Revoke-Token/) to learn how to revoke Sync data authorization token. After that, [re-activate Sync for the mailbox](../Authorizing-Sync-Engine-to-Work-with-Your-Data/).

&nbsp;

* * *

&nbsp;

### Investigate synchronization issues

A synchronization issue occurs when {{ product_name }} is unable to synchronize data between Salesforce and Microsoft Exchange / Office 365 / Gmail due to some reason. In many cases, these issues are caused by required data unavailability on email server side, e.g. missing Contact key fields values, like Last name, or by specific Salesforce rules that may prevent users from editing or deleting records of certain types.

When a Sync issue occurs, {{ product_name }} notifies the concerned users in the following ways:  

* In MS Outlook, the item for which a Sync issue occurred is assigned two custom categories: a red *“Sync Error”* category and a white category providing extra details  

<p>
    <img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5832fc42903360645bfa6a98.png">
</p>

&nbsp;

In Gmail mail client, the item for which a Sync issue occurred is assigned a red marker (Events) or a custom label *"Salesforce Emails/Sync Error"*

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sync-Issues\gmail-error-category.png">
    <br><br><br>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Sync-Issues\event-error-category.png">
</p>

&nbsp;

* Information about logged sync issues is displayed on the **Issues** tab of [{{ product_name }}'s Dashboard](../How-to-Open-Sync-Dashboard-(Adaptive-view)/). To view issues for a certain processed item type: under **Issues**, select issue type. Note that you can instantly view the Salesforce (or MS Exchange) item that caused the issue by clicking the **Salesforce** or **Exchange** icon on the right  

<p>
    <img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\574d89849033605108fde730.png">
</p>

&nbsp;

- All issues [are also registered in {{ short_name }} Admin panel](../Monitoring-Users-and-Organizations/) for monitoring and resolution by the local Admin

&nbsp;

&nbsp;

### Resolve synchronization issues

* If the issue occurred because a required (key) field was left empty, fill in the missing key fields

* Consult [the table of Sync error codes](../Sync-Issues-Troubleshooter/) for a solution

* For the cases when an issue cannot be resolved locally, it is recommended to contact our [Support and CSM team](mailto:support@revenuegrid.com): you can click the **Help me resolve this issue** button and send a report; make sure to include details and screenshots, when applicable

<p><img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5832fc5b903360645bfa6a9b.png">
</p>

&nbsp;

!!! warning "Important"
    Note that when you are using {{ product_name }} there should be no other software running that performs data transfer between MS Exchange and [Salesforce API](http://trailhead.salesforce.com/modules/api_basics/units/api_basics_overview) (e.g. Salesforce Lightning sync, Salesforce Inbox, Salesforce for Outlook, etc.) Running different MS Exchange – Salesforce sync applications simultaneously will cause sync conflicts and items duplication. If you encounter this kind of unexpected behavior, please check that with your Salesforce admin or, if you are a Salesforce admin, check for such software in the following places:  
    **1.** **[Salesforce Setup](http://help.salesforce.com/articleView?id=basics_nav_setup.htm) > Apps > App Manager**  
    **2.** [Connected Apps](http://help.salesforce.com/articleView?id=connected_app_overview.htm&type=5)  
    **3.** [Salesforce Login History](http://help.salesforce.com/articleView?id=users_login_history.htm&type=5). After you find apps which cause sync conflicts, please refer to [this Salesforce help article](https://dreamevent.secure.force.com/articleView?id=connected_app_delete.htm&type=5) to learn how to disable them. Please also note that apps which use Salesforce API but do not exchange data between Salesforce and MS Exchange will not cause sync conflicts

&nbsp;

&nbsp;

* * *

&nbsp;

## Renewing Salesforce or Mail Data Access Credentials

If Exchange / Office 365 / Google or Salesforce access credentials expire or get changed, {{ product_name }} can no longer synchronize users' data. After that happens, affected end users or their Admin receive a notification email with instructions how to re-activate the Sync Engine via [the Sidebar](../Introduction/); a corresponding notification will also appear in users' [{{ short_name }} Dashboard](../How-to-Open-Sync-Dashboard-(Adaptive-view)/).

To renew MS Exchange / Office 365 or Salesforce access for {{ short_name }} Sync Engine, follow the steps provided in [this article](../Renewing-Exchange-and-Salesforce-Account-Credentials/).

<br>

In case a persistent Sync issue occurs, for example due to Sync misconfiguration or [user account switching to another tenant](../Managing-Users-via-the-Solution-s-Admin-Panel/), see [this article](../Revoke-Token/) to learn how to revoke Sync data authorization token. After that, [re-activate Sync for the mailbox](../Authorizing-Sync-Engine-to-Work-with-Your-Data/).

Also see additional details on Salesforce access renewal in [this article](../Set-up-Salesforce-Auth/#re-establishing_connection_after_refresh_token_expiration).

&nbsp;

&nbsp;

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
