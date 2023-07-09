---
title: List of Revenue Grid-assigned stages of a sequence
description: Detailed overview of Revenue Grid-assigned stages of a Sequence
---


  
# List of Stages your <i>Sequence</i> can be on

<p style="font-size:15px"><i>2 min read - updated few hours ago</i> </p>
<!-- ShareThis BEGIN -->
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis -->

Every prospect who is enrolled into a <a href="../Sequences/">sequence</a>, falls onto a certain stage associated with his/her life-cycle progress within the sequence. Once added to a sequence, initially a prospect is on "Not started" stage. Some sequence stage updates are automatic, others are initiated by RG users based on prospects' replies. 

![](../assets/images/Sequences/seq-stages.png)



------



### Stages of sequences



**Not started** - a prospect has been added to a sequence, but the sequence is not active or no step has been scheduled by the system yet.

**Started** - the first step of a sequence has been planned and scheduled by the system, but hasn't been executed yet.

**Approaching** - at least one step has been executed already, expecting more steps to execute.

**Success** - when on this stage, a prospect will not be reached out by sequence steps anymore. It means that negotiation with the prospect is taking place outside of Revenue Grid. A prospect gets to this stage when a RG user marks his/her [Person Status](../Prospect-Statuses/#types_of_person_statuses) so by choosing "Finished: Success" manually through [Action Center's Replies tab](../Replies/), or on the [Sequences' *Recipients* tab](../Recipients/#mass_actions) or via [Sequence widget](../Sidebar/). 

**Not interested** - a prospect gets to this stage when a RG user marks his/her [Person Status](../Prospect-Statuses/#types_of_person_statuses) so by choosing "Finished: Not interested" manually through [Action Center's Replies tab](../Replies/), or on the [Sequences' Recipients tab](../Recipients/#mass_actions) or via [Sequence widget](../Sidebar/). 

**Opted out** - when a prospect is on this stage, it means either he/she has unsubscribed through [the unsubscribe link](../Settings/#unsubscribe_links) or RG user marked his/her [Person Status](../Prospect-Statuses/#types_of_person_statuses) so on [Action Center's Replies tab](../Replies/), or on the [Sequences' Recipients tab](../Recipients/#mass_actions), or on the [profile page](../People/#contactlead_profile), or via [Sequence widget](../Sidebar/).

**Bounced** - this stage is auto-assigns when *Undelivered Mail Returned to sender* type of an email is received in response to your email type of a step. Or else you can assign a prospect to Bounced [Person Status](../Prospect-Statuses/#types_of_person_statuses) via [Sequence widget](../Sidebar/) and in its turn this stage will be assigned automatically.

**Unresponsive **- this stage is auto-assigned when there has been no response from a prospect to an email type of a step for 1 week.



------



### Corresponding Person Status

This table represents corresponding [Person Status](../Prospect-Statuses/#types_of_person_statuses) per each Sequence Stage available in Revenue Grid.



<table>
    <thead>
        <tr>
            <th rowspan=3 colspan=3 align="center"><b>Revenue Grid</b></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center"><b>Sequence Stage</b></td>
            <td align="center"><b>⇄</b></td>
            <td align="center"><b>Person Status</b></td>
        </tr>
        <tr>
            <td align="center">Not started</td>
            <td align="center">↔</td>
            <td align="center">Not contacted</td>
        </tr>
            <td align="center">Started</td>
        	<td align="center">↔</td>
            <td align="center">Just added</td>
        </tr>
        <tr>
            <td align="center">Bounced</td>
            <td align="center">↔</td>
            <td align="center">Bounced</td>
        </tr>
        <tr>
            <td align="center">Approaching</td>
            <td align="center">↔</td>
            <td align="center">In progress</td>
        </tr>
        <tr>
            <td align="center">Opted out</td>
            <td align="center">↔</td>
            <td align="center">Unsubscribed</td>
        </tr>
        <tr>
            <td align="center">Not interested</td>
            <td align="center">↔</td>
            <td align="center">Not interested</td>
        </tr>
         <tr>
            <td align="center">Success</td>
            <td align="center">↔</td>
            <td align="center">Success</td>
        </tr>
         <tr>
            <td align="center">Unresponsive</td>
            <td align="center">↔</td>
            <td align="center">Unresponsive</td>
        </tr>
    </tbody>
</table>











