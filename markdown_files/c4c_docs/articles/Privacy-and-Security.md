# Privacy and Security  

&nbsp;

<span style="color: #e74125;font-size: 17px;font-weight: 700;line-height: 30px;padding: 0px 10px;outline: none;border-radius: 2px;text-decoration: none;background-color: #fff;display: inline-block;border: 0px solid #000;transition: .3s all;width: auto;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="display: inline-block;vertical-align: middle;height: 32px;object-fit: contain;"></span><span style="color: #e74125;font-size: 17px;font-weight: 700;line-height: 30px;padding: 0px 10px;outline: none;border-radius: 2px;text-decoration: none;background-color: #fff;display: inline-block;border: 0px solid #000;transition: .3s all;width: auto;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="display: inline-block;vertical-align: middle;height: 32px;object-fit: contain;"></span><span style="color: #e74125;font-size: 17px;font-weight: 700;line-height: 30px;padding: 0px 10px;outline: none;border-radius: 0px;text-decoration: none;background-color: #fff;display: inline-block;border: 0px solid #000;transition: .3s all;width: auto;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="display: inline-block;vertical-align: middle;height: 32px;object-fit: contain;"></span> 

&nbsp;

### Data Privacy Policy

We consider your privacy very seriously. As such, we adhere to the following basic principles to protect your privacy:

*   We NEVER share your personal information with third parties.
*   SAP Cloud for Customer Server-Side Integration NEVER permanently stores any of your SAP Cloud For Customer or Exchange/Office 365/Google data (contacts, e-mails, and so on). That data is only passed through the cloud app, temporarily kept in memory, and NEVER written to any persistent storage. 
    *   What is stored: identifiers and last modified dates for the records synchronized. Also, we temporarily keep names of records for which synchronization service experienced issues solely to display that to you as error messages.
*   Any personally identifiable information which gets transferred through our servers is secured with industry standard protocols and technologies, more on this below.

For more details, see [Revenue Grid Privacy Policy](https://revenuegrid.com/privacy-policy/).

&nbsp;

&nbsp;

### Relevant Certification

[Privacy Shield](https://www.privacyshield.gov/Program-Overview) certified

[GDPR](https://gdpr-info.eu/) compliant

[ISO-27001](https://www.iso.org/isoiec-27001-information-security.html) certified (information security management)

&nbsp;

&nbsp;

### Security Policies

With over 15 years of experience in building and implementing successful enterprise solutions, we know that e-mail communication and CRM stand among the very key assets of any business. 

Security of all your Exchange/Office 365/Google and CRM data, all communications between your systems and SAP Cloud for Customer SSI, and all user interactions with our system is our topmost priority.

We are continuously focused on a multi-level, layered approach to provide our customers with the highest level of security, from the physical security of certified data centers to the applications designed to be secure.  

&nbsp;

#### Application Design

SAP Cloud for Customer SSI is built as a scalable and secure Windows Azure service which supports geo-distributed data centers and can guarantee the highest levels of availability and resilience, meeting industry standards for secure applications.

&nbsp;

#### User Authentication

While SAP Cloud for Customer SSI supports legacy solutions (e.g., Microsoft Exchange 2010), the users are always advised to go with the most secure approach:

*   Use of OAUTH2 for Office 365, with fallback to login/password authentication on legacy Microsoft Exchange servers
*   Use of impersonated Exchange setup, where IT team grants SAP Cloud for Customer SSI permissions to access specific users' mailboxes
*   Use of Single Sign-On for secure authentication of Outlook Add-In/Chrome Extension users 

&nbsp;

#### Granular Access Control

The granular access control is based on the concept of Permissions, Roles, Principals, Resources, and Authorizations that provides leveled access to user data and configurations:

*   Each possible access or action is controlled by specific Permission
*   Combination of Permissions into Roles allows defining exact operations, which can be done
*   Assigning Principals specific Roles to specific Resources results in the flexible privilege-based configuration of responsibilities

Access policy is configured for ALL SAP Cloud for Customer SSI users, including internal Administration, Sales, Support, and Customer Success Teams, to ensure customer data is available only to the right people with the right level of access.

&nbsp;

#### Data Protection

SAP Cloud for Customer SSI applies multi-level protection of sensitive data from accidental or malicious loss, whether in transit, at rest, or on the go. Among other techniques, this includes:

*   **Access to SAP Cloud for Customer and Office 365 data:** Access is performed through registered applications on respective services, via [TLS 1.2 protocol](https://www.ssl.com/article/tls-1-3-is-here-to-stay/)
*   **In-transit encryption:** All information exchange with SAP Cloud for Customer SSI, Microsoft Exchange or Google servers, and user interactions is encrypted with [SSL](https://www.ssl.com/faqs/faq-what-is-ssl/)
*   **At rest encryption:** Configuration data is encrypted at rest on physical database level
*   **Secrets handling:** Secrets (tokens, passwords) are additionally encrypted on application level using keys stored separately from DB. Further, APIs are built in a way where secrets never leave SAP Cloud for Customer SSI borders
*   **Data backup and point-in-time restore:** Configuration data is continuously backed-up. It exists in multiple copies with ability to do point-in-time restore
*   **Data isolation:** Synchronization data for different users are physically isolated, which guarantees information cannot be transferred between the users of SSI in ways other than those defined by SAP Cloud for Customer SSI or Microsoft Exchange / Google

&nbsp;

#### Infrastructure

*   **Data centers:** SAP Cloud for Customer SSI is hosted in Microsoft Azure data centers which comply with the highest security requirements. For more information on Microsoft Azure Datacenter security principles, see [this article](https://www.microsoft.com/en-us/TrustCenter/Security/AzureSecurity)
*   **Security Updates:** SAP Cloud for Customer SSI operates as a managed cloud solution that includes automatic updates and security patches
*   **Firewalls and network access:** SAP Cloud for Customer SSI leverages Microsoft Azure capabilities to run service in a secure network with limited and audited external access
*   **Networking:** None of the SAP Cloud for Customer SSI servers are accessible from outside the network. Publicly visible services operate behind the firewall and load balancer in the virtual private network

&nbsp;

&nbsp;