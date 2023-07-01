---
description: Overview of the Record Description field and adding Quick Memos via the RG Email Sidebar
---
# The Record Description Field and Adding Quick Memos via the Sidebar  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! tip "Tip"
    See also: an advanced feature for enhancing Event, Contact, or Task Descriptions, [Smart Description](../Using-the-Smart-Description-Feature/)

When processing records, besides having your record notes at hand – in the *Description* field at the bottom of the record's detailed view that mirrors the standard object Description field in Salesforce – you sometimes need to quickly add an informative comment or update about a record, as a note or reminder for yourself or for a colleague working with the same record. The Add Quick Memo feature of {{ product_name }} serves this purpose.

Quick memos are added on top of the record's Description, put as log entries including a date/time stamp and the name of the memo's contributor. The Add Quick Memo function is not available for objects which have no Description field.

To add a Quick memo to a record:

1\. Expand the record's card in the Sidebar by clicking on it

2\. Select the **Quick Memo** tab among the tabs shown in the card

3\. Enter the memo's text in the "Add memo to {object's} description" field and click **Post** to add the memo

Note that at this step you can also attach a relevant file from among the email's attachments to the record, by clicking the  attach icon located next to the Post button and selecting the file.

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5bd2f72a04286356f0a51b84.gif" style="width: 40%; height: 40%;">
</p>

&nbsp;

Now you and your colleagues can see the memo in the record's description and react to it.

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5bd2f85f2c7d3a01757a72c7.png)

&nbsp;

!!! warning "Important"
    if Add Quick Memo is unavailable with the *"description not found"* notification displayed, that means the standard Salesforce object Description field is either not enabled for this object type via [{{ product_name }} Customization page's central pane, Detailed view](../Customization-Settings-Explained/#8_customizing_detailed_card_view) or is [marked as read-only/non-editable in Salesforce](http://webkul.com/blog/field-accessibility-salesforce/)  

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5bd30a1004286356f0a51c3e.png" class="minimized">
</p>


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