---
description: How can users and administrators install the RGES Add-In from an XML manifest file or URL
---
# How to Install the Add-In from an XML Manifest File or URL  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*5 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

This article contains detailed instructions to help the users and local Administrators to install the [**{{ product_name }} Outlook Add-In**](../AddIn-vs-Sync-Functions/) Web (Cloud) implementation from a Manifest file (*.xml*) or URL.  
Also see [this Microsoft guide](https://docs.microsoft.com/en-us/office/dev/add-ins/outlook/sideload-outlook-add-ins-for-testing) on MS Outlook Add-Ins installation.  
This solution installation scenario can be used specifically for customized Enterprise implementations of {{ product_name }} including a special set of features and preferences, for example [delegated access components](../Using-MS-Outlook-Delegated-Calendars/) accessed via {{ product_name }}.

!!! tip "Tip"
    Refer to [this article](../Email-Integration-Full-Deployment-Scenarios/) for a summary of various {{ product_name }} mass deployment scenarios.

&nbsp;

&nbsp;

### Installing the {{ product_name }} for Salesforce Add-In in Office 365

To install the {{ product_name }} Add-In, do the following:

**1\.** Open the Add-Ins management dialog in Office 365 Outlook in one of the following ways:

- in MS Outlook Desktop: on the home ribbon, click the Get Add-ins icon

<p><img src="..\..\assets\images\Install-and-Run\get-add-ins.png">
</p>

&nbsp;


- in MS Outlook on the Web: follow the steps 1-4 provided in [this Microsoft article](https://docs.microsoft.com/en-us/office/dev/add-ins/outlook/sideload-outlook-add-ins-for-testing) 

&nbsp;
or

&nbsp;

- open this O365 URL directly in your browser: <https://outlook.office365.com/mail/inclientstore>

&nbsp;

**2\.** If needed, log in with your mail account via the standard Office 365 Sign in dialog 

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5ad4dae22c7d3a0e93675eaa.png">
<br>
<br>
<img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5ad4dadd2c7d3a0e93675ea8.png">
</p></details>



&nbsp;

**3\.** After you log in, the *Add-Ins for Outlook* dialog will be opened. In this dialog, open the tab **My add-ins**

<p><img src="../../assets/images/Getting-Started/First-Steps/install_url_1.png" class="minimized">
</p>

&nbsp;

**4\.** Next, scroll down the tab and click the button **+ Add a custom add-in**

<p><img src="../../assets/images/Getting-Started/First-Steps/custom-add-ins.png" class="minimized">
</p>

&nbsp;

**5\.** You can install the Add-In from one of the following sources

![](../assets/images/Getting-Started/First-Steps/url_file_piece.png)
&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**5.1.** *Add from URL*

* In the *URL* field of the pane that appears, enter the full link leading to the {{ product_name }} installation (.xml manifest) file provided by [{{ company_name }} support team](mailto:support@revenuegrid.com) and click **Next**. 
&nbsp;
  
  ![](../assets/images/Getting-Started/First-Steps/url_piece.png)

  &nbsp;
  
* On the next page, click **Install**

  ![](../assets/images/Getting-Started/First-Steps/file_2.png)
  &nbsp;

  &nbsp;
  
  or
  
  &nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**5.2.** *Add from File*
&nbsp;

* In the Explorer window, navigate to the *.xml* manifest file provided by [{{ company_name }} support team](mailto:support@revenuegrid.com) and click **Open** and then **Next**

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5ad4c666042863075092759f.png" class="minimized">
</p>


  &nbsp;

  

* In the next dialog, click **Continue**

  ![](../assets/images/Getting-Started/First-Steps/file_2.png)

  &nbsp;
  

!!! note "Note"
    {{ product_name }} accesses and handles the end users' email and CRM data in a most secure and private manner, according to our [Privacy and Security guarantees](https://revenuegrid.com/privacy-policy/), so approving this data access is safe. 

&nbsp;

Now the **{{ product_name }}** Add-In will appear in the list of available apps on the *Add-Ins for Outlook* page.

&nbsp;

**6\.** To verify that the {{ product_name }} Add-In was installed successfully, check that the new *Salesforce* ribbon group has appeared in MS Outlook ribbon

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5ad4c6fb2c7d3a0e93675d60.png)

&nbsp;

&nbsp;

* * *

&nbsp;

### Installing the {{ product_name }} for Salesforce Add-In for MS Exchange on Premise

&nbsp;

To install the **{{ product_name }}** Add-In, do the following:

**1.** Open your corporate [Outlook on the Web page](https://docs.microsoft.com/en-us/exchange/troubleshoot/client-connectivity/set-up-web-access) URL in your browser. If you do not have the URL, you can contact your local MS Exchange Administrator to get it

!!! tip "Tip"
    You may also be able to find out the URL using your MS Outlook Desktop client. In Outlook Desktop: open the **File** tab, then click the item **Info**. Next, copy the URL displayed under the line *"Access this account on the web"* at the top

&nbsp;

**2.** Enter your login (the domain / user name) and password into the designated fields on the page and click **Sign in**

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5ad5e3a10428630750927e74.png)

&nbsp;

**3.** If your username and password are correct, the **Mail** page (the **Inbox** by the default) opens

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5ad5e3fb0428630750927e77.png" class="minimized">
</p>

&nbsp;
**4.** Click the  **Menu **icon and select **Options** in the upper right corner of the window

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5ad5e44b2c7d3a0e9367655d.png)

