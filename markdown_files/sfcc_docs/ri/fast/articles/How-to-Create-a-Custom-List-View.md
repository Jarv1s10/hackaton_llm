---
description: If you need to review or work with closed Cases and Opportunities, you can configure a custom Salesforce list view to be used in RGES
---
# How to Create a Custom List View to Work with Closed Cases or Opportunities  
  

*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

By default, {{ product_name }} only displays non-closed Cases or Opportunities, filtering the closed ones for objects view focusing considerations. However, in case you also need to review or work with closed Cases and Opportunities, you can configure a [custom Salesforce list view](https://help.salesforce.com/articleView?id=customviews.htm&type=5) to be used in {{ product_name }} to also include closed ones into view scope.

Follow the steps below to create such view:

**1\.** Log in to your Salesforce account, select the **Cases** or **Opportunities** tab and [create a new list view](https://help.salesforce.com/articleView?id=customviews.htm&type=5), e.g. *All Cases*

<details><summary>>>Click to see an animation<<</summary>
<img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Create-Custom-View\salesforce.gif" alt="Create a custom view in Salesforce">

<br>
<img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Create-Custom-View\new_list_1.png">


</p></details>

**2\.** Open {{ product_name }} in MS Outlook Desktop or On the Web version and select **Menu** > [**Customization**](../Customization-Settings-Explained/)

**3\.** Find the **Support Case** or **Opportunity** object in the Customization page's central pane and expand **Other settings**

**4\.** Set the new list view created on step ( **1** ) in:  

   * The [global search view picklist](../Customization-Settings-Explained/#63_defining_the_searchview_scope) if you want to search among *all* Cases/Opps using [{{ product_name }} search](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-(Adaptive-view)/)  
   
   * The [contextual search view picklist](../Customization-Settings-Explained/#63_defining_the_searchview_scope) is you want {{ product_name }} to display closed Cases/Opps in the Sidebar after you select an email or event, along with non-closed ones  

![](../assets/images/Using-SmartCloud-Connect/How-To-s/Create-Custom-View/add_object.png)

&nbsp;

**5\.** Now you will see closed Cases or Opportunities along with non-closed ones in the Sidebar and be able to [search among them](../Searching-for-Existing-Salesforce-Records-and-Creating-New-Records-%28Adaptive-view%29/).

![](../assets/images/Using-SmartCloud-Connect/How-To-s/Create-Custom-View/cases_displayed.png)



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
