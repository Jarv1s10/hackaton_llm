# Introduction: How to Use the Add-In

&nbsp;

<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>
<div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>
<div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

Server-Side Integration ("*SSI*" onwards) brings all power of SAP Cloud or Customer seamlessly into your mailbox, making it easy for you to process data between your e-mail client running on any platform and SAP Cloud for Customer on several intuitive clicks. SSI data handling is performed fully automatically or selectively; the solution excludes the necessity to switch back and forth between applications and data copy-pasting.

&nbsp;

!!! note "Note"
    SSI is **not** a standalone application, it is an [Add-In installed in your MS Outlook App or on the Web version](../How-to-Open-C4C-SSI-Sidebar/), also available as a [Chrome Extension for Gmail](../Use-with-Gmail/). The Sidebar's look and functions are mostly identical on all platforms

&nbsp;

After [SSI has been installed for you](../How-to-Configure-Admin/):

- Server-Side Integration tabs appear in your SAP Cloud for Customer profile. [See this article](../How-to-Open-Your-C4C-SSI-Settings-Profile/) for complete information  
- Several custom categories and/or folders appear in your mail client:  
&nbsp;&nbsp;&nbsp;**A.** *SAP E-Mails* for e-mails  
&nbsp;&nbsp;&nbsp;**B.** *SAP Cloud for Customer* for calendar items  
&nbsp;&nbsp;&nbsp;**C.** *SAP Contacts*, *SAP Accounts*, *SAP Individual Customers* for Outlook Contacts  
&nbsp;&nbsp;&nbsp;**D.** *SAP Tasks* for Outlook Tasks  
- An SSI icon is added to your MS Outlook Desktop ribbon and MS Outlook on the Web context actions menu. The icon reads *"View context of SAP Cloud for Customer"*; in Outlook on the Web the SAP icon is available in the actions menu next to a viewed or composed e-mail  

&nbsp;

After you click on the icon in [MS Outlook Desktop ribbon](../How-to-Open-C4C-SSI-Sidebar/), in [Outlook on the Web context menu](../Open-in-Outlook-Web/), or in [Gmail web interface](../Use-with-Gmail/), you will see SSI Sidebar:



<details><summary>>>> Expand to see how to open SSI Sidebar <<<</summary>
<p>
<b>Outlook (Desktop) ribbon</b>
    <img src="..\..\assets\images\Start\icon_ribbon.png">
<br>
<br>
<b>Outlook.com / Office.com</b>
    See <a href = "..\Open-in-Outlook-Web\">this article</a>.
</p>
</details>



 &nbsp;



!!! tip "Tip"
    You can "zoom in" the Sidebar to make its text bigger the way you zoom in web pages. To do that, click on the Sidebar, press the *Control (Ctrl)* button and scroll the mouse wheel up. All Sidebar components will be expanded and slightly re-arranged.
    To accommodate the expanded controls in the Sidebar's pane, you can also stretch the Sidebar sideways: hover the cursor over the left-hand edge of the Sidebar so it looks like this **⇼**, then hold the left mouse button and stretch the Sidebar leftwards

&nbsp;



![](..\assets\images\Start\sidebar-explained.png)

&nbsp;

