---
description: Learn how to set up Role Hierarchy in your Salesforce org
---

# How to Set Up Role Hierarchy in Salesforce

*2 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

<br>

Configuration of [Role Hierarchy in Salesforce](https://help.salesforce.com/s/articleView?id=sf.ls_set_up_roles_and_hierarchies.htm&type=5) is a crucial prerequisite for the fully-fledged use of Intelligence Package by Revenue Grid. The data about users roles within an organization is used for pipeline reporting, sales forecasting, monitoring each team’s performance, and filtering by specific roles in your org. 

Role Hierarchy enables assigning users to roles, so that they can view, edit, and report on all data that’s owned by or shared with users below them in their role hierarchy. 

<br>
!!! warning "Important"
    Intelligence Package uses Salesforce Role Hierarchy as a primary source for Revenue Grid role hierarchy in sales reports. Thus, every user must be assigned to a role, otherwise their data won’t be displayed in [opportunity insights](https://docs.revenuegrid.com/articles/Opportunity-details/), [forecasts](https://docs.revenuegrid.com/articles/forecast-table/), [pipeline reports](https://docs.revenuegrid.com/articles/Reports-tab/), and other functionality offered by Revenue Grid. Lack of or incorrect roles assignment can lead to inaccuracies in sales reporting and forecasting. 
    
!!! tip "Tip"
    Set the users that require the visibility of the entire org performance at the highest level in Role Hierarchy. 
<br>
<hr>  

## To set up Role Hierarchy in your org:

<p style="margin-left:5%">
<img src="..\..\assets\images\intelligence-package\role-hierarchy\gear.png" style="width: 30%; float: right;margin-left:2%; margin-right: 10%;">
 <b>1.</b> Click on the <b>Gear</b> ⚙  icon and select <b>Setup</b>
    <br><br><br><br><br><br><br>
<img src="..\..\assets\images\intelligence-package\role-hierarchy\roles.png" style="width: 30%; float: right;margin-left:2%; margin-right: 10%;">
<b>2.</b> In the Quick Find box in the left-hand sidebar, enter <b>Roles</b> to quickly find the necessary setting 
    <br><br><br><br><br>
 <b>3.</b> On the opened page, click <b>Set up roles</b>
    <br><br>
 <b>4.</b> If you see the Role Hierarchy previously set up for your org, make sure that it includes all key figures on your sales team. 
 <br><br>
 If you see an empty page follow the steps provided below.  
 <br><br>
 <br>
 </p>

<p> 
<details><summary> Click here to see an example of how your org's Roles Hierarchy may look like</summary>
<img src="..\..\assets\images\intelligence-package\role-hierarchy\role-hier.png" class="minimized">
</details> 
</p>

<br>
<hr>
<br>
 
### Create a new role 

!!! tip "Tip"
    For using Intelligence Package offered by Revenue Grid, you don't necessarily need to add all roles existing in your company. You can add only the roles for sales team and key managers involved in sales. 
<br>

<p style="margin-left:5%">
    <b>5.</b> To <a href="https://help.salesforce.com/s/articleView?id=sf.admin_roles.htm&type=5">create a new user role</a> in your org’s Role Hierarchy: 
</p>
<p style="margin-left:10%">
    <b>5.1.</b> Find the role under which you want to add the new role. The person on the new role will report to the role under which it's created. If you are creating a top-manager role, you can add it directly under your org's name.
        <br><br>
    <img src="..\..\assets\images\intelligence-package\role-hierarchy\add-role.png" style="width: 40%; float: right;margin-left:2%; margin-right: 10%;"> 
    <b>5.2.</b> Click <b>Add Role</b> 
        <br><br><br><br>
    <b>5.3.</b> On the <b>New Role</b> page, fill in the required fields:
</p>
<ul style="margin-left:15%">
    <li>Label</li>
    <li>Role Name (auto populates)</li>
    <li>This role reports to (It’s auto-populated with the role name under which you added the new role, but you can also edit it.)</li> 
    <li>Role Name to be displayed in reports</li>
</ul>
</p>
<p style="margin-left:10%">
    <b>5.4.</b> Click <b>Save</b> to apply the changes 
</p>
<p>
    <img src="..\..\assets\images\intelligence-package\role-hierarchy\user.gif" style="width:80%">
</p>  


!!! note "Note"
    If you [create a new user using the Users page](https://help.salesforce.com/s/articleView?id=sf.adding_new_users.htm&type=5) and assign them a specific role in your org. They will **NOT** be automatically added to your org's Role Hierarchy. The role specification on the New User Creation page in Salesforce only means that this user **can** be assigned to the selected role in the Role Hierarchy. It's just an [administrative field](https://help.salesforce.com/s/articleView?id=sf.user_fields.htm&type=5) that specifies position of user within an organization. Such a user must be manually assigned to the corresponding role in Role Hierarchy and will appear on the list of Available Users for selected role on assigning user to role in Role Hierarchy.
<br>

<hr>
<br>

### Assign a user to an already existing role  
<p style="margin-left:5%">
    <b>6.</b> After creating the necessary roles, <a href="https://help.salesforce.com/s/articleView?id=sf.assigning_users_to_roles.htm&type=5">assign a user to the role</a>: 
</p>
<p style="margin-left:10%">
    <b>6.1.</b> Select the role to which you want to assign the user 
        <br><br>
         <img src="..\..\assets\images\intelligence-package\role-hierarchy\assign-userto-role.png" style="width: 50%; float: right;margin-left:2%; margin-right: 10%;"> 
    <b>6.2.</b> Click <b>Assign User to Role</b>  
        <br><br><br><br>
    <b>6.3.</b> Select the user you want to assign to the role in the <b>Available Users</b> column and click <b>Add</b> to add them to the <b>Selected Users</b> for Role column.
        <br><br>
    <b>6.4.</b> Click <b>Save</b> to apply the changes
</p>
<p>
    <img src="..\..\assets\images\intelligence-package\role-hierarchy\add-user.gif" style="width:80%">
</p>   
<br>

!!! tip "Tip"
    If you see no users in the Available Users column, try changing the Available Users Search filter above the column. 


<br>
<hr>
<br>

### Change the user that is already assigned to a specific role 

<p style="margin-left:5%">
    If you need to substitute an already assigned user with another user for a specific role: 
</p>
<p style="margin-left:10%">
    <b>1.</b> Select the role for which you want to change the assigned user
        <br><br>
     <img src="..\..\assets\images\intelligence-package\role-hierarchy\user-to-role.png" style="width: 50%; float: right;margin-left:2%; margin-right: 10%;">     
    <b>2.</b> Click <b>Assign User to Role</b>  
        <br><br><br>
    <b>3.</b> Select the user you want to unassign from the role in the the <b>Selected Users</b> column and click the <b>Remove</b> button.
        <br><br>
     <b>4.</b> Next, select the user you want to assign to the role in the <b>Available Users</b> column and click <b>Add</b> to add them to the <b>Selected Users</b> for Role column.
        <br><br>
    <b>5.</b> Click <b>Save</b> to apply the changes
</p>
<p>
    <img src="..\..\assets\images\intelligence-package\role-hierarchy\substitute.gif" style="width:80%">
</p>

<br>

!!! tip "Tip"
    If you see no users in the Available Users column, try changing the Available Users Search filter above the column. 

<br>
!!! tip "Tip"
    If your org is large with a large number of users, you can configure delegated administration and assign delegated administrators to manage users in specified roles and all their subordinate roles. You can refer to this Salesforce Help article for more information about [Delegate Administrators](https://help.salesforce.com/s/articleView?id=sf.delegating_user_administration.htm&type=5)