&nbsp;

**5.** Click the **General** tab and choose **Manage add-ins**

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5ad5e4c40428630750927e84.png" class="minimized">
</p>

&nbsp;

**6.** Click the **+** (Add) button and then choose the source you want to install the Add-In from

![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5ad5e5180428630750927e8b.png)

&nbsp;


&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**6.1.** [Add from AppSource](../How-to-Install-and-Run-the-Solution-all-configurations/#1_installing_smartcloud_connect_outlook_add-in_standard_webcloud_installation). At AppSource page that opens, search for *{{ product_name }} for Salesforce*, open the Add-In's page and click **Add**. Note, this option is applicable only for the {{ product_name }} for Salesforce product.  
Any other customized product implementations should be installed either from an URL or a Manifest file.

&nbsp;

or

&nbsp;

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **6.2.** Install from a URL

* In the *URL* field of the pane that appears, enter the {{ product_name }} installation URL provided by [{{ company_name }} support team](mailto:support@revenuegrid.com), an *.xml* manifest file hosted on the web. Then click **Next** 


![](../assets/images/Getting-Started/First-Steps/url_piece.png)

&nbsp;

* On the next page, click **Install**

![](../assets/images/Getting-Started/First-Steps/file_2.png)

&nbsp;

!!! note "Note"
    {{ product_name }} accesses and handles the end users' email and CRM data in a most secure and private manner, according to our [Privacy and Security guarantees](https://revenuegrid.com/privacy-policy/), so approving this data access is safe 

&nbsp;

or

&nbsp;

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **6.3.** Install from an .xml file (manifest)

* Click **Browse** in the pane that appears

![](../assets/images/Getting-Started/First-Steps/file_piece.png)

&nbsp;

* In the Explorer window, navigate to the .xml manifest file provided by [{{ company_name }}](mailto:support@revenuegrid.com) and click **Open** and then **Next**

<p><img src="../../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5ad4c666042863075092759f.png" class="minimized">
</p>

&nbsp;

* On the final step, click **Install**

  ![](../assets/images/Install-and-Run/exch-confirmation.png)
&nbsp;

&nbsp;

!!! note "Note"
    {{ product_name }} accesses and handles the end users' email and CRM data in a most secure and private manner, according to our [Privacy and Security guarantees](https://revenuegrid.com/privacy-policy/), so approving this data access is safe 

&nbsp;

Now the **{{ product_name }}** Add-In will appear in the list of available apps on the *Add-Ins for Outlook* page.

&nbsp;

**7\.** To verify that the {{ product_name }} Add-In was installed successfully, check that the new *Salesforce* ribbon group has appeared MS Outlook ribbon


![](../assets/images/d33v4339jhl8k0cloudfrontnet/docs/assets/57398d2e903360669faf1f0a/images/5ad4c6fb2c7d3a0e93675d60.png)
&nbsp;



&#160;
 &#160;

