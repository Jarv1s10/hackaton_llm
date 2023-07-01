---
description: Detailed comparison of Desktop (MSI) and Cloud (Web) Implementations
search:
  exclude: true
---
# {{ product_name }} Desktop (MSI) and Cloud (Web) Implementations Compared  
  
**[the Desktop (.MSI) Implementation  is no longer supported]**

<br>

*[Productivity Package Home page](../../)*

<!--<i>For users of the Email Sidebar on:</i><br><br>-->
<!--<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>-->

<!--&nbsp;-->

<!--*2 min read*  -->

<!-- ShareThis BEGIN --> 
<!--<div class="addthis_inline_share_toolbox"></div>-->
<!-- End ShareThis --> 

<!--&nbsp;-->

<!--!!! warning "Important"-->
<!--    Note that Desktop (.MSI) implementation will be deprecated based on Microsoft technical updates. See [this article](../How-to-Install-and-Run-the-Desktop-MSI-implementation-MS-Outlook/#desktop_msi_planned_deprecation) for more information-->

<!--&nbsp;-->


<!--Besides the deployment differences summarized in [this table](../How-to-Install-and-Run-the-Solution-all-configurations/#a_less_recommended_option_is_installing_revenue_inbox_add-in_desktop_implementation_from_an_msi_file_windows_os_only), {{ product_name }} Desktop (.MSI) and Cloud (Web) versions have minor differences in their feature sets.-->

<!--### Cloud (Web) version features not present in the Desktop (.MSI) version-->

<!--*   Requires no installation, just needs to be enabled in [MS Exchange web admin panel](../Mass-Deployment-of-the-Add-In-Office-365/)-->
<!--*   Works in Outlook for Mac, or in Outlook on the Web (Outlook.com, Outlook.office.com) opened in a browser-->
<!--*   Native mobile Add-In support in Outlook for iOS or Android-->
<!--*   Allows inserting files as MS Outlook item attachments when creating new email or calendar items-->
<!--*   Salesforce sign-in should only be made once per account-->
<!--*   [Suggestions](../Context-Specific-Actions/) on creating new Tasks / Events based on [key phrases](http://www.microsoft.com/en-us/research/group/natural-language-processing/) retrieved from message body are displayed in **Smart Actions** bar > **More...** > **Observations**-->
<!--*   {{ product_name }} can be [*pinned*](../Sidebar-Pinning/) (fixed for auto-opening when an email or calendar item is selected or opened) in:-->
<!--    - Office 365 or C2R (click-to-run) Outlook 2016 or later for Windows  -->
<!--    - build *7668.2000* or later for users in the Current or Office Insider Channels  -->
<!--    - build *7900.xxxx* or later for users in Deferred channels), Outlook 2016 or later for Mac (version *16.13.503* or later), and Outlook Online (Outlook.live.com, Outlook.office.com)  -->
<!--*   Tracking of addresses listed in an email's *BCC* field by [Initial Search](../Initial-Search-and-Applied-Record-Filters/) can only be enabled in the Cloud (Web) implementation of {{ product_name }}-->

<!--&nbsp;-->

<!--### Desktop (.MSI) features not present in the Cloud (Web) version-->

<!--*   Only this {{ short_name }} implementation supports scenarios involving POP/IMAP and SMTP mail servers and working with MS Exchange 2013 mailboxes-->

<!--*   A drag and drop signature-to-contact processing mechanism was  implemented for this version; it allows to quickly populate a new Contact's fields by  selecting the signature of an email and then dropping it into {{ product_name }}. What fields can be extracted from a signature: -->
<!--      *First/Last name* -->
<!--      *Address* -->
<!--      *Title* -->
<!--      *Email* -->
<!--      *Phones (if multiple, assigned according to the Contact's phone fields order)* -->
<!--      *Account*-->

<!--*   {{ product_name }} can be [*pinned*](../Sidebar-Pinning/) (marked for auto-opening when an email is selected in the *Inbox*, *Sent*, or *Salesforce* folder) in:-->

<!--    * Office 365 or [C2R (Click-to-Run)](https://support.office.com/en-us/article/how-to-install-office-with-click-to-run-in-office-online-programs-1e7450bc-ab99-421c-a869-563468276552) Outlook 2016 or later for Windows (build *7668.2000* or later for users in the Current or Office Insider Channels, build *7900.xxxx* or later for users in Deferred channels)-->
<!--    * Outlook 2016 or later for Mac (version *16.13.503* or later)  -->

<!--    Can **not** be pinned in: Outlook 2016 and later set up with Windows Installer (after update *16.0.4738.1000*). Refer to [this article](https://www.itprotoday.com/office-365/determining-if-office-installation-click-run-or-not) to learn how to define if your MS Outlook installation is Click-to-Run or set up with Windows Installer.      -->

<!--*   Sidebar pinning state is separated for inspector and explorer Outlook window types. More details [here](../Sidebar-Pinning/#scc-desktop-msi-inspector-and-explorer-windows-pinning-separated)-->

<!--*   Sidebar pinning is also available for MS Outlook calendar-->

<!--*   MS Exchange 2013 full support (with [{{ short_name }} Add-In](../Introduction/))-->

<!--*   Minor limitation: this implementation requires periodic re-signing in to Salesforce (once every 2-3 days, depending on the local security settings)-->

<!--*   In this implementation, the *Log a Call* icon is put in [Smart Actions](../All-User-Actions-in-Add-In-Sidebar/#smart_actions)-->





<!--&#160;-->
<!-- &#160;-->