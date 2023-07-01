---
description: Learn how to configure and use a Gmail / Google Workspace (G Suite) Service Account for sync activation
---
# How to Configure and Use a Gmail / Google Workspace (G Suite) Service Account for Sync Activation  
  

<!--<i>For users of the Email Sidebar on:</i><br><br>-->
<!--<div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> -->

&nbsp;

*6 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

Gmail / Google Workspace (G Suite) Service Accounts are used for various mail access management tasks, for example to mass-authorize {{ product_name }} [Sync engine](../Synchronization-Engine-An-Overview/) to work with the end users' Gmail data via [{{ short_name }} Chrome Extension for Gmail](../Gmail-Extension/).

Within this scenario, a service account configured by the local mail Admin provides a simple way to authorize multiple Gmail boxes for {{ short_name }} use, so the end users do not need to [get their mailboxes authorized manually](../How-to-Set-Up-the-Chrome-Extension-for-Salesforce-and-Gmail/), and keep it connected every time they change  their password. This makes [adding new product users](../Managing-Users-via-the-Solution-s-Admin-Panel/) easier and allows admins and Managers to ensure that all users [get all {{ product_name }} features unrolled](../Email-Integration-Full-Deployment-Scenarios/) for them.

The steps to configure Gmail / Google Workspace (G Suite) Service Account:  

