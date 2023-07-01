---
description: How to implement the mass provisioning scenario of the RGES Chrome Extension for Gmail Users
---
# Mass Provisioning of the Chrome Extension for Gmail Users  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

Customers of [{{ product_name }} for Salesforce and Gmail](../Using-the-Solution-for-Salesforce-and-Gmail/) can make use of this mass provisioning scenario and [the mass deployment scenario for Windows systems](../Chrome-Extension-Mass-Deployment/) (via Active directory) to set up the Solution for all end users in an Org.

These scenarios are typically performed by the local email/mail server Administrator. If the company prefers not to grant Gmail / Google Workspace (G Suite) data access to {{ product_name }} for each individual end user's mailbox due to security policies or the end users being too many.

!!! note "Note"
    Handling of your email/calendar and CRM data by {{ product_name }} Chrome Extension for Gmail is based on the same [set of Privacy and Security principles](../Privacy-and-Security/) as {{ product_name }} Add-In for MS Outlook Desktop or On the Web version

After the {{ product_name }} Chrome Extension has been installed in the end users' Chrome browsers either [individually](../How-to-Set-Up-the-Chrome-Extension-for-Salesforce-and-Gmail/) or [in bulk by the Admin](../Chrome-Extension-Mass-Deployment/), follow the below steps to configure and use a Gmail / Google Workspace (G Suite) Service account to mass-configure {{ short_name }} for the end users.

**1\.** You should prepare an in-org Gmail / Google Workspace (G Suite) account which will be used <u>only</u> for providing Gmail data access for {{ short_name }} end users

**2\.** Configure this account as a Service account. Follow [the Google guide 1](https://support.google.com/a/answer/7378726?hl=en) or instructions in [this {{ short_company_name }} help article](../Gmail-Service-Account/) to create a Gmail service account or [guide 2](https://support.google.com/gsuitemigrate/answer/9222993?hl=en) to create a Google Workspace (G Suite) service account via Google console

**3\.** Follow [this Google guide](https://support.google.com/gsuitemigrate/answer/9226376?hl=en) to authorize the service account to access other accounts' data

The scopes required for the service account on *Step 4* for the above mentioned Google guide:

```
https://www.googleapis.com/auth/gmail.readonly,  
https://www.google.com/m8/feeds/,  
https://www.googleapis.com/auth/calendar,  
https://www.googleapis.com/auth/drive,  
https://www.googleapis.com/auth/drive.appdata,  
https://www.googleapis.com/auth/gmail.labels,  
https://www.googleapis.com/auth/gmail.modify,  
https://www.googleapis.com/auth/tasks,  
https://www.googleapis.com/auth/userinfo.email,  
https://www.googleapis.com/auth/gmail.compose,  
https://www.googleapis.com/auth/contacts,  
https://www.googleapis.com/auth/userinfo.profile
```
<br>
!!! note "Note"
    The scope "https://www.googleapis.com/auth/drive" is optional, if [*DisableDriveAttachments* is enabled](../Special-Admin-Panel-Settings/#extra_configuration_settings).  


&nbsp;

**4\.** Next [Log in to {{ product_name }} Admin panel](../How-to-Log-In-to-the-Admin-Panel/) with Admin credentials provided by RevenueGrid.com

**5\.** On the **Organizations** tab, select the Organization which the end users belong to; see the articles on [managing organizations](../Managing-Organizations-via-the-Admin-Panel/) and [managing users](../Managing-Users-via-the-Solution-s-Admin-Panel/) in {{ short_name }} Admin panel

**6\.** Select the **E-mail configuration** subtab for this organization and pick **Google Service Account** in the **Mailbox Access Type** box

**7\.** An *Upload JSON file* line will appear; click the button **Upload file** next to it, browse your hard drive and select the [JSON Web Token file](https://flaviocopes.com/jwt/) which was generated on Step 2 of this guide

**8\.** Now, if everything was configured correctly, you will see the *Project ID* and *Client ID* of your service account and its *Connection status*





&#160;
 &#160;



