# "Unable to Validate the Client Identity Token" Error when Starting Add-In

&nbsp;

&nbsp;

**[ This article is work-in-progress ]**

&nbsp;

&nbsp;

## Symptoms

1. When starting SSI Add-In the following error message is shown:

* "*Unable to validate the client identity token. Please restart the e-mail client*" or

<p>
<img src= "..\..\assets\images\identity-token\1.png">
</p>

&nbsp;

* "*Unable to load the identity token. Please restart Microsoft Outlook*"

<p>
<img src= "..\..\assets\images\identity-token\2.png">
</p>

&nbsp;

2. Customer is reporting that they cannot load the Add-In. It is saying "*Looks like your login session has expired. We will refresh it*" and then the Add-In is trying to load until it stops

<p>
<img src= "..\..\assets\images\identity-token\3.png">
</p>

&nbsp;

Restarting E-Mail client (MS Outlook) and resetting the MS Exchange password doesn't help.

&nbsp;

* * *

&nbsp;

## Causes

This issue is caused by a misconfiguration on the customer’s MS Exchange server\firewall. The identity token, which is used to authenticate a user in Add-In, contains an encoded Exchange MetaData URL, which is used to download Exchange meta-info and perform the validation process. Server-Side Integration is trying to connect to Exchange MetaData URL *https://somehost.com:443/autodiscover/metadata/json/1*, which is an internal resource in the customer’s network and can not be accessed from the internet.

&nbsp;

* * *

&nbsp;

## Resolution

To resolve the issue, it is required properly configure Identity Token URL on the MS Exchange server to make it available from external networks.

&nbsp;

Please note the items below to run SAP Cloud for Customer Server-Side Integration properly:

