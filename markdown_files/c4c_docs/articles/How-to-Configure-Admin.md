# Deployment and Configuring SAP Cloud for Customer Server-Side Integration by Admin

&nbsp;

!!! tip "Tip"
    Also refer to [this SAP Help Portal article](https://help.sap.com/docs/SAP_CLOUD_FOR_CUSTOMER/24765b551a014b779b95c7b07d8e9079/da012ebc244e420984cc26150b52c95e.html) and [this SAP blog entry](https://blogs.sap.com/2018/04/19/c4c-server-side-integration-with-microsoft-outlook/) for relevant Admin level instructions

!!! warning "Important"
    Please note that if you mass-deploy SAP Cloud for Customer SSI for the end users without making use of [*MS Exchange Impersonated access*](../Configure-Impersonation/), additional setup actions will also be required on the user side. To address that, spread [this article](../How-to-Configure-User/) among the end users

&nbsp;

&nbsp;

## 1\. Deployment considerations

SAP Cloud for Customer SSI Server-Side Integration can be mass-deployed for the end users following one of the two main scenarios, depending on the Microsoft Exchange authentication type setting:

&nbsp;&nbsp;&nbsp;&nbsp;**1.1** Authentication based on [Microsoft Exchange Impersonation](https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange) is a scenario where the local Exchange Admin configures an [impersonating service account](../Configure-Impersonation/) for a specific organization (group of users) entitled to use SAP Cloud for Customer SSI, and then this impersonating account is used to authorize SSI Sync access to their data. This is the recommended approach, since it doesn't require any actions from the end users to complete tool deployment  

&nbsp;&nbsp;&nbsp;&nbsp;**1.2** Authentication based on Microsoft Exchange Direct Logon (or Office 365 Oauth, or Google Direct Logon) is a scenario where general deployment is carried out by the local Admin, by setting up SAP Cloud for Customer SSI Add-In, but after that the users must log in to the Add-In and [enter their Microsoft Exchange/Office 365/Google credentials in its settings](../How-to-Configure-User/). This approach is less recommended and can be applied for smaller groups of users, since it requires additional actions from the end users to complete tool deployment

&nbsp;

* * *

&nbsp;

## 2\. Admin deployment actions

### &nbsp; &nbsp; &nbsp; &nbsp;2.1 Prerequisites

Before starting SAP Cloud for Customer SSI deployment, the Admin must decide what mail server access authentication type will be used, [*Microsoft Exchange Impersonation*](https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange) or *Microsoft Exchange Direct Logon* for MS Exchange, or *Office 365 OAuth* for Office 365, or *Google Direct Logon* for Gmail.

If *Microsoft Exchange Impersonation* (see point **1.1** above) is to be used, first an [impersonating service account must be configured](../Configure-Impersonation/) by the local MS Exchange admin for a group of end users' e-mail accounts entitled to use the tool. After that, proceed to the steps below.

If *Microsoft Exchange Direct Logon* (see point **1.2** above) is to be used, you may proceed directly to the steps below.  

&nbsp;

&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;**2.1.1** Log in to SAP Cloud for Customer SSI using Admin account (Key User) credentials

&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;**2.1.2** Go to **E-Mail Integration** (1) > **Groupware Settings** (2) page. Note that it is available exclusively for the local SAP Cloud for Customer Admin; regular users can access only the *User Settings*

<!-- Do regular users not have access to Groupware Settings? -->

![](..\assets\images\Admin\1.png)

&nbsp;

* * *

&nbsp;

### &nbsp; &nbsp; &nbsp; &nbsp;2.2 Configuring user Profile settings

!!! tip "Tip"
    Also refer to [this article](../How-to-Open-Your-C4C-SSI-Settings-Profile/) for detailed information on SAP Cloud for Customer SSI Profiles configuration

A SAP Cloud for Customer SSI Profile is a collection of configurable settings and parameters which define what functional patterns SSI for Microsoft Outlook follows for a specific set of users. It can be adjusted individually or in bulk to suit end users' needs better.

Profile configuration steps *2.2.1 – 2.2.4* can be skipped, if you intend to apply the *DEFAULT PROFILE TEMPLATE* for the Organization to be created. In this case all users within the same organization will obtain a default set of preferences and settings provided in the solution.

&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;**2.2.1** On the *Groupware Settings* page, open the *Profiles* tab

&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;**2.2.2** Find the *DEFAULT PROFILE TEMPLATE* item and click **Copy Default Profile Template**

![](..\assets\images\Admin\2.png)

&nbsp;

&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;**2.2.3** Enter a *Profile name* and configure profile settings. There are two relevant configuration tabs, *Sync Settings* and *Add-In Settings*  

![](..\assets\images\Admin\3.png)

&nbsp;

&nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;**a.** Use the *Sync Settings* tab to configure SSI Synchronization settings which define the patterns of records syncing between SAP Cloud for Customer and the users' mailboxes  

<details><summary>>>> Click to see a screenshot <<<</summary>
<img src="..\..\assets\images\Admin\4.png">
</details>

&nbsp; 

&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;**b.** Use the *Add-In Settings* tab to configure SSI Add-In settings which define the nuances of the Add-In's functioning, such as the set of object types and their fields to be displayed and managed via the Add-In in MS Outlook

<details><summary>>>> Click to see a screenshot <<<</summary>
<img src="..\..\assets\images\Admin\5.png">
</details>

&nbsp;

&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;**2.2.4** Click **Save** or **Save and Apply Profile for All Users** in the upper right corner of the tab to finish configuring user Profile settings  

![](..\assets\images\Admin\6.png)

&nbsp;

* * *

&nbsp;

### &nbsp; &nbsp; &nbsp; &nbsp;2.3 Configuring an Organization

Organization is a group of users sharing a common set of SSI settings. An Organization's name and settings can only be adjusted by the SAP Cloud for Customer Admin.

The Organization configuration step can be skipped, if the *DEFAULT ORGANIZATION* profile will be used. In this case all its users' Sync will be authorized to access Microsoft Exchange with the same authentication method and will share the same default Profile.

&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;**2.3.1** On the *Groupware Settings* page, open the *Organizations* tab

&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;**2.3.2** Click **New** to create a new Organization

![](..\assets\images\Admin\7.png)

&nbsp;

&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;**2.3.3** Enter Organization name into the *Name* field and choose a *Profile* (the *DEFAULT PROFILE TEMPLATE* or the Profile that was specifically created for organization on the previous step)

In the *E-mail Configuration* section:

&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;**a.** If *Microsoft Exchange Impersonation* access type was chosen:

- Select this type in the *Mailbox Access Type* field
- Enter the login credentials of the [impersonated Microsoft Exchange account](../Configure-Impersonation/) configured by your local Exchange Administrator
- Enter your [Exchange Web Services (EWS) URL](https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/explore-the-ews-managed-api-ews-and-web-services-in-exchange) provided by your local Exchange Admin. By default, the EWS URL is set to *https://**[your mail server's URL]**/EWS/Exchange.asmx*. The EWS URL can also be auto-discovered, by clicking the **Auto-discover** button in the same tab  

&nbsp;

!!! note "Note"
    If *Microsoft Exchange Direct Logon* or *Office 365 OAuth* or *Google Direct Logon* access type is used, this deployment scenario implies that each end user will be required to enter one's Exchange mailbox credentials [manually in SAP Cloud for Customer SSI Sync settings](../How-to-Configure-User/)  

&nbsp;

&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;**b.** If *Microsoft Exchange Direct Logon* access type was chosen, select it in the **Mailbox Access Type** field. The access credentials will be entered by every end user individually  

&nbsp;

&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;**2.3.4** Click **Save** in the upper right corner of the tab to save and apply the settings

![](..\assets\images\Admin\8.png)

&nbsp;

* * *

&nbsp;

### &nbsp; &nbsp; &nbsp; &nbsp;2.4 User Provisioning

Provisioning is the procedure of granting and managing end users' access to SAP Cloud for Customer SSI.

&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;**2.4.1** On the *Groupware Settings* page, open the *Provisioning* tab

&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;**2.4.2** Select the users to be provisioned by clicking the **+** (Add) button next to them in the *Actions* column, or by selecting them using the checkboxes on the left-hand side and then clicking **Activate Selected** for bulk selection  

![](..\assets\images\Admin\9.png)

&nbsp;

&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;**2.4.3** On the next page:

- Select the *Organization* and *Profile* created on steps *2.2.1 – 2.2.4* and *2.3.1 – 2.3.4*
- The *Mailbox Access Type* will be set automatically, according to the Organization's settings, thus it cannot be changed from this dialog
- Optionally, at this step you can also select the *Send Welcome E-Mail* checkbox to notify the provisioned users that they got the access to SAP Cloud for Customer SSI
- Click **Provisioning** in the upper right corner of the tab  

![](..\assets\images\Admin\10.png)

&nbsp;

* * *

&nbsp;

### &nbsp; &nbsp; &nbsp; &nbsp;2.5 Enabling Users to work with SSI

*(involves using Exchange Impersonation, see point **1.1**)*

&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;**2.5.1** On the *Groupware Settings* page, open the *Users* tab and find a user provisioned on steps *2.4.1 – 2.4.3*

!!! tip "Tip"
    To filter users belonging to a specific Organization, enter its name in the text input field at the top of the *Organization* column

![](..\assets\images\Admin\11.png)  

&nbsp;

&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;**2.5.2** Click on the User's name and open the *E-Mail Configuration* subtab

&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;**2.5.3** Enter the e-mail address that belongs to the [impersonating e-mail account](../Configure-Impersonation/) (see point **1.1**) and click **Save**

![](..\assets\images\Admin\12.png)

&nbsp;

&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;**2.5.4** Now you can directly activate SAP Cloud for Customer SSI synchronization and enable the Add-In for the users' e-mail accounts by selecting the corresponding items in the picklist summoned by clicking the *Gear* button in the upper right corner of the tab

![](..\assets\images\Admin\13.png)

&nbsp;

&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;**2.5.5** (optional) You can check provisioned users' Mailbox Connectivity via the same drop-down menu  

&nbsp;

&nbsp;