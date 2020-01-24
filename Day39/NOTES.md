2020 - 1 - 24
=============

Goals
=====
  * Learn some things about code or computer science or python
  * Go down rabbit holes
  * Have fun
  * Viewer Code Review


Topic
=====
  * Multi-Tenacy Applications
    Multiple users, sharded data across multiple sources,
    for data isolation and what not.


Beanie Baby™ TY™ Application for store info about their collections.


DB Multi-Tenancy
  - Store Beanie Baby info, we don't want the data in the same
    database as another users. ArtMatt is super concered about his
    Beanie Babies
  - Begin has his won DB

Application Tenency:
  - ArtMatt wants this skin, and these customizations.
    artmatt.beanie.ty
  - begin.beanie.ty


Personal Experience
---
  * Do you have 2 customers yet?
    Or are you going to exercise the multi-tenant functionality
    always often.

    Problem with developing Multi-Apps:
      - Building with 2 clients in mind, only ever
        really having one, or just developing, and using
        one. And you think you applicaton is multi-tenant.
        Once you actually get client number 2, things fall apart.
      - If you don't have multiple customers, you shouldn't try to
        multi-tenant.
      - This could be over-engineering in the beginning.

Is this for money or fun???
  - Money: Overengineering
  - Fun: Hell yeah, lets do it


You have to plan ahead alot more:
  * How are we deploying instances of our application
    New Customer signs up, what do we have to do
    to give them an instance?
  * Whats the breakdown between infrastructure and application,
    shared stuff and what consistutes an instance.
    Centralized Logging for internal, that all instances connect to.
    each instance needs a DB.
    Code + Datastore. Docker Images to ECS and an RDS cluster.
  * In our code, we are going to have shared code, then other code
    that has to be multi-tenant aware. This is a big problem.
    Rememebr to scope every single query to a client, build some
    abstraction or framework.



Client Sign Up Story
====================

You are trying to sell your on-prem business:
  * Theres a whole crew of people in the company,
    trying to move off prem, and cloud is the biggest
    buzzword.


## On-Prem Story
  * Ohh I want to sign up for service!
  * Schedule time to go on site
  * Figure out thier hardware setup
  * Install software bespoke by hand
  * On-Board and Test
  * Schedule a maintence schedule and on-call
  * Determine and SLA.
  * Client uses Software!


## Cloud Native Story
  * Ohh I want to sign up for service!
  * Sign-up on the spot
  * automation creates and deploys tenant quickly
  * Client is using application


We can do On-Prem, as long as we are ok with not being able to:
  * scale
  * afford engineers
  * have people sleep at night


Deploy Story:
============
  - Docker Image of Code
  - Whats the language
  - How do we make money
  - Both these things are on-prem
  - Django Application
  - Postgresql
    - On Prem


Advice for Multi-Tenancy:
=========================
  * If you have to build infrastructure for each client.
    Then that infrastructure needs to be in code, needs to be
    easily deployable and teardownable.
    Have to use one of the following:
      - Cloudformation
      - Terraform
      - Pulumi
      - Something!


Options:
========

Multi-Tenancy On-Prem
  The hardest one to build, maintain, scale, deploy.
  Costs the most
  Riskiest
  Estiamted Cost: $500,000
  Estiamted Annually Cost: $100,000


Multi-Tenancy Cloud Native
  Estiamted Cost: $100,000
  Estimated Annual Cost: $10,000

AWS Outposts
===
  * AWS managed on-prem server, you can run RDS, and anything,
    9,000 and they do it for you.



Problem:
===
  * Client wants software
  * Client has an unecceary restriction or requirement that makes it harder
    to make said software for no reason.



I would do some fact gathering and documentation:
---
  * When did you decide to do On-Prem?
  * Who
















Viewer Questions
================

Questions
=========

Learnings
=========
  * AMD the go to CPU
  * Nvidia is the leader in GPU, but AMD is lil cheaper
  * 50% of the cost of Computer should be GPU

Ponderings
==========

Opinions
========
  * On-Prem versus Cloud Native Multi-Tenancy Apps are entirely different Beasts

Debates
=======

Python Interview
================

Scraps
======


Quotes
======
  - "Ideas aren't worth anything. Execution is."
  
