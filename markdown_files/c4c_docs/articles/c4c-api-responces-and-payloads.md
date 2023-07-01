# How to Work with SAP Cloud for Customer API Responses and Payloads

&nbsp;

&nbsp;

**[ This article is work-in-progress ]**

&nbsp;

&nbsp;

!!! warning "Important"
    Do not confuse the SAP team with the SSI team. The **SAP team** works only on the CRM (SAP Cloud for Customer) side, while the **SSI team** is responsible for SSI Synchronization and Add-In operations

&nbsp;

Most of the issues occurring during the synchronization or Add-In usage are related to root causes lying on the SAP Cloud for Customer side. The scope of responsibility of the Server-Side Integration team ends here since the nature of the issue has to be looked into and advised by the SAP Cloud for Customer Developers. 

This article provides knowledge on how to collect needed information (payloads) for escalating cases for a review to the SAP Cloud for Customer Developers and how to identify if an issue is not related to an SSI bug or problem.

&nbsp;

* * *

&nbsp;

## How to collect information that describes issue causes

1. Find a sync log where the issue occurs. The problem can be defined as a sync failure or sync issue.

2. Navigate to the *job.log* file first to identify if the issue comes from INFO TID:79 **[SiteInMemory:C4CConnector]**. If not, the issue cannot be related to the SAP Cloud for Customer API response.

3. Navigate to the *C4C_Dump*. The operations are broken down and named separately there.

<p>
<img src= "..\..\assets\images\c4c-api-responces-and-payloads\1.png">
</p>

&nbsp;

4. Navigate to a file that describes affected operation, find the corresponding payload (request and response) defining the issue.

<p>
<img src= "..\..\assets\images\c4c-api-responces-and-payloads\2.png">
</p>

&nbsp;

&nbsp;

If the response contains any kind of message coming from the SAP side with corresponding response headers – it should be copied to a separate file (including a request) and attached to the incident as evidence. There could be no SAP response at all – the request may also be collected and sent to the SAP API team, asking for the reason for the absent response.

Please do not mix up the SAP response with an exception in *C4C_dump*. All exceptions are thrown from the SSI side and should be looked at by the SSI team in case the response from SAP is valid. Please do not attach the exception info for the SAP team since it is not their scope of responsibility to check it.

&nbsp;

The response may be valid but not acceptable in terms of SSI design. Review the error message carefully and investigate the data returned by SAP. Check if the data returned is valid or not. 

The same payloads can be generated using the OData monitor.

&nbsp;

To check the authorization permissions, navigate to the **001_Permissions_c4codataapi** file. In the response payload, you will find information on read/write access to a collection. For example, navigate to *EntitySetName='AppointmentCollection'* and see if the following attributes have value **true**. The attributes to check are: "*HasReadAccess*" and "*HasWriteAccess*".

&nbsp;

* * *

&nbsp;

## Summary

Payloads in SAP Cloud for Customer have the most important meaning and have to be reviewed and analyzed first. The user interface, in this case, has much less priority since SSI works exclusively with SAP Cloud for Customer API.

&nbsp;

&nbsp;