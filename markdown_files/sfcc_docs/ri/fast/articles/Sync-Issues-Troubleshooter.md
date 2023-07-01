---
description: Revenue Grid Sync Engine errors troubleshooting table
---
# {{ company_name }} Synchronization Error Codes  
  

<i>For users of the Email Sidebar on:</i><br><br>
<div class="container" style="display: inline-block; height: 42px; width: 162px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Exchange1.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: 163px; padding: 5px 10px; background-color: #fff;"><img src="https://revenuegrid.com/revenue-inbox/wp-content/uploads/Office365.svg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div><div class="container" style="display: inline-block; height: 42px; width: auto; padding: 5px 10px; background-color: #fff;"><img src="https://smartcloudconnect.io/wp-content/uploads/2021/08/logo-Gmail.jpg" style="height: 100%; object-fit: contain; vertical-align: middle;"></div> 

&nbsp;

*6 min read*  

<!-- ShareThis BEGIN --> 
<div class="addthis_inline_share_toolbox"></div>
<!-- End ShareThis --> 

&nbsp;

This sync issues table is an addition to the articles [one](../Handling-Sync-Issues/) and [two](../Monitoring-Users-and-Organizations/) on monitoring end users' synchronization status in [{{ product_name }} Admin panel](../How-to-Log-In-to-the-Admin-Panel/).



**Error types**

**SE errors:** are registered during a sync session, do not suspend synchronization

**SC errors:** are caused by problems in configuration, synchronization is stopped

**SD errors:** appear when invalid data is retrieved from either side; only some of these errors stop synchronization

**SI errors:** internal sync engine errors

**SW errors:** statuses listed in the sync dump and log file. If an error occurs on a sync session, this status serves as the error description

&nbsp;

**Error severity levels**

**(L)ow:** issue does not affect synchronization

**(M)oderate:** issue is likely to affect synchronization

**(S)evere:** issue stops synchronization and can normally be fixed locally

**(C)ritical:** issue stops synchronization and cannot be fixed locally

&nbsp;

**Sync Engine errors troubleshooting table**

| **Error code** | **Severity** | **Cause(s)**                                                 | **Solution**                                                 |
| -------------- | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| SC0001         | M            | Key field:{ ':(field name)':}:{ for type ':(type name)':} does not exist or is not supported | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SC0002         | L            | Unable to synchronize because both storages declare the 'provide object-state' procedure | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SC0003         | L            | Both storages support up-syncing                             | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SC0004         | L            | Both storages provide read-only records                      | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SC0005         | L            | Setting states for read-only records is not permitted        | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SC0006         | L            | Removing unmatched records for read-only records is not permitted:{ (type: ':(type name)'):} | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SC0007         | L            | Link restoring is not permitted for read-only records:{ (type: ':(type name)'):} | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SC0008         | L            | Orphan cleanup is not permitted for read-only records:{ (type: ':(type name)', link field: ':(link name)'):} | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SC0009         | L            | Neither storage supports up-syncing                          | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SC0010         | S            | The type:{ ':(type name)':} was not found among synchronization types | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SC0011         | S            | Snapshot creator support is specified in storage features, but no actual support is detected | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SC0012         | L            | Custom deduplicator expected                                 | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SC0013         | L            | Maximum query length (max_query_size parameter) is set to zero for the custom deduplicator | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SC0014         | C            | Undefined state is not permitted for records:{ (object id ':(object id)'):} | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SC0015         | C            | Unknown record type:{: ':(type name)':}                      | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SC0016         | M            | Merge conflicts resolution is not permitted:{for ':(type name)':} | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SC0017         | M            | Synchronization scheme contains duplicate types:{: :(type name):} | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SC0018         | M            | Synchronization type:{ ':(type name)':} contains duplicate links:{: :(link name):} | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SC0019         | M            | No fields were found in the natural key of synchronization type:{ ':(type name)':} | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SC0020         | M            | Synchronization type:{ ':(type name)':} contains duplicate fields in the natural key:{: :(field name):} | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SC0021         |              | reserved                                                     |                                                              |
| SC0022         | L            | Exclusions processing is not permitted for external snapshot creator | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SC0023         | L            | Limiting the number of snapshot records is not permitted for external snapshot creator | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SC0024         | L            | Declaring the 'support frequency' feature is not allowed for external snapshot creator:{ (type: ':(type name)'):} | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SC0025         | L            | Wrong custom object state was detected:{ (state: ':(name)', value: :(value)):} | Check your synchronized data and resync                      |

 

