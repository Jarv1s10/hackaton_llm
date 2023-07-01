---
description: Learn how to convert a shared MS Exchange mailbox to a regular user mailbox
---
# How to Convert a Shared MS Exchange Mailbox to a Regular User Mailbox  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div>

&nbsp;

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

{{ company_name }} and {{ company_name }} work with data from end users' email  accounts; handling of email and calendar data from shared Exchange mailboxes [is not supported](../Frequently-Asked-Questions/#24_does_revenue_grid_allow_handling_items_from_an_exchange_shared_mailbox). Some setup scenarios require converting an existing [shared MS Exchange mailbox](https://docs.microsoft.com/en-us/exchange/collaboration/shared-mailboxes/shared-mailboxes?view=exchserver-2019) to an individual user one, in order to enable {{ company_name }} and {{ company_name }} functions for it. This article describes two ways to do that: using MS Exchange Admin Center or MS Exchange Online PowerShell.

A converted account can be used by an end user or [configured as a Service account](../Impersonation-O365/) for [mass deployment of {{ company_name }} / {{ company_name }}](../Email-Integration-Full-Deployment-Scenarios/).



!!! tip "Tip"
    Also see these Microsoft articles [article 1](https://docs.microsoft.com/en-us/microsoft-365/admin/email/convert-user-mailbox-to-shared-mailbox?view=o365-worldwide) and [article 2](https://docs.microsoft.com/en-us/microsoft-365/admin/email/about-shared-mailboxes?view=o365-worldwide)

&nbsp;

!!! note "Note"
    After mailbox conversion all mail data it contains remains intact

&nbsp;

&nbsp;

## Method 1: Convert using [MS Exchange Admin Center](https://docs.microsoft.com/en-us/exchange/exchange-admin-center)

&nbsp;

**1.** Log in to the Admin Center with Exchange Admin credentials <https://outlook.office365.com/ecp>

&nbsp;

**2.** Click **Recipients** > **Shared** and select the shared account that you want to convert

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Convert-Shared/convert1.png" class="minimized">
</p>

&nbsp;

**3.** Click **Yes** in the *Warning* dialog and then **Close** the dialog after conversion is complete

![](../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Convert-Shared/convert2.png)

&nbsp;

![](../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Convert-Shared/convert3.png)

&nbsp;

**4.** Next, to activate the converted user, open Microsoft 365 Admin Center and log in to it with Admin credentials <https://admin.microsoft.com>

&nbsp;

**5.** Click **Users** > **Active Users**, search for recently converted mailboxes

<p><img src="../../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Convert-Shared/convert4.png" class="minimized">
</p>

&nbsp;

**6.** [Assign an Exchange license](https://www.microsoft.com/en-us/microsoft-365/exchange/microsoft-exchange-licensing-faq-email-for-business) for each converted mailbox and **Save changes** to apply the changes

![](../assets/images/Configuration-&-Settings/Admin-Settings-&-Actions/Convert-Shared/convert5.png)

&nbsp;

* * *

&nbsp;

## Method 2: Convert using [Exchange Online PowerShell](https://docs.microsoft.com/en-us/powershell/exchange/exchange-online-powershell?view=exchange-ps)

&nbsp;

**1.** Open PowerShell and connect to your Microsoft 365 tenant by entering the following cmdlets:

*$UserCredential = Get-Credential*  

*$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri https://outlook.office365.com/powershell-liveid/ -Credential $UserCredential -Authentication Basic -AllowRedirection*  

*Import-PSSession $Session*  

*Connect-MsolService*  

&nbsp;

**2.** Next, to convert a mailbox from shared to regular by entering the following cmdlet, where {Shared1} is the mailbox's name:

*Set-Mailbox {Shared1} -Type Regular*  

&nbsp;

**3.** Now check that the mailbox was successfully converted to regular by entering the following:

*Get-Mailbox -Identity shared1 | Format-List RecipientTypeDetails*  

*RecipientTypeDetails : UserMailbox*  

&nbsp;

**4.** Next, to ensure that the mailbox is active and has a license assigned: view the summary information about mailboxes' plans and licenses for  each plan, by running the following command:

*Get-MsolAccountSku*

&nbsp;

**5.** If there is no usage location assigned to the converted mailbox, you can assign it with this cmdlet:

*Set-MsolUser -UserPrincipalName "{shared1@contoso.com}" -UsageLocation US*

&nbsp;

In addition, to assign an Exchange license to the converted mailbox, enter the following command (use the *AccountSkuId* retrieved on step **4**):

*Set-MsolUserLicense -UserPrincipalName "{shared1@contoso.com}" -AddLicenses "<AccountSkuId> "*

&nbsp;

&nbsp;


<style>
  .banners {
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .banners a.button {
      background-color: #FFC827;
      color: #2F3341;
      box-shadow: 0 5px 35px rgba(146, 146, 146, 0.2);
      padding: 20px;
      font-family: Graphic, arial;
      font-weight: 600;
      line-height: 24px;
      margin-top: -100px;
      border-radius: 3px;
      cursor: pointer;
      transition: .1s;
  }

  .banners a.button:hover {
    transform: scale(1.05);
  }

  .banners a.button a:hover,
  .banners a.button a:visited {
      color: #2F3341;
  }

  .banner-3 a.button {
    margin-left: 45%;
  }
</style>

<br>
<div class="banners banner-2">
  <img src="../../assets/images/banners/banner-2.svg" style="width: 100%; height: 100%;">
  <a class="button" href="https://revenuegrid.com/request-demo/?utm_source=kb_rg&utm_medium=referral&utm_campaign=eac_demo&utm_content=banner" target="_blank">Book a free demo</a>
</div>