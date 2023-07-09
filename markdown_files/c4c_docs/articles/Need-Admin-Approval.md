# How to Resolve the "Need Admin Approval" Error

&nbsp;

The "Need Admin Approval" error may occur when a standard user attempts to authenticate their Office 365 mailbox into SSI:

<p>
    <img src="..\..\assets\images\Troubleshooting\need-approval1.png">
</p>

&nbsp;

!!! warning "Important"
    An important server-side prerequisite must be clarified with your local Admin or [SSI Support team](https://support.sap.com/en/contact-us.html). To be able to authenticate access, your company's Office 365 server must have a [valid MPN ID from Microsoft](https://docs.microsoft.com/en-us/partner-center/mpn-create-a-partner-center-account). If no MPN ID is configured, SSI App might be regarded as *unverified*, and for this reason, it will not be listed among access consent Apps in Admin settings

&nbsp;

The error is caused by User permission settings in corporate [MS Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/), where the option "*User can consent to apps accessing company data on their behalf*" is set to "*No*", along with its derivative setting for accessing the groups' data. 
&nbsp;

These settings are located in **All services** > **Enterprise applications** > **User settings** in MS Azure Active Directory.

<p>
    <img src="..\..\assets\images\Troubleshooting\need-approval2.png">
</p>

&nbsp;

* * *

&nbsp;

## Problem solutions

### Method 1

To resolve the issue, the local Office 365 Admin can consent for the App on the initial login. This method requires the O365 Admin to be an SAP Cloud for Customer user also [provisioned as an SSI user](../How-to-Configure-Admin/).

&nbsp;

Admin should perform the following configuration actions:

**1\.** Log in to SAP Cloud for Customer with Office 365 Admin account credentials

**2\.** Go to **E-Mail Integration** (1) > **User Settings** (2) > **Sync Settings** (3) > **E-Mail Configuration** (4) and click **Change** (5) in the bottom right corner

<p>
    <img src="..\..\assets\images\User\1.png">
</p>

&nbsp;

**3\.** A [standard Office 365 OAuth dialog](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-v2-protocols) will be opened in your browser. Log in with Office 365 Admin credentials

**4\.** In the following "*Permissions Requested*" dialog window, select the checkbox **Consent on behalf of your organization** and click **Accept**

<p>
    <img src="..\..\assets\images\Troubleshooting\need-approval8.png">
</p>

&nbsp;

**5\.** You will see a confirmation message "Signed in successfully"

Now consent to use the App has been granted for the whole Office 365 Org, and all end users can authenticate their Office 365 mailbox into SSI.

&nbsp;

**An optional extra step:**

In case Office 365 Admin does not intend to use Server-Side Integration afterward, a "Reset mailbox" procedure can be executed for their account in [SSI "Groupware Settings" tab](../How-to-Configure-Admin/), or they can be [unprovisioned from SSI](../How-to-Configure-Admin/#24_user_provisioning).

&nbsp;

* * *

&nbsp;

### Method 2

Another option to resolve the issue is to allow the end users to register consent for Apps on their own, as described in [this Microsoft article](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/configure-user-consent-groups?tabs=azure-portal).

!!! warning "Important"
    If this method is used, the end users will be able to register consent for **any** third party Apps; for some enterprises such setup might contradict general Office Apps security policies

&nbsp;

**1\.** Log in to Azure AD with Admin credentials

**2\.** Go to **Enterprise applications** > **User settings**

**3\.** Switch the setting "*User can consent to apps accessing company data on their behalf*" to **Yes**

<p>
    <img src="..\..\assets\images\Troubleshooting\need-approval9.png">
</p>

&nbsp;

Enabling of the setting "*User can consent to apps accessing company data for the groups they own*" is optional.

Now all users can consent to SSI accessing company data on their behalf without Admin approval.

&nbsp;

&nbsp;

**Also see the following articles for more information:**  

[Microsoft Consent framework](https://docs.microsoft.com/en-us/azure/active-directory/develop/consent-framework)

[Microsoft App Consent Experience](https://docs.microsoft.com/en-us/azure/active-directory/develop/application-consent-experience)

&nbsp;

&nbsp;