---
description: How to clear MS Edge browser cache and cookies to refresh the Add-In
---
# Clearing MS Edge Browser Cache and Cookies to Refresh the Add-In  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

The general recommendations after adjusting {{ short_name }} [customization](../Customization-Settings-Explained/), [synchronization](../Configuring-Activities-Synchronization-Settings/), or [other](../Special-Admin-Panel-Settings/) settings are

- refresh the Sidebar by right-clicking on it and then selecting *Reload*
- close and reopen MS Outlook
- log out and then log back in {{ product_name }}

Normally, performing these actions is enough to refresh the Sidebar to apply the updated settings; however, in some cases clearing MS Edge cache and cookies may be additionally required.

MS Edge is used to render {{ product_name }} in MS Outlook on Windows systems. For this reason having MS Edge on your Windows system is a prerequisite for using the Add-In in your MS Outlook Desktop. Even if you do not use this browser, it is usually installed by default. Your MS Edge cache and cookies contain Sidebar rendering data; clearing the old data will refresh the Sidebar to reflect the changes in settings if other ways did not work out. In addition, cache and cookies clearing can help in certain rare cases of Sidebar interface elements being jumbled or displaying irrelevant data.

&nbsp;

* * *

&nbsp;

## To clear MS Edge WebView2 cache and cookies in your Windows system

<r>
!!! warning "Important"
    This instruction is intended only for the users of MS Edge WebView2, thus, make sure that,  [WebView2](https://developer.microsoft.com/en-us/microsoft-edge/webview2/) is installed on your device. To find out whether WebView2 is installed on your device, click on the **Windows icon** (Start button) in the Toolbar. Go to **Settings** > **Apps** > **Apps & Features**. In the *Search this list* field, enter WebView2 and check whether **WebView2 Runtime** is in the search results

<br><br>

**1\.** Close all MS Outlook windows

<br>
**2\.** Copy this path to the clipboard: 

        %LOCALAPPDATA%\Microsoft\Office\16.0\WEF\
<br><br>
<p><img src="..\..\assets\images\Configuration-&-Settings\User-Settings\clear-cache\1.png" style="width:45%; display:inline-block; vertical-align:middle; margin-left:1%;float: right" class="minimized"></p>

**3\.** Open **File Explorer** by clicking on the folder icon in the Toolbar


<br><br><br><br><br>
<p><img src="..\..\assets\images\Configuration-&-Settings\User-Settings\clear-cache\2.png" style="width:55%; display:inline-block; vertical-align:middle; margin-left:1%;float: right" class="minimized"></p>

**4\.** Paste the copied path to address field and press **Enter** on the keyboard 

<br><br><br><br><br><br><br>
<p><img src="..\..\assets\images\Configuration-&-Settings\User-Settings\clear-cache\3.png" style="width:55%; display:inline-block; vertical-align:middle; margin-left:1%;float: right" class="minimized"></p>
**5\.** Select the folder **webview2** and **delete** it. 
<br><br>
You can delete the folder by pressing Delete on the keyboard or right-clicking on the folder and selecting Delete from the drop-down menu

<br><br><br><br>
**6\.** Open MS Outlook 

**7\.** Select an email and click on the Add-In icon to start it 



<hr>



<style>
  .banners {
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .banners a.button {
      background-color: #FFC827;
      color: #2F3341;
      box-shadow: 0 5px 35px rgba(146, 146, 146, 0.2);
      padding: 20px;
      font-family: Graphic, arial;
      font-weight: 600;
      line-height: 24px;
      margin-top: -100px;
      border-radius: 3px;
      cursor: pointer;
      transition: .1s;
  }

  .banners a.button:hover {
    transform: scale(1.05);
  }

  .banners a.button a:hover,
  .banners a.button a:visited {
      color: #2F3341;
  }

  .banner-3 a.button {
    margin-left: 45%;
  }
</style>

<br>
<div class="banners banner-3">
  <img src="../../assets/images/banners/banner-3.svg" style="width: 100%; height: 100%;">
  <a class="button" href="https://revenuegrid.com/sign-up/?utm_source=kb_rg&utm_medium=referral&utm_campaign=eac&utm_content=banner" target="_blank">Try {{ company_name }} for free</a>
</div>