---
description: An overview of Revenue Intelligence package setup, configuration and functionality
---

# Intelligence Package Rollout

**[admin-level article]**
&nbsp;

*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

This article describes the step-by-step rollout of [Intelligence Package](https://revenuegrid.com/pricing/). It includes the steps that should be performed by the org's admins (e.g., *Salesforce and corporate firewall configuration, Managed package installation, assignment of Signals Managers and signals configuration*) and by the solution's end users (e.g., *installation of RG Email Sidebar, signing in to Revenue Grid*). All described steps are mandatory to ensure the correct functioning of the solution.

!!! warning "Important"  
    Intelligence Package must be rolled out by users with admin rights in Salesforce and Revenue Grid. The first user who signs up with the solution automatically acquires admin rights in Revenue Grid. 

<br>
Intelligence Package rollout comprises the following steps: 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Step 1. [Configure your Salesforce](../intelligence-package-rollout/#step_1_configure_your_salesforce) 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Step 2. [Install Revenue Grid Salesforce managed package](../intelligence-package-rollout/#step_2_install_revenue_grid_salesforce_managed_package) 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Step 3. [Configure the corporate firewall](../intelligence-package-rollout/#step_3_configure_the_corporate_firewall) 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Step 4. [Install RG Email Sidebar](../intelligence-package-rollout/#step_4_install_rg_email_sidebar) 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Step 5. [Sign in to Revenue Grid](../intelligence-package-rollout/#step_5_sign_in_to_revenue_grid) 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Step 6. [Configure Signals](../intelligence-package-rollout/#step_6_configure_signals) 

<br>

<hr>


## Step 1. Configure your Salesforce 
 
!!! note "Note"  
    The Salesforce configuration described below is not obligatory. Intelligence Package can function without them out-of-the-box. However, it’s recommended to finetune your Salesforce space as described because these prerequisites contribute to better data visualization and visibility in reports, forecasts, and charts. 

Revenue Grid uses Salesforce data for analytics, forecasts, reports, and other functionality of Intelligence Package. Correct configuration and setup of your Salesforce org are crucial to ensure that the whole range of the functionality offered by the solution is available to users.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1.1.** <a href="https://docs.revenuegrid.com/ri/fast/articles/Dashboard-Prerequisites/" target="_blank">Configure customized My Domain</a> in Salesforce

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1.2.** <a href="../collaborative-forecasts/" target="_blank">Enable Collaborative Forecasts</a>  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1.3.** <a href="../role-hierarchy/" target="_blank">Set up the Role Hierarchy</a>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1.4.** <a href="https://docs.revenuegrid.com/ri/fast/articles/assign-forecasting-manager-role/" target="_blank">Enable users in Collaborative Forecasts and select forecast managers</a>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1.5.** <a href="../assign-quotas/" target="_blank">Assign Quotas to Users</a> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1.6.** <a href="../forecast-category-and-opportunity-stage/" target="_blank">Check your org's Forecast Categories configuration</a> and if necessary <a href="../forecast-category-and-opportunity-stage/#how_to_change_stage_mapping_for_forecast_categories" target="_blank">adjust the mapping between Opportunity Stages and Forecast Categories</a>  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1.7.** <a href="../new-list-view/" target="_blank">Create a new  Salesforce list view</a> to filter the Opportunities to be displayed in Revenue Grid

<br> 

<hr>

## Step 2. Install Revenue Grid Salesforce managed package

Revenue Grid Salesforce managed package is a part of the solution that should be installed to enable the additional features like the auxiliary custom fields, classes, widgets, forecasts, reports, and other components.


Installation of Revenue Grid Salesforce managed package consists of several steps:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2.1.** <a href="https://docs.revenuegrid.com/ri/fast/articles/Admin-Managed-Package/#i_install_revenue_grid_managed_package" target="_blank">Install Revenue Grid managed package</a>  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2.2.** <a href="https://docs.revenuegrid.com/ri/fast/articles/Admin-Managed-Package/#ii_configure_the_app_in_salesforce" target="_blank">Configure the Revenue Grid app in Salesforce</a>  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2.3.** <a href="https://docs.revenuegrid.com/ri/fast/articles/Dashboard-Salesforce/" target="_blank">Configure RG Widgets in Salesforce</a>   

&nbsp;

!!! warning "Updating managed package"   
    Revenue Grid managed package gets updated regularly. Each update includes functionality improvements and bugfixes. Thus, to ensure that your company can take the most of using Revenue Grid, it's crucial to have the latest version of Revenue Grid managed package installed. 
    
    You can find the link to the latest version of the package in the topmost section of [this article](https://docs.revenuegrid.com/ri/fast/articles/Admin-Managed-Package/#:~:text=You%20can%20get%20the%20latest%20version%20of%20the%20managed%20package%20here)
 &nbsp;
      
<hr>

## Step 3. Configure the corporate firewall   


Configure your corporate firewall to work with Revenue Grid as described in <a href="https://docs.revenuegrid.com/ri/fast/articles/Overcoming-Firewall-Issues/" target="_blank">this article</a>.


&nbsp;

<hr>

## Step 4. Install RG Email Sidebar 

Next, end users must install RG Email Sidebar and activate the sync by connecting their Salesforce account and mailbox. 


Refer to [this article](https://docs.revenuegrid.com/ri/fast/articles/First-Steps/) for the list of articles describing how users can install and run RG Email Sidebar on different operating systems, mail servers, and devices.

<br>

!!! tip "Tip"
    If your company requires other deployment scenarios other than the independent installation of the solution by end users, refer to the [Frequently asked questions](../intelligence-package-rollout/#frequently_asked_questions) section below to learn more about mass deployment and impersonation options


&nbsp;

<hr>

## Step 5. Sign in to Revenue Grid 

Next, the end users must sign in to Revenue Grid as described in [this article](https://docs.revenuegrid.com/articles/Setup/) using the same mailbox and Salesforce account they specified on signing in with RG Email Sidebar.


&nbsp;
<hr>

## Step 6. Configure Signals 

Besides the signals that are enabled by default and manually created by the end users, Revenue Grid also offers configurable signals that are created and managed by admins and Signals Managers, i.e., users with signals configuration management rights. 

In this step, admins should appoint users who can manage signals in Revenue Grid and configure the signals in the Signals Builder to ensure that users get the required notifications.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**6.1.** [Allow signals configuration management for specific users](../signals-manager/) 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**6.2.** [Configure the necessary signals in Signals Builder](https://docs.revenuegrid.com/ri/fast/articles/signals-settings-and-parameters/) 

&nbsp;

!!! warning "Important"  
    A prerequisite for using all signals is the sync activation by connecting with the Salesforce account and mailbox and [signing in to Revenue Grid](https://revenuegrid.com/log-in/). It means that only the users with active sync, who signed in to Revenue Grid at least once, will receive all relevant signal notifications. If the sync is not active, Revenue Grid is not able to detect any inbound/outbound emails and events in user's mailbox. Thus, no signals based on this data are generated.




&nbsp;
<hr>

## Frequently asked questions 

This section provides the answers to the most frequently asked questions about Intelligence Package rollout.

&nbsp;

#### 1. How to provision the end users if my company won’t use RG Email Sidebar with the Intelligence package?

If your company will not use RG Email Sidebar, the end users should be provisioned with the user Registration Wizard as described in <a href="https://docs.revenuegrid.com/ri/fast/articles/User-Registration-Wizard/" target="_blank">this help article</a>. Our Support team will provide you with the Registration Wizard link tailored specially for your company.
<br><br><br>


#### 2. Are there any options for mass deployment of RG Email Sidebar?

Yes, mass deployment scenarios are avaliable for all compatible mail servers: 
<ul>
    <li> <a href="https://docs.revenuegrid.com/ri/fast/articles/Mass-Deployment-of-the-Add-In-Office-365/" target="_blank">Mass Deployment of the Add-In (Office 365)</a></li>
    <li> <a href="https://docs.revenuegrid.com/ri/fast/articles/Mass-Deployment-of-the-Add-In-MS-Exchange/" target="_blank">Mass Deployment of the Add-In (MS Exchange 2016, 2019)</a></li>
    <li> <a href="https://docs.revenuegrid.com/ri/fast/articles/Chrome-Extension-Mass-Deployment/" target="_blank">Mass Deployment of the Chrome Extension for Gmail</a></li>
</ul>
<br><br><br>


#### 3. Can my company use Impersonation for easier management of the connection?

If necessary, the you can use the Impersonation to ensure the for easier management of the users' connection. Refer to the relevant help article to learn how to configure it:
<ul>
    <li><a href="https://docs.revenuegrid.com/ri/fast/articles/Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/" target="_blank">How to Set Up Sync via Impersonation & Configure User Mailboxes</a></li> 
    <li><a href="https://docs.revenuegrid.com/ri/fast/articles/Impersonation-O365/" target="_blank">How to Configure Impersonation to Deploy the Solution (Office 365)</a></li> 
    <li><a href="https://docs.revenuegrid.com/ri/fast/articles/Set-up-An-Impersonation-Service-Account/" target="_blank">How to Configure Impersonation to Deploy the Solution (MS Exchange On-Premises)</a></li> 
    <li><a href="https://docs.revenuegrid.com/ri/fast/articles/Impersonation-Graph/" target="_blank">How to Configure Impersonation to Deploy the Solution via MS Graph Connection (Office 365)</a></li> 
    <li><a href="https://docs.revenuegrid.com/ri/fast/articles/Impersonation-Alternative/" target="_blank">Impersonation Setup: Hybrid Scenarios</a></li> 
</ul>
<br><br><br>

#### 4. With what Salesforce editions is Intelligence Package compatible?

Intelligence Package is compatible with all Salesforce editions that include Collaborative Forecasts, including Sales Cloud, Sales & Service Cloud, Financial Services, Experience Cloud editions. 
<br><br>
Refer to <a href="https://docs.revenuegrid.com/ri/fast/articles/Supported-Salesforce-Editions/" target="_blank">this article</a> for more specific information on supported Salesforce editions.
<br><br><br>

#### 5. Can Intelligence Package be used with Partner Community licenses?

Intelligence Package is compatible with Saleaforce Partner Community licenses. Your partner portal user's opportunities roll up to the forecast of the account owner, who is this user's forecast manager in the role-based forecasts hierarchy. 
<br><br>
Refer to <a href="https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/forecasts.pdf" target="_blank">this Salesforce guide</a> to learn how partner portal users can work with Collaborative Forecasts.
<br><br>

!!! warning "Important"
    Revenue Grid supports only the following Salesforce Experience Cloud subdomains: <u>force.com</u>, <u>salesforce.com</u>, <u>siteforce.com</u>, <u>my.site.com</u>