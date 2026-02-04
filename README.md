⚠️ Project Status: Archived

This repository is no longer under active development.
It remains public as a portfolio reference for architecture,
service design, and DevOps-related decisions.

# Online Reservation – API

**Quick overview (scanner-friendly)**

Backend API for a service-oriented online reservation application.  
Part of a microservice-focused portfolio with an emphasis on clean architecture, clear interfaces, and practical backend development.

---

## Overview

This repository contains the **API component** of the portfolio project **Online Reservation**.

The API forms the backend foundation of the application and provides clearly defined interfaces for reservation-related business logic.  
The primary focus is on **structure**, **traceability**, and **extensibility**, not on rapid feature completeness.

The project is intentionally designed as a **work in progress** and evolves incrementally.

---

## Objective

The goal of this project is to develop a backend API that:

- reflects realistic requirements  
- is maintainable and clearly structured  
- has well-defined responsibilities  
- fits into a service-oriented architecture  
- serves as a foundation for future microservices  

The focus is on **clean API design** and **clear business logic**, not on UI or framework showcases.

---

## Architectural Concept

The API follows an **API-first approach** and is structured so that:

- routing, business logic, and persistence are clearly separated  
- data models and interfaces are explicitly defined  
- extensions (e.g. auth service, user service) can be implemented as separate services  

Additional domain-specific or technical services are implemented in **separate repositories** and integrated via well-defined interfaces.

---

## Technical Stack

- Python 3.11  
- FastAPI  
- Pydantic (request/response validation)  
- SQLAlchemy (persistence layer)  
- Docker (local development environment)  
- Git & GitHub  

---

## Project Status

🚧 **Work in Progress**

**Status: 07 January 2025**

The current state reflects the development progress as of the date above.  
Changes to architecture, structure, and implementation are explicitly expected during the ongoing development process.

Current focus:

- stable project and folder structure  
- clean separation of layers  
- understandable and traceable API endpoints  
- conscious documentation of architectural decisions  

Functional extensions are added incrementally.

---

## Portfolio Context

This project is part of my developer portfolio and demonstrates my transition from classic web application development towards **API- and service-oriented backend architecture**.

The goal is not perfection, but **realism**:  
decisions, trade-offs, and technical compromises are meant to remain visible and understandable.

