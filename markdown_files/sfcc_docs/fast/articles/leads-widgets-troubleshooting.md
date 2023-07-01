--- 
description: Learn how to troubleshoot an issue where no information about Leads is displayed in RG Lead Activity History and RG Lead Sequences widgets in Salesforce 
 
--- 
# How to Troubleshoot Issues with {{ short_company_name }} Lead Activity History and {{ short_company_name }} Lead Sequences Widgets in Salesforce
 
 
<p style="font-size:15px"><i>2 min read</i></font></p>
<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 
&nbsp;

If you successfully installed [{{ company_name }} Managed Package](https://docs.revenuegrid.com/ri/fast/articles/Admin-Managed-Package/) and added [{{ company_name }} widgets](https://docs.revenuegrid.com/articles/sfdc-widgets/) to your Salesforce environment, yet the information about leads is not displayed in [{{ short_company_name }} Lead Activity History](https://docs.revenuegrid.com/articles/sfdc-widgets/#prospects_activity) and [{{ short_company_name }} Lead Sequences](https://docs.revenuegrid.com/articles/sfdc-widgets/#sequences_enrolled) widgets on the Lead page in Salesforce, instead, there is only the *Import to {{ company_name }}* button, you may need to perform several additional setup steps described below.    

&nbsp;

<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\lead-widgets\leads-widgets-issue.png"style="width:100%;"></p>
&nbsp;
  
!!! warning "Important" 
    An **essential prerequisite** for correct automatic import of the information about Leads is the setup of **{{ short_company_name }} Send an Email to Lead**. If it is not added to the Lead page layout in Salesforce, no information will be displayed in {{ short_company_name }} Lead Activity History and {{ short_company_name }} Lead Sequences widgets. Learn how to configure {{ short_company_name }} widgets in [this step-by-step guide](https://docs.revenuegrid.com/ri/fast/articles/Dashboard-Salesforce/) 
&nbsp;    
&nbsp;
***
&nbsp;
  
### **To ensure proper information display in {{ short_company_name }} Lead Activity History and {{ short_company_name }} Lead Sequences widgets:**       
&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1\.** Open {{ company_name }} in your web browser   

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2\.** In the upper right corner of the interface, click on your profile photo   
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**3\.** In the drop-down menu, select **Settings**   
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**4\.** On the Platform Settings, find **Salesforce**    
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**5\.** Select the checkbox *Enable automatic import of prospects into {{ company_name }} from Salesforce email sendout widget*    
<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\lead-widgets\lead-widget-rg.png" class="minimized" style="width:90%;"></p>
&nbsp;
  
<details><summary>Click to see an animation</summary>  
<p><img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\lead-widgets\leads-widgets.gif" class="minimized"></p>
</details>
&nbsp;  
  
  
Performing these steps should result in Leads information auto-import in the widgets, and you will be able to see it in your Sales Console in Salesforce. 

