# Formal Requirements

The project must be passed to attend the oral exam.

The project should be done in groups, preferably of 4 people and not more than 5 people per group. The report must contain a section stating who wrote what part of the report.

The project will consist of three ‘parts’. Part one will cover how we structure our process, backlog, and initial release planning. Part two will cover the initial design of the Minimum Viable Product (MVP) and implementation of some of the system. Part three will cover extended testing and integration of the system with 3rd party systems.

Part two and part three will be based on the previous parts of the project. All parts of the project will be based on the same interview. Document all assumptions you make!

If you don’t comply with these requirements you will fail the project!

This project is a made up case, but will have a lot of resemblance to the real world

# Background And Vision

I’m so happy that you want to be a part of this start-up. It’s going to be awesome! We need to get the first product into the hands of our customers as soon as possible to help us become profitable and to make money to continue our work.

I have managed to find our first client for our product. This first customer is super important to us, and is willing to buy the project if we can show good progress with a steady stream of deliverables.

Let us look at our product idea, in case you forgot: We want to build a system where our client can keep track of their inventory. What is in stock, what needs to be ordered from our suppliers, and a initial version of a shopping basket.

This of course needs to be an online service with a corresponding (mobile friendly) website and maybe at some point a dedicated app. For starters, people working in the warehouse needs an easy to use website.

# Interview with an Manager

**Carsten**: Thank you so much for showing an interrest in our product! I am really stoked that you took the time out of your, I assume, busy calendar to talk to me! Can you maybe tell me a bit about yourself and the company you work for?

**Manager**: My name is Mr. Manager. I have worked within consumer goods for more than 10 years, and the last 3 years have been here in Gravia Moribunda (_Henceforth called **GM**_). GM is a distributor of pots and pans. We have a rather big group of travelling salesmen going from store to store to sell our products, and a lot of staff working in our warehouse. Our problem is our old IT systems from, properly, before you were even born. It is really showing its age.

**Carsten**: I don’t think we can do anything about the Travelling Salesmen, but I would suggest you to talk to O(n)-time Solutions. They have a really promising heuristic in the making. But we can do something about your IT system!

**Manager**: Ha ha. I know. The handling of inventory would is essential! Every salesman needs to know what products can be sold to a store, and at the moment we are spending quite a lot of time handling this manually at our main warehouse. Some send requests via email, some by iMessage, some send them with the Postal Service and some only give them to us when they are in the office. This process is very time consuming for us, and makes it difficult for us to close a given month from a financial view because we might get some orders after 2-3 months, due to very slow postal service. We would also like at some point to look at integrating with our different suppliers ordering systems. That would also be really useful for us!

**Carsten**: How would you know this situation had improved?

**Manager**: Hmm, that is a really good question! Let me think for a second.

I would know it has become better when we only get orders from the salesmen in one channel. I don’t know if this should be email or a separate system. Emails are easy, but we have an entire group of people handleing the orders and sometimes we end up handling the same orders twice. Hence, it would be nice to have some kind of system that would show if the orders had already been handled and shipped.

**Carsten**: Ok, is correct to say you would like a system that gives you a simple overview of the incomming orders and wether or not they have been packed correctly, and later shipped?

**Manager**: Yes, but we also need to make sure that everything is in order, hence we need to make sure that we have the shop information like adress, manger etc. Hmm. What else? Hmm… Let me think… A list of items the store have ordered, which store that ordered it, who is their contact on our side, what discount did they get, and… Hmm… I think that is it.

**Carsten**: Would it be OK if we talked to a couple of the salesmen to hear how they would like to submit their orders? And then maybe we can come up with a good way to make it easy for the salesmen, while at the same time automate as much as possible of the filing it afterwards? After that we can talk with the warehouse people. Would that be OK with you? Or would you rather that we focus on the warehouse first?

**Manager**: You are more than welcome to try, but they are not hourly paid, hence they do not earn anything when they are talking to you. But you are welcome to try to talk to some of them. I can give you a list of potential people to talk to.

**Carsten**: That would be really awesome! Thank you! You mentioned something about integrating with your suppliers to restock your own warehouse. Should we look into that?

**Manager**: Yes please. We have two primary suppliers, let us call them **A** and **B**. They both provide an API for ordering products from them, but their API differs a bit. But I’m sure you’ll manage. I would like us to be able to automatically order items from the two suppliers if our stock level gets under 5. The number 5 might need to be updated, hence make it easy to change.

