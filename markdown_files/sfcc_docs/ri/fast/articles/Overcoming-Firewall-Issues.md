---
description: Step-by-step guidance on configuring the corporate firewall to get the Solution running
---
# How to Configure the Corporate Firewall to Get the Solution Running  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*4 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

To handle customers' data enclosed in a secured corporate environment, {{ product_name }}'s components [{{ short_name }} Add-In / Chrome Extension](../AddIn-vs-Sync-Functions/) and [{{ short_name }} Sync Engine](../Synchronization-Engine-An-Overview/) require two sets of allow-list rules to be configured by the local mail server and Salesforce Admins:  
**1.** {{ short_name }} infrastructure IPs allow-listed to access the corporate mail server and Salesforce  
**2.** Firewall exceptions configured for end users' work devices. All listed {{ company_name }} and third-party resources are guaranteed to be secure, according to [{{ company_name }} privacy and security policies](../Privacy-and-Security/#privacy_and_security); all transferred data is encrypted with [TLS 1.2](https://en.wikipedia.org/wiki/Transport_Layer_Security)  

All {{ product_name }} traffic is intended to go directly, <u>not</u> through a proxy connection. 

&nbsp;

**Why do the IPs get changed in some updates?**

- {{ short_name }} server-side performance boosting (with up-to-date server equipment)
- Possible server-side disaster recovery scenarios improvement, by reducing users impact and functions recovery time (using the extra backup servers)
- Some of the reserved addresses are in resting state, they will be used in case of main servers downing, ensuring minimum users impact; they will be left unchanged in case of future server-side migrations

&nbsp;



&nbsp;

#### November 2021 {{ company_name }} Resources' IP Update

In November 2021 {{ company_name }} Azure resources' IPs got updated, ensuring: A. extra stability considering geographic proximity; B. even more security; C. allow-list config facilitation. During November 2021, all customers must add the four new ranges to their allow-lists and remove the old {{ short_name }} IPs from the allow-lists.

Starting with December 2021, to access customers' corporate mail servers and Salesforce [{{ company_name }} Sync Engine](../Synchronization-Engine-An-Overview/) and [Add-In / Chrome Extension](../Introduction/) will be using only four designated IP ranges in different geographic locations: US Central and US East, Europe West and Europe North; four main use and four standby IPs are allocated within every range.

[{{ short_name }} Chrome Extension for Google](../Chrome-Extension-Intro/) requires the same set of IPs, plus [Chrome Web Store](https://chrome.google.com/webstore/category/extensions) resource allow-listing is required.



&nbsp;

&nbsp;

#### 1. {{ short_name }} Resources Allow-Listed to Access the Mail Server and Salesforce

!!! tip "Tip"
    A *mask* - an IP ending with /28, /29, /30, /31, etc. on the lists represents a hidden range of several secure affiliated IPs allocated with [Classless Inter-Domain Routing (CIDR)](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing). For customers' convenience, we've expanded ranges of the updated masks list

&nbsp;



All these are *Inbound* connections; MS Exchange / O365 / Google and Salesforce servers getting accessed by {{ company_name }} components. Protocol: 443 / HTTPS



```
Dedicated IPs added in November 2021:

20.112.208.0/29 mask
actual range 20.112.208.0 - 20.112.208.7

20.80.207.144/29 mask
actual range 20.80.207.144 - 20.80.207.151

20.103.185.48/29 mask
actual range 20.103.185.48 - 20.103.185.55

20.105.57.72/29 mask
actual range 20.105.57.72 - 20.105.57.79
```
&nbsp;

##### For EU-only Customers

If you need a EU-only Data Locality and you have got a confirmation from {{ company_name }} team that your {{ short_name }} tenant is provisioned with enabled *Data Locality* feature, you may allow-list only the dedicated EU ranges:

```
20.103.185.48/29 mask
actual range 20.103.185.48 - 20.103.185.55

20.105.57.72/29 mask
actual range 20.105.57.72 - 20.105.57.79
```

&nbsp;

&nbsp;

##### Full {{ company_name }} Package IPs

These IPs must be allow-listed in every organization that uses the [full {{ company_name }} package](https://docs.revenuegrid.com/) to enable its functioning. Also see [this article](https://docs.revenuegrid.com/articles/Overcoming-Firewall-Issues/) for more information.

````
Sequenced outbound emails automation, Campaigns, Sales Engagement:
52.173.139.99
52.173.188.229
52.173.184.127
52.173.186.243
52.173.190.95
52.176.107.202
52.173.184.202
52.173.190.226
	

{{ company_name }} Signals:
23.99.196.180
168.61.185.160
168.61.178.14
23.99.133.3
104.43.130.88
168.61.153.98
168.61.165.70
168.61.188.249


Indexer:
40.119.56.217

Auxiliary:
Org's Microsoft Exchange (OWA, ECP,EWS, etc.), if needed
login.salesforce.com and its dependencies
fonts.gstаtic.com
chrome.google.com for {{ short_name }} Chrome Extension
````



&nbsp;

&nbsp;

##### Handling Salesforce Access Restrictions

In addition, in some Orgs Salesforce logging in and data access are restricted for a pre-set IP addresses range. If you cannot log in to Salesforce via {{ product_name }}, make sure that the above listed IP addresses are included in Login / Trusted IP ranges of your [Salesforce account](https://help.salesforce.com/articleView?id=mc_si_update_ip_ranges.htm&type=5) or [Org](https://help.salesforce.com/articleView?id=security_networkaccess.htm&type=5). Please find more info on how to manage them in  [this official Salesforce blog](https://developer.salesforce.com/blogs/tech-pubs/2015/09/login-ip-ranges-security.html) or their official documentation regarding [Login IP ranges](https://developer.salesforce.com/docs/atlas.en-us.securityImplGuide.meta/securityImplGuide/users_profiles_epui_login_ip_ranges_edit.htm) and [Trusted IP ranges](https://developer.salesforce.com/docs/atlas.en-us.securityImplGuide.meta/securityImplGuide/security_networkaccess.htm).

&nbsp;

&nbsp;

* * *

&nbsp;

#### 2. Work Devices' Firewall Exceptions for {{ short_name }} Add-In / Chrome Extension

!!! tip "Tip"
    Contact your firewall software vendor for guidance how to configure allow-list rules

&nbsp;


All these are Outbound connections from end users' work devices. Protocol: 443 / HTTPS

&nbsp;

##### Main {{ company_name }} Resources

```
*.revenuegrid.com
*.invisible.io
*.invisiblesolutions.com
*.smartcloudconnect.io
```

&nbsp;

##### Auxiliary Resources

These are auxiliary CDN, API, Microsoft, Google, Cloudflare, Bootstrap, etc. resources used by the solution.

```
*.revenuegrid.commaxcdn.bootstrapcdn.com
appsforoffice.microsoft.com
fonts.googleapis.com
cdnjs.cloudflare.com
ajax.googleapis.com
az416426.vo.msecnd.net
```

&nbsp;

##### Extra Resources for Troubleshooting

Add these additional resources to firewall exceptions if issues occur on opening [{{ product_name }}](../Introduction/), [Sync dashboard](../How-to-Open-Sync-Dashboard-(Adaptive-view)/), [Customization page](../Customization-Settings-Explained/), or [{{ short_name }} Admin panel](../How-to-Log-In-to-the-Admin-Panel/). These are required Salesforce, Microsoft, wizards or guides rendering, and other relevant resources.  
In addition, to be able to access Sync Engine settings make sure that your browser's ad blocking plugins (e.g. AdBlock Plus or uBlock Origin) are disabled for {{ short_name }} Sync dashboard web page.

```
*.smartcloudconnect.io
*.salesforce.com
dc.services.visualstudio.com
logo.clearbit.com
autocomplete.clearbit.com
api.genderize.io
api.ipify.org
static.userguiding.com
api.userguiding.com
ust.userguiding.com
```

&#160;
 &#160;