* [Step 1. Create a Project](../Gmail-Service-Account/#step_1_create_a_project)  

* [Step 2. Enable Gmail API Sets](../Gmail-Service-Account/#step_2_enable_gmail_api_sets)  

* [Step 3. Create a Service Account User](../Gmail-Service-Account/#step_3_create_a_service_account_user)  

* [Step 4. Configure Google Workspace Marketspace OAuth client](../Gmail-Service-Account/#step_4_configure_google_workspace_marketspace_oauth_client)  

* [Step 5. Enable the Service Account in Gmail](../Gmail-Service-Account/#step_5_enable_the_service_account_in_gmail)  

* [Step 6. Set Up Domain Delegation](../Gmail-Service-Account/#step_6_set_up_domain_delegation)  

* [Step 7. Use the configured service account to authorize users in {{ short_name }} Admin panel](../Gmail-Service-Account/#step_7_use_the_configured_service_account_to_authorize_users_in_rges_admin_panel)

!!! tip "Tip"
    After mass {{ short_name }} Sync activation via a Gmail service account, you can proceed to [mass-deploying the {{ short_name }} Chrome extensions for the end users](../Chrome-Extension-Mass-Deployment/); the mass deployment procedure is only available on Windows systems, via [MS Active Directory](https://searchwindowsserver.techtarget.com/definition/Active-Directory)

&nbsp;


<!--<iframe src="https://player.vimeo.com/video/458080336" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>-->

&nbsp;
***
&nbsp;

## Step 1. Create a Project

**1\.1.** Log in to your Org's Gmail / Google Workspace (G Suite) Console with a Super administrator credentials at <https://console.developers.google.com/>  

If you haven't used the Console before, you will first need to agree to the Console's Terms of Service.

<br>
**1\.2.** Click the button **Select a project ▾** in the upper left corner of the Console

![](../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/g0.png)

&nbsp;
<br><br>
**1\.3.** In the dialog that appears, click **New Project** 

![](../assets/images/Configuration-%26-Settings/Admin-Settings-%26-Actions/Gmail-Service-Account/g1.png)
 &nbsp;
<br><br>
**1\.4.** Enter a Project name and click **Create**. In this example we set the name *Gmail Service Account*

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/g2.png" style="width: 80%">
</p>


&nbsp;

&nbsp;
***
&nbsp;


## Step 2. Enable [Gmail API Sets](https://developers.google.com/gmail/api)

<br>
**2\.1.** Select your Project from the list and click the **ENABLE APIS AND SERVICES** button

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/g3.png" class="minimized">
</p>

<br><br>

 **2\.2.** On the API Library page that opens, use the search box to find **GMAIL API**, click on it and then **Enable** it on the next page.  
 
Note that enabling the APIs here does **not** instantly grant the access, it is a prerequisite to add the corresponding permission scopes later  

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/g4.gif" class="minimized">
</p>


&nbsp;


**2\.3.** In the same manner find and enable four more [API sets](https://developers.google.com/gmail/api) for the service account:   

* **Google Calendar API**
* **Google People API**
* **Google Drive API**
* **Tasks API**

&nbsp;

&nbsp;
***
&nbsp;

## Step 3. Create a Service Account User

<br>
**3\.1.** Click the **☰** (Navigation menu) icon (1) in the upper left corner of the Console and select **IAM & admin**(2) > **Service accounts**(3) in the navigation pane

![](../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/g6.png)

<br><br>

**3\.2.** In the next dialog, click **+ CREATE SERVICE ACCOUNT**

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/g7.png" class="minimized">
</p>

&nbsp;
<br><br>
**3\.3.** Enter a name to identify the service account and fill in the **Service account description** field, then click **CREATE**

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/g8.png" style="width: 70%">
</p>

&nbsp;
<br>
**3\.4.** In the next section, set the value **Project** > **Owner** in the field *Select a role* and click **Continue** 

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/g9.gif"  style="width:70%" class="minimized">
</p>

&nbsp;

**3\.5.** Then click **DONE** in the next section

&nbsp;
<br>
 **3\.6.** The next step, click the **⁝** (Menu) icon in the *Actions* column of the created service account and select **Manage keys**

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/g10.png" class="minimized">
</p>

<br><br>
**3\.7.** On the newly opened page, click **ADD KEY** and select **Create new key** from the drop-down list

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/g10-1.png" class="minimized">
</p>


<br><br>
**3\.8.** Select JSON format for the key (the default one) and click **CREATE**  

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/g11.png" style="width:70%" class="minimized">
</p>


<br><br>
**3\.9.** The JSON file will be automatically downloaded to your hard drive; store the Key file securely, as it unlocks access to your Gmail resources. This file will be used at a later step. Close the download notification and proceed to the next step

![](../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/g12.png)

&nbsp;

&nbsp;
***
&nbsp;


## Step 4. Configure Google Workspace Marketspace OAuth client

<br>
**4\.1.** On the same page, switch to the **DETAILS** tab

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/g14.png">
</p>

&nbsp;

**4\.2.** On the Details tab, scroll down to the **Advanced settings** subsection. Expand the section. Then copy the *Client ID* of the created service account to a text file or the clipboard to be used later

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/g4-2.png" style="width:80%">
</p>

&nbsp;
<br><br>
**4\.3.** Scroll down to find the section **Google Workspace Marketspace OAuth client** and click **Configure**  

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/g4-3.png" style="width:80%">
</p>
&nbsp;
<br><br>
**4\.4.** On the OAuth consent screen page, select the **Internal** user type and click **Create**  

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/g4-4.png" style="width:90%">
</p>
&nbsp;
<br><br>
**4\.5.** On the next page, edit the app registration information:

<p style="margin-left:5%">
<b>4.5.1.</b> Fill in the app information to be showed on the consent screen:
<ul style="margin-left:10%">
<li> Enter <b>{{ company_name }}</b> in the <i>App Name</i> field </li>
<li> Enter <b>your organization's user support email</b> in the <i>User support email</i> field</li>
</ul>
</p>
<p style="margin-left:10%"><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/g4-5-1.png" style="width:80%">
</p>

<br><br>
<p style="margin-left:5%">
<b>4.5.2.</b> Under Authorised domains, 
<ul style="margin-left:10%">
<li> Click <b>ADD DOMAIN</b></li>
<li> Enter the authorized domain address provided by <a href="mailto:support@revenuegrid.com"> {{ company_name }} Support team</a> in the <i>Authorized domain 1</i> field and click <b>Add Domain</b></li>
</ul>
</p>
<p style="margin-left:10%"><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/g4-5-2.png" style="width:80%">
</p>

<br>
<p style="margin-left:5%">  
<br><br>
<b>4.5.3.</b> Under Developer contact information, enter the email address of <b>your organization’s admin</b> 
<p style="margin-left:10%"><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/g4-5-3.png" style="width:80%">
</p>

<br><br>
<b>4.5.4.</b> Click <b>Save and Continue</b> 
</p>

<br>
**4\.6.** On the next page, click **Add or Remove Scopes**  

<br>
**4\.7.** In the section *"Manually add scopes"*, add the following coma-separated scopes in the scopes field: 
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
When done, click **Add to Table** and **UPDATE**

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/g4-7.gif" style="width:80%">
</p>

<br>
**4\.8.** Click **Save and Continue** to proceed 

<br>
**4\.9.** On the next page, review the information you have entered and click **Back to Dashboard**


&nbsp;

&nbsp;
***
&nbsp;

## Step 5. Enable the Service Account in Gmail

<br>
**5\.1.** Log in to the [Google Workspace Admin Console](https://admin.google.com/?hl=en_US)


<br>
 **5\.2.** On the right hand side navigation panel, click **Security**


<br>
**5\.3.** Find **Access and data control** and click **API controls** 


<br>
**5\.4.** On the *API Controls* page that opens, click **MANAGE THIRD-PARTY APP ACCESS**

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/g21.png" class="minimized">
</p>

&nbsp;

**5\.5.** In the "App access control" window that opens, click **Configure new app** and select **OAuth App Name Or Client ID** on the picklist

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/g22.png" class="minimized">
</p>

&nbsp;

**5\.6.** Now you need to find the OAuth app to connect it. Enter the **Client ID**, a digits only line that you copied in the Step **4.2** into the *Search for app name or client ID* field and click **SEARCH**

!!! tip "Tip"
    If you didn't copy the Client ID, it can be retrieved in the following way: click **☰** (Menu) in the upper left corner of the Console window. Then select **IAM & admin** and click **Service accounts**. Once there, find the service account and click **Edit** in the Actions column menu, then copy the contents of the *Client ID* field from the account parameters page

&nbsp;

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/g20.png" class="minimized">
</p>

&nbsp;

**5\.7.** If everything was configured correctly, you will see *{{ company_name }}* (or another app name that you entered) in the results. Click **SELECT** on the right hand side

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/g24.png" class="minimized">
</p>

&nbsp;

**5\.8.** The next step: select the checkbox next to the Client ID, then click **SELECT** in the bottom right corner of the dialog

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/g25.png" class="minimized">
</p>

&nbsp;

**5\.9.** In the next dialog, set App access to **Trusted: Can access all Google services** and click **CONFIGURE**

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/g26.png" class="minimized">
</p>

&nbsp;

**5\.10.** Next, you will see the list of configured API apps, including *{{ company_name }}* (or another app name you specified).

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/g27.png" class="minimized">
</p>

&nbsp;

&nbsp;
***
&nbsp;

## Step 6. Set Up Domain Delegation

<br>
**6\.1.** Go back to Gmail Admin Console's **Security** tab (see the step **5\.2.**), then go to **Access and data control** > **API controls**


&nbsp;

**6\.2.** Click **MANAGE DOMAIN-WIDE DELEGATION** at the bottom of the page  

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/g29.png" class="minimized">
</p>

&nbsp;

**6\.3.** In the pane "Domain-wide delegation", click **Add new** API client

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/g30.png" class="minimized">
</p>

&nbsp;

**6\.4.** In the dialog "Add a new client ID" that appears:

- enter the Client ID that you copied in the step **4.2**
- populate the *OAuth scopes* field with the following comma-separated values:
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


&nbsp;

- Click **AUTHORISE**



&nbsp;

**6\.3.** Hold up for 5 minutes for the configuration to be applied

Now you are all set up to use the Gmail Service Account for end users authorization.

&nbsp;

&nbsp;
***
&nbsp;

## Step 7. Use the configured service account to authorize users in [{{ short_name }} Admin panel](../How-to-Log-In-to-the-Admin-Panel/)

<br>
After you create a Gmail Service Account you must authorize the users in {{ product_name }} Admin panel.

To do that:  

**7.1\.** [Login to the Admin panel](../How-to-Log-In-to-the-Admin-Panel/) with admin credentials provided by {{ short_name }} Support team  


**7.2\.** Click on the [**ORGANIZATIONS** tab](../Managing-Organizations-via-the-Admin-Panel/) and select your Org  


**7.3\.** Open the **E-MAIL CONFIGURATION** subtab  

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/gmail-org.png" class="minimized">
</p>

&nbsp;


**7.4\.** Click **Choose File** next to *Upload JSON file*, select the Private key .json file you generated at point ( **3.8** ) of the above instruction, then click **Upload**   


**7.5\.** Click **Save** in the upper right corner of the subtab and then click **Check Users' Google Impersonated Access** to make sure that the procedure was successful   

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Gmail-Service-Account/check-save.png" class="minimized">
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
<div class="banners banner-2">
  <img src="../../assets/images/banners/banner-2.svg" style="width: 100%; height: 100%;">
  <a class="button" href="https://revenuegrid.com/request-demo/?utm_source=kb_rg&utm_medium=referral&utm_campaign=eac_demo&utm_content=banner" target="_blank">Book a free demo</a>
</div>
<br>
