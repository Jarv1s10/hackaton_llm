# How to Set Up SAP Cloud for Customer Server-Side Integration for Gmail


<span style="color: #e74125;font-size: 17px;font-weight: 700;line-height: 30px;padding: 0px 10px;outline: none;border-radius: 0px;text-decoration: none;background-color: #fff;display: inline-block;border: 0px solid #000;transition: .3s all;width: auto;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="display: inline-block;vertical-align: middle;height: 32px;object-fit: contain;"></span>

&nbsp;

&nbsp;

**[ This article is work-in-progress ]**

&nbsp;

&nbsp;

!!! tip "Tip"
    Also, refer to this [SAP Help Portal article](https://help.sap.com/docs/SAP_CLOUD_FOR_CUSTOMER/24765b551a014b779b95c7b07d8e9079/4119370ae02549b1ba80c6af7149d84c.html) on setting up SSI for Gmail for more information
    
&nbsp;

The setup of SAP Cloud for Customer for Gmail requires several preliminary actions on the SAP Cloud for Customer side, including [user provisioning](#user_provisioning_in_sap_cloud_for_customer) and [SSI Sync enabling](#enabling_ssi_synchronization_for_the_user). They are necessary to ensure the correct configuration of the SSI Google Chrome extension. 

&nbsp;

&nbsp;

## User provisioning in SAP Cloud for Customer

Key User must provision the SAP Cloud for Customer end users configured for "Google Direct Logon" to provide them with access to SAP Cloud for Customer SSI for Gmail.

In order to provision end users, follow the steps documented in [this article, section 2.4 User Provisioning](../How-to-Configure-Admin/#24_user_provisioning).

&nbsp;

* * * 

&nbsp;

## Enabling SSI synchronization for the user

!!! warning "Important"
    Enabling SSI synchronization is crucial to allow users to log in to the SAP Google Chrome extension. If SSI sync remains disabled, the user login will fail

In order to enable SSI synchronization for particular user, follow the steps documented in [this article](../How-to-Configure-User/).

&nbsp;

* * * 

&nbsp;

## SSI Google Chrome extension setup

### 1. Add the SAP Cloud for Customer for Gmail extension to your Google Chrome

To add the SAP Cloud for Customer for Gmail extension to your Chrome or Chromium-based browser:

**1.1.** In the Google Chrome browser, open this [Chrome Web Store link](https://chrome.google.com/webstore/detail/sap-cloud-for-customer-fo/dpolpgcoaadhofccfkjdknifhofinflb)


<details><summary>>>> Click to see a screenshot <<<</summary>
<img src="../../assets/images/set-up-for-gmail/1.png">
</details>

&nbsp;

**1.2.** Click the button **Add to Chrome**, then click **Add extension** in the confirmation dialog that will appear

<img src="../../assets/images/set-up-for-gmail/2.png">

&nbsp;

* * *

&nbsp;

<!--This step is no longer needed by design-->
<!--
### 2. Specify the SAP Cloud for Customer tenant for the SSI Google Chrome extension

!!! note "Note"
    This is an important step to link your **provisioned user** with **SAP Cloud for Customer tenant** through the SSI Google Chrome extension

&nbsp;

To specify the SAP Cloud for Customer tenant for the added SSI Google Chrome extension:

<img src="../../assets/images/set-up-for-gmail/3.png" style="width:50%;float:right;margin-left:2%;"/>

**2.1.** Go to the SAP Cloud for Customer home page and copy the tenant value from the URL bar. In this case, the value for the tenant is *https://my308305.vlab.sapbydesign.com/*

&nbsp;

!!! warning "Important"
    **Do not** forget to include **https://** while you copy the URL from the URL bar

&nbsp;

**2.2.** In the Chrome browser, click the **'Puzzle' icon** (1) in the upper right corner, then click **SAP Cloud for Customer for Gmail** (2) in the opened dialog

<img src="../../assets/images/set-up-for-gmail/4.png">

&nbsp;

**2.3.** In the extension's dialog, enter the copied SAP Cloud for Customer tenant and click **Apply**

<img src="../../assets/images/set-up-for-gmail/5.png">

&nbsp;

* * *

&nbsp;
-->
### 2. Sign in to Gmail and grant SSI access to work with your Gmail and Google Calendar data

!!! note "Note"
    Handling of your e-mail/calendar and CRM data by SSI Chrome Extension for Gmail is based on the same [set of Privacy and Security principles](../Privacy-and-Security/) as SSI Add-In for MS Outlook Desktop or On the Web version

&nbsp;

To grant SSI access to interact with your Google account, do the following:

**2.1.** After signing in to Gmail, open the SSI Extension by clicking the SAP Cloud for Customer icon (1) in the pane on the right-hand side

**2.2.** In the extension's pane, click **Grant access to my Google account** (2)

<img src="../../assets/images/set-up-for-gmail/6.png">

&nbsp;

**2.3.** The *Choose an account* dialog will appear, select your account in it

<img src="../../assets/images/set-up-for-gmail/7.png">

&nbsp;

Next, you will see the *Logon was successful* window.

From now the setup of SAP Cloud for Customer for Gmail is finished, and the SSI Google Chrome extension is ready for use.

&nbsp;

* * *

&nbsp;

## How to remove the extension from Chrome

Refer to this [Google Chrome Support instruction](https://support.google.com/chromebook/answer/2589434?hl=en) to learn how to remove the extension from your Chrome browser.

&nbsp;

&nbsp;