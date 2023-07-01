# Searching for Relevant Cloud of Customer Records via the Sidebar  

&nbsp;

SAP Cloud for Customer [Server-Side Integration Add-In / Chrome Extension Sidebar](../Introduction/) allows the users to instantly find records of any type in your CRM to do a quick data check or to [save a business e-mail or calendar activity with](../Save-Dialog/).

!!! tip "Tip"
    See [this article](../Create-New-Records/) to learn how to create new Cloud for Customer records directly from your e-mail client using SSI

&nbsp;

### Searching for Records in Cloud for Customer ("user-initiated search")


With SAP Cloud for Customer SSI Add-in, you can easily search among all your Cloud for Customer records: Contacts, Accounts, Opportunities, Leads, Activities (Tasks and Calendar events), Support Cases, or any [custom Cloud for Customer object types peculiar to your Org](../How-to-Add-A-Custom-Object/).

To search for existing Cloud for Customer records, do the following:   

**1\.**  In the Cloud for Customer SSI Add-In/Google extension, click the search icon in the upper-right corner of the Sidebar, then enter your search criteria in the **Search in** box.   

!!! tip "Tip"
    After you click on the *Search In* box, you will see 5 records that you worked with recently

&nbsp;

**2\.**  In the drop-down list of record types, select the record type you want to search for. To search for records of all types, select **All Records**. The search results will be shown as record cards, also displaying the values in the [records' key fields](../How-to-Use-C4C-SSI/#3_cards_detailed_view_for_instant_reference) to make it possible to differentiate among similar records.  

!!! note "Note"
    You can search for records by parts of a word in records' key fields, but at least 3 characters must be entered in the Search field

&nbsp;
<!-- Animation doesn't exist
<details><summary>>>> Click to see an animation <<<</summary>
<p>
    <img src="..\..\assets\images\d33v4339jhl8k0cloudfrontnet\docs\assets\57398d2e903360669faf1f0a\images\5bd9fd9e04286356f0a54b30.gif">
</p>
</details>

&nbsp;
-->
&nbsp;

### Why an existing record might be absent in search results?

​    If you do not see a record you need in search results, make sure to check the following Cloud for Customer SSI customization settings for this object type:  
​    • The **Hide on search** setting  
​    • **Global search** and **Contextual search** filters  
​    • The **Search By** field  
​    • If searching for an item associated with an internal (in-org) e-mail address, also make sure that the **Include internal e-mails into search results** setting is enabled  

&nbsp;

