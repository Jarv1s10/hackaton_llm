# Server-Side Integration Logs

&nbsp;

&nbsp;

**[ This article is work-in-progress ]**

&nbsp;

&nbsp;

Server-Side synchronization writes logs for each user for every synchronization session, which can be used to investigate any issues related to the synchronization component of Server-Side Integration.

&nbsp;

## How to collect Server-Side Integration logs

### Requirements

To collect logs, the following requirements should be met:

1. You should have a **Key User** (administrator) SAP Cloud for Customer account
2. Know the **User** who is experiencing issues
3. Know the exact **date and time** when the issue occurred

&nbsp;

### Steps to proceed

1. Log in to SAP Cloud for Customer with Key User account
2. Go to **E-Mail Integration** > **Groupware Settings** > **Users**

<p>
<img src= "..\..\assets\images\ssi-logs\4.png">
</p>

&nbsp;

3. Search for an affected user by any convenient field, e.g. by *Name*, and open the user's page

<p>
<img src= "..\..\assets\images\ssi-logs\5.png">
</p>

&nbsp;

4. Go to the **Statistics** tab and find a sync session by date or status. Type in "*Error*" to the status field to filter out only failed sync sessions

5. In the *Actions* column, click the **Download Logs** button to download logs

<p>
<img src= "..\..\assets\images\ssi-logs\6.png">
</p>

&nbsp;

6. A pack of logs should be downloaded in a **.zip archive**, which can be investigated further to find the root cause of the issue

&nbsp;

* * *

&nbsp;

## Types of logs written by Server-Side Integration

SAP Cloud for Customer Server-Side Integration stores the following types of logs:

<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <p>Log name</p>
            </th>
            <th>
                <p>Description</p>
            </th>
            <th>
                <p>Log format</p>
            </th>
        </tr>
        <tr>
            <td>
                <p>
                    <strong>C4C Dump</strong>
                </p>
            </td>
            <td>
                <p>Contains an HTTP trace of synchronization session between SAP Cloud for Customer and Server-Side Integration connector</p>
            </td>
            <td>
                <p>.txt</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>
                    <strong>Configuration</strong>
                </p>
            </td>
            <td>
                <p>Contains a list of settings that were used during synchronization</p>
            </td>
            <td>
                <p>.xml</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>
                    <strong>Exchange Data Dump</strong>
                </p>
            </td>
            <td>
                <p>Contains data trace between the Server-Side Integration connector and Microsoft Exchange server and a list of actions performed in Exchange storage</p>
            </td>
            <td>
                <p>.xml</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>
                    <strong>Sync Dump</strong>
                </p>
            </td>
            <td>
                <p>Synchronization trace between 2 storages: SAP Cloud for Customer and Exchange</p>
            </td>
            <td>
                <p>.xml</p>
            </td>
        </tr>
    </tbody>
</table>

&nbsp;

The following additional information is also stored in the **.zip archive** along with logs:

* *autoresolvers.xml* – contains auto-resolver rules in case of synchronization conflict
* *Site.xml* – a list of settings
* *synchronization_scheme.xml* – mapping scheme for different object types
* *.json* – contains cached information for each object type to suppress synchronization, if some fields were updated on SAP Cloud for Customer, which is not used in synchronization
* *job.txt* – contains a list of all jobs, which were performed by connectors during synchronization


<!-- Need to clarify the list and types of logs/dump contained in .zip archive -->

&nbsp;

&nbsp;


