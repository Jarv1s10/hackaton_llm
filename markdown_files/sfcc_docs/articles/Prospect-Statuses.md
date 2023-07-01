---
title: List of all Revenue Grid-assigned statuses of prospects
description: Detailed overview of Revenue Grid Prospect Statuses
---

  
# Revenue Grid Prospect Statuses

<p style="font-size:15px"><i>4 min read - updated few hours ago</i> </p>
<!-- ShareThis BEGIN -->
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis -->
<br>

<p><img src="../../assets/images/People/personstatus.png" style="margin-left:15px;  float: right; width: 50%; height: 50%;">
Every prospect in Revenue Grid is assigned a certain Person Status based on their reaction to Sequence steps. The life-cycle of statuses start from <i>Just Added</i>, once a prospect gets imported into Revenue Grid.
</p>
Prospect status updates can be:

- automatic, triggered by a [Sequence stage change](../Sequences-Stages/)
- initiated by users on Revenue Grid side on [Action Center](../Planner/), [Audience](../People/), [Sequences' Recipients tab](../Recipients/) or via [Sequence widget](../Sidebar/)
- or initiated by users on Salesforce side and get reflected on Revenue Grid side automatically according to [custom mapping](../Prospect-Statuses/#custom_salesforce_mapping)



!!! tip "Tip"
    If you do **not** want prospect's Revenue Grid status to get updated automatically when a Sequence [proceeds to its next stage](../Sequences-Stages/), clear the "*Update Person status on Sequence Stage Change*" checkbox in the [Sequence's settings](../Settings-of-Sequences). That is useful, for example, if running a secondary nurturing [email Sequence](../Create-new-sequence/).

------

## Default types of Person statuses


**Just added**  - prospect has been added to [Audience page](../People/) but it's not involved in any Sequences yet.

**Not contacted**  - this status indicates that a prospect has been added to a sequence, but no outreach has been made yet.

**Approaching** - prospect engagement is in progress, going through the [steps](../Create-new-sequence/#adding_and_editing_steps_toof_a_sequence) according to the sequence schedule.

**On hold** - this status is assigned manually by a RG user. Such prospect will not proceed to a following step within any Sequences enrolled.


**Success** - this status is assigned manually by a RG user by clicking "Finish: Success" on [Action Center's Replies tab](../Replies/), on the [Sequences' Recipients tab](../Recipients/#mass_actions) or via [Sequence widget](../Sidebar/). This status means that the engagement was successful, thus sequence will not reach out to this prospect anymore and further negotiations will take place outside of Revenue Grid.

**Not interested**  - this status is assigned manually by a RG user by clicking "Finish: Not interested" on [Action Center's Replies tab](../Replies/), on the [Sequences' *Recipients* tab](../Recipients/#mass_actions) or via [Sequence widget](../Sidebar/) when a prospect expresses his/her disinterest in this campaign. However, this prospect can still be contacted in a course of other campaigns.

**Opted Out** - this status can be assigned both, manually or automatically. Manually by a RG user by clicking "Finish: Opt Out" on [Action Center's Replies tab](../Replies/), on the [Sequences' Recipients tab](../Recipients/#mass_actions), on the [profile page](../People/#contactlead_profile), or via [Sequence widget](../Sidebar/). Also it may happen automatically if a prospect clicks [the unsubscribe link](../Settings/#unsubscribe_links) in a received email.

**Bounced** - this status is also can be assigned both, manually or automatically. Manually via [RG Sequence widget](../Sidebar/). Automatically, if a [hard bounce](https://whatis.techtarget.com/definition/hard-bounce) delivery failure notification was received in response to a [Sequence email](../Create-new-sequence/#email_type_of_a_step), then Revenue Grid will change this prospect's status to Bounced; in addition, the delivery failure automatic email will be put to the [Notifications](../Notifications/) tab in the Action Center. 

!!! tip "Note"
    If a prospect has **Bounced** status, then it's not going to be possible to *Opt out* the prospect anywhere throughout Revenue Grid. Whether on [Audience](../People/#mass_action), [Prospect's Profile page](../People/#contactlead_profile), [Recipients](../Recipients/#mass_actions) tabs nor via the [Sidebar](../Sidebar).

**Unresponsive** - this prospect status is automatically assigned if there has been no response from a prospect to [automated email sequence messages](../Create-new-sequence/#email_type_of_a_step) for 1 week. In this case either another communication channel should be used or another lead from the same company should be engaged. If a prospect responds some time later, the status can be updated to *Success*, *Not interested*, or *Opted out*.


<br>
<br>
<hr>

## Custom Salesforce mapping to boolean or pick-list types of a field

When a contact’s or a lead’s status changes in Revenue Grid, it may get reflected in Salesforce according to custom mapping. It also may work other way around; if a status changes directly in Salesforce, then it gets reflected in Revenue Grid. Custom mapping of Revenue Grid statuses to Salesforce depends on each company’s needs and business flow. 

<div class="admonition hint">
<p class="admonition-title">Here is an example how it works</p>
<p style="font-size:16px"> Let's say you mapped an additional field (Rating) and its value (Warm), to the "Approaching" status.
<img src="../../assets/images/Settings/map-status.png" style="width: 90%; height: 90%;"/>
Explained:<br>
When a lead's Person status changes to Approaching in Revenue Grid, along with Salesforce field (Status) changing to "Attempting to Contact", also another Salesforce field (Rating) will get populated with corresponding value (Warm).
<br><br>
And since the "Bidirectional" checkbox is selected, similarly the mirroring will happen other way around as well. If the field (Rating) of a lead gets changed to (Warm), <b>AND</b> in the field (Status) gets changed to "Attempting to Contact" in Salesforce, then the lead's Person status in Revenue Grid will be changed to "Approaching".
</p>
</div>
<br><br>

<hr>
<img src="../../assets/images/Settings/addnewstatus.gif" style="float: center; width: 90%; height: 90%;"/>

#### How to create a new custom Prospect status and map to a Salesforce field (boolean or pick-list types)
Go to <a href="../Settings/#status_mapping">Settings→Status mapping</a>
<h3>8 steps</h3>
<p style="margin-left:2%;">
1. Choose what type of a status you want to add a new item to (you can add to Success or to Failed statuses, not to General ones)<br> 
2. Click "New status" button<br> 
3. Name you new status and click Confirm icon<br> 
4. Click "New mapping" button<br> 
5. Choose a Salesforce field (boolean or pick-list types)<br> 
6. Choose a value for that field to be populated once a prospect gets assigned the status<br> 
7. Press "Save" button on the bottom of the page<br>
8. OPTIONAL: If you want the status to get mirrored bidirectionally, then select the corresponding checkbox.
 <p style="margin-left:5%;">
 When selected, not only the chosen field will be populated with the chosen value in Salesforce once a prospect is assigned the corresponding Person status, but other way around as well. Meaning, if the chosen value gets populated in Salesforce, then in Revenue Grid the prospect's status will be changed to the corresponding one.<br><br>
 </p>
</p>

<br><br>

Refer to this article for description of [Sequence stages](../Sequences-Stages/#stages_of_sequences).










