# Smart Description: How It Works

&nbsp;

&nbsp;

**[ This article is work-in-progress ]**

&nbsp;

&nbsp;

The notes area contains a combination of selected Smart Description fields and a free-text Notes section, separated by a delimiter (line of text “++++++++++++++++++++++++++++++++++”).

Smart Description fields are shown above the notes section, then goes separator and then Notes field value (if any).

&nbsp;

1. The Smart Description area is read-only (no changes to the fields are sent back to the server), and in case of changes on the MS Exchange/Google side, it will be reverted on the next synchronization to the server version

2. The free-text Notes section is editable and is synchronized with SAP Cloud for Customer notes bi-directionally

3. If the value is not set on the SAP Cloud for Customer side, just “*&lt;field name&gt;:*” is shown

4. Section format (separator and how fields name and values are shown) is not configurable by users and key users but can be done by Professional Services engagement

5. Smart Description area and delimiter do not appear on SAP Cloud for Customer as part of notes content

6. If the delimiter is completely deleted on the MS Exchange/Google side, all content of the notes area will be considered as note field value and will be synchronized to SAP Cloud for Customer notes. Then read-only Smart Description section will be re-created again with a delimiter

7. The list of fields shown in Smart Description is configurable by a key user or user. Any field available for a user with at least the view permission can be included

&nbsp;

!!! warning "Important"
    Enabling Smart Description **wouldn’t affect** already synced objects. Only objects created or updated after enabling Smart Description will be affected  
    To update objects already synced to MS Outlook, you need to **re-initialize** the user’s mailbox in Settings on the Admin panel

&nbsp;

&nbsp;