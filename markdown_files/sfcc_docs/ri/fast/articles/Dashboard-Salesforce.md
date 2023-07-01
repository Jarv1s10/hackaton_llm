---
description: Learn how to add and configure Revenue Grid Widgets in Salesforce interface
---
# How To Add Revenue Grid Widgets in Salesforce
  

*8 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

In the context of Salesforce user interface, a {{ company_name }} / {{ product_name }} widget is a visual representation of your CRM and business communication data rendered via [Salesforce Canvas app](https://developer.salesforce.com/docs/atlas.en-us.platform_connect.meta/platform_connect/canvas_framework_intro.htm) pane. Sales management widgets normally include detailed Salesforce information on Lead, Contact, or Opportunity engagement status, sales reports, conversion/win rate, average deal size, revenue, etc. A Sales management widget allows Sales Managers to monitor the performance of their sales teams with the help of accurate metrics. What is more, sales widgets can help sales reps analyze their progress and see what else they should do to meet their quota.

There are several types of sales widgets: sales representative widgets, sales manager widgets, deal performance widgets, and more.

{{ company_name }}’s Sales Widgets allow you to instantly view how well your team is engaging with important deals or Opportunities that need a fast reply, and make sure you act right on opportunities with no planned activities or old Opportunities with no recent activities.

The configurable widgets offered by {{ company_name }} are based on [Salesforce native Canvas App technology](https://developer.salesforce.com/docs/atlas.en-us.platform_connect.meta/platform_connect/canvas_framework_intro.htm). Refer to [this Salesforce article](https://developer.salesforce.com/docs/atlas.en-us.platform_connect.meta/platform_connect/canvas_framework_supported_browsers.htm) for the list of web browsers officially compatible with Salesforce Canvas widgets. 

Specific {{ product_name }} widgets that can be added to Salesforce interface:

- [{{ short_name }} user Sidebar](../Introduction/) 
- Opportunity records
- Contact records
- Lead records
- Sync settings and Sync config
- [{{ short_name }} Admin panel for Admin users](../How-to-Log-In-to-the-Admin-Panel/)

Refer to [this {{ company_name }} Docs article](https://docs.revenuegrid.com/articles/sfdc-widgets/#widgets_related_to_email_and_crm_integration_component) to get a notion of what each of these widgets looks like.

&nbsp;


Also see [this dedicated article](../Dashboard-Users-Only/) to learn how to configure personalized widgets sets for different users or set up the widgets for a Salesforce Admin user.

In addition to that, you may add to your Salesforce the widgets [Engagement](https://docs.revenuegrid.com/articles/Planner/) and [Signals](https://docs.revenuegrid.com/articles/Signals/) specific for the [full {{ company_name }} revenue intelligence package](https://docs.revenuegrid.com/). See [this article](https://docs.revenuegrid.com/articles/sfdc-widgets/) for complete information.
&nbsp;
***
&nbsp;

## How To Configure {{ product_name }} Widgets in Salesforce
&nbsp;

### Stage 1: Configuration Prerequisites  
&nbsp;  

{{ product_name }} Widgets setup is based on several essential Salesforce configuration prerequisites. Omitting either one of these prerequisites will result in errors. See [this article](../Dashboard-Troubleshooting/) for information on troubleshooting different widgets configuration errors.

!!! note "Note"
    All configuration actions are performed via a [local Salesforce Admin account](https://www.salesforce.com/blog/what-is-a-salesforce-admin/). All these adjustments are guaranteed to be secure under [{{ company_name }} Privacy and Security policies](https://revenuegrid.com/privacy-policy/)

&nbsp;

**1\.1.** First and foremost, submit a request that you intend to configure {{ short_name }} Salesforce widgets to [our support team](mailto:support@revenuegrid.com). In the request, make sure to specify what widgets are going to use: {{ product_name }} ones and/or {{ company_name }} ones. This way you'll get the *ServerSyncTenantUrl* and *RevenueGridTenantUrl* parameters required for the setup. Alternatively, you can generate the tenant URLs following the step-by-step instruction in [this article](../How-to-generate-tenant-urls/) 



**1\.2.** Next, you should enable *My domain* for your Salesforce Org, as described in [this article](../Dashboard-Prerequisites/)  



**1\.3.** Install {{ company_name }} managed package for your Org. See [this article](../Admin-Managed-Package/) to learn how to do that  



**1\.4.** As soon as the prerequisites are configured, proceed to setup Stages 2 and 3 described below  
&nbsp;
***
&nbsp;

### Stage 2: Setup Steps
&nbsp;    

!!! tip "Tip"
    Please perform Stage 2 steps most accurately, since a mistake here is likely to result in [misconfiguration issues](../Dashboard-Troubleshooting/)

&nbsp;

#### 2.1. Set up tenant URLs

&nbsp;
  
Before setting up tenant URls, you need to generate the URLs. To do this, follow the steps described in [this article](../How-to-generate-tenant-urls/).

**2\.1.1.** Switch to Lightning Experience as described in [this Salesforce article](https://help.salesforce.com/articleView?id=000337767&type=1&mode=1)    

**2\.1.2.** Click the **Gear** (Setup Menu) icon in the upper right corner of the page to open [Salesforce Setup menu](https://help.salesforce.com/articleView?id=basics_nav_setup.htm&type=0)    

**2\.1.3.** In the *Quick Search* field in the upper left corner, type *"custom settings"* to quickly find the necessary settings category and click on it    

**2\.1.4.** In the "Custom Settings" pane on the right, click **Manage** next to *CanvasAppSettings*   

The other two REVGRD Custom settings items *{{ company_name }} Values* and *Trigger Settings* should be left intact.

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\configupd1.png" class="minimized">
</p> 

&nbsp;

**2\.1.5.** Next, click **Edit** for CanvasAppSettings

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\configupd4.png" class="minimized">
</p></details> 

&nbsp;

**2\.1.6.** **Edit** the value of the field *ServerSyncTenantUrl* used for {{ product_name }} widgets rendering    

**2\.1.7.** Insert the corresponding URL you [generated](../How-to-generate-tenant-urls/) or received from {{ product_name }} Support team at *Stage 1* into the field  

!!! warning "Important"
    Make sure there **is** a slash **/** character at the end of the *ServerSyncTenantUrl* value. Otherwise, the users won't get {{ short_name }} Widget content with no issue cause indication

&nbsp;  

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Widgets/configupd5-2.png"style="width: 90%; height: 90%;" class="minimized">
</p>  


&nbsp;

**2\.1.8.** **Edit** the value of the field *RevenueGridTenantUrl* used for {{ company_name }} widgets rendering    

**2\.1.9.** Insert the corresponding URL you [generated](../How-to-generate-tenant-urls/) or received from {{ product_name }} Support team at *Stage 1* into the field  

!!! warning "Important"
    Make sure there **is no** slash **/** character at the end of the *RevenueGridTenantUrl* value. Otherwise, the users won't get {{ company_name }} Widget content with no issue cause indication

&nbsp;

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Widgets/configupd5-1.png"style="width: 90%; height: 90%;" class="minimized">
</p> 
&nbsp;

**2\.1.10.** Click **Save** at the top of the page to apply the changes  

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\configupd7.png"style="width: 70%; height: 70%;" class="minimized">
</p></details> 

&nbsp;

The resulting setup should look as follows:  

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\configupd6.png" class="minimized">
</p>  

&nbsp;
***
&nbsp;

#### 2.2. Set up users authorization
&nbsp;    

**2\.2.1.** Switch to Lightning Experience as described in [this Salesforce article](https://help.salesforce.com/articleView?id=000337767&type=1&mode=1)   

**2\.2.2.** Click the **Gear** (Setup Menu) icon in the upper right corner of the page to open [Salesforce Setup menu](https://help.salesforce.com/articleView?id=basics_nav_setup.htm&type=0)   

**2\.2.3.**In the *Quick Search* field in the upper left corner, type "*App Manager*" to quickly find the necessary setting   

**2\.2.4.** Click **Manage** next to *InvisibleSuite* App that has a Type *Connected* (Managed)   

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\user-policies-upd.png" class="minimized">
</p>  
&nbsp;

!!! tip "Tip"
    In case you cannot find the needed item on the list, sort the list by *Developer Name* and look for *{{ company_name }} for Salesforce*
    ![](../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Widgets/developer_name.png)

&nbsp;

**2\.2.5.** On the App's page, click **Edit Policies**   

**2\.2.6.** Set the value  **Admin approved users are pre-authorized** in the picklist *Permitted Users*  

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\admin-approved-users.png"style="width: 90%; height: 90%;" class="minimized">
</p>

&nbsp;

**2\.2.7.** Click **Save** to apply the changes    
&nbsp;
***
&nbsp;

#### 2.3. Set up User profiles
&nbsp;

**2\.3.1.** Switch to Lightning Experience as described in [this Salesforce article](https://help.salesforce.com/articleView?id=000337767&type=1&mode=1)  

**2\.3.2.** Click the **Gear** (Setup Menu) icon in the upper right corner of the page to open [Salesforce Setup menu](https://help.salesforce.com/articleView?id=basics_nav_setup.htm&type=0)  

**2\.3.3.** In the *Quick Search* field in the upper left corner, type "*App Manager*" to quickly find the necessary setting  

**2\.3.3.** Click **Manage** next to *InvisibleSuite* App that has a Type *Connected* (Managed)  

**2\.3.4.** Click **Manage Profiles** on the App's page  

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\manage-profiles.png" class="minimized">
</p>

&nbsp;

**2\.3.5.** Then select the checkboxes of the User Profiles for which the application will be installed. Normally, **Standard Users** would be the targeted profiles among other profiles. It’s recommended to choose **System Administrators** as well


<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Managed-Package/managed-package-manage-profiles.gif" class="minimized">
</p>
  

&nbsp;

**2\.3.6.** Click **Save** button to apply the changes  

&nbsp;  
***
&nbsp;

#### 2.4. Finalizing setup in Salesforce User Interface
&nbsp;

At this stage end users need to get {{ short_company_name }} Widgets mounted in their Salesforce user interface. 

&nbsp;
&nbsp;

#### [Admin Panel](../How-to-Log-In-to-the-Admin-Panel/) and [{{ short_name }} User Sidebar](../Introduction/) widgets



**2\.4.1.** In the upper right-hand corner, open *App Launcher*, select **Sales Console** from the drop-down list that appears   
  
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\widgets-step-1.png"style="width: 50%; height: 50%;">
</p>

&nbsp;

**2\.4.2.**	On the new *Sales Console* page that opens, find the *Navigation panel*. Click on the down arrow (1). On the drop-down menu, click the **Edit** button (2) &nbsp;  

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\widgets-step-2.png"style="width: 70%; height: 70%;" class="minimized">
</p>

**2\.4.3.**	After that click **Add More Items**

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\widgets-step-3- add-more-items.png"style="width: 70%; height: 70%;"  class="minimized">
</p>

&nbsp;

**2\.4.3.** Click **All** (1) in *Available Items*

**2\.4.4.** Select the checkboxes **[Admin UI](../How-to-Log-In-to-the-Admin-Panel/)** and {{ short_name }} **[User UI](../Introduction/)** (2) in the list; they are added after *Managed Package* installation at an earlier step

**2\.4.5.** Click the button **Add 2 Nav Items** (3) at the bottom   
  
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\widgets-step 4-add-2-nav-items.png"style="width: 70%; height: 70%;" class="minimized">
</p>

&nbsp;

**2\.4.6.** Apply the modifications by clicking **Save**

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\widgets_save.png">
</p></details> 

&nbsp;

**2\.4.7.** Both *Admin UI* ([Admin Panel](../How-to-Log-In-to-the-Admin-Panel/)) and *User UI* ([{{ short_name }} User Sidebar](../Introduction/)) tabs are now available on the navigation bar

&nbsp;
* * *
&nbsp;

## Contact, Lead, and Opportunity Widgets Setup
&nbsp;    

!!! note "Note"
    The same procedure is used for Contact, Lead, or Opportunity records' layout adding in Salesforce user interface. The steps are identical

&nbsp;

**1\.** Switch to Lightning Experience, as described in [this Salesforce article](https://help.salesforce.com/articleView?id=000337767&type=1&mode=1). Depending on the widgets you would like to add, go to Contact, Lead, or Opportunity tab in the navigation pane

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

&nbsp;

* * *

&nbsp;

### Specific Widget Blocks

Contact, Lead, and Opportunity widgets have slightly different sets of blocks. Refer to record-specific blocks detailing below:

&nbsp;

#### Contact Widget blocks

**Contact** records' layout can be equipped with the following widget blocks:

- [Revenue Engage](https://docs.revenuegrid.com/articles/Sequences/)-related  
  1. Contact_Overview  
  2. Contact_Activity  
  3. [Contact_Sequences](https://docs.revenuegrid.com/articles/Sequences/)  



- [Revenue Signals](https://docs.revenuegrid.com/articles/Signals/)-related  
  1. [{{ short_company_name }} Signals](https://docs.revenuegrid.com/articles/Signals/)  
  2. [RG_Pipeline](https://docs.revenuegrid.com/articles/Pipeline-visibility/)  



- General use  
  1. [Admin Panel](../How-to-Log-In-to-the-Admin-Panel/)  
  2. [{{ short_name }} User Sidebar](../Introduction/)  




After adding the needed widget blocks, click **Save** in the upper right corner of the *Lightning App Builder* page to apply the changes
<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\save.png">
</p></details> 



&nbsp;

&nbsp;

#### Lead Widget blocks

**Lead** layout can be equipped with the following widget blocks:

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\visualforce_lead.png" class="minimized">
</p></details> 

&nbsp;

- [Revenue Engage](https://docs.revenuegrid.com/articles/Sequences/)-related  
  1. Lead_Activity  
  2. Lead_Overview  
  3. [Lead_Sequences](https://docs.revenuegrid.com/articles/Sequences/)  



- [Revenue Signals](https://docs.revenuegrid.com/articles/Signals/)-related  
  1. [{{ short_company_name }} Signals](https://docs.revenuegrid.com/articles/Signals/)  
  2. [RG_Pipeline](https://docs.revenuegrid.com/articles/Pipeline-visibility/)  



- General use  
  1. [Admin Panel](../How-to-Log-In-to-the-Admin-Panel/)  
  2. [{{ short_name }} User Sidebar](../Introduction/)  

&nbsp;

After adding the needed widget blocks, click **Save** in the upper right corner of the *Lightning App Builder* page to apply the changes

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\save.png">
</p></details> 

&nbsp;

&nbsp;

#### Opportunity Widget blocks

**Opportunity** layout can be equipped with the following widget blocks:

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\visualforce_opportunity.png" class="minimized">
</p></details> 


&nbsp;

- [Revenue Engage](https://docs.revenuegrid.com/articles/Sequences/)-related widgets  
  1. [Opty_RevenueGrid](https://docs.revenuegrid.com/articles/sfdc-widgets/#opportunity_and_account_widgets)  
  2. Opty_RG_Activity  
  3. Opty_RG_Connections  
  4. [Opty_RG_Engagement](https://docs.revenuegrid.com/articles/Planner/)  
  5. [Opty_RG_Signals](https://docs.revenuegrid.com/articles/Signals/)  



- [Revenue Signals](https://docs.revenuegrid.com/articles/Signals/)-related widgets  
  1. [{{ short_company_name }} Signals](https://docs.revenuegrid.com/articles/Signals/)  
  2. [RG_Pipeline](https://docs.revenuegrid.com/articles/Pipeline-visibility/)  



- General use  
  1. [Admin Panel](../How-to-Log-In-to-the-Admin-Panel/)  
  2. [{{ short_name }} User Sidebar](../Introduction/)  

&nbsp;

After adding the needed widget blocks, click **Save** in the upper right corner of the *Lightning App Builder* page to apply the changes

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\save.png">
</p></details> 

&nbsp;



