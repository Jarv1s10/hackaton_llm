---
description: Detailed overview of Revenue Grid Data Privacy and Security policies
---
# Privacy and Security  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*5 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

### Data Privacy Policy

We take our customers’ data privacy and security with utmost seriousness.  
Our solution {{ product_name }} performs synchronization of business communication and CRM data between users' CRM accounts and mailboxes.   
{{ product_name }} for Salesforce synchronizes the following types of authorized users' data: Calendar items, Tasks, Contacts, Email messages, and file Attachments. Using the solution’s Dashboard, the users can [define which record types](../Choosing-What-to-Synchronize/) to [synchronize](../Synchronization-Engine-An-Overview/) via {{ short_name }} service, as well as [other aspects of its functioning](../How-to-Open-Sync-Dashboard-(Adaptive-view)/).   
For more details, see the *“Product-specific Privacy Terms”* section of the complete [{{ company_name }} Data Security Policies document](https://revenuegrid.com/privacy-policy/).

&nbsp;

### Official certification and regular audit

&nbsp;

⇛ [SOC2 Type II certified](https://www.aicpa.org/content/dam/aicpa/interestareas/frc/assuranceadvisoryservices/downloadabledocuments/trust-services-criteria.pdf): Security, Availability, Processing Integrity, Confidentiality, and Privacy Audit  

⇛ [Privacy shield](https://www.privacyshield.gov/Program-Overview) certified  

- [EU-U.S. Privacy Shield Framework](https://www.privacyshield.gov/participant?id=a2zt0000000CjKUAA0&status=Active)  

- [Swiss-U.S. Privacy Shield Framework](https://www.privacyshield.gov/participant?id=a2zt0000000CjKUAA0&status=Active)  

⇛ [GDPR](https://gdpr.eu/tag/gdpr/) compliant   

⇛ [HIPAA Seal of Compliance](https://compliancy-group.com/hipaa-compliance-verification/) verified

⇛ [ISO-27001](https://www.iso.org/isoiec-27001-information-security.html) (Information Security Management set) certified  

⇛ [A multisided solution security review carried out by NCC Group](https://cyberstore.nccgroup.com/our-services/service-details/8/cyber-security-review)  

⇛ {{ company_name }} is a longstanding [certified Microsoft Partner](https://partner.microsoft.com/en-us/membership/windows-and-devices-competency) based on [special competency requirements](https://partner.microsoft.com/en-us/membership/competencies)  

⇛ All {{ company_name }} components undergo regular [penetration tests](https://en.wikipedia.org/wiki/Penetration_test) carried out by independent contractors  

⇛ {{ company_name }} technical support team ensures super-fast reaction to security cases as well other kinds of reports. See [this article](https://revenuegrid.com/news/g2-best-support-badge/) for more information  

&nbsp;

&nbsp;

## Confidentiality and Availability  

We implemented appropriate technical, organizational, and administrative systems, policies, and procedures designed to ensure the security, integrity, and confidentiality of customer data and to mitigate the risk of unauthorized access to or use of customer content.

Unless other terms apply or agreed otherwise, with respect to subscription based SaaS Services, during the prepaid subscription Revenue Grid will use commercially reasonable efforts to make the SaaS Services available 24 hours per day, 7 (seven) days per week, except for planned maintenance and emergency downtime and any unavailability due to circumstances out of Revenue Grid's control (including but not limited to customer's misuse of the Services; failures of customer's or its users' internet connectivity; Internet or other network traffic problems etc.).

&nbsp;

&nbsp;

### Security Policies

With over 13 years of experience of building and implementing successful enterprise solutions, we know very well that email correspondence and CRM data stand among the key assets of any modern business. For this reason handling all communications between your email and CRM systems and {{ product_name }} with maximum security is our topmost priority.

We follow a multi-level layered approach, which is continuously updated with the latest technologies to ensure the highest level of security for our customers' data, from complete physical security of Microsoft certified data centers we use to secured access authorization procedures for the end users (see below) and the [latest gen encrypted data transfer protocols](https://docs.microsoft.com/en-us/office365/troubleshoot/security/prepare-tls-1.2-in-office-365).  

&nbsp;

#### Application Design

[{{ company_name }} Sync component](../AddIn-vs-Sync-Functions/) is built as a scalable customized [Microsoft Azure service](https://searchcloudcomputing.techtarget.com/definition/Windows-Azure) which supports geo-distributed data centers and provides the highest levels of availability and resilience; it matches Microsoft's standards for secure applications.

[The Add-In component of {{ product_name }}](../Introduction/) is a [MS Outlook add-in](https://docs.microsoft.com/en-us/outlook/add-ins/) verified by Microsoft that works directly with users' email and CRM data, also displaying relevant information for the end users and conveying their inputs and actions to {{ short_name }} Sync or directly to Salesforce. The [Chrome Extension](../How-to-Set-Up-the-Chrome-Extension-for-Salesforce-and-Gmail/) option for [{{ short_name }} integration into Gmail](../Using-the-Solution-for-Salesforce-and-Gmail/) works in the same manner as the Add-In and is [verified by Google](https://developer.chrome.com/extensions/single_purpose).

&nbsp;

#### Service Authentication

While {{ product_name }} also supports legacy authentication solutions, for example to work with MS Exchange 2010, by default all {{ short_name }} end users follow the most secure access authentication procedures:

* [Single Sign-On](https://help.salesforce.com/articleView?id=sso_about.htm&type=5) to access Salesforce and [OAuth 2.0](https://oauth.net/2/) or [MS Graph](../MS-Graph/) for Office 365

* Using [EWS](../Working-With-EWS/) to authorize MS Exchange data access, with optional fallback to login/password authentication for legacy MS Exchange servers

* Using [OAuth 2.0](https://developers.google.com/gmail/imap/xoauth2-protocol) to authorize Gmail and Google calendar data access for [{{ short_name }} Chrome Extension](../Using-the-Solution-for-Salesforce-and-Gmail/) users

* Possibility of mass mailboxes provisioning via [Impersonated Exchange access](../Setting-Up-Impersonated-Access-and-Configuring-Mailbox-Access-for-Organizations-and-Users/), where the local Exchange Admin grants {{ product_name }} permissions to work with specified users' mailboxes and calendar data

* Possibility of mass Salesforce provisioning via [impersonating account or API-only user](../Set-up-Salesforce-Auth/), where the local Salesforce Admin grants {{ product_name }} permissions to work with specified users' Salesforce data 

  

&nbsp;

#### Granular Access Control

Our app's access to user configurations and data is built on granular level, it is based on the concepts of Permissions, Roles, Principals, Resources and Authorizations:

*   All data views, transfers, or other related actions are controlled by structured permission rules
*   Combination of Permission sets into Roles allows to define allowed operations scopes very specifically
*   In {{ short_name }} data access architecture, assigning of Principals, Roles for specific Resources access, results in granting of the minimum required permissions level for performing of very specific tasks

This access control policy covers **all** {{ product_name }} users, including {{ company_name }} Admins: Sales, Support and Customer Success teams, to ensure that the customers' data is accessible **only** by the entitled end users.

&nbsp;

#### Data Protection

{{ product_name }} ensures multi-level protection of sensitive data from accidental or malicious loss, whether in transit, at rest, or on the go. Among standard techniques, that includes:

*   **Access to Salesforce, Office 365, and Gmail data** is performed through certified apps on respective services  
*   **In-transit encryption**: all data transfers between Salesforce/Microsoft Exchange or Google servers as well as user interactions with them via {{ short_name }} are encrypted with [TLS protocol](https://www.internetsociety.org/deploy360/tls/basics/)  
*   **At rest encryption**: all relevant configuration data is [encrypted in rest state](https://docs.microsoft.com/en-us/azure/security/fundamentals/encryption-atrest) on [physical storage database level](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption)  
*   **Secrets handling**: all used access secrets (tokens, passwords) are additionally encrypted on application level using keys transferred separately from the data. Furthermore, {{ short_name }} [API connections](https://www.upwork.com/hiring/development/intro-to-apis-what-is-an-api/) are designed in such a way so access secrets never leave {{ product_name }} perimeter  
*   **Data backup and point-in-time restore**: users' and orgs' configuration data is continuously backed-up automatically; it is kept as multiple copies, ensuring the possibility to do a point-in-time restore
*   **Data isolation**: [server-side synchronization of data](../Synchronization-Engine-An-Overview/) of different {{ short_name }} users is logically and physically isolated, which guarantees that no data can be transferred or leak between the users, in any other ways but ones defined by Salesforce or Microsoft Exchange / Office 365 / Gmail

&nbsp;

#### Infrastructure

*   **Data centers**: {{ product_name }} is hosted on [Microsoft Azure data centers](https://azure.microsoft.com/en-us/global-infrastructure/) which ensure the [highest security levels](https://docs.microsoft.com/en-us/azure/security/fundamentals/overview)
*   **Security Updates**: {{ product_name }} is a managed cloud solution; that, regular besides updates of {{ short_name }} features, implies automatic front-end and back-end data security infrastructure updates  
*   **Firewalls and network access**: {{ product_name }} uses Microsoft Azure's capabilities to run its services in a secure virtual network with limited and strictly audited external access
*   **Networking**: no server used by {{ product_name }} for user data transfers or config keeping is accessible from outside the network. Any externally visible services operate behind a firewall and a load balancer within this virtual private network



&#160;
 &#160;

