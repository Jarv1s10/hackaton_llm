---
description:
---
# Salesforce Forecast Categories and Opportunity Stages

*4 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

## Standard Salesforce forecast categories 

A forecast category is a category that is assigned to an opportunity based on its opportunity stage. The forecast categories help sales representatives and managers to navigate through their sales process in the current sales period. They ensure better visibility and performance monitoring.  

<a href="https://www.salesforceben.com/forecast-categories-in-salesforce-everything-you-need-to-know/"> Salesforce forecast categories</a> are the baseline for [Revenue Grid reports](https://docs.revenuegrid.com/articles/Reports-tab/) and [forecasts](https://docs.revenuegrid.com/articles/forecast-table/) which are intended to ensure higher sales visibility and more customized projections. Thus, proper configuration of forecast categories and opportunity stages is an essential prerequisite for the seamless use of Revenue Grid functionality. 

<br>
The standard Salesforce forecast categories are: 
<p style="margin-left:7%">
    <b>Pipeline</b> – The sum of opportunities that are in the early stages of the sales process. 
        <br><br>
    <b>Best Case</b> – The sum of opportunities that may be won by the end of the current period, given the ideal sales process scenario. 
        <br><br>
    <b>Commit</b> – The sum of opportunities that are going well and are likely to be won during the current period 
        <br><br>
    <b>Omitted</b> – The opportunities that were closed with the “lost result”. This figure is omitted in the forecasts. 
        <br><br>
    <b>Closed</b> – The sum of the Opportunities that were closed won during the current period. 
</p>



<hr>

## Opportunity Stages

Forecasts are built based on the mapping between the Opportunity Stage and the Forecast Category. You can customize the mapping between the Opportunity Stage and the Forecast Category to ensure that it accurately reflects the sales process in your company.  

Here is the example of a standard Salesforce stage mapping: 

<p>
    <img src="..\..\assets\images\intelligence-package\opp-stage\example.png" class="minimized" style="width:90%">
</p>

<br>
<hr>
<br>

!!! tip "Tip"
    Opportunities stages and categories must be mapped reasonably to ensure that your team can benefit from using RG reports and forecasts. For example, if all stages from 10% to 90% fall within the Pipeline category in your company's mapping, it's recommended to change the mapping to match your company's actual sales cycle.
<br>


### How to change stage mapping for forecast categories 

If necessary, you can change the mapping between Opportunity Stages and the Forecast Categories. To do that: 

<p style="margin-left:7%">
    <b>1.</b> In Sales Console, switch to <b>Opportunity</b> in Navigation Menu
    <br><br>
        <img src="..\..\assets\images\intelligence-package\opp-stage\2.png" style="width: 30%; float: right;margin-left:2%; margin-right: 10%;">
    <br>
    <b>2.</b> Click the <b>Gear</b> (Setup Menu) icon in the upper right corner of the page
     <br><br>
    <b>3.</b> Select <b>Edit Object</b>
     <br><br> <br><br>
     <img src="..\..\assets\images\intelligence-package\opp-stage\4.png" style="width: 30%; float: right;margin-left:2%; margin-right: 10%;">
    <br>
    <b>4.</b> Go to <b>Fields & Relationships</b>
     <br><br>  <br><br>
    <b>5.</b> On the list, find <b>Stage</b>
     <br><br>
    <b>6.</b> Scroll down to <i>Opportunity Stages Picklist Values</i>
     <br><br>
    <b>7.</b> Click <b>Edit</b> next to the Stage to change its mapping. 
    <br> <br>
    Or click <b>New</b> to create a new stage
    <br><br>
   <b>8.</b> You can change the percentage for the stage, forecast category for the stage, and add a description
   <br><br>
  <b>9.</b>Click <b>Save</b> to apply the changes
   <br><br>
        <img src="..\..\assets\images\intelligence-package\opp-stage\7.gif" class="minimized">
    <br>
</p>