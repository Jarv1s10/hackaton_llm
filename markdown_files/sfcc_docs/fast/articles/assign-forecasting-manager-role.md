---
description: Learn how to assign a forecast manager to a hierarchy role in Salesforce
---
# How to Assign a Forecast Manager


*3 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;
  
&nbsp;

The [forecast hierarchy](https://help.salesforce.com/s/articleView?id=sf.forecasts3_hierarchy_overview.htm&type=5) is an expandable list of users or territories involved in [forecasting](https://help.salesforce.com/s/articleView?id=sf.dato_visualize_widgets_advanced_forecasting.htm&type=5). It determines the forecasts roll up in a company and regulates who can access and adjust forecasts.        


The role-based forecast hierarchy utilizes the user [role hierarchy](https://help.salesforce.com/s/articleView?id=sf.ls_create_roles_and_hierarchies.htm&type=5) – users are assigned to forecast managers for specific roles.   
  
  
Only one user may be designated as a Forecast Manager in the forecast hierarchy. This user has access to all forecasts and opportunities of subordinate users in the role hierarchy, while other users in the forecast hierarchy see only their own numbers. Forecast managers can also adjust and modify the reports on their Forecasts tab in Salesforce and see the adjustments introduced by subordinate users.       
    

See [this Salesforce guide](https://help.salesforce.com/s/articleView?id=sf.forecasts3_setting_up_your_forecasts_hierarchy.htm&type=5) or follow the instructions below to assign a forecast manager.

&nbsp;  

!!! warning "Important"  
    Salesforce Role Рierarchy affects {{ company_name }} filters used for [{{ short_company_name }} Opportunities](https://docs.revenuegrid.com/articles/Opportunity-details/) and [team performance analytics](https://docs.revenuegrid.com/articles/sales-rep-performance/). If no forecast manager is assigned to a role in the forecast hierarchy, neither this role nor its subordinate roles are included in the forecasts. The forecast manager should be assigned to key roles to ensure the proper generation of {{ short_company_name }} statistics and reports  
&nbsp;
&nbsp;


## **1\.**	Enable Users in Collaborative Forecasts      
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1.1.**	 Log in to Salesforce with [Admin credentials](https://admin.salesforce.com/blog/2020/introducing-admin-center-a-new-home-for-salesforce-administrators)    
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1\.2\.**	 Switch to Lightning Experience as described in [this Salesforce article](https://help.salesforce.com/articleView?id=000337767&type=1&mode=1)    
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1\.3\.**	Click the **Gear** (Setup Menu) icon in the upper right corner of the page to open [Salesforce Setup menu](https://help.salesforce.com/articleView?id=basics_nav_setup.htm&type=0)    
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1\.4\.**	In the *Quick Search* field in the upper left corner of the page, type *"Users"* to quickly find the necessary setting     
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1\.5\.**	 On the *All Users* page, click **Edit** next to the users you want to enable  

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\assign-forecasting-manager-role\edit-users.png" class="minimized">
</p>  
&nbsp;    

  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1\.6\.**	 On the *General information* section, select the **Allow Forecasting** checkbox    
  
<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\assign-forecasting-manager-role\allow-forecasting-checkbox.png">
</p>  
&nbsp;
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1\.7\.**	Make sure to specify the user's role under *General information*    

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\assign-forecasting-manager-role\user-role.png" class="minimized">
</p>  
&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1\.8\.**	 Click  **Save** button to apply the changes

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1\.9\.** On the *All Users* page, you will see that the assigned role for the user appeared on the list

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\assign-forecasting-manager-role\edit-users-result.png" class="minimized">
</p>  
&nbsp;


&nbsp;
***
&nbsp;


## **2\.**	Select a Forecast Manager for a Manager Role      
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2\.1\.**	 In the *Quick Search* field, type *" Forecasts Hierarchy"* to quickly find the necessary setting        
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2\.2\.**	 On the *Forecasts Hierarchy* page, click **Expand all** to see the whole hierarchy     
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2\.3\.**	  Next, find the role for which you want to select a forecast manager and click **Enable Users**. 

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\assign-forecasting-manager-role\hierarchy-enable-users.png">
</p>  
&nbsp;


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2\.4\.** On the newly opened page, move users (1) between the Available Users and Enabled Users lists using **Add** and **Remove** buttons (2). Apply the modifications by clicking **Save** (3)

<details><summary> >>> Click to see a screenshot <<< </summary>
<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\assign-forecasting-manager-role\forecasts-users.png" class="minimized">
</p>  
&nbsp;
</details>


!!! warning "Important"    
    Please note that only Enabled Users can be assigned to Forecast Manager role
&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2\.5\.**	Click **Edit Manager** next to the role for which you want to select a forecast manager    

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\assign-forecasting-manager-role\hierarchy-edit-manager.png">
</p>  
&nbsp;

  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2\.6\.**	 On the *Forecasts Manager Assignment* page, select the relevant person from the drop-down list (1). Click **Save** button to apply the changes (2)

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\assign-forecasting-manager-role\forecast-manager-list.png">
</p> 

&nbsp;


&nbsp;

&nbsp;

