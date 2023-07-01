---
description: The procedure for mass-activating Salesforce access for multiple users
---
# How To Mass-Activate Salesforce Access for Multiple Users  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*3 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! tip "Tip"
    To use {{ product_name }} Admin panel, special access permissions are required. To request the permissions for your organization, [contact {{ company_name }} support team by email](mailto:support@revenuegrid.com). Admin panel provides tools for managing end users and some of its key settings it includes duplicate {{ product_name }} [Customization](../Customization-Settings-Explained/) and [Sync](../Configuring-Activities-Synchronization-Settings/) settings on Admin level

This article is an addition to the articles [Managing Organizations](../Managing-Organizations-via-the-Admin-Panel) and [Managing Users](../Managing-Users-via-the-Solution-s-Admin-Panel/).

The {{ short_company_name }} Sync Engine provides the possibility to perform bulk authorization of users [in Salesforce](../Authorizing-Sync-Engine-to-Work-with-Your-Data/). Combined with [mass Email access authorization via Exchange Impersonation](../Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/), it allows to exclude the necessity of any setup actions from the end users. In addition, if this option is used, no authorization prompts will pop up for the end users to refresh an expired access token.

To set up immediate out-of-the-box Salesforce connection for all {{ short_company_name }} users in your Org, use the new sub-tab **Salesforce Connectivity** of [{{ short_name }} Admin panel's Organizations tab](../Managing-Organizations-via-the-Admin-Panel/). A prerequisite for this feature is creation of either a service Salesforce account granted full data visibility in the Org or an API only user set up to authorize Salesforce access for multiple end users. Presently, the latter authentication option is unavailable.


!!! warning "Important"
    Mass-authorization of users in Salesforce with Salesforce Service Account is compatible only with {{ short_company_name }} Sync. It is not yet available for the Add-In mass-authorization.

!!! warning "Important"
    In March 2023 release, the new Admin Panel was introduced. The support of the legacy Admin Panel will be ceased soon, thus we strongly encourage that our customers switch to the new Admin Panel. This article contains two sections:  
    • [How to mass-authorize users in the new Admin Panel](#how_to_mass-authorize_users_in_the_new_admin_panel)  
    • [How to mass-authorize users in the legacy Admin Panel](#how_to_mass-authorize_users_in_the_legacy_admin_panel)

&nbsp;
* * *

&nbsp;

## How to mass-authorize users in the new Admin Panel

### Authorization using a service account with granted data visibility

Follow the below instruction to mass-authorize Salesforce access for the end users via the *Salesforce Connectivity* tab.

!!! warning "Important"
    The Salesforce account to be used for this feature should be a specially created service-only account, no active {{ short_name }} user account can be used for that

**1\.** Create a Salesforce user account with [granted data visibility](https://help.salesforce.com/articleView?id=category_visibility_whatis.htm&type=5) for all data in the Org (*"View all data"*) that will be accessed and managed by {{ short_name }} users in your company. If you intend to mass-authorize {{ short_name }} end users' access to [a Salesforce Sandbox environment](https://help.salesforce.com/articleView?id=data_sandbox_manage.htm&type=5), create a corresponding service user account in this environment. Note that you should **not** provision the account in {{ product_name }}, as it will only be used for Salesforce access authorization

&nbsp;

**2\.** [Open {{ short_company_name }} Admin panel](../How-to-Log-In-to-the-Admin-Panel/) > **Profiles** tab > **Connectivity** subtab

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Salesforce-Connectivity\set-up-sf-auth\sf-connectivity.png">
</p>

&nbsp;

**3\.** On the subtab, in the CRM block, click the **Log in with Salesforce** button

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Salesforce-Connectivity\set-up-sf-auth\log-in-with-sf.png"  style="width:60%">
</p>

&nbsp;
!!! note "Note"
    Presently, only the *Salesforce OAuth authorization* option is available; it implies that the pre-set service Salesforce account's [refresh token](https://help.salesforce.com/articleView?id=remoteaccess_oauth_refresh_token_flow.htm&type=5) will be used to authorize access for a specified group of {{ short_name }} end users

&nbsp;

**4\.**  Log in to the pre-set service account via a [standard Salesforce OAuth window](https://help.salesforce.com/articleView?id=remoteaccess_authenticate_overview.htm) that will be opened in your browser 

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Salesforce-Connectivity\set-up-sf-auth\sf-auth.png"  style="width:60%">
</p> 

&nbsp;

**5\.** If authorization was successful, you will see that the Salesforce service account status changed to *Connected*
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Salesforce-Connectivity\set-up-sf-auth\sf-connected.png"  style="width:60%">
</p> 

&nbsp;

* * *

&nbsp;

#### Re-establishing connection after refresh token expiration

If the service account's refresh token expires, which results in the entitled end users' [{{ short_company_name }} Sync](../Synchronization-Engine-An-Overview/) being [suspended](../Handling-Sync-Issues/), the local {{ short_company_name }} Admin sees a status change to *Disconnected* in the CRM block on the Connectivity tab


&nbsp;

!!! tip "Tip"
    Users' sync status/Salesforce connection can also be monitored via the [Users](../Managing-Users-via-the-Solution-s-Admin-Panel/) sub-tab of Admin panel's Profiles tab. Specifically, the Synchronization status of the users whose synchronization changes to the *Disabled* status; if clicking on such user brings up a notification "*invalid_grant: expired access/refresh token*", that means the user's access token requires refreshing

&nbsp;

To get a new refresh token and reestablish Salesforce connection:

**1\.** Open the *Connectivity* subtab of the Profile tab in the {{ short_company_name }} Admin panel  

**2\.** Click **Refresh** in the CRM block

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Salesforce-Connectivity\set-up-sf-auth\sf-refresh.png" style="width:60%">
</p> 

&nbsp;

**3\.** Log in to the pre-set service account afresh via a [standard Salesforce OAuth window](https://help.salesforce.com/articleView?id=remoteaccess_authenticate_overview.htm) that will be opened in your browser 

Now {{ short_company_name }} users' Salesforce connection will be recovered.

<br>
<hr>
<br>

## How to mass-authorize users in the legacy Admin Panel


<iframe src="https://player.vimeo.com/video/461379352" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>

&nbsp;

### Authorization using a service account with granted data visibility

Follow the below instruction to mass-authorize Salesforce access for the end users via the *Salesforce Connectivity* tab.

!!! warning "Important"
    The Salesforce account to be used for this feature should be a specially created service-only account, no active {{ short_name }} user account can be used for that

**1\.** Create a Salesforce user account with [granted data visibility](https://help.salesforce.com/articleView?id=category_visibility_whatis.htm&type=5) for all data in the Org (*"View all data"*) that will be accessed and managed by {{ short_name }} users in your company. If you intend to mass-authorize {{ short_name }} end users' access to [a Salesforce Sandbox environment](https://help.salesforce.com/articleView?id=data_sandbox_manage.htm&type=5), create a corresponding service user account in this environment. Note that you should **not** provision the account in {{ product_name }}, as it will only be used for Salesforce access authorization

**2\.** [Open {{ short_name }} Admin panel](../How-to-Log-In-to-the-Admin-Panel/) > **Organizations** tab > **Salesforce Connectivity** sub-tab

&nbsp;

**3\.** On the sub-tab, toggle the switch button **Login using Salesforce Service Account** to *Enabled*


<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Salesforce-Connectivity\default-disabled.jpg" class="minimized">
</p>

&nbsp;

**4\.** Presently, only the *Salesforce OAuth authorization* option is available; it implies that the pre-set service Salesforce account's [refresh token](https://help.salesforce.com/articleView?id=remoteaccess_oauth_refresh_token_flow.htm&type=5) will be used to authorize access for a specified group of {{ short_name }} end users

 **5\.** Next, click *Connect to Salesforce* (regular Salesforce Org authorization) or *Connect to Salesforce Sandbox* ([Salesforce Sandbox environment](https://help.salesforce.com/articleView?id=deploy_sandboxes_intro.htm&type=5) authorization) to proceed 

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Salesforce-Connectivity\select-sandbox.jpg" class="minimized">
</p>

&nbsp;

**6\.**  Log in to the pre-set service account via a [standard Salesforce OAuth window](https://help.salesforce.com/articleView?id=remoteaccess_authenticate_overview.htm) that will be opened in your browser 

<p><img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5b6b07ba2c7d3a03f89d7a23.png">
</p> 

&nbsp;

**7\.** If authorization was successful, you will see *Salesforce connection status: Salesforce connection established successfully* and the service account's user ID

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Salesforce-Connectivity\setup-account.jpg" class="minimized">
</p> 

&nbsp;

* * *

&nbsp;

#### Re-establishing connection after refresh token expiration

If the service account's refresh token expires, which results in the entitled end users' [{{ short_name }} Sync](../Synchronization-Engine-An-Overview/) being [suspended](../Handling-Sync-Issues/), the local {{ product_name }} Admin gets a corresponding notification in the Salesforce Connectivity tab

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Salesforce-Connectivity\connectivity_lost.jpg" class="minimized">
</p> 

&nbsp;

!!! tip "Tip"
    Users' sync status/Salesforce connection can also be monitored via the [Users](../Managing-Users-via-the-Solution-s-Admin-Panel/) sub-tab of Admin panel's Organizations tab. Specifically, the users whose synchronization is suspended are marked with red color; if clicking on such user brings up a notification "*invalid_grant: expired access/refresh token*", that means the user's access token requires refreshing

&nbsp;

To get a new refresh token and re-establish Salesforce connection:

**1\.** Open the *Salesforce Connectivity* tab of {{ short_name }} Admin panel  

**2\.** Click **Yes** in the "*Salesforce connectivity was lost ...*" dialog

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Salesforce-Connectivity\dialog-yes.jpg">
</p> 

&nbsp;

**3\.** Log in to the pre-set service account afresh via a [standard Salesforce OAuth window](https://help.salesforce.com/articleView?id=remoteaccess_authenticate_overview.htm) that will be opened in your browser 

Now {{ short_name }} users' Salesforce connection will be recovered.



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
      margin-top: -80px;
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
<div class="banners banner-1">
  <img src="../../assets/images/banners/banner-1.svg" style="width: 100%; height: 100%;">
  <a class="button" href="https://revenuegrid.com/sign-up/?utm_source=kb_rg&utm_medium=referral&utm_campaign=eac&utm_content=banner" target="_blank">Sign up for a free trial</a>
</div>