---
description: Detailed overview of RGES Initial Search and Applied Record Filters
---
# {{ product_name }} Initial Search and Applied Record Filters  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*10 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

In {{ product_name }}, automatic search for relevant Salesforce records (initial search) follows a specific algorithm of interactions between the Add-In/Gmail Extension, MS Exchange / Office 365 (or Gmail), and Salesforce. The below diagram illustrates the general relevant records retrieval principle applied by the Add-In / Chrome Extension.

&nbsp;

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5be9b62f04286304a71c2860.png" style="width: 80%; height: 80%;">
</p>

&nbsp;

!!! note "Note"
    The Initial Search also determines what [object category tabs](../All-User-Actions-in-Add-In-Sidebar/#1_items_categorizing) will be present on the Add-In's home screen, based on Salesforce configuration data. Note that while some added object types with set Salesforce views will be handled in "out-of-the-box" {{ short_name }} configuration, other custom ones must be [specifically configured](../How-to-Add-A-Custom-Object/) to be handled by {{ short_name }}

&nbsp;

!!! warning "Important"  
    During initial parsing, the search in Salesforce is performed by email addresses through all [“*Email*” type fields](https://help.salesforce.com/s/articleView?id=sf.custom_field_types.htm&type=5) on the “*Contact*” record type in Salesforce.   
      
    For example:  
    A Contact object in Salesforce may include the additional [custom fields](https://help.salesforce.com/s/articleView?id=sf.customize_customfields.htm&type=5) "*Personal email*" or "*Secondary email*". Both these fields belong to the “*Email*” field type. Thus, the Add-In / Chrome Extension will search by these fields by default, even if they are not added in [the *Search By* field](../Using-the-Search-by-List-Customization-Setting/) on objects in [Customization settings](../Customization-Settings-Explained/). 

<br>
After an email message/calendar item is selected or opened in your email client and the Add-In / Chrome Extension is open:

1. The Add-In / Chrome Extension obtains the full list (initial list) of senders/recipients from this item in MS Exchange
2. {{ product_name }} filters the initial list by removing the addresses which contain your corporate domain(s) (“internal emails”) and the addresses/domains specifically blocklisted from saving in Salesforce by {{ company_name }} synchronization, this way creating an aggregated list of addresses
3. Next, {{ product_name }} passes the resulting list to Salesforce to match these email addresses with objects stored in Salesforce
4. Salesforce matches the addresses from the aggregated list against the record fields
5. The results are displayed in the {{ product_name }} as [Related records](../Viewing-Salesforce-Records-Related-to-your-Email-(Adaptive-view)/)

&nbsp;

&nbsp;


### **The resulting Related records list will include**

* Associated Lead retrieved based on the email addresses and any records that match email addresses mentioned in email body

  or

* Associated Contact retrieved based on the email addresses, their associated Account and other business records (Opportunities, Cases), as well as other objects linked to this Account

* If no associated Leads or Contacts are found, the list will include Accounts retrieved based on their *Website address* field value matching the email address's domain

!!! warning "Important"
    {{ short_name }} doesn't perform a search by free email services domains (e.g. *gmail.com*, *yahoo.com*, etc.) to prevent linking with unrelated objects in Salesforce having the same email domains

* Other related records found, based on data retrieved from message Subject, Body (e.g. mentioned email addresses), and Signature. This includes your Org-specific custom objects, provided you have [added them to {{ short_name }} handling scope](../How-to-Add-A-Custom-Object/)

!!! note "Note"
    If the aggregated list contains no addresses (that is, all addresses were filtered out as internal/blocklisted), the message is categorized as Internal and no related records are displayed for it

!!! note "Note"
    If {{ product_name }} reads a support Case's code contained in the message’s Subject field, it also retrieves and adds the corresponding Case to the related records list. Additionally, If there are direct links to Salesforce records (e.g., *http://yourcompany.my.salesforce.com/0011J00001C5VJa*) or email addresses mentioned in message body, these items are also added to the list

Note that searching for records related to internal emails can also be performed, if the Add-In / Chrome Extension is configured to do so by enabling the **Include internal emails into search results** option on [{{ product_name }} Customization page](../Customization-Settings-Explained/) – this option excludes internal email addresses filtering by Initial Search.

&nbsp;

* * *

&nbsp;

### **How {{ product_name }} filters records are displayed in search results**

In addition to the [customizable viewed items filters](../Customization-Settings-Explained/#63_defining_the_searchview_scope) applied to make [{{ product_name }}](../Introduction/)'s displaying of Salesforce records convenient and focused, it includes specific filters applied for items being synced which are required for sync optimization and focusing, so the items actually displayed in {{ product_name }} search results are what remains after application of all these filters, besides the [search criteria you have entered](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-(Adaptive-view)/).

The applied filters are:

1.  The “internal emails” filter and the [*Do not load related objects lists* filter](../Customization-Settings-Explained/#2_application_settings) to learn how to disable or enable these filters), as well as secondary "items focusing" [Salesforce views](https://help.salesforce.com/articleView?id=customviews.htm&type=5) which can be set in [customization settings](../Customization-Settings-Explained/#5_choosing_a_set_of_salesforce_objects_to_display) (**Global search filter** and **Contextual search filter**)  
2.  The [blocklisted](../Configuring-Activities-Synchronization-Settings/#blocklisting_email_addresses_and_domains) addresses / domains filter and other [filters applied on records synchronization](../Synchronization-Engine-An-Overview/)

This way, if the searched for item is not displayed, it may have been hidden by one of the above listed filters. To determine the reason why the record was not shown in search results:

*   Read [the article](../How-to-Save-Internal-or-Blacklisted-Emails-in-Salesforce-%28Adaptive-view%29/) about the handling of filtered internal and blocklisted emails. To find the list of filtered emails, go to the **Smart Actions** bar > **More...** > **Observations**, “Some not important emails were filtered:“ in {{ product_name }}

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5b71aff12c7d3a03f89da34e.png)

&nbsp;

*   Read articles describing the settings of the relevant filters on {{ product_name }} [Customization page](../Customization-Settings-Explained/) and [Synchronization dashboard](../How-to-Open-Sync-Dashboard-(Adaptive-view)/)

!!! warning "Important"
    In addition, to bring up only actual records, {{ product_name }} initial search applies specific filters for certain objects listed in Related records. To be included, an Opportunity object must be either be closed within 1 year (365 days) in the past or expected to be closed within 6 months (180 days) from the present date; a Support Case object must be open and created within 3 months (90 days) in the past from the current date. Please also refer to [this article](../How-to-Create-a-Custom-List-View/) to learn how to include closed Cases and Opportunities into {{ short_name }} handling scope

&nbsp;

* * *

&nbsp;

### **Internal Emails, Corporate Domains, and the Blocklist**

By default, {{ product_name }} recognizes your corporate email domains on the Org level in the **[{{ short_name }} Admin panel](../How-to-Log-In-to-the-Admin-Panel/)** and does not auto-save emails to/from such addresses in Salesforce if [the corresponding setting](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_emails_emails_autosharing) is enabled.  

!!! note "Note"
    You can always make use of [user-initiated search](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-(Adaptive-view)/#searching_for_records_in_salesforce_adaptive_view) if you want to save an email categorized as internal or blocklisted to Salesforce, linked to an existing object

The list of internal (in-org) email addresses/domains is defined via the [corresponding field](../Special-Admin-Panel-Settings/#organization_email_domains) in [{{ short_name }} Admin panel](../How-to-Log-In-to-the-Admin-Panel/). {{ product_name }} also appends different variations of [your corporate email domain(s)](../Special-Admin-Panel-Settings/#organization_email_domains) (based on the list of aliases retrieved from MS Exchange / Office 365) to this list, as comma-separated values.  

&nbsp;

In case you need to enable retrieval of related records for internal (in-org) email messages and calendar items, follow the steps below:

1. In the {{ product_name }}, click the **Menu** button and go to the **Customization** page

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5be3222e04286304a71bfe88.png)

&nbsp;

2. In the **Application Settings** area, select the **Include internal emails into search results** checkbox

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5be9b67f04286304a71c2866.png)

&nbsp;

3. Click  **Save** in the upper right corner 

This will enable {{ product_name }} to work with internal email addresses on the Organization's level, thus the Add-In / Chrome Extension will also disregard the corporate email addresses list on all [synchronization sessions](../Synchronization-Engine-An-Overview/).

&nbsp;

The users who have access to their [Customization settings](../Customization-Settings-Explained/) can add both email addresses and domains to the not-to-be-saved-by-sync blocklist, in the **Misc. Settings** block, **Email Domains blocklisted From Syncing** box. Messages or events received from users with the specified emails or domains in their email addresses will **not** be [auto-saved in Salesforce](../Synchronization-Engine-An-Overview/). Note that the list does not support using [wildcards](https://www.computerhope.com/jargon/w/wildcard.htm).  

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5be9b68f04286304a71c2867.png)

&nbsp;

!!! warning "Important"  
    A special global setting blocklists all free email services (e.g. *gmail.com*, *yahoo.com*, etc.) from auto-syncing by default, so you don’t need to add all of them to the Blocklist box. To change or customize this setting, contact our [support team](mailto:support@revenuegrid.com)  

This [user-defined blocklist](../Blocklisting-Email-Addresses-and-Domains/) is complemented by [the all-Org blocklist](../Special-Admin-Panel-Settings/#emails_domains_blocklisted_from_sync). Refer to [this article](../Two-Layers-Blacklisting/) for more information on how these two blocklists.

&nbsp;


To save internal emails by selecting the **Include internal emails into search results** checkbox (as described above), make sure that your corporate domain is not listed in the **Email Domains Blocklisted From Syncing** box as well. 

!!! warning "Important"
    If an email is sent to multiple receivers and only some of the addresses are on the blocklist, the email will still be saved and linked to the records associated with the recipients who are not blocklisted

&nbsp;

* * *

&nbsp;

### **Prefilled Field Values Priority**

In the latest {{ product_name }} updates, when a single field is prefilled by either two or all of the three existing prefilling mechanisms, there is an established priority defining which prefilled value prevails [listed from higher priority to lower priority]:

1. Explicit field prefilling [performed by the Add-In](../AddIn-vs-Sync-Functions/) based on item scanning or [initial search](../Initial-Search-and-Applied-Record-Filters/) results
   
2. Prefilling of default values set by [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/)  
   
3. Default values defined by Salesforce (e.g. default picklist items)    

In addition, any prefilled field value can be modified through {{ product_name }} by the users.

&nbsp;

* * *

&nbsp;

### **Strict Initial Search**

{{ product_name }} initial search is based on [Salesforce search](http://help.salesforce.com/articleView?id=search_how_search_works.htm&type=5); by default its results include all records linked to an object one of whose fields specified in the [Search by list](../Using-the-Search-by-List-Customization-Setting/) contains a matching identifying value (e.g. email address or name) extracted from the incoming email message or calendar item. This broad search approach is useful in most cases, as it is highly inclusive.
However, when applied to searching among internal emails (that is, **Allow creating duplicated emails in Salesforce** is enabled), the default broad search might retrieve too many undesired associated records from Salesforce, including owned records and ones retrieved via [WhoId / WhatId fields](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/). To prevent that, {{ product_name }} always applies _strict initial search_ for internal emails, making the results more focused.

!!! note "Note"
    If broad initial search matches are too many, only a selection of  them is displayed in Related records. If you notice that occurring, i.e. you see some distantly related records instead of expected ones, it might be necessary to enable strict initial search permanently to get focused results. Send a corresponding request to our [Support team](mailto:support@revenuegrid.com) to enable permanent application of strict initial search in your configuration

&nbsp;

* * *

&nbsp;


### **Opportunity Contact Roles Associations**

Please note that in the latest {{ product_name }} updates contact roles set for Opportunity objects are also considered on initial search and associated records found through the roles are also listed in Related records in the Sidebar.

&nbsp;

* * *

&nbsp;

### **Related Records Retrieval Pattern**

* If an incoming/outgoing Email or Event has an associated Contact linked to an Account, both will be displayed in related record list retrieved by Initial Search

* Initial Search displays among Related records only those additional Contact associations (e.g. Opportunities or Cases) which object-specific user defined [Contextual search filter](../Customization-Settings-Explained/#6_customizing_object_card_appearance_and_behavior) allows to handle

* If there are [duplicate records](../Item-Deduplication-Mechanisms/) found which are based on the same email address, e.g. a Lead and a Contact, all of them will be listed among Related records

* If an incoming/outgoing Email or Event has an associated Contact but no Account linked to it, there will be no direct suggestion to create an Account for it, since some business contacts might represent no companies and thus require no Account linking

!!! note "Note"
    If an Account's *Website* field corresponds to an email domain used in correspondence, {{ product_name }} Initial Search will list it among Related records only if no other associated records were found.
    In addition, on Contact creation, when suggesting an Account to be associated with the Contact, Initial Search first checks for related Contacts and Accounts by domain of the email address specified for the created Contact; then, if no records are found this way, it searches for Accounts which contain website link corresponding to the email domain.  
    
!!! warning "Important"
    If no associated records were found in Salesforce, {{ short_name }} will **not** perform a search by free email services domains (e.g. *gmail.com*, *yahoo.com*, etc.) to prevent linking with unrelated objects having the same email addresses' domains

&nbsp;

* * *

&nbsp;

### **Additional notes on the [Global Search View Setting](../Customization-Settings-Explained/#6_customizing_object_card_appearance_and_behavior)**

* Besides the Related record list, the Global search filter is also applied when objects are internally searched for by their identifier. This may cause certain confusions:
    Additional related objects (Accounts, Opportunities, Cases, or custom objects) will be essentially filtered out of display according to set [Global view](../Customization-Settings-Explained/#63_defining_the_searchview_scope). For example, if you select Accounts to be filtered out by this setting, Initial Search will retrieve and display all Contacts associated with a relevant Account along with the primary related Contact, but not the Account itself.
    Similarly, clicking on a reference to an object filtered out by the actual [Global view](../Customization-Settings-Explained/#63_defining_the_searchview_scope) will not open the object in the Sidebar.
    On [{{ product_name }} user-initiated search](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-(Adaptive-view)/), records not belonging to the actual [Global view](../Customization-Settings-Explained/#63_defining_the_searchview_scope) may appear in {{ product_name }} search suggestions, but selecting them will not bring up any search results.  
* Sometimes, if certain records were not retrieved by Initial Search because of the [Global view](../Customization-Settings-Explained/#63_defining_the_searchview_scope) applied, the Add-In / Chrome Extension will suggest creating them. And if the user creates them via the Add-In / Chrome Extension, Salesforce may respond with a [duplicate records notification](https://help.salesforce.com/articleView?id=managing_duplicates_overview.htm&type=5)



&#160;
 &#160;

