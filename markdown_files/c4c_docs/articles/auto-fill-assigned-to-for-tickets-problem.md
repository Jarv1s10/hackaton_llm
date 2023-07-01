# Auto-fill "Assigned To" for Tickets Feature not Working

&nbsp;

&nbsp;

**[ This article is work-in-progress ]**

&nbsp;

&nbsp;

## Symptoms

The user enabled **Auto-fill "Assigned To" for Tickets** option on the User Profile Customization page in Groupware Settings:

<p>
<img src= "..\..\assets\images\auto-fill-assigned-to-problem\3.png">
</p>

However, **Assigned To** field remains empty in SAP Cloud for Customer.

&nbsp;

* * *

&nbsp;

## Causes

The feature **Auto-fill "Assigned To" for Tickets** wasn't configured properly.

&nbsp;

* * *

&nbsp;

## Resolution

To resolve the problem, make sure that the field **Assigned To (Reference)** is available for the Ticket object in the Сustomization and that the **Display on Create** option is selected:

<p>
<img src= "..\..\assets\images\auto-fill-assigned-to-problem\4.png">
</p>

&nbsp;

&nbsp;