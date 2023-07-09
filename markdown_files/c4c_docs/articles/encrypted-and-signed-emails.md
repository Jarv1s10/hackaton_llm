# Support of Encrypted and Signed E-Mails

&nbsp;

&nbsp;

**[ This article is work-in-progress ]**

&nbsp;

&nbsp;

## What are Encrypting and Digital Signature

**Encrypting an e-mail message** in Microsoft Office Outlook protects the privacy of the message by converting it from (readable) plain-text into (scrambled) cipher-text. Only the recipient who has the private key that matches the public key used to encrypt the message can decipher the message for reading. Any recipient without the corresponding private key would see only garbled text. More details about encrypted e-mail can be found [here](https://support.microsoft.com/en-us/office/encrypt-email-messages-373339cb-bf1a-4509-b296-802a39d801dc).

**A digital signature** attached to an e-mail message offers another layer of security by assuring the recipient that you &#8211; not an imposter &#8211; signed the contents of the e-mail message. Your digital signature, which includes your certificate and public key, originates from your digital ID. And that digital ID serves as your unique digital mark and signals the recipient that the content hasn't been altered in transit. More details about the signed e-mail can be found [here](https://support.microsoft.com/en-us/office/secure-messages-by-using-a-digital-signature-549ca2f1-a68f-4366-85fa-b3f4b5856fc6).

&nbsp;

* * *

&nbsp;

## How Encrypting and Digital Signature works

The Add-In supports native MS Outlook *encryption functionality* with certificates issued by different vendors.

After MS Outlook is configured to encrypt e-mails, new buttons "**Encrypt**" and "**Sign**" are added to the ribbon of the e-mail.

<p>
<img src= "..\..\assets\images\encrypted-signed-emails\1.png">
</p>

&nbsp;

Such e-mail has a corresponding sign that identifies this e-mail as encrypted one.

<p>
<img src= "..\..\assets\images\encrypted-signed-emails\2.png">
</p>

&nbsp;

In order to exchange with encrypted e-mail, both users should obtain e-mail certificates and exchange with certificate public keys.

&nbsp;

* * *

&nbsp;

## Support of encrypted and signed e-mails

The complicated encryption and digital signing logic create many limitations which prevent SSI Sync and Add-In from properly operating.

In case the user selects an encrypted and/or signed e-mail message and tries to **open the Add-In**, the following error message will occur:

"*You cannot perform this action. Permission to this message is restricted*."

<p>
<img src= "..\..\assets\images\encrypted-signed-emails\3.png">
</p>

&nbsp;

This is a MS Outlook message, not an Add-In error. MS Outlook prevents add-in opening as it is not allowed to perform any operations with such e-mail messages.

If the user adds a “SAP Cloud for Customer” category to save encrypted/signed e-mail, the category will be added, but the e-mail won’t be saved to SAP Cloud for Customer.

As a result, because of existing Microsoft limitations, there is no way to save encrypted or/and signed e-mail messages to SAP Cloud for Customer using SSI Sync or Add-In.

&nbsp;

* * *

&nbsp;

## Exclusions (Microsoft Update)

!!! note "Note"
    The referencing article on Microsoft update you can find [here](https://learn.microsoft.com/en-us/office/dev/add-ins/outlook/outlook-add-ins-overview#mailbox-items-available-to-add-ins)

The most important points regarding the update are:

* Add-ins activate on digitally signed messages in MS Outlook associated with a Microsoft 365 subscription. On Windows, this support was introduced with *build 8711.1000*

* Starting with MS Outlook *build 13229.10000* on Windows, add-ins can now activate on items protected by Information Rights Management (IRM). For more information about this feature in preview, refer to [Add-In activation on items protected by IRM](https://learn.microsoft.com/en-us/javascript/api/requirement-sets/outlook/preview-requirement-set/outlook-requirement-set-preview?view=excel-js-preview#add-in-activation-on-items-protected-by-information-rights-management-irm)

&nbsp;

&nbsp;
