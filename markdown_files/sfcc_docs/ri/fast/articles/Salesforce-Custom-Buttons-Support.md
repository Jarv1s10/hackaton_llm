---
description: Overview of RGES support for Salesforce custom buttons
---
# {{ product_name }} Support for Salesforce Custom Buttons  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

When you are viewing a Salesforce object in {{ product_name }}, the Add-In / Chrome Extension also renders [custom Salesforce buttons](http://trailhead.salesforce.com/en/modules/lex_customization/units/lex_customization_buttons_links) available for this object type. These [custom buttons set up to open URLs or perform specific actions in Salesforce](http://help.salesforce.com/articleView?id=defining_custom_links.htm&type=5) are fully functional in {{ product_name }}.

!!! warning "Important"
    only those custom buttons which open links in your web browser or perform actions implemented as Salesforce links are supported. Additionally, in the latter case if you are not logged in to Salesforce, upon clicking the button you will be prompted to login to Salesforce via a standard Salesforce OAuth window. Please also note that unsupported Salesforce buttons will not be displayed in the Sidebar

To view and use custom buttons/actions available for an object, you need to click the <img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/open_in_sf.png" style="display: inline-block;vertical-align: middle;width: 18px;margin-left: 1px;height: 14px;object-fit: contain;"> icon that appears next to the record's name when you hover mouse over the record's header in the Sidebar:

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5bc76d412c7d3a04dd5bcd2a.png)

&nbsp;

The standard custom buttons listed for Contact, Lead, or Account objects are:

*   open the record in Salesforce  
*   open the associated company's website  
*   search for the Contact, Lead, or Company in LinkedIn  
*   send SMS  



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
<div class="banners banner-2">
  <img src="../../assets/images/banners/banner-2.svg" style="width: 100%; height: 100%;">
  <a class="button" href="https://revenuegrid.com/request-demo/?utm_source=kb_rg&utm_medium=referral&utm_campaign=eac_demo&utm_content=banner" target="_blank">Book a free demo</a>
</div>