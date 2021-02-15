# celonis_case_study

Solutions Architect - Interview Challenge

Setting the scene
You are a Solutions Architect at Celonis and the Sales Team have closed a two process deal at ACME Healthcare, a major healthcare company. The two processes they have decided to analyze are their Purchase to Pay process and claims adjudication process.
Before implementation can begin, the security architect at ACME Healthcare would like to understand how Celonis will fit within their IT architecture and landscape.
The Sales Executive who has led the deal has insight into their setup and has provided you with the following information:

1.	The security architect for ACME Healthcare already has had a short intro into the product from his colleagues and knows its purpose.
2.	ACME Healthcare is a large multi-national organization and it's implied not all of their IT is universal across all business units.
3.	The data relevant for their procurement process is on Oracle EBS.
4.	The underlying source system for where the Claims Data lies cannot be accessed directly by Celonis, but ACME will be able to provide flat file exports.
5.	As ACME is a healthcare company, they are very security conscious.

Part 1 – Customer Onboarding
You are to engage the customer and hold a 10 minute presentation to establish a plan on how the company’s business technical requirements can be satisfied so the Celonis implementation project can begin.

We will be expecting you to drive the session and obtain the answers you need to draw a rough outline of how you would implement and deploy Celonis to the client. You will need to come prepared to present the following:

•	Data Integration Oracle EBS
a.	Describe the process of extracting data from their Oracle EBS system using the JDBC connector for their procurement process.
b.	Describe at a high level the steps needed for the server team, database team, and network team.
•	User Authentication
a.	How users will be authenticated in Celonis via SAML?

Please prepare a couple slides to share this information with ACME’s security architect.

Part 2 – Data Pipeline
For the claims data, the customer has now given you below sample flat file export and have asked you to evaluate, whether and how this file can be imported into Celonis IBC.
Please provide a short overview of available options.
Please write a short python snippet that reads the data and delivers it to the Celonis Data Push API. The code should be handed over to ACME’s security architect for a short review, so please make sure to keep your code clean and documented. 
As a bonus goal, you could show the loaded data in an analysis in Celonis IBC – if that doesn’t work out, don’t worry! The main goal of this exercise is to connect the data to IBC, not analyze it.
 

Helpful links to prepare for the session
Celonis IBC Documentation: https://help.celonis.cloud
Celonis IBC Overview: https://help.celonis.cloud/help/display/CIBC/Celonis+Intelligent+Business+Cloud 
Data Input Documentation: https://help.celonis.cloud/help/display/CIBC/Data+Input 
SSO Documentation: https://help.celonis.cloud/help/pages/viewpage.action?pageId=12321316
Celonis Reference Documentation: https://celonis.github.io/pycelonis/reference.html
Celonis Security Documentation: https://www.celonis.com/trust-center/
