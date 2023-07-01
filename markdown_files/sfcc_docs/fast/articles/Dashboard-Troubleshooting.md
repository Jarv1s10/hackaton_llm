---
description: How to troubleshoot Revenue Grid widgets errors
---
# Troubleshooting Revenue Grid Widgets Errors  
  

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

This article is an addition to the [main {{ company_name }} Salesforce managed package setup article](../Admin-Managed-Package/). It describes possible errors and misconfiguration cases and their solutions.

&nbsp;

| Widgets set                                                  | How the issue manifests in Salesforce interface              | Issue explanation                                            | Solution                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [{{ company_name }}](https://docs.revenuegrid.com/articles/sfdc-widgets/) | No error message; {{ company_name }} logon dialogue is displayed   | [Tenant misconfig](../Dashboard-Salesforce/#1_set_up_tenant_urls); more than one tenant was created during configuration | [Contact our Support team](mailto:support@revenuegrid.com)   |
| [{{ company_name }}](../Dashboard-Salesforce/)                    | *"Account not provisioned as {{ company_name }} user, so you cannot access {{ company_name }} User panel (SFA-011)"* | No *ServerSyncTenantUrl* value or a wrong value entered.<br />Possibly a mismatch of accounts used to access the Add-In and the Widget.<br />Also occurs if [{{ short_name }} Sync Engine was not activated](../Authorizing-Sync-Engine-to-Work-with-Your-Data/) for the user, so the user does not exist in the tenant | Perform the [three Setup Steps](../Dashboard-Salesforce/#stage_2_setup_steps) afresh; make sure user is [logged into the Add-In](../How-to-Install-and-Run-the-Solution-for-Office-365-Mailboxes/#ii_rg_email_sidebar_logon) with the same Salesforce account as one for which the widgets are configured.<br />If that does not help, ask [our Support team](mailto:support@revenuegrid.com) to check that [{{ short_name }} Sync is activated](../Authorizing-Sync-Engine-to-Work-with-Your-Data/) for the user in the proper tenant |
| [{{ company_name }}](https://docs.revenuegrid.com/articles/sfdc-widgets/) or [{{ company_name }}](../Dashboard-Salesforce/) | No error message; Visualforce frame in Salesforce interface is blank | *ServerSyncTenantUrl* value **has no** trailing slash **/** character, so it is unusable in the system.<br />*RevenueGridTenantUrl* value **has** a trailing slash **/** character that makes it unusable in the system. | Perform the [three Setup Steps](../Dashboard-Salesforce/#stage_2_setup_steps) afresh; make sure there <b>is</b> a slash **/** character at the end of the *ServerSyncTenantUrl* value and there <b>is no</b> slash **/** character at the end of the *RevenueGridTenantUrl* value |
| [{{ company_name }}](https://docs.revenuegrid.com/articles/sfdc-widgets/) | No error message; a "Table and chair" Import to *Revenue Engage* picture is displayed on Contacts importing to {{ company_name }} | Several possible causes:<br /> No Email field value on Lead / Contact cards;<br /> Possibly the Lead / Contact was imported to {{ short_company_name }} through a *.csv* file | Check; Make sure that *Email address* value is present in Lead and Contact record cards in Salesforce; <br />Make sure there is no duplicate for this Lead/Contact in {{ short_company_name }} and press on "Import to Revenue Engage".<br />If that does not help, please report to [our Support team](mailto:support@revenuegrid.com) |
| [{{ company_name }}](https://docs.revenuegrid.com/articles/sfdc-widgets/) or [{{ company_name }}](../Dashboard-Salesforce/) | *"Message:" The requested resource does not support http method 'GET'"* | A configuration step was performed incorrectly               | Perform the [Setup Steps](../Dashboard-Salesforce/#stage_2_setup_steps) afresh |
| [{{ company_name }}](https://docs.revenuegrid.com/articles/sfdc-widgets/) or [{{ company_name }}](../Dashboard-Salesforce/) | *"No permissions to [view namespace [REVGRD] and the API [InvisibleSuite]](../Dashboard-Salesforce/#1_set_up_tenant_urls)*" notifications | The roles *Standard User* and *mail server Administrator* were not enabled with checkmarks on widgets configuring | Enable both these roles for Salesforce profiles, as described in [this article](../Dashboard-Salesforce/#3_set_up_user_profiles) |
| [{{ short_company_name }} Lead Activity History](https://docs.revenuegrid.com/articles/sfdc-widgets/#prospects_activity) or [{{ short_company_name }} Lead Sequences](https://docs.revenuegrid.com/articles/sfdc-widgets/#sequences_enrolled) | No error message; a "Table and chair" Import to *Revenue Engage* picture is displayed on Leads importing to {{ company_name }} | Several possible causes:<br>*{{ short_company_name }} Send an Email to Lead* widget was not added to Salesforce interface; <br> *"Enable automatic import of prospects into {{ company_name }} from Salesforce email sendout widget"* permission was not granted in {{ company_name }}             | Refer to [this article](../Dashboard-Salesforce/) to learn how to set up *{{ short_company_name }} Send an Email to Lead* widget and <br> to [this article](../leads-widgets-troubleshooting/) to learn how to grant all necessary permissions in {{ company_name }} |
| [{{ short_company_name }} Lead Sequences](https://docs.revenuegrid.com/articles/sfdc-widgets/#sequences_enrolled) | No error message;<br>"Add sequence" (<b>+</b>) button is missing on the *{{ short_company_name }} Lead Sequences* widget | Several possible causes:<br>the recipient is opted out from sequences;<br>the limit of the active sequences has been reached | Refer to [this article](../missing-add-sequence-button/) to learn how to investigate and resolve the issue |

&nbsp;

&nbsp;



