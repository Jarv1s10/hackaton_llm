# Cloud for Customer SSI Synchronization: An Overview

&nbsp;

!!! tip "Tip"
    Also see [this article](../Add-In-vs-Sync/) for a functional comparison for SSI Sync Engine and SSI Add-In

&nbsp;

The core data synchronization *process* described in this article is not to be confused with the toggleable Cloud for Customer SSI *features*  – auto-saving (auto-syncing) of every new incoming/outgoing e-mail or events, or auto-saving of new messages in selected correspondence threads. These functions are carried out by this process and if synchronization is not [set up](../How-to-Configure-User/) or [is suspended](../Synchronization-Dashboard/) by the user or due to an error, these features will not work.

Cloud for Customer SSI Synchronization (SSI Sync) is a recurrent background (server-side) process of two-way data exchange between your e-mail account (on an MS Exchange, Office 365, or Gmail server) and your SAP Cloud for Customer account, that the tool performs 24/7 to maintain consistency between your e-mail/calendar items and their matching SAP Cloud for Customer objects, also considering your choices and actions in Cloud for Customer SSI Sidebar and your e-mail client (via the dedicated category or folder. Cloud for Customer SSI Sync does **not** depend on whether Cloud for Customer SSI Add-In is opened in your e-mail client. The data is transferred securely server-to-server over [EWS](http://docs.microsoft.com/en-us/previous-versions/office/developer/exchange-server-2010/dd877045(v%3Dexchg.140)) in the case of MS Exchange, or using [TLS](https://support.google.com/a/answer/2520500?hl=en)/[SSL](https://www.lifewire.com/tls-vs-ssl-4156306) in the case of Gmail, and over the official and secure SAP Cloud for Customer API to/from your SAP Cloud for Customer account.

By default, Cloud for Customer SSI Sync is performed every 30 minutes; it runs regardless of whether Cloud for Customer SSI Sidebar or MS Outlook/other supported e-mail client is opened or not, as server-to-server data exchange unnoticed by the users.
Since data exchange is carried out between your e-mail server and SAP Cloud for Customer server while your local e-mail client and the Sidebar only serve to display e-mail/calendar data and register your choices and actions, Cloud for Customer SSI Sync does not consume any noticeable amount of your local internet traffic.

The key aspects of synchronization process can be flexibly adjusted by the end users individually via [SAP Cloud for Customer Profiles](../Customization-Settings-Sync/), or by the local admin via [Admin settings](../How-to-Configure-Admin/). Synchronization can be [manually suspended or forced to run sooner than the next scheduled session](../Synchronization-Dashboard/). It may also get suspended due to errors and monitored for troubleshooting.

Maintaining data mirroring is based on tables of matching fields mapped between MS Exchange / Office 365 calendar items, Tasks, Contacts and corresponding SAP Cloud for Customer objects. These mapping tables are used to compare the values in matching fields and transfer updated values from e-mail server to SAP Cloud for Customer or vice versa, replacing old values in corresponding fields with actual ones. This ongoing data mirroring process has its specific exceptions and overriding patterns applied in certain cases as required by convenience of use considerations. Additionally, there are [custom sync adjustment options](../Customization-Settings-Sync/) which alter the general reciprocal mirroring principle according to users' preferences.

!!! note "Note"
    Unlike continuous mirror-syncing of MS Exchange / Office 365 calendar items, Tasks, Contacts, saving of e-mails is always a one-way MS Exchange → SAP Cloud for Customer process by definition, and it is performed only one time per e-mail
&nbsp;

Besides this core data mirroring process, synchronization sessions include several interrelated jobs: checking for E-Mails, Events, Tasks, Contacts assigned the *SAP Cloud for Customer* category, creation of SAP Cloud for Customer objects based on new e-mails or calendar items and user input, finding and linking of related records in SAP Cloud for Customer, deletion of a matching object if the procedure requires that (for example, removal from SAP Cloud for Customer of an event that got cancelled on the e-mail server).



!!! warning "Important"
    Some actions can only be performed via synchronization: saving of calendar items in SAP Cloud for Customer, saving of e-mail messages in *Compose mode*, saving of e-mails, contacts, or tasks by assigning them the *SAP Cloud for Customer* category or moving to the dedicated *SAP Cloud for Customer* folder. Additionally, due to the sync interval it may take up to 30 minutes for a corresponding record to appear in SAP Cloud for Customer after your performed either of these saving actions. However, please note that several other actions involving creation or updating of SAP Cloud for Customer records do not depend on synchronization, as they are performed by Cloud for Customer SSI Add-In immediately in SAP Cloud for Customer, e.g. saving e-mail messages using the Save button in [*Read mode*](../Emails-Processing/#read_mode_and_compose_mode_in_ms_exchange_office_365) or initial saving (creation) of calendar items in SAP Cloud for Customer

&nbsp;

#### Auto-linking of e-mail/event/task items created by sync

Another important aspect of synchronization is auto-linking of Task, E-Mail, or Event objects created in SAP Cloud for Customer by the Sync Engine. Created SAP Cloud for Customer objects which mirror your e-mail messages and calendar items get
automatically associated with a relevant Contact/Lead, or Account. This linking pattern is used both on auto-saving and user-initiated saving through custom category/dedicated MS Outlook folder. 

&nbsp;

#### Automatic creation of Contacts or Leads by Cloud for Customer SSI (Autoresolving)

Cloud for Customer SSI can automatically create required Leads or Contacts for meeting attendees whose addresses have not been registered in SAP Cloud for Customer previously (*unresolved meeting attendees*). The Calendar Event object created in SAP Cloud for Customer to [match](../Contacts-Handling/#special_patterns_applied_on_contacts_processing) the saved item will be linked to this Lead or Contact. Note that SSI will be lacking data to fill in auto-created Leads' or Contacts' key fields, so the users should populate these fields later via the [Sidebar](../Introduction/).

To request enabling of the Auto-resolving feature for your org, send a corresponding request to SAP Cloud for Customer, specifying if you would prefer Leads or Contacts to be auto-created for based on unresolved meeting attendees' addresses.

Note that e-mail addresses and domains blocklisted from syncing by an individual Cloud for Customer SSI user (e.g. personal contacts) or by the Org Admin will **not** be processed on Leads/Contacts auto-resolving by Cloud for Customer SSI for this user.

Optionally, Cloud for Customer SSI can also auto-create new Accounts to link the auto-created Leads or Contacts to in case there is no appropriate Account found by [Cloud for Customer SSI Initial Search](../initial-search-and-applied-filters/). These auto-created Accounts' names will be based on the corporate e-mail domain used in the business correspondence being saved. Later their specific details can be populated by the user.

&nbsp;
