---
description: Learn how to manage Contacts via the Solution (Contacts Sync)
---
# Managing Contacts via the Solution (Contacts Sync)  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*6 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

[{{ company_name }} synchronization](../Synchronization-Engine-An-Overview/) performs continuous two-way syncing of your business Contacts between MS Exchange / Office 365 or Gmail and Salesforce. Once [activated](../Authorizing-Sync-Engine-to-Work-with-Your-Data/), data synchronization runs every 30 minutes on server side.
Bidirectional mail server ↔ Salesforce syncing of Contacts carried out by {{ short_name }} sync is a versatile process that also ensures conveying of Salesforce contacts into your [Exchange address book](https://docs.microsoft.com/en-us/exchange/address-books/address-books) and their use by [MS Outlook Desktop / On the Web AutoComplete](https://support.microsoft.com/en-sg/help/2199226/information-about-the-outlook-autocomplete-list) on email composing or meeting creation.

!!! tip "Tip"
    Refer to [this article](../Object-Fields-Mapping-Patterns/#ms_outlook_contacts) to learn how MS Exchange / Office 365 Contact item fields are matched with [Salesforce Contacts](https://help.salesforce.com/articleView?id=contacts_overview.htm&type=5) by {{ product_name }}.
    Also refer to [this article](../Choosing-What-to-Synchronize/) for more details on configuring objects synchronization.

&nbsp;

!!! warning "Important"
    Depending on your license, the appearance of your Sync Settings page may be different. Below you can find instructions on how to renew access credentials on the **Legacy** and **New** Sync Settings pages. Proceed with the steps according to the appearance of your Sync Setting page:

    * [New Sync Settings page](#enabling_contacts_sync_on_the_new_sync_settings_page)

    * [Legacy Sync Settings page](#enabling_contacts_sync_on_the_legacy_sync_settings_page)


&nbsp;


## Enabling Contacts Sync on the new Sync Settings page

After [{{ short_name }} sync is set up](../Authorizing-Sync-Engine-to-Work-with-Your-Data/), to enable Contacts sync, go to the Sync Settings page (see the article [Opening the Dashboard](../How-to-Open-Sync-Dashboard-(Adaptive-view)/)). You will see the *General* subtab where you can enable the **Sync Salesforce contacts** switch button in the Contacts block:


<p><img src="..\..\assets\images\Configuration-&-Settings\User-Settings\contacts-sync\contacts-sync.png">
</p>

&nbsp;

To set a focused [Salesforce list view](https://help.salesforce.com/articleView?id=customviews.htm&type=5) to be applied by {{ product_name }} on Contacts downsyncing from Salesforce to your mail client:

<img src="..\..\assets\images\Configuration-&-Settings\User-Settings\what-to-sync\view.png" style="width:50%; display:inline-block; vertical-align:middle; margin-left:10px; float: right">

* click **Customize scope** in the *Contacts* block

* select one of the options: *All available Contacts*, *Only my Contacts* (this view is set by default), *Custom Salesforce view*

* in case need to select *Custom Salesforce view*, specify a [preconfigured Salesforce Contacts custom view](https://trailhead.salesforce.com/en/content/learn/modules/lex_customization/lex_customization_list) in the corresponding picklist 


&nbsp;

* click **Apply** to enable the view

<p><img src="..\..\assets\images\Configuration-&-Settings\User-Settings\contacts-sync\apply.png" style="width:80%;">
</p>

&nbsp;

After [{{ short_company_name }} synchronization](../Synchronization-Engine-An-Overview/) is [set up](../Authorizing-Sync-Engine-to-Work-with-Your-Data/), {{ product_name }} creates in MS Exchange / Office 365 a dedicated folder **Salesforce Contacts** and mirrors all business contacts which you own in Salesforce as Exchange/Office 365 contacts put in this folder, matching their fields according to [established mapping patterns](../Object-Fields-Mapping-Patterns/#ms_outlook_contacts).
However, note that your Contacts existing in MS Exchange / Office 365 prior to {{ short_name }} sync activation will **not** be synced with Salesforce, unless you specifically select them to be synced using either one of the methods described below.

&nbsp;
&nbsp;

## Marking Contacts to be synced

!!! tip "Tip"
    See [this article](../Using-the-Solution-for-Salesforce-and-Gmail/#syncing_contacts_in_salesforce) to learn how to sync Gmail contacts

&nbsp;

There are two ways to synchronize an MS Exchange / Office 365 contact with Salesforce via {{ product_name }}:

#### By creating or moving a Contact in the Salesforce Contacts folder

* Select the **Salesforce Contacts** folder in MS Outlook Desktop / On the Web Contacts tab and click the **New Contact** icon; then fill in the contact's data and save it. {{ product_name }} will assign the new Contact the *Salesforce* category and create of a matching Contact object in Salesforce by [{{ short_name }} sync](../Synchronization-Engine-An-Overview/).

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5a394d94042863087ede4478.png" class="minimized">
</p>

<br>
<br>


* Alternatively, drag and drop or right-click and move an existing Contact to the *Salesforce Contacts* folder - it will be saved in Salesforce on the following sync session. To be continuously synced with Salesforce, contacts should remain in this folder; any updates made on either side will be mirrored on the other, through two-way synchronization.

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5a3946f12c7d3a08f41f52db.png" class="minimized">
</p>

<br>
<br>

#### Syncing a Contact using the custom Salesforce category

Alternatively, you can save a contact in Salesforce by assigning it the *Salesforce* category.

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5a394efb042863087ede4489.png" class="minimized">
</p>

<br>
<br>;

{{ product_name }} will move the marked contact to the *Salesforce Contacts* folder and create a matching Contact object in Salesforce on the following sync session.

!!! note "Note"
    If the Salesforce category is unassigned after an item was moved to the dedicated Salesforce folder and synchronized with Salesforce, {{ short_name }} sync will automatically restore the category on this item on the following sync session – items will remain synced if you just unassign the custom category from them but leave them in the dedicated folder.
    In the opposite case, if a synchronized item is removed from the dedicated Salesforce folder to be unsynced, {{ short_name }} sync will automatically remove the custom category from this item on the following sync session



!!! note "Note"
    Your personal MS Exchange / Office 365 contacts located in the default *Contacts* folder or other folders will **not** get saved in Salesforce. Only the contacts assigned the *Salesforce* category or moved to the *Salesforce Contacts* folder will get saved

&nbsp;
* * *
&nbsp;

#### Special Patterns Applied on Contacts Processing

When a Contact is created and synchronized from MS Outlook to Salesforce, the following pattern is applied in order to find a relevant Account to link this Contact to:

1\. The value of the Contact's *Company* field is used to search for relevant Account(s) in Salesforce  

2\. If an Account with exact *Company* field matching is found - the Account is used for Contact linking. In case there are several Accounts found, one with the earliest creation date is used  

3\. If there is no direct match, the *Company* field's value is searched for among sub-strings of Account names in Salesforce, and if there is only one matching Account found, it is used to link the Contact to. If no relevant Account is found this way, see point **4**  

4\. If no matches with the *Company* field's value are found among Account names in Salesforce, a Contact with empty Account association is attempted to be created in Salesforce  

!!! tip "Tip"
    In case you want to adjust the Contacts processing mechanisms to meet your company's specific preferences: by adding extra required fields, changing default values in some fields, ensuring auto-linking to a specific Account, etc., please send a corresponding configuration request to [our Support team](mailto:support@revenuegrid.com), describing your preferences in detail

<br>
<br>

**Contact updates syncing**

When a Contact located in the **Salesforce Contacts** folder in MS Outlook is modified, these changes are conveyed (up-synced) to its matching Salesforce Contact object on the following sync session. A [two-way sync pattern](../Special-Sync-Options-Save-Events-As-Other-&-One-Way-Sync/) is used, so if you modify a Contact's fields values in Salesforce, they will be down-synced to its matching Contact in MS Outlook.

&nbsp;

**Deleting a Contact in Exchange/Office 365**

If you remove an already synchronized Contact from the **Salesforce Contacts** folder or delete it, {{ product_name }} checks the value of the **Auto-removal** setting (see the article [Choosing What to Synchronize](../Choosing-What-to-Synchronize/)) and proceeds accordingly:

* if Contacts Auto-removal is allowed - the Contact gets deleted from Salesforce as well, on the following [sync session](../Synchronization-Engine-An-Overview/)

* if Contacts Auto-removal is not allowed - the Contact gets automatically re-created in the **Salesforce Contacts** folder on the following sync session, its fields' values retrieved from Salesforce

&nbsp;

**Adding a Contact in Salesforce**

When a new Contact is added in Salesforce and it is visible within the set view (see [above](../Synchronization-of-Contacts/#enabling_contacts_sync)), it appears in the **Salesforce Contacts** folder in Outlook after the next synchronization.

&nbsp;

**Modifying a Contact in Salesforce**

When an existing Contact is modified in Salesforce and it belongs to the set list view (see [above](../Synchronization-of-Contacts/#enabling_contacts_sync)), the corresponding contact in the *Salesforce Contacts* folder in MS Exchange / Office 365 gets updated, on the following [sync session](../Synchronization-Engine-An-Overview/).

&nbsp;

**Deleting a Contact in Salesforce**

When a synced Contact is deleted in Salesforce, the corresponding contact in the *Salesforce Contacts* folder in MS Exchange / Office 365 gets deleted as well, on the following [sync session](../Synchronization-Engine-An-Overview/).



<hr>


## Enabling Contacts Sync on the legacy Sync Settings page

After [{{ short_name }} sync is set up](../Authorizing-Sync-Engine-to-Work-with-Your-Data/), to enable Contacts sync, go to Synchronization Dashboard (see the article [Opening the Dashboard](../How-to-Open-Sync-Dashboard-(Adaptive-view)/)), open **Sync Settings > Filters** in the pane on the left-hand side and enable the switch button under Contacts:

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5be9b4b82c7d3a31944ddae6.png" class="minimized">
</p>

&nbsp;

To set a focused [Salesforce list view](https://help.salesforce.com/articleView?id=customviews.htm&type=5) to be applied by {{ product_name }} on Contacts downsyncing from Salesforce to your Mail client:

* open [Sync dashboard](../How-to-Open-Sync-Dashboard-(Adaptive-view)/) > Sync Settings > Filters

* click **> Customize** under *Contacts*

* select one of the options: *All available contacts*, *Only my contacts* (this view is set by default), *Custom view*

* in case you selected *Custom view*, specify a [preconfigured Salesforce Contacts custom view](https://trailhead.salesforce.com/en/content/learn/modules/lex_customization/lex_customization_list) in the corresponding picklist 

  ![](../assets/images/Using-SmartCloud-Connect/How-To-s/Managing-Contacts/custom_views.png)

  

&nbsp;

* click **Save** to enable the view

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5be9b4c72c7d3a31944ddae7.png)

&nbsp;

After [{{ short_name }} synchronization](../Synchronization-Engine-An-Overview/) is [set up](../Authorizing-Sync-Engine-to-Work-with-Your-Data/), {{ product_name }} creates in MS Exchange / Office 365 a dedicated folder **Salesforce Contacts** and mirrors all business contacts which you own in Salesforce as Exchange/Office 365 contacts put in this folder, matching their fields according to [established mapping patterns](../Object-Fields-Mapping-Patterns/#ms_outlook_contacts).
However, note that your Contacts existing in MS Exchange / Office 365 prior to {{ short_name }} sync activation will **not** be synced with Salesforce, unless you specifically select them to be synced using either one of the methods described below.

&nbsp;
&nbsp;


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