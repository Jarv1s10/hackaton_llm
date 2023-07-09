---
description: How to configure the possibility to embed custom Canvas App widgets and dashboards into regular user or Admin user interfaces
---
# Dashboard Widgets Prerequisite: My Domain in Salesforce  
  

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

This article is an addition to the [main {{ company_name }} Salesforce managed package setup article](../Admin-Managed-Package/). It describes how to configure the possibility to embed custom [Canvas App](https://developer.salesforce.com/docs/atlas.en-us.platform_connect.meta/platform_connect/canvas_framework_intro.htm) widgets and dashboards into regular user or Admin user interfaces in a Salesforce Org.

!!! tip "Tip"
    Refer to [this Salesforce article](https://developer.salesforce.com/docs/atlas.en-us.platform_connect.meta/platform_connect/canvas_framework_supported_browsers.htm) for the list of web browsers officially compatible with Salesforce Canvas widgets

&nbsp;

&nbsp;

## Configure My Domain for Your Salesforce Org



A crucial prerequisite is to configure [*My Domain* for your Salesforce Org](https://help.salesforce.com/articleView?id=sf.domain_name_overview.htm&type=5) in advance, as most Org Admins skip doing that. See [this Salesforce guide](https://salesforce.vidyard.com/watch/oFQ26FCXPVOA90xZaVDDjA) or follow the instructions below to configure it.

 

[My Domain](https://help.salesforce.com/articleView?id=sf.domain_name_overview.htm&type=5) serves as a native Salesforce framework that allows embedding custom widgets like {{ company_name }} / {{ product_name }}. My Domain is also required to install [*{{ short_name }}* Managed Package](../Admin-Managed-Package/).  

!!! warning "Important"
    Salesforce automatically assigns a default a domain name to any newly created org. However, it's recommended to change the default domain to the custom one to prevent any issues with using the full scope of {{ company_name }} managed package functionality.


Complete configuration Steps 1-4 to set up My Domain:  

### Setup Step 1

- Log in to Salesforce with [Admin credentials](https://admin.salesforce.com/blog/2020/introducing-admin-center-a-new-home-for-salesforce-administrators)  
- Switch to Lightning Experience as described in [this Salesforce article](https://help.salesforce.com/articleView?id=000337767&type=1&mode=1)  
- Click the **Gear** (Setup Menu) icon in the upper right corner of the page to open [Salesforce Setup menu](https://help.salesforce.com/articleView?id=basics_nav_setup.htm&type=0)  
- In the *Quick Search* field in the upper left corner, type *"My Domain"* to quickly find the necessary setting  

&nbsp;
***
&nbsp;

### Setup Step 2

- On *My Domain Settings* page, click **Edit**

- Generate a relevant domain for your Org and enter it into *My Domain Name* field  

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\my-domain\my-domain-settings.png" style="width=70%" class="minimized">
</p>

&nbsp;

- After that, click **Check Availability** to see if you can use this domain name      

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\my-domain\my-domain-availability.png" class="minimized">
</p>  
&nbsp;  

- If the name is not available, generate another available one  

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\my-domain\my-domain-unavailable.png" style="width: 90%; height: 90%;" class="minimized">
</p>
&nbsp;

- If the name is available, click **Save** button    

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\my-domain\my-domain-save.png" class="minimized">
</p>   
&nbsp;  
  

- Next, the domain provisioning will start  

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\my-domain\my-domain-provisioning.png" class="minimized">
</p></details> 
&nbsp;  

***    

&nbsp;

### Setup Step 3

- As soon as the domain is set up and provisioned, you'll receive a confirmation email in Salesforce Admin's mailbox    

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\my-domain\my-domain-email.png">
</p></details>   

&nbsp;  

- Refresh My Domain page in your web browser to make sure it works


- Now the button **Deploy New Domain** becomes active, click it to finish My Domain configuring

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\my-domain\my-domain-deploy.png">
</p>  

&nbsp;
***
&nbsp;

### Setup Step 4    

- Once you click **Deploy New Domain** button, you will be automatically redirected to Salesforce *Log In* page. 

- It is not recommended to adjust any other My Domain configuration settings

- After all required actions are performed, you will see that the domain name on *My Donain Settings* has changed:  

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Widgets\my-domain\my-domain-final.png" class="minimized">
</p>

&nbsp;

&nbsp;

