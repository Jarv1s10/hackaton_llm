# Setting Up SAP Cloud for Customer SSI Sync via Impersonation and Configuring Users Mailboxes  


<span style="color: #e74125;font-size: 17px;font-weight: 700;line-height: 30px;padding: 0px 10px;outline: none;border-radius: 2px;text-decoration: none;background-color: #fff;display: inline-block;border: 0px solid #000;transition: .3s all;width: auto;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="display: inline-block;vertical-align: middle;height: 32px;object-fit: contain;"></span><span style="color: #e74125;font-size: 17px;font-weight: 700;line-height: 30px;padding: 0px 10px;outline: none;border-radius: 2px;text-decoration: none;background-color: #fff;display: inline-block;border: 0px solid #000;transition: .3s all;width: auto;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="display: inline-block;vertical-align: middle;height: 32px;object-fit: contain;"></span>

&nbsp;

[MS Exchange / Office 365 Impersonation](http://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange) is used in scenarios when a single administrative service account is used to access and manage many end user accounts, to view or adjust their settings or perform various actions on these accounts' behalf.
In SAP Cloud for Customer SSI setup context, Impersonation allows to automatically activate SSI synchronization for all relevant user accounts in bulk, via an [impersonating MS Exchange service account](https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/how-to-configure-impersonation).

&nbsp;

!!! tip "Tip"
    Also refer to [this blog entry](https://blogs.sap.com/2019/01/13/how-to-configure-sap-cloud-for-customer-exchange-impersonation/) for relevant instructions

&nbsp;

&nbsp;

### Setting up SSI Sync for multiple users via Exchange/Office 365 Impersonated Access

&nbsp;

**1\.** Open MS Exchange or Office 365 Admin center. Refer to the following articles to learn how to do that:

*   [Office 365](https://support.office.com/en-us/article/about-the-office-365-admin-center-758befc4-0888-4009-9f14-0d147402fd23)
*   [Exchange 2013](https://technet.microsoft.com/en-us/library/jj150562(v=exchg.150).aspx#access)
*   [Exchange 2016, 2019](https://technet.microsoft.com/en-us/library/jj150562(v=exchg.160).aspx)

&nbsp;

**2\.** Create an MS Exchange/Office 356 service account and assign it [Impersonation permissions](https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange) using the following step-by-step guides:

* [MS Exchange](https://cloudsolutions.atlassian.net/wiki/spaces/CKB/pages/4358166/Setting+up+Application+Impersonation+for+Exchange+or+Office+365) 
* [Office 365](https://www.mailsdaddy.com/blogs/how-to-grant-application-impersonation-rights-office365/)


&nbsp;

**3\.** Set up an Organization containing all relevant user mail accounts:

&nbsp;&nbsp;&nbsp;&nbsp;**3.1\.** Log in to SAP Cloud for Customer SSI Admin panel (the login credentials are provided by [SAP Cloud for Customer support](https://support.sap.com/en/contact-us.html))

&nbsp;&nbsp;&nbsp;&nbsp;**3.2\.** [Create an Organization](../How-to-Configure-Admin/#23_configuring_an_organization) in SAP Cloud for Customer SSI Admin panel [optional]

&nbsp;&nbsp;&nbsp;&nbsp;**3.3\.** [Add all relevant user accounts to the created Organization](../How-to-Configure-Admin/#24_user_provisioning) [optional]

&nbsp;

**4.** Proceed to the instructions below to bulk-activate SAP Cloud for Customer SSI Sync for all user accounts

&nbsp;

&nbsp;

#### Configuring Mailbox Access for SSI Sync

To configure or update an Organization's access to the mailbox:  

&nbsp;&nbsp;&nbsp;&nbsp;**4.1\.** Go to the *Organizations* tab and select the needed Organization or create one which will include all users covered by a single Impersonating account, then go to the **E-Mail Configuration** section  

&nbsp;

!!! note "Note"
    If your company uses several different Microsoft Exchange deployments, you will need to create several SAP Cloud for Customer SSI Organizations for every group of users residing on a specific server

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;**4.2\.** In the **Mailbox Access Type** drop-down list, select **Microsoft Exchange Impersonation** mailbox access type  

&nbsp;&nbsp;&nbsp;&nbsp;**4.3\.** In the *Account Logon* field, enter the Impersonating account's name  

&nbsp;&nbsp;&nbsp;&nbsp;**4.4\.** In the *Password* field, enter the Impersonating account's password  

**5\.** In the *Exchange Web Services (EWS) URL* field, enter the [EWS URL](https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/start-using-web-services-in-exchange) used in your MS Exchange

**6\.** Click **Save** to finish the procedure

![](..\assets\images\Admin\8.png)

&nbsp;

&nbsp;