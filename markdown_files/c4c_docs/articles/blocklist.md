# Blocklisted, Corporate, and Internal E-Mails and Domains Processing

&nbsp;

&nbsp;

SSI recognizes e-mail addresses and domains added to the **Blocklisted persons and domains** field, filters them out during the initial search, and prevents them from autosaving to SAP Cloud for Customer. However, users are able to save items sent to / received from blocklisted contacts manually via the Add-In search.

The **Blocklisted persons and domains** field is also used for blocklisting the internal e-mail addresses and domains. SSI automatically identifies and adds your corporate e-mail domain to this field, and it can not be removed either.

&nbsp;

Users and admins can manage the blocklist according to company or personal needs:

* Users can add and remove e-mails and domains to / from the **Blocklisted persons and domains** field located in **User Settings** > **Sync Settings** > **Detailed Settings**

<p>
<img src="../../assets/images/Initial_Search/blocklist1.png">
</p>

&nbsp;

<p>
    <img src="../../assets/images/Initial_Search/blocklist2.png" style="width:43.91%; display:inline-block; vertical-align:middle; margin-left:8px;float: right">
</p>

* Users can blocklist a person or domain directly from Add-In by clicking the <b>&middot;&middot;&middot;&middot;</b> (More) button on the object and selecting **Block this person** or **Block this e-mail domain** in the opened dialog

<br><br><br>

* Admins can manage the blocklisted e-mails and domains in **General Sync Settings** of [**User Profile**](../How-to-Configure-Admin/#22_configuring_user_profile_settings) that is being configured and assigned to users

&nbsp;

!!! note "Note"
    Note that users do not have permission to make changes to the blocklist managed by admin

&nbsp;

!!! warning "Important"
    If an e-mail is received from multiple senders, and only some of the e-mail addresses are on the blocklist, the e-mail will still be saved and linked to the records associated with the senders who are not blocklisted

&nbsp;

&nbsp;