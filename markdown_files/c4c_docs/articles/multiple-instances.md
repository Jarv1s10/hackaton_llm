# Multiple Instances of the Add-In are Installed to One User

&nbsp;

&nbsp;

**[ This article is work-in-progress ]**

&nbsp;

&nbsp;

## Symptoms

User is having several (2 or more) copies installed on the mailbox. Ribbon contains 2 icons and **Manage Add-In** list contains 2 items as well.


<p>
<img src= "..\..\assets\images\multiple-instances\1.png">
</p>

&nbsp;

* * *

&nbsp;

## Causes

*Manifest.xml* of the Add-In contains the add-in ID (e.g. *&lt;Id&gt;50936338-55a0-441e-a889-d4e95c9667fd&lt;/Id&gt;*) and technically MS Exchange allows installing only one instance of the Add-In with the same ID. Add-Ins from different tenants (test\prod) may have different IDs, so that's why multiple add-ins can be installed.

&nbsp;

* * *

&nbsp;

## Resolution

To resolve the issue the following steps should be proceeded:

1. Delete all copies of the Add-In using any convenient method (via **Groupware Settings**, OWA (Outlook Web Access), or MS Exchange Admin Center)
2. Identify the target SAP Cloud for Customer tenant and deploy the Add-In from that tenant (either from **Groupware Settings** or manually through MS Exchange Admin Center using *manifest.xml*)

<!-- -->

&nbsp;

&nbsp;