| Error code | **Severity** | **Cause(s)**                                                 | **Solution**                                                 |
| ---------- | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| SD0000     | C            | Record already synchronized:{: ':(object id)':}:{ in ':(storage id)':} | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SD0001     | L            | Record type mismatch:{ ':(type name)':}:{ vs. ':(existing type)':}:{ for ':(object id)':}:{ in ':(storage id)':} | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SD0002     | M            | Additional affiliates (values for link fields in object info) were detected for:{ ':(type name)':} object:{ (id=':(object   id)'):} | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SD0003     | C            | Returned fields number:{ (:(returned amount)):} is not equal to the number of requested fields:{ (:(requested amount)):}:{ for object ':(object id)':} | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SD0004     | C            | Unknown duplicate source record:{ (:(object id)):}           | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SD0005     | C            | Type specified by deduplicator differs from type provided by sync engine for the following record:{ (:(object id)):} | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SD0006     | L            | Record:{ ':(object id)':}:{ in storage ':(storage id)':} was not found | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SD0007     | C            | Returned:{ ':(type name)':} records number:{ (:(returned amount)):} does not equal to requested records number:{ (:(requested amount)):} | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SD0008     | C            | Returned fields number:{ (:(returned amount)):} does not equal to requested fields number:{ (:(requested amount)):}:{ for object ':(object id)':} | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SD0009     | C            | Duplicate IDs were detected for the following records:{: ':(object id)':} | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SD0010     | C            | Reused record identifier was detected:{ (reused id ':(object id)'):} | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SD0011     | C            | Invalid filter criteria were detected:{ (:(value)):}         |                                                              |
| SD0012     | C            | Types mismatch:{ for ':(object id)':}:{: ':(type name)' and ':(existing type)':} | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SD0013     | C            | Duplicate record:{ id ':(object id)':}:{ of ':(type name)':} | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SD0014     | C            | The :{':(type name)' :} object identifier cannot be empty    | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SD0015     | C            | The :{':(type name)' :}object identifier cannot be set to a value that indicates a broken link | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SD0016     | C            | The :{':(type name)' :}object:{ (:(object id)):} affiliate:{ #:(index):} identifier cannot be empty | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SD0017     | C            | The :{':(type name)' :}object:{ (:(object id)):} affiliate:{ #:(index):} identifier cannot be set to a value that indicates a broken link | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SD0018     | C            | The :{':(type name)' :}object:{ (:(object id)):} affiliate:{ #:(index):} type cannot be empty | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SD0019     | L            | Maximum snapshot records limit is exceeded:{ (:(limit)/:(total)/:(pinned)):} | Change filters or unpin some objects in  Customization settings, then resync |
| SD0020     | C            | The meta_descriptor type:{ ':(type name)':} contains duplicate fields:{: :(field name):} | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SD0021     | C            | Created snapshot is not integral:{: :(value) unresolved objects:} | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SD0022     | C            | Failed to retrieve the records of the following type:{ ':(type name)':}:{ (requested: :(requested amount), returned: :(returned amount), inaccessible: :(inaccessible amount)):} | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SD0023     | M            | Reverting changes is not applicable for record (:{object id ':(object id)':}:{ from ':(storage id)':}) | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SD0024     |              | reserved                                                     |                                                              |
| SD0025     | M            | Synchronization was stopped in order to prevent creation of duplicates for the following item(s):{ (:(total)):}: :{:(object id 0) in :(storage id 0):}:{:(object id 1) in :(storage id 1):}:{:(object id 2) in :(storage id 2):}:{:(object id 3) in :(storage id 3):}:{:(object id 4) in :(storage id 4):}. Please check if any other synchronization solution is running and disable it. To resume sync, modify/delete objects causing duplications and resume sync. | Check your synchronized data and resync                      |

 

| Error code | **Severity** | **Cause(s)**                                                 | **Solution**                            |
| ---------- | ------------ | ------------------------------------------------------------ | --------------------------------------- |
| SE0001     | L            | Adding read-only records is not allowed                      | Check your synchronized data and resync |
| SE0002     | L            | Parent record was not added:{ (link field ':(link   name)'):} | Check your synchronized data and resync |
| SE0003     | M            | Reused record identifier detected:{ (reused id ':(object id)'):} | Check your synchronized data and resync |
| SE0004     | L            | Target record from post-update list was not found:{ (object id ':(object id)'):} | Check your synchronized data and resync |
| SE0005     | L            | Target record from post-update list was updated   prematurely:{ (object id ':(object id)'):} | Check your synchronized data and resync |

 

| Error code | **Severity** | **Cause(s)**                                                 | **Solution**                                                 |
| ---------- | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| SI0001     | L            | The query_objects method is not implemented for stale_requestor | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SI0006     | L            | Local_id:{ ':(object id)':} does not exist                   | Check your synchronized data and resync                      |
| SI0007     | L            | Columns:{ ':(field name)':} already exist                    | Check your synchronized data and resync                      |
| SI0008     | L            | Field:{ ':(field name)':} does not exist                     | Check your synchronized data and resync                      |
| SI0009     | L            | Invalid VARIANT passed                                       | Check your synchronized data and resync                      |
| SI0010     | L            | Invalid base passed                                          | Check your synchronized data and resync                      |
| SI0011     | L            | Values count must match column size:{ :(value):}!            | Check your synchronized data and resync                      |
| SI0012     | L            | The job requested to run has already been completed          | n/a                                                          |
| SI0013     | L            | Synchronization failed to complete                           | Check [Issues tab in Sync dashboard](../Handling-Sync-Issues/) for conflicts for more information |

 

| Error code | **Severity** | **Cause(s)**                                                 | **Solution**                                                 |
| ---------- | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| SW0000     | L            | Synchronization was completed successfully                   | n/a                                                          |
| SW0001     | L            | Synchronization was interrupted by user or by {{ product_name }} | If this code appears not on user terminating sync manually but on sync session timeout (it is set to 1 hour by default), please [Contact us](mailto:support@revenuegrid.com) to get the timeout value increased |
| SW0002     | M            | Detected: :{:(conflicts amount):} conflict(s), :{:(duplicates amount):} duplicate(s), :{:(issues amount):} issue(s), :{:(confirmations amount):} confirmation(s) | Check [Issues tab in Sync dashboard](../Handling-Sync-Issues/) for conflicts for more information |
| SW0003     | S            | Unknown internal error occurred                              | [Contact us, describing the issue in detail](mailto:support@revenuegrid.com) |
| SW0004     | M            | Detected: :{:(conflicts amount):} conflict(s), :{:(duplicates amount):} duplicate(s), :{:(confirmations amount):} confirmation(s) | Check [Issues tab in Sync dashboard](../Handling-Sync-Issues/) for conflicts for more information |



&#160;
 &#160;

