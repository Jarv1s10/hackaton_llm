# SSI Synchronization Errors

&nbsp;

&nbsp;

**[ This article is work-in-progress ]**

&nbsp;

&nbsp;

Synchronization error is a case, when synchronization becomes completely non-functional and no records can be synchronized.

!!! warning "Important"
    Do not confuse synchronization **error** and synchronization **issue**, when only specific records can not be synchronized

&nbsp;

### Synchronization errors examples

Synchronization error due to authentication issue on the Microsoft Exchange side:

<p>
<img src= "..\..\assets\images\sync-errors\1.png">
</p>

&nbsp;

Synchronization error due to issues on the SAP Cloud for Customer side:

<p>
<img src= "..\..\assets\images\sync-errors\2.png">
</p>

&nbsp;

* * *

&nbsp;

## Known synchronization errors

<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <p>Source</p>
            </th>
            <th>
                <p>Message</p>
            </th>
            <th>
                <p>Solution</p>
            </th>
        </tr>
        <tr>
            <td>
                <p>ExchangeConnector</p>
            </td>
            <td>
                <p>Authentication error</p>
            </td>
            <td>
                <p>Synchronization was disabled due to restricted access to your mailbox.<br />Probably your e-mail password was changed</p>
                <p>Here are two easy steps to make it work again:</p>
                <ul>
                    <li>
                        <p>Open <strong>SAP Cloud for Customer</strong> &gt; <strong>E-Mail Integration</strong> &gt; <strong>Sync Settings</strong> &gt; <strong>E-Mail Configuration</strong></p>
                    </li>
                    <li>
                        <p>Enter your new password and click the <strong>Save </strong>button</p>
                    </li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <p>ExchangeConnector</p>
            </td>
            <td>
                <p>Authentication error &ndash; OAuthRefreshToken might have expired</p>
            </td>
            <td>
                <p>In order to re-enable the synchronization, go to <strong>SAP Cloud for Customer</strong> &gt; <strong>E-Mail Integration</strong> &gt; <strong>Sync Settings</strong> &gt; <strong>E-Mail Configuration</strong> and update your Exchange authorization settings, and then re-enable the synchronization on the main page</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Synchronization engine</p>
            </td>
            <td>
                <p>A limit on the number of snapshot records is exceeded (10000/10040/0)</p>
            </td>
            <td>
                <p>The number of synced records exceeded the allowed limit. If the total amount of synchronized records exceeds the default 10000 records, the user may receive a such error message</p>
                <p>To resolve it, a user should adjust synchronization filters to reduce the number of synchronized records</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ExchangeConnector</p>
            </td>
            <td>
                <p>Unexpected Exchange error</p>
            </td>
            <td>
                <p>The request failed. The remote server returned an error: (404) Not Found &ndash; EWS URL &ndash; incorrect; use is not present</p>
                <p>The remote server returned an error: (403) &ndash; (additional investigation is needed) in case if it is not O365, then collect more information by <a href="https://testconnectivity.microsoft.com/">https://testconnectivity.microsoft.com</a></p>
                <p>The XML document ended unexpectedly &ndash; additional investigation is needed</p>
                <p>Organization &quot;<em>AUSPR01A001.PROD.OUTLOOK.COM/Microsoft Exchange Hosted Organizations/1111.onmicrosoft.com - AUSPR01A001.PROD.OUTLOOK.COM/ConfigurationUnits/1111.onmicrosoft.com/Configuration</em>&quot; is marked for removal &ndash; inform the customer about Microsoft disabling users Org, yet user e-mail can be inactive as well</p>
                <p>Unsupported property field URI type &ndash; check &quot;Server: Kerio Connect 9.0.3&quot; in the Exch datadump &ndash; inform the user that our product does not compatible with &quot;Kerio Connect&quot;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>C4CC Connector</p>
            </td>
            <td>
                <p>Remote server returned an error: (500) Internal server error</p>
            </td>
            <td>
                <p>Requires investigation on the SAP Cloud for Customer side</p>
            </td>
        </tr>
    </tbody>
</table>

<!-- Need to check the table: C4CC, ExchangeConnector, errors, etc.-->


&nbsp;

&nbsp;


