---
description: Overview of special sync adjustments: sharing various Salesforce objects as calendar items & one-way synchronization patterns
---
# Special Sync Adjustments: Sharing Various Salesforce Objects as Calendar Items & One-way Synchronization Patterns  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*3 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

#### Syncing [custom](https://trailhead.salesforce.com/en/content/learn/modules/data_modeling/objects_intro) as well as [standard](https://help.salesforce.com/articleView?id=co_overview.htm&type=5) Salesforce objects (e.g. Tasks) as MS Exchange calendar items

The latest {{ product_name }} updates include a possibility to set special patterns for calendar items synchronization. 

!!! note "Note"
    Please note that presently this feature can be enabled by request sent to [our Support team](mailto:support@revenuegrid.com) including a detailed description of your specific use preferences

Using this feature, [a custom Salesforce object](https://help.salesforce.com/articleView?id=co_overview.htm&type=5), [a Task](https://help.salesforce.com/articleView?id=tasks.htm&type=5) or [another standard object](https://trailhead.salesforce.com/en/content/learn/modules/data_modeling/objects_intro) can be [handled](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/) by {{ product_name }} to be synced as an MS Exchange / Office 365 calendar item. Note that this syncing can only be done in one direction: from Salesforce to MS Exchange, and not the other way.
In addition, when a custom object gets synced to MS Outlook, it is assigned a custom MS Outlook category that reflects the object type which it is based on.

**Requirements and limitations:**

- the target custom or standard object(s) should have a [Date field](https://help.salesforce.com/articleView?id=formula_using_date_datetime.htm&type=5) or two [Date/Time fields](https://help.salesforce.com/articleView?id=formula_using_date_datetime.htm&type=5)
- several [extra custom fields](../Admin-Managed-Package/#specific_fields_classes_and_components_the_invisible_suite_package_adds_to_your_salesforce_configuration) must be added to the object to enable all [event syncing](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/) mechanisms
- recurring events synchronization is not supported for these scenarios

&nbsp;

* * *

&nbsp;

#### One-way Synchronization

By default {{ company_name }} synchronization of MS Exchange / Office 365 or Gmail calendar items, Tasks, and Contacts is two-way: items within [synchronization scope](../Synchronization-Engine-An-Overview/) assigned the custom Salesforce category in MS Outlook are mirrored on both sides (with [certain exceptions](../Calendar-Items-Sync-Special-Patterns-Attendees-Lists,-Private-Items,-Item-Unsharing-and-Deletion/) for Calendar items). That is, if an object is modified on either side, these changes are conveyed to the other side so the items remain identical.

However, to meet the customers' specific preferences, in the latest {{ product_name }} updates advanced one-way synchronization options were introduced for calendar items. Previously, one-way syncing was used in some custom configurations to make events "read-only" on the Salesforce side (set as single source of truth) – that is, non-modifiable by [{{ company_name }} synchronization](../Synchronization-Engine-An-Overview/) when changes were made to their matching objects in MS Exchange.

!!! note "Note"
    Please note that presently this feature is available by request sent at to [our Support team](mailto:support@revenuegrid.com) including a detailed description of your specific use preferences

&nbsp;

**1. Mail server → Salesforce upsyncing**

With this feature enabled, changes (modification, deletion) made to events through your email client and {{ product_name }} will override any changes made to them directly in Salesforce. You can make use of this feature if, for example, if you do not manage events through Salesforce. With this setting enabled, any changes made to records in Salesforce will be replaced with data up-synced from your email client.

!!! warning "Important"
    Note that events *created* in Salesforce will be down-synced to your MS Exchange / Office 365/Gmail calendar, but modifications or deletions of events in Salesforce will be reverted on the following sync session. For example, if you create and sync a Salesforce event with MS Exchange / Office 365 and then correct something about it or delete it in Salesforce, your corrections will not be kept. As a workaround you can make the necessary corrections in the corresponding event (or delete and event) in MS Outlook and these changes will be up-synced to Salesforce

&nbsp;

**2. Salesforce → Mail server downsycing**

!!! tip "Tip"
    Also refer to [this article](../Choosing-What-to-Synchronize/) to learn how to disable down-syncing for specific item types

This option enables one-way transferring of item changes (creation, modification, deletion) from Salesforce to MS Outlook, while event updates made in MS Outlook will **not** be kept or conveyed to Salesforce. For example, this feature can be used to perform one-way spreading of information about an all-org public event among the employees via Salesforce. 

!!! note "Note"
    Processing of the one-way updates as well as reverting of changes on either side according to specified priority is carried out on [{{ company_name }} synchronization sessions](../Synchronization-Engine-An-Overview/), not instantly

Additionally, in the latest {{ product_name }} updates there is a new [special setting](../Special-Admin-Panel-Settings/#auto-share_outbound_sent_emails_only) that enables [auto-sharing](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_emails_emails_autosharing) of only outbound (sent) emails in Salesforce, but not inbound (inbox) ones.

Also note that in the latest {{ short_name }} updates the [Global setting](../Special-Admin-Panel-Settings/#extra_configuration_settings) *ServiceEventDeletionStrategy* was introduced to make it possible to perform automatic deletion of calendar items from MS Exchange calendar by [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/) if they were deleted from Salesforce calendar by the users.



&#160;
 &#160;

