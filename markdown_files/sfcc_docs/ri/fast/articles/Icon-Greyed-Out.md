---
description: RGES Add-In's Icons are Greyed Out: How to troubleshoot this issue
---
# How to Resolve the Issue Where the Add-In's Icons are Greyed Out  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*1 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;


<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\icon-greyed-out\icon-greyed-out.png" style="width:35%; display:inline-block; vertical-align:middle; margin-left:5%;float: right">
</p>


If after [installing {{ short_name }} Add-In in MS Outlook](../How-to-Install-and-Run-the-Solution-all-configurations/), the "Open {{ product_name }}" icon and other associated icons in MS Outlook ribbon are greyed-out, unclickable, or unresponsive, that occured due to several reasons. This article describes the reasons for Add-In's icons greying out and possible ways to address this issue. 

<br>
<hr> 
<br>

## No email is selected 

{{ short_name }} Add-In's icons become clickable only if you have an email opened in your mail client. If no email is, the Add-In's icons are unclickable. 

First, **open an email** you want to save to Salesforce in your mail client, then **click on the {{ short_name }} Add-In icon** in the ribbon to open the Sidebar. 

<br> 
<hr> 
<br>
 

## Conflict with a COM (Component Object Model) MS Office add-in 


Another reason the Add-In's icons are greyed-out, unclickable, or unresponsive in MS Outlook ribbon is a conflict with a [COM (Component Object Model) MS Office add-in](https://blogs.msdn.microsoft.com/deva/2008/05/12/outlook-add-in-what-is-a-com-add-in-what-you-need-to-create-a-com-add-in/), e.g. *Adobe PDFMaker Office COM addin*, installed locally on your PC.


Microsoft prioritizes COM add-ins over [web Office add-ins](https://docs.microsoft.com/en-us/outlook/add-ins/). As a result, MS Outlook disables the {{ short_name }} Add-In when a conflict is detected. More information about that be found on [Stack Overflow](https://stackoverflow.com/questions/49058694/o365-add-ins-disabled-when-com-add-in-present/49160361#49160361).

If this is happening to you, to be able to use {{ product_name }}, try [removing the unused COM add-ins](https://support.office.com/en-us/article/view-manage-and-install-add-ins-in-office-programs-16278816-1948-4028-91e5-76dca5380f8d) from your MS Outlook setup. If this is not possible, you might consider using the [Desktop/MSI implementation](../Troubleshooting-Product-Desktop-MSI-Implementation/) of {{ product_name }}.


<br> 
<hr> 
<br>

## Disabled Reading Pane in MS Outlook 

<br>
The {{ product_name }} cannot be started, and the associated icons are greyed-out or unclickable in the MS Outlook ribbon if the [Reading Pane](https://support.microsoft.com/en-us/office/use-and-configure-the-reading-pane-to-preview-messages-2fd687ed-7fc4-4ae3-8eab-9f9b8c6d53f0#:~:text=To%20turn%20on%20or%20move,then%20select%20Right%20or%20Bottom.) is set to Off.  

<br>
<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\icon-greyed-out\reading-pane.png" style="width:45%; display:inline-block; vertical-align:middle; margin-left:5%;float: right">
</p>

**1\.** To enable the Reading Pane in MS Outlook 

**2\.** Switch to the **View** tab in the upper part of the Outlook interface  

**3\.** Next, in the **Layout** section click on **Reading Pane** 

**4\.** Select either **Right** or **Bottom** from the drop-down list 

**5\.** Next, open an email you want to save to Salesforce  

**6\.** Click on the {{ short_name }} icon in the ribbon to open the Sidebar 

 

&#160;
 &#160;

