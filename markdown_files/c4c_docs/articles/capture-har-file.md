# How to Capture Add-In Trace (HAR File) with Microsoft Edge DevTools Preview

&nbsp;

&nbsp;

In some cases, [our support team](https://support.sap.com/en/contact-us.html) can ask you to provide the captured SSI Add-In trace (HAR file) for the troubleshooting analysis. This article provides detailed instructions on how to capture the HAR file from the Outlook Add-In using Microsoft Edge DevTools Preview.

!!! tip
    Refer to [this Microsoft article](https://learn.microsoft.com/en-us/azure/azure-portal/capture-browser-trace) for more information on browser trace capturing

&nbsp;

***

## System requirements

To capture SSI Add-In trace (HAR file) from Outlook using **Microsoft Edge DevTools Preview**, your system must meet the following requirements:

* *Windows 10*, version **1903** or later ([how to check Windows version](https://support.microsoft.com/en-us/windows/which-version-of-windows-operating-system-am-i-running-628bec99-476a-2c13-5296-9dd081cdd808))
* *Office 365*, version **16.0.11629** or later ([how to check Outlook version](https://support.microsoft.com/en-us/office/what-version-of-outlook-do-i-have-b3a9568c-edb5-42b9-9825-d48d82b2257c))

<br>

If your system does not meet the above requirements, consult the table below, showing other tools for trace capturing:

#### List of tools for trace (HAR file) capturing on different systems

<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <p>OS / Platform</p>
            </th>
            <th>
                <p>Browser</p>
            </th>
            <th>
                <p>Tool for trace capturing</p>
            </th>
        </tr>
        <tr>
            <td>
                <p>Office on the web (OWA interface)</p>
            </td>
            <td>
                <p>The browser in which Office is opened</p>
            </td>
            <td>
                <p><em>Developer Tools</em> in the browser opened</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>macOS</p>
            </td>
            <td>
                <p>Safari</p>
            </td>
            <td>
                <p><a href="https://support.apple.com/guide/safari-developer/safari-developer-tools-overview-dev073038698/11.0/mac"><em>Developer Tools</em> in Safari</a></p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Windows / non-subscription Office 2013 or later</p>
            </td>
            <td>
                <p>Internet Explorer 11</p>
            </td>
            <td>
                <p><a href="https://www.telerik.com/fiddler"><i>Fiddler</i></a> / <a href="https://learn.microsoft.com/en-us/office/dev/add-ins/testing/debug-add-ins-using-f12-tools-ie#debug-a-task-pane-add-in-using-the-f12-tools"><i>IEChooser</i></a></p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Windows 10 ver. &lt; <b>1903</b> / Office 365</p>
            </td>
            <td>
                <p>Internet Explorer 11</p>
            </td>
            <td>
                <p><a href="https://www.telerik.com/fiddler"><i>Fiddler</i></a> / <a href="https://learn.microsoft.com/en-us/office/dev/add-ins/testing/debug-add-ins-using-f12-tools-ie#debug-a-task-pane-add-in-using-the-f12-tools"><i>IEChooser</i></a></p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Windows 10 ver. &GreaterEqual; <b>1903</b> /<br>
                Office 365 ver. &lt; <b>16.0.11629</b></p>
            </td>
            <td>
                <p>Internet Explorer 11</p>
            </td>
            <td>
                <p><a href="https://www.telerik.com/fiddler"><i>Fiddler</i></a> / <a href="https://learn.microsoft.com/en-us/office/dev/add-ins/testing/debug-add-ins-using-f12-tools-ie#debug-a-task-pane-add-in-using-the-f12-tools"><i>IEChooser</i></a></p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Windows 10 ver. &GreaterEqual; <b>1903</b> /<br>
                Office 365 ver. &GreaterEqual; <b>16.0.11629</b></p>
            </td>
            <td>
                <p>Microsoft Edge</p>
            </td>
            <td>
                <p><a href="https://apps.microsoft.com/store/detail/microsoft-edge-devtools-preview/9MZBFRMZ0MNJ?hl=en-us&gl=us&rtc=2&source=lp&activetab=pivot%3Aoverviewtab"><i>Microsoft Edge DevTools</i></a> /<br>
                <a href="https://docs.telerik.com/fiddler/configure-fiddler/tasks/usefiddlerasreverseproxy"><i>Fiddler</i> with loop back</a></p>
            </td>
        </tr>
</table>

<br>
***
<br>

## Install Microsoft Edge DevTools Preview app

To capture HAR files (logs) from Edge-engine running apps (such as Outlook on the desktop), you can use **Microsoft Edge DevTools Preview** app.

You can get the **Microsoft Edge DevTools Preview** app from the Microsoft Store via [this link](https://www.microsoft.com/store/productId/9MZBFRMZ0MNJ).

!!! tip
    The interface of *Microsoft Edge DevTools Preview* is similar to the *DevTools* interface in Edge or Chrome browsers

<br>
***
<br>

## Capture SSI Add-In trace (HAR file)

<p>
    <img src="..\..\assets\images\capture-har-file\local.png" style="width:31.61%; display:inline-block; vertical-align:middle; margin-left:10px;float: right">
</p>

1. Launch **Microsoft Edge DevTools Preview** and go to the **Local** tab

<br><br><br>

2. Launch your **Outlook** on the desktop and [open SSI Add-In](../How-to-Open-C4C-SSI-Sidebar/)
<br><br>

<p>
    <img src="..\..\assets\images\capture-har-file\refresh.png" style="width:30.4%; display:inline-block; vertical-align:middle; margin-left:10px;float: right">
</p>

3. Click the **Refresh** button in **Microsoft Edge DevTools Preview** to get actual network activity from the launched Add-In

<br><br>

4. Double-click on the appeared *SSI Add-In* debug target
<br><br>

<p>
    <img src="..\..\assets\images\capture-har-file\network.png" style="width:46.52%; display:inline-block; vertical-align:middle; margin-left:10px;float: right">
</p>

5. In the opened window, go to the **Network** tab

<br><br><br><br>

<p>
    <img src="..\..\assets\images\capture-har-file\start-stop.png" style="width:46.52%; display:inline-block; vertical-align:middle; margin-left:10px;float: right">
</p>

6. Check if logs recording is enabled (**Start** button is grayed out, and **Stop** button is active)

<br><br>

<p>
    <img src="..\..\assets\images\capture-har-file\clear-session.png" style="width:46.52%; display:inline-block; vertical-align:middle; margin-left:10px;float: right">
</p>

7. Click the **Clear Session** icon to remove collected traces

<br><br><br>

<p>
    <img src="..\..\assets\images\capture-har-file\console.png" style="width:46.52%; display:inline-block; vertical-align:middle; margin-left:10px;float: right">
</p>

8. Go to the **Console** tab

<br><br><br><br>

<p>
    <img src="..\..\assets\images\capture-har-file\clear.png" style="width:46.52%; display:inline-block; vertical-align:middle; margin-left:10px;float: right">
</p>

9. Click the **Trash Bin** icon to clear the Console logs

<br><br><br><br>

<p>
    <img src="..\..\assets\images\capture-har-file\location-reload.png" style="width:46.52%; display:inline-block; vertical-align:middle; margin-left:22px;float: right">
</p>

10. Insert the following command in the Console field and press **Enter** to execute it:

<!--commentary break to make the following copyable without an extra line-->

    location.reload()

<br>

!!! warning "Important"
    This is a necessary step before you start reproducing an issue
    
    <code>location.reload()</code> command makes Add-In restart without closing it. So after you reproduce an issue and save the HAR trace from Microsoft EDGE DevTools Preview, you get the complete picture of what was done
    
    Many issues have root causes popping up at the beginning of Add-In loading. And not always are such traces captured into logs without applying this command

<br>

11. Go to SSI Add-In in Outlook and execute the steps (actions) to reproduce an issue

12. Return to Microsoft EDGE DevTools Preview and go to the **Network** tab again

<p>
    <img src="..\..\assets\images\capture-har-file\export.png" style="width:46.52%; display:inline-block; vertical-align:middle; margin-left:10px;float: right">
</p>

13. Click the **Export as HAR** button to save the collected logs as *.har* file

<br><br><br><br>

Once you perform the above actions, forward the exported HAR file containing SSI Add-In trace to our support team for further analysis.

<br>
***
<br>

## Related resources

* [Download Microsoft EDGE DevTools](https://www.microsoft.com/en-us/p/microsoft-edge-devtools-preview/9mzbfrmz0mnj?rtc=2&source=lp&activetab=pivot:overviewtab)

* [Requirements for running Office Add-Ins](https://docs.microsoft.com/en-us/office/dev/add-ins/concepts/requirements-for-running-office-add-ins)

* [Browsers used by Office Add-Ins](https://docs.microsoft.com/en-us/office/dev/add-ins/concepts/browsers-used-by-office-web-add-ins)

&nbsp;

&nbsp;