This document outlines the causes and immediate actions following the App Engine outage on January 12th, 2024, and the measures we are implementing to prevent similar incidents in the future.
On January 12th, 2024, all Google App Engine applications experienced varying levels of service degradation for two hours and twenty minutes, from 7:48 AM to 10:09 AM PT (15:48 to 18:09 GMT). The outage was triggered by a power failure in our primary data center. Although the App Engine infrastructure is designed to recover quickly from such issues, this particular incident, coupled with internal procedural shortcomings, prolonged the restoration process.
Despite our preparedness for such failures, our response revealed several critical issues:
Our on-call staff had procedures in place for this type of outage, but they were unfamiliar with them and lacked sufficient training in the specific recovery process for this situation.
Recent improvements to the datastore's multihoming capabilities had altered the recovery procedure, but documentation was not fully updated, leading to confusion during the incident.
The production team lacked a clear policy for when and how the on-call staff should take decisive, user-facing actions like unscheduled failovers. This uncertainty led to a premature decision to return to a partially functioning data center.
We did not adequately plan for a scenario where a power outage affects only part of a data center (in this case, about 25% of machines). This oversight led to incorrect assessments of the data center's recovery status.
During the eventual migration of traffic to the backup data center, a small number of Datastore entity groups (affecting approximately 25 applications) became stuck in an inconsistent state due to the failover process. This affected less than 0.00002% of data stored in the Datastore.
Despite significant efforts to improve our handling of such outages over the past year, procedural issues diminished their effectiveness.
What Are We Doing to Fix It?
To prevent similar issues, we are implementing the following measures:
We will conduct regular drills for all on-call staff, covering all production procedures, including rare and complex ones. All team members must complete these drills before joining the on-call rotation.
We will perform bi-monthly audits of our operations documentation to ensure that all necessary procedures are easily accessible and that outdated documents are clearly marked as "Deprecated."
We will establish a clear policy framework to help on-call staff make quick, confident decisions about user-facing actions during failures, allowing them to respond more effectively in emergencies.
We believe these new procedures would have reduced the impact of last week's outage from about two hours of total downtime to 10-20 minutes of partial downtime.
In response to this outage, we are also making a significant infrastructural change to App Engine. Currently, App Engine offers a single Datastore configuration that provides low write latency and strong consistency at the expense of lower availability during unexpected failures. In light of this incident and user feedback, we are developing two Datastore configurations:
The existing configuration, offering low-latency and strong consistency with lower availability during unexpected failures (like power outages).
A new configuration that prioritizes higher availability using synchronous replication for reads and writes, but with significantly higher latency.
We believe offering these options will allow users to make informed decisions about the trade-offs they are willing to accept for their applications.
We apologize for the impact of the February 24th service disruption on your applications. While we are proud of App Engine's reliability, we recognize that there is always room for improvement. You can trust that we will continue to work hard to enhance the service and minimize the impact of low-level outages on our customers.
Timeline
7:48 AM: Internal monitoring detects issues in our primary data center, with an increasing number of errors. Users begin reporting problems in the Google App Engine discussion group.
7:53 AM: Google Site Reliability Engineers send a broad notification about a power outage in our primary data center. Although backup power generators are in place, around 25% of machines did not receive power in time and crashed. On-call staff is alerted.
8:01 AM: The primary on-call engineer assesses the situation and determines that App Engine is down. The engineer alerts product managers and engineering leads to handle communication about the outage. A brief post is made in the external group, indicating that the issue is under investigation.
8:22 AM: Analysis shows that while power has been restored, many machines remain offline, particularly those in the GFS and Bigtable clusters, rendering the Datastore unusable. The on-call team discusses initiating an unexpected failover to the backup data center.
8:36 AM: The App Engine team posts an update on the outage to the appengine-downtime-notify group and the App Engine Status site.
8:40 AM: The on-call engineer discovers conflicting procedures due to recent changes in the Datastore operations process. The team attempts to contact the engineers responsible for the changes to clarify the correct procedure.
8:44 AM: While waiting for clarification, the on-call engineer attempts to move traffic to a read-only state in the backup data center. However, an unexpected configuration issue prevents this from working correctly.
9:08 AM: Engineers are troubleshooting the read-only traffic issue in the backup data center. Meanwhile, the primary on-call engineer mistakenly believes that the primary data center has recovered and attempts to restore traffic there, without realizing that full recovery is unlikely at this stage.
9:18 AM: It becomes clear that the primary data center has not recovered, and traffic is moved back to the backup data center. The on-call team focuses on the failover process.
9:35 AM: An engineer familiar with the failover procedure is reached and begins guiding the team through the process. Traffic is initially moved to the backup data center in read-only mode.
9:48 AM: App Engine begins serving read-only traffic from the backup data center. Applications that handle read-only periods properly should now be operational, though in a limited capacity.
9:53 AM: The correct failover procedure is confirmed, and the full failover process begins.
10:09 AM: The failover procedure completes successfully, and App Engine resumes normal operations with full read and write capabilities.
10:19 AM: A follow-up post is made to the appengine-downtime-notify group, informing users that App Engine is now fully operational.
