---
description: Activities linking patterns in Salesforce and RGES explained 
---
# Activities Linking Patterns in Salesforce  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>
<div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>
<div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*4 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

**[this article is work-in-progress]**

&nbsp;

&nbsp;

&nbsp;

According to the basic [Salesforce Activities](https://help.salesforce.com/articleView?id=activities.htm&type=5) linking principles:

- By default, a [Task](https://developer.salesforce.com/docs/atlas.en-us.sfFieldRef.meta/sfFieldRef/salesforce_field_reference_Task.htm) object mirroring [an email you've saved](../Saving-Emails-in-Salesforce-1.-Function-Overview/) can be linked to a single [Business record](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) via the *Related To* field and to a reasonable number of [People records](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) via the *Name* field. If your Org is using [EmailMessages](https://help.salesforce.com/articleView?id=emailadmin_enhanced_email_considerations.htm&type=5) instead (Enhanced Email feature enabled), this object type can be linked to a reasonable number of [People and Business records](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/), both via the *Related To* field. If a Lead is linked to an email, no other People or Business records can be linked
- An [Event](https://developer.salesforce.com/docs/atlas.en-us.sfFieldRef.meta/sfFieldRef/salesforce_field_reference_Event.htm) can be linked to several [Business records](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) via the *Related To* field and to a reasonable number of [People records](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) via the *Name* field. For internal (in-org) meeting attendees, Salesforce creates copies of Event objects.
- All saved Activities (emails and calendar items) except ones linked to a Lead **must** be linked to an Account. This mandatory pattern is based on a Salesforce requirement, see Salesforce Help [article](https://help.salesforce.com/articleView?id=000336268&type=1&mode=1) for more information

&nbsp;


&nbsp;

* * *

&nbsp;

## Emails linking patterns

{{ product_name }} can save [MS Outlook](../Saving-Emails-in-Salesforce-1.-Function-Overview/) and [Gmail emails](../Using-the-Solution-for-Salesforce-and-Gmail/#saving_emails_in_salesforce) as completed [Salesforce Tasks](https://developer.salesforce.com/docs/atlas.en-us.sfFieldRef.meta/sfFieldRef/salesforce_field_reference_Task.htm) or as [EmailMessages](https://developer.salesforce.com/docs/atlas.en-us.sfFieldRef.meta/sfFieldRef/salesforce_field_reference_EmailMessage.htm) (if [Enhanced Email](https://help.salesforce.com/articleView?id=emailadmin_enhanced_email_considerations.htm&type=5) is enabled in your Org).

Note that if [Allow creating duplicated emails in Salesforce](../Item-Deduplication-Mechanisms/#allow_creating_email_duplicates_in_salesforce) is enabled in [{{ product_name }} Customization settings](../Customization-Settings-Explained/), you can get the resulting Task or EmailMessage linked to any reasonable number of [People and Business records](https://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/), by allowing {{ product_name }} to create several duplicates of it in Salesforce; each of these duplicates will be linked to a specific record, thus working around the limiting rules.



### Saved as Tasks

!!! tip "Tip"
    Also see the cases described in [this article](../Save-Email-Dialog/#special_considerations_what_combinations_of_records_can_be_linked_to_saved_emails)

&nbsp;

A Salesforce Task based on a saved MS Outlook or Gmail email can be linked to a reasonable number of [People records](https://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) and [Business records](https://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/).


&nbsp;

#### Quick-saved as Tasks

If you use the **Quick save** icon located in a record card's header in the [Sidebar](../Introduction/) to save an email as a Salesforce Task ([Enhanced Email](https://help.salesforce.com/s/articleView?id=sf.emailadmin_enhanced_email_considerations.htm&type=5) not enabled), the resulting Task will be linked to this record only.



&nbsp;

### Saved as EmailMessages

!!! tip "Tip"
    Also see the cases described in [this article](../Save-Email-Dialog/#special_considerations_what_combinations_of_records_can_be_linked_to_saved_emails)

A Salesforce EmailMessage that matches an email saved via {{ product_name }} can be linked to a reasonable number of [People records](https://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) and to a single [Business record](https://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/).

&nbsp;

#### Quick-saved as EmailMessages

If you use the Quick save icon located in a record card's header in the [Sidebar](../Introduction/) to save an email as a Salesforce EmailMessage ([Enhanced Email](https://help.salesforce.com/s/articleView?id=sf.emailadmin_enhanced_email_considerations.htm&type=5) enabled), the resulting EmailMessage will be linked to all eligible records associated with addresses included in the email's *To*, *From*, *CC* fields.


&nbsp;

### Opportunities linking on emails auto-saving

On [email auto-saving scenarios](../Configuring-Activities-Synchronization-Settings/#automatic_saving_of_emails_emails_autosharing), a related Opportunity gets linked to the resulting Task only if the following conditions are satisfied:

- [Link to Opportunities is enabled in Sync settings](../Configuring-Activities-Synchronization-Settings/#linking_to_opportunities)
- The email gets auto-saved with a Contact that has the Contact Role in the Opportunity

&nbsp;

* * *

&nbsp;

## Events linking patterns

A Salesforce Event that matches a meeting saved via {{ product_name }} can be linked to a reasonable number of [People records](https://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) and to a single relevant [Business record](https://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/).

!!! note "Note"
    {{ product_name }} also offers a unique optional possibility to link multiple [Business Records](https://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) to Events saved in Salesforce [via {{ short_name }} Sync](../Synchronization-Engine-An-Overview/); this function is not available in Salesforce out-of-the-box.   
    This feature requires [{{ company_name }} Salesforce managed package installation](../Admin-Managed-Package/) and can be enabled for our  customers upon request

&nbsp;

#### In-org attendees

For all in-org (internal) meeting attendees Salesforce creates copies of the [Event object](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_objects_event.htm?search_text=event) synced via {{ product_name }}, as child Events under the organizer's parent Event.

&nbsp;

&nbsp;

## Linking on [Auto-Saving](../Autosaving-Patterns/#events_auto-saving) or Saving via Category/Folder

Also see the general related records retrieval pattern described in [this article](../Initial-Search-and-Applied-Record-Filters/#the_resulting_related_records_list_will_include).

&nbsp;

* * *

&nbsp;

## Linking via the Save dialog

When saving an email or calendar item via the Save button in [{{ product_name }}](../Introduction/), you can select [People and Business records](http://www.sfdcpoint.com/salesforce/difference-between-whoid-and-whatid/) to be linked to it in Salesforce in the Save email/Save event dialog. See [this article](../Save-Email-Dialog/) for more information. The dialog automatically controls what set of records can be linked to the saved item, based on your actual configuration. For details, refer to the below table:

&nbsp;



| [Allow creating  duplicates](../Item-Deduplication-Mechanisms/#allow_creating_email_duplicates_in_salesforce) setting | [Enhanced Email](https://help.salesforce.com/articleView?id=emailadmin_enhanced_email_overview.htm&type=5)   (saving email directly) | A Lead already linked                        | User adds a Business record   ([WhatId](https://www.forcetalks.com/salesforce-topic/what-is-the-difference-between-whoid-and-whatid-how-can-we-associate-the-task-with-the-salesforce-opportunity-using-whatid)) | A Business record already linked ([WhatId](https://help.salesforce.com/articleView?id=emailadmin_enhanced_email_overview.htm&type=5)) | Meeting has multiple attendees | User adds a Contact   ([WhoId](https://www.forcetalks.com/salesforce-topic/what-is-the-difference-between-whoid-and-whatid-how-can-we-associate-the-task-with-the-salesforce-opportunity-using-whatid)) | User adds a Lead   ([WhoId](https://www.forcetalks.com/salesforce-topic/what-is-the-difference-between-whoid-and-whatid-how-can-we-associate-the-task-with-the-salesforce-opportunity-using-whatid)) | A Contact already linked                            | Notification |
| ----------------------------------------------------- | --------------------------------------------- | ----------------------------------------------------- | ---------------------------------- | -------------------------------- | ---------------------- | --------------------- | --------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| Enabled                                               | any                                           | any                                                   | any                                | any                              | any                    | any                   | any                         | any                                                        | None |
| Disabled                                            | Enabled                                   | any                                                   | Yes                               | Yes                             | any                    | any                   | any                         | any                                                        | Cannot link several  Business records in your config |
| Disabled                                             | Enabled                                      | any                                                   | Either  one or none                | any                              | any                    | any                   | any                         | No                                                        | None |
| Disabled                                            | Disabled                                     | Yes                                                  | any                                | any                              | any                    | any                   | any                         | any                                                        | Lead selected,  cannot link more objects             |
| Disabled                                             | Disabled                                     | No                                          | Yes                               | Yes                             | any                    | any                   | any                         | any                                                        | Cannot link several  Business records in your config |
| Disabled                                            | Disabled                                     | No                                            | Either  one or none                | Yes                             | any                    | any                   | any                         | No                                                        | None |
| Disabled                                             | Disabled                                     | No                                       | Either  one or none                | No                              | At least one           | Yes                  | Contact is already selected | Contact already  selected, cannot link more People records | None |
| Disabled                                             | Disabled                                     | No                                           | Either  one or none                | No                              | Either  one or none    | No                   | No |                                                            | None |

&nbsp;

&#160;

