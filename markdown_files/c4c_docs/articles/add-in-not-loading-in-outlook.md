# Add-In not Loading in MS Outlook, Troubleshooting Steps

&nbsp;

&nbsp;

This article provides basic troubleshooting guidance if the Add-In doesn't load in MS Outlook. Proceed with the following steps to investigate and resolve the issue.

&nbsp;

## Check Add-In status

1. Make sure the Add-In is installed by verifying its status in SAP Cloud for Customer. Go to **E&#8209;Mail Integration** > **Groupware Settings** > **Users**. Find and open the affected user, click the "Gear" button in the upper right corner and click **Check Add-in Status**

<p>
<img src= "..\..\assets\images\add-in-not-loading-in-outlook\1.png">
</p>

&nbsp;

2. Upon the check of the Add-In Status, you should obtain the following result messages:

<p>
<img src= "..\..\assets\images\add-in-not-loading-in-outlook\2.png">
</p>

&nbsp;

3. Log in to Exchange server Outlook Web Access (OWA) or open MS Office 365 account in a web browser and make sure Add-In is loading successfully

<p>
<img src= "..\..\assets\images\add-in-not-loading-in-outlook\4.png">
</p>

&nbsp;

* * *

&nbsp;

## Check the current MS Outlook version

If Add-In works in OWA but doesn't load in MS Outlook – check the current MS Outlook version and make sure the most recent updates are installed. Also, refer to additional information about versions on the Microsoft page [here](http://social.technet.microsoft.com/wiki/contents/articles/31133.outlook-and-outlook-for-mac-update-file-versions.aspx#A).

Try to install any other free Add-In from the MS Office store and check, if it works.

&nbsp;

* * *

&nbsp;

## Clear Add-In local storage

<p>
    <img src="..\..\assets\images\add-in-not-loading-in-outlook\inspect.png" style="width:36.37%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

<br>
<b>1.</b> Open SSI in your MS Outlook, right-click on the Add-In area and select **Inspect** in the contextual menu to open the **DevTools** window

* If nothing happens when you right-click on the Add-In area, alternatively, you can use **Microsoft Edge DevTools Preview**. [Get it in Microsoft Store](https://apps.microsoft.com/store/detail/microsoft-edge-devtools-preview/9MZBFRMZ0MNJ?hl=en-us&gl=us&rtc=2&source=lp&activetab=pivot%3Aoverviewtab) and refer to [this article](../capture-har-file/) to learn how to use it

<br><br><br>

* If none of the above options work, most likely the Add-In runs on Internet Explorer, so you need to use [**IEChooser**](https://learn.microsoft.com/en-us/office/dev/add-ins/testing/debug-add-ins-using-f12-tools-ie). To launch IEChooser:
    * Open [File Explorer](https://support.microsoft.com/en-us/windows/find-and-open-file-explorer-ef370130-1cca-9dc5-e0df-2f7416fe1cb1#WindowsVersion=Windows_10), copy the path *C:\Windows\System32\F12\IEChooser.exe*, paste it to the address field in the File Explorer window, and press **Enter** on the keyboard. Then proceed with steps as with Microsoft Edge DevTools

<br><br>

<b>2.</b> In the opened DevTools window, go to the **Application** tab

<p>
<img src= "..\..\assets\images\add-in-not-loading-in-outlook\application.png">
</p>

<br>

<p>
    <img src="..\..\assets\images\add-in-not-loading-in-outlook\storage.png" style="width:26.19%; display:inline-block; vertical-align:middle; margin-left:10px;float: right">
</p>

<br>
<b>3.</b> On the left-hand **Storage** pane, expand **Local Storage** and select the option that appeared below

<br><br><br>

<b>4.</b> Click the **&osol; Clear All** button to clear the Add-In local storage

<p>
<img src= "..\..\assets\images\add-in-not-loading-in-outlook\clear-all.png">
</p>

&nbsp;

* * *

&nbsp;

## Clear the MS Office cache

Sometimes changes to Add-In commands, such as the icon for a ribbon button or the text of a menu item, do not seem to take effect. Clear the MS Office cache of the old versions. Delete the content of folder *%LocalAppData%\Microsoft\Office\15.0\WEF* (for MS Office 2016, it would be 16.0) and restart MS Outlook.

&nbsp;

&nbsp;