* Make sure the MetaData URL *https://somehost.com:443/autodiscover/metadata/json/1* (where *somehost.com* is an Exchange server external URL) is available from external networks or the firewall is set to allow the connection from IP addresses listed [below](#productive_landscape_ip_addresses). If there is any authentication enabled to access this URL, it should be disabled as well.  
For example, try accessing the same URL in Office 365 (*<https://outlook.office365.com/autodiscover/metadata/json/1>*), a similar response is expected.

* The Exchange server must accept incoming EWS (Exchange Web Services) calls from SAP Cloud for Customer Server-Side Integration. AutoDiscover may have to be set up. More details on AutoDiscover are available [here](https://learn.microsoft.com/en-us/previous-versions/office/exchange-server-2010/bb201695(v=exchg.141)).  
SAP Cloud for Customer Server-Side Integration IP addresses to authorize on the Exchange server side are documented [below](#productive_landscape_ip_addresses). Incoming EWS calls can be assessed for legitimacy by checking that they originate from within this IP range and contain a valid JWT (JSON Web Token). Details about JWT are available [here](https://docs.microsoft.com/en-us/outlook/add-ins/inside-the-identity-token).

* The Exchange server is configured to generate JWTs properly, so they indicate the URL SAP Cloud for Customer Server-Side Integration utilized to connect to the Exchange server. That URL may be the same as the AutoDiscover URL and is referred to as the MetaData URL in the JWT. If SAP Cloud for Customer Server-Side Integration still doesn’t work, a standard check to conduct is to review Certificates on the Exchange server and ensure their validity.

<!--The first sentence is kinda weird and complicated; what is the meaning?-->

* Make sure that EWS is properly configured to be available inside and outside of the organization by executing the following command:  
    * *C:\windows\system32>Get-WebServicesVirtualDirectory |Select name, \*url\* | fl*

* Exchange MetaData URL should be available from external networks, so if any proxy or firewall is used, make sure they are available from the internet.  

<!--Who are 'they' - URL(s) or proxy/firewall??-->

&nbsp;

## Productive landscape (IP Addresses)

<details><summary>>>> Click to see SSI IP addresses <<<</summary>

<br />
<strong>IP addresses of SAP Cloud for Customer Server-Side Integration</strong>
<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <p>Location</p>
            </th>
            <th>
                <p>SU</p>
            </th>
            <th>
                <p>Resource</p>
            </th>
            <th>
                <p>Main location</p>
            </th>
            <th>
                <p>List of PIPs in IP range</p>
            </th>
            <th>
                <p />
            </th>
            <th>
                <p>DR location</p>
            </th>
            <th>
                <p>List of PIPs in IP range</p>
            </th>
            <th>
                <p>Website (public DNS)</p>
            </th>
        </tr>
        <tr>
            <td>
                <p>WDC</p>
            </td>
            <td>
                <p>Wdcprod01</p>
            </td>
            <td>
                <p>web, worker</p>
            </td>
            <td>
                <p>
                    <a href="https://portal.azure.com/#@revenuegrid.com/resource/subscriptions/a112f56e-a5f0-489a-845c-d3cb60827d85/resourceGroups/Reserved-IP-Addresses/providers/Microsoft.Network/publicIPPrefixes/Reserved_IP_Addresses_CentralUS03/overview">40.89.246.90/31</a>
                </p>
            </td>
            <td>
                <p>40.89.246.90,<br />40.89.246.91</p>
            </td>
            <td>
                <p>Wdcprod-AKS<br />Wdcprod01</p>
            </td>
            <td>
                <p>
                    <a href="https://portal.azure.com/#@revenuegrid.com/resource/subscriptions/a112f56e-a5f0-489a-845c-d3cb60827d85/resourceGroups/Reserved-IP-Addresses/providers/Microsoft.Network/publicIPPrefixes/Reserved_IP_Addresses_EastUS02/overview">20.81.29.60/31</a>
                </p>
            </td>
            <td>
                <p>20.81.29.60,<br />20.81.29.61</p>
            </td>
            <td>
                <p>sapcfc-sap-wdcprod01-sync.c4c.invisiblesolutions.com</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>WDC</p>
            </td>
            <td>
                <p>Wdctest01</p>
            </td>
            <td>
                <p>web, worker</p>
            </td>
            <td>
                <p>
                    <a href="https://portal.azure.com/#@revenuegrid.com/resource/subscriptions/a112f56e-a5f0-489a-845c-d3cb60827d85/resourceGroups/Reserved-IP-Addresses/providers/Microsoft.Network/publicIPPrefixes/Reserved_IP_Addresses_EastUS01/overview">52.186.90.126/31</a>
                </p>
            </td>
            <td>
                <p>52.186.90.126,<br />52.186.90.127</p>
            </td>
            <td>
                <p>Wdctest-AKS<br />Wdctest01</p>
            </td>
            <td>
                <p>
                    <a href="https://portal.azure.com/#@revenuegrid.com/resource/subscriptions/a112f56e-a5f0-489a-845c-d3cb60827d85/resourceGroups/Reserved-IP-Addresses/providers/Microsoft.Network/publicIPPrefixes/Reserved_IP_Addresses_CentralUS04/overview">20.84.212.112/31</a>
                </p>
            </td>
            <td>
                <p>20.84.212.112,<br />20.84.212.113</p>
            </td>
            <td>
                <p>sapcfc-sap-wdctest01-sync.c4c.invisiblesolutions.com</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>WDC mod</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>
                    <a href="https://portal.azure.com/#@revenuegrid.com/resource/subscriptions/a112f56e-a5f0-489a-845c-d3cb60827d85/resourceGroups/Reserved-IP-Addresses/providers/Microsoft.Network/publicIPPrefixes/Reserved_IP_Addresses_EastUS03/overview">20.121.86.250/31</a>
                </p>
            </td>
            <td>
                <p>20.121.86.250;<br />20.121.86.251</p>
            </td>
            <td>
                <p />
            </td>
            <td>
                <p>
                    <a href="https://portal.azure.com/#@revenuegrid.com/resource/subscriptions/a112f56e-a5f0-489a-845c-d3cb60827d85/resourceGroups/Reserved-IP-Addresses/providers/Microsoft.Network/publicIPPrefixes/Reserved_IP_Addresses_CentralUS07/overview">52.228.162.70/31</a>
                </p>
            </td>
            <td>
                <p>52.228.162.70;<br />52.228.162.71</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>FRA</p>
                <p>FRA mod</p>
            </td>
            <td>
                <p>Fraprod01-05</p>
                <p>Fratest01</p>
                <p>Fratest21</p>
                <p>Fraprod21</p>
            </td>
            <td>
                <p>web, worker</p>
            </td>
            <td>
                <p>
                    <a href="https://portal.azure.com/#@revenuegrid.com/resource/subscriptions/33b1da52-153f-4025-a908-f06ecc770b17/resourceGroups/Reserved-IP-Addresses/providers/Microsoft.Network/publicIPPrefixes/Reserved_IP_Addresses_GermanyWestCentral01/overview">20.79.94.108/30</a><br>
                <br />
                <br />
                <br />
                </p>
                <p>
                    <a href="https://portal.azure.com/#@revenuegrid.com/resource/subscriptions/33b1da52-153f-4025-a908-f06ecc770b17/resourceGroups/Reserved-IP-Addresses/providers/Microsoft.Network/publicIPPrefixes/Reserved_IP_Addresses_GermanyWestCentral02/overview">20.79.101.104/30</a><br>
                <br />
                <br />
                <br />
                </p>
                <p>
                    <a href="https://portal.azure.com/#@revenuegrid.com/resource/subscriptions/33b1da52-153f-4025-a908-f06ecc770b17/resourceGroups/Reserved-IP-Addresses/providers/Microsoft.Network/publicIPPrefixes/Reserved_IP_Addresses_GermanyWestCentral03/overview">20.52.203.122/31</a><br>
                <br />
                </p>
                <p>
                    <a href="https://portal.azure.com/#@revenuegrid.com/resource/subscriptions/33b1da52-153f-4025-a908-f06ecc770b17/resourceGroups/Reserved-IP-Addresses/providers/Microsoft.Network/publicIPPrefixes/Reserved_IP_Addresses_GermanyWestCentral04/overview">20.79.89.96/30</a>
                </p>
            </td>
            <td>
                <p>20.79.94.108,<br />20.79.94.109,<br />20.79.94.110,<br />20.79.94.111</p>
                <p>20.79.101.104,<br />20.79.101.105,<br />20.79.101.106,<br />20.79.101.107</p>
                <p style="color:red;">20.52.203.122,<br />20.52.203.123</p>
                <p style="color:red;">20.79.89.96;<br />20.79.89.97;<br />20.79.89.98;<br />20.79.89.99</p>
                <p />
            </td>
            <td>
                <p>Fratest-AKS<br />Fratest01<br />Fraprod01<br />Fraprod&#8209;AKS</p>
                <p>Fraprod02<br />Fraprod03<br />Fraprod04<br />Fraprod05</p>
                <p>Fratest21<br>
                <br /></p>
                <p>Fraprod21</p>
            </td>
            <td>
                <p>
                    <a href="https://portal.azure.com/#@revenuegrid.com/resource/subscriptions/33b1da52-153f-4025-a908-f06ecc770b17/resourceGroups/Reserved-IP-Addresses/providers/Microsoft.Network/publicIPPrefixes/Reserved_IP_Addresses_WestEurope02/overview">20.50.236.104/30</a><br>
                <br />
                <br />
                <br />
                </p>
                <p>
                    <a href="https://portal.azure.com/#@revenuegrid.com/resource/subscriptions/33b1da52-153f-4025-a908-f06ecc770b17/resourceGroups/Reserved-IP-Addresses/providers/Microsoft.Network/publicIPPrefixes/Reserved_IP_Addresses_WestEurope03/overview">20.54.192.120/30</a><br>
                <br />
                <br />
                <br />
                </p>
                <p>
                    <a href="https://portal.azure.com/#@revenuegrid.com/resource/subscriptions/33b1da52-153f-4025-a908-f06ecc770b17/resourceGroups/Reserved-IP-Addresses/providers/Microsoft.Network/publicIPPrefixes/Reserved_IP_Addresses_WestEurope04/overview">51.105.215.150/31</a><br>
                <br />
                </p>
                <p>
                    <a href="https://portal.azure.com/#@revenuegrid.com/resource/subscriptions/33b1da52-153f-4025-a908-f06ecc770b17/resourceGroups/Reserved-IP-Addresses/providers/Microsoft.Network/publicIPPrefixes/Reserved_IP_Addresses_GermanyNorth01/overview">20.113.195.212/30</a>
                </p>
            </td>
            <td>
                <p>20.50.236.104,<br />20.50.236.105,<br />20.50.236.106,<br />20.50.236.107</p>
                <p>20.54.192.120,<br />20.54.192.121,<br />20.54.192.122,<br />20.54.192.123</p>
                <p style="color:red;">51.105.215.150,<br />51.105.215.151</p>
                <p style="color:red;">20.113.195.212; 20.113.195.213; 20.113.195.214; 20.113.195.215</p>
                <p />
            </td>
            <td>
                <p>sapcfc-sap-fraprod<strong>[01..05]</strong>-sync.c4c.invisiblesolutions.com</p>
                <p>sapcfc-sap-fratest01-sync.c4c.invisiblesolutions.com</p>
                <p>sapcfc-sap-fratest21-sync.c4c.invisiblesolutions.com</p>
                <p>sapcfc-sap-fraprod21-sync.c4c.invisiblesolutions.com</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>PER<br>
                <br /></p>
                <p><br>
                <br /></p>
                <p>PER mod</p>
            </td>
            <td>
                <p>Perprod01</p>
                <p>Pertest01</p>
            </td>
            <td>
                <p>web, worker</p>
            </td>
            <td>
                <p>
                    <a href="https://portal.azure.com/#@revenuegrid.com/resource/subscriptions/a112f56e-a5f0-489a-845c-d3cb60827d85/resourceGroups/Reserved-IP-Addresses/providers/Microsoft.Network/publicIPPrefixes/Reserved_IP_Addresses_AustraliaSoutheast01/overview">40.115.90.12/31</a><br>
                <br />
                </p>
                <p>
                    <a href="https://portal.azure.com/#@revenuegrid.com/resource/subscriptions/a112f56e-a5f0-489a-845c-d3cb60827d85/resourceGroups/Reserved-IP-Addresses/providers/Microsoft.Network/publicIPPrefixes/Reserved_IP_Addresses_AustraliaEast01/overview">20.53.187.192/31</a><br>
                <br />
                </p>
                <p>
                    <a href="https://portal.azure.com/#@revenuegrid.com/resource/subscriptions/a112f56e-a5f0-489a-845c-d3cb60827d85/resourceGroups/Reserved-IP-Addresses/providers/Microsoft.Network/publicIPPrefixes/Reserved_IP_Addresses_AustraliaSoutheast03/overview">20.70.88.90/31</a>
                </p>
            </td>
            <td>
                <p>40.115.90.12,<br />40.115.90.13</p>
                <p style="color:red;">20.53.187.192,<br />20.53.187.193</p>
                <p style="color:red;">20.70.88.90;<br />20.70.88.91</p>
            </td>
            <td>
                <p>PerProd-AKS<br />PerProd01</p>
                <p>Pertest-AKS<br />Pertest01</p>
            </td>
            <td>
                <p>
                    <a href="https://portal.azure.com/#@revenuegrid.com/resource/subscriptions/a112f56e-a5f0-489a-845c-d3cb60827d85/resourceGroups/Reserved-IP-Addresses/providers/Microsoft.Network/publicIPPrefixes/Reserved_IP_Addresses_AustraliaEast02/overview">20.193.1.176/31</a><br>
                <br />
                </p>
                <p>
                    <a href="https://portal.azure.com/#@revenuegrid.com/resource/subscriptions/a112f56e-a5f0-489a-845c-d3cb60827d85/resourceGroups/Reserved-IP-Addresses/providers/Microsoft.Network/publicIPPrefixes/Reserved_IP_Addresses_AustraliaSoutheast02/overview">13.70.173.238/31</a><br>
                <br />
                </p>
                <p>
                    <a href="https://portal.azure.com/#@revenuegrid.com/resource/subscriptions/a112f56e-a5f0-489a-845c-d3cb60827d85/resourceGroups/Reserved-IP-Addresses/providers/Microsoft.Network/publicIPPrefixes/Reserved_IP_Addresses_AustraliaEast03/overview">20.248.144.52/31</a>
                </p>
            </td>
            <td>
                <p>20.193.1.176,<br />20.193.1.177</p>
                <p style="color:red;">13.70.173.238,<br />13.70.173.239</p>
                <p style="color:red;">20.248.144.52;<br />20.248.144.53</p>
            </td>
            <td>
                <p>sapcfc-sap-perprod01-sync.c4c.invisiblesolutions.com</p>
                <p>sapcfc-sap-pertest01-sync.c4c.invisiblesolutions.com</p>
            </td>
        </tr>
    </tbody>
</table>
</details>

&nbsp;

### Related resources

[Getting Internal Server Error 500 when creating New-CsPartnerApplication for Exchange 2013](https://learn.microsoft.com/en-us/archive/blogs/jenstr/getting-internal-server-error-500-when-creating-new-cspartnerapplication-for-exchange-2013)

[Server to Server communication is broken – how to fix it?](https://digitalbamboo.wordpress.com/tag/metadatejson/)

&nbsp;

&nbsp;
