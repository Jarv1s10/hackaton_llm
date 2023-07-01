---
description: Step-by-step access authorization troubleshooting guide for Salesforce OAuth error
---
# Access Authorization Troubleshooting: Salesforce OAuth error  
  

*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

The essence of the issue: after clicking on the "Connect to Salesforce" button to run {{ short_name }} Add-In a Salesforce OAuth error *OAUTH_APPROVAL_ERROR_GENERIC* occurs:

<p>
    <img src="../../assets/images/Using-SmartCloud-Connect/How-To-s/Troubleshooting/SF-OAuth-Error.png">
</p>

&nbsp;

It only happens if [API use](https://help.salesforce.com/s/articleView?id=sf.security_api_access_control_about.htm&type=5) is enabled for the user in Salesforce.

&nbsp;

&nbsp;

The issue's cause: the *OAUTH_APPROVAL_ERROR_GENERIC* error may occur on user logon if the user's Profile in Salesforce is restricted by IP range limits. That also blocks any connections from [Connected Apps](https://help.salesforce.com/s/articleView?id=sf.connected_app_overview.htm&type=5).

&nbsp;

To resolve the issue, first adjust Salesforce restricted IPs configuration for the concerned Profile, to ensure that the range includes the actual IP the user attempts a logon from, e.g. one outside of the corporate network:  

**1\.** [Open Salesforce **Setup**](https://help.salesforce.com/s/articleView?id=sf.basics_nav_setup.htm&type=5), type *Profiles* in the Quick Find box and select **Profiles**  
**2\.** Expand relevant Profile's settings by clicking on its name  
**3\.** On the Profile settings page, click **Login IP Ranges** to check and adjust the restrictions  

&nbsp;

If that does not help, also try changing Connected Apps restrictions to Relaxed:

By default, *IP Relaxation* is set to "Enforce IP restrictions" for any Connected Apps, this prevents {{ short_name }} usage from unexpected IPs. To set "Relax IP restrictions":

**1\.** [Open Salesforce **Setup**](https://help.salesforce.com/s/articleView?id=sf.basics_nav_setup.htm&type=5), type *connected apps* in the Quick Find box and select **Manage Connected Apps**  
**2\.** Select **{{ company_name }} for Salesforce** and click **Edit** in the Action column  
**3\.**  In the *IP Relaxation* field, select **Relax IP restrictions**  

<p>
    <img src="../../assets/images/Using-SmartCloud-Connect/How-To-s/Troubleshooting/Relax-IP.png">
</p>

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