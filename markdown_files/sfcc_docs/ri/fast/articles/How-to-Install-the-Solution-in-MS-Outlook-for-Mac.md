---
description: Detailed overview of RG Email Sidebar for MS Outlook installation procedure for MacOS
---
# How to Install the Solution in MS Outlook for Mac  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*4 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! note "Note"
    All user data and login credentials passed through {{ product_name }} infrastructure are secured by [{{ company_name }} Privacy & Security principles](../Privacy-and-Security/)

!!! tip "Tip"
    Supported MS Outlook for Mac versions: 2016, 2019

&nbsp;

### For an Office 365 account

<iframe src="https://player.vimeo.com/video/386536131" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
&nbsp;

!!! tip "Tip"
    Alternatively, you can install the Add-In directly via <https://outlook.office.com> or <https://outlook.live.com/owa> opened in your web browser. See the steps in [this article](../How-to-Install-and-Run-the-Solution-for-Office-365-Mailboxes/)

{{ product_name }} installation in MS Outlook for Mac follows the [standard MS Outlook addin installation steps](https://support.office.com/en-ie/article/get-an-office-add-in-for-outlook-1ee261f9-49bf-4ba6-b3e2-2ba7bcab64c8):

**1\.** Click **Get Add-ins** in MS Outlook for Mac ribbon

<p><img src="../../assets/images/Install-and-Run/MacOS/install_1.png" class="minimized">
</p>

&nbsp;

**2\.** MS Outlook Add-In management window will be opened. In the *Search add-ins* box on the right-hand side, type *"{{ company_name }}"* and select **{{ product_name }} for Salesforce**

<p><img src="../../assets/images/Install-and-Run/MacOS/install_2.png" class="minimized">
</p>

&nbsp;

**3\.** In the next window that appears, click **Add**

<p><img src="../../assets/images/Install-and-Run/MacOS/install_3.png" class="minimized">
</p>

&nbsp;

You will see {{ product_name }} icons added to MS Outlook for Mac ribbon.

<p><img src="../../assets/images/Install-and-Run/MacOS/ribbon_icons.png" class="minimized">
</p>

In addition, corresponding controls are now added to your mail account opened in <https://outlook.com> or <https://outlook.live.com/owa/>. See [this article](../Open-in-Outlook-Web/) for more information.



!!! note "Note"
    The Add-In will now also be available for your mail account logged in on other compatible devices with MS Outlook running. This way, you won't need to install it additionally in your MS Outlook Mobile for iOS and Android, Outlook on the Web/Office 365 (<https://outlook.com>, <https://outlook.live.com/owa/>), or MS Outlook for Windows

&nbsp;

**4\.** Next, you need to [log on to {{ product_name }}](../How-to-Install-and-Run-the-Solution-for-Office-365-Mailboxes/#ii_rg_email_sidebar_logon)

#### **Important note: initial log on**

Before you log on to {{ product_name }} in MS Outlook for MacOS, it is necessary to perform an initial log on via [Outlook on the Web](https://searchwindowsserver.techtarget.com/definition/Microsoft-Outlook-on-the-web-formerly-Outlook-Web-App-OWA) in your web browser. This is a one-time step required because of certain peculiarities how the browser pop-up window necessary for the initial {{ short_name }} authentication is handled on MacOS. To do that:

​    &nbsp;&nbsp;&nbsp;&nbsp;**4.1\.** Open <https://outlook.com/> or <https://outlook.office.com/owa> in your web browser and log in with your Office 365 mail credentials

​    &nbsp;&nbsp;&nbsp;&nbsp;**4.2\.** Open {{ product_name }} (see [this article](../Open-in-Outlook-Web/) to learn how to do that)

​    &nbsp;&nbsp;&nbsp;&nbsp;**4.3\.** In the Sidebar, select **Connect to Salesforce** or [another available login option](../How-to-Install-and-Run-the-Solution-all-configurations/#2_logging_on_to_smartcloud_connect). Note: make sure that your Safari browser [does not block pop-up windows](http://osxdaily.com/2019/02/05/how-allow-pop-up-windows-safari-mac/)

![](../assets/images/Install-and-Run/MacOS/logon.png)



​    &nbsp;&nbsp;&nbsp;&nbsp;**4.4\.** A [standard Salesforce Single Sign-On](https://help.salesforce.com/articleView?id=sso_about.htm&type=5) pop-up window will be opened. Enter your Salesforce login credentials and click **Log in** to authorize {{ short_name }} to work with your Salesforce data.
![](../assets/images/Install-and-Run/MacOS/sso.png)



Now you may proceed to [logging on to {{ product_name }}](../How-to-Install-and-Run-the-Solution-all-configurations/#2_logging_on_to_smartcloud_connect) in MS Outlook for MacOS.

&nbsp;

* * *

### For an MS Exchange account

<iframe src="https://player.vimeo.com/video/384031982" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
&nbsp;

**1\.** Click the red **Office add-ins** icon in your MS Outlook for Mac's ribbon

**2\.** Enter your MS Exchange login credentials in the Exchange login window that opens in your web browser

**3\.** On the Add-In management page that will appear, click on the **+** (Add) button and then choose the source that you want to install {{ product_name }} from. For an MS Exchange mailbox, you can install the Add-In only from a manifest URL or file location. The installation link or the *.xml* manifest file is provided to the customers by [RevenueGrid.com Sales team](mailto:sales@revenuegrid.com)

**4\.** Select **Add from a URL** or **Add from a file**, then

- Enter the manifest's URL and click **Next** or  
- **Browse** your hard drive and select the downloaded .xml file and click **Next ** 

**5\.** Click **Install** to confirm add-in installation, then click **OK**

Now the {{ short_name }} Add-In has been added to your MS Outlook add-ins list and to your email account.  

You will see {{ product_name }} icons added to MS Outlook for Mac ribbon:

<p><img src="../../assets/images/Install-and-Run/MacOS/ribbon_icons.png" class="minimized">
</p>

In addition, corresponding controls are now added to your mail account opened in [Outlook on the Web](https://docs.microsoft.com/en-us/exchange/clients/outlook-on-the-web/outlook-on-the-web?view=exchserver-2019). See [this article](../Open-in-Outlook-Web/) for more information.

&nbsp;

!!! note "Note"
    The Add-In will now also be available for your mail account logged in on other compatible devices with MS Outlook running. This way, you won't need to install it additionally in your MS Outlook Mobile for iOS and Android, Outlook on the Web (<https://outlook.com>, <https://outlook.live.com/owa/>), or MS Outlook for Windows

&nbsp;


​    **1\.** Open {{ product_name }} by clicking the **Open {{ product_name }}** icon in MS Outlook ribbon

​    **2\.** In the Sidebar, select **Connect to Salesforce** or [another available login option](../How-to-Install-and-Run-the-Solution-all-configurations/#2_logging_on_to_smartcloud_connect). Note: make sure that your Safari browser [does not block pop-up windows](http://osxdaily.com/2019/02/05/how-allow-pop-up-windows-safari-mac/)

![](../assets/images/Install-and-Run/MacOS/logon.png)



​    **3\.** A [standard Salesforce Single Sign-On](https://help.salesforce.com/articleView?id=sso_about.htm&type=5) pop-up window will be opened. Enter your Salesforce login credentials and click **Log in** to authorize {{ short_name }} to work with your Salesforce data.
![](../assets/images/Install-and-Run/MacOS/sso.png)

&nbsp;

**4\.** On the following screen, activate [{{ company_name }} Sync](../Synchronization-Engine-An-Overview/) by entering your MS Exchange login credentials and clicking **Connect to Exchange**

!!! warning "Important"
    If you are using several different email boxes for your correspondence (not [aliases](https://support.office.com/en-us/article/add-or-remove-an-email-alias-in-outlook-com-459b1989-356d-40fa-a689-8f285b13f1f2)), make sure to authorize [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/) for the same email box as one for which you installed the [Add-In](../Introduction/), otherwise the [Sync engine functions](../AddIn-vs-Sync-Functions/) will work incorrectly even though {{ short_name }} Sync will appear to be running

&nbsp;

![](../assets/images/Install-and-Run/SyncAuth/new_dialog.png)

&nbsp;

In some configurations you may also need to enter a valid [Exchange Web Services link](https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/start-using-web-services-in-exchange) specific to your company's Exchange configuration. To do that, click the **More v** button and paste the EWS link provided by your local admin into the field. 



!!! warning "Important"
    Note that if Sync activation is skipped, a number of [key {{ product_name }} features](../AddIn-vs-Sync-Functions/) will be unavailable



&#160;
 &#160;


<style>
  .banners {
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .banners a.button {
      background-color: #FFC827;
      color: #2F3341;
      box-shadow: 0 5px 35px rgba(146, 146, 146, 0.2);
      padding: 20px;
      font-family: Graphic, arial;
      font-weight: 600;
      line-height: 24px;
      margin-top: -100px;
      border-radius: 3px;
      cursor: pointer;
      transition: .1s;
  }

  .banners a.button:hover {
    transform: scale(1.05);
  }

  .banners a.button a:hover,
  .banners a.button a:visited {
      color: #2F3341;
  }

  .banner-3 a.button {
    margin-left: 45%;
  }
</style>

<br>
<div class="banners banner-3">
  <img src="../../assets/images/banners/banner-3.svg" style="width: 100%; height: 100%;">
  <a class="button" href="https://revenuegrid.com/sign-up/?utm_source=kb_rg&utm_medium=referral&utm_campaign=eac&utm_content=banner" target="_blank">Try {{ company_name }} for free</a>
</div>