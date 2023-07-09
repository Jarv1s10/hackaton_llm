---
description:
---

# Revenue Leaks Funnel

**[This article is work-in-progress]**

<p style="font-size:15px"><i>3 min read - updated few hours ago</i></font></p>
<!-- ShareThis BEGIN -->
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis -->
</p>

Revenue Leaks Funnel visualizes the sales process based on the data from Salesforce. It provides a detailed overview of stage-to-stage Opportunities conversion and leakage. 

<p>
    <img src="../../assets/images/2301/revenue-leaks.png" class="minimized"/>
</p>
<br><br>
<hr>

### All Opportunities in the period


**NEW** – the Opportunities whose creation date is in the selected period and whose close date is or was in the selected period. 

**PULLED IN** – the Opportunities that were created before the selected period started and whose close date changed from the future period to the selected period. 

**EXISTING ON START** – the Opportunities that were created before the selected period started. As of the beginning of the selected period, their close date was in the selected period. 

**PUSHED IN** – the Opportunities whose close date changed from the previous period to the selected period during the selected period. 

<br>
<hr>
<br>

### Opportunities' evolution thoughout the period


**ON STAGE** – the Opportunities that are at this stage in the selected period. 

**EXISTING ON START** – the Opportunities that were created and existed at this stage before the selected period started. 

**SUCCESSFULLY PASSED** – the Opportunities that were at this stage and moved to the next stage in the selected period. 

**SKIPPED** – the Opportunities that skipped this stage and moved to the next stage in the selected period. 

**SLIPPED** – the Opportunities whose close date changed from the selected period to the next period. 

**LOST** – the Opportunities that were lost at this stage in the selected period. 

<br>
<hr>
<br>

## See the numbers that matter

Revenue Leaks Funnel visualized how Opportunities move from one stage to another in numbers. In the top section of the funnel, you can see:

<img src="../../assets/images/2301/numbers.png"  style="width:80%;"/> 

<p style="margin-left:5%; margin-right:10%;"> 
<b>1.</b> Opportunities stages according to the stages mapping in Salesforce
<br><br>
<b>2.</b> Amount of the Opportunities that moved to the next stage in dollars and percents from the sum on the previous stage
<br><br>
<b>3.</b> Number of the Opportunities that moved to the next stage and the percentage from the number of Opportunities on the previous stage
</p>

