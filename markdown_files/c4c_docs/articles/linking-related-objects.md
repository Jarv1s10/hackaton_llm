# Saving E-Mail, Appointment, Visit, Phone Call via Add-In. How Linking Related Objects Works?

&nbsp;

&nbsp;

**[ This article is work-in-progress ]**

&nbsp;

&nbsp;

Linking related objects by SAP Cloud for Customer Server-Side Integration is based on other SSI processes, such as the **initial search** of records in SAP Cloud for Customer and applied **filters** during the initial search. Refer to [this article](../initial-search-and-applied-filters/) for more information on SSI initial search and applied record filters.

&nbsp;

The key points describing the logic of linking related objects while saving E-Mails, Appointments, Visits, or Phone Calls via SSI Add-In are the following:

* The objects retrieved during "Initial search" (parsing) are displayed in the Add-In

* Saving an E-Mail (Appointment, Visit, Phone Call) to one of the objects retrieved during the initial parsing would also link this E-Mail to **all of the retrieved objects** automatically

* Saving an E-Mail (Appointment, Visit, Phone Call) to an object that was searched manually (the object was not retrieved by SSI initial search) would link this E-Mail to the manually searched object **PLUS** all objects retrieved by the initial search

* The behavior (pattern) of the linking related objects is **not customizable**

* The linking related objects works identically for saving via **compose mode** and **read mode**

&nbsp;

&nbsp;