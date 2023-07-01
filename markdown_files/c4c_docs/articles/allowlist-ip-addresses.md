# How to Allowlist the IP Addresses and Other Related Resources

&nbsp;

&nbsp;

**[ This article is work-in-progress ]**

&nbsp;

&nbsp;

To allowlist the product components correctly, it is necessary to perform the following steps:

1. [Determine the Scale Unit name](#determine_the_scale_unit_name)
2. Based on Scale Unit, [allowlist IP addresses of SAP Cloud for Customer Azure productive landscape](#allowlist_ip_addresses_of_sap_cloud_for_customer_azure_productive_landscape_for_corresponding_scale_unit)
3. [Allowlist the CDNs](#allowlist_the_cdns)

&nbsp;

## Determine the Scale Unit name

To determine the Scale Unit (SU) name, do the following actions:

1. Download <a href="..\..\assets\files\determine_su.zip" download> <strong>determine_su.zip</strong></a> and extract the **su.bat** file from it
2. Launch **su.bat**
3. In the opened window, enter tenant name in format "my######.crm.ondemand.com"
4. The tenant name will be displayed as follows:

<p>
<img src= "..\..\assets\images\allowlist-ip-addresses\1.png">
</p>

&nbsp;

In provided example Scale Unit name is "**fratest**"

&nbsp;

* * *

&nbsp;

## Allowlist IP addresses of SAP Cloud for Customer Azure productive landscape for corresponding Scale Unit

Once you find your Scale Unit name, you can find the IP address for allowlisting that corresponds to your Scale Unit in the following table:

### Productive landscape (IP Addresses)

<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <p>Location</p>
            </th>
            <th>
                <p>Scale Unit</p>
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

&nbsp;

* * *

&nbsp;

## Allowlist the CDNs

The CDNs are the same for all Scale Units, so you may use the list of CDNs below to allowlist the corresponding CDNs:

#### Add-In CDNs

* maxcdn.bootstrapcdn.com
* code.jquery.com
* cdnjs.cloudflare.com
* appsforoffice.microsoft.com
* unpkg.com
* cdnjs.cloudflare.com

&nbsp;

#### Server-Side Sync CDNs

* cdnjs.cloudflare.com
* fonts.googleapis.com
* maxcdn.bootstrapcdn.com
* cdn.jsdelivr.net
* ajax.googleapis.com

&nbsp;

#### Telemetry CDN

* az416426.vo.msecnd.net

&nbsp;

#### OAuth CDNs

* https://login.windows.net
* https://outlook.office365.com

&nbsp;

#### Other CDNs

* https://invisiblesolutions.com
* https://appsforoffice.microsoft.com/lib/1.1/hosted/office.js
* https//az416426.vo.msecnd.net/scripts/a/ai.0.js
* (customer's tenant URL)
* Customer EWS URL and JSON metadata URL's in case of on-prem Exchange

&nbsp;

&nbsp;
