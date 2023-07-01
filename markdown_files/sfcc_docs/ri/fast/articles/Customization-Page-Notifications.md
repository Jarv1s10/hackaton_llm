---
description: Detailed overview of Customization page notifications
---
# Customization Page Notifications Explained  
  

*3 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

### Success notifications

| Notification text                                            | Meaning / action to be taken                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Click "Save" to apply changes for card "{object name}".      | A reminder to save the changes made in a card.               |
| Default values restored successfully. Click Save to apply them. | Customization settings were reset, click Save to apply the change. |
| Customization imported successfully. Click Save to apply it. | Customization settings were imported, click Save to apply the change. |
| Successfully scheduled {{ product_name }} customization update. Close all MS Outlook windows to apply it. Note: {{ product_name }} may take 2-3 minutes to load after new settings were applied. | Customization settings will be updated.                      |
| Customization pushing has been scheduled; it may take between 5 and 60 minutes, depending on users count. Once it is completed, you will receive an email notification with the results. | Customization settings will be pushed to selected users.     |
| Customization from user "{username}" was loaded successfully. Click Save to apply it. | Customization settings have been received, click Save to apply them. |

&nbsp;

### General notifications

| Notification text                                            | Meaning / action to be taken                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| If Tasks are disabled, {{ product_name }} will not save emails in Salesforce, unless Enhanced Email objects are used in your configuration instead of Tasks. | Make sure that either Tasks or Email messages are enabled to be used for emails saving in Salesforce. |
| If Events are disabled, {{ product_name }} will not save calendar items in Salesforce. | Make sure that Events are enabled if you use calendar items saving (appointments, meetings, events). |
| Please select at least one user for customization pushing.   | Specify user(s) who will receive the customization settings. |
| A required field {field name} in {object name} that refers to {'or' separated Objects list} was selected. Add {'or' separated Objects list} to {{ product_name }} scope. See this article for more information. | Objects referenced in required fields must be enabled.       |

&nbsp;

### Warning notifications

| Notification text                                            | Meaning / action to be taken                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Page access token expired. Please reopen Customization page from the Add-In's menu. | Page access expired due to inactivity, page reopening required. |
| Not authorized; please reload the Add-In and reopen Customization page from its menu. | Page access expired due to inactivity, page reopening required to make any Customization settings changes. |
| Validation failed for {comma separated Objects list} objects. Please check and fill in all required fields in the central pane ('Objects in {{ product_name }}'). | Some of required fields on object cards are not filled, please define required fields' values. |
| Not all Salesforce forms are loaded for {comma separated Objects list}. Please hold up for a while. | Wait for the objects cards to load.                          |
| Not all Salesforce views are loaded for {comma separated Objects list}. Please hold up for a while. | Wait for the objects views (filters) to load.                |
| Customization changing not possible, check your permissions. If the issue persists, contact our Support team. | Cannot load data from Salesforce or error on Salesforce data processing. |
| Imported customization data is not valid. If unable to resolve the issue, contact our Support team. | A non-JSON file selected or JSON data corrupted or file does not contain settings data. |
| Version: {version} is not supported.                         | Not used (only version 1.0 is available)                     |
| An error occurred. Please reload the Add-In and reopen Customization page from its menu, then try again. If the issue persists, contact our Support team. | Appears on the following undefined server errors:<br />- Cannot retrieve user customization<br />- Cannot retrieve data from Salesforce<br />- Cannot reset customization to default values<br />Some server errors will be indicated specifically. |



&#160;
 &#160;