From what I have heard both suppliers have some developer documentation available that I guess can answer the questions you migt have. If not, please let me know, and I will see if I can find the correct person for you to talk to.

**Carsten**: Ok! Thank you for letting me know! I think I have something to go on now! I will take it to the Development Team and I’m pretty sure the Product we are developing will solve a lot of your problems.

# Part 1: Preparing our Process

In the first part of the project, your group needs to make the necessary preparations for the first sprint(s).

The report must include:

- A description and classification of the different stakeholders
- A description and classification of the different users (End Users, Super Users, and System User)
    - Who will be the user base? What is in it for them?
    - Who will maintain the platform on a daily basis and offer support to end users?
    - Which internal and third party systems will interact with out system?
- A prioritized backlog containing all found requirements, both functional and non-functional in a format of your choice
- An discussion on how and why you choose to structure your backlog as you did

For all of the items above you must:

- Document your decisions
- Document your assumptions
- Discuss your approach to the task and your solution of it
- Include the outcome of the task either in the report or in an appendix

# Part 2: Making our First Product Delivery

In this second part of the project we will start to focus on implementing our new system.

## Flows in the System

To align inside the team, we have agreed to make a workshop to align on how the flows should be in the system.

You must provide UML Sequence Diagrams for each flow/User Goal, and one consolidated UML Class Diagram with all the identified Domain classes. Document your sequence diagrams and your classes.

- Create and Submit order from a salesman
- Order items from suppliers **A** and **B**

## API For Mobile Apps

We have had a new meeting with the **Manager** from GM. He would like to create apps for smartphones using an external company. Hence, we need to make an API specification for this. This must be documented using Swagger or Open API. In this first iteration we need to specify the following endpoints:

- Fetch a list orders for the specific salesman
- View order details
- Create a new order

All these endpoints needs to be secured using API Keys. The API must be on at least level 2 of the Richardson Maturity Scale.

You must document your design design decisions, why and how you came up with the input, output and models. You must provide the specification as an appendix in the report.

This is only about specification, not about implementing it!

In a real project, we would start to agree on the interface, before going to the implementation.

## Implementation and Testing

> [!WARNING]
> To keep the scope of this assignment reasonable it is accepted to store data in memory (HashMap, LinkedList, …) with no persistence. But you must document this and what consequences does that have.

We need to quickly get something to the hands of our users. For this we need to start the implementation as soon as possible. It is important that we get a system that is maintainable and of high quality.

You must implement a system capable of handling some of the requirements.

It should have at least the following functionality:

- List orders from shops
- Create Order
- View order
- Pack order
- Create a User
- List Users and their orders

At least three classes must be tested and a unit test coverage report must be made and attached to the report. For the report discuss the coverage you have reached. Is the code tested sufficiently? Any spots that could require more unit testing?

You must provide the Cyclomatic Complexity of each method and class.

- Upload a video showing the code running with your commentary.

## Documenting the Architecture

With the classes implemented you must document your architecture. Some questions to ask yourself and document the answers to are:

- Is this a layered architecture? 1 layer? 2 layers? 3 layers?
- Looking at the article by Renzel, what distributions patterns have you used, if any?
- Does the architecture live up to the relevant [Agile Principles](https://agilemanifesto.org/principles.html) ?

## User Interface

For this you have two options, either:

- Implement a simple User Interface / Working Prototype and hook it up with your classes for at least one sequence / flow
- Create a High-Fidelity Prototype for the User Interface for at least two sequences / flows

For the one you select you must document the decisions behind your User Interface. It is not required to provide pixel-perfect User Interfaces but sketch out the idea behind it.

- Record a video showing your User Interface and how it works

## Integrating With The Suppliers

In the interview we learned that they would like to integrate with the suppliers **A** and **B**, rather sooner than later. They provide a REST API of Richardson Maturity level 2.

The process with the API from the suppliers is in short: Authenticate, fetch list of products, their IDs, and their stock levels. When you have validated that the suppliers have the items in stock, submit an order with their IDs.

**A** provides data as JSON. **B** provides data as XML.

You need to provide a design of how to structure the system and document the design choices. What assumptions have you made about their API?

Some things to help:

- How would you expect to call the different endpoints with the information given?
- What design patterns could be useful?
- Can interfaces help? If yes, why? If not, why not?
- What assumptions do you need to make
