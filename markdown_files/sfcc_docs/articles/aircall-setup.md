---
description: Set up AirCall for making calls from Revenue Grid
---

# How to set up AirCall voice calls for Revenue Grid 

<p style="font-size:15px"><i>3 min read - updated few hours ago</i></font></p>
<!-- ShareThis BEGIN -->
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis -->
</p>
&nbsp;

*4 min read*  

&nbsp;

This article describes how to connect <a href="https://aircall.io/" target="_blank">AirCall</a> to Revenue Grid for making voice calls from {{ short_company_name }} Action Center or Revenue Grid Dial widget in Salesforce.  


The AirCall setup for {{ company_name }} consists of the following stages: 

1. [Create an AirCall account](#1_create_an_aircall_account)

2. [Create a phone number](#2_create_a_phone_number)

3. [Connect AirCall to {{ company_name }}](#3_connect_aircall_to_rg)

4. [Assign numbers to individual users in {{ company_name }}](#4_assign_numbers_to_individual_users_in_revenue_grid)

5. [Using AirCall integration](#5_using_aircall_integration_in_rg)

<br>
<hr>
<br>

A prerequisite for using the AirCall integration is to have an active account and phone numbers in AirCall. Follow the steps described below to set up and configure the basic AirCall account. 

!!! tip "Tip"  
    If you already have your account configured and phone numbers created, skip sections 1 and 2, and proceed with the next one. 

<br>
<hr>
<br> 
## 1. Create an AirCall account  

Go to <a href="https://aircall.io/" target="_blank">https://aircall.io/</a> and create an account. 
 
You can learn more about setting it up in <a href="https://aircall.io/onboarding/" target="_blank">this AirCall onboarding article</a>. 
<br>
<hr>
<br>
## 2. Create a phone number 

Follow the steps described in <a href="https://support.aircall.io/hc/en-gb/articles/10375395483037" target="_blank">this article</a> or in our guide below to create your first phone number in AirCall. 

2.1. <a href="https://dashboard.aircall.io/login" target="_blank">Log in</a> to the AirCall Dashboard 

2.2. Click **Create or port number** in the upper right-hand corner of the *Number overview* page 
<img src="..\..\assets\images\aircall\create-number.png">
<br>

2.3. Select **Create a number** from the drop-down list 

2.4. Next, select the number type: a Classic Number or an IVR Number 

2.5. Specify the details: 

* Location 

* Type: toll-free or local number 

* Area code 

* Number's name 

* Assign a team or a user to the number (optional) 

<img src="..\..\assets\images\aircall\classic-number.png">
<br>

2.6. Click **Create number** 

<br>
<hr>
<br> 
 
## 3. Connect AirCall to RG  

The steps described below are performed by the admin. 

3.1. <a href="https://dashboard.aircall.io/login" target="_blank">Log in</a> to the AirCall Dashboard 

3.2. In the left-hand-side navigation menu, go to **Integrations & API** > **API keys**

<img src="..\..\assets\images\aircall\integrations-and-api.png">
<br>

3.3. Click **Generate on API key**
<img src="..\..\assets\images\aircall\generate.png" style="width:70%">

<br>

3.4. In the *Generate API key* dialog, **copy API ID and API Token values and save them** in a text editor for further use. 

<img src="..\..\assets\images\aircall\copy.png">
<br>

!!! warning "Important"    
    Close the dialog only **after** you have copied the API ID and API Token values. If you close the dialog without copying and saving both values in a text editor, you will need to generate new API key as described in steps 3.3-3.4. 
<br>

3.5. [Log in](https://revenuegrid.com/log-in/) to {{ company_name }} 

<img src="..\..\assets\images\aircall\profile-settings.png" style="width:40%; display:inline-block; vertical-align:middle; margin-left:10px; float: right">
3.6. Click on your profile photo in the upper-right-side corner of the interface and go to **Settings**  

<br><br><br><br><br>
<img src="..\..\assets\images\aircall\sms-and-calls.png" style="width:35%; display:inline-block; vertical-align:middle; margin-left:10px; float: right">
3.7. Next click on **Sequences** under *Platform settings* 

3.8. Go to **SMS & calls** 


<br><br><br><br><br><br><br>
<img src="..\..\assets\images\aircall\aircall.png" style="width:50%; display:inline-block; vertical-align:middle; margin-left:10px; float: right">
3.9. Select **AirCall** on the list of available providers 

3.10. Insert the values copied in the step 3.4 in the corresponding boxes 

3.11. Click **Save** at the bottom of the page to enforce the changes 
<br><br><br><br><br>

<br>
<hr>
<br>  
 
## 4. Assign numbers to individual users in {{ company_name }} 

This step can be performed by admins for individual users or by very individual users who will be using AirCall in {{ company_name }}.  

**An extra step for admins:** Under Administration, click Users, find the necessary user on the list and proceed with step 4.4.

4.1. <a href="https://revenuegrid.com/log-in/" target="_blank">Log in</a> to {{ company_name }}

<img src="..\..\assets\images\aircall\profile-settings.png" style="width:40%; display:inline-block; vertical-align:middle; margin-left:10px; float: right">
4.2. Click on your profile photo in the upper-right-side corner of the interface 

4.3. Go to **Settings** 

<br><br>

<img src="..\..\assets\images\aircall\personal.png" style="width:30%; display:inline-block; vertical-align:middle; margin-left:10px; float: right">
4.4. Click on **Sequences** under *Personal settings* 

4.5. Go to the **General** tab 


<br><br><br><br><br><br>
4.6. In the Phone settings section, select the necessary Communication user and Voice number from the drop-down lists. 
<img src="..\..\assets\images\aircall\user.png">
<br>

The Communication user and Voice number lists are based on the information about added users and phone numbers retrieved from AirCall. You can learn more about adding users in AirCall dashboard in <a href="https://support.aircall.io/hc/en-gb/articles/10375354696861" target="_blank">this article</a> and how to configure calls distribution and assigning users to phone numbers in <a href="https://support.aircall.io/hc/en-gb/articles/10375395341725" target="_blank">this article</a>. 

!!! warning "Important"  
    **One phone number must be assigned to one communication user in Revenue Grid**. Assignment of one voice number to multiple users is not possible 

<br>
<hr>
<br> 

## 5. Using AirCall integration in RG 

After selecting Communication user and Voice number, {{ company_name }} will use the corresponding number for making voice calls from the Action Center or from the Dial out widget in your Salesforce interface. 

Due to AirCall limitation, the integration in Revenue Grid supports only making calls while sending SMS is not available.  

<br>
 
### Making calls with AirCall integration 

When recipients reach a phone call type of step, you will see a <a href="https://docs.revenuegrid.com/articles/to-dos/" target="_blank">corresponding notification on the To-dos tab</a> in your Action Center. 

The cell phone number of the recipient is retrieved from Salesforce. If the phone number field is blank, you can type in the number. Note that manually typed in numbers won't be saved to Salesforce. 


A prerequisite for <a href="https://docs.revenuegrid.com/articles/to-dos/#make_a_call" target="_blank">making calls from the Action Center</a> is to have the AirCall app opened and logged in with the user that is specified in the Communication user field in {{ company_name }}. It can be a <a href="https://aircall.io/download/" target="_blank">desktop or mobile app</a>, or Salesforce integration. 

After you click the *Make a call* button in the Action Center, the AirCall app will start dialing and the phone call will take place in the AirCall app.  

!!! warning "Important"    
    To make a call, when clicking the Make a call button in the Action Center in {{ company_name }}, you must also have the AirCall app opened and logged in with the user that is specified in the Communication user field in Revenue Grid. If the app is not opened and logged in, you will not be able to make calls. 