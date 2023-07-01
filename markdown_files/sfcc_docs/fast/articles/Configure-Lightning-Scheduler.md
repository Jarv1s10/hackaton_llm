---
description: Learn how to configure Salesforce Lightning Scheduler Integration with Revenue Grid
---
# How to Configure Salesforce Lightning Scheduler Integration with {{ company_name }}  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*4 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! tip "Tip"
    See [this article](https://revenuegrid.com/blog/salesforce-lightning-scheduler/) for more information on using Salesforce Lightning Scheduler and [this article](../Configure-Lightning-Scheduler/) to learn how the underlying API endpoints work. Also, see this video <https://youtu.be/D6betOrxAwo> to learn how to work with Salesforce Lightning Scheduler via {{ product_name }}

&nbsp;

This article provides the steps on how to configure [Salesforce Lightning Scheduler](https://help.salesforce.com/articleView?id=ls_overview.htm&type=5) integration with {{ product_name }}.

!!! warning "Important"
    So far,  this feature is implemented only for EWS users and is not available for the MS Graph users

&nbsp;

### Step 1: Dedicated Salesforce Managed Package Installation

**This is a bulk action performed by the Admin for all end users.**

!!! note "Note"
    The prerequisite for Managed package installation is to set up Salesforce Lightning Scheduler, as described in [this Salesforce article](https://help.salesforce.com/s/articleView?id=sf.ls_set_up.htm&type=5)

&nbsp;

Running Salesforce Lightning Scheduler integration requires a set of special Salesforce objects and classes. {{ company_name }} created a special [Salesforce Managed Package](https://help.salesforce.com/articleView?id=ls_overview.htm&type=5) that includes all required assets to facilitate the integration setup process.

The integration package *{{ short_company_name }} Lightning Scheduler Adapter* should be installed by the local Salesforce Admin as described in [this Salesforce article](https://help.salesforce.com/s/articleView?id=sf.distribution_installing_packages.htm&type=5); follow the steps below:  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1\.1.** Make sure that you have set up [My Domain](http://help.salesforce.com/articleView?id=domain_name_overview.htm&type=5) name for your Salesforce Org and deployed it for the users. Please follow the instructions in [this {{ company_name }} article](../Dashboard-Prerequisites/) to learn how to do that  

Another  prerequisite for Managed package installation is to enable the setting **Publish Appointments as Platform Events** in *Salesforce Scheduler Settings*.   
  
To do this:  
  
* **Switch to [Lightning Experience](https://help.salesforce.com/articleView?id=000337767&type=1&mode=1)**    
  
* Click the **Gear** (Setup Menu) icon in the upper right corner of the page to open [Salesforce Setup menu](https://help.salesforce.com/articleView?id=basics_nav_setup.htm&type=0)    
  
* In the *Quick Search* field in the upper left corner, type *"Scheduler Settings"* to quickly find the necessary tab  
  
* On the newly opened *Salesforce Scheduler Settings* page, enable the setting **Publish Appointments as Platform Events**
   

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Salesforce-Connectivity\scheduler-settings-enabled.png" class="minimized" style="width:90%"></p>
  
&nbsp;  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1\.2.** Open package installation link:   

**You can get the latest version of the managed package here:**   
<https://login.salesforce.com/packaging/installPackage.apexp?p0=04t09000000vMou>

Managed package updates are released regularly. Guidance on updating managed package is provided in [this section](#updating_the_salesforce_lightning_scheduler).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1\.3.** Log in to your Salesforce account (it must have Admin permissions in your Org)  

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1\.4.** Select the checkbox *I acknowledge that I’m installing a Non-Salesforce Application that is not authorized for distribution as part of Salesforce’s AppExchange Partner Program* to permit installation  


<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\install-scheduler.png" class="minimized" style="width:90%">
</p>


&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1\.5.** Indicate if you want to install the package for:

- All users in your Org
- **(recommended)** Only for specific users who will be using Lightning Scheduler integration
- Only for the Admins

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1\.6.** Click the **Install** button in the lower right corner of the page  

You'll see a notification "*Installing and Granting Access to Specific Users...*", then receive an email message that the package has been installed successfully.

&nbsp;

!!! note "Note"
    The managed package is guaranteed to be secure, confidential, and free of any malicious content, under [{{ company_name }} Privacy & Security policies](../Privacy-and-Security/)

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1\.7.** Next, after the managed package is installed, log in to Salesforce with [Admin credentials](https://admin.salesforce.com/blog/2020/introducing-admin-center-a-new-home-for-salesforce-administrators)    
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1\.8.** Switch to Lightning Experience as described in [this Salesforce article](https://help.salesforce.com/articleView?id=000337767&type=1&mode=1)    
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1\.9.** Click the **Gear** (Setup Menu) icon in the upper right corner of the page to open [Salesforce Setup menu](https://help.salesforce.com/articleView?id=basics_nav_setup.htm&type=0)    
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1\.10.** In the *Quick Search* field in the upper left corner, type *"Custom Settings"* to quickly find the necessary setting     

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1\.11.** On the *Custom Settings* page, click **Manage** button next to *Scheduler Setting* label    
  
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Salesforce-Connectivity\custom-settings-scheduler.png" class="minimized">
</p>  

&nbsp;
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1\.12.** Next, on the *Scheduler Setting* page, click **Edit** action next to the *Scheduler* name    
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1\.13.** On the Scheduler Setting Edit page, paste the *Clientid* you received from [our Support team](mailto:support@revenuegrid.com) in the relevant field and click **Save**
  
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Salesforce-Connectivity\custom-settings-scheduler-clientid.png" class="minimized">
</p>  

<br>
<hr>
<br>

### Step 2: Set the Custom Apex Class

**This is a bulk action performed by the Admin for all end users.**

In order to accurately retrieve occupied Lightning Scheduler hours spans from Salesforce, a custom Apex Class included in the managed package must be set in [Salesforce Scheduling policy settings](https://help.salesforce.com/s/articleView?id=sf.pfs_scheduling.htm&type=5). Follow the steps below to do that:  

**2\.1.** [Open Salesforce Setup Menu](https://help.salesforce.com/s/articleView?id=sf.basics_nav_setup.htm&type=5)   

**2\.2.** In the *Quick Find* field in the upper left corner of Salesforce Setup page, enter "*Scheduling policies*''  

**2\.3.** Click on **Scheduling policies** in the navigation pane on the left; you will see the list of policies in the main pane  


<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Salesforce-Connectivity\scheduling-policy.png" class="minimized" style="width:90%">
</p>

&nbsp;

**2\.4.** In the *Scheduling Policies* dialog, Click **Edit** next to *Default Appointment Scheduling Policy*  

**2\.5.** In the field *Check External Systems for Resource Availability*, enter the value *ServiceResourceScheduleHandlerImpl*; it is a dedicated Apex class included in the managed package  


<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Salesforce-Connectivity\policy-edit.png" class="minimized" style="width:90%">
</p>

&nbsp;

**2\.6.** Click **Save** at the bottom of the dialog  

Now Lightning Scheduler integration is connected and ready to be used. See [this video](https://youtu.be/D6betOrxAwo) to learn how to use the feature.


<br>
<hr>
<br>

### Step 3: Connect Lightning Scheduler Integration

**It's recommended that the Admin performs this action in a dedicated Salesforce Service Account.**

Next, you need to connect integration via the installed managed package. Perform the following steps:

**3\.1** [Open Salesforce Setup Menu](https://help.salesforce.com/s/articleView?id=sf.basics_nav_setup.htm&type=5) 

**3\.2.** In the *Quick Find* field in the upper left corner of Salesforce Setup page, enter "*Remote site settings*"

**3\.3.** Click on **Remote Site Settings** in the navigation pane on the left; you will see the list of remote sites configured for your Org in the main pane
<p>
<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Salesforce-Connectivity\remote-site.png" class="minimized" style="width:50%">
</p>
&nbsp;

**3\.4.** Click the **New Remote Site** button
<p>
<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Salesforce-Connectivity\new-site.png" class="minimized" style="width:90%">
</p>
&nbsp;

**3\.5.** On the Remote Site Edit page: 

* Enter “*LSA*” in the **Remote Site Name** 

* Enter the specific Sync URL provided by {{ company_name }} support team for your Org, e.g. *https://sample-sync.revenuegrid.com* in the **Remote Site URL** 

* Make sure that the **Active** checkbox **is enabled** 

* Click **Save** 

<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Salesforce-Connectivity\edit.png" class="minimized" style="width: 70%;">
&nbsp;

**3\.6.** In the *Quick Find* field in the upper left corner of Salesforce Setup page, enter "*Installed packages*"


**3\.7.** Click on **Installed packages** in the navigation pane on the left; you will see the list of Managed packages installed in your Org in the main pane

**3\.8.** Click on **Configure** next to *{{ short_company_name }} Lightning Scheduler Adapter* package  
&nbsp;

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Salesforce-Connectivity\installed-packages.png" class="minimized" style="width:90%">
</p>

&nbsp;

**3\.9.** In the dialog that appears, enter the specific Sync URL provided by [{{ company_name }} support team](mailto:support@revenuegrid.com) for your Org, e.g., *https://sample-sync.revenuegrid.com*, into the designated field

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Salesforce-Connectivity\link-connect.png" class="minimized">
</p>

&nbsp;

**3\.10.** Click the button **Connect** next to the field

**3\.11.** You will see a link appear on the page


**3\.12.** Copy the link and open it in an incognito browser window

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Salesforce-Connectivity\open-link.png" style="width:90%">
</p>


**3\.13.** You will see a standard Salesforce OAuth window. Log in to it with Salesforce credentials to authorize data access for integration  

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Salesforce-Connectivity\oauth.png" style="width:50%">
</p>

**3\.14.** Go back to the page in step 3.5. and check whether the green popup notification “*Connected*” appeared. 

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Salesforce-Connectivity\connected.png" style="width:90%" class="minimized">
</p>


<br>
<hr>
<br>


### Step 4: Check your connection status

**1.** Enter the specific Sync URL provided by [{{ company_name }} support team](mailto:support@revenuegrid.com), e.g., *https://sample-sync.revenuegrid.com*, into the URL field in your web browser 

**2.** Select the option “Sign in with Salesforce” 

**3.** You will see a standard Salesforce OAuth window. Log in to it with Salesforce credentials to access {{ short_company_name }} sync settings page 

**4.** Check the connection status.  
If the connection wasn’t established, contact [our support team](mailto:support@revenuegrid.com) for assistance.

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Salesforce-Connectivity\connection-stat.png" class="minimized"></p>


<br>
<hr>
<br>

### Step 5: Configure the necessary Salesforce flows (auxiliary)

!!! warning "Important"
    This is the auxiliary step **ONLY** for the organizations which use custom Salesforce flows created from *Inbound New Guest Appointment* and *Book Appointment from Invitation* [standard flow templates](https://help.salesforce.com/s/articleView?id=sf.ls_provided_flows.htm&type=5) for scheduling appointments. <br><br> 
    If your organization does **not** use any custom Salesforce flows created from *Inbound New Guest Appointment* and *Book Appointment from Invitation* standard flow templates, skip this step
<br>

If your company utilizes the Salesforce flows created using the *Inbound New Guest Appointment* and *Book Appointment from Invitation* [standard flow templates](https://help.salesforce.com/s/articleView?id=sf.ls_provided_flows.htm&type=5) for scheduling appointments, you must configure your custom flows additionally to use the {{ short_company_name }} Lightning Scheduler Adapter. 


**1\.** Switch to [Lightning Experience](https://help.salesforce.com/articleView?id=000337767&type=1&mode=1)    
 
<!--<p><img src="..\..\assets\images\Configuration-&-Settings\User-Settings\partner-community\setup.png" style="width:55%; display:inline-block; vertical-align:middle; margin-left:1px;float: right" class="minimized"></p>  -->
**2\.** Click the **Gear** (Setup Menu) icon in the upper right corner of the page to open [Salesforce Setup menu](https://help.salesforce.com/articleView?id=basics_nav_setup.htm&type=0)    
  
<!--<p><img src="..\..\assets\images\Configuration-&-Settings\User-Settings\partner-community\partner-com1.png" style="width:55%; display:inline-block; vertical-align:middle; margin-left:1px;float: right" class="minimized"></p>-->
**3\.** In the *Quick Search* field in the upper left corner, type *"Flows"* to quickly find the necessary tab  
  
**4\.** Next, in the list of flows, find the one that was created from the template *Inbound New Guest Appointment*
<p style="margin-left:7%">
    <b>4.1.</b> Click on the flow to open the <b>Flow builder</b>
<br><br>
    <b>4.2.</b> Then find the <b>Action: Save Appointment</b> block and click on it
</p>
<p>
    <img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Salesforce-Connectivity/action1.png" style="width:75%;" class="minimized">
</p>
<br>
<p style="margin-left:7%">
    <b>4.3.</b> In the dialog window, click on the <b>Advanced</b> section to expand it
<br><br>
    <b>4.4.</b> In Transaction control, select the option "<b>Let the flow decide (recommended)"</b>
</p>
<p>
    <img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Salesforce-Connectivity/let-the-flow-decide.png" style="width:85%;" class="minimized">
</p>
<br>
<p style="margin-left:7%">
    <b>4.5.</b> Click <b>Done</b>
<br><br>
    <b>4.6.</b> In the upper right-hand corner, click <b>Save</b> to enforce the changes
</p>
<br><br>

**5\.** In the list of flows, find the one that was created from the template *Book Appointment from Invitation*
<p style="margin-left:7%">
    <b>5.1.</b> Click on the flow to open the <b>Flow builder</b>
<br><br>
    <b>5.2.</b> Then find the <b>Action: Save Guest Appointment</b> block and click on it
</p>
<p>
    <img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Salesforce-Connectivity/action2.png" style="width:65%;" class="minimized">
</p>
<br>
<p style="margin-left:7%">
    <b>5.3.</b> In the dialog window, click on the <b>Advanced</b> section to expand it
<br><br>
    <b>5.4.</b> In Transaction control, select the option <b>"Let the flow decide (recommended)"</b>
</p>
<p>
    <img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Salesforce-Connectivity/let-the-flow-decide.png" style="width:85%;" class="minimized">
</p>
<br>
<p style="margin-left:7%">
    <b>5.5.</b> Click <b>Done</b> 
<br><br>
    <b>5.6.</b> In the upper right-hand corner, click <b>Save</b> to enforce the changes
</p>

<br>
<hr>
<br>

### Updating the Salesforce Lightning Scheduler 

To catch up with the latest Salesforce updates and ensure seamless Lightning Scheduler Integration functioning, we regularly release updates. The updated links are published in this article's topmost section.


To upgrade to the latest Salesforce Lightning Scheduler version:

**1\.** Open the new managed package link in your web browser  

**2\.** Log in to your Salesforce account (it must have Admin permissions in your Org)


**3\.** Indicate if you want to upgrade the package for:

- *All users in your Org*
- (recommended) *Install for specific Profiles*  which will be using {{ company_name }} components
- *Only for the Admins*



**4\.** If you chose *Install for specific Profiles*, set the needed profiles scope using the controls underneath 

!!! note "Note"
    Also see [the relevant Salesforce guide](https://developer.salesforce.com/docs/atlas.en-us.230.0.appExchangeInstallGuide.meta/appExchangeInstallGuide/appexchange_install_installation.htm) for details

**5.** Select the checkbox *I acknowledge that I’m installing a Non-Salesforce Application that is not authorized for distribution as part of Salesforce’s AppExchange Partner Program* to permit installation

**6.** Click the **Install** button in the lower right corner of the page

You’ll see a notification “*Installing and Granting Access to Specific Users…*”, then receive an email message that the package has been installed successfully.