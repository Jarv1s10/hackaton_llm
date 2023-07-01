# Error "SAP Cloud for Customer Server-Side Integration for MS Outlook is not Supported for This User"

&nbsp;

&nbsp;

**[ This article is work-in-progress ]**

&nbsp;

&nbsp;

## Symptoms

The Key User attempts to install the SSI Add-In remotely for a specific user. An error occurs "*Error: SAP Cloud for Customer Server-Side Integration for Microsoft Outlook is not supported for this user*".

<p>
<img src= "..\..\assets\images\ssi-not-supported-for-this-user\3.png">
</p>

&nbsp;

The check of Add-In status shows the following message:

<p>
<img src= "..\..\assets\images\ssi-not-supported-for-this-user\5.png">
</p>

&nbsp;

* * *

&nbsp;

## Causes

The Key User attempts to install the Server-Side Integration Add-In to an unsupported version of MS Exchange.

&nbsp;

* * *

&nbsp;

## Resolution

Contact your Exchange administrator to find out the version of MS Exchange used in your organization. The supported environments are listed in the following [article](../supported-environments/).

SSI Add-In supports only Microsoft Exchange 2013 or above.

<!-- Need to clarify the supported versions of MS Exchange.
There is no information on supported environments on SAP Help Portal -->

&nbsp;

&nbsp;