# "ISSM-004: Foreign Customization Detected in User's Mailbox" Synchronization Error

&nbsp;

&nbsp;

**[ This article is work-in-progress ]**

&nbsp;

&nbsp;



&nbsp;

## Symptoms

Synchronization fails with an error "*ISSM-004: Foreign customization detected in user's mailbox &ndash; set by instance 'my000000.crm.ondemand.com'* ".

<p>
<img src= "..\..\assets\images\issm-004-foreign-customization\1.png">
</p>

&nbsp;

* * *

&nbsp;

## Causes

The issue occurs because the user’s mailbox was already initialized on a different tenant. The initial tenant URL is shown in the error message. Potential case: if a user with the same mailbox switches from test to production tenant using **Force Delete** feature; or if a user was not deleted at all. In this case, the data structure remains in the user’s mailbox, and such an error message would be shown to the user.

To avoid this from happening again, the user should be deprovisioned from the tenant using the standard **Delete** feature in **E-Mail Integration** > **Groupware Settings** > **Users** before switching to a different tenant. Connection to the mailbox should be established so the data structure clean-up can be executed appropriately during deletion.

&nbsp;

* * *

&nbsp;

## Resolution

There are two methods available to resolve the issue:

&nbsp;

#### Method 1 (recommended)

1. If you still have access to the initial tenant, which is shown in the message, log in to that tenant as a Key User
2. Go to **E-Mail Integration** > **Groupware Setting** > **Users** and find a user who is experiencing an error
3. Open the user profile, click the "**Gear**" button in the upper right corner and click **Reset mailbox**

<p>
<img src= "..\..\assets\images\issm-004-foreign-customization\2.png">
</p>

&nbsp;

4. Once mailbox is reset, log in to the new tenant and start the synchronization

&nbsp;

#### Method 2

1. Log in as a Key User on affected tenant
2. Go to **E-Mail Integration** > **Groupware Setting** > **Users** and find a user, who is experiencing an error
3. Open the user profile, click the "**Gear**" button in the upper right corner and click **Re-initialize User's mailbox**

<p>
<img src= "..\..\assets\images\issm-004-foreign-customization\3.png">
</p>

&nbsp;

4. Once user's mailbox is re-initialized, start the synchronization
5. If synchronization still works on the initial tenant &ndash; the same error will occur on that tenant

<!-- -->


&nbsp;

&nbsp;


