---
description: Overview of preconditions for enabling advanced Calendar Synchronization (recurring events syncing and events deduplication)
---
# Preconditions for Enabling Advanced Calendar Synchronization (Recurring Events Syncing and Events Deduplication)  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! warning "Important"
    Presently, there is a limitation on syncing of recurring meetings/appointments series if your are using [Salesforce Lightning Experience](https://trailhead.salesforce.com/content/learn/modules/lex_migration_introduction/lex_migration_introduction_whatis): series of recurring calendar items created in Salesforce Lightning Experience cannot be *downsynced* to MS Exchange / Office 365 by {{ product_name }}.
    At that, series of recurring MS Exchange / Office 365 calendar items can be *upsynced* to Salesforce Lightning, but only as [Salesforce Classic format events](https://help.salesforce.com/articleView?id=viewing_events_cex.htm&type=5); therefore, they stay uneditable over Salesforce Lightning. As a workaround, you can temporarily [switch to Salesforce Classic](https://help.salesforce.com/articleView?id=000230642&type=1) to edit them in Salesforce or edit them in MS Outlook and upsync the changes.

To enable {{ product_name }} to [synchronize recurring calendar items](../Saving-Calendar-Items-in-Salesforce-(Adaptive-view)/) in Salesforce or [advanced events deduplication](../Item-Deduplication-Mechanisms/) you need to ask your local Salesforce admin to request the *Advanced calendaring* feature to be activated for your Org. Please refer to [this instruction](http://help.salesforce.com/articleView?id=000123530&language=en_US&type=1) to learn how to log a corresponding case with Salesforce Support. Once this feature is enabled for your org, all fields required for recurring events sync and advanced deduplication will be added to the Event object. Specifically, enabling the *Advanced calendaring* feature adds the following fields to [Salesforce Event objects](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_event.htm):

* The *OriginalInstanceDateTime* field used for syncing recurring calendar items  
* The *ClientGuid* field used for [advanced events deduplication](../Item-Deduplication-Mechanisms/)  

Previously, these fields could be set up manually in Salesforce settings, now they are only available with this Salesforce feature enabled by Salesforce support.



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