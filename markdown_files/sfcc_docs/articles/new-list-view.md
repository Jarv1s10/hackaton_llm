---
description: Detailed guide on creating new list views in Salesforce and configuring its filters to work with Revenue Grid
---

# How to create a new list view and configure it to work with Revenue Grid

*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 


You can configure specific list views on the Opportunities tab in Salesforce to ensure that Revenue Grid builds its analytics, forecasts, and reports based on the filtered Salesforce data. The list views created following the instructions provided below are displayed as **Default Filters** in the *Filter by* drop-down list on the Opportunities and reports pages. With such flexible filtering, users can include or exclude specific data from reporting and forecasting in Revenue Grid.
 
This article describes creating a new list view and configuring it to work with Revenue Grid. 

<hr>
 
## Create a new list view in Salesforce 

**1.** Open your Salesforce 

**2.** Switch to **Sales Console** 

**3.** Open the **Opportunity** tab 

**4.** Click on the **Gear** icon in the upper right corner of the Opportunity tab 

**5.** Choose **New**  

**6.** Fill in the required fields: 

* **List Name** – The name of the filter which will be displayed on the list of filters in Revenue Grid. For example, *RG Forecast* 
* **List API Name** – API name which must start with “**REVGRD_**“ to be displayed on the list of filters in Revenue Grid. For example, *REVGRD_Forecast* 

!!! warning "Important" 
    List API Name must start with **REVGRD_** to be displayed on the list of default filters in Revenue Grid 
    
&nbsp;

*  **Who sees this list view?** 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Only I can see this list view** – select this option to create the list view that will be visible only to you. Your colleagues won’t be able to see it.  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**All users can see this list view** – select this option to create the list view that will be visible to all users in your org.  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Share list view with groups of users** – select this option to create the list view that will be visible only to selected groups of users in your org. 

**7.** Save the new list view 



!!! tip "Tip" 
    The created list view will appear on the “*Filter by*” list of filters under *Default Filters* on the Opportunities tab, Forecast Table, Forecast Chart, and on other report pages 
&nbsp;

<hr>
 
## Configure the list filters to match your needs 

After saving the new list view, the filters panel will appear on the right-hand side of the window in Salesforce. 

**8.** Click **Add filter** and select the necessary filtering criteria. For example, you can exclude renewals from reporting and forecasting. 

**9.** Click **Done**

**10.** Save the changes