**1\.** The **Refresh** icon. Click this icon to actualize data in the Sidebar after [configuration updates](../How-to-Open-Your-C4C-SSI-Settings-Profile/)   
**2\.** Object card's header; the card is expanded for CRM data reference. To collapse a card, click on the header   
**3\.** Basic object card listing the record's key fields. The SAP objects are retrieved based on addresses in the e-mail's *To/CC* or *From* fields   
**4\.** The button **Show Related Items**: click it to view the [list of SAP Cloud for Customer items related to this object](../initial-search-and-applied-filters/)  
**5\.** The button **i Details**: click to view the [detailed card](../How-to-Use-C4C-SSI/#3_cards_detailed_view_for_instant_reference) that includes the all object fields  
**6\.** Another related Contact's card header, the card is collapsed. To expand a card, click on the header  
**7\.** Another related object, an Account retrieved based on an a Contact's association   
**8\.** The **📌** (Pin) icon in the Sidebar's header, used to define whether SSI Sidebar should be set for auto-opening (pinned) in the e-mail client  
**9\.** The **x** (Close) icon used to close the Sidebar. See [this article](../How-to-Open-C4C-SSI-Sidebar/) to learn how to open it again  
**10\.** The **⊕** (Add) icon used to create new SAP Cloud for Customer objects. See [this article](../Create-Records/) to learn how to use this function   
**11\.** The **⚙** (Menu) icon; the menu includes three items: **Profile**, **Force Sync**, **About**   

- Clicking on *Profile* opens SAP Cloud for Customer user account in web browser  
- Clicking on *About* displays the following information: SSI Cloud for Customer version and ID of the SAP tenant the logged in user belongs to  
- Clicking on *Force Sync* allows to initiate an [SSI Sync session](../C4C-SSI-Sync-Overview/) ahead of the standard 30 minute interval. This allows to reduce SAP saving span for Calendar items or composed e&#8209;mails to 2-3 minutes. Besides that, forcing is used to relaunch Sync after [resolving a sync issue](../Sync-Issues-Troubleshooting/)     

**12\.** The **....** (More Actions) icon that opens the extra actions menu. Presently, the menu contains the action *Open the object* directly in SAP Cloud for Customer. Use e-mail templates action will also be added to this menu  
**13\.** The **📌** (Pin) icon in an object's header, used to define the order of object cards on the list. Pinned cards go to the top in the Sidebar   
**14\.** The *Search* field with the icons **Filters** and **Perform search** next to it. See [this article](../Search-Records/) to learn how to use SSI SAP objects search    
**15\.** The button **Save this E-Mail**: click this button to save selected e-mail to SAP Cloud for Customer, linked to this object. See [this article](../Save-Dialog/) to learn more   



&nbsp;
&nbsp;

* * *

&nbsp;

### Key SSI features


&nbsp;

- **[Get Contextual Cloud for Customer Data](../initial-search-and-applied-filters/)**. SSI instantly brings relevant and actualized Cloud for Customer data for any selected e-mail, calendar item, contact, or task. This data is displayed right in your MS Outlook or Gmail next to a selected item; it includes the list of associated Cloud for Customer objects, related activities, and much more  
&nbsp;

*   **[Synchronize Contacts, Calendar, and Tasks](../What-Is-C4C-SSI/)**. Automatically synchronize your Contacts, Calendar items, and Tasks between Cloud for Customer and your e-mail client  

&nbsp;

*   **[Save E-Mails in Cloud for Customer](../Emails-Processing/)**. Save your business e-mails in Cloud for Customer [using e-mail client's integrated means (categories, folders, labels)](../Emails-Processing/#2_semi-automatic_saving_via_dedicated_folder) or via SSI Sidebar's [Save dialog](../Save-Dialog/), associating them with specified relevant records. Your e-mails will instantly appear in Cloud for Customer as e-mail objects; files attached to e-mails can also be [saved in Cloud for Customer along with them](../Emails-Processing/#saving_files_attached_to_e-mails_in_sap_c4c)  
&nbsp;

*   **[Create or Update Cloud for Customer Records Right From Your Inbox](../Create-Records/)**. Create or update a Cloud for Customer record of any type, including your custom ones, without leaving your e-mail application. For your convenience, SSI analyzes the contents of e-mails and pre-fills relevant fields on new records creation  
&nbsp;

*   **[Find Cloud for Customer Objects Quickly](../Search-Records/)**. Instantly find useful CRM data right from your mailbox for reference or linking: search through all relevant objects in your Org or objects of a specific type only  
&nbsp;

*   **Use It on Your Smartphone**. Via [two-way server-side synchronization](../C4C-SSI-Sync-Overview/) between Cloud for Customer and Exchange/Office 365, your mobile device is always up to date with CRM Contacts, Meetings, and Tasks. Modify any Contact and see it updated in Cloud for Customer, or save an important business e-mail from your MS Outlook mobile on a few taps  

&nbsp;

*   **[Tune It the Way You Want](../Customization-Settings-Addin/)**. SSI is easily customized to fit specific business needs: choose which Cloud for Customer objects and object fields you want to view and edit via the Sidebar, or which criteria should be applied on relevant records retrieval from Cloud for Customer. [Tailored Profile templates pre-configured by a Key user](../How-to-Open-Your-C4C-SSI-Settings-Profile/) can be applied in bulk for group of users that perform different roles in the CRM    

&nbsp;
* * *

&nbsp;

#### SSI User Interface Localizations

**Different language localizations** are available for our users. SSI interface, dashboards, and settings are available in 12 world languages. Refer to [this article](../configuring-localization/) for more information on SSI localization configuring.

* Chinese (Simplified, People's Republic of China)
* Czech (Czechia)
* Dutch (Netherlands)
* English (United States)
* French (France)
* German (Germany)
* Italian (Italy)
* Japanese (Japan)
* Polish (Poland)
* Portuguese (Brazil)
* Russian (Russia)
* Spanish (Spain)

&nbsp;
