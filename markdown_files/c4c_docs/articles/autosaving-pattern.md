# How E-Mail and Event Automatic Saving (Autosharing) Works

&nbsp;

&nbsp;

**[ This article is work-in-progress ]**

&nbsp;

&nbsp;

The autosaving (autosharing) function helps you get all relevant e-mail messages and calendar events automatically saved to SAP Cloud for Customer. This article describes the core logic and pattern of the SSI autosaving process.

!!! note "Note"
    Autosaving runs with every synchronization session performed by SSI. Refer to [this article](../C4C-SSI-Sync-Overview/) for more information on SSI synchronization functions

&nbsp;

&nbsp;

## E-Mails autosaving

The following diagram describes the main pattern and logic of e-mail automatic saving to SAP Cloud for Customer by SSI.

<img src="../../assets/images/autosaving-pattern/4.svg" style="width:65%">

&nbsp;

* * *

&nbsp;

## Events autosaving

The autosaving of calendar event pattern is completely the same as e-mail autosaving. The difference is that the e-mail addresses are fetched from the participants' section for event autosaving, while for e-mail autosaving, the “To” field is used.

&nbsp;

&nbsp;