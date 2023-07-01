# How to Obtain SAP Cloud for Customer Metadata

&nbsp;

&nbsp;

In some cases, our support team can ask you to provide SAP Cloud for Customer metadata for the troubleshooting analysis.

Metadata is an *XML* data file, the main source of objects and fields configuration for Server-Side Integration. Inspection of field definitions in metadata can help our team to investigate and handle issues associated with discrepancies between SAP Cloud for Customer and Server-Side Integration.

!!! tip "Tip"
    Learn more about Metadata XML in [this Microsoft article](https://learn.microsoft.com/en-us/openspecs/office_file_formats/ms-qdeff/aef664f7-e00b-4683-9724-0dec509dc658)

&nbsp;

The following guide will help you to obtain SAP Cloud for Customer metadata for further analysis.

&nbsp;
***
&nbsp;

## Method 1 – obtain metadata directly from tenant

<br>
To obtain SAP Cloud for Customer metadata directly from the tenant, you need to open the corresponding Metadata URL in your web browser.

<p style="margin-left:2%">
    <br>
    <b>1.</b> Open SAP Cloud for Customer in your web browser
    <br><br>
    <b>2.</b> Copy the following part of the URL to the clipboard:
</p>

    /sap/c4c/odata/v1/c4codataapi/$metadata?sap-label=true

<p style="margin-left:2%">
    <br>
    <b>3.</b> Paste the copied part after your tenant URL in the web browser and press <b>Enter</b> on the keyboard to retrieve metadata. Example of the resulting URL:
</p>

<p style="margin-left:4%">
    <i>https://[your tenant URL]/sap/c4c/odata/v1/c4codataapi/$metadata?sap-label=true</i>
</p>

<br>

<p>
    <img src="..\..\assets\images\obtain-metadata\tenant.gif">
</p>

<p style="margin-left:2%">
    <br>
    <b>4.</b> Once the page is fully loaded, copy the SAP Cloud for Customer metadata and save it to a new <i>XML</i> file
</p>

&nbsp;
***
&nbsp;

## Method 2 – obtain metadata from sync logs

<br>
Another way to obtain SAP Cloud for Customer metadata is to extract it from the downloaded sync logs. Refer to [this article](../ssi-logs/) to learn how to collect Server-Side Integration logs.

!!! note "Note"
    To collect SSI logs, you need to have a **Key User** (administrator) SAP Cloud for Customer account

&nbsp;

Once you have downloaded the SSI logs, proceed with the following steps to extract SAP Cloud for Customer metadata:

<p style="margin-left:2%">
    <br>
    <b>1.</b> Open the downloaded logs and go to <b>Logs</b> > <b>C4C_Dump</b> > <b>ConnectorGeneric_0</b>
    <br><br>
    <b>2.</b> Open the <i>000_Initialize_c4codataapi.txt</i> file and find the logged metadata under <i>HTTP Response</i>
</p>

<details><summary>Click to see a screenshot</summary>
    <p>
        <img src="..\..\assets\images\obtain-metadata\logged.png">
    </p>
</details>

<p style="margin-left:2%">
    <br>
    <b>3.</b> Copy the SAP Cloud for Customer metadata and save it to a separate <i>XML</i> file
</p>

&nbsp;

!!! warning "Important"
    Please note that metadata is cached by the sync engine, so it might not be available in every sync log

&nbsp;

&nbsp;