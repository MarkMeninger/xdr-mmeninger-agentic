# Cursor Project: Create Variable CQL Requirements and related artifacts

## Business Objectives

Original requirements from CSM meeting to support homenet variables for use in reports across all iSensors.

CSMs manually create hundreds of reports showing directional traffic for customers using complex search queries.

Variables would allow new reports to be generated that could be re-used across all sensors saving hundreds of CSM hours and solve a business need asked by all iSensor customers.

## Cursor Opportunity

Provide an MVP deliverable that would have Claude examine all artifacts to create a holistic set of output requirements using

1. Original customer requirements including the query use-cases created today by CSMs for all iSensors to observe sensor traffic.
2. The NIDS schema which would be the input source into the CQL variables to solve the business problem as well as input into example queries that would be part of the MVP.
3. Taegis Advanced query user-docs to educate the LLM on CQL syntax and functionality.
4. Templates for epics, Taegis user docs and release notes to generate the content that can be submitted to the engineering and docs team.

## Key Folders in this Repo

**Data** contains

- **A) Taegis-Docs:** Source files from Taegis docs teams for several CQL functionality areas used to train the LLM.
- **B) Requirements gathering content:** Contains all the inputs for creating the output requirements.
- **C) Competitive:** Holds references to similar capability in SIEMs with variable support. I thought about passing this to Claude but ended up not needing to.
- **D) Taegis-Schemas:** Holds the NIDS protobuf schema definition file.

**Learning**

Contains KT (knowledge transfer) items from the LLM to me that I want to keep record of.

**Output**

Contains the artifacts that I would manually generate as part of my job.

**Src**

Contains source code that Claude generated for a few purposes, mostly for generating content from the templates I created for my requirements and docs deliverables. It also contains the templates Claude and I came up with to generate my deliverables.

**Test**

This folder was used to hold outputs from the LLM so I could evaluate quality and completeness.

## Lessons Learned

1. This is an extremely powerful way to create outputs. I was able to in a single place aggregate all my input data, review and analyze in real-time to deliver.

2. Claude was able to quickly learn without me explicitly defining context guardrails and deliver what I wanted. Once I saw this happening I just continued on until I finished my outputs.

3. I am barely scratching the surface. This was a rapid output that I think is good quality. However as I didn't set context to the LLM I didn't learn that power and ability to generate my output in that way.

4. **TODOs**
   - **a)** Automate access to source code vs my download and paste locally. Would be much faster.
   - **b)** Build hooks into the source code to have Claude give me guidance on effort and feasibility. T-shirt sized project and why.
   - **c)** Re-usable workbench: refactor my work to have a reusable Claude workbench that I can re-use across projects. This is hard-coded.
   - **d)** Create hooks into Jira and other tools to automate my requirements definition.
