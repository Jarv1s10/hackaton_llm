# "Forbidden" Error after Key User Deletion

&nbsp;

&nbsp;

**[ This article is work-in-progress ]**

&nbsp;

&nbsp;

## Symptoms

1. Key User navigates to *Users* tab and deletes himself
2. An error is displayed "*Forbidden - GET https://%tenantid%-0crm-0ondemand-0com.c4c.invisiblesolutions.com/api/users This page or action is forbidden*"

<p>
<img src= "..\..\assets\images\forbidden-error-key-user-deletion\1.png">
</p>

3. After opening *Groupware Settings* page Key User appears again in user's list

&nbsp;

* * *

&nbsp;

## Causes

This is an expected behavior, as long as Key User (Administrator) has deleted himself, he can no longer access pages in groupware settings. As soon as user re-opens the *Groupware Settings* page, Key User will be provisioned again.

&nbsp;

* * *

&nbsp;

## Resolution

1. Key Users planned to be disabled (deleted) **must not open** *Groupware Settings* anymore. Such users will no longer be provisioned
2. **Do not delete Key Users** from the *Users* tab, leave them "as is"
3. Restrict access rights for such users in SAP Cloud for Customer, so they don't have access to *Groupware Settings* and Key User permissions

&nbsp;

&nbsp;