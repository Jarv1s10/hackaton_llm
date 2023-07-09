---
description: Detailed description and step-be-step guide on how to implement personalized per-user and admin user setup of widgets
---
# Revenue Grid Widgets: Personalized Per-User Setup and Admin User Setup
  

*3 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

This article is an addition to the [main {{ product_name }} Widgets setup article](../Dashboard-Salesforce/). It describes two special configuration scenarios:

- [Widgets installation on personalized per user basis](../Dashboard-Users-Only/#how_to_configure_contact_lead_or_opportunity_widgets_for_a_salesforce_admin_user_account), used instead of [installing the same set for everyone](../Dashboard-Salesforce/)  
- [Widgets setup for a Salesforce Admin user](../Dashboard-Users-Only/#how_to_configure_contact_lead_or_opportunity_widgets_for_a_salesforce_admin_user_account)  

&nbsp;

## Individualized Widgets Setup on Per-User Basis

{{ product_name }} widgets that can be added to Salesforce interface:

- [{{ short_name }} user Sidebar](../Introduction/)  
- [Opportunity](../Dashboard-Salesforce/#opportunity_widget_blocks)  
- [Contact](../Dashboard-Salesforce/#contact_widget_blocks)  
- [Lead](../Dashboard-Salesforce/#lead_widget_blocks)  
- [{{ short_name }} Admin panel for Admin users](../How-to-Log-In-to-the-Admin-Panel/)  

&nbsp;

### **To Configure {{ product_name }} Widgets in Salesforce**

The prerequisite for configuring {{ product_name }} Widgets for a Salesforce user account is to install {{ company_name }} managed package for the Salesforce Org. Follow the instructions in [this article](../Admin-Managed-Package/) to configure the prerequisites.

After My Domain was configured and [{{ short_company_name }} managed package](../Admin-Managed-Package/) was set up, proceed to Salesforce configuration steps below.

&nbsp;

!!! tip "Tip"
    Please perform the following steps most accurately, since a mistake here is likely to result in [misconfiguration errors](../Dashboard-Troubleshooting/)

&nbsp;

#### 1. Set up tenant URLs
  
For setting up tenant URLs, the Salesforce Admin needs *RevenueGridTenantUrl* and *ServerSyncTenantUrl*. To generate *RevenueGridTenantUrl* and *ServerSyncTenantUrl* required for {{ short_company_name }} Managed Package configuration, you can either contact [our Support team](mailto:support@revenuegrid.com) or follow the instructions provided in the section below.
<br><br>

!!! warning "Important"
    Depending on your license, the appearance of your Sync Settings page may be different. Below you can find instructions on how to generate tenant URLs on the **New** and **Legacy** Sync Settings pages. Proceed with the steps according to the appearance of your Sync Setting page:

    * [Generate tenant URLs on the new Sync Settings page](#generate_tenant_urls_on_the_new_sync_settings_page)
    * [Generate tenant URLs on the legacy Sync Settings page](#generate_tenant_urls_on_the_legacy_sync_settings_page)

&nbsp;

##### Generate tenant URLs on the new Sync Settings page

<p>
    <img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\sync-settings.png" style="width:27.5%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

* Open {{ product_name }}, click the <b>&#x2630; Menu</b> button, go to **Sync settings**

<br><br><br>

* Next, the {{ company_name }} Sync Settings page will open. Find the **address bar** at the top of the page

<p>
    <img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\sync-settings-url.png">
</p>

<br>

* Select the address starting with **https** and ending with **.com**.    
Ignore everything after **.com**

<p>
    <img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\tenant-url.png">
</p>

<br>

The selected address is your *RevenueGridTenantUrl*.

* To generate *ServerSyncTenantUrl*  add the "**-sync**"-part to the address before *.revenuegrid.com* and the **slash** ( **/** ) after *.com*

<br>
In the very end, you should get the URLs  that follow this pattern:

* **RevenueGridTenantUrl**  
https://[ *your tenant* ].revenuegrid.com

* **ServerSyncTenantUrl**    
https://[ *your tenant* ]-sync.revenuegrid.com/

!!! warning "Important"
    Make sure there **is** a slash **/** character at the end of the *ServerSyncTenantUrl* value and there **is no** slash **/** character at the end of the *RevenueGridTenantUrl* value. Otherwise, the users won't get {{ company_name }} Widget content with no issue cause indication    

&nbsp;

***

&nbsp;

##### Generate tenant URLs on the legacy Sync Settings page

* Open {{ product_name }}, click the <b>&#x2630; Menu</b> button, go to **Sync settings**   

* Next, the {{ company_name }} Sync Settings page will open. Find the **address bar** at the top of the page

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\url-generation.png"style="width: 80%; height: 80%;" class="minimized">  
</p>

&nbsp;

* In the address bar, you’ll see the address of the page. Select the address starting with **http** and ending with **.com/**. Ignore everything after .com/

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\selected-url.png"style="width: 80%; height: 80%;">  
</p>

&nbsp;

The selected address is your *ServerSyncTenantUrl*.

* To generate *RevenueGridTenantUrl*  remove the “**-sync**”-part from the address and the **slash** ( **/** ) after *.com*  
In the very end, you should get the URLs  that follow this pattern:

* **RevenueGridTenantUrl**  
https://[ *your tenant* ].revenuegrid.com

* **ServerSyncTenantUrl**    
https://[ *your tenant* ]-sync.revenuegrid.com/

!!! warning "Important"
    Make sure there **is** a slash **/** character at the end of the *ServerSyncTenantUrl* value and there **is no** slash **/** character at the end of the *RevenueGridTenantUrl* value. Otherwise, the users won't get {{ company_name }} Widget content with no issue cause indication    

&nbsp;

##### How to set up tenant URLs

- Switch to Lightning Experience as described in [this Salesforce article](https://help.salesforce.com/articleView?id=000337767&type=1&mode=1)  
- Open [Salesforce *Setup* settings](https://help.salesforce.com/articleView?id=sf.basics_nav_setup.htm&type=5)  
- In the *Quick Search* field type *"Custom Settings"*  
- Click **Manage** button next to the *CanvasAppSettings* label; press *Ctrl+F* to find it quickly if the list is big 

<p><img src= "..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\managed-package-2.png" style="width: 90%; height: 90%;" class="minimized">
</p>

&nbsp;

- Find the settings *RevenueGridTenantUrl* and *ServerSyncTenantUrl*, then click *Edit* to modify them:

<p><img src= "..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\managed-package-3.png" style="width: 90%; height: 90%;" class="minimized">
</p>

&nbsp;

- Update *RevenueGridTenantUrl* with a specific {{ short_company_name }} tenant URL   

- Update *ServerSyncTenantUrl* with a specific {{ short_company_name }} tenant URL

!!! warning "Important"
    Make sure there **is** a slash **/** character at the end of the *ServerSyncTenantUrl* value and there **is no** slash **/** character at the end of the *RevenueGridTenantUrl* value. Otherwise, the users won't get {{ company_name }} Widget content with no issue cause indication

&nbsp;
***
&nbsp;

#### 2. Set up user authorization

- Switch to Lightning Experience as described in [this Salesforce article](https://help.salesforce.com/articleView?id=000337767&type=1&mode=1)  
- Click the **Gear** (Setup Menu) icon in the upper right-hand corner of the page to open [Salesforce Setup menu](https://help.salesforce.com/articleView?id=basics_nav_setup.htm&type=0)  
- In *Quick Search* type "App Manager"  
- Click **Manage** next to *InvisibleSuite* App that has a Type *Connected* (Managed)   

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\user-policies-upd.png" class="minimized">
</p>    

&nbsp;

!!! tip "Tip"
    In case you cannot find the needed item *InvisibleSuite - Connected (Managed)* on the list, sort the list by *Developer Name* and look for *{{ company_name }} for Salesforce*
    ![](../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Widgets/developer_name.png)

&nbsp;

- On the next page, click **Edit Policies**  
- Set the value  **Admin approved users are pre-authorized** in the picklist *Permitted Users*  

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\admin-approved-users.png"style="width: 90%; height: 90%;" class="minimized">
</p>

&nbsp;

- Click **Save** to apply configuration updates  

&nbsp;
* * *
&nbsp;

## How to Configure Contact, Lead, or Opportunity Widgets for a Salesforce Admin User Account

&nbsp;

If you configure the widgets for a regular Salesforce user account, the steps provided in [this article](../Dashboard-Salesforce/) are sufficient; however, for a Salesforce Admin user extra configuration steps are required to setup the widgets for other users in their org. 
  
!!! note "Note"
    The same procedure is used for Contact, Lead, or Opportunity records' layout adding in Salesforce user interface. The steps are identical

&nbsp;

**1\.** Switch to Lightning Experience, as described in [this Salesforce article](https://help.salesforce.com/articleView?id=000337767&type=1&mode=1). Go to Contact, Lead, or Opportunity tab in navigation pane

**2\.** Click the **Gear** (Setup Menu) icon in the upper right corner of the page to open [Salesforce Setup menu](https://help.salesforce.com/articleView?id=basics_nav_setup.htm&type=0)  

**3\.** Select **Edit Page** in the menu  

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\widgets-setup1.png"style="width: 90%; height: 90%;" class="minimized">
</p>

&nbsp;

After you get to the *Lightning App Builder* page, you can modify the page's layout to include {{ company_name }} widgets.

**4\.** Scroll to the bottom of the list in the pane on the left to get to *Visualforce* item  

**5\.** Click **Visualforce** and drag-and-drop this item to the central area:  

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\managed-package-add-widgets.gif" class="minimized">
</p></details> 

&nbsp;

**6\.** Set the functionality for this particular frame emerging from {{ company_name }} by selecting the necessary widget from the drop-down list *"Visualforce Page Name"* (1). The selected widget will appear in the Visualforce component on the page (2)  

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\overview.png"style="width: 70%; height: 70%;" class="minimized">
</p></details> 

&nbsp;

You may add as many Visualforce frames as you require, the limit is the number of {{ company_name }} widget blocks available in the picklist above.

**7.** After completing the widget Setup click **Activation** in the upper right-hand corner

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\activation_button.png"style="width: 45%; height: 45%;">
</p>

&nbsp;

**8.** In the dialog that appears, switch to **App, Record Type, And Profile**    
  
**9.** Click the **Assign to Apps, Record Types, and Profiles** button:  

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\activation_dialogues.png"style="width: 70%; height: 70%;" class="minimized">
</p>

&nbsp;

**10.** Select the Apps that you want to add {{ company_name }} Widgets to; most often these are **Sales** and **Sales Console**   
  
**11.** Click **Next**  

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\activation_select.png" class="minimized">
</p>

&nbsp;

**12.** At the next page, keep the default *Form factor* values **Desktop and phone** and click **Next** in the bottom right-hand corner

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\activation_phone_and_app.png"style="width: 80%; height: 80%;">
</p>

&nbsp;

**13.** Select the checkbox **Master** and click **Next**  

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\activation_master.png"style="width: 70%; height: 70%;">
</p>

&nbsp;
  
**14.** Select applicable profile types. Usually, these are **Standard User** and **System Administrator**. After that click **Next**  

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\activation_user_profiles.png" style="width: 60%; height: 60%;">
</p></details> 

&nbsp;

**15.** Review the sepcified values and click **Save** button to apply configuration updates  

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\activation_save.png"style="width: 80%; height: 80%;"  class="minimized">
</p>

&nbsp;

**16.** Click **Save** in the upper right corner of the *"Lightning App Builder"* page to save configuration updates  

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\save.png">
</p>

&nbsp;

**17.** Return from *"Lightning App Builder"* to the Contact, Lead, or Opportunity tab by clicking the **🡨** (Back) icon in the upper left corner  

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\back_button.png">
</p>

&nbsp;