---
description: How to obtain cached Microsoft Outlook web add-in manifests, compress them to archive, and forward to RG support team
---

# How to Obtain MS Outlook Add-in Manifests and Forward Them to the Support Team

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container"
        style="
        display: inline-block;
        height: 42px;
        width: 162px;
        padding: 5px 10px;
        background-color: #fff;">
        <img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" 
            style="
        	height: 100%;
            object-fit: contain;
            vertical-align: middle;">
</div>
<div class="container"
        style="
        display: inline-block;
        height: 42px;
        width: 163px;
        padding: 5px 10px;
        background-color: #fff;">
        <img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" 
            style="
        	height: 100%;
            object-fit: contain;
            vertical-align: middle;">
</div>

&nbsp;

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

In some cases, [{{ company_name }} support team](mailto:support@revenuegrid.com) can ask you to provide the cached MS Outlook web add-in manifests for the troubleshooting analysis. This will help our team to investigate and handle manifest-related issues promptly and efficiently.

!!! tip "Tip"
    Refer to [this Microsoft article](https://learn.microsoft.com/en-us/office/dev/add-ins/outlook/manifests) for more information regarding MS Outlook add-in manifests
    
&nbsp;

The following guide will help you to find the MS Outlook add-in manifests on your device, archive them, and forward to [{{ short_company_name }} support team](mailto:support@revenuegrid.com).

&nbsp;

***

&nbsp;

## 1. Find the folder containing MS Outlook add-in manifests 

MS Outlook add-in manifest is a particular file describing how the add-in integrates across Outlook clients. Manifests are stored locally on your device, so you can easily find and send them to the support team.

There are 2 ways how you can find MS Outlook add-in manifests. You can use either of them.

&nbsp;

### Option 1 – Using File Explorer

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\obtain-add-in-manifests\file-explorer.png" style="width:33.92%; display:inline-block; vertical-align:middle; margin-left:8px; float: right">
</p>

<p style="margin-left:5%">
<b>1.1.</b> Open <a href="https://support.microsoft.com/en-us/windows/find-and-open-file-explorer-ef370130-1cca-9dc5-e0df-2f7416fe1cb1#WindowsVersion=Windows_10">File Explorer</a> by clicking the <b>Folder</b> icon on the taskbar or the Start menu, or pressing the <b>Windows logo key + E</b> on your keyboard
<br><br><br>
<b>1.2.</b> Copy this path to the clipboard:
</p>
```
%userprofile%\AppData\Local\Microsoft\Office\16.0\Wef\
```
<br>
<p style="margin-left:5%">
<b>1.3.</b> Paste the copied path to the address field in the opened File Explorer window
</p>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\obtain-add-in-manifests\paste-explorer.png">
</p>

<br>
<p style="margin-left:5%">
<b>1.4.</b> Press <b>Enter</b> on the keyboard to go to the folder with the add-in manifests in File Explorer
</p>
&nbsp;

Alternatively, follow the steps described in **Option 2** below
&nbsp;

&nbsp;

### Option 2 – Using the Run command window

<p style="margin-left:5%">
<b>2.1.</b> Open the <a href="https://www.digitalcitizen.life/run-window-windows-7-why-use-it-anymore/"><b>Run</b> command window</a> by pressing the <b>Windows logo key + R</b> on your keyboard
<br><br><br>
<b>2.2.</b> Copy this path to the clipboard:
</p>
```
%userprofile%\AppData\Local\Microsoft\Office\16.0\Wef\
```
<br>

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\obtain-add-in-manifests\paste-run.png" style="width:52.78%; display:inline-block; vertical-align:middle; margin-left:8px; float: right">
</p>

<p style="margin-left:5%">
<b>2.3.</b> Paste the copied path to the <i>Open</i> field in the opened <b>Run</b> command window
<br><br><br><br><br><br><br>
<b>2.4.</b> Click <b>OK</b> to initialize the command that opens File Explorer and locates the folder with the add-in manifests in it
</p>

&nbsp;

&nbsp;

<b>3.</b> Once you perform the above actions, File Explorer will display the list of folders. The folder with the random ID name contains necessary MS Outlook add-in manifests. Copy this folder to the desktop so that you can take actions with it without any undesired impact on the original files

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\obtain-add-in-manifests\manifests-folder.png">
</p>

&nbsp;

***

&nbsp;

## 2. Compress the folder to archive

&nbsp;

!!! note "Note"
    [Compressing](https://en.wikipedia.org/wiki/Lossless_compression) your files to an [archive](https://en.wikipedia.org/wiki/Archive_file) ensures that the {{ short_company_name }} support team gets them intact and unchanged  

&nbsp;

To compress the folder to an archive, right-click the folder, and select **Send to** > **Compressed (zipped) folder**.

<p>
    <img src= "..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\obtain-add-in-manifests\compress.png">
</p>

&nbsp;

<p>
    <img src="..\..\assets\images\Using-SmartCloud-Connect\How-To-s\Troubleshooting\obtain-add-in-manifests\archive.png" style="width:26.72%; display:inline-block; vertical-align:middle; margin-left:8px; float: right">
</p>

A new zipped folder (archive) with the same name will be created in the same location.

&nbsp;

&nbsp;

!!! tip "Tip"
    If you face an issue where an archive is not being created, then rename the folder with the random ID name to any much shorter name and try to compress it once more

&nbsp;

***

&nbsp;

## 3. Forward the archive to {{ short_company_name }} support team

Forward the created archive containing the cached MS Outlook web add-in manifests to [{{ company_name }} support team](mailto:support@revenuegrid.com) in the reply or in a newly composed email message.