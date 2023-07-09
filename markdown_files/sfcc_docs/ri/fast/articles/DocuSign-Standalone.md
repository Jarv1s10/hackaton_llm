---
description: How to work with DocuSign Sidebar from your MS Outlook interface
---
# How To Configure and Use DocuSign Sidebar  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

*[The article is work-in-progress]*

&nbsp;

&nbsp;

&nbsp;

<iframe src="https://player.vimeo.com/video/266275462" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>

&nbsp;

The DocuSign (formerly SpringCM) stand-alone App is a custom solution implemented by {{ company_name }} for several customers.

The App is an MS Outlook add-in similar to [{{ company_name }} Add-In](../Introduction/) that includes a Sidebar pane integrated into MS Outlook interface. It allows the end users to instantly save or retrieve files attached to emails or calendar items to/from their corporate DocuSign account.

&nbsp;

### Firewall whitelisting prerequisite

To enable {{ product_name }} Add-In to work with DocuSign storage, your local mail server Administrator should allow-list the following IPs for inbound and outbound connection in the corporate firewall.

!!! tip "Tip"
    Check out the description of a typical whitelisting procedure for the standard Windows 10 firewall [here](https://www.howtogeek.com/112564/how-to-create-advanced-firewall-rules-in-the-windows-firewall/)

&nbsp;

```
104.44.128.14
104.44.128.15
104.44.128.16
104.44.128.17
65.52.33.205
104.210.148.43
13.84.129.10
13.84.55.90
104.214.118.162
104.44.128.13
104.214.20.1
```

&nbsp;

&nbsp;

### Logging in with [DocuSign SSO](https://community.springcm.com/s/article/Single-Sign-On-SSO-1657199242)

After the DocuSign stand-alone App has been installed for you by your local Admin or {{ company_name }} CSM team, you will see its Sidebar on the left-hand side of your MS Outlook interface. To start using the app, you need to log in to it via DocuSign SSO system by entering your DocuSign login credentials.

[Single Sign-On (SSO) Authorization](https://community.springcm.com/s/article/Authorizing-SpringCM-Desktop-and-Mobile-Applications-728746621) is used when you access DocuSign from an identify provider configured by your account Administrator. In this case, the user is accessing a centralized authentication server that all other applications and systems use.
The  following are requirements for using the Single Sign-on as the  authorization method. If these conditions are not met, then when the  user selects Authorize, they will be prompted to log in to DocuSign as  if Standard Authorization was selected.

- The account must be configured in DocuSign for SSO
- The account ID must be provided to the users as they setup their application
- The user's default account must be setup for SSO

&nbsp;

To log in with SSO:

1. Open the Sidebar and click **Log In**

![](../assets/images/Configuration-&-Settings/User-Settings/SpringCM-Integration/login-step-01.png)

&nbsp;

2. Select **Log in with SSO**

![](../assets/images/Configuration-&-Settings/User-Settings/SpringCM-Integration/login-step-02.png)

&nbsp;

3. Enter your **Account ID** and click **Log In**. The Account ID is provided by your local DocuSign Admin

![](../assets/images/Configuration-&-Settings/User-Settings/SpringCM-Integration/login-step-03.png)

&nbsp;

&nbsp;



