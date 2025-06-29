# ASV ACCLAIM Assignment - Customer Support Chatbot (Team Avengers)

<!-- TOC -->
* [ASV ACCLAIM Assignment - Customer Support Chatbot (Team Avengers)](#asv-acclaim-assignment---customer-support-chatbot-team-avengers)
  * [Why Wong AI?](#why-wong-ai)
  * [Team Members](#team-members)
  * [Objectives](#objectives)
  * [Features](#features)
  * [Technologies Used](#technologies-used)
  * [Next Steps (Production Readiness):](#next-steps-production-readiness)
    * [Deployment Options](#deployment-options)
    * [LLM/OpenAI](#llmopenai)
  * [Appendix](#appendix)
    * [Known limitations in the current prototype](#known-limitations-in-the-current-prototype)
<!-- TOC -->

This chatbot is designed to assist customers with their queries. A knowledge base containing common customer queries for a fictitious telecom company is considered as a basis for RAG.

We named the AI Assistant as **Wong AI**
## Why Wong AI?
Our team's name is **Avengers**, and **Wong AI** is a reference to the character **Wong** (part of the **Avengers team of superheroes**) from the **Marvel Cinematic Universe**, 
who is known for his wisdom and ability to assist others. The name reflects our goal of creating an AI assistant 
that is helpful, knowledgeable, and reliable. 😊

| Wong                      | The Wong AI                  |
|---------------------------|------------------------------|
| ![image](public/wong.png) | ![image](public/wong_ai.png) |
 |



## Team Members

| # | Emp. Id | Name                | Email                          | Role                                      |
|---|---------|---------------------|--------------------------------|-------------------------------------------|
| 1 | 36384   | **Dinesh Velhal**   | dv0036384@techmahindra.com     | Tech Lead, Design, Development            |
| 2 | 746756  | **Rajnish Kumar**   | rk00746756@techmahindra.com    | Product / Requirements / Data Preparation |
| 3 | 306885  | **Sonali Shaha**    | sonali.shaha@techmahindra.com  | Support                                   |


## Objectives
- To provide a user-friendly interface for customers to get assistance with their queries.
- To ensure quick and accurate responses to customer inquiries.
- To create guardrails for responses from the knowledge base only
- To maintain a professional and helpful tone in all interactions.
- To create a prototype that can be further developed into a full-fledged application.

## Features
- **User-Friendly Interface**: The chatbot is designed to be easy to use, allowing customers to quickly find the information they need.
- **Quick Responses**: The chatbot is capable of providing instant responses to customer queries, reducing wait times.
- **Knowledge Base Integration**: The chatbot is integrated with a knowledge base to provide accurate and relevant information.
- **User Experience** - Customizable UI (Dark & Light mode), SShortcuts for frequently asked questions

## Technologies Used
- `Python`: The primary programming language used for developing the chatbot.
- `Chainlit`: A framework for building chatbots and other conversational applications.
- `OpenAI`: Used for natural language processing and understanding.
- `Pandas`: For data manipulation and analysis.
- `JSON`: For data interchange and storage.
- `ChromaDB`: A vector database for storing and retrieving knowledge base information.

## Next Steps (Production Readiness):
### Deployment Options
Chainlit allows multiple deployment options, including:
- Deploy as a **web app**
- Deploy as a **Slack app**
- Deploy as a **MS Teams app**
- Deploy as a **Discord app**
- Deploy as a **React app** for integrating with existing web applications
- Deploy as a **Copilot** (As a sidebar in existing applications)
More details can be found in the [Chainlit documentation](https://docs.chainlit.io/deploy/overview)

In addition, a deployment pipeline with continuous testing must be built (covering unit tests, integration tests, end-to-end tests, security tests, and performance tests) to ensure the chatbot is production-ready.

### LLM/OpenAI
- Build content filtering for bias, toxicity, abusive language, and other harmful content.
- Build guardrails for Copyright compliance and data privacy.


## Appendix
### Known limitations in the current prototype
- No audit trail of user interactions.
- No user authentication or authorization.
- Limited error handling and logging.
- The chatbot is currently limited to a single knowledge base and does not support multiple knowledge bases.
- Support queries requiring complex reasoning or multi-turn conversations may not be handled effectively.
- RAG is based on in-memory ChromaDB collection, which means for every new user session, the knowledge base needs to be reloaded, 
which can lead to increased response times for the first query. (This can be mitigated by using a persistent ChromaDB collection, which can be set up in production environments.)
- The chatbot does not currently support voice input or output.
- The chatbot does not have a fallback mechanism for queries that cannot be answered by the knowledge base.
- The chatbot does not currently support multi-language queries or responses.
- The chatbot does not have a mechanism for handling user feedback or ratings.
