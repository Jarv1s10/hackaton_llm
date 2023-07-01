---
description: Learn how RG Email Sidebar works with required fields and layouts in Salesforce
---
# How the Solution Works with Required Fields and Layouts in Salesforce  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*4 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! warning "Important"
    {{ product_name }} only supports custom Salesforce page layouts if record types are configured. Learn about configuring record types in the following [article](https://help.salesforce.com/articleView?id=creating_record_types.htm&type=5)

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5be31efd2c7d3a31944daf12.png" class="minimized">
</p>

&nbsp;

In Salesforce, page layouts control the layout and organization of fields on record cards. They also help to determine which fields are visible or read-only.

{{ product_name }} supports custom Salesforce layouts – limit fields to display for each object type without altering your Salesforce layout settings.

{{ product_name }} takes into consideration both record types and user profiles when displaying Salesforce fields in the Add-In / Chrome Extension. For example, if a user at your organizations has access only to a specific “Account” record type (e.g., “Enterprise Account”) with a configured page layout, they will only see fields specified in that particular layout when creating / updating / viewing records in the Add-In / Chrome Extension. 

!!! note "Note"
    Learn more about creating and modifying Salesforce page layouts in the following [article](http://help.salesforce.com/articleView?id=customize_layout.htm&type=5) 

&nbsp;

### **Fields and Related Records**

By default, {{ product_name }} uses the same field order that is specified in your record page layouts to display Salesforce records when you create / view / update them using the Add-In / Chrome Extension. All changes you make to your record page layout will be reflected in the Add-In / Chrome Extension, including related objects as well as the field order.You could find details on that in the article below.

!!! note "Note"
    To update data displaying in {{ product_name }} after changing the settings, either open Customization page without saving (this way {{ product_name }} will retrieve the most recent data from Salesforce), or open {{ product_name }} and allow up to 5 minutes to get the layout changes applied automatically

You can remove specific fields from {{ product_name }} using **Customization** page. To do this, first go to the **Customization** page by clicking the **Menu** button in the Add-In / Chrome Extension.

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5be3222e04286304a71bfe88.png)

&nbsp;

On Customization settings page, find the object card you want to edit and click **Detailed view**. 

In the window that appears, you can add Salesforce fields to be reflected in the Add-In / Chrome Extension. By default, {{ product_name }} uses the fields selected on the **Detail** page in Salesforce, but you can add all Salesforce fields used in the page layout from the **Fields that are in Salesforce, but not on Account's card in {{ product_name }}** list.

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5be3217b2c7d3a31944daf2e.png" class="minimized">
</p>

Selected fields will be shown in the Add-In based on your page layout. To adjust their order, edit the page layout in Salesforce. Find out more in the article below. 

Click the  **Notepad** icon to show more details about the field. Additionally, you can marked the field as **Important**.

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5be3215604286304a71bfe7f.gif)

Important fields are prioritized for displaying when you create new records or view existing records in the **Detailed** view. You can select or clear the **Show only important fields** checkbox to display only the fields you marked as important, and vice versa.

However, {{ product_name }} takes into consideration the fields in your **Record Layouts** first. If you designate certain fields in your layouts as required, they will be important by default. 

!!! note "Note"
    If you designate a field as **Important**, but it is not in your Salesforce record layout, it will not be shown in the Add-In / Chrome Extension

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5be321212c7d3a31944daf2c.png)

&nbsp;

You can add an additional layer of data control by allowing users to create / update only certain record types in the Add-In / Chrome Extension. Please refer to [this article](../Customization-Settings-Explained/#6_customizing_object_card_appearance_and_behavior) to learn more. 

!!! note "Note"
    If you are using the 2-column layout in Salesforce, {{ product_name }} will follow the Tab-key Order of your choice to display fields

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5be320a304286304a71bfe70.png)

&nbsp;

Additionally, {{ product_name }} sorts related lists in the **Detailed View** based on the page layout. In Salesforce, on the **Page Layout** settings page, you can order related objects by dragging them into desired positions. These positions will be reflected in the Add-In / Chrome Extension. Additionally, {{ product_name }} fetches custom Labels for Related Lists, so if you rename them in Salesforce, they will be renamed in {{ product_name }} as well.

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5be320902c7d3a31944daf26.png" class="minimized">
</p>

&nbsp;

!!! warning "Important"
    If certain fields in your Salesforce layout are set as _required_ or _read-only_, that will be reflected in the Add-In / Chrome Extension. They will be also handled as important

{{ product_name }} takes into consideration your page layouts and all additional setting on the Customization page while displaying fields in the Create New record form.

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5be3207804286304a71bfe6c.png)

&nbsp;

&nbsp;

### **Custom Buttons**

{{ product_name }} displays custom buttons added in Salesforce in the Add-In / Chrome Extension. If you have any custom buttons configured on the page layout, you can access them by clicking the ●●● (More) button in the record's **Detailed view**.

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/585a7585c697912ffd6c4986.png)

&nbsp;

!!! warning "Important"
    Presently, {{ product_name }} supports only custom buttons and links retrieved from Salesforce layouts data. Learn more about creating and managing Salesforce custom buttons [this article](https://help.salesforce.com/articleView?id=links_useful_custom_buttons.htm&type=5)



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
      margin-top: -80px;
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
<div class="banners banner-1">
  <img src="../../assets/images/banners/banner-1.svg" style="width: 100%; height: 100%;">
  <a class="button" href="https://revenuegrid.com/sign-up/?utm_source=kb_rg&utm_medium=referral&utm_campaign=eac&utm_content=banner" target="_blank">Sign up for a free trial</a>
</div>