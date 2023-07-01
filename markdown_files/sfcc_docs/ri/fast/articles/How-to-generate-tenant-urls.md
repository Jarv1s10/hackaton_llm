---  
description: This article provides a step-by-step instruction on generating tenant URLs for RG managed package configuration
---
# How to generate tenant URLs  
  

*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

This article is an addition to the main [{{ product_name }} Widgets setup article](../Dashboard-Salesforce/). It describes how to generate tenant URLs required for {{ short_company_name }} Managed Package configuration.  
  
To generate RevenueGridTenantUrl and ServerSyncTenantUrl, you can either contact [our Support team](mailto:support@revenuegrid.com) or follow the instructions provided below:  

**1.**	Open {{ product_name }}, click the Menu button, and go to **Sync settings**   

**2.**	Next, the {{ company_name }} Sync Settings page will open. Find the **address bar** at the top of the page      
  
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\url-generation.png"style="width: 80%; height: 80%;" class="minimized">  
</p>
&nbsp;

**3.**	In the address bar, you'll see the address of the page. Select the address starting with **http** and ending with **.com/**. Ignore everything after .com/    
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\selected-url.png"style="width: 80%; height: 80%;">  
</p>
&nbsp;


The selected address is your *ServerSyncTenantUrl*.

**4.** To generate *RevenueGridTenantUrl*  remove the “**-sync**”-part from the address and the **slash** ( **/** ) after *.com*  

In the very end, you should get the URLs that follow this pattern:

* **RevenueGridTenantUrl**  
https://[ *your tenant* ].revenuegrid.com

* **ServerSyncTenantUrl**    
https://[ *your tenant* ]-sync.revenuegrid.com/
  
  
!!! warning "Important"
    Make sure there **is** a slash **/** character at the end of the *ServerSyncTenantUrl* value and there **is no** slash **/** character at the end of the *RevenueGridTenantUrl* value. Otherwise, the users won't get {{ company_name }} Widget content with no issue cause indication    

&nbsp;

Save these URLs to be used later during [tenant URLs setup](../Dashboard-Salesforce/#21_set_up_tenant_urls).  
  

&nbsp;

&nbsp;



