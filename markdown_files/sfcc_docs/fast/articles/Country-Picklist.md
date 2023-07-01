---
description: Step-by-step guide on setting up country code picklist in the RG Email Sidebar
---
# How to Set Up Country Code Picklist in the Sidebar  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

If your Salesforce Org configuration includes the [Country picklist](https://help.salesforce.com/articleView?id=admin_state_country_picklists_overview.htm&type=5) for Contact objects, the picklist will **not** be displayed in [{{ product_name }}](../Introduction/) for such objects out-of-the-box.

To get the picklist listed in the Sidebar, do the following:

**1\.** Open [{{ short_name }} Customization settings](../Customization-Settings-Explained/#1_how_to_open_customization_page)

**2\.** On the [page's central pane](../Customization-Settings-Explained/#8_customizing_detailed_card_view), find the object type *Contact*

**3\.** Click **Detailed view** at the bottom of the object's tab. The "*Contact - Fields to be available in sidebar Add-In*" dialog will appear

**4\.** Type "*Mailing Country Code (Picklist)*" in the *Filter* field and click **+** to add it. The field's name is not intuitive but that's the required picklist

**5\.** Apply the updated settings by clicking **Save** in the upper right corned of the Customization settings page

&nbsp;

Now, after your reopen MS Outlook, the *Mailing Country Code* picklist will be present in the Sidebar for opened Contact objects.

&#160;
 &#160;

