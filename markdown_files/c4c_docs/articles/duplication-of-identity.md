# How to Resolve "Values user@outlook.com for Settings ExchSMTPEmailAddress are Causing a Duplication of the Identity for Some Employees" 

&nbsp;

&nbsp;

**[ This article is work-in-progress ]**

&nbsp;

&nbsp;

## Symptoms

When trying to link an e-mail to a user in the **E-Mail Configuration** tab, the following error is shown: "*Values user@outlook.com for settings ExchSMTPEmailAddress are causing a duplication of the identity for some employees*".

&nbsp;

* * *

&nbsp;

## Causes

Some other tenants already use the specified e-mail address. Since identity validation works in cross-tenant mode, the error occurs.

&nbsp;

* * *

&nbsp;

## Resolution 

If the user **has access** to older tenants, the user should be deleted from them first, then, it can be provisioned on the new tenant, and the e-mail address can be used again. Do the following steps to delete the user from older tenants:

1. Go to **E-Mail Integration** > **Groupware Settings** > **Users**
2. Find the required user and open its profile page
3. In the upper right corner, click the 'Gear' button and then click **Delete** from the drop-down dialog

&nbsp;

If the user **doesn't have access** to older tenants, they should be deprovisioned by SAP, and within the next two hours, they will be deleted in E-Mail Integration, and the user should be able to use them again.

<!-- "... to use them again" - to use what? older tenants for self deletion or new tenant?
who perform deletion - user or key user?
Deprovisioned by SAP support team or who? -->

&nbsp;

&nbsp;


