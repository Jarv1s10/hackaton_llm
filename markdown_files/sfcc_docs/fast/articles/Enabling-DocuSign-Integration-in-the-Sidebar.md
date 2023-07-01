---
description: Step-by-step guide on how to enable DocuSign integration in the RG Email Sidebar
---
# How To Enable DocuSign Integration in the Sidebar  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

You can effectively work with DocuSign and several other popular online corporate file storages {{ product_name }}.

!!! note "Note"
    Presently, several {{ product_name }} user interface elements, e.g. the Sync settings, refer to *DocuSign* storage by its former name *SpringCM*.

&nbsp;

!!! tip "Tip"
    See [this article](../How-to-work-with-DocuSign-Document-Storage-via-the-Sidebar/) to learn how to work with DocuSign via [{{ product_name }}](../Introduction/)

&nbsp;


### Firewall whitelisting prerequisite

To enable {{ product_name }} Add-In to work with DocuSign storage, your local mail server Administrator should allow-list the following IPs for inbound and outbound connection in the corporate firewall.

!!! tip "Tip"
    Check out the description of a typical whitelisting procedure for the standard Windows 10 firewall [here](https://www.howtogeek.com/112564/how-to-create-advanced-firewall-rules-in-the-windows-firewall/)

&nbsp;

#### For [typical {{ product_name }} DocuSign integration usage](../How-to-work-with-DocuSign-Document-Storage-via-the-Sidebar/)

```
104.44.128.14
13.84.180.32
13.65.255.36
23.98.216.34
13.65.25.127
23.98.220.106
13.65.43.153
52.171.129.2

```

&nbsp;


* * *

&nbsp;

### How to set up DocuSign access in {{ short_name }} Sync Settings



To set up DocuSign document storage access for your {{ product_name }} for Salesforce account, do the following:

*   Open [**{{ product_name }}** Sidebar](../Introduction/)
*   Click the **Menu** button and then select **Sync settings**

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5be0608b04286356f0a56fbb.png)

&nbsp;

*   The [Sync Dashboard](../Configuring-Activities-Synchronization-Settings/) login page will open. After you log in to it via Salesforce OAuth window, navigate to the **Sync settings > Integrations** tab in the pane on the left

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5ae1c4002c7d3a5063b4e64b.png" class="minimized">
</p>

&nbsp;


*   After you click DocuSign's icon in the *Document storage* list, you can view the details of the connected DocuSign account (if one is connected): username (email address), the actual configuration, the DocuSign URL, or you can set up DocuSign connection by clicking the button **Connect**

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5ae1c4572c7d3a5063b4e651.png)

&nbsp;


*   Then do the following:

    **1\.** Choose the environment of the DocuSign account you want to connect (*Production* or *UAT*)

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5ae1c47c2c7d3a5063b4e653.png)

&nbsp;

**2\.** Enter your DocuSign *Login Name* and *Password* and click **Log In**

!!! note "Note"
    All user credentials and data are guaranteed to be secured, under [RevenueGrid Privacy and Security regulations](../Privacy-and-Security/)

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5ae1c4912c7d3a5063b4e655.png)

&nbsp;

**3\.** On the next screen, click **Approve**

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5ae1c4a22c7d3a5063b4e657.png)

&nbsp;

**4\.** Wait around a minute till the access is granted

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5ae1c4b32c7d3a5063b4e658.png)

&nbsp;

Once you have set up DocuSign access, you will notice the following changes in your {{ product_name }}. Reload your Add-In by double-clicking on **Open {{ product_name }} for Salesforce** icon in Microsoft Outlook ribbon.

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5be0611d04286356f0a56fbc.png" class="minimized">
</p>

&nbsp;


*   Click **DocuSign** in the Menu
*   A dialog window will appear on the Sidebar

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5ae31bb72c7d3a3f981f046e.png)

&nbsp;


*   Click the **Settings** button
*   Read [this article]hat you can view details of a **DocuSign** account connected to CRM (on the **Sync settings → Integrations** page in the **Dashboard** (choose **DocuSign** section)). Here you can view the username (email address), actual configuration and URL to login for the actual user

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5ae1c4dd2c7d3a5063b4e65c.png)

&nbsp;

To update **User** credentials used to access **DocuSign** or refresh the **{{ product_name }} for Salesforce** access token click the **Refresh** button. Or click **Disconnect** button to disconnect an access.



&#160;
 &#160;



