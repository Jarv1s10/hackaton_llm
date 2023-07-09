---
description: Learn how to pin your RG Email Sidebar in your configuration of MS Outlook
---
# {{ product_name }} pinning mechanics explained  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

[{{ short_name }} Add-In](../Introduction/)'s Sidebar can be “pinned” on the right-hand side of MS Outlook user interface next to processed emails in both Desktop and [Outlook on the Web](https://en.wikipedia.org/wiki/Outlook_on_the_web) implementations. “Pinning” means set to be opened automatically for emails or calendar items viewed or composed by the users. Automatic Sidebar opening is MS Outlook Calendar is only available in the customized [{{ product_name }} MSI (Desktop) version](../Desktop-MSI-and-Cloud-Web-Implementations-Comparison/).

[{{ short_name }} Outlook Add-In's Sidebar](../All-User-Actions-in-Add-In-Sidebar/) **can** be pinned for emails in the following configurations of MS Outlook:

- Office 365 [C2R (Click-to-Run)](https://support.office.com/en-us/article/how-to-install-office-with-click-to-run-in-office-online-programs-1e7450bc-ab99-421c-a869-563468276552) Outlook 2016 or later for Windows (build  *7668.2000* or later for users  in the Current or Office Insider Channels, build *7900.xxxx* or later for  users in Deferred channels)  
- Outlook 2016 or later for Mac (version *16.13.503* or later)  
- *Outlook.office.com* or *Outlook.com* or *Outlook.live.com* opened in your web browser; in this configuration the most efficient way to interact with {{ product_name }} is to [fix its icon for quick viewing](../Open-in-Outlook-Web/#how_to_fix_the_open_scc_icon_in_outlook_on_the_web_interface)  
- In [MS Outlook for Mac](../How-to-Install-the-Solution-in-MS-Outlook-for-Mac/) and [{{ product_name }} MSI implementation](../Desktop-MSI-and-Cloud-Web-Implementations-Comparison/) {{ product_name }} pinning works in a basic manner (no separation for inspector and explorer windows)  

&nbsp;

The Sidebar **cannot** be pinned for emails in:
 
- MS Outlook Desktop versions earlier than 2016 build *7668.2000*  

Thus it should be opened by clicking the **Open {{ product_name }}** icon in Outlook ribbon for every selected email or calendar item.

&nbsp;

&nbsp;

## {{ short_name }} Cloud Implementation: inspector and explorer windows pinning state separated



Separate Outlook Sidebar pinning mechanisms are used in two different view modes explained below. If the Sidebar is pinned for automatic opening in one mode, it will **not** be auto-opened in another mode.





 These types are:

**1\.** *Inspector* MS Outlook view: when an email is selected in the *Inbox* or *Sent* folder and displayed in MS Outlook main pane  

**2\.** *Explorer* MS Outlook view: when an email is opened in a separate window by double-clicking on it or by composing a new email, a replying, or forwarding  

This separation allows the end users to set Sidebar pinning according to their preferences in different contexts.

!!! tip "Tip"
    If you close the Sidebar by clicking the **x** icon in its upper right corner, the actual pinning state will be lost

&nbsp;

&nbsp;

## [{{ short_name }} for Gmail and Salesforce Chrome Extension](../Chrome-Extension-Intro/)'s Sidebar pinning

Due to Gmail web user interface Sidebar rendering peculiarities, in Gmail interface there is no special pin function: the {{ short_name }} Extension's Sidebar is either opened or closed.



&#160;
 &#160;

