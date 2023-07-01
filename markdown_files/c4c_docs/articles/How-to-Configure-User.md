# Configuring SAP Cloud for Customer Server-Side Integration by User

&nbsp;

&nbsp;

If the local Admin has [deployed SAP Cloud for Customer SSI](../How-to-Configure-Admin/) using *Microsoft Exchange Direct Logon*, *Office 365 OAuth*, or *Google Direct Logon* Mailbox Access type, the below actions must be performed by the user to get the SSI running.

!!! warning "Important"
    If SSI was deployed using [*Microsoft Exchange Impersonalization*](../Configure-Impersonation/), **no more setup actions are required** on the user side

&nbsp;

&nbsp;

## Initialize SSI connection to the mailbox account

**1.** Log in to SAP Cloud for Customer with your user credentials, go to **User Settings** (1) > **Sync Settings** (2) > **E-Mail Configuration** (3) > click on the **Change** (4) button

<p>
<img src="../../assets/images/User/1.png">
</p>

&nbsp;

&nbsp;

**2.** In the following dialog, select your e-mail account type: *MS Office 365*, *Google*, or *MS Exchange/Outlook.com*  

!!! note "Note"
    This dialog can be skipped for users belonging to an [Organization](../How-to-Configure-Admin/#23_configuring_an_organization) within which admin has specified the particular e&#8209;mail service already

<p>
<img src="../../assets/images/User/2.png">
</p>

&nbsp;

&nbsp;

**3.** At the next step, you will be asked to perform the authentication. The authentication procedure depends on the selected Mailbox Access type, so follow the instructions in the opened dialog or window to authenticate your user account

If any problem arises during the authentication procedure, you can be redirected to the extended login dialog, where you should enter additional account details.

<details><summary>> > > Click to see a screenshot < < <</summary>
<p>
<img src="../../assets/images/User/extended-login.png">
</p>
</details>

!!! warning "Important"
    Your e-mail account's login credentials will be stored securely in Microsoft Azure infrastructure and never revealed anywhere or accessed by anyone, according to [Privacy & Security Policy](../Privacy-and-Security/)

<!--
<p>
<img src="../../assets/images/User/3.png">
</p>
-->

&nbsp;

&nbsp;

**4.** Once the authentication is finished, the *"Synchronization was enabled"* notification should appear

<p>
<img src="../../assets/images/User/4.png">
</p>

&nbsp;

Now the SAP Cloud for Customer SSI Add-In (Sidebar) should be enabled automatically for this e-mail account. To verify that, open your mailbox, select any non-automatically generated e-mail message, and check whether the SSI Add-In icon has appeared.

<!--
<p>
<img src="../../assets/images/Start/web_small1.png">
</p>
-->

&nbsp;

&nbsp;

***

&nbsp;

&nbsp;

## SSI custom folders and categories in the mailbox

Once the SSI connection to the mailbox account is finished, SSI starts [synchronizing](../C4C-SSI-Sync-Overview/) the data between your mailbox and SAP Cloud for Customer. When the first sync session is complete, several dedicated folders and custom categories should be auto-created in your MS Outlook (or Gmail). The duration of the first synchronization depends on the amount of data that should be processed and may take longer than a regular sync.

For the accounts and contacts two-way synchronization, SSI uses the custom folders named *SAP Accounts*, *SAP Contacts*, and *SAP Individual Customers*:

<p>
<img src="../../assets/images/User/6.png">
</p>

&nbsp;

Additionally, SSI uses the custom categories for saving objects from MS Exchange / Office 365 / Gmail to SAP Cloud for Customer and for indicating their sync status:

<p>
<img src="../../assets/images/User/categories.png">
</p>

&nbsp;

!!! note "Note"
    If you are getting any error messages during initial configuration, the Add-In (Sidebar) doesn't appear, or these custom folders are not created in your mailbox, contact your local Admin for assistance

&nbsp;

After setting up the tool, you may proceed to your SAP Cloud for Customer page to set SSI Profile settings according to your preferences. More details in [this article](../How-to-Open-Your-C4C-SSI-Settings-Profile/).

&nbsp;

&nbsp;


