---
search:
  exclude: true
---

# [Deprecated!] Invisible Suite Managed Package  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*3 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! warning "Important"
    The obsolete Invisible Suite managed package was removed from general use. Please only use the [updated {{ company_name }} Managed package](../Admin-Managed-Package/) instead
	
&nbsp;

&nbsp;

&nbsp;

To enable the full scope of {{ product_name }} features after [installing the Solution](../How-to-Install-and-Run-the-Solution-all-configurations/), the local Salesforce Admin should make several minor adjustments in Salesforce configuration: add special auxiliary custom fields and classes.

{{ company_name }} automated and facilitated this step by introducing the Invisible Suite [managed Salesforce package](http://developer.salesforce.com/docs/atlas.en-us.appExchangeInstallGuide.meta/appExchangeInstallGuide/appexchange_install_notification.htm).

!!! note "Note"
    The managed package is guaranteed to be secure, confidential, and free of any malicious content, under [{{ company_name }} Privacy & Security policies](../Privacy-and-Security/)

&nbsp;

#### To install the Invisible Suite package

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1\.** Make sure that you have set up [My Domain](http://help.salesforce.com/articleView?id=domain_name_overview.htm&type=5) name for your Salesforce Org and Deployed it to Users. Please follow the [instructions in this Salesforce Help video (00:55 - 02:05)](http://salesforce.vidyard.com/watch/oFQ26FCXPVOA90xZaVDDjA) to learn how to do that

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2\.** Open the package installation link:

* [Package for regular use in Salesforce Production](https://login.salesforce.com/packaging/installPackage.apexp?p0=04t1r000000b6bh)
* [Package for Salesforce Sandbox use](https://login.salesforce.com/packaging/installPackage.apexp?p0=04t1r000001U5Eg). Learn more about the specifics of installing packages in a Sandbox in [this Salesforce help](https://help.salesforce.com/articleView?id=distribution_installing_packages.htm&type=5) article

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**3\.** Log in to your Salesforce account (it must have Admin permissions in your org)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**4\.** Select the checkbox *I acknowledge that I’m installing a Non-Salesforce Application that is not authorized for distribution as part of Salesforce’s AppExchange Partner Program* to permit installation.  

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/install_package.png" class="minimized">
</p>

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**5\.** Define how you want to install the package: for all users in your org, for specific user profiles, or for only for the Admins

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**6\.** Click the **Install** button in the lower right corner of the page



&nbsp;

* * *
&nbsp;


The Invisible Suite package adds custom fields and classes which are required for the following features to work:



&nbsp;

#### I. [Emails deduplication](../Item-Deduplication-Mechanisms/)

Prevents creation of multiple Task/EmailMessage objects for the same email saved in Salesforce. Has a [setup prerequisite](../Item-Deduplication-Mechanisms/#general_deduplication_feature_prerequisite).

&nbsp;

#### II. [Auto-saving all emails in threads](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_email_threads)

Enables [automatic saving of new received or sent emails to the conversation thread they belong to](../Save-All-Emails-in-a-Thread/). To enable this feature, the *ConversationId* field should be specified in the [**Thread ID** setting](../Special-Admin-Panel-Settings/#email_threads_auto-sync) in {{ product_name }} Admin panel.

&nbsp;

#### III. [Email direction indicator](../Special-Admin-Panel-Settings/#email_direction_field) (inbound/outbound)

To enable this feature, the *IsInbound* field should be specified in the [**Email direction** field](../Special-Admin-Panel-Settings/#email_direction_field) in {{ product_name }} Admin panel.

&nbsp;

#### IV. Defining if an email is internal (sent to or received from a colleague)

The custom *IsInternal* field of Task records is auto-filled by {{ product_name }} depending on whether the sender's/recipients' email addresses or domains are [categorized as internal (in-organization) ones](../Special-Admin-Panel-Settings/#organization_email_domains).

&nbsp;

&nbsp;

#### Managed Package contents

Specific fields, classes, and components the Invisible Suite package adds to your Salesforce configuration:

| **Name**                       | **Parent Object** | **Type**              | Used for                                                     |
| ------------------------------ | ----------------- | --------------------- | ------------------------------------------------------------ |
| InternetMessageId              | Activity          | Custom Field          | [Email deduplication](../Item-Deduplication-Mechanisms/#general_email_deduplication/) |
| IsCreatedBySync                | Activity          | Custom Field          | Possibility to filter Activities auto-created by synchronization, if needed |
| attendees_lookupController     |                   | Apex Class            | Auxiliary                                                    |
| IsInbound                      | Activity          | Custom Field          | Email direction indicator                                    |
| attendees_lookupControllerTest |                   | Apex Class            | Auxiliary                                                    |
| attendees_search               |                   | Apex Class            | Auxiliary                                                    |
| strike_responseData            |                   | Apex Class            | Auxiliary                                                    |
| ConversationId                 | Activity          | Custom Field          | [Auto-Save All Emails in A Thread](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_email_threads) |
| strike_utilities               |                   | Apex Class            | Auxiliary                                                    |
| Attendees Preview              | User              | Field Set             | Attendees management                                         |
| strike_evt                     |                   | Aura Component Bundle | Auxiliary                                                    |
| Attendees Preview              | Lead              | Field Set             | Attendees management                                         |
| defaultTokens                  |                   | Aura Component Bundle | Auxiliary                                                    |
| attendees_multiLookup          |                   | Aura Component Bundle | Auxiliary                                                    |
| strike_tile                    |                   | Aura Component Bundle | Auxiliary                                                    |
| attendees                      |                   | Aura Component Bundle | Auxiliary                                                    |
| Attendees Preview              | Contact           | Field Set             | Attendees management                                         |
| IsInternal                     | Activity          | Custom Field          | Defines if an email belongs to [an internal (in-Org) address/domain](../Initial-Search-and-Applied-Record-Filters/#internal_emails_corporate_domains_and_the_blocklist) |
| IsOpenedByRecipient            | Activity          | Custom Field          | (optional) can be configured to reflect the email's [Engagement status](../Tracking-Customer-Engagement-with-Magic-Pixel-%28Adaptive-view%29/) |
| IsCreatedByAddin               | Contact           | Custom Field          | (optional) can be configured to indicate if the item was created using [{{ product_name }}](../Introduction/) |
| IsCreatedBySync                | Contact           | Custom Field          | (optional) can be configured to indicate if the item was created by [{{ short_name }} Sync Engine](../Synchronization-Engine-An-Overview/) (see [autoresolving](../Synchronization-Engine-An-Overview/#automatic_creation_of_contacts_or_leads_by_rg_email_sidebar_autoresolving)) |

&nbsp;
* * *
&nbsp;

#### How to Uninstall the package

Follow the steps below if you need to uninstall the Invisible Suite package from your Salesforce org:

**1\.** Log in to your Salesforce account (it must have Admin permissions in your org)

**2\.** Open Salesforce [Setup menu](https://help.salesforce.com/articleView?id=basics_nav_setup.htm&type=5)

**3\.** Enter *installed packages* in the **Quick find** field in the upper left corner of the page and select **Installed Packages**

**4\.** Find Invisible Suite in the list of installed packages and click the **Uninstall** button next to it  

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/uninstall.png" class="minimized">
</p>

&nbsp;

**5\.** Scroll down to the bottom of the page that appears and select the checkbox *Yes, I want to uninstall this package and permanently delete all associated components*, then click **Uninstall**

&nbsp;

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/uninstall2.png" class="minimized">
</p>

&#160;
 &#160;

