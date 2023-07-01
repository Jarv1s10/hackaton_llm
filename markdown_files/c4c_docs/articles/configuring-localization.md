# Server-Side Integration Localization

&nbsp;

&nbsp;

**[ This article is work-in-progress ]**

&nbsp;

## Supported user interface localizations

<!--https://www.alchemysoftware.com/livedocs/ezscript/Topics/Catalyst/Language.htm-->

SSI interface, dashboards, and settings are available in **12 world languages**. The default language is **English**, which is also used for non-supported localizations.

* Chinese (Simplified, People's Republic of China)
* Czech (Czechia)
* Dutch (Netherlands)
* English (United States)
* French (France)
* German (Germany)
* Italian (Italy)
* Japanese (Japan)
* Polish (Poland)
* Portuguese (Brazil)
* Russian (Russia)
* Spanish (Spain)

&nbsp;

&nbsp;

* * *

&nbsp;

&nbsp;

## Groupware Settings and User Settings localization

The SSI language on the web depends on SAP Cloud for Customer user interface localization, which user selects during login only and cannot be changed independently in Server-Side Integration settings.

<p>
<img src= "..\..\assets\images\ssi-localization\1.png" style="width: 50%; height: 50%;">
</p>

<details><summary>>>> Click to see screenshot <<<</summary>
<p>
The language selected during login applies to the whole web interface
</p>
<p>
<img src= "..\..\assets\images\ssi-localization\2.png">
</p>
</details>

&nbsp;

&nbsp;

* * *

&nbsp;

&nbsp;

## Server-Side synchronization and E-Mail templates localization

Localization in synchronization service defines the language of customization on MS Exchange/Google Storage like Shared Folders names, Shared Categories names, and messages in Status categories.

Update of localization forces MS Exchange/Google Storage re-initialization (removal of old data and synchronization of new data).

E-mail templates sent to the user (e-mail about sync failure, expired MS Exchange password, welcome e-mail) match the same language defined in synchronization settings.

&nbsp;

&nbsp;

### Localization configuring by standard user

1. Make sure the desired language is configured in SAP Cloud for Customer user settings

<p>
<img src= "..\..\assets\images\ssi-localization\5.png">
</p>

&nbsp;

2. Go to **E-Mail Integration** > **User settings** > **Sync Settings** > **Detailed Settings**

3. Click **Apply** at the *Localization* block

<p>
<img src= "..\..\assets\images\ssi-localization\4.png">
</p>

&nbsp;

4. Go to the *Dashboard* page and start **Force Sync** to finish localization configuring

&nbsp;

&nbsp;

### Localization configuring by key user

1. Open Business User in Administrator section in SAP Cloud for Customer and select desired language

<p>
<img src= "..\..\assets\images\ssi-localization\6.png">
</p>

&nbsp;

2. Next, go to **E-Mail Integration** > **Groupware Settings** > **Users**

3. Open User, click 'Gear' button and select **Apply Localization**

<p>
<img src= "..\..\assets\images\ssi-localization\key-user-localization.png">
</p>

&nbsp;

&nbsp;

* * *

&nbsp;

&nbsp;

## Add-In localization

Add-In interface language depends on configuration of e-mail client used and is taken from:

* Language settings in MS [Outlook Web Access](https://outlook.office.com/mail) (OWA) configuration, if Add-In is used in OWA

<p>
<img src= "..\..\assets\images\ssi-localization\owa.png">
</p>

&nbsp;

* Outlook display language (**File** > **Options** > **Language**), if Add-In is used in the desktop MS Outlook

<p>
<img src= "..\..\assets\images\ssi-localization\desktop-outlook.png">
</p>

&nbsp;

&nbsp;

* * *

&nbsp;

&nbsp;

## Add-In localization on mobile devices

The Add-In language in MS Outlook for iOS application is being managed by the device Region settings. You may adjust the Region using the following steps:

1. Go to device **Settings** > **General** > **Language & Region** > **Region**

<p>
<img src= "..\..\assets\images\mobile-devices\ios-localization-1.png" style="width: 45%; height: 45%;">
</p>

&nbsp;

2. Search for the required Region and confirm the Change to the selected region. The MS Outlook app will be restarted automatically, and the Add-In should apply the corresponding language

<p>
<img src= "..\..\assets\images\mobile-devices\ios-localization-2.png" style="width: 45%; height: 45%;">
</p>

&nbsp;

&nbsp;