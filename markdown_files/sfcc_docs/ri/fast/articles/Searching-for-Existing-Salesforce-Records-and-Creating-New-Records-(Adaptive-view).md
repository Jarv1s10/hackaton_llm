---
description: Learn how to use RG Email Sidebar to search for existing Salesforce Records
---
# Searching For Existing Salesforce Records via the Sidebar  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

{{ product_name }} [Add-In / Chrome Extension Sidebar](../Introduction/) allows the users to instantly find records of any type in Salesforce to do a quick data check or to [save a business email or Calendar activity with](../Save-Email-Dialog/).

!!! tip "Tip"
    See [this article](../Create-New-Records/) to learn how to create new Salesforce records directly from your email client using {{ product_name }}

&nbsp;

### Searching for Records in Salesforce ("user-initiated search")


With {{ product_name }} Add-in, you can easily search among all your Salesforce records: Contacts, Accounts, Opportunities, Leads, Activities (Tasks and Calendar events), Support Cases, or any [custom Salesforce object types peculiar to your Org](../How-to-Add-A-Custom-Object/).

To search for existing Salesforce records, do the following:   

**1\.**  In {{ product_name }} Add-In/Google extension, click the search icon in the upper right corner of the Sidebar, then enter your search criteria in the **Search in** box.   

!!! tip "Tip"
    After you click on the *Search In* box, you will see 5 records that you worked with recently

&nbsp;

**2\.**  In the picklist of record types, select the record type you want to search for. To search for records of all types, select **Salesforce**. The search results will be shown as record cards, also displaying the values in the [records' key fields](../How-the-Solution-Works-with-Required-Fields-and-Layouts-in-Salesforce/#fields_and_related_records) to make it possible to differentiate among similar records.  

!!! note "Note"
    You can search for records by parts of a word in records' [key fields](../How-the-Solution-Works-with-Required-Fields-and-Layouts-in-Salesforce/#fields_and_related_records), but at least 3 characters must be entered in the search field

&nbsp;

<details><summary>>>> Click to see an animation <<<</summary>
<p>
    <img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5bd9fd9e04286356f0a54b30.gif" style="width: 50%; height: 50%;">
</p>
</details>
&nbsp;

&nbsp;

### Why an existing record might be absent in search results?

​    If you do not see a record you need in search results, make sure to check the following {{ short_name }} customization settings for this object type:  
​    • [The **Hide on search** checkbox](../Customization-Settings-Explained/#6_customizing_object_card_appearance_and_behavior)  
​    • [**Global search** and **Contextual search** filters](../Customization-Settings-Explained/#63_defining_the_searchview_scope)  
​    • [The **Search By** field](../Using-the-Search-by-List-Customization-Setting/)  
​    • If searching for an item associated with an internal (in-org) email address, also make sure that the [**Include internal emails into search results** setting](../Customization-Settings-Explained/#2_application_settings) is enabled

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

