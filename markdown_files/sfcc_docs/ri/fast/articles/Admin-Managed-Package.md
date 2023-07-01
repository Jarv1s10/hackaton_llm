---
title: Revenue Grid Managed Package
description: Setup and configuration of Revenue Grid managed package & Salesforce visual components
---

# Revenue Grid Managed Package & Salesforce Visual Components Setup  


<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*10 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

To enable the full scope of {{ company_name }} features after [installing the Solution](../How-to-Install-and-Run-the-Solution-all-configurations/), the local Salesforce Admin should install a special *{{ company_name }}* [Salesforce managed package](http://developer.salesforce.com/docs/atlas.en-us.appExchangeInstallGuide.meta/appExchangeInstallGuide/appexchange_install_notification.htm) that includes a number of auxiliary custom fields, classes, and other components. The package was previously known as the *{{ company_name }}* managed package.

**You can get the latest version of the managed package here:**   
<https://login.salesforce.com/packaging/installPackage.apexp?p0=04t1P000000ElXz>

**Managed package for Professional Salesforce edition:**
<https://login.salesforce.com/packaging/installPackage.apexp?p0=04t1P0000006KNH>

The Publisher name of the package *InvisibleCRM* is an old brand name of {{ company_name }}.

&nbsp;

Besides providing the auxiliary elements, the managed package enables {{ company_name }} controls integration into Salesforce user account interface, using a [custom Salesforce Canvas app mechanism](https://developer.salesforce.com/docs/atlas.en-us.platform_connect.meta/platform_connect/canvas_framework_intro.htm). This possibility is available for both [Salesforce Classic UI and Salesforce Lightning Experience](https://help.salesforce.com/articleView?id=lex_aloha_comparison.htm&type=5).  

&nbsp;

!!! note "Note"
    The managed package is guaranteed to be secure, confidential, and free of any malicious content, under [{{ company_name }} Privacy & Security policies](../Privacy-and-Security/)

&nbsp;

!!! note "Note"
    If the error "*This package can't be installed*" occurred on the managed package installation to the [Salesforce Professional Edition](https://help.salesforce.com/s/articleView?id=sf.overview_edition.htm&type=5), refer to [this article](../managed-package-installation-failed/) to learn how to handle the issue

&nbsp;

* * *

&nbsp;

#### The extra features provided by the package

**1\.** The possibility to dock [{{ product_name }}](../Introduction/) into a user's Salesforce page, this way enabling various scenarios of convenient emails and calendar data handling directly from users' Salesforce accounts. It is implemented as a [Salesforce Canvas](https://developer.salesforce.com/docs/atlas.en-us.platform_connect.meta/platform_connect/canvas_framework_intro.htm) pane; such panes are used to add various visual pages to Salesforce user interface

!!! tip "Tip"
    Another use for the [Salesforce Canvas](https://developer.salesforce.com/docs/atlas.en-us.platform_connect.meta/platform_connect/canvas_framework_intro.htm) component is to make [{{ product_name }} Admin Panel](../How-to-Log-In-to-the-Admin-Panel/) settings faster to access and manage for the local Admin users, by docking the Admin panel as a Canvas pane onto their Salesforce pages

&nbsp;

**2\.** The package includes an extended set of custom object fields required for using the complete [revenue intelligence package {{ company_name }}](https://docs.revenuegrid.com/) as well as for advanced {{ product_name }} features, e.g. [Engagement logging in Salesforce](../How-to-Use-SCC-Engagement-Panel-%28Adaptive-view%29/#engagement_data_logging_in_salesforce). That also covers some of the fields and components added by the [older Invisible Suite managed package](../Admin-Managed-Package/#specific_fields_classes_and_components_the_revenue_inbox_package_adds_to_your_salesforce_configuration)

**3\.** Direct and handy [Salesforce reports](https://help.salesforce.com/articleView?id=rd_reports_overview.htm&type=5) access and use. With this component installed, the end users will be able to use a pre-configured set of [Salesforce reports](../Salesforce-Reports/) or [customize reports](https://help.salesforce.com/articleView?id=reports_defining_report_types.htm&type=5) to be used for their specific needs

**4\.** For [Revenue Engage revenue intelligence platform](https://docs.revenuegrid.com/) users, the package allows to dock Revenue Engage tabs straight into their Salesforce user interface, as [Visualforce components](https://trailhead.salesforce.com/en/content/learn/modules/visualforce_fundamentals)

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\RE-tabs.png" class="minimized">
</p></details>



&nbsp;

* * *

&nbsp;

#### I. Install {{ company_name }} managed package

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1.** Make sure that you have set up [My Domain](http://help.salesforce.com/articleView?id=domain_name_overview.htm&type=5) name for your Salesforce Org and Deployed it to Users. Please follow the instructions in [this {{ company_name }} article](../Dashboard-Prerequisites/) or [this Salesforce Help article](https://help.salesforce.com/s/articleView?id=sf.domain_name_setup.htm&type=5) to learn how to do that

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2.** Open package installation link:  

* [Package for regular use in Salesforce Production](https://login.salesforce.com/packaging/installPackage.apexp?p0=04t1P000000ElXz)

* [Package for Salesforce Sandbox use](https://login.salesforce.com/packaging/installPackage.apexp?p0=04t1P000000ElXz). Learn more about the specifics of installing packages in a Sandbox in [this Salesforce help](https://help.salesforce.com/articleView?id=distribution_installing_packages.htm&type=5) article

  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**3.** Log in to your Salesforce account (it must have Admin permissions in your Org)
&nbsp;
&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**4.** Indicate if you want to install the package for:
&nbsp;
&nbsp;  
  
- *All users in your Org*    
- (recommended) *Install for specific Profiles*:  which will be using {{ company_name }} components     
- *Only for the Admins*  
    

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\install_new.png" style="width: 80%; height: 80%;">
</p>

&nbsp;
&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**5.** If you chose *Install for specific Profiles*, set the needed profiles scope using the controls underneath

!!! note "Note"
    Also see [the relevant Salesforce guide](https://developer.salesforce.com/docs/atlas.en-us.230.0.appExchangeInstallGuide.meta/appExchangeInstallGuide/appexchange_install_installation.htm) for details

&nbsp;

<details><summary> >>> Click to see the controls' screenshots <<< </summary>
<p>
<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\RG-package-2.png">
</p>
<br>
<br>
<br>
<p>
<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\RG-package-3.png">
</p>
<br>
<br>
<br>
<p>
<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\RG-package-4.png">
</p></details>

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**6.** Click the button **Install** underneath

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**7.** Next, you will see the following notification, click the **Done** button, and soon you will receive an email message from Salesforce confirming that the package was installed.

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\RG-longer.png" style="width: 90%; height: 90%;">
</p>

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**8.** After {{ company_name }} Salesforce managed package is successfully installed, you can access it in the Salesforce Navigation panel: Platform tools > Apps > Packaging > Installed Packages

<p><img src= "..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\package-location.png" style="width: 90%; height: 90%;" class="minimized">
</p>




&nbsp;

* * *

&nbsp;

#### II. Configure the app in Salesforce

After the managed package has been installed, you can proceed to configuring the {{ company_name }} app in Salesforce.
    
  
!!! warning "Important"  
    For completing {{ company_name }} app configuration, you will need to generate tenant URLs. Learn how to generate *RevenueGridTenantUrl* and *ServerSyncTenantUrl* in this [{{ company_name }} article](../How-to-generate-tenant-urls/) or contact [our Support team](mailto:support@revenuegrid.com)
&nbsp;

**1\.** Click on the **Gear** ⚙  icon and select **Setup**    
  
<p><img src= "..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\managed-package-1.png" style="width: 50%; height: 50%;">
</p> 

&nbsp;  

**2\.** In the left-hand sidebar go to **Custom Code** > **Custom Settings**. On the list, find the Namespace Prefix value *REVGRD* and click on the **Manage** button next to the *CanvasAppSettings* label. Once it opens, click **Edit**    
  
<p><img src= "..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\managed-package-2.png" style="width: 90%; height: 90%;" class="minimized">
</p>

&nbsp;  

**3\.** On the newly opened *CanvasAppSettings Edit* page, enter the [tenant URLs](../How-to-generate-tenant-urls/)  *RevenueGridTenantUrl* and *ServerSyncTenantUrl* value fields. Make sure the URLs start with **https**. After entering the URLs into the relevant fields, click **Save**      
  
<p><img src= "..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\managed-package-3.png" style="width: 90%; height: 90%;" class="minimized">
</p> 

&nbsp;  

<details><summary> >>> Click to see an animation <<< </summary>
<p><img src= "..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\managed-package-urls.gif" class="minimized">
</p></details>  

&nbsp;  

**4\.** Next, to setup user authorization policies go to **Platform Tools** > **Apps** > **App Manager** (1). Choose *Revenue Inbox for Salesforce* (2) from app list and click **Manage** (3)      
  
<p><img src= "..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\managed-package-4.png" style="width: 90%; height: 90%;" class="minimized">
</p>

&nbsp;

**5\.** On the newly opened page, click **Edit Policies** button, then in *Permitted Users* field choose *Admin approved users are pre-authorized* and confirm it in the pop-up window. Click **Save** button to apply the changes    
  
<details><summary> >>> Click to see an animation <<< </summary>
<p><img src= "..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\managed-package-app-manager.gif" class="minimized">
</p></details>  

&nbsp;  

**6\.** Down on the *Connected App* page, click **Manage Profiles**, then choose User Profiles for which the application will be installed. Normally, standard users would be the targeted profiles among other profiles. It's recommended to choose system administrators as well. Save changes after selecting relevant User Profiles    
  
<details><summary> >>> Click to see an animation <<< </summary>
<p><img src= "..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\managed-package-manage-profiles.gif" class="minimized">
</p></details>  

&nbsp;
* * *
&nbsp;

#### III. Add {{ company_name }} components to Salesforce user interface

After you set up the Managed Package and configure the app in Salesforce, you can dock {{ company_name }} panes (widgets) in Salesforce User Interface.  
See the video guide below to learn how to do that:

<iframe src="https://player.vimeo.com/video/418953523" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>  

&nbsp;  

##### How to configure {{ company_name }} widgets for an invividual user  
    
Refer to [this article](../Dashboard-Salesforce/#24_finalizing_setup_in_salesforce_user_interface) for a step-by-step instruction on configuring {{ company_name }} widgets for an individual user.  

##### How to setup {{ company_name }} dashboard widgets for other users in your Org
  
Refer to [this article](../Dashboard-Users-Only/#how_to_configure_contact_lead_or_opportunity_widgets_for_a_salesforce_admin_user_account) for configuration instructions for Salesforce Admins intending to set up {{ company_name }} widgetsfor other users in their Org  

&nbsp;

* * *

&nbsp;

#### Updating the {{ company_name }} managed package

To catch up with the latest Salesforce updates and ensure {{ short_name }} new features functioning, we regularly release {{ company_name }} managed package updates. The updated links are published in this article's topmost section.

To upgrade to the latest Managed Package version:

**1\.** Open the new managed package link in your web browser  

**2\.** Log in to your Salesforce account (it must have Admin permissions in your Org)

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\install_new.png">
</p></details>

&nbsp;

**3\.** Indicate if you want to upgrade the package for:

- *All users in your Org*
- (recommended) *Install for specific Profiles*:  which will be using {{ company_name }} components
- *Only for the Admins*

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\upgrade.png">
</p></details>

&nbsp;

**4\.** If you chose *Install for specific Profiles*, set the needed profiles scope using the controls underneath 

!!! note "Note"
    Also see [the relevant Salesforce guide](https://developer.salesforce.com/docs/atlas.en-us.230.0.appExchangeInstallGuide.meta/appExchangeInstallGuide/appexchange_install_installation.htm) for details

&nbsp;

<details><summary> >>> Click to see the controls' screenshots <<< </summary>
<p>
<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\RG-package-2.png">
</p>
<br>
<br>
<br>
<p>
<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\RG-package-3.png">
</p>
<br>
<br>
<br>
<p>
<img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\RG-package-4.png">
</p></details>

&nbsp;

**6.** Click the button **Upgrade** underneath

Next, you will see the following notification, click the **Done** button, and soon you will receive an email message from Salesforce confirming that the package was upgraded:

<details><summary> >>> Click to see a screenshot <<< </summary>
<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\Managed-Package\upgrading.png">
</p></details>




&nbsp;

* * *

&nbsp;

#### Uninstalling the {{ company_name }} managed package

Follow the steps below if you need to uninstall the {{ company_name }} managed package from your Salesforce configuration:

**1\.** Log in to your Salesforce account (it must have Admin permissions in your Org)

**2\.** Open [Setup menu](https://help.salesforce.com/articleView?id=basics_nav_setup.htm&type=5) in Salesforce

**3\.** Enter *installed packages* in the **Quick find** field in the upper left corner of the page and select **Installed Packages**

**4\.** Find {{ company_name }} on the list of installed packages and click the **Uninstall** button next to it

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\uninstall_new.png" class="minimized">
</p>


&nbsp;

**5\.** Scroll down to the bottom of the page that appears and select the checkbox *Yes, I want to uninstall this package and permanently delete all associated components*, then click **Uninstall**

<p><img src="..\..\assets\images\Configuration-&-Settings\Admin-Settings-&-Actions\uninstall2.png" class="minimized">
</p>



&nbsp;
* * *
&nbsp;

#### Package Contents

Specific fields, classes, and components the {{ company_name }} package adds to your Salesforce configuration:

&nbsp;

<table>
    <colgroup>
        <col span="3">
        <col style="width:170px">
    </colgroup>
        <tr>
            <th>
                <p>Field</p>
            </th>
            <th>
                <p>Parent object</p>
            </th>
            <th>
                <p>Type</p>
            </th>
            <th>
                <p>API name</p>
            </th>
            <th>
                <p>Description</p>
            </th>
        </tr>
        <tr>
            <td>
                <p>Last Activity Date</p>
            </td>
            <td>
                <p>Lead</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Last_Activity_Date__c</p>
            </td>
            <td>
                <p>Field shows the last activity date for the Lead object. This field stores information about the date of the last activity in Email or Event.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Last Activity Date</p>
            </td>
            <td>
                <p>Opportunity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Last_Activity_Date__c</p>
            </td>
            <td>
                <p>Field shows the last activity date for the Opportunity object. This field stores information about the date of the last activity in Email or Event.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Last Activity Date</p>
            </td>
            <td>
                <p>Contact</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Last_Activity_Date__c</p>
            </td>
            <td>
                <p>Field shows the last activity date for the Contact object. This field stores information about the date of the last activity in Email or Event.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Last Activity Date</p>
            </td>
            <td>
                <p>Account</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Last_Activity_Date__c</p>
            </td>
            <td>
                <p>Field shows the last activity date for the Account object. This field stores information about the date of the last activity in Email or Event.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Last Inbound Email Date</p>
            </td>
            <td>
                <p>Lead</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Last_Inbound_Email_Date__c</p>
            </td>
            <td>
                <p>Field shows the last inbound Email date for the Lead object</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Last Inbound Email Date</p>
            </td>
            <td>
                <p>Opportunity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Last_Inbound_Email_Date__c</p>
            </td>
            <td>
                <p>Field shows the last inbound Email date for the Opportunity object</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Last Inbound Email Date</p>
            </td>
            <td>
                <p>Contact</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Last_Inbound_Email_Date__c</p>
            </td>
            <td>
                <p>Field shows the last inbound Email date for the Contact object</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Last Inbound Email Date</p>
            </td>
            <td>
                <p>Account</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Last_Inbound_Email_Date__c</p>
            </td>
            <td>
                <p>Field shows the last inbound Email date for the Account object</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Last Outbound Email Date</p>
            </td>
            <td>
                <p>Lead</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Last_Outbound_Email_Date__c</p>
            </td>
            <td>
                <p>Field shows the last outbound Email date for the Lead object</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Last Outbound Email Date</p>
            </td>
            <td>
                <p>Opportunity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Last_Outbound_Email_Date__c</p>
            </td>
            <td>
                <p>Field shows the last outbound Email date for the Opportunity object</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Last Outbound Email Date</p>
            </td>
            <td>
                <p>Contact</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Last_Outbound_Email_Date__c</p>
            </td>
            <td>
                <p>Field shows the last outbound Email date for the Contact object</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Last Outbound Email Date</p>
            </td>
            <td>
                <p>Account</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Last_Outbound_Email_Date__c</p>
            </td>
            <td>
                <p>Field shows the last outbound Email date for the Account object</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Needs Reply</p>
            </td>
            <td>
                <p>Opportunity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Needs_Reply__c</p>
            </td>
            <td>
                <p>Indicates Opportunities with an Inbound email as the last touch which was not replied</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Leed Needs Reply</p>
            </td>
            <td>
                <p>Lead</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Leed_Needs_Reply__c</p>
            </td>
            <td>
                <p>This field indicates Leads with Inbound email as the last touch without an answer</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Created By SCC</p>
            </td>
            <td>
                <p>Lead</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__CreatedBySCC__c</p>
            </td>
            <td>
                <p>Field-indicator on the Lead object which mark created by RevenurGrid objects</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Created By SCC</p>
            </td>
            <td>
                <p>Opportunity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__CreatedBySCC__c</p>
            </td>
            <td>
                <p>Field-indicator on the Opportunity object which mark created by RevenurGrid objects</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Created By SCC</p>
            </td>
            <td>
                <p>Contact</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__CreatedBySCC__c</p>
            </td>
            <td>
                <p>Field-indicator on the Contact object which mark created by RevenurGrid objects</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Created By SCC</p>
            </td>
            <td>
                <p>Account</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__CreatedBySCC__c</p>
            </td>
            <td>
                <p>Field-indicator on the Account object which mark created by RevenurGrid objects</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Created By SCC</p>
            </td>
            <td>
                <p>Case</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__CreatedBySCC__c</p>
            </td>
            <td>
                <p>Field-indicator on the Case object which mark created by RevenurGrid objects</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Created By SCC</p>
            </td>
            <td>
                <p>Activity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__CreatedBySCC__c</p>
            </td>
            <td>
                <p>Field-indicator on the Activity object which mark created by RevenurGrid objects</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>RG Status</p>
            </td>
            <td>
                <p>Opportunity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Status__c</p>
            </td>
            <td>
                <p>Revenue Guide Status text field for the Opportunity</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Booking Link</p>
            </td>
            <td>
                <p>User</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__BookingLink__c</p>
            </td>
            <td>
                <p>Static link for booking a meeting with a specific user</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Send Date</p>
            </td>
            <td>
                <p>Activity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__SendDate__c</p>
            </td>
            <td>
                <p>The actual date when an Email or Event invite was sent or received</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Sent</p>
            </td>
            <td>
                <p>Activity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Sent__c</p>
            </td>
            <td>
                <p>Indicates outbound Activities</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Thread Id</p>
            </td>
            <td>
                <p>Activity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__ThreadId__c</p>
            </td>
            <td>
                <p>Email Thread ID. It is added to perform <a href="../Configuring-Activities-Synchronization-Settings-rg/#automatic_saving_of_email_threads">auto-saving of emails in a thread</a></p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Internet Message Id</p>
            </td>
            <td>
                <p>Activity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__InternetMessageId__c</p>
            </td>
            <td>
                <p>Email Internet <a href="https://en.wikipedia.org/wiki/Message-ID">Message-ID</a>. Added to ensure there are no <a href="https://docs.revenuegrid.com/ri/fast/articles/Item-Deduplication-Mechanisms/#general_email_deduplication">duplicates</a> saved. Is also used to verify that the email was already sent or received, by matching this value with Mailbox analytics / Exchange or Gmail data</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Is Internal</p>
            </td>
            <td>
                <p>Activity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__IsInternal__c</p>
            </td>
            <td>
                <p>Indicates if an Activity is Internal (in-Org) or External (outside contacts)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Is Outbound</p>
            </td>
            <td>
                <p>Activity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__IsOutbound__c</p>
            </td>
            <td>
                <p>Indicates if an Activity is Outbound or Inbound</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Saved Manually AddIn</p>
            </td>
            <td>
                <p>Activity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__SavedManuallyAddIn__c</p>
            </td>
            <td>
                <p>Indicates whether this activity was logged manually via the Sidebar</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Inbound Emails Count</p>
            </td>
            <td>
                <p>Lead</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Inbound_Emails_Count__c</p>
            </td>
            <td>
                <p>Indicates the number of inbound Emails for the Lead object</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Inbound Emails Count</p>
            </td>
            <td>
                <p>Opportunity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Inbound_Emails_Count__c</p>
            </td>
            <td>
                <p>Indicates the number of inbound Emails for the Opportunity object</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Inbound Emails Count</p>
            </td>
            <td>
                <p>Contact</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Inbound_Emails_Count__c</p>
            </td>
            <td>
                <p>Indicates the number of inbound Emails for the Contact object</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Inbound Emails Count</p>
            </td>
            <td>
                <p>Account</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Inbound_Emails_Count__c</p>
            </td>
            <td>
                <p>Indicates the number of inbound Emails for the Account object</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Outbound Emails Count</p>
            </td>
            <td>
                <p>Opportunity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Outbound_Emails_Count__c</p>
            </td>
            <td>
                <p>Indicates the number of outbound Emails for the Opportunity object</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Outbound Emails Count</p>
            </td>
            <td>
                <p>Contact</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Outbound_Emails_Count__c</p>
            </td>
            <td>
                <p>Indicates the number of outbound Emails for the Contact object</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Outbound Emails Count</p>
            </td>
            <td>
                <p>Account</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Outbound_Emails_Count__c</p>
            </td>
            <td>
                <p>Indicates the number of outbound Emails for the Account object</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Last Meeting Date</p>
            </td>
            <td>
                <p>Lead</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Last_Event_Date__c</p>
            </td>
            <td>
                <p>Date of the latest Event for the Lead object</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Last Meeting Date</p>
            </td>
            <td>
                <p>Opportunity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Last_Event_Date__c</p>
            </td>
            <td>
                <p>Date of the latest Event for the Opportunity object</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Last Meeting Date</p>
            </td>
            <td>
                <p>Contact</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Last_Event_Date__c</p>
            </td>
            <td>
                <p>Date of the latest Event for the Contact object</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Last Meeting Date</p>
            </td>
            <td>
                <p>Account</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Last_Event_Date__c</p>
            </td>
            <td>
                <p>Date of the latest Event for the Account object</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Last Analytics Sync Date</p>
            </td>
            <td>
                <p>Lead</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Analytics_Last_Sync_Date__c</p>
            </td>
            <td>
                <p>Date of the latest Analytics Sync for the Lead object</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Last Analytics Sync Date</p>
            </td>
            <td>
                <p>Opportunity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Analytics_Last_Sync_Date__c</p>
            </td>
            <td>
                <p>Date of the latest Analytics Sync for the Opportunity object</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Last Analytics Sync Date</p>
            </td>
            <td>
                <p>Contact</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Analytics_Last_Sync_Date__c</p>
            </td>
            <td>
                <p>Date of the latest Analytics Sync for the Contact object</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Last Analytics Sync Date</p>
            </td>
            <td>
                <p>Account</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Analytics_Last_Sync_Date__c</p>
            </td>
            <td>
                <p>Date of the latest Analytics Sync for the Account object</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Meetings Count</p>
            </td>
            <td>
                <p>Lead</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Events_Count__c</p>
            </td>
            <td>
                <p>Number of Events for the Lead object</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Meetings Count</p>
            </td>
            <td>
                <p>Opportunity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Events_Count__c</p>
            </td>
            <td>
                <p>Number of Events for the Opportunity object</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Meetings Count</p>
            </td>
            <td>
                <p>Contact</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Events_Count__c</p>
            </td>
            <td>
                <p>Number of Events for the Contact object</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Total Meetings Count</p>
            </td>
            <td>
                <p>Account</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Total number of Events for the Account object</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Employees Engaged Count</p>
            </td>
            <td>
                <p>Lead</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Internal_Contacts_Count__c</p>
            </td>
            <td>
                <p>Number of internal employees engaged in communication with this Lead</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Employees Engaged Count</p>
            </td>
            <td>
                <p>Opportunity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Internal_Contacts_Count__c</p>
            </td>
            <td>
                <p>Number of internal employees engaged in communication with this Opportunity</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Employees Engaged Count</p>
            </td>
            <td>
                <p>Contact</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Internal_Contacts_Count__c</p>
            </td>
            <td>
                <p>Number of internal employees engaged in communication with this Contact</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Employees Engaged Count</p>
            </td>
            <td>
                <p>Account</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Internal_Contacts_Count__c</p>
            </td>
            <td>
                <p>Number of internal employees engaged with this Account</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>External Engaged Contacts Count</p>
            </td>
            <td>
                <p>Opportunity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__External_Contacts_Count__c</p>
            </td>
            <td>
                <p>External people engaged in this Opportunity communication</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Engaged Contacts</p>
            </td>
            <td>
                <p>Account</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__External_Contacts_Count__c</p>
            </td>
            <td>
                <p>Number of engaged Contacts</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>First Opened</p>
            </td>
            <td>
                <p>Activity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__First_Opened__c</p>
            </td>
            <td>
                <p>Date/Time the email was first opened</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Last Opened</p>
            </td>
            <td>
                <p>Activity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Last_Opened__c</p>
            </td>
            <td>
                <p>Date/Time the Email was last opened</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Inbound Emails Effort</p>
            </td>
            <td>
                <p>Lead</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Inbound_Emails_Effort__c</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>Inbound Emails Effort</p>
            </td>
            <td>
                <p>Opportunity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Inbound_Emails_Effort__c</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>Inbound Emails Effort</p>
            </td>
            <td>
                <p>Contact</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Inbound_Emails_Effort__c</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>Inbound Emails Effort</p>
            </td>
            <td>
                <p>Account</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Inbound_Emails_Effort__c</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>Outbound Emails Effort</p>
            </td>
            <td>
                <p>Lead</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Outbound_Emails_Effort__c</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>Outbound Emails Effort</p>
            </td>
            <td>
                <p>Opportunity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Outbound_Emails_Effort__c</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>Outbound Emails Effort</p>
            </td>
            <td>
                <p>Contact</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Outbound_Emails_Effort__c</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>Outbound Emails Effort</p>
            </td>
            <td>
                <p>Account</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Outbound_Emails_Effort__c</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>Events Effort</p>
            </td>
            <td>
                <p>Lead</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Events_Effort__c</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>Events Effort</p>
            </td>
            <td>
                <p>Opportunity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Events_Effort__c</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>Events Effort</p>
            </td>
            <td>
                <p>Contact</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Events_Effort__c</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>Events Effort</p>
            </td>
            <td>
                <p>Account</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Events_Effort__c</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>Effort Total Time</p>
            </td>
            <td>
                <p>Lead</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Total_Effort__c</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>Effort Total Time</p>
            </td>
            <td>
                <p>Opportunity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Total_Effort__c</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>Effort Total Time</p>
            </td>
            <td>
                <p>Contact</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Total_Effort__c</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>Effort Total Time</p>
            </td>
            <td>
                <p>Account</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Total_Effort__c</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>Email Opens Tracker ID</p>
            </td>
            <td>
                <p>Activity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Email_Opens_Tracker_ID__c</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>From</p>
            </td>
            <td>
                <p>Activity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__From_del__c</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>RG Score</p>
            </td>
            <td>
                <p>Opportunity</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__RG_Score__c</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>CanvasApp</p>
            </td>
            <td style="word-break: break-all">
                <p>CanvasAppSettings</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__CanvasApp__c</p>
            </td>
            <td>
                <p>Used for CanvasApp name</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>CanvasAppNameSpace</p>
            </td>
            <td style="word-break: break-all">
                <p>CanvasAppSettings</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__CanvasAppNameSpace__c</p>
            </td>
            <td>
                <p>Used for CanvasAppNameSpace name</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>ServerSyncTenantUrl</p>
            </td>
            <td style="word-break: break-all">
                <p>CanvasAppSettings</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__ServerSyncTenantUrl__c</p>
            </td>
            <td>
                <p>Used for Server Sync Tenant URL</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>RevenueGridTenantUrl</p>
            </td>
            <td style="word-break: break-all">
                <p>CanvasAppSettings</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__RevenueGridTenantUrl__c</p>
            </td>
            <td>
                <p>Used for Revenue Grid Tenant URL</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>Lead_Activity</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Lead_Activity</p>
            </td>
            <td>
                <p>Revenue Engage Lead Activity Widget</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>Lead_Activity_Trends</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Lead_Activity_Trends</p>
            </td>
            <td>
                <p>Revenue Engage Lead Activity Trends Widget</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>Lead_Overview</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Lead_Overview</p>
            </td>
            <td>
                <p>Revenue Engage Lead Overview Widget</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>Lead_Sequences</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Lead_Sequences</p>
            </td>
            <td>
                <p>Revenue Engage Lead Sequences Widget</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>Lead_Signals</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Lead_Signals</p>
            </td>
            <td>
                <p>Revenue Engage Signals for Leads</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>Lead_Connections</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Lead_Connections</p>
            </td>
            <td>
                <p>Revenue Engage Lead Connections Widget</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>Contact_Activity</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Contact_Activity</p>
            </td>
            <td>
                <p>Revenue Engage Contact Activity Widget</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>Contact_Activity_Trends</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Contact_Activity_Trends</p>
            </td>
            <td>
                <p>Revenue Engage Contact Activity Trends Widget</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>Contact_Overview</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Contact_Overview</p>
            </td>
            <td>
                <p>Revenue Engage Contact Overview Widget</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>Contact_Sequences</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Contact_Sequences</p>
            </td>
            <td>
                <p>Revenue Engage Contact Sequences Widget</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>Contact_Signals</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Contact_Signals</p>
            </td>
            <td>
                <p>Revenue Engage Signals for Contacts</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>Contact_Connections</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Contact_Connections</p>
            </td>
            <td>
                <p>Revenue Engage Contact Connections Widget</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>Contact_Engagement</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Contact_Engagement</p>
            </td>
            <td>
                <p>Revenue Engage Contact Engagement Widget</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>Account_Activity</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Account_Activity</p>
            </td>
            <td>
                <p>Revenue Engage Account Activity Widget</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>Account_Connections</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Account_Connections</p>
            </td>
            <td>
                <p>Revenue Engage Account Connections Widget</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>Account_Engagement</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Account_Engagement</p>
            </td>
            <td>
                <p>Revenue Engage Account Engagement Widget</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>Account_Signals</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Account_Signals</p>
            </td>
            <td>
                <p>Revenue Engage Signals for Accounts</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>Opty_RG_Activity</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Opty_RG_Activity</p>
            </td>
            <td>
                <p>Revenue Guide Activity Trends Widget for Opportunities</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>Opty_RG_Connections</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Opty_RG_Connections</p>
            </td>
            <td>
                <p>Opportunity Connections: People involved in communication, Sankey chart</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>Opty_RG_Engagement</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Opty_RG_Engagement</p>
            </td>
            <td>
                <p>Revenue Guide Engagement Widget for Opportunities: last touch, documents, roles, etc.</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>Opty_RG_Signals</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Opty_RG_Signals</p>
            </td>
            <td>
                <p>Revenue Guide Signals for Opportunities</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>Opty_RevenueGrid</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Opty_RevenueGrid</p>
            </td>
            <td>
                <p>Opportunity created using RG Email Sidebar</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>UserUI</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__UserUI</p>
            </td>
            <td>
                <p>Visualforce page that allows opening RG Email Sidebar in Salesforce</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>AdminUI</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__AdminUI</p>
            </td>
            <td>
                <p>Visualforce page that allows opening Revenue Grid Admin Page in Salesforce</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>RG_Pipeline</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__RG_Pipeline</p>
            </td>
            <td>
                <p>General Revenue Guide Pipeline (Opportunities) widget implemented as a general tab in the Sales app in Salesforce</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>RG_Pipeline_Waterfall</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__RG_Pipeline_Waterfall</p>
            </td>
            <td>
                <p>General Revenue Guide Pipeline Waterfall widget implemented as a general tab in the Sales app in Salesforce</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>RG_Pipeline_Flow</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__RG_Pipeline_Flow</p>
            </td>
            <td>
                <p>General Revenue Guide Pipeline Flow widget implemented as a general tab in the Sales app in Salesforce</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>RG_Send_Email_Lead</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__RG_Send_Email_Lead</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>RG_Send_Email_Opportunity</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__RG_Send_Email_Opportunity</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>RG_Send_Email_Contact</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__RG_Send_Email_Contact</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>RI_User_Mailbox_Config</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__RI_User_Mailbox_Config</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>RI_User_Salesforce_Config</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__RI_User_Salesforce_Config</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>RI_User_Additional_Config</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__RI_User_Additional_Config</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>RG_Log_Call_Lead</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__RG_Log_Call_Lead</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>RG_Log_Call_Contact</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__RG_Log_Call_Contact</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>RG_Signals</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__RG_Signals</p>
            </td>
            <td>
                <p>General Revenue Guide Signals widget, implemented as a general tab in the Sales app in Salesforce</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>RG_Forecast_Tracker</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Opty_RG_Engagement</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>RG_Forecast</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__RG_Forecast</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>RG_Team_Performance</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__RG_Team_Performance</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>RevenueGrid</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__RevenueGrid</p>
            </td>
            <td>
                <p>General Revenue Grid widget designed to be used as a general tab in Sales app in Salesforce. Is actually the whole RG web app, is opened on RE Planner.</p>
            </td>
        </tr>
        <tr>
            <td style="word-break: break-all">
                <p>Account_RevenueGrid</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Account_RevenueGrid</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>Accounts</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td style="word-break: break-all">
                <p>REVGRD__Accounts</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>RevenueInbox: Sales Activity report</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Dashboard</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>RevenueInbox: Sales Activity report enables the managers to see the activity statistics per each Sales Representative</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>RevenueInbox: Stalled opportunities</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Dashboard</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>RevenueInbox: Stalled opportunities report enables the managers to see the statistics on stalled opportunities</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Opportunity Last touch</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Report</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>Completed Events Last Week with Invitees</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Report</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>The number of meetings per Sales Representative held in the last 7 days</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Planned Events with Invitees</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Report</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>The number of meetings per Sales Representative planned for the next 7 days</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Opportunities that need reply</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Report</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>The list of Opportunities with an Inbound email as last touch and that lack answer</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Inbound Emails Last Week</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Report</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>The number of inbound Emails for each Sales Representative received in the last 7 days</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Activities per Sales Rep</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Report</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Activity statistics per each Sales Representative</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Opps older than 150d w/o activity 60d</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Report</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Opportunities created more than 150 days ago without any activity in the last 60 days</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Opportunities w/o planned Activity</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Report</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Opportunities without any planned Activity</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Opps closing next 30d w/o activity 7d</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Report</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Opportunities that are to be closed within next 30 days without any activity in the last 7 days</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Opps closing next 90d w/o activity 30d</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Report</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>Opportunities that are to be closed within next 90 days without any activity in the last 30 days</p>
            </td>
        </tr>
</table>

&nbsp;

#### Spring 2023 package updates

<table data-layout="default">
        <tr>
            <th>
                <p>Component Name</p>
            </th>
            <th>
                <p>Type</p>
            </th>
            <th>
                <p>Description</p>
            </th>
        </tr>
        <tr>
            <td>
                <p>Calendars</p>
            </td>
            <td>
                <p>Visualforce Page</p>
            </td>
            <td>
                <p>This is a brand new component.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ConfigApp</p>
            </td>
            <td>
                <p>Aura Component Bundle</p>
            </td>
            <td>
                <p>This is an upgraded component. It will be updated to the new version.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Home</p>
            </td>
            <td>
                <p>Lightning Page</p>
            </td>
            <td>
                <p>This is an upgraded component. It will be updated to the new version.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>DynamicCanvasApp</p>
            </td>
            <td>
                <p>Aura Component Bundle</p>
            </td>
            <td>
                <p>This is an upgraded component. It will be updated to the new version.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ConfigCmp</p>
            </td>
            <td>
                <p>Aura Component Bundle</p>
            </td>
            <td>
                <p>This is an upgraded component. It will be updated to the new version.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>All CallOuts</p>
            </td>
            <td>
                <p>List View</p>
            </td>
            <td>
                <p>This is a brand new component.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Disable InstantSyncTrigger</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td>
                <p>This is an upgraded component. It will be updated to the new version.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Next Step Updated</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td>
                <p>This is a brand new component.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Disable EventTrigger</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td>
                <p>This is a brand new component.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Disable TaskTrigger</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td>
                <p>This is a brand new component.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Disable OpportunityTrigger</p>
            </td>
            <td>
                <p>Custom Field</p>
            </td>
            <td>
                <p>This is a brand new component.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Update NextStepUpdated</p>
            </td>
            <td>
                <p>Flow Version</p>
            </td>
            <td>
                <p>This is a brand new component.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>CallOut</p>
            </td>
            <td>
                <p>Custom Object</p>
            </td>
            <td>
                <p>This is an upgraded component. It will be updated to the new version.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ClientId Config</p>
            </td>
            <td>
                <p>Custom Object</p>
            </td>
            <td>
                <p>This is an upgraded component. It will be updated to the new version.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Signals Report</p>
            </td>
            <td>
                <p>Custom Object</p>
            </td>
            <td>
                <p>This is an upgraded component. It will be updated to the new version.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Trigger Settings</p>
            </td>
            <td>
                <p>Custom Object</p>
            </td>
            <td>
                <p>This is an upgraded component. It will be updated to the new version.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Calendars</p>
            </td>
            <td>
                <p>Tab</p>
            </td>
            <td>
                <p>This is a brand new component.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Revenue Inbox for Salesforce</p>
            </td>
            <td>
                <p>Connected App</p>
            </td>
            <td>
                <p>This is an upgraded component. It will be updated to the new version.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SM003_Http</p>
            </td>
            <td>
                <p>Apex Class</p>
            </td>
            <td>
                <p>This is an upgraded component. It will be updated to the new version.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>TaskTriggerHandler</p>
            </td>
            <td>
                <p>Apex Class</p>
            </td>
            <td>
                <p>This is an upgraded component. It will be updated to the new version.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>OpportunityTriggerHandler</p>
            </td>
            <td>
                <p>Apex Class</p>
            </td>
            <td>
                <p>This is an upgraded component. It will be updated to the new version.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>EventTriggerHandler</p>
            </td>
            <td>
                <p>Apex Class</p>
            </td>
            <td>
                <p>This is an upgraded component. It will be updated to the new version.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>T013_TaskTest</p>
            </td>
            <td>
                <p>Apex Class</p>
            </td>
            <td>
                <p>This is an upgraded component. It will be updated to the new version.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>T012_Event</p>
            </td>
            <td>
                <p>Apex Trigger</p>
            </td>
            <td>
                <p>This is an upgraded component. It will be updated to the new version.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>T012_EventTest</p>
            </td>
            <td>
                <p>Apex Class</p>
            </td>
            <td>
                <p>This is an upgraded component. It will be updated to the new version.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>T014_Opportunity</p>
            </td>
            <td>
                <p>Apex Trigger</p>
            </td>
            <td>
                <p>This is an upgraded component. It will be updated to the new version.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>T013_Task</p>
            </td>
            <td>
                <p>Apex Trigger</p>
            </td>
            <td>
                <p>This is an upgraded component. It will be updated to the new version.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Config</p>
            </td>
            <td>
                <p>Apex Class</p>
            </td>
            <td>
                <p>This is an upgraded component. It will be updated to the new version.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SM007_postEvent</p>
            </td>
            <td>
                <p>Apex Class</p>
            </td>
            <td>
                <p>This is an upgraded component. It will be updated to the new version.</p>
            </td>
        </tr>
</table>