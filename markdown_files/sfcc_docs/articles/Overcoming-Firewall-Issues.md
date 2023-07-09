---
description: Learn how to configure the corporate firewall to get the product running
---

# How to Configure the Corporate Firewall to Get the Product Running


<p style="font-size:15px"><i>2 min read - updated few hours ago</i> </p>
<!-- ShareThis BEGIN -->
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis -->
<br>

Some network environments are locked down via Firewall and allow connecting only to allowed IP addresses/domains from within their corporate networks.

The table below lists IPs and domains which must be reachable from your local network for proper operation of automated sequences and guided selling components of Revenue Grid.

<div class="admonition attention">
<p class="admonition-title">Prerequisite</p>
<p>Within the scope of configuring your corporate Firewall for proper functioning of Revenue Grid, as a prerequisite you have to allow certain destinations related to other component, Revenue Grid Email Sidebar. <a href="https://docs.revenuegrid.com/ri/fast/articles/Set-up-Salesforce-Auth/">Refer to this article for the list of IPs and domains</a></p>
</div>

End users' devices should be able to reach the destinations mentioned in the table below through TCP/443 (HTTPS)

<table>
    <thead>
        <tr>
			<th><b>Destination</b></th>
            <th><b>Details</b></th>
        </tr>
    </thead>
    <tbody>

        <tr>
           <td>*revenuegrid.com
           </td>
    
           <td>Revenue Grid user interface. Should lead to Revenue Grid instance <br> <br>API for sequenced emailing functionality of Revenue Grid Sales Engagement component. Should lead to Sales Engagement instance</td>
       </tr>
       
        <tr>
           <td>52.173.139.99,<br>
           52.173.188.229,<br>52.173.184.127,<br>52.173.186.243,<br>52.173.190.95,<br>52.176.107.202,<br>52.173.184.202,<br>52.173.190.226,<br></td>
           <td>Sequenced outbound email automation<br>Engagement Campaigns<br>Sales Engagement<br></td>
       </tr>
       
        <tr>
           <td>23.99.196.180,<br>168.61.185.160,<br>168.61.178.14,<br>23.99.133.3,<br>104.43.130.88,<br>168.61.153.98,<br>168.61.165.70,<br>168.61.188.249<br></td>
           <td>Revenue Signals<br></td>
       </tr>
       
        <tr>
           <td>40.119.56.217<br></td>
           <td>Indexer<br></td>
       </tr>
       <tr>
           <td>Microsoft Exchange (OWA, ECP,EWS, etc.)</td>
           <td>Only if applicable</td>
       </tr>
       <tr>
           <td>login.salesforce.com and its dependencies.<br> Refer to Salesforce for details</td>
           <td>Authorization with Salesforce account</td>
       </tr>
       <tr>
           <td>dc.services.visualstudio.com</td>
           <td>AppInsights logging</td>
       </tr>
       <tr>
           <td>fonts.gооoagleapis.com<br> fonts.gstаtic.com</td>
           <td>Nunito Sans font for UI</td>
       </tr>
       <tr>
           <td>logo.clearbit.com</td>
           <td>Organization logos by email domain for Contacts</td>
       </tr>
       <tr>
           <td>api.ipify.org</td>
           <td>Detecting current user IP. Needed for proper work of email opens and link clicks analytics</td>
       </tr>
    </tbody>
</table>

<div class="admonition hint">
<p class="admonition-title">Important</p>
<p>All listed IPs are guaranteed to be secure, according to our <a href="../Privacy-and-Security/">privacy and security policies</a> transferred data is encrypted with <a href="https://en.wikipedia.org/wiki/Transport_Layer_Security">TLS 1.2</a></p>
</div>

<br>








