---
description: Configuration of Revenue Signals explained
---

# List of Configurable Signals and their Parameters  
  

*16 min read*  

&nbsp;

**[ This is the article for Signals managers]**    
  
&nbsp;
&nbsp;

!!! warning "Important"    
    This {{ short_company_name }} article is intended for [Signals Managers](../../../../articles/signals-manager/), i.e. users that are allowed to create signals for an organization or a team. It enlists the available configurable Revenue signals, their descriptions, parameters, and templates.    
&nbsp;
  
Revenue Signals are manually or automatically created alerts for sales representatives that notify about important occurrences and overall deal progress. They ensure that no event, email, or status change remains unnoticed or unreplied.    
  
  
When a deal reaches a specific stage or a critical occurrence takes place (a new email received, a meeting invite is unresponded for a particular number of days, etc.), signals notify the accountable employees about that and suggest the next steps to take. 

Besides the signals enabled by default and manually created signals, {{ company_name }} Intelligence package includes a flexible Signal Builder for creating custom signals of specific types. Below, you can find the detailed overview of the available signals presets, their configurable parameters, and sample templates. The enlisted signals presets are available by default.

&nbsp;  

!!! tip "Tip"  
    Refer to [this article](https://docs.revenuegrid.com/articles/Signals/) for an overview of Revenue signals for end users and to [this {{ short_name }} article](../revenue-signals/) to learn how to manage signals directly from your email client    
&nbsp;

&nbsp;
***
&nbsp;

## 1. Chosen conditions met for the Salesforce object
  

**Description**

This signal will be triggered when the chosen object meets all configured conditions.  
  
The generic Salesforce check job is intended to collect Salesforce objects which match the predefined filter and generate a signal for each of such objects.      
  

<p> 
<img src="..\..\assets\images\Internal-Use\signals-parameters\chosen-conditions-met-for-the-salesforce-object.png" class="minimized">
</p>
&nbsp;

<table data-layout="default">
    <tbody>
        <tr>
            <th colspan="2">
                <h3>Parameters</h3>
            </th>
        </tr>
        <tr>
            <td>
                <h4><strong>Trigger</strong></h4>
                <ul>
                    <li>
                        <p>Enabled – default value – True</p>
                    </li>
                    <li>
                        <p>Affected object:</p>
                        <ul>
                            <li>
                                <p>Lead</p>
                            </li>
                            <li>
                                <p>Contact</p>
                            </li>
                            <li>
                                <p>Opportunity</p>
                            </li>
                            <li>
                                <p>Account</p>
                            </li>
                        </ul>
                    </li>
                    <li>
                        <p>Recipient:</p>
                        <ul>
                            <li>
                                <p>Object Owner</p>
                            </li>
                            <li>
                                <p>Manager</p>
                            </li>
                            <li>
                                <p>Users</p>
                            </li>
                        </ul>
                    </li>
                    <li>
                        <p>Object filter SOQL (Mandatory)</p>
                    </li>
                </ul>
            </td>
            <td>
                <h4><strong>Action</strong></h4>
                <ul>
                    <li>
                        <p>Score – default value – &quot;-1&quot;</p>
                    </li>
                    <li>
                        <p>Dismiss the signal automatically after (hours) – default value –&nbsp; 336</p>
                    </li>
                    <li>
                        <p>Notification title (Mandatory)</p>
                    </li>
                    <li>
                        <p>Signal destinations:</p>
                        <ul>
                            <li>
                                <p>Action Center – default value – True, read only</p>
                            </li>
                            <li>
                                <p>Email – default value – True</p>
                            </li>
                            <li>
                                <p>MS Teams&nbsp; – default value – True</p>
                            </li>
                        </ul>
                    </li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>


<details><summary>Click to see the Configurable Parameters</summary>  

<h3>Configurable Parameters</h3>
<p>Configuration parameters are stored in the <strong>GenericSalesforceCheckConfiguration</strong> table in the signals database.</p>

<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <h3>Parameter</h3>
            </th>
            <th>
                <p>Description</p>
            </th>
            <th>
                <p>Default value</p>
            </th>
        </tr>
        <tr>
            <td>
                <p>ContextUserId</p>
            </td>
            <td>
                <p>Signals User ID that will be used to query data from Salesforce. Therefore this user must have complete visibility in Salesforce</p>
            </td>
            <td>
                <p>–</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsBlocked</p>
            </td>
            <td>
                <p>Flag indicating whether this job is disabled by {{ short_company_name }} authority (i.e., CSM, DevOps, admins, etc.)</p>
            </td>
            <td>
                <p>False</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsEnabled</p>
            </td>
            <td>
                <p>Flag indicating whether this job is enabled by tenant owner (i.e., customer)</p>
            </td>
            <td>
                <p>True</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Schedule</p>
            </td>
            <td>
                <p><a href="https://en.wikipedia.org/wiki/Cron">Cron</a> recurrence rule to execute this job (<a href="https://crontab.guru/">this</a> editor may be useful)</p>
            </td>
            <td>
                <p>*/30 * * * *</p>
                <p>(i.e., every thirty minutes)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>AutoDismissSignalAfterHours</p>
            </td>
            <td>
                <p>For how long the signal remains actual since its due date (the number of hours). After a specified time period (in hours), the signal is auto-dismissed.</p>
                <p>The value should be higher than or equal to 1</p>
            </td>
            <td>
                <p>336</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalScore</p>
            </td>
            <td>
                <p>Score to assign to the created signal</p>
            </td>
            <td>
                <p>-1</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalPririty</p>
            </td>
            <td>
                <p>Priority of the generated signals</p>
                <p>Possible values are:</p>
                <ul>
                    <li>
                        <p>Alert = 0</p>
                    </li>
                    <li>
                        <p>Notification = 1</p>
                    </li>
                </ul>
            </td>
            <td>
                <p>0</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ObjectType</p>
            </td>
            <td>
                <p>Salesforce object type to which filter should be applied.</p>
                <p>Possible values are:</p>
                <ul>
                    <li>
                        <p>Account = 1</p>
                    </li>
                    <li>
                        <p>Contact = 2</p>
                    </li>
                    <li>
                        <p>Lead = 3</p>
                    </li>
                    <li>
                        <p>Opportunity = 4</p>
                    </li>
                </ul>
                <p>Required</p>
            </td>
            <td>
                <p>–</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ObjectFilter</p>
            </td>
            <td>
                <p>Filter which must be applied to all Salesforce objects of type <em>ObjectType</em></p>
            </td>
            <td>
                <p>–</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>FilterDescription</p>
            </td>
            <td>
                <p>Caption text that will be displayed in the email subject and teams notification title</p>
                <p>Required</p>
            </td>
            <td>
                <p>–</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>RepeatSignalAfterDismissDays</p>
            </td>
            <td>
                <p>The number of days to wait before sending the signal again after the user dismissed it. The related Salesforce object should still satisfy the filter configurations.</p>
                <p>Valid value range: [1; 2147483647].</p>
            </td>
            <td>
                <p>7</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>AssigneeType</p>
            </td>
            <td>
                <p>Indicates to whom the created signals will be assigned.</p>
                <p>Possible values are:</p>
                <ul>
                    <li>
                        <p>ObjectOwner = 1 – signals user that corresponds to Salesforce user, owner of the matching object</p>
                    </li>
                    <li>
                        <p>ObjectOwnerManager = 2 – signals users that correspond to Salesforce users to whom object owner reports (under Salesforce user roles hierarchy)</p>
                    </li>
                    <li>
                        <p>ListedUsers = 3 – users explicitly listed in <em>AssigneesSignalsIds</em></p>
                    </li>
                </ul>
            </td>
            <td>
                <p>–</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>MaxMatchingObjectsCount</p>
            </td>
            <td>
                <p>The maximum number of Salesforce objects matching <em>ObjectFilter </em>for which signals are created. If the total number of matching objects exceeds the value specified in this parameter, then any signals will be created&nbsp;</p>
                <p>Valid value range: [1; 2147483647].</p>
            </td>
            <td>
                <p>25</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>AssigneesSignalsIds</p>
            </td>
            <td>
                <p>The array of signal Users IDs in JSON format which must be used as signal assignees</p>
                <p>Must contain at least one item if <em>AssigneeType</em> is set to 3 (ListedUsers)</p>
            </td>
            <td>
                <p>–</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalBodyTemplate</p>
            </td>
            <td>
                <p>Razor template should be used to render signal body</p>
            </td>
            <td>
                <p>–</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsEmailNotificationEnabled</p>
            </td>
            <td>
                <p>Indicates whether email notification will be sent to assignees after signal is created</p>
            </td>
            <td>
                <p>true</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>EmailNotificationTemplate</p>
            </td>
            <td>
                <p>Razor template should be used to render email notification body</p>
            </td>
            <td>
                <p>–</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsTeamsNotificationEnabled</p>
            </td>
            <td>
                <p>Indicates whether Teams notification will be sent to assignees after signal is created</p>
            </td>
            <td>
                <p>true</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>TeamsNotificationTemplate</p>
            </td>
            <td>
                <p>Razor template to be used to render Teams notification body</p>
            </td>
            <td>
                <p>–</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>LastRunDate</p>
            </td>
            <td>
                <p>The date and time job configuration was last executed</p>
                <p>Readonly</p>
            </td>
            <td>
                <p>–</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>LastRunStatus</p>
            </td>
            <td>
                <p>Configuration execution status:</p>
                <ul>
                    <li>
                        <p>Unknown = 0 - job configuration has never been executed before</p>
                    </li>
                    <li>
                        <p>Success = 1 - job configuration has been executed successfully</p>
                    </li>
                    <li>
                        <p>ObjectIsNotSupported = 2 - selected <em>ObjectType</em> is not available on the Salesforce</p>
                    </li>
                    <li>
                        <p>FilterIsInvalid = 3 - filter specified in <em>ObjectFilter</em> is invalid (e.g. at least one of the filter fields is not available)</p>
                    </li>
                    <li>
                        <p>TooManyMatchingObjects = 4 - number of objects which match&nbsp;<em>ObjectFilter</em> is higher than <em>MaxMatchingObjectsCount</em></p>
                    </li>
                </ul>
                <p>Readonly</p>
            </td>
            <td>
                <p>–</p>
            </td>
        </tr>
    </tbody>
</table>
</details>


<details><summary>Click to see the examples of signal settings</summary>  

<h3>Examples of signal settings</h3>
<ul>
    <li>
        <p>I am a Sales Manager and I want to get reminders if the opportunity is less than 90, 60, or 30 days away from the close date</p>
    </li>
</ul>  
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The opportunity is less than 90 days away from the close date</p>
<p> 
    <img src="..\..\assets\images\Internal-Use\signals-parameters\generic\generic-sales-manager-1.png"style="width: 90%; height: 90%;" class="minimized">
</p>
&nbsp;  
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The opportunity is less than 60 days away from the close date</p>
<p> 
    <img src="..\..\assets\images\Internal-Use\signals-parameters\generic\generic-sales-manager-2.png"style="width: 90%; height: 90%;" class="minimized">
</p>
&nbsp;
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The opportunity is less than 30 days away from the close date</p>
<p> 
    <img src="..\..\assets\images\Internal-Use\signals-parameters\generic\generic-sales-manager-3.png"style="width: 90%; height: 90%;" class="minimized">
</p>
&nbsp;
<ul>
    <li>
        <p>I am a Sales Contributor and I want to get reminders if the opportunity is less than 15 days away from the close date and is at the &quot;Proposal Price Quote&quot; stage</p>
    </li>
<p> 
    <img src="..\..\assets\images\Internal-Use\signals-parameters\generic\generic-sales-contributor-1.png"style="width: 90%; height: 90%;" class="minimized">
</p>
&nbsp;
    <li>
        <p>I'm a Sales Contributor and I want to get a notification if the close date has passed and the opportunity isn&rsquo;t closed</p>
    </li>
</ul>
<p> 
    <img src="..\..\assets\images\Internal-Use\signals-parameters\generic\generic-sales-contributor-2.png"style="width: 90%; height: 90%;" class="minimized">
</p>
&nbsp;
<ul>
    <li>
        <p>I am a Sales Contributor and I want to get a notification if the opportunity is closed with an amount of more than $50 000.</p>
    </li>
<p> 
    <img src="..\..\assets\images\Internal-Use\signals-parameters\generic\generic-sales-contributor-3.png"style="width: 90%; height: 90%;" class="minimized">
</p>
&nbsp;
    <li>
        <p>I am a Sales Director and I want my employees to get reminders if the Title of the Lead is not filled in and the Status is not &ldquo;Close-Converted&rdquo;</p>
    </li>
<p> 
    <img src="..\..\assets\images\Internal-Use\signals-parameters\generic\generic-sales-director-1.png"style="width: 90%; height: 90%;" class="minimized">
</p>
&nbsp;
    <li>
        <p>I am a Sales Director and I want my employees to get a reminder if the Created date of the Lead is more than 30 days ago and has the &ldquo;Opened-Not Contacted&rdquo; status</p>
    </li>
</ul>
<p> 
    <img src="..\..\assets\images\Internal-Use\signals-parameters\generic\generic-sales-director-2.png"style="width: 90%; height: 90%;" class="minimized">
</p>
&nbsp;
<ul>
    <li>
        <p>I am a Sales Director and I want my employees to get reminders if the open opportunity doesn't have any next steps</p>
    </li>
</ul>
<p> 
    <img src="..\..\assets\images\Internal-Use\signals-parameters\generic\generic-sales-director-3.png"style="width: 90%; height: 90%;" class="minimized">
</p>
&nbsp;
<ul>
    <li>
        <p>I am a CEO and I want to get a notification if&nbsp;an opportunity was created with the value exceeding $50,000</p>
    </li>
</ul>
<p> 
    <img src="..\..\assets\images\Internal-Use\signals-parameters\generic\generic-ceo.png"style="width: 90%; height: 90%;" class="minimized">
</p>
&nbsp;
</details>

&nbsp;  
***  
&nbsp;  
  
## 2. Follow-up reminder after meeting with a prospect  
    

**Description**  

This signal automatically reminds the sales reps to send follow-ups after meetings if there has been no registered interaction with the relevant contact associated with a Lead since the meeting.  

<p> 
<img src="..\..\assets\images\Internal-Use\signals-parameters\follow-up-reminder-after-meeting-with-a-prospect.png" class="minimized">
</p>
&nbsp;

<table data-layout="default">
    <tbody>
        <tr>
            <th colspan="2">
                <h3>Parameters</h3>
            </th>
        </tr>
        <tr>
            <td>
                <p><strong>Trigger</strong></p>
                <ul>
                    <li>
                        <p>Enabled/Disabled – default value – True</p>
                    </li>
                    <li>
                        <p>Follow-up check interval (hours) – default value – 24</p>
                    </li>
                    <li>
                        <p>Filter</p>
                    </li>
                </ul>
            </td>
            <td>
                <p><strong>Action</strong></p>
                <ul>
                    <li>
                        <p>Score – default value – &quot;-1&quot;</p>
                    </li>
                    <li>
                        <p>Dismiss the signal automatically after (hours)&nbsp; – &nbsp;default value – 336</p>
                    </li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>
&nbsp;

<details><summary>Click to see the Configurable Parameters</summary>  

<h3>Configurable Parameters</h3>  

<p>Configuration parameters are stored in the&nbsp;<strong>LeadMeetingFollowupReminderConfiguration</strong> table in the signals database.</p>
<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <p>Parameter</p>
            </th>
            <th>
                <p>Description</p>
            </th>
            <th>
                <p>Default value</p>
            </th>
        </tr>
        <tr>
            <td>
                <p>ContextUserId</p>
            </td>
            <td>
                <p>Signals User ID that will be used to query data from Salesforce, PeopleGraph, and Signals. Therefore this user must have complete visibility in Salesforce and on the Signals page</p>
            </td>
            <td>
                <p>-</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsBlocked</p>
            </td>
            <td>
                <p>Flag indicating whether this job is disabled by {{ short_company_name }} authority (i.e., CSM, DevOps, admins, etc.)</p>
            </td>
            <td>
                <p>False</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsEnabled</p>
            </td>
            <td>
                <p>Flag indicating whether this job is enabled by tenant owner (i.e., customer)</p>
            </td>
            <td>
                <p>True</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Schedule</p>
            </td>
            <td>
                <p><a href="https://en.wikipedia.org/wiki/Cron">Cron</a> recurrence rule to execute this job (<a href="https://crontab.guru/">this</a> editor may be useful for this purpose)</p>
            </td>
            <td>
                <p>0 */2 * * *</p>
                <p>(i.e., every two hours)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>AutoDismissSignalAfterHours</p>
            </td>
            <td>
                <p>For how long the signal remains actual since its due date (the number of hours). After the specified time period (in hours), the signal is auto-dismissed</p>
            </td>
            <td>
                <p>240</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalScore</p>
            </td>
            <td>
                <p>Score to assign to the created signal</p>
            </td>
            <td>
                <p>-1</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>FollowupCheckTimeoutHours</p>
            </td>
            <td>
                <p>Number of hours to wait after the event start date before checking for missing follow-up email</p>
            </td>
            <td>
                <p>24</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>LeadFilter</p>
            </td>
            <td>
                <p>SOQL query to select only significant leads</p>
                <p>(e.g. Lead_Score_SQL__c = 'X1' OR Lead_Score_SQL__c = 'X2')</p>
            </td>
            <td>
                <p>-</p>
                <p>(i.e., all Leads are applicable)</p>
            </td>
        </tr>
    </tbody>
</table>
</details>

&nbsp;  
***  
&nbsp;  

## 3. Meeting follow-up reminder for the open opportunity prospect  
  

**Description**

This signal automatically reminds sales reps to send follow-ups after meetings if there has been no registered interaction with the relevant Contact associated with an Opportunity since the meeting.

<p> 
<img src="..\..\assets\images\Internal-Use\signals-parameters\meeting-follow-up-reminder-for-the-open-opportunity-prospect.png" class="minimized">
</p>
&nbsp;  
  

<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <h3>Parameters</h3>
            </th>
            <th>
                <p />
            </th>
        </tr>
        <tr>
            <td>
                <p><strong>Trigger</strong></p>
                <ul>
                    <li>
                        <p>Enabled/Disabled – default value – True</p>
                    </li>
                    <li>
                        <p>Match Opportunities by Account – default value – True</p>
                    </li>
                    <li>
                        <p>Followup check interval (hours) – default value – 24</p>
                    </li>
                    <li>
                        <p>Filter</p>
                    </li>
                </ul>
            </td>
            <td>
                <p><strong>Action</strong></p>
                <ul>
                    <li>
                        <p>Score – default value – &quot;-1&quot;</p>
                    </li>
                    <li>
                        <p>Dismiss the signal automatically after (hours) – default value -336</p>
                    </li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>


<details><summary>Click to see the Configurable Parameters</summary> 

<h3>Configurable Parameters</h3>
<p>Configuration parameters are stored in the&nbsp;<strong>OpportunityMeetingFollowupReminderConfiguration</strong> table in the signals database.</p>
<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <p>Parameter</p>
            </th>
            <th>
                <p>Description</p>
            </th>
            <th>
                <p>Default value</p>
            </th>
        </tr>
        <tr>
            <td>
                <p>ContextUserId</p>
            </td>
            <td>
                <p>Signals User ID that will be used to query data from Salesforce, PeopleGraph, and Signals. Therefore this user must have complete visibility in Salesforce and Signals</p>
            </td>
            <td>
                <p>–</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsBlocked</p>
            </td>
            <td>
                <p>Flag indicating whether this job is disabled by {{ short_company_name }} authority (i.e., CSM, DevOps, admins, etc.)</p>
            </td>
            <td>
                <p>False</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsEnabled</p>
            </td>
            <td>
                <p>Flag indicating whether this job is enabled by tenant owner (i.e., customer)</p>
            </td>
            <td>
                <p>True</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Schedule</p>
            </td>
            <td>
                <p><a href="https://en.wikipedia.org/wiki/Cron">Cron</a> recurrence rule to execute this job (<a href="https://crontab.guru/">this</a> editor may be useful)</p>
            </td>
            <td>
                <p>0 */2 * * *</p>
                <p>(i.e., every two hours)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>AutoDismissSignalAfterHours</p>
            </td>
            <td>
                <p>For how long the signal remains actual since its due date (the number of hours). After the specified time period (number of hours), the signal is auto-dismissed</p>
            </td>
            <td>
                <p>240</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalScore</p>
            </td>
            <td>
                <p>Score to assign to the created signal</p>
            </td>
            <td>
                <p>-1</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>FollowupCheckTimeoutHours</p>
            </td>
            <td>
                <p>Number of hours to wait after the event start date before checking for missing follow-up email</p>
            </td>
            <td>
                <p>24</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>OpportunityFilter</p>
            </td>
            <td>
                <p>SOQL query WHERE clause to select only significant Opportunities</p>
                <p>(e.g. Amount &gt; 10000)</p>
            </td>
            <td>
                <p>IsClosed &lt;&gt; true AND Probability &gt; 0</p>
                <p>(abovementioned filter cannot be changed; the custom filter is combined (using AND) with the base filter)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>MatchOpportunitiesByAccount</p>
            </td>
            <td>
                <p>Flag indicating how to find the Opportunities that are related to event participants:</p>
                <ul>
                    <li>
                        <p>event participant's email matches the Contact that is assigned to the Opportunity contact role (False)</p>
                    </li>
                    <li>
                        <p>event participant's email matches the Contact that is assigned to the Opportunity contact role or contact, and the Opportunity is bound to the same account (True)</p>
                    </li>
                </ul>
            </td>
            <td>
                <p>True</p>
            </td>
        </tr>
    </tbody>
</table>
</details>

&nbsp;  
***  
&nbsp;  

## 4. No interaction with the open opportunity prospects
  

**Description**

<p>The user gets a notification when there is no communication within an open Opportunity during a specific time period.</p>
<ul>
    <li>
        <p>The Opportunity stage is not 100% Won/Lost</p>
    </li>
    <li>
        <p>Opportunity close date is equal to or later than TODAY</p>
    </li>
    <li>
        <p>No scheduled meeting found for the Opportunity</p>
    </li>
    <li>
        <p>For Opportunities with a stage less than 50%:</p>
        <ul>
            <li>
                <p>No activity (email/meeting) found for the Opportunity within the last 30 days</p>
            </li>
        </ul>
    </li>
    <li>
        <p>For Opportunities with a stage 50% and more:</p>
        <ul>
            <li>
                <p>No activity (email/meeting) found for the Opportunity during the last 15 days</p>
            </li>
        </ul>
    </li>
    <li>
        <p>Auto-dismiss signals if:</p>
        <ul>
            <li>
                <p>Activity appeared in the Opportunity</p>
            </li>
            <li>
                <p>SF Next step was updated</p>
            </li>
            <li>
                <p>New scheduled meetings appeared&nbsp;</p>
            </li>
        </ul>
    </li>
    <li>
        <p>Signal recipient: Opportunity owner</p>
    </li>
</ul>

<p> 
<img src="..\..\assets\images\Internal-Use\signals-parameters\no-interaction-with-the-open-opportunity-prospects.png" class="minimized">
</p>
&nbsp;  

<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <h3>Parameters</h3>
            </th>
            <th>
                <p />
            </th>
        </tr>
        <tr>
            <td>
                <p><strong>Trigger</strong></p>
                <ul>
                    <li>
                        <p>Enabled/Disabled – default value – False</p>
                    </li>
                    <li>
                        <p>After stage boundary period (days) – default value – 15</p>
                    </li>
                    <li>
                        <p>Before stage boundary period (days) – default value – 30</p>
                    </li>
                    <li>
                        <p>Repeat signal after dismiss interval (days) – default value – 7</p>
                    </li>
                    <li>
                        <p>Opportunity CloseDate upper boundary (days)&nbsp; – default value – 180</p>
                    </li>
                    <li>
                        <p>Stage boundary value – default value – 50</p>
                    </li>
                    <li>
                        <p>Signal body template</p>
                    </li>
                    <li>
                        <p>Filter</p>
                    </li>
                </ul>
            </td>
            <td>
                <p><strong>Action</strong></p>
                <ul>
                    <li>
                        <p>Score – default value – &quot;-3&quot;</p>
                    </li>
                    <li>
                        <p>Dismiss the signal automatically after (hours) – default value – 336</p>
                    </li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>

<details><summary>Click to see the Configurable Parameters</summary> 

<h3>Configurable Parameters</h3>

<p>Configuration parameters are stored in the&nbsp;<strong>NoCommunicationInOpenOpportunityForLastNDaysConfiguration</strong> table in the signals database.</p>
<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <p>Parameter</p>
            </th>
            <th>
                <p>Description</p>
            </th>
            <th>
                <p>Default value / Comments</p>
            </th>
        </tr>
        <tr>
            <td>
                <p>Schedule</p>
            </td>
            <td>
                <p><a href="https://en.wikipedia.org/wiki/Cron">Cron</a> recurrence rule to execute this job (<a href="https://crontab.guru/">this</a> editor may be useful)</p>
            </td>
            <td>
                <p>0&nbsp;*/1&nbsp;*&nbsp;*&nbsp;*</p>
                <p>Please note that currently, only  the UTC time zone is supported, so if you want<br />the signal to appear at 9:00 on the user&rsquo;s time zone, you should specify the correct UTC date/time value in the schedule</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>AutoDismissSignalAfterHours</p>
            </td>
            <td>
                <p>For how long the signal remains actual since its due date (the number of hours). After the specified time period (number of hours), the signal is auto-dismissed</p>
            </td>
            <td>
                <p>336</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalScore</p>
            </td>
            <td>
                <p>Score to assign to the created signal</p>
            </td>
            <td>
                <p>-3</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>StageBoundaryValue</p>
            </td>
            <td>
                <p>This value is used to split Opportunities into 2 sets:</p>
                <ul>
                    <li>
                        <p>Opportunities with Probability exceeding or equal to this value</p>
                    </li>
                    <li>
                        <p>Opportunities with a Probability less than this value</p>
                    </li>
                </ul>
                <p>You can configure separate date range for each set.</p>
            </td>
            <td>
                <p>50</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>AfterStageBoundaryPeriodInDays</p>
            </td>
            <td>
                <p>This value is used to construct dates filter for Opportunities having [<strong>Probability</strong>] &gt;= [<strong>StageBoundaryValue</strong>]<br />and to calculate dates range the activities for Opportunities must fall within:</p>
                <p>oppt[<strong>Probability</strong>] &gt;= [<strong>StageBoundaryValue</strong>] and [<strong>CreatedDate</strong>] &lt;= [<strong>UtcCurrentDate</strong> - <strong>AfterStageBoundaryPeriodInDays</strong>]</p>
            </td>
            <td>
                <p>15 days</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>BeforeStageBoundaryPeriodInDays</p>
            </td>
            <td>
                <p>This value is used to construct dates filter for Opportunities having [<strong>Probability</strong>] &lt; [<strong>StageBoundaryValue</strong>]<br />and to calculate dates range the activities for Opportunities must fall within:</p>
                <p>oppt[<strong>Probability</strong>] &lt; [<strong>StageBoundaryValue</strong>] and [<strong>CreatedDate</strong>] &lt;= [<strong>UtcCurrentDate</strong> - <strong>BeforeStageBoundaryPeriodInDays</strong>]</p>
            </td>
            <td>
                <p>30 days</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>RepeatSignalAfterDismissIntervalInDays</p>
            </td>
            <td>
                <p>Interval for repeating dismissed signal</p>
            </td>
            <td>
                <p>7 days</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>OpportunityCloseDateUpperBoundaryInDays</p>
            </td>
            <td>
                <p>This value is used to construct dates range filter for Opportunities [<strong>CloseDate</strong>] field value:</p>
                <p>oppty[<strong>CloseDate</strong>] &lt;=&nbsp;[<strong>UtcCurrentDate</strong> + <strong>OpportunityCloseDateUpperBoundaryInDays</strong>]</p>
            </td>
            <td>
                <p>180 days</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SalesForceOpportunitiesMasterFilter</p>
            </td>
            <td>
                <p>Additional filter that can be applied for selected Opportunities</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalBodyTemplate</p>
            </td>
            <td>
                <p>Razor page signal body template</p>
            </td>
            <td>
                <p>See below</p>
            </td>
        </tr>
    </tbody>
</table>
</details>


<details><summary>Click to see the default signal body template</summary>   

<p></p>
<p><b>Default signal body template</b></p>

```
<div class="signals-body">
    @if (Model.LastTouch == null)
    {
        <h3>No activities found</h3>
    }
    else
    {
        if (!string.IsNullOrEmpty(Model.LastTouch.Recipients))
        {
            <b>Suggested action:</b>
            <ul>
                <li>Send follow up to @Model.LastTouch.Recipients</li>
            </ul>
        }
        <p/>
        <b>Last @Model.LastTouch.ActivityType:</b>
        <ul>
            <li><b>Subject:</b> @Model.LastTouch.Subject</li>
            <li><b>Date:</b> @Model.LastTouch.Date</li>
            <li><b>From:</b> @Model.LastTouch.From</li>
            <li><b>To:</b> @Model.LastTouch.To</li>
            <li><b>Cc:</b> @Model.LastTouch.Cc</li>
        </ul>
 
        if (!string.IsNullOrEmpty(Model.LastTouch.Body))
        {
            <hr/>
            @Raw(@Model.LastTouch.Body)
        }
    }
    </div>
    
    <style>
    .text-truncate {
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        display: inline-block;
        vertical-align: text-top;
        width: 500px;
    }
 
    .signals-body {
        font-family: 'Nunito Sans', sans-serif !important;
        font-size: 14px !important;
        font-weight: 400;
        line-height: 1.5;
        color: #3e5569;
        text-align: left;
    }
    </style>
    
```
</details>

&nbsp;  
***  
&nbsp;  

## 5. No next steps for an open opportunity  
    

**Description**  

<p>This signal reminds an Opportunity owner that there's no next step planned for an open Opportunity.</p>
<p>This signal is pushed to the Opportunity owner when there is no next step scheduled for an open Opportunity.</p>
<p>Use case</p>
<ul>
    <li>
        <p>Signal score: -5</p>
    </li>
    <li>
        <p>Opportunity stage is not in 100%</p>
    </li>
    <li>
        <p>The close date is actual</p>
    </li>
    <li>
        <p>Next meeting (SF or CH) AND SF task AND SF Next step wasn't found</p>
    </li>
    <li>
        <p>Check period: every 1 day</p>
    </li>
    <li>
        <p>Auto-resolve signal if some next step appeared for the Opportunity</p>
    </li>
</ul>

<p> 
<img src="..\..\assets\images\Internal-Use\signals-parameters\no-next-steps-for-an-open-opportunity.png" class="minimized">
</p>
&nbsp;  

<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <h3>Parameters</h3>
            </th>
            <th>
                <p />
            </th>
        </tr>
        <tr>
            <td>
                <p><strong>Trigger</strong></p>
                <ul>
                    <li>
                        <p>Enabled/Disabled &ndash; default value &ndash; True</p>
                    </li>
                    <li>
                        <p>Repeat the signal after expiration (days) &ndash; default value &ndash; 7</p>
                    </li>
                    <li>
                        <p>Filter</p>
                    </li>
                </ul>
            </td>
            <td>
                <p><strong>Action</strong></p>
                <ul>
                    <li>
                        <p>Score &ndash; default value &ndash; &quot;-5&quot;</p>
                    </li>
                    <li>
                        <p>Dismiss the signal automatically after (hours) &ndash; default value &ndash; 336</p>
                    </li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>


<details><summary>Click to see the Configurable Parameters</summary> 

<h3>Configurable Parameters</h3>  

<p>Configuration parameters are stored in the&nbsp;<strong>OpportunityNextStepNotScheduledConfiguration</strong> table in the signals database.</p>
<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <p>Parameter</p>
            </th>
            <th>
                <p>Description</p>
            </th>
            <th>
                <p>Default value / Comments</p>
            </th>
        </tr>
        <tr>
            <td>
                <p>SalesForceOpportunitiesMasterFilter</p>
            </td>
            <td>
                <p>SOQL filter expression to be added to the default Opportunities filter expression</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>RepeatSignalAfterDismissInDays</p>
            </td>
            <td>
                <p>Dismissed signal may be reactivated after specified time period (number of days) if it's still actual</p>
            </td>
            <td>
                <p>7</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Schedule</p>
            </td>
            <td>
                <p><a href="https://en.wikipedia.org/wiki/Cron">Cron</a> recurrence rule to execute this job (<a href="https://crontab.guru/">this</a> editor may be useful)</p>
            </td>
            <td>
                <p>0&nbsp;9&nbsp;*&nbsp;*&nbsp;*<br /></p>
                <p>Please note that currently only the UTC time zone is supported, so if you want<br />the signal to appear at 9:00 on the user&rsquo;s time zone, you should specify the correct UTC date/time value in the schedule</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>AutoDismissSignalAfterHours</p>
            </td>
            <td>
                <p>For how long the signal remains actual since its due date (the number of hours). After the specified time period (number of hours), the signal is auto-dismissed</p>
            </td>
            <td>
                <p>240</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalScore</p>
            </td>
            <td>
                <p>Score to assign to the created signal</p>
            </td>
            <td>
                <p>-5</p>
            </td>
        </tr>
    </tbody>
</table>
</details>

&nbsp;  
***  
&nbsp;  

## 6. Response delay from a prospect  
    
  
**Description**  

<p>This signal notifies the sales reps that their Leads haven't been responded to for a number of days.</p>
<p>This signal is sent if the external recipient of the email did not send any outbound email and did not participate in any meeting after the original email was sent.</p>
<p>If any Lead related to an active &quot;<em>no response from Lead</em>&quot; signal is no longer treated as significant or Contact related to that Lead was involved in any interaction (has an inbound or outbound email or participated in a meeting) since the original email was sent, then the corresponding signal is auto-dismissed.</p>

<p> 
<img src="..\..\assets\images\Internal-Use\signals-parameters\response-delay-from-a-prospect.png" class="minimized">
</p>
&nbsp;  

<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <h3>Parameters</h3>
            </th>
            <th>
                <p />
            </th>
        </tr>
        <tr>
            <td>
                <p><strong>Trigger</strong></p>
                <ul>
                    <li>
                        <p>Enabled &ndash; default value &ndash; False</p>
                    </li>
                    <li>
                        <p>Skip Contacts in active drip campaign &ndash; default value &ndash; True</p>
                    </li>
                    <li>
                        <p>Lead identity field name &ndash; default value &ndash; Name</p>
                    </li>
                    <li>
                        <p>Lead identity field name &ndash; default value &ndash; SCC_Deduplication__c</p>
                    </li>
                    <li>
                        <p>Response check interval (days) &ndash; default value &ndash; 5</p>
                    </li>
                    <li>
                        <p>Filter</p>
                    </li>
                </ul>
            </td>
            <td>
                <p><strong>Action</strong></p>
                <ul>
                    <li>
                        <p>Score &ndash; default value &ndash; &quot;-1&quot;</p>
                    </li>
                    <li>
                        <p>Dismiss the signal automatically after (hours) &ndash; default value &ndash;&nbsp; 336</p>
                    </li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>

<details><summary>Click to see the Configurable Parameters</summary> 

<h3>Configurable Parameters</h3>
<p>Configuration parameters are stored in the <strong>NoResponseFromLeadConfiguration</strong> table in the signals database.</p>
<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <p>Parameter</p>
            </th>
            <th>
                <p>Description</p>
            </th>
            <th>
                <p>Default value</p>
            </th>
        </tr>
        <tr>
            <td>
                <p>ContextUserId</p>
            </td>
            <td>
                <p>Signals User ID that will be used to query data from Salesforce, PeopleGraph, Signals, and Drip. Therefore this user must have complete visibility in Salesforce, Signals, and Drip</p>
            </td>
            <td>
                <p>&ndash;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsBlocked</p>
            </td>
            <td>
                <p>Flag indicating whether this job is disabled by {{ short_company_name }} authority (i.e., CSM, DevOps, admins, etc.)</p>
            </td>
            <td>
                <p>False</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsEnabled</p>
            </td>
            <td>
                <p>Flag indicating whether this job is enabled by tenant owner (i.e., customer)</p>
            </td>
            <td>
                <p>True</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Schedule</p>
            </td>
            <td>
                <p><a href="https://en.wikipedia.org/wiki/Cron">Cron</a> recurrence rule to execute this job (<a href="https://crontab.guru/">this</a> editor may be useful)</p>
            </td>
            <td>
                <p>0 */2 * * 1-5</p>
                <p>(i.e., every two hours on workdays)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>AutoDismissSignalAfterHours</p>
            </td>
            <td>
                <p>For how long the signal remains actual since its due date (the number of hours). After the specified time period (number of hours), the signal is auto-dismissed</p>
            </td>
            <td>
                <p>240</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalScore</p>
            </td>
            <td>
                <p>Score to assign to the created signal</p>
            </td>
            <td>
                <p>-1</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ResponseCheckWorkdays</p>
            </td>
            <td>
                <p>For how long to wait (the number or business days) since email receipt before generating the &quot;no response from Lead&quot; signal</p>
            </td>
            <td>
                <p>5</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>LeadFilter</p>
            </td>
            <td>
                <p>SOQL query to select only significant leads</p>
                <p>(e.g. Lead_Score_SQL__c = 'X1' OR Lead_Score_SQL__c = 'X2')</p>
            </td>
            <td>
                <p>&ndash;</p>
                <p>(i.e., all Leads are applicable)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>LeadIdentityFieldName</p>
            </td>
            <td>
                <p>Name of Salesforce Lead field, which identifies Lead. This field's value is used in the signal subject to reference the Lead.</p>
                <p>e.g.</p>
                <p>&quot;No response from our side to X1 lead...&quot; if&nbsp;LeadIdentityFieldName =&nbsp;Lead_Score_SQL__c</p>
                <p>&quot;No response from our side to John Dow lead...&quot; if&nbsp;LeadIdentityFieldName =&nbsp;Name.</p>
                <p>&quot;No response from our side to <a href="mailto:john.dow@domain.com">john.dow@domain.com</a> lead...&quot; if&nbsp;LeadIdentityFieldName =&nbsp;Email.</p>
            </td>
            <td>
                <p>Name</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SkipContactsInActiveDripCampaign</p>
            </td>
            <td>
                <p>Flag indicating whether to skip Leads that are currently under an active Drip sequence</p>
            </td>
            <td>
                <p>True</p>
            </td>
        </tr>
    </tbody>
</table>
</details>

&nbsp;  
***  
&nbsp;  

## 7. Response delay from the open opportunity prospect
  
  
**Description**  

<p>This signal notifies the sales reps when their Opportunity contacts haven't been responded to for a number of days.</p>
<p>This signal is sent if any Contact related to the same Opportunity as the original recipient of the email did not send any outbound email and did not participate in any meeting after the original email was sent.</p>
<p>If any Opportunity related to an active &quot;<em>no response from Opportunity</em>&quot; signal is no longer treated as significant, or Contact related to that Opportunity was involved in any interaction (has an inbound or outbound email or participated in a meeting) since the original email was sent then corresponding signal is auto-dismissed.</p>

<p> 
<img src="..\..\assets\images\Internal-Use\signals-parameters\response-delay-from-the-open-opportunity-prospect.png" class="minimized">
</p>
&nbsp;  

<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <h3>Parameters</h3>
            </th>
            <th>
                <p />
            </th>
        </tr>
        <tr>
            <td>
                <p><strong>Trigger</strong></p>
                <ul>
                    <li>
                        <p>Enabled &ndash; default value &ndash; True</p>
                    </li>
                    <li>
                        <p>Match Opportunities by Account &ndash; default value &ndash; True</p>
                    </li>
                    <li>
                        <p>Skip Contacts in active drip campaign &ndash; default value &ndash; True</p>
                    </li>
                    <li>
                        <p>Email Message Id field on Task &ndash; default value &ndash; SCC_Deduplication__c</p>
                    </li>
                    <li>
                        <p>Response check interval (days) &ndash; default value &ndash; 5</p>
                    </li>
                    <li>
                        <p>Filter</p>
                    </li>
                </ul>
            </td>
            <td>
                <p><strong>Action</strong></p>
                <ul>
                    <li>
                        <p>Score &ndash; default value &ndash; &quot;-1&quot;</p>
                    </li>
                    <li>
                        <p>Dismiss the signal automatically after (hours) &ndash; default value &ndash;&nbsp;336</p>
                    </li>
                </ul>
                <p />
            </td>
        </tr>
    </tbody>
</table>


<details><summary>Click to see the Configurable Parameters</summary>   

<h3>Configurable Parameters</h3>
<p>Configuration parameters are stored in the <strong>NoResponseFromOpportunityConfiguration</strong> table in the signals database.</p>
<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <p>Parameter</p>
            </th>
            <th>
                <p>Description</p>
            </th>
            <th>
                <p>Default value</p>
            </th>
        </tr>
        <tr>
            <td>
                <p>ContextUserId</p>
            </td>
            <td>
                <p>Signals User ID that will be used to query data from Salesforce, PeopleGraph, Signals, and Drip. Therefore this user must have complete visibility in Salesforce, Signals, and Drip</p>
            </td>
            <td>
                <p>&ndash;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsBlocked</p>
            </td>
            <td>
                <p>Flag indicating whether this job is disabled by {{ short_company_name }} authority (i.e., CSM, DevOps, admins, etc.)</p>
            </td>
            <td>
                <p>False</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsEnabled</p>
            </td>
            <td>
                <p>Flag indicating whether this job is enabled by tenant owner (i.e., customer)</p>
            </td>
            <td>
                <p>True</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Schedule</p>
            </td>
            <td>
                <p><a href="https://en.wikipedia.org/wiki/Cron">Cron</a> recurrence rule to execute this job (<a href="https://crontab.guru/">this</a> editor may be useful)</p>
            </td>
            <td>
                <p>0 */2 * * 1-5</p>
                <p>(i.e., every two hours on workdays)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>AutoDismissSignalAfterHours</p>
            </td>
            <td>
                <p>For how long the signal remains actual since its due date (the number of hours). After the specified time period (number of hours), the signal is auto-dismissed</p>
            </td>
            <td>
                <p>240</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalScore</p>
            </td>
            <td>
                <p>Score to assign to the created signal</p>
            </td>
            <td>
                <p>-1</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ResponseCheckWorkdays</p>
            </td>
            <td>
                <p>For how long to wait (the number or business days) since email receipt before generating the &quot;no response from Opportunity&quot; signal</p>
            </td>
            <td>
                <p>5</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>OpportunityFilter</p>
            </td>
            <td>
                <p>SOQL query WHERE clause to select only significant Opportunities</p>
                <p>(e.g. Amount &gt; 10000)</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>MatchOpportunitiesByAccount</p>
            </td>
            <td>
                <p>Flag indicating how to find the Opportunities that are related to email:</p>
                <ul>
                    <li>
                        <p>email participant's address matches Salesforce contact, that is assigned to the Opportunity contact role (False)</p>
                    </li>
                    <li>
                        <p>email participant's address matches a contact that is assigned to Opportunity contact role or Contact and Opportunity are bound to the same account, or email domain matches parent account website (True)</p>
                    </li>
                </ul>
            </td>
            <td>
                <p>True</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SkipContactsInActiveDripCampaign</p>
            </td>
            <td>
                <p>Flag indicating whether to skip contacts that are currently under an active Drip sequence</p>
            </td>
            <td>
                <p>True</p>
            </td>
        </tr>
    </tbody>
</table>
</details>

&nbsp;  
***  
&nbsp;  

## 8. Response delay to a prospect

**Description**  

<p>This signal notifies the sales reps that an email from a Lead hasn't been replied to for a number of days.</p>
<p>This signal is sent if the sender of the email did not receive any inbound emails and did not participate in any meeting after the original email was sent.</p>
<p>If any lead related to an active &quot;no response to Lead&quot; signal is no longer treated as significant, or Contact related to that Lead was involved in any kind of interaction (has an inbound or outbound email or participated in a meeting) since the original email was sent then corresponding signal is auto-dismissed.</p>

<p> 
<img src="..\..\assets\images\Internal-Use\signals-parameters\response-delay-to-a-prospect.png" class="minimized">
</p>
&nbsp;

<table data-layout="default">
    <tbody>
        <tr>
            <th colspan="2">
                <h3>Parameters</h3>
            </th>
        </tr>
        <tr>
            <td>
                <p><strong>Trigger</strong></p>
                <ul>
                    <li>
                        <p>Enabled &ndash; default value &ndash; False</p>
                    </li>
                    <li>
                        <p>Skip Contacts in active drip campaign &ndash; default value &ndash; True</p>
                    </li>
                    <li>
                        <p>Lead identity field name &ndash; default value &ndash; Name</p>
                    </li>
                    <li>
                        <p>Lead identity field name &ndash; default value &ndash; SCC_Deduplication__c</p>
                    </li>
                    <li>
                        <p>Response check interval (days) &ndash; default value &ndash; 5</p>
                    </li>
                    <li>
                        <p>Filter</p>
                    </li>
                </ul>
            </td>
            <td>
                <p><strong>Action</strong></p>
                <ul>
                    <li>
                        <p>Score &ndash; default value &ndash; &quot;-1&quot;</p>
                    </li>
                    <li>
                        <p>Dismiss the signal automatically after (hours) &ndash; default value &ndash; 336</p>
                    </li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>


<details><summary>Click to see the Configurable Parameters</summary> 

<h3>Configurable Parameters</h3>
<p>Configuration parameters are stored in the <strong>NoResponseToLeadConfiguration</strong> table in the signals database.</p>
<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <p>Parameter</p>
            </th>
            <th>
                <p>Description</p>
            </th>
            <th>
                <p>Default value</p>
            </th>
        </tr>
        <tr>
            <td>
                <p>ContextUserId</p>
            </td>
            <td>
                <p>Signals User ID that will be used to query data from Salesforce, PeopleGraph, Signals, and Drip. Therefore this user must have complete visibility in Salesforce, Signals, and Drip</p>
            </td>
            <td>
                <p>&ndash;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsBlocked</p>
            </td>
            <td>
                <p>Flag indicating whether this job is disabled by {{ short_company_name }} authority (i.e., CSM, DevOps, admins, etc.)</p>
            </td>
            <td>
                <p>False</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsEnabled</p>
            </td>
            <td>
                <p>Flag indicating whether this job is enabled by tenant owner (i.e., customer)</p>
            </td>
            <td>
                <p>True</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Schedule</p>
            </td>
            <td>
                <p><a href="https://en.wikipedia.org/wiki/Cron">Cron</a> recurrence rule to execute this job (<a href="https://crontab.guru/">this</a> editor may be useful)</p>
            </td>
            <td>
                <p>0 */2 * * 1-5</p>
                <p>(i.e., every two hours on workdays)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>AutoDismissSignalAfterHours</p>
            </td>
            <td>
                <p>For how long the signal remains actual since its due date (the number of hours). After the specified time period (number of hours), the signal is auto-dismissed</p>
            </td>
            <td>
                <p>240</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalScore</p>
            </td>
            <td>
                <p>Score to assign to the created signal</p>
            </td>
            <td>
                <p>-1</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ResponseCheckWorkdays</p>
            </td>
            <td>
                <p>The number of business days since email receipt before the &quot;no response to Lead&quot; signal is created</p>
            </td>
            <td>
                <p>5</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>LeadFilter</p>
            </td>
            <td>
                <p>SOQL query to select only significant leads</p>
                <p>(e.g. Lead_Score_SQL__c = 'X1' OR Lead_Score_SQL__c = 'X2')</p>
            </td>
            <td>
                <p>&ndash;</p>
                <p>(i.e. all Leads are applicable)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>LeadIdentityFieldName</p>
            </td>
            <td>
                <p>Name of Salesforce Lead field, which identifies lead. This field's value is used in the signal subject to reference the Lead.</p>
                <p>e.g.</p>
                <p>&quot;No response from our side to X1 lead...&quot; if&nbsp;LeadIdentityFieldName =&nbsp;Lead_Score_SQL__c</p>
                <p>&quot;No response from our side to John Dow lead...&quot; if&nbsp;LeadIdentityFieldName =&nbsp;Name.</p>
                <p>&quot;No response from our side to <a href="mailto:john.dow@domain.com">john.dow@domain.com</a> lead...&quot; if&nbsp;LeadIdentityFieldName =&nbsp;Email.</p>
            </td>
            <td>
                <p>Name</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SkipContactsInActiveDripCampaign</p>
            </td>
            <td>
                <p>Flag indicating whether to skip Leads that are currently involved in an active Drip sequence</p>
            </td>
            <td>
                <p>True</p>
            </td>
        </tr>
    </tbody>
</table>
</details>  

&nbsp;  
***  
&nbsp;  

## 9. Response delay to the open opportunity prospect


**Description**

<p>This signal notifies sales reps that an email from an Opportunity hasn't been replied to for a number of days.</p>
<p>This signal is generated if the sender of the email did not receive any inbound emails and did not participate in any meeting after the original email was sent.</p>
<p>If any opportunity related to an active &quot;<em>no response to Opportunity</em>&quot; signal is no longer treated as significant, or Contact related to that Opportunity was involved in any interaction (has an inbound or outbound email or participated in the meeting) since the original email was sent then corresponding signal is auto-dismissed.</p>

<p> 
<img src="..\..\assets\images\Internal-Use\signals-parameters\response-delay-to-the-open-opportunity-prospect.png" class="minimized">
</p>
&nbsp; 

<table data-layout="default">
    <tbody>
        <tr>
            <th colspan="2">
                <p><strong>Parameters</strong></p>
            </th>
        </tr>
        <tr>
            <td>
                <p><strong>Trigger</strong></p>
                <ul>
                    <li>
                        <p>Enabled &ndash; default value &ndash; True</p>
                    </li>
                    <li>
                        <p>Match Opportunities by Account &ndash; default value &ndash; True</p>
                    </li>
                    <li>
                        <p>Skip Contacts in active drip campaign &ndash; default value &ndash; True</p>
                    </li>
                    <li>
                        <p>Response check interval (days) &ndash; default value &ndash; 5</p>
                    </li>
                    <li>
                        <p>Email Message Id field on Task &ndash; default value &ndash; SCC_Deduplication__c</p>
                    </li>
                    <li>
                        <p>Filter</p>
                    </li>
                </ul>
            </td>
            <td>
                <p><strong>Action</strong></p>
                <ul>
                    <li>
                        <p>Score &ndash; default value &ndash; &quot;-1&quot;</p>
                    </li>
                    <li>
                        <p>Dismiss the signal automatically after (hours) &ndash; default value &ndash; 336</p>
                    </li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>


<details><summary>Click to see the Configurable Parameters</summary> 

<h3>Configurable Parameters</h3>
<p>Configuration parameters are stored in the <strong>NoResponseToOpportunityConfiguration</strong> table in the signals database.</p>
<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <p>Parameter</p>
            </th>
            <th>
                <p>Description</p>
            </th>
            <th>
                <p>Default value</p>
            </th>
        </tr>
        <tr>
            <td>
                <p>ContextUserId</p>
            </td>
            <td>
                <p>Signals User ID that will be used to query data from Salesforce, PeopleGraph, Signals, and Drip. Therefore this user must have complete visibility in Salesforce, Signals, and Drip</p>
            </td>
            <td>
                <p>&ndash;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsBlocked</p>
            </td>
            <td>
                <p>Flag indicating whether this job is disabled by {{ short_company_name }} authority (i.e., CSM, DevOps, admins, etc.)</p>
            </td>
            <td>
                <p>False</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsEnabled</p>
            </td>
            <td>
                <p>Flag indicating whether this job is enabled by tenant owner (i.e., customer)</p>
            </td>
            <td>
                <p>True</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Schedule</p>
            </td>
            <td>
                <p><a href="https://en.wikipedia.org/wiki/Cron">Cron</a> recurrence rule to execute this job (<a href="https://crontab.guru/">this</a> editor may be useful)</p>
            </td>
            <td>
                <p>0 */2 * * 1-5</p>
                <p>(i.e., every two hours on workdays)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>AutoDismissSignalAfterHours</p>
            </td>
            <td>
                <p>For how long the signal remains actual since its due date (the number of hours). After the specified time period (number of hours), the signal is auto-dismissed</p>
            </td>
            <td>
                <p>240</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalScore</p>
            </td>
            <td>
                <p>Score to assign to the created signal</p>
            </td>
            <td>
                <p>-1</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ResponseCheckWorkdays</p>
            </td>
            <td>
                <p>For how long to wait (the number or business days) since email receipt before generating the &quot;no response to Opportunity&quot; signal</p>
            </td>
            <td>
                <p>5</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>OpportunityFilter</p>
            </td>
            <td>
                <p>SOQL query WHERE clause to select only significant Opportunities</p>
                <p>(e.g. Amount &gt; 10000)</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>MatchOpportunitiesByAccount</p>
            </td>
            <td>
                <p>Flag indicating how to find Opportunities that are related to email:</p>
                <ul>
                    <li>
                        <p>email participant's address matches Salesforce contact, that is assigned to the Opportunity contact role (False)</p>
                    </li>
                    <li>
                        <p>email participant's address matches a Contact that is assigned to Opportunity contact role or Contact and Opportunity are bound to the same account, or email domain matches parent account website (True)</p>
                    </li>
                </ul>
            </td>
            <td>
                <p>True</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SkipContactsInActiveDripCampaign</p>
            </td>
            <td>
                <p>Flag indicating whether to skip contacts that are currently involved in an active Drip sequence</p>
            </td>
            <td>
                <p>True</p>
            </td>
        </tr>
    </tbody>
</table>
</details>

&nbsp;  
***  
&nbsp;  

## 10. Opportunity renewal reminder


**Decription**

<p>This signal notifies about the upcoming renewal date for your Opportunity</p>
<ul>
    <li>
        <p>The customer sets up an opportunities filter to select matching records</p>
    </li>
    <li>
        <p>Signals for matching Opportunities are generated every business day, and the Opportunity's CloseDate value is used to generate the signal titles</p>
    </li>
    <li>
        <p>If a signal for a given Opportunity already exists, but it's &quot;too old&quot;, a reminder signal is generated</p>
    </li>
    <li>
        <p>If a reminder already exists, but it's &quot;too old&quot; it's &quot;snoozed&quot;</p>
    </li>
</ul>

<p> 
<img src="..\..\assets\images\Internal-Use\signals-parameters\opportunity-renewal-reminder.png" class="minimized">
</p>
&nbsp; 

<table data-layout="default">
    <tbody>
        <tr>
            <th colspan="2">
                <h3>Patameters</h3>
            </th>
        </tr>
        </tr>
        <tr>
            <td>
                <p><strong>Trigger</strong></p>
                <ul>
                    <li>
                        <p>Enabled &ndash; default value &ndash; False</p>
                    </li>
                    <li>
                        <p>Repeat the signal after expiration (days) &ndash; default value &ndash; 7</p>
                    </li>
                    <li>
                        <p>Overdue (days) - default value &ndash; 3</p>
                    </li>
                    <li>
                        <p>Filter (default value)</p>
                    </li>
                </ul>
            </td>
            <td>
                <p><strong>Action</strong></p>
                <ul>
                    <li>
                        <p>Score &ndash; default value &ndash; &quot;-1&quot;</p>
                    </li>
                    <li>
                        <p>Dismiss the signal automatically after (hours) &ndash; default value &ndash;&nbsp; 336</p>
                    </li>
                    <li>
                        <p><a href="https://docs.revenuegrid.com/ri/fast/articles/signals-settings-and-parameters/#15_summary_team_meetings_with_customers:~:text=Click%20to%20see%20the%20default%20signal%20body%20template">Signal body template</a></p>
                    </li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>


<details><summary>Click to see the Configurable Parameters</summary>   

<h3>Configurable Parameters</h3>
<p>Configuration parameters are stored in the&nbsp;<strong>OpportunityRenewalReminderConfiguration</strong>&nbsp;table in the signals database.</p>
<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <p>Parameter</p>
            </th>
            <th>
                <p>Description</p>
            </th>
            <th>
                <p>Default value / Comments</p>
            </th>
        </tr>
        <tr>
            <td>
                <p>Schedule</p>
            </td>
            <td>
                <p><a href="https://en.wikipedia.org/wiki/Cron">Cron</a> recurrence rule to execute this job (<a href="https://crontab.guru/">this</a> editor may be useful)</p>
            </td>
            <td>
                <p>0 0 * * 1-5</p>
                <p>Please note that currently only the UTC time zone is supported, so if you want<br />the signal to appear at 9:00 on the user's time zone, you should specify the correct UTC date/time value in the schedule</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>AutoDismissSignalAfterHours</p>
            </td>
            <td>
                <p>For how long the signal remains actual since its due date (the number of hours). After the specified time period (number of hours), the signal is auto-dismissed</p>
            </td>
            <td>
                <p>336</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalScore</p>
            </td>
            <td>
                <p>Score to assign to the created signal</p>
            </td>
            <td>
                <p>-1</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>RepeatSignalAfterDismissIntervalInDays</p>
            </td>
            <td>
                <p>Interval for repeating dismissed signal</p>
            </td>
            <td>
                <p>7 days</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SalesForceOpportunitiesFilter</p>
            </td>
            <td>
                <p>Custom filter for matching Opportunities selection</p>
            </td>
            <td>
                <p>See the signal workflow section</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>OverdueInDays</p>
            </td>
            <td>
                <p>This value is used to find outdated signals/reminders.<br />if signal's/reminder's [DueDate] &lt; [CurrentUtcDate] -&nbsp;[OverdueInDays] it is considered to be outdated</p>
            </td>
            <td>
                <p>3</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalBodyTemplate</p>
            </td>
            <td>
                <p>Razor page signal body template</p>
            </td>
            <td>
                <p>See below</p>
            </td>
        </tr>
    </tbody>
</table>
</details>

<details><summary>Click to see the default signal body template</summary>   

<p></p>
<p><b>Default signal body template</b></p>

```
<div class="signals-body">
    <h3>Suggested Actions:</h3>
    <ul>
        <li>Update the renewal date for @Helper.FormatSalesforceLink(@Model.Opportunity.Name, @Model.Opportunity.Id)</li>
        @if (!string.IsNullOrEmpty(Model.Opportunity?.Account?.Id) && !string.IsNullOrEmpty(Model.Opportunity?.Account?.Name))
        {
            <li>Follow up with your contact from @Helper.FormatSalesforceLink(@Model.Opportunity.Account.Name, @Model.Opportunity.Account.Id)</li>
        }
    </ul>
</div>
 
<style>
    .signals-body {
        font-family: 'Nunito Sans', sans-serif !important;
        font-size: 14px !important;
        font-weight: 400;
        line-height: 1.5;
        color: #3e5569;
        text-align: left;
    }
</style>
    
```
</details>

&nbsp;  
***  
&nbsp;  

## 11. The close date doesn't correspond to the stage

  
**Description**  

<p>This signal notifies when low-stage Opportunities get close to their Close dates.</p>
<p>The Opportunity stage alert signal is intended to notify a user when any of their Opportunities does not meet recommendations depending on the time remaining to the Opportunity close date. Recommendations are based on the Opportunity&rsquo;s probability and next step update interval.</p>

<p> 
<img src="..\..\assets\images\Internal-Use\signals-parameters\the-close-date-doesn-t-correspond-to-stage.png" class="minimized">
</p>
&nbsp;  

<table data-layout="default">
    <tbody>
        <tr>
            <th colspan="2">
                <h3>Patameters</h3>
            </th>
        </tr>
        <tr>
            <td>
                <p><strong>Trigger</strong></p>
                <ul>
                    <li>
                        <p>Enabled &ndash; default value &ndash; False</p>
                    </li>
                    <li>
                        <p>Stage 1 days until CloseDate &ndash; default value &ndash; 30</p>
                    </li>
                    <li>
                        <p>Stage 1 Probability &ndash; default value &ndash; 50</p>
                    </li>
                    <li>
                        <p>Stage 1 next step update interval (days) &ndash; default value &ndash; 3</p>
                    </li>
                    <li>
                        <p>Stage 2 days until CloseDate &ndash; default value &ndash; 45</p>
                    </li>
                    <li>
                        <p>Stage 2 Probability &ndash; default value &ndash; 30</p>
                    </li>
                    <li>
                        <p>Stage 2 next step update interval (days) &ndash; default value &ndash; 0</p>
                    </li>
                    <li>
                        <p>Repeat the signal after expiration (days)&nbsp; &ndash; default value - 7</p>
                    </li>
                    <li>
                        <p>Stage 1 filter</p>
                    </li>
                    <li>
                        <p>Stage 2 filter</p>
                    </li>
                </ul>
            </td>
            <td>
                <p><strong>Action</strong></p>
                <ul>
                    <li>
                        <p>Score &ndash; default value &ndash; &quot;-1&quot;</p>
                    </li>
                    <li>
                        <p>Dismiss the signal automatically after (hours) &ndash; default value &ndash; 72</p>
                    </li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>


<details><summary>Click to see the Configurable Parameters</summary> 

<h3>Configurable Parameters</h3>
<p>Configuration parameters are stored in the <strong>OpportunityStageAlertConfiguration</strong> table in the signals database.</p>
<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <p>Parameter</p>
            </th>
            <th>
                <p>Description</p>
            </th>
            <th>
                <p>Default value</p>
            </th>
        </tr>
        <tr>
            <td>
                <p>ContextUserId</p>
            </td>
            <td>
                <p>Signals User ID that will be used to query data from Salesforce. Therefore this user must have complete visibility in Salesforce</p>
            </td>
            <td>
                <p>-</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsBlocked</p>
            </td>
            <td>
                <p>Flag indicating whether this job is disabled by {{ short_company_name }} authority (i.e., CSM, DevOps, admins, etc.)</p>
            </td>
            <td>
                <p>False</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsEnabled</p>
            </td>
            <td>
                <p>Flag indicating whether this job is enabled by tenant owner (i.e., customer)</p>
            </td>
            <td>
                <p>True</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Schedule</p>
            </td>
            <td>
                <p><a href="https://en.wikipedia.org/wiki/Cron">Cron</a> recurrence rule to execute this job (<a href="https://crontab.guru/">this</a> editor may be useful)</p>
            </td>
            <td>
                <p>*/30 * * * 1-5</p>
                <p>(i.e. every thirty minutes)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>AutoDismissSignalAfterHours</p>
            </td>
            <td>
                <p>For how long the signal remains actual since its due date (the number of hours). After the specified time period (number of hours), the signal is auto-dismissed</p>
            </td>
            <td>
                <p>72</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalScore</p>
            </td>
            <td>
                <p>Score to assign to the created signal</p>
            </td>
            <td>
                <p>-1</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>RepeatSignalAfterDismissDays</p>
            </td>
            <td>
                <p>The number of days to wait before sending the signal after the user dismissed it if the opportunity still does not meet the recommendation.</p>
                <p>Valid value range: [-1;&nbsp;2147483647].</p>
                <p>-1 means that this signal will never be sent again for a particular Opportunity after the user dismisses it.</p>
            </td>
            <td>
                <p>7</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Stage1DaysTillCloseDate</p>
            </td>
            <td>
                <p>Number of days before the Opportunity close date for the first recommendation</p>
                <p>Valid value range: [1;&nbsp;2147483647].</p>
            </td>
            <td>
                <p>30</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Stage1Probability</p>
            </td>
            <td>
                <p>Expected probability for the first recommendation</p>
                <p>Valid value range: [1;&nbsp;99].</p>
            </td>
            <td>
                <p>50</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Stage1NextStepUpdateIntervalDays</p>
            </td>
            <td>
                <p>Expected Opportunity next step update frequency for the first recommendation</p>
                <p>Valid value range:&nbsp;[0; 2147483647]</p>
                <p>0 means that the next step update frequency does not matter</p>
            </td>
            <td>
                <p>3</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Stage1OpportunityFilter</p>
            </td>
            <td>
                <p>SOQL query WHERE clause to select only a subset of Opportunities for the first recommendation</p>
                <p>(e.g. Amount &gt; 10000)</p>
            </td>
            <td>
                <p>-</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Stage2DaysTillCloseDate</p>
            </td>
            <td>
                <p>Number of days before the Opportunity close date for the second recommendation</p>
                <p>Valid value range: [1;&nbsp;2147483647].</p>
            </td>
            <td>
                <p>45</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Stage2Probability</p>
            </td>
            <td>
                <p>Expected probability for the send recommendation</p>
                <p>Valid value range: [1;&nbsp;99].</p>
            </td>
            <td>
                <p>30</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Stage2NextStepUpdateIntervalDays</p>
            </td>
            <td>
                <p>Expected Opportunity next step update frequency for the second recommendation</p>
                <p>Valid value range:&nbsp;[0; 2147483647]</p>
                <p>0 means that the next step update frequency does not matter</p>
            </td>
            <td>
                <p>0</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Stage2OpportunityFilter</p>
            </td>
            <td>
                <p>SOQL query WHERE clause to select only a subset of Opportunities for a second recommendation</p>
                <p>(e.g. Amount &gt; 10000)</p>
            </td>
            <td>
                <p>–</p>
            </td>
        </tr>
    </tbody>
</table>
</details>

&nbsp;  
***  
&nbsp;  

## 12. Context reminder before the meeting with a Prospect
  
  
**Description**  

<p>An automatic reminder for sales reps to mention a certain topic during upcoming events.</p>
<p>This signal is designed for people with the authority to set up signals for other users within the org.</p>
<p>This signal is a live recurrent reminder of sales playbook steps associated with the particular group of objects AND a signal for updates from the sales playbook.</p>

**Conditions** 
<ul>
    <li>
        <p>The user needs to set up a custom reminder linked to a certain activity type</p>
    </li>
    <li>
        <p>The recipient of the signal should be an event owner/event organizer</p>
    </li>
    <li>
        <p>Activities are taking place in the future, first &ndash; check ClickHouse, then use Salesforce as a source of data. If it is a call activity &ndash; only Salesforce</p>
    </li>
    <li>
        <p>Object/Activity type is defined by the user by filters</p>
    </li>
</ul>

<p> 
<img src="..\..\assets\images\Internal-Use\signals-parameters\context-reminder-before-the-meeting-with-a-prospect.png" class="minimized">
</p>
&nbsp;

<table data-layout="default">
 <tbody>
        <tr>
            <th colspan="2">
                <h3>Parameters</h3>
            </th>
        </tr>
        <tr>
            <td>
                <p><strong>Trigger</strong></p>
                <ul>
                    <li>
                        <p>Enabled &ndash; default value &ndash; True</p>
                    </li>
                    <li>
                        <p>Reminder period date (from)</p>
                    </li>
                    <li>
                        <p>Reminder period date (to)</p>
                    </li>
                    <li>
                        <p>Affected object:</p>
                        <ul>
                            <li>
                                <p>&nbsp;Lead</p>
                            </li>
                            <li>
                                <p>Contact</p>
                            </li>
                            <li>
                                <p>Opportunity</p>
                            </li>
                            <li>
                                <p>Account</p>
                            </li>
                        </ul>
                    </li>
                </ul>
                <ul>
                    <li>
                        <p>Activity source:</p>
                        <ul>
                            <li>
                                <p>Salesforce Event</p>
                            </li>
                            <li>
                                <p>Calendar Event</p>
                            </li>
                        </ul>
                    </li>
                </ul>
                <ul>
                    <li>
                        <p>Object filter – default value CreatedDate = LAST_N_DAYS:365</p>
                    </li>
                    <li>
                        <p>Event filter</p>
                    </li>
                </ul>
            </td>
            <td>
                <p><strong>Action</strong></p>
                <ul>
                    <li>
                        <p>Score &ndash; default value &ndash; &quot;0&quot;</p>
                    </li>
                    <li>
                        <p>Dismiss the signal automatically after (hours) &ndash; default value &ndash;&nbsp; 1 &ndash; twice for two reminders</p>
                    </li>
                    <li>
                        <p>Send a reminder before calendar event (mins)&nbsp; default value &ndash; 15</p>
                    </li>
                    <li>
                        <p>Signal text (Mandatory)</p>
                    </li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>

<details><summary>Click to see the Configurable Parameters</summary> 

<h3>Configurable Parameters</h3>
<p>Configuration parameters are stored in the <strong>MeetingReminderConfiguration</strong> table in the signals database.</p>
<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <p>Parameter</p>
            </th>
            <th>
                <p>Description</p>
            </th>
            <th>
                <p>Default value</p>
            </th>
        </tr>
        <tr>
            <td>
                <p>ContextUserId</p>
            </td>
            <td>
                <p>Signals User ID that will be used to query data from Salesforce. Therefore this user must have full visibility there.</p>
            </td>
            <td>
                <p>&ndash;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsBlocked</p>
            </td>
            <td>
                <p>Flag indicating whether this job is disabled by {{ short_company_name }} authority (i.e., CSM, DevOps, admins, etc.)</p>
            </td>
            <td>
                <p>False</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsEnabled</p>
            </td>
            <td>
                <p>Flag indicating whether this job is enabled by tenant owner (i.e., customer)</p>
            </td>
            <td>
                <p>True</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Schedule</p>
            </td>
            <td>
                <p><a href="https://en.wikipedia.org/wiki/Cron">Cron</a> recurrence rule to execute this job (<a href="https://crontab.guru/">this</a> editor may be useful)</p>
            </td>
            <td>
                <p>*/15 * * * 1-5</p>
                <p>(i.e., every 15 minutes)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>AutoDismissSignalAfterHours</p>
            </td>
            <td>
                <p>The number of hours signal remains actual since its due date. After the specified time period (number of hours), the signal is auto-dismissed</p>
            </td>
            <td>
                <p>72</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalScore</p>
            </td>
            <td>
                <p>Score to assign to the created signal</p>
            </td>
            <td>
                <p>0</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsTeamsNotificationEnabled</p>
            </td>
            <td>
                <p>Flag indicating whether this job should send a signal to Microsoft Teams bot</p>
            </td>
            <td>
                <p>true</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsPushNotificationEnabled</p>
            </td>
            <td>
                <p>Flag indicating whether this job should send signal as a push notification</p>
            </td>
            <td>
                <p>true</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>TeamsNotificationTemplate</p>
            </td>
            <td>
                <p>Microsoft Teams notification template</p>
            </td>
            <td>
                <p>The default template</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>RelatedObjectType</p>
            </td>
            <td>
                <p>Enum, defines a type of Salesforce object, meeting should be related to. Possible values:</p>
                <p>Lead = 0,<br />Contact = 1,<br />Opportunity = 2,<br />Account = 3</p>
            </td>
            <td>
                <p>0 (Lead)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>RelatedObjectTypeFilter</p>
            </td>
            <td>
                <p>SOQL string filter, applied to RelatedObjectType.<br />Default value for<br />Lead = 0 - &quot;CreatedDate = LAST_N_DAYS:365&quot;;Contact = 1 - &quot;&quot;<br />Opportunity = 2 - &quot;CloseDate = THIS_FISCAL_QUARTER&quot;;<br />Account = 3 - &quot;&quot;</p>
            </td>
            <td>
                <p>CreatedDate = LAST_N_DAYS:365</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>EventDataSource</p>
            </td>
            <td>
                <p>Enum, defines a source and object type of meetings processed by signal:</p>
                <p>SalesforceEvent = 0,<br />SalesforceCall = 1, (task)<br />Calendar = 2</p>
            </td>
            <td>
                <p>0 (Salesforce event)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SalesforceEventFilter</p>
            </td>
            <td>
                <p>SOQL string filter applied on event or task. Applied on EventDataSource != 2&nbsp;</p>
            </td>
            <td>
                <p>null (empty)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ContactRolesMode</p>
            </td>
            <td>
                <p>Enum, defines a mode of processing Opportunity contacts, applied only for RelatedObjectType = 2:</p>
                <p>Disabled = 0,<br />UseOnly = 1,<br />UseWithAccount = 2</p>
            </td>
            <td>
                <p>0 (Disabled)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ContactRolesNames</p>
            </td>
            <td>
                <p>JSON Array of contact roles to be filtered. Applied only when ContactRolesMode != 0.<br />Mandatory if ContactRolesMode = 1.</p>
            </td>
            <td>
                <p>[] (empty array)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SendReminderBeforeMinutes</p>
            </td>
            <td>
                <p>Minutes (more than 0) before the meeting when the signal should appear</p>
            </td>
            <td>
                <p>15</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ReminderMessage</p>
            </td>
            <td>
                <p>A reminder message string</p>
            </td>
            <td>
                <p>null (empty)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ActiveAfterDateTime</p>
            </td>
            <td>
                <p>A date-time, a job is active after (should be less than ActiveBeforeDateTime)</p>
            </td>
            <td>
                <p>DateTime.MinValue</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ActiveBeforeDateTime</p>
            </td>
            <td>
                <p>A date-time, a job is active before (should be greater than ActiveAfterDateTime)</p>
            </td>
            <td>
                <p>DateTime.MaxValue</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalBodyTemplate</p>
            </td>
            <td>
                <p>UI notification template</p>
            </td>
            <td>
                <p>The default template</p>
            </td>
        </tr>
    </tbody>
</table>
</details>

&nbsp;  
***  
&nbsp;  

## 13. Summary received for the past event

**Description**

<p>This signal notifies sales reps that they received the summary of the past event from the organizer.</p>
<p>The sales rep held the meeting with the customer and sent a summarizing email after the meeting. If the sales rep missed this step, the one would get a signal&nbsp;<a href="https://docs.revenuegrid.com/ri/fast/articles/signals-settings-and-parameters/#3_meeting_follow-up_reminder_for_the_open_opportunity_prospect">Follow up reminder after meeting with the Opportunity contact</a>.&nbsp;</p>  

The signal consists of the following data in&nbsp;summary:    
  
* The Opportunity Name  
* The Follow-up sender's Name  
* Email recipient's Names  
* Date of the email  
* Email body  
* Subject line


<p> 
<img src="..\..\assets\images\Internal-Use\signals-parameters\summary-received-for-the-past-event.png" class="minimized">
</p>
&nbsp; 


<table data-layout="default">
    <tbody>
        <tr>
            <th colspan="2">
                <h3>Parameters</h3>
            </th>
        </tr>
        <tr>
            <td>
                <p><strong>Trigger</strong></p>
                <ul>
                    <li>
                        <p>Enabled &ndash; default value &ndash; True</p>
                    </li>
                    <li>
                        <p>Match Opportunities by Account &ndash; default value &ndash; True</p>
                    </li>
                    <li>
                        <p>Max summary response time (hours) &ndash; default value &ndash; 4</p>
                    </li>
                    <li>
                        <p>Assignee (Mandatory)</p>
                    </li>
                    <li>
                        <p>Activity source:</p>
                        <ul>
                            <li>
                                <p>By hierarchy</p>
                            </li>
                            <li>
                                <p>By signals' IDs</p>
                            </li>
                        </ul>
                    </li>
                    <li>
                        <p>&quot;Hierarchy role name (Mandatory)&quot; or if chosen &quot;By signals ids&quot; the parameter named &quot;Team signals users ids&nbsp; (Mandatory)&quot;</p>
                    </li>
                    <li>
                        <p>Filter</p>
                    </li>
                </ul>
            </td>
            <td>
                <p><strong>Action</strong></p>
                <ul>
                    <li>
                        <p>Score &ndash; default value &ndash; &quot;0&quot;</p>
                    </li>
                    <li>
                        <p>Dismiss the signal automatically after (hours) &ndash; default value &ndash; 240</p>
                    </li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>

<details><summary>Click to see the Configurable Parameters</summary> 

<h3>Configurable Parameters</h3>
<p>Configuration parameters are stored in the <strong>SummaryReceivedForPastEventFromSalesRep</strong> table in the signals database.</p>
<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <p>Parameter</p>
            </th>
            <th>
                <p>Description</p>
            </th>
            <th>
                <p>Default value</p>
            </th>
        </tr>
        <tr>
            <td>
                <p>ContextUserId</p>
            </td>
            <td>
                <p>Signals User ID that will be used to query data from Salesforce, PeopleGraph, and Signals. Therefore this user must have complete visibility in Salesforce and Signals</p>
            </td>
            <td>
                <p>&ndash;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsBlocked</p>
            </td>
            <td>
                <p>Flag indicating whether this job is disabled by {{ short_company_name }} authority (i.e., CSM, DevOps, admins, etc.)</p>
            </td>
            <td>
                <p>False</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsEnabled</p>
            </td>
            <td>
                <p>Flag indicating whether this job is enabled by tenant owner (i.e., customer)</p>
            </td>
            <td>
                <p>True</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Schedule</p>
            </td>
            <td>
                <p><a href="https://en.wikipedia.org/wiki/Cron">Cron</a> recurrence rule to execute this job (<a href="https://crontab.guru/">this</a> editor may be useful)</p>
            </td>
            <td>
                <p>0 */2 * * *</p>
                <p>(i.e., every two hours)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>HierarchyRoleName</p>
            </td>
            <td>
                <p>Name of Salesforce role, for which hierarchy will be built&nbsp;(mandatory if TeamQueryMode = 0 (by hierarchy))</p>
            </td>
            <td>
                <p>CEO (*)</p>
                <p>(* - NULL by default, should be filled)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>AutoDismissSignalAfterHours</p>
            </td>
            <td>
                <p>The number of hours signal remains actual since its due date. After the specified time period (number of hours), the signal is auto-dismissed</p>
            </td>
            <td>
                <p>240</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalScore</p>
            </td>
            <td>
                <p>Score to assign to the created signal</p>
            </td>
            <td>
                <p>0</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>OpportunityFilter</p>
            </td>
            <td>
                <p>SOQL query WHERE clause intended to select only significant opportunities</p>
                <p>(e.g. Amount &gt; 10000)</p>
            </td>
            <td>
                <p>IsClosed &lt;&gt; true AND Probability &gt; 0</p>
                <p>(abovementioned filter cannot be changed; the custom filter is combined (using AND) with the base filter)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>MatchOpportunitiesByAccount</p>
            </td>
            <td>
                <p>Flag indicating how to find Opportunities that are related to event participants:</p>
                <ul>
                    <li>
                        <p>event participant's email matches the Contact that is assigned to the Opportunity contact role (False)</p>
                    </li>
                    <li>
                        <p>event participant's email matches the Contact that is assigned to the Opportunity contact role or Contact and Opportunity are bound to the same account (True)</p>
                    </li>
                </ul>
            </td>
            <td>
                <p>True</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>AssigneeUserId</p>
            </td>
            <td>
                <p>Mandatory.<br />The signals User ID of a person that will receive the signal.<br />The signal is displayed only if that person's email address is not present on a meeting follow-up email.</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>TeamSignalUsersIds</p>
            </td>
            <td>
                <p>A string, JSON array of signals User IDs of a team (mandatory if TeamQueryMode = 1 (by signal ids))</p>
            </td>
            <td>
                <p>JSON array of strings.<br />Sample: [&quot;33215A2E-A347-43D0-C507-08D98F71A95F&quot;]</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>TeamQueryMode</p>
            </td>
            <td>
                <p>Enum, values 0 &ndash; by hierarchy, 1 &ndash; by signals IDs; determines the strategy of querying users of a team</p>
            </td>
            <td>
                <p>0</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>MaxSummaryResponseTime</p>
            </td>
            <td>
                <p>The time span, the time between an event and a summary email</p>
            </td>
            <td>
                <p>4</p>
            </td>
        </tr>
    </tbody>
</table>
</details>

&nbsp;  
***  
&nbsp;  

## 14. Summary: Team meetings with customers
  
  
**Description**  

<p>A daily summary of important, upcoming customer meetings.</p>
<p>The digest is sent on workdays, not earlier than DigestTime. It includes the meetings for last, current, and future workdays.</p>

<p> 
<img src="..\..\assets\images\Internal-Use\signals-parameters\summary-team-meetings-with-customers.png" class="minimized">
</p>
&nbsp;  

<table data-layout="default">
    <tbody>
        <tr>
            <th colspan="2">
                <h3>Parameters</h3>
            </th>
        </tr>
        <tr>
            <td>
                <p><strong>Trigger</strong></p>
                <ul>
                    <li>
                        <p>Enabled &ndash; default value &ndash; True</p>
                    </li>
                    <li>
                        <p>Digest Time&nbsp;</p>
                    </li>
                    <li>
                        <p>Assignee (Mandatory)</p>
                    </li>
                    <li>
                        <p>Team query mode:</p>
                        <ul>
                            <li>
                                <p>By hierarchy</p>
                            </li>
                            <li>
                                <p>By signals ids</p>
                            </li>
                        </ul>
                    </li>
                    <li>
                        <p>Roles hierarchy (Mandatory) or if chose &quot;By signals ids&quot; the parameter named Team signals ids&nbsp; (Mandatory)</p>
                    </li>
                    <li>
                        <p>Filter</p>
                    </li>
                </ul>
            </td>
            <td>
                <p><strong>Action</strong></p>
                <ul>
                    <li>
                        <p>Recipients (Mandatory)</p>
                    </li>
                    <li>
                        <p>Signal body template</p>
                    </li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>

<details><summary>Click to see the Configurable Parameters</summary> 

<h3>Configurable parameters</h3>

<p>Configuration parameters are stored in the <strong>TeamMeetingsDigestConfiguration</strong> table in the signals database.</p>
<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <p>Parameter</p>
            </th>
            <th>
                <p>Description</p>
            </th>
            <th>
                <p>Default value</p>
            </th>
        </tr>
        <tr>
            <td>
                <p>ContextUserId</p>
            </td>
            <td>
                <p>Signals User ID that is used to query data from Salesforce, PeopleGraph, Signals, and Drip. Therefore, this user must have complete visibility in Salesforce, Signals, and Drip</p>
            </td>
            <td>
                <p>&ndash;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsBlocked</p>
            </td>
            <td>
                <p>Flag indicating whether this job is disabled by {{ short_company_name }} authority (i.e., CSM, DevOps, admins, etc.)</p>
            </td>
            <td>
                <p>False</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsEnabled</p>
            </td>
            <td>
                <p>Flag indicating whether this job is enabled by tenant owner (i.e., customer)</p>
            </td>
            <td>
                <p>True</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Schedule</p>
            </td>
            <td>
                <p><a href="https://en.wikipedia.org/wiki/Cron">Cron</a>&nbsp;recurrence rule to execute this job (<a href="https://crontab.guru/">this</a>&nbsp;editor may be useful)</p>
            </td>
            <td>
                <p>*/30 * * * *</p>
                <p>(i.e., every 30 minutes)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>TeamQueryMode</p>
            </td>
            <td>
                <p>Mode of team participants query. Values: 0 - ByHierarchy, 1 - BySignalIds.</p>
            </td>
            <td>
                <p>0 (ByHierarchy)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>HierarchyRoleName</p>
            </td>
            <td>
                <p>Name of Salesforce role, for which hierarchy will be built (mandatory if TeamQueryMode&nbsp;= 0)</p>
            </td>
            <td>
                <p>CEO (*)</p>
                <p>(* - NULL by default, should be filled)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>TeamSignalsIds</p>
            </td>
            <td>
                <p>JSON array of signal IDs to be queried as a team for digest (mandatory if TeamQueryMode&nbsp;= 1)</p>
            </td>
            <td>
                <p>the array of Guid (*)</p>
                <p>(* - NULL by default, should be filled)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>RecipientsEmailAddresses</p>
            </td>
            <td>
                <p>JSON array of email addresses to receive a digest (f.e., [&quot;andy.young@<a href="http://revenuegrid.com/">revenuegrid.com</a>&quot;])</p>
            </td>
            <td>
                <p>&ndash;</p>
                <p>(Email message with a digest will be sent to&nbsp;all managers)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>OpportunityFilter</p>
            </td>
            <td>
                <p>SOQL query WHERE clause to select only significant Opportunities</p>
            </td>
            <td>
                <p>&ndash;</p>
                <p>(all Opportunities)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>TimeZoneOffsetTicks</p>
            </td>
            <td>
                <p>Time zone offset in ticks; ticks from the UTC time zone. Filled in automatically based on Salesforce time zone of AssigneeUser or ContextUser.</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>DigestTime</p>
            </td>
            <td>
                <p>Digest time in time zone defined by TimeZoneOffsetTicks</p>
            </td>
            <td>
                <p>08:00:00</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>AssigneeUserId</p>
            </td>
            <td>
                <p>The main recipient of the signal. {{ short_company_name }} signal will be assigned to this user, as well as the time zone determined. If there is an Email in Salesforce for this user, it will also be added to the list of recipients (Mandatory)</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
    </tbody>
</table>
</details>


&nbsp;  
***  
&nbsp;  

## 15. Summary: Top templates by success rate  
  
  
**Description**  

<p>Monthly summary of top templates by success rate.</p>
<p>This signal shows what templates performed best in terms of success rate over a specific period of time, e.g., LAST 30 days.</p>
<p>Admins receive this signal once a week.</p>  
  
<p> 
<img src="..\..\assets\images\Internal-Use\signals-parameters\summary-top-templates-by-success-rate.png" class="minimized">
</p>
&nbsp;  

<table data-layout="default">
    <tbody>
        <tr>
            <th colspan="2">
                <h3>Parameters</h3>
            </th>
        </tr>
        <tr>
            <td>
                <p><strong>Trigger</strong></p>
                <ul>
                    <li>
                        <p>Enabled &ndash; default value &ndash; True&nbsp;</p>
                    </li>
                    <li>
                        <p>Period (days) &ndash; default value &ndash; 30</p>
                    </li>
                </ul>
            </td>
            <td>
                <p><strong>Action</strong></p>
                <ul>
                    <li>
                        <p>Dismiss the signal automatically after (hours) &ndash; default value &ndash; 336</p>
                    </li>
                    <li>
                        <p>Max items count &ndash; default value &ndash; 20</p>
                    </li>
                    <li>
                        <p>User to receive notifications (Mandatory)</p>
                    </li>
                    <li>
                        <p> Signal body template</p>
                    </li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>

<details><summary>Click to see the Configurable Parameters</summary> 

<h3>Configurable Parameters</h3>
<p>Configuration parameters are stored in the&nbsp;<strong>TopRatedTemplatesStatsConfiguration</strong> table in the signals database.</p>
<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <p>Parameter</p>
            </th>
            <th>
                <p>Description</p>
            </th>
            <th>
                <p>Default value / Comments</p>
            </th>
        </tr>
        <tr>
            <td>
                <p>PeriodInDays</p>
            </td>
            <td>
                <p>Number of days the selection is made for</p>
            </td>
            <td>
                <p>default value &ndash; 30 days, min value &ndash; 1 day</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>NotificationUserId</p>
            </td>
            <td>
                <p>The ID of the signals User that will receive the selected data</p>
            </td>
            <td>
                <p>No default value, this user <strong>must be specified</strong> before running the signal</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>MaxItemsCount</p>
            </td>
            <td>
                <p>Max number of items to select for the rating</p>
            </td>
            <td>
                <p>20</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalBodyTemplate</p>
            </td>
            <td>
                <p>Signal body template in Razor syntax</p>
            </td>
            <td>
                <p>see signal body template below</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Schedule</p>
            </td>
            <td>
                <p><a href="https://en.wikipedia.org/wiki/Cron">Cron</a> recurrence rule to execute this job (<a href="https://crontab.guru/">this</a> editor may be useful)</p>
            </td>
            <td>
                <p>0&nbsp;9&nbsp;*&nbsp;*&nbsp;FRI</p>
                <p>Please note that currently, only the UTC time zone is supported, so if you want<br />the signal to appear at 9:00 am on the user's time zone, you should specify the correct UTC date/time value in the schedule</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>AutoDismissSignalAfterHours</p>
            </td>
            <td>
                <p>For how long the signal remains actual since its due date (the number of hours). After the specified time period (number of hours), the signal is auto-dismissed</p>
            </td>
            <td>
                <p>336</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalScore</p>
            </td>
            <td>
                <p>Score to assign to the created signal</p>
            </td>
            <td>
                <p>-1</p>
            </td>
        </tr>
    </tbody>
</table>
</details>

<details><summary>Click to see the sample signal body template</summary>   

<p></p>
<p><b>Sample signal body template</b></p>

```
<div class="signals-body">
@if (Model.Stats != null && Model.Stats.Any())
{
<table class="digest-table">
<caption><h3>Templates</h3></caption>
<thead>
<tr class="table-header">
<th class="align-items-center"><span class="mr-15">Name</span></th>
<th class="align-items-center"><span class="mr-15">Created</span></th>
<th class="align-items-center"><span class="mr-15">Success rate (@Model.Period)</span></th>
<th class="align-items-center"><span class="mr-15">Success rate (general)</span></th>
</tr>
</thead>
<tbody>
@foreach (var mt in Model.MailTemplatesStats)
{
<tr>
<td><span class="text-truncate mr-15"><a class="font-weight-bold" href="@mt.DripsUrl" target="_blank">@mt.Name</a></span></td>
<td class="align-right nowrap"><span class="mr-15">@mt.Created</span></td>
<td class="numeric-cell"><span class="mr-15">@mt.RecipientsSuccessRate</span></td>
<td class="numeric-cell"><span class="mr-15">@mt.OverallHistoricalSuccessRate</span></td>
</tr>
}
</tbody>
</table>
}
</div>
 
<style>
.text-truncate {
overflow: hidden;
text-overflow: ellipsis;
white-space: nowrap;
display: inline-block;
vertical-align: text-top;
width: 500px;
}
 
.mr-15 {
margin-right: 15px;
}
 
.signals-body {
font-family: 'Nunito Sans', sans-serif !important;
font-size: 14px !important;
font-weight: 400;
line-height: 1.5;
color: #3e5569;
text-align: left;
}
 
.align-right {
text-align: right;
}
 
.nowrap {
white-space: nowrap;
}
 
.ci-circle-information::before {
content: "\f118";
}
 
.ci::before {
font-family: ci !important;
font-style: normal;
font-weight: normal !important;
vertical-align: middle;
}
 
.ci {
line-height: 1;
display: inline;
margin-right: 5px;
}
 
*, ::after, ::before {
box-sizing: border-box;
}
 
.align-items-center {
-ms-flex-align: center !important;
align-items: center !important;
}
 
.table-header {
border-bottom: 1px solid #dee2e6 !important;
white-space: nowrap;
}
 
.font-weight-bold {
font-weight: 700 !important;
}
 
a, a:hover {
text-decoration: none !important;
background-color: transparent;
}
 
a:not(.sidebar-link, .breadcrumb, .settings-link), a:hover:not(.sidebar-link, .breadcrumb, .settings-link) {
color: #316BBA;
}
 
.numeric-cell {
padding-left: 20px;
padding-right: 5px;
vertical-align: top;
text-align: right;
white-space: nowrap;
}
 
.prompt {
border-radius: .25em;
min-width: 54px;
padding: .25rem;
padding-left: .5rem;
padding-right: .5rem;
display: inline-block;
margin: 5px 0 5px;
}
 
td:first-child {
padding-right: 40px;
}
 
tr:first-child > td {
padding-top: 10px;
}
 
.bg-good {
background: #eff4eb;
}
 
.table-header > th {
border-bottom: 1px solid #dee2e6 !important;
}
 
.digest-table {
border-collapse: collapse;
}
 
.side-btn {
position: absolute;
right: 10px !important;
top: 0px;
text-align: center;
vertical-align: middle;
display: inline !important;
}
 
.side-btn > span {
vertical-align: sub;
}
 
.btn:not(:disabled):not(.disabled) {
cursor: pointer;
}
 
.btn-secondary:not(.active) {
background-color: #2F3341 !important;
}
 
.btn {
border-radius: 5px;
}
 
.btn-secondary, .btn-secondary:hover {
border: 1px solid #2F3341 !important;
}
 
.btn-secondary {
min-width: 125px;
height: 40px;
color: #fff !important;
background-color: #6c757d;
border-color: #6c757d;
}
 
.btn {
height: 40px;
transition: color 0.2s ease-in-out, background 0.2s ease-in-out, border 0.2s ease-in-out !important;
padding: .375rem .75rem !important;
font-size: .875rem !important;
align-items: center;
}
 
.btn-secondary:hover:not(.disabled) {
background: white !important;
color: #2F3341 !important;
}
 
.btn-secondary, .btn-secondary:hover {
border-color: #2F3341 !important;
}
 
.btn:hover {
transform: none !important;
box-shadow: none !important;
}
 
.btn:hover {
color: #212529;
/* text-decoration: none; */
}
</style>
    
```
</details>

&nbsp;  
***  
&nbsp;  

## 16. Summary: Top sequences by success rate


**Description**

<p>Monthly summary of top sequences by success rate.</p>
<p>This signal shows what sequences performed best in terms of success rate over a period of time, e.g., LAST 30 days.</p>
<p>Admins receive this signal once a week.</p>


<p> 
<img src="..\..\assets\images\Internal-Use\signals-parameters\summary-top-sequences-by-success-rate.png" class="minimized">
</p>
&nbsp;  

<table data-layout="default">
    <tbody>
        <tr>
            <th colspan="2">
                <h3>Parameters</h3>
            </th>
        </tr>
        <tr>
            <td>
                <p><strong>Trigger</strong></p>
                <ul>
                    <li>
                        <p>Enabled &ndash; default value &ndash; True</p>
                    </li>
                    <li>
                        <p>Period (days) &ndash; default value &ndash; 30</p>
                    </li>
                </ul>
            </td>
            <td>
                <p><strong>Action</strong></p>
                <ul>
                    <li>
                        <p>Dismiss the signal automatically after (hours) &ndash; default value &ndash; 336</p>
                    </li>
                    <li>
                        <p>Max items count &ndash; default value &ndash; 20</p>
                    </li>
                    <li>
                        <p>User to receive notifications (Mandatory)</p>
                    </li>
                    <li>
                        <p>Signal body template</p>
                    </li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>


<details><summary>Click to see the Configurable Parameters</summary> 

<h3>Configurable Parameters</h3>
<p>Configuration parameters are stored in the&nbsp;<strong>TopRatedCampaignsStatsConfiguration</strong> table in the signals database.</p>
<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <p>Parameter</p>
            </th>
            <th>
                <p>Description</p>
            </th>
            <th>
                <p>Default value / Comments</p>
            </th>
        </tr>
        <tr>
            <td>
                <p>PeriodInDays</p>
            </td>
            <td>
                <p>Number of days the selection is made for</p>
            </td>
            <td>
                <p>default value &ndash; 30 days, min value &ndash; 1 day</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>NotificationUserId</p>
            </td>
            <td>
                <p>The ID of the signals user that will receive the selected data</p>
            </td>
            <td>
                <p>No default value, this user <strong>must be specified</strong> before running the signal.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>MaxItemsCount</p>
            </td>
            <td>
                <p>Max number of items to select for the rating</p>
            </td>
            <td>
                <p>20</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalBodyTemplate</p>
            </td>
            <td>
                <p>Signal body template in Razor syntax</p>
            </td>
            <td>
                <p>see signal body template below</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Schedule</p>
            </td>
            <td>
                <p><a href="https://en.wikipedia.org/wiki/Cron">Cron</a> recurrence rule to execute this job (<a href="https://crontab.guru/">this</a> editor may be useful)</p>
            </td>
            <td>
                <p>0&nbsp;9&nbsp;*&nbsp;*&nbsp;FRI</p>
                <p>Please note that currently only UTC time zone is supported, so if you want<br />to make signal firing at 9:00 am on the user&rsquo;s time zone, you need to specify the correct UTC date/time value in the schedule</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>AutoDismissSignalAfterHours</p>
            </td>
            <td>
                <p>The number of hours signal remains actual since its due date. After the specified time period (the number of hours), the signal is auto-dismissed</p>
            </td>
            <td>
                <p>336</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalScore</p>
            </td>
            <td>
                <p>Score to assign to the created signal</p>
            </td>
            <td>
                <p>-1</p>
            </td>
        </tr>
    </tbody>
</table>
</details>


<details><summary>Click to see the sample signal body template</summary>   

<p></p>
<p><b>Sample signal body template</b></p>

```
<div class="signals-body">
    @if (Model.Stats != null && Model.Stats.Any())
    {
        <table class="digest-table">
            <caption><h3>Sequences</h3></caption>
            <thead>
                <tr class="table-header">
                    <th class="align-items-center"><span class="mr-15">Name</span></th>
                    <th class="align-items-center"><span class="mr-15">Created</span></th>
                    <th class="align-items-center"><span class="mr-15">Recipients</span></th>
                    <th class="align-items-center"><span class="mr-15">Success rate (@Model.Period)</span></th>
                    <th class="align-items-center"><span class="mr-15">Success rate (general)</span></th>
                </tr>
            </thead>
            <tbody>
                @foreach (var cs in Model.CampaignsStats)
                {
                    <tr>
                        <td><span class="text-truncate mr-15"><a class="font-weight-bold" href="@cs.DripsUrl" target="_blank">@cs.Name</a></span></td>
                        <td class="align-right nowrap"><span class="mr-15 align-right">@cs.Created</span></td>
                        <td class="numeric-cell"><span class="mr-15">@cs.RecipientsCount</span></td>
                        <td class="numeric-cell"><span class="mr-15">@cs.RecipientsSuccessRate</span></td>
                        <td class="numeric-cell"><span class="mr-15">@cs.OverallHistoricalSuccessRate</span></td>
                    </tr>
                }
            </tbody>
        </table>
    }
</div>
 
<style>
    .text-truncate {
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        display: inline-block;
        vertical-align: text-top;
        width: 500px;
    }
 
    .mr-15 {
        margin-right: 15px;
    }
 
    .signals-body {
        font-family: 'Nunito Sans', sans-serif !important;
        font-size: 14px !important;
        font-weight: 400;
        line-height: 1.5;
        color: #3e5569;
        text-align: left;
    }
 
    .align-right {
        text-align: right;
    }
 
    .nowrap {
        white-space: nowrap;
    }
 
    .ci-circle-information::before {
        content: "\f118";
    }
 
    .ci::before {
        font-family: ci !important;
        font-style: normal;
        font-weight: normal !important;
        vertical-align: middle;
    }
 
    .ci {
        line-height: 1;
        display: inline;
        margin-right: 5px;
    }
 
    *, ::after, ::before {
        box-sizing: border-box;
    }
 
    .align-items-center {
        -ms-flex-align: center !important;
        align-items: center !important;
    }
 
    .table-header {
        border-bottom: 1px solid #dee2e6 !important;
        white-space: nowrap;
    }
 
    .font-weight-bold {
        font-weight: 700 !important;
    }
 
    a, a:hover {
        text-decoration: none !important;
        background-color: transparent;
    }
 
        a:not(.sidebar-link, .breadcrumb, .settings-link), a:hover:not(.sidebar-link, .breadcrumb, .settings-link) {
            color: #316BBA;
        }
 
    .numeric-cell {
        padding-left: 20px;
        padding-right: 5px;
        vertical-align: top;
        text-align: right;
        white-space: nowrap;
    }
 
    .prompt {
        border-radius: .25em;
        min-width: 54px;
        padding: .25rem;
        padding-left: .5rem;
        padding-right: .5rem;
        display: inline-block;
        margin: 5px 0 5px;
    }
 
    td:first-child {
        padding-right: 40px;
    }
 
    tr:first-child > td {
        padding-top: 10px;
    }
 
    .bg-good {
        background: #eff4eb;
    }
 
    .table-header > th {
        border-bottom: 1px solid #dee2e6 !important;
    }
 
    .digest-table {
        border-collapse: collapse;
    }
 
    .side-btn {
        position: absolute;
        right: 10px !important;
        top: 0px;
        text-align: center;
        vertical-align: middle;
        display: inline !important;
    }
 
        .side-btn > span {
            vertical-align: sub;
        }
 
    .btn:not(:disabled):not(.disabled) {
        cursor: pointer;
    }
 
    .btn-secondary:not(.active) {
        background-color: #2F3341 !important;
    }
 
    .btn {
        border-radius: 5px;
    }
 
    .btn-secondary, .btn-secondary:hover {
        border: 1px solid #2F3341 !important;
    }
 
    .btn-secondary {
        min-width: 125px;
        height: 40px;
        color: #fff !important;
        background-color: #6c757d;
        border-color: #6c757d;
    }
 
    .btn {
        height: 40px;
        transition: color 0.2s ease-in-out, background 0.2s ease-in-out, border 0.2s ease-in-out !important;
        padding: .375rem .75rem !important;
        font-size: .875rem !important;
        align-items: center;
    }
 
    .btn-secondary:hover:not(.disabled) {
        background: white !important;
        color: #2F3341 !important;
    }
 
    .btn-secondary, .btn-secondary:hover {
        border-color: #2F3341 !important;
    }
 
    .btn:hover {
        transform: none !important;
        box-shadow: none !important;
    }
 
    .btn:hover {
        color: #212529;
        /* text-decoration: none; */
    }
</style>
    
```
</details>

&nbsp;  
***  
&nbsp;  

## 17. Summary: Top engaged sequence prospects  
  
  
**Description**

<p>A daily summary of top engaged Leads of your active sequences.</p>
<p>The Top Engaged Leads signal is intended for:</p>
<ul>
    <li>
        <p>maintaining the Top Engaged tag on Drip contacts</p>
    </li>
    <li>
        <p>maintaining the Action Required tag on Drip contacts</p>
    </li>
    <li>
        <p>sending daily notifications about top engaged Leads to Drip contacts' owner</p>
    </li>
</ul>
<p>On schedule, for each Drip contact, the signal retrieves an active sequence within which the Contact was added for the last time. Only Contacts in the &ldquo;<em>InProgress</em>&rdquo; state and campaigns in the &ldquo;<em>Running</em>&rdquo; state are considered.</p>
<p>For each Contact, the last sequence pair retrieves the number of link clicks, and email opens from MailApp</p>

<p> 
<img src="..\..\assets\images\Internal-Use\signals-parameters\summary-top-engaged-sequence-prospects.png" class="minimized">
</p>
&nbsp;  


<table data-layout="default">
    <tbody>
        <tr>
            <th colspan="2">
                <h3>Parameters</h3>
            </th>
        </tr>
        <tr>
            <td>
                <p><strong>Trigger</strong></p>
                <ul>
                    <li>
                        <p>Enabled &ndash; default value &ndash; True</p>
                    </li>
                    <li>
                        <p>Contacts count &ndash; default value &ndash; 20</p>
                    </li>
                </ul>
            </td>
            <td>
                <p><strong>Action</strong></p>
                <ul>
                    <li>
                        <p>Dismiss the signal automatically after (hours) &ndash; default value &ndash; 24</p>
                    </li>
                    <li>
                        <p>Signal body template</p>
                    </li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>


<details><summary>Click to see the Configurable Parameters</summary> 

<h3>Configurable Parameters</h3>
<p>Configuration parameters are stored in the <strong>TopEngagedLeadsConfiguration</strong> table in the signals database.</p>
<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <p>Parameter</p>
            </th>
            <th>
                <p>Description</p>
            </th>
            <th>
                <p>Default value</p>
            </th>
        </tr>
        <tr>
            <td>
                <p>ContextUserId</p>
            </td>
            <td>
                <p>Signals User ID that will be used to query data from Drip and MailApp. Therefore this user must have complete visibility there.</p>
            </td>
            <td>
                <p>&ndash;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsBlocked</p>
            </td>
            <td>
                <p>Flag indicating whether this job is disabled by {{ short_company_name }} authority (i.e., CSM, DevOps, admins, etc.)</p>
            </td>
            <td>
                <p>False</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsEnabled</p>
            </td>
            <td>
                <p>Flag indicating whether this job is enabled by tenant owner (i.e. customer)</p>
            </td>
            <td>
                <p>True</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Schedule</p>
            </td>
            <td>
                <p><a href="https://en.wikipedia.org/wiki/Cron">Cron</a> recurrence rule to execute this job (<a href="https://crontab.guru/">this</a> editor may be useful)</p>
            </td>
            <td>
                <p>0 8 * * *</p>
                <p>(i.e., every day at 8:00 AM)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>AutoDismissSignalAfterHours</p>
            </td>
            <td>
                <p>For how long the signal remains actual since its due date (the number of hours). After the specified time period (number of hours), the signal is auto-dismissed</p>
            </td>
            <td>
                <p>24</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalScore</p>
            </td>
            <td>
                <p>Score to assign to the created signal</p>
            </td>
            <td>
                <p>0</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ContactsCount</p>
            </td>
            <td>
                <p>The number of most active Contacts to collect.</p>
                <p>Valid value range (0; 2147483647]</p>
            </td>
            <td>
                <p>20</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalBodyTemplate</p>
            </td>
            <td>
                <p>Signal body template in Razor syntax</p>
            </td>
            <td>
                <p>see the signal body template below</p>
            </td>
        </tr>
    </tbody>
</table>
</details>

<details><summary>Click to see the signal body template</summary>   

<p></p>
<p><b>Signal body template</b></p>


```
<div class="signals-body">
	<div>We have collected @(Model.Contacts.Count == 1 ? "" : Model.Contacts.Count + " ")top engaged @(Model.Contacts.Count == 1 ? "lead" : "leads") based on your active sequences</div>
	<div class="prompt bg-good p-1 pl-3 pr-3 align-items-center"><i class="ci ci-circle-information"></i><span class="text-truncate">Suggested action: review and move @(Model.Contacts.Count == 1 ? "lead" : "leads") to a special sequence.</span></div>
	<table class="digest-table">
		<thead>
			<tr class="table-header">
				<th class="align-items-center"><span class="text-truncate mr-15">Name</span></th>
				<th class="align-items-center"><i class="ci ci-small ci-eye"></i><span class="text-truncate mr-15">Opens</span></th>
				<th class="align-items-center"><i class="ci ci-small ci-click"></i><span class="text-truncate mr-15">Clicks</span></th>
			</tr>
		</thead>
		<tbody>
			@foreach (var contact in Model.Contacts)
			{
				<tr>
					<td><a class="font-weight-bold" href="@contact.DripUrl">@contact.Name</a><br>@contact.Title</td>
					<td class="numeric-cell">@contact.OpensCount</td>
					<td class="numeric-cell">@contact.ClicksCount</td>
				</tr>
			}
		</tbody>
	</table>
	<a href="@Model.ActionRequiredContactsUrl" class="btn btn-secondary side-btn"><span class="align-items-center">View Leads</span></a>
</div>


<style>
	.text-truncate {
		overflow: hidden;
		text-overflow: ellipsis;
		white-space: nowrap;
		display: inline;
		vertical-align: text-top;
	}

	.mr-15 {
		margin-right: 15px;
	}

	.signals-body {
		font-family: 'Nunito Sans', sans-serif !important;
		font-size: 14px !important;
		font-weight: 400;
		line-height: 1.5;
		color: #3e5569;
		text-align: left;
	}

	.ci-eye::before {
		content: "\f12f";
	}

	.ci-circle-information::before {
		content: "\f118";
	}

	.ci::before {
		font-family: ci !important;
		font-style: normal;
		font-weight: normal !important;
		vertical-align: middle;
	}

	.ci {
		line-height: 1;
		display: inline;
		margin-right: 5px;
	}

	*, ::after, ::before {
		box-sizing: border-box;
	}

	.ci-click::before {
		content: "\f11c";
	}

	.align-items-center {
		-ms-flex-align: center !important;
		align-items: center !important;
	}

	.table-header {
		border-bottom: 1px solid #dee2e6 !important;
	}

	.font-weight-bold {
		font-weight: 700 !important;
	}

	a, a:hover {
		text-decoration: none !important;
		background-color: transparent;
	}

		a:not(.sidebar-link, .breadcrumb, .settings-link), a:hover:not(.sidebar-link, .breadcrumb, .settings-link) {
			color: #316BBA;
		}

	.numeric-cell {
		padding-left: 20px;
		padding-right: 5px;
		vertical-align: top
	}

	.prompt {
		border-radius: .25em;
		min-width: 54px;
		padding: .25rem;
		padding-left: .5rem;
		padding-right: .5rem;
		display: inline-block;
		margin: 5px 0 5px;
	}

	td:first-child {
		padding-right: 40px;
	}

	tr:first-child > td {
		padding-top: 10px;
	}

	.bg-good {
		background: #eff4eb;
	}

	.table-header > th {
		border-bottom: 1px solid #dee2e6 !important;
	}

	.digest-table {
		border-collapse: collapse;
	}

	.side-btn {
		position: absolute;
		right: 10px !important;
		top: 0px;
		text-align: center;
		vertical-align: middle;
		display: inline !important;
	}

		.side-btn > span {
			vertical-align: sub;
		}

	.btn:not(:disabled):not(.disabled) {
		cursor: pointer;
	}

	.btn-secondary:not(.active) {
		background-color: #2F3341 !important;
	}

	.btn {
		border-radius: 5px;
	}

	.btn-secondary, .btn-secondary:hover {
		border: 1px solid #2F3341 !important;
	}

	.btn-secondary {
		min-width: 125px;
		height: 40px;
		color: #fff !important;
		background-color: #6c757d;
		border-color: #6c757d;
	}

	.btn {
		height: 40px;
		transition: color 0.2s ease-in-out, background 0.2s ease-in-out, border 0.2s ease-in-out !important;
		padding: .375rem .75rem !important;
		font-size: .875rem !important;
		align-items: center;
	}

	.btn-secondary:hover:not(.disabled) {
		background: white !important;
		color: #2F3341 !important;
	}

	.btn-secondary, .btn-secondary:hover {
		border-color: #2F3341 !important;
	}

	.btn:hover {
		transform: none !important;
		box-shadow: none !important;
	}

	.btn:hover {
		color: #212529;
		/* text-decoration: none; */
	}
</style>

    
```
</details>

&nbsp;  
***  
&nbsp;  

## 18. Sequence daily digest  
  
  
**Description**  

<p>Daily digest that shows users their sequence activities.</p>
<p>Email digest for user's active sequences ( private or shared) and the same digest for each delegator.</p>
<p>The signal starts at 6 a.m.</p>
  
  

<table data-layout="default">
    <tbody>
        <tr>
            <th colspan="2">
                <h3>Parameters</h3>
            </th>
        </tr>
        <tr>
            <td>
                <p><strong>Trigger</strong></p>
                <ul>
                    <li>
                        <p>Enabled/Disabled &ndash; default value &ndash; True</p>
                    </li>
                </ul>
            </td>
            <td>
                <p><strong>Action</strong></p>
                <ul>
                    <li>
                        <p>Time zone &ndash; default value &ndash; UTC Coordinated Universal time</p>
                    </li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>

<details><summary>Click to see a screenshot</summary>   
<p> 
<img src="..\..\assets\images\Internal-Use\signals-parameters\sequence-daily-digest-1.png">
</p>
</details>

<details><summary>Click to see a screenshot</summary>
<p> 
<img src="..\..\assets\images\Internal-Use\signals-parameters\sequence-daily-digest-2.png">
</p>
</details>

&nbsp;  
***  
&nbsp;  


## 19. No Salesforce activity after the object was changed  
  
  
**Description**  

<p>Automatic reminders for sales reps if the required activities haven't been performed after changing the object.</p>
<p>This signal activated if Salesforce business object was changed recently (any field value change) with no activity created in Salesforce afterwards. The signal activates for every object with:</p>
<ul>
    <li>
        <p>metadata attributes:</p>
        <ul>
            <li>
                <p>queryable: true</p>
            </li>
            <li>
                <p>searchable: true</p>
            </li>
            <li>
                <p>retrievable: true</p>
            </li>
        </ul>
    </li>
    <li>
        <p>Task and Event that contains WhoId or WhatId relationship to this object</p>
    </li>
    <li>
        <p>Histories relationship</p>
    </li>
    <li>
        <p>Owner reference</p>
    </li>
</ul>

<p> 
<img src="..\..\assets\images\Internal-Use\signals-parameters\no-next-steps-for-an-open-opportunity.png" class="minimized">
</p>

<table data-layout="default">
    <tbody>
        <tr>
            <th colspan="2">
                <h3>Parameters</h3>
            </th>
        </tr>
        <tr>
            <td>
                <p><strong>Trigger</strong></p>
                <ul>
                    <li>
                        <p>Enabled &ndash; default value &ndash; False</p>
                    </li>
                    <li>
                        <p>Start date of change tracking (Mandatory)</p>
                    </li>
                    <li>
                        <p>Time after a change to check activities (hours) &ndash; default value &ndash; 336</p>
                    </li>
                    <li>
                        <p>Check Activities:&nbsp;</p>
                        <ul>
                            <li>
                                <p>Event enabled</p>
                            </li>
                            <li>
                                <p>Activity enabled</p>
                            </li>
                        </ul>
                    </li>
                    <li>
                        <p>Salesforce Object:</p>
                        <ul>
                            <li>
                                <p>Lead</p>
                            </li>
                            <li>
                                <p>Contact</p>
                            </li>
                        </ul>
                    </li>
                    <li>
                        <p>Tracking field name (Mandatory)</p>
                    </li>
                    <li>
                        <p>Tracking field name History (Mandatory)</p>
                    </li>
                    <li>
                        <p>Object filter</p>
                    </li>
                    <li>
                        <p>Task filter</p>
                    </li>
                    <li>
                        <p>Event filter</p>
                    </li>
                </ul>
            </td>
            <td>
                <p><strong>Action</strong></p>
                <ul>
                    <li>
                        <p>Score &ndash; default value &ndash; &quot;-1&quot;</p>
                    </li>
                    <li>
                        <p>Dismiss the signal automatically after (hours) &ndash; default value &ndash; 336</p>
                    </li>
                    <li>
                        <p>Signal destinations</p>
                        <ul>
                            <li>
                                <p>Action center</p>
                            </li>
                            <li>
                                <p>Email</p>
                            </li>
                            <li>
                                <p>MS Teams</p>
                            </li>
                        </ul>
                    </li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>



<details><summary>Click to see the Configurable Parameters</summary> 

<h3>Configurable Parameters</h3>
<p>Configuration parameters are stored in the <strong>NoSalesforceActivityAfterObjectWasChangedConfiguration</strong> table in the signals database.</p>
<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <p>Parameter</p>
            </th>
            <th>
                <p>Description</p>
            </th>
            <th>
                <p>Default value</p>
            </th>
        </tr>
        <tr>
            <td>
                <p>ContextUserId</p>
            </td>
            <td>
                <p>Signals User ID that will be used to query data from Salesforce, PeopleGraph, and Signals. Therefore this user must have complete visibility in Salesforce and Signals</p>
            </td>
            <td>
                <p>&ndash;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>TenantId</p>
            </td>
            <td>
                <p>Tenant ID which will be used to query data from Salesforce, PeopleGraph, and Signals.</p>
            </td>
            <td>
                <p>&ndash;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Created Date</p>
            </td>
            <td>
                <p>Date of signal configuration creation</p>
            </td>
            <td>
                <p>&ndash;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsBlocked</p>
            </td>
            <td>
                <p>Flag indicating whether this job is disabled by {{ short_company_name }} authority (i.e., CSM, DevOps, admins, etc.)</p>
            </td>
            <td>
                <p>False</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsEnabled</p>
            </td>
            <td>
                <p>Flag indicating whether this job is enabled by tenant owner (i.e., customer)</p>
            </td>
            <td>
                <p>True</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Schedule</p>
            </td>
            <td>
                <p><a href="https://en.wikipedia.org/wiki/Cron">Cron</a> recurrence rule to execute this job (<a href="https://crontab.guru/">this</a> editor may be useful)</p>
            </td>
            <td>
                <p>0 */2 * * *</p>
                <p>(i.e., every two hours)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>AutoDismissSignalAfterHours</p>
            </td>
            <td>
                <p>For how long the signal remains actual since its due date (the number of hours). After the specified time period (number of hours), the signal is auto-dismissed</p>
            </td>
            <td>
                <p>336</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ProcessingStartDate</p>
            </td>
            <td>
                <p>Start date for tracking changes</p>
            </td>
            <td>
                <p>&ndash;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SObjectTypeName</p>
            </td>
            <td>
                <p>Name of SObject type to be used. Only Lead and Contact&nbsp;are affected by the first iteration.</p>
            </td>
            <td>
                <p>&ndash;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SObjectAnchorFieldName&nbsp;&nbsp;</p>
            </td>
            <td>
                <p>Name of anchor field of SObjectTypeName to be triggered on</p>
            </td>
            <td>
                <p>&ndash;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SObjectAnchorFieldHistoryName</p>
            </td>
            <td>
                <p>Name of anchor field of SObjectTypeName History to be triggered on</p>
            </td>
            <td>
                <p>&ndash;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SObjectFilter</p>
            </td>
            <td>
                <p>SOQL filter for SObject</p>
            </td>
            <td>
                <p>string</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ActivityCheckTimeoutHours</p>
            </td>
            <td>
                <p>Time after SObjectAnchorFieldName change should be tracked&nbsp;</p>
            </td>
            <td>
                <p>336</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ActivitiesChecks</p>
            </td>
            <td>
                <p>Parameter to set activities checks.<br />Activities checks:</p>
                <ul>
                    <li>
                        <p>CheckScheduledEvents - Flag indicating whether this job should check scheduled events after SObjectAnchorFieldName was changed</p>
                    </li>
                    <li>
                        <p>CheckActivities - Flag indicating whether this job should check tasks created after SObjectAnchorFieldName was changed</p>
                    </li>
                </ul>
                <p>Values:</p>
                <ul>
                    <li>
                        <p><strong>0 </strong>- CheckScheduledEvents and CheckActivities are both disabled</p>
                    </li>
                    <li>
                        <p><strong>1 </strong>- CheckScheduledEvents - enabled and CheckActivities - disabled (but the result is the same as for <strong>0</strong> due to activities not being checked)</p>
                    </li>
                    <li>
                        <p><strong>2</strong> - CheckScheduledEvents - disabled and CheckActivities - enabled</p>
                    </li>
                    <li>
                        <p><strong>3&nbsp;</strong>-&nbsp; CheckScheduledEvents and CheckActivities are both enabled</p>
                    </li>
                </ul>
            </td>
            <td>
                <p>3</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>TaskFilter</p>
            </td>
            <td>
                <p>SOQL filter for the related task</p>
            </td>
            <td>
                <p>empty</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>EventFilter</p>
            </td>
            <td>
                <p>SOQL filter for the related event</p>
            </td>
            <td>
                <p>empty</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalBodyTemplate</p>
            </td>
            <td>
                <p>Razor template for rendering signal body</p>
            </td>
            <td>
                <p>&ndash;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsEmailNotificationEnabled</p>
            </td>
            <td>
                <p>Indicates whether email notification will be sent to assignees after signal is created</p>
            </td>
            <td>
                <p>false</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>EmailNotificationTemplate</p>
            </td>
            <td>
                <p>Razor template for rendering email notification body</p>
            </td>
            <td>
                <p>&ndash;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsTeamsNotificationEnabled</p>
            </td>
            <td>
                <p>Indicates whether Teams notification will be sent to assignees after signal is created</p>
            </td>
            <td>
                <p>true</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>TeamsNotificationTemplate</p>
            </td>
            <td>
                <p>Razor template to be used to render Teams notification body</p>
            </td>
            <td>
                <p>&ndash;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalScore</p>
            </td>
            <td>
                <p>Score to assign to the created signal</p>
            </td>
            <td>
                <p>-1</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalPriority</p>
            </td>
            <td>
                <p>Priority of the generated signals</p>
                <p>Possible values are:</p>
                <ul>
                    <li>
                        <p>Alert = 0</p>
                    </li>
                    <li>
                        <p>Notification = 1</p>
                    </li>
                </ul>
                <p />
            </td>
            <td>
                <p />
                <p />
                <p />
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>RepeatSignalAfterDismissDays</p>
            </td>
            <td>
                <p>The number of days to wait before sending the signal after the user dismissed it if the related Salesforce object still meets filter settings.</p>
                <p>Valid value range: [1; 2147483647].</p>
            </td>
            <td>
                <p>7</p>
            </td>
        </tr>
    </tbody>
</table>
</details>


&nbsp;  
***  
&nbsp;  


## 20. Follow-up reminder after Salesforce event with Salesforce object    
  
  
**Description**    
  

<p>Automatic reminders for sales reps if no task was created or no field was changed after the relevant event took place.</p>
<p>Existing follow-up reminder signals apply only to events from Calendar, while this signal functions upon Salesforce events and generic relations.</p>
<p>The signal activates for every object with:</p>
<ul>
    <li>
        <p>metadata attributes:</p>
        <ul>
            <li>
                <p>queryable: true</p>
            </li>
            <li>
                <p>searchable: true</p>
            </li>
            <li>
                <p>retrievable: true</p>
            </li>
        </ul>
    </li>
    <li>
        <p>Event containing WhoId or WhatId relationship to this object</p>
    </li>
    <li>
        <p>AccountId field and Account that include a reference (If AccountFieldUpdateCheckEnabled)</p>
    </li>
</ul>

<p> 
<img src="..\..\assets\images\Internal-Use\signals-parameters\follow-up-reminder-after-salesforce-event-with-salesforce-object.png" class="minimized">
</p>

<table data-layout="default">
    <tbody>
        <tr>
            <th colspan="2">
                <h3>Parameters</h3>
            </th>
        </tr>
        <tr>
            <td>
                <p><strong>Trigger</strong></p>
                <ul>
                    <li>
                        <p>Enabled &ndash; default value &ndash; False</p>
                    </li>
                    <li>
                        <p>Follow-up check interval (hours) &ndash; default value &ndash; 3</p>
                    </li>
                    <li>
                        <p>Salesforce Object:</p>
                        <ul>
                            <li>
                                <p>Lead</p>
                            </li>
                            <li>
                                <p>Contact</p>
                            </li>
                        </ul>
                    </li>
                    <li>
                        <p>Object filter</p>
                    </li>
                    <li>
                        <p>Task filter</p>
                    </li>
                    <li>
                        <p>Event filter</p>
                    </li>
                </ul>
            </td>
            <td>
                <p><strong>Action</strong></p>
                <ul>
                    <li>
                        <p>Score &ndash; default value &ndash; &quot;-1&quot;</p>
                    </li>
                    <li>
                        <p>Dismiss the signal automatically after (hours) &ndash; default value &ndash; 336</p>
                    </li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>  
  



<details><summary>Click to see the Configurable Parameters</summary> 

<h3>Configurable Parameters</h3>
<p>Configuration parameters are stored in the&nbsp;<strong>LeadMeetingFollowupReminderConfiguration</strong> table in the signals database.</p>
<table data-layout="default" ac:local-id="dc4f300a-318a-4728-9a38-d272906f892d">
    <tbody>
        <tr>
            <th>
                <p>Parameter</p>
            </th>
            <th>
                <p>Description</p>
            </th>
            <th>
                <p>Default value</p>
            </th>
        </tr>
        <tr>
            <td>
                <p>ContextUserId</p>
            </td>
            <td>
                <p>Signals User ID that will be used to query data from Salesforce, PeopleGraph, and Signals. Therefore this user must have complete visibility in Salesforce and Signals</p>
            </td>
            <td>
                <p>&ndash;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsBlocked</p>
            </td>
            <td>
                <p>Flag indicating whether this job is disabled by {{ short_company_name }} authority (i.e., CSM, DevOps, admins, etc.)</p>
            </td>
            <td>
                <p>False</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsEnabled</p>
            </td>
            <td>
                <p>Flag indicating whether this job is enabled by tenant owner (i.e., customer)</p>
            </td>
            <td>
                <p>True</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Schedule</p>
            </td>
            <td>
                <p><a href="https://en.wikipedia.org/wiki/Cron">Cron</a> recurrence rule to execute this job (<a href="https://crontab.guru/">this</a> editor may be useful)</p>
            </td>
            <td>
                <p>0 */2 * * *</p>
                <p>(i.e., every two hours)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SObjectTypeName</p>
            </td>
            <td>
                <p>Name of SObject type to be used. Only Lead and Contact&nbsp;are affected by the first iteration</p>
            </td>
            <td>
                <p>Lead</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>AutoDismissSignalAfterHours</p>
            </td>
            <td>
                <p>For how long the signal remains actual since its due date (the number of hours). After the specified time period (number of hours), the signal is auto-dismissed</p>
            </td>
            <td>
                <p>240</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalScore</p>
            </td>
            <td>
                <p>Score to assign to the created signal</p>
            </td>
            <td>
                <p>-1</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>FollowupCheckTimeoutHours</p>
            </td>
            <td>
                <p>Number of hours to wait after the event start date before checking for missing follow-up email</p>
            </td>
            <td>
                <p>24</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SObjectFilter</p>
            </td>
            <td>
                <p>SOQL query to select only significant leads</p>
                <p>(e.g. Lead_Score_SQL__c = 'X1' OR Lead_Score_SQL__c = 'X2')</p>
            </td>
            <td>
                <p>&ndash;</p>
                <p>(i.e., all Leads are applicable)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>TaskFilter</p>
            </td>
            <td>
                <p>Related task object filter (By agreement, TaskFilter and EventFilter should contain direct object or relation query based on shared activities set up for the environment.)</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>EventFilter</p>
            </td>
            <td>
                <p>Related event object filter (shouldn't include any of the date-time properties. By agreement, TaskFilter and EventFilter should contain direct object or relation query, based on shared activities set up for the environment.)</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>AccountFieldUpdateCheckEnabled</p>
            </td>
            <td>
                <p>Flag indicating that an additional account history check should be added to filtering (can't be set for objects without Account reference, for example, Lead)</p>
            </td>
            <td>
                <p>False</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>AccountFieldName</p>
            </td>
            <td>
                <p>Name of field to track (should be tracked by SF) (mandatory if AccountFieldUpdateCheckEnabled)</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
    </tbody>
</table>
</details>

&nbsp;  
***  
&nbsp;


## 21. New response from a prospect    
  
  
**Description**    
  
The user is notified when a new email is received from an Opportunity over a certain size.

<ol>
    <li>
        <p>For signal generation, the system collects all emails which were added since the last mail check. The emails matching the following conditions are being excluded:</p>
        <ol>
            <li>
                <p>Email's related Contact is from the organization’s domain</p>
            </li>
            <li>
                <p>Email is outbound and was sent earlier than inbound email for the same Contact</p>
            </li>
            <li>
                <p>Email’s related Contact is involved in the active Drip campaign and the &quot;Skip Contacts In Active Drip Campaign&quot; parameter is set to &quot;True&quot;</p>
            </li>
        </ol>
    </li>
    <li>
        <p>Depending on the &quot;Match Opportunities By Account&quot; parameter, for each email, the system finds a significant matching Opportunity in Salesforce: the email’s related Contact is assigned to the Opportunity contact role, or the email’s related Contact and Opportunity are bound to the same account.</p>
    </li>
    <li>
        <p>Send the signal to the Opportunity owner and manager (to signal the user with a manager role), who are not involved in this communication. If the Opportunity owner and all managers are being the recipients &dash; do not send them the signal.</p>
    </li>
</ol>

<p> 
<img src="..\..\assets\images\Internal-Use\signals-parameters\new-response-from-a-prospect.png" class="minimized">
</p>

&nbsp;

<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <h3>Parameters</h3>
            </th>
            <th>
                <p />
            </th>
        </tr>
        <tr>
            <td>
                <p><strong>Trigger</strong></p>
                <ul>
                    <li>
                        <p>Enabled/Disabled &ndash; default value &ndash; True</p>
                    </li>
                    <li>
                        <p>Skip Contacts In Active Drip Campaign &ndash; default value &ndash; True</p>
                    </li>
                    <li>
                        <p>Match Opportunities By Account &ndash; default value &ndash; True</p>
                    </li>
                    <li>
                        <p>Filter</p>
                    </li>
                </ul>
            </td>
            <td>
                <p><strong>Action</strong></p>
                <ul>
                    <li>
                        <p>Score &ndash; default value &ndash; &quot;3&quot;</p>
                    </li>
                    <li>
                        <p>Dismiss the signal automatically after (hours) &ndash; default value &ndash; 336</p>
                    </li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>


<details><summary>Click to see the Configurable Parameters</summary> 

<h3>Configurable Parameters</h3>

<p>Configuration parameters are stored in the <strong>NewResponseFromOpportunityConfiguration</strong> table in the signals database.</p>

<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <p>Parameter</p>
            </th>
            <th>
                <p>Description</p>
            </th>
            <th>
                <p>Default value</p>
            </th>
        </tr>
        <tr>
            <td>
                <p>ContextUserId</p>
            </td>
            <td>
                <p>Signals User ID that will be used to query data from Salesforce, PeopleGraph, Signals, and Drip. Therefore this user must have complete visibility in Salesforce, Signals, and Drip</p>
            </td>
            <td>
                <p>&ndash;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsBlocked</p>
            </td>
            <td>
                <p>Flag indicating whether this job is disabled by {{ short_company_name }} authority (i.e., CSM, DevOps, admins, etc.)</p>
            </td>
            <td>
                <p>False</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsEnabled</p>
            </td>
            <td>
                <p>Flag indicating whether this job is enabled by tenant owner (i.e., customer)</p>
            </td>
            <td>
                <p>True</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Schedule</p>
            </td>
            <td>
                <p><a href="https://en.wikipedia.org/wiki/Cron">Cron</a> recurrence rule to execute this job (<a href="https://crontab.guru/">this</a> editor may be useful)</p>
            </td>
            <td>
                <p>0 */2 * * 1-5</p>
                <p>(i.e., at minute 0 past every 2nd hour on every day-of-week from Monday through Friday)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>AutoDismissSignalAfterHours</p>
            </td>
            <td>
                <p>For how long the signal remains actual since its due date (the number of hours). After the specified time period (number of hours), the signal is auto-dismissed</p>
            </td>
            <td>
                <p>336</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalScore</p>
            </td>
            <td>
                <p>Score to assign to the created signal</p>
            </td>
            <td>
                <p>3</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>OpportunityFilter</p>
            </td>
            <td>
                <p>SOQL query WHERE clause intended to select only significant Opportunities</p>
                <p>(e.g. Amount &gt; 10000)</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>MatchOpportunitiesByAccount</p>
            </td>
            <td>
                <p>Flag indicating how to find Opportunities that are related to email:</p>
                <ul>
                    <li>
                        <p>email participant's address matches the Salesforce contact that is assigned to the Opportunity contact role (False)</p>
                    </li>
                    <li>
                        <p>email participant's address matches a Contact that is assigned to the Opportunity contact role, or the Contact and the Opportunity are bound to the same account (True)</p>
                    </li>
                </ul>
            </td>
            <td>
                <p>True</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SkipContactsInActiveDripCampaign</p>
            </td>
            <td>
                <p>Flag indicating whether to skip contacts that are currently under an active Drip sequence</p>
            </td>
            <td>
                <p>True</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>LastSyncDateTime</p>
            </td>
            <td>
                <p>UTC date and time when mail was checked for a particular tenant. Null means that check has never been run before</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
    </tbody>
</table>
</details>


&nbsp;  
***  
&nbsp;


## 22. New response to a prospect   
  
  
**Description**  

The user is notified, when a new email has been sent to an Opportunity over a certain size.
  
<ol>
    <li>
        <p>For signal generation, the system collects all emails which were added since the last mail check. The emails matching the following conditions are being excluded:</p>
        <ol>
            <li>
                <p>Email's related Contact is from the organization’s domain</p>
            </li>
            <li>
                <p>Email is inbound and was sent earlier than outbound email for the same Contact</p>
            </li>
            <li>
                <p>Email’s related Contact is involved in the active Drip campaign and the &quot;Skip Contacts In Active Drip Campaign&quot; parameter is set to &quot;True&quot;</p>
            </li>
        </ol>
    </li>
    <li>
        <p>Depending on the &quot;Match Opportunities By Account&quot; parameter, for each email, the system finds a significant matching Opportunity in Salesforce: the email’s related Contact is assigned to the Opportunity contact role, or the email’s related Contact and Opportunity are bound to the same account.</p>
    </li>
    <li>
        <p>Send the signal to the Opportunity owner and manager (to signal the user with a manager role), who are not involved in this communication. If the Opportunity owner and all managers are being the recipients &dash; do not send them the signal.</p>
    </li>
</ol>

<p> 
<img src="..\..\assets\images\Internal-Use\signals-parameters\new-response-to-a-prospect.png" class="minimized">
</p>

&nbsp;

<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <h3>Parameters</h3>
            </th>
            <th>
                <p />
            </th>
        </tr>
        <tr>
            <td>
                <p><strong>Trigger</strong></p>
                <ul>
                    <li>
                        <p>Enabled/Disabled &ndash; default value &ndash; True</p>
                    </li>
                    <li>
                        <p>Skip Contacts In Active Drip Campaign &ndash; default value &ndash; True</p>
                    </li>
                    <li>
                        <p>Match Opportunities By Account &ndash; default value &ndash; True</p>
                    </li>
                    <li>
                        <p>Filter</p>
                    </li>
                </ul>
            </td>
            <td>
                <p><strong>Action</strong></p>
                <ul>
                    <li>
                        <p>Score &ndash; default value &ndash; &quot;3&quot;</p>
                    </li>
                    <li>
                        <p>Dismiss the signal automatically after (hours) &ndash; default value &ndash; 336</p>
                    </li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>


<details><summary>Click to see the Configurable Parameters</summary> 

<h3>Configurable Parameters</h3>

<p>Configuration parameters are stored in the <strong>NewResponseFromOpportunityConfiguration</strong> table in the signals database.</p>

<table data-layout="default">
    <tbody>
        <tr>
            <th>
                <p>Parameter</p>
            </th>
            <th>
                <p>Description</p>
            </th>
            <th>
                <p>Default value</p>
            </th>
        </tr>
        <tr>
            <td>
                <p>ContextUserId</p>
            </td>
            <td>
                <p>Signals User ID that will be used to query data from Salesforce, PeopleGraph, Signals, and Drip. Therefore this user must have complete visibility in Salesforce, Signals, and Drip</p>
            </td>
            <td>
                <p>&ndash;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsBlocked</p>
            </td>
            <td>
                <p>Flag indicating whether this job is disabled by {{ short_company_name }} authority (i.e., CSM, DevOps, admins, etc.)</p>
            </td>
            <td>
                <p>False</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>IsEnabled</p>
            </td>
            <td>
                <p>Flag indicating whether this job is enabled by tenant owner (i.e., customer)</p>
            </td>
            <td>
                <p>True</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Schedule</p>
            </td>
            <td>
                <p><a href="https://en.wikipedia.org/wiki/Cron">Cron</a> recurrence rule to execute this job (<a href="https://crontab.guru/">this</a> editor may be useful)</p>
            </td>
            <td>
                <p>0 */2 * * 1-5</p>
                <p>(i.e., at minute 0 past every 2nd hour on every day-of-week from Monday through Friday)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>AutoDismissSignalAfterHours</p>
            </td>
            <td>
                <p>For how long the signal remains actual since its due date (the number of hours). After the specified time period (number of hours), the signal is auto-dismissed</p>
            </td>
            <td>
                <p>336</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SignalScore</p>
            </td>
            <td>
                <p>Score to assign to the created signal</p>
            </td>
            <td>
                <p>-1</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>OpportunityFilter</p>
            </td>
            <td>
                <p>SOQL query WHERE clause intended to select only significant Opportunities</p>
                <p>(e.g. Amount &gt; 10000)</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
        <tr>
            <td>
                <p>MatchOpportunitiesByAccount</p>
            </td>
            <td>
                <p>Flag indicating how to find Opportunities that are related to email:</p>
                <ul>
                    <li>
                        <p>email participant's address matches the Salesforce contact that is assigned to the Opportunity contact role (False)</p>
                    </li>
                    <li>
                        <p>email participant's address matches a Contact that is assigned to the Opportunity contact role, or the Contact and the Opportunity are bound to the same account (True)</p>
                    </li>
                </ul>
            </td>
            <td>
                <p>True</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SkipContactsInActiveDripCampaign</p>
            </td>
            <td>
                <p>Flag indicating whether to skip contacts that are currently under an active Drip sequence</p>
            </td>
            <td>
                <p>True</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>LastSyncDateTime</p>
            </td>
            <td>
                <p>UTC date and time when mail was checked for a particular tenant. Null means that check has never been run before</p>
            </td>
            <td>
                <p />
            </td>
        </tr>
    </tbody>
</table>
</details>


&nbsp;  