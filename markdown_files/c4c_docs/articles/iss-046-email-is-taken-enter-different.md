# "ISS-046: E-Mail xxx@xxx.xxx is Already Taken. Please Enter a Different E-Mail Address" Error

&nbsp;

&nbsp;

**[ This article is work-in-progress ]**

&nbsp;

&nbsp;

## Symptoms

When trying to provision the user or during auto-provisioning (when Key User opens **Groupware Settings** for the first time) user is getting message "*ISS-046: E-Mail xxx@xxx.xxx is already taken. Please enter a different e-mail address*", where *xxx@xxx.xxx* is user's e-mail address.

&nbsp;

* * *

&nbsp;


## Causes

The issue occurs because identical e-mail addresses are used for the same users within one tenant.

For example, a USER1 with e-mail *user1@test.com* was provisioned a while ago. Then USER1 was deleted from SAP Cloud for Customer, however, it remained in Server-Side Integration. Now, when a new USER2 with the e-mail address *user1@test.com*, which is identical to the USER1's e-mail address, attempts to get provisioned – an error occurs.

&nbsp;

* * *

&nbsp;


## Resolution

To resolve the issue the following options can be used:

&nbsp;

### Option 1

Go to **E-Mail Integration** > **Groupware Settings** > **Users**. Find the affected user with the same e-mail address and either **Delete** or **Force delete** the user. 

&nbsp;

### Option 2

Change the e-mail address of the user you are trying to provision in SAP Cloud for Customer.

&nbsp;

&nbsp;