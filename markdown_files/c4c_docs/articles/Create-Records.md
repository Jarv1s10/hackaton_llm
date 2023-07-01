# How to Create SAP Cloud for Customer Objects Directly in SSI Add-In

&nbsp;

&nbsp;

Server-Side Integration allows you to create any business object or activity in your SAP Cloud for Customer directly in SSI Sidebar without leaving your mailbox. This article contains step-by-step guidance on how to create new SAP Cloud for Customer objects in the SSI Add-In in different ways.

&nbsp;

## Creating objects using the Add button

The basic option to create a new business object or activity is to use the **&CirclePlus;** (Add) button in the [SSI Sidebar's](../Introduction/) header:

1. Open Server-Side Integration Add-In in your mailbox

2. Click the **&CirclePlus;** (Add) button (1) and select the object type you need to create from the drop-down list (2)

<p>
<img src="../../assets/images/create-records/plus-button.png">
</p>

&nbsp;

!!! note "Note"
    The SAP objects listed in the drop-down list correspond to those enabled on the [Add-In Customization page](../Customization-Settings-Addin/)

&nbsp;

3. Enter all required object's details in the **Save {Object type}** dialog that appears

<p>
<img src="../../assets/images/create-records/save-individual-customer.png">
</p>

&nbsp;

4. Click **Save** to create the object in SAP Cloud for Customer

!!! warning "Important"
    Note that the required fields are highlighted on the object's creation card and are obligatory for filling

&nbsp;

&nbsp;

***

&nbsp;

## Creating objects via "Not Found in SAP" cards

The next option is to create Contact or Lead objects via "Not Found in SAP" cards shown in the Sidebar. SSI shows unknown record cards when no related objects were found in SAP Cloud for Customer during the [initial search](../initial-search-and-applied-filters/). To create the Contact or Lead object using the "Not Found in SAP" cards:

1. Open Server-Side Integration Add-In in your mailbox

2. Select or open an e-mail or event with representative(s) yet not saved to SAP Cloud for Customer and let SSI perform the initial search

3. Once the initial search is completed, SSI will show the unknown record card(s) in the Sidebar. Click the **Contact** or **Lead** button at the bottom of the card to initialize the object creation

<p>
<img src="../../assets/images/create-records/add-to-sap-as.png">
</p>

&nbsp;

4. In the opened **Save Contact** or **Save Lead** dialog, fill in the object details

<p>
<img src="../../assets/images/create-records/save-contact.png">
</p>

&nbsp;

5. Click **Save** to create the object in SAP Cloud for Customer

!!! note "Note"
    Note that the **Lead** object is disabled in the [Add-In Customization](../Customization-Settings-Addin/) by default. In order to make **Lead** object available in the Add-In, you need to enable it on the [Customization page](../Customization-Settings-Addin/)

&nbsp;

&nbsp;

***

&nbsp;

## Creating linked objects inside the object creation dialog

Also, SSI allows you to create a linked business object inside the object creation dialog in the Sidebar. For example, when creating a new Contact, you can create a new Account and link them right away.

1. Open Server-Side Integration Add-In in your mailbox

2. Start creating a new (primary) business object in the SSI Sidebar

3. Activate the linked object field (1), then select the required object type next to the *Create new* text (2) to initialize the creation of a new linked object (secondary)

<p>
<img src="../../assets/images/create-records/create-new-linked.png">
</p>

&nbsp;

4. Once you selected the linked object, the secondary object creation dialog appears

<p>
<img src="../../assets/images/create-records/save-account1.png">
</p>

&nbsp;

5. Fill in the object details and click **Save** to complete the creation of the linked object. Then you will be returned to the primary object creation dialog with the newly created object indicated in the linked object field

<p>
<img src="../../assets/images/create-records/create-new-linked2.png">
</p>

&nbsp;

6. Continue entering other details and click **Save** to complete the creation of the primary business object

&nbsp;

&nbsp;