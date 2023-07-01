# Functions comparison: <br>SAP Cloud for Customer SSI Add-In app vs. SAP Cloud for Customer SSI sync engine  

&nbsp;

&nbsp;

| Component<br />Function                                      | MS Outlook/Office 365 Add-In app                             | Server-to-server synchronization engine                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| E-mails processing                                            | Save button: “manual” (selective) saving in [*Read mode*](../Emails-Processing/#read_mode_and_compose_mode_in_ms_exchange_office_365); saved by sync in *Compose mode* | Via the dedicated “SAP Cloud for Customer” folder or the custom SAP Cloud for Customer category |
| Calendar items processing                                    | Clicking the Save button in the side pane for a calendar item initiates its saving by sync, not by the Add-In; however, in this case special object linking can be set in the "Save event" dialog | By assigning the SAP Cloud for Customer category; automatic object linking is applied |
| Saving/syncing functions                                     | Single time one-way saving of e-mails in [*Read mode*](../Emails-Processing/#read_mode_and_compose_mode_in_ms_exchangeoffice_365)<br />Updating of details of already saved calendar items<br /> | Initial saving of calendar items<br /><br />Syncing of Contacts and Tasks<br />Saving of e-mails in Compose mode<br />Auto-saving |
| MS Outlook/O365 Contacts syncing                             |                                                              | Saving and then continuous mirroring of Contacts put in the SAP Cloud for Customer Contacts folder;  automatic objects linking is applied |
| MS Outlook/O365 Tasks syncing                                |                                                              | Saving and then continuous mirroring of Tasks assigned the SAP Cloud for Customer category; automatic objects linking is applied |
| Business objects creation in SAP Cloud for Customer          | User-initiated creation and creation of objects associated with e-mails saved in [Read mode](../Emails-Processing/#read_mode_and_compose_mode_in_ms_exchange_office_365) | Optional auto-creation for unresolved attendees              |
| Objects search in SAP Cloud for Customer                     | User-initiated search is conducted by the Add-In             | Auto-search of related Lead/Contact/Account to be auto-linked on items auto-saving |
| Initial search (Related records list collection)             | Conducts Initial Search; scans e-mails  subject, body, and signature; displays collected Related records list<br />Auto-fills objects' key fields based on retrieved relevant data | Auto-links objects according to established pattern          |
| Fully automatic saving of new e-mails, meetings, appointment<br />Selective automatic saving of e-mails | Selection of threads to be auto-saved using the Add-In's interface; however, saving itself is performed by the Sync Engine | All [auto-saving scenarios](../Emails-Processing/#3_automatic_saving_with_auto-save) are performed entirely by Sync |
| Attendees auto-resolving (automatic creation of relevant Leads or Contacts based on not yet processed e-mail addresses among synced meeting's attendees) |                                                              | Relevant Leads and Contacts, as well as Individual Customers and Accounts, can only be created by the Sync Engine |

&nbsp;

&nbsp;
