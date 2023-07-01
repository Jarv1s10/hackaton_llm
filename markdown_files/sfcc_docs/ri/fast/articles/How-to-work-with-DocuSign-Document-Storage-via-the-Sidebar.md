---
description: The procedure of working with DocuSign Document Storage via the RG Email Sidebar
---
# Working with DocuSign Document Storage via the Sidebar  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*3 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

!!! note "Note"
    Presently, several {{ product_name }} user interface elements, e.g. the Sync settings, refer to *DocuSign* storage by its former name *SpringCM*

[DocuSign](http://www.springcm.com/products/document-management), a convenient and secure platform for document/contract storage and management, can be effectively accessed from the {{ product_name }} Add-In: after [setting up DocuSign](../Enabling-DocuSign-Integration-in-the-Sidebar/) you can directly upload and retrieve documents to/from the DocuSign storage in several mouse-clicks in the Sidebar.

!!! warning "Important"
    Please note that when you save the attached files by selecting them in the **Attachments** section in the Sidebar, the files attached to an email are saved in Salesforce, and not in DocuSign. Only the below described procedures are used to work with files stored in DocuSign

&nbsp;

!!! tip "Tip"
    Also refer to [this video guide](https://vimeo.com/266275462) to see how DocuSign integration works in {{ product_name }}

&nbsp;

### Save an Email's Attachment(s) to DocuSign

**1\.** With {{ product_name }} open, select the email containing the needed attachment(s) in MS Outlook

**2\.** In {{ product_name }}, open the relevant business record's [Detailed view](../All-User-Actions-in-Add-In-Sidebar/#5_improved_records_browsing_and_updating) by clicking **>** in its header, then click on the **Documents** tab

![](../assets/images/Using-SmartCloud-Connect/How-To-s/How-to-Store-and-Retrieve-File-Attachments-from-SpringCM/3.png)

&nbsp;

**3\. ** You will see the directories structure in your DocuSign storage. Click the **Upload Files** button at the top of the dialog

**4\.** In the _"Upload attachments to"_ dialog window that appears, select the attachment(s) you want to save in DocuSign by filling the corresponding checkboxes, then click **Next**

!!! note "Note"
    On the attachments list, there will also be the ["default attachment"](../Attachments-Handling-(Basic)/#the_default_attachment_eml_copy_of_an_email) – the email message rendered as an .eml file

   ![](../assets/images/Using-SmartCloud-Connect/How-To-s/How-to-Store-and-Retrieve-File-Attachments-from-SpringCM/5.png)

&nbsp;

**5\.** In the next *Save Attachments to DocuSign* dialog, navigate the directories structure and open the DocuSign folder where you want to save selected file(s) and click **Upload**

!!! note "Note"
    In the latest {{ product_name }} updates, the folder for attachments saving is set automatically – it's the root folder with the linked record's name

![](../assets/images/Using-SmartCloud-Connect/How-To-s/How-to-Store-and-Retrieve-File-Attachments-from-SpringCM/6.png)

&nbsp;



You will see a success toast notification "*Selected files were successfully uploaded to DocuSign*"

![](../assets/images/Using-SmartCloud-Connect/How-To-s/How-to-Store-and-Retrieve-File-Attachments-from-SpringCM/7.png)

&nbsp;

&nbsp;

### Attach a File Retrieved from DocuSign to an Email Message

!!! warning "Important"
    Attaching files stored in DocuSign to messages can only be done in [compose mode](../Saving-Emails-in-Salesforce-2.-Ways-to-Save-an-Email-(Adaptive-view)/)

**1\.** With {{ product_name }} open, compose a new email that you want to attach a file from DocuSign to, by clicking New Email, Reply/Reply all or Forward in MS Outlook 

**2\.** In {{ product_name }}, open the relevant business record's detailed view by clicking **>** in its header, then click on the **Documents** tab

**3\.** You will see the directories structure in your DocuSign storage that you will be able to navigate through; there will be a paperclip icon next to every file in it

   ![](../assets/images/Using-SmartCloud-Connect/How-To-s/How-to-Store-and-Retrieve-File-Attachments-from-SpringCM/4.png)

&nbsp;

**4\.** To retrieve a file from DocuSign and attach it to the message, click on the paperclip icon

&nbsp;

### DocuSign Integration Limitations

- There is a hard limit on the size of attached files being saved in DocuSign: 20 Mb max for the typical implementation.
- If your DocuSign storage has just been set up and contains no files, {{ product_name }} will not be able to work with it, displaying an error notification "It seems there are no related documents fount in DocuSign. They could be not generated yet, so please open this record and navigate to the tab with Documents, wait until they are loaded and then refresh {{ product_name }}. In case the issue persists, please contact your Salesforce administrator". In order to start working with it, please first [store any file in your DocuSign via Salesforce](https://www.springcm.com/video-tour-springcm-for-salesforce)

![](../assets/images/Using-SmartCloud-Connect/How-To-s/How-to-Store-and-Retrieve-File-Attachments-from-SpringCM/error.png)



&#160;
 &#160;


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
      margin-top: -80px;
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
<div class="banners banner-1">
  <img src="../../assets/images/banners/banner-1.svg" style="width: 100%; height: 100%;">
  <a class="button" href="https://revenuegrid.com/sign-up/?utm_source=kb_rg&utm_medium=referral&utm_campaign=eac&utm_content=banner" target="_blank">Sign up for a free trial</a>
</div>