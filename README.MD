# DM571 Software Engineering Project - Online Booking System

This repository contains the project report and related artifacts for the [DM571](https://odin.sdu.dk/sitecore/index.php?a=fagbesk&id=136536&lang=en&listid=) Software Engineering course project, done in colaboration with [@jonas-bork](https://github.com/jonas-bork), [@sofusl90](https://github.com/sofusl90) and [@Caerullean ](https://github.com/Caerullean). 

The project involved designing and documenting an online booking/scheduling system for volunteers at a fictional community cinema ("Local Cinema"), based on stakeholder interviews and course principles. Key implementation features include a **frontend built with [Django](https://www.djangoproject.com)** and a **custom Python in-memory data store** incorporating security measures like **bcrypt**.

**Please see the included [DM571_Project_report.pdf](assets/DM571_Project_report.pdf) report for full details** on requirements analysis, design choices, implementation, and testing.

> [!IMPORTANT]
> Please note that the git commit history might not fully reflect the individual contributions, as we pair programmed using the [VS Code Live Share extension](https://marketplace.visualstudio.com/items/?itemName=MS-vsliveshare.vsliveshare).


## Project Overview & Goal

Based on an interview with the "Chairman" of Local Cinema, the project aimed to replace manual/disparate shift scheduling methods with a cohesive, web-based system. The core goals included:

*   Allowing cinema members (technical staff, sales, cleaners, etc.) to view schedules and book/manage their shifts online.
*   Providing "Super" users (Supers) with tools to manage shifts, member eligibility, and scheduling defaults.
*   Ensuring accessibility and usability, particularly for potentially tech-illiterate volunteers.
*   Establishing a foundation for future features like integration with ticketing systems or third-party calendars.

**For full details on the requirements, please see the official assignment description:**

➡️ **[Project description](./assets/ProjectDescription.md)** ⬅️


## Project Structure (3 Parts)

The course project was divided into three main parts, each building upon the previous one:

### Part 1: Preparing our Process
*(Corresponds roughly to Sections 2, 3, 4 in the report)*

This initial phase focused on understanding the project requirements and planning the development process.

**Key Activities & Deliverables:**

*   **Stakeholder Analysis:** Identified and classified stakeholders (Members, Chairman, Visitors, Government) using the Salience Model. (See Report - Section 2.1 / Appendix A)
*   **User Analysis:** Defined user roles (End Users, Super Users, System Users), their needs, maintenance responsibilities, and system interactions. (See Report - Section 3 / Appendix B)
*   **Prioritized Product Backlog:** Created a backlog of functional and non-functional requirements (primarily as user stories) using Fibonacci estimation. (See Report - Section 4)
*   **Backlog Discussion:** Justified the structure, prioritization, and scoring methods used for the backlog. (See Report - Section 4.1)

### Part 2: Making our First Product Delivery
*(Corresponds roughly to Sections 5, 6, 7, 8, 10 in the report)*

This phase focused on designing the system architecture, specifying an API, implementing a core part of the system, and developing a user interface concept.

**Key Activities & Deliverables:**

*   **System Flows:** Modeled key user interactions (e.g., Member Books Shift, Super Creates User) using UML Sequence Diagrams. (See Report - Section 5.2)
*   **Domain Model:** Created a consolidated UML Class Diagram representing the core entities (Member, Super, Shift, Schedule, Show, etc.). (See Report - Section 5.1 / Appendix I)
*   **API Specification:** Designed and documented a Level 2 REST API (using OpenAPI/Swagger) for essential functionalities (fetching schedules, signing up for shifts, managing shifts) intended for potential third-party use. (See Report - Section 6 / Appendix C)
*   **Implementation:** Developed core classes (Member, Super, AutomaticScheduler) in Python (likely using the Django framework, based on report context). *Note: Data persistence was initially handled in memory for scope management.* (See Report - Section 7)
*   **Testing:** Implemented unit tests for key classes, generating coverage reports and calculating Cyclomatic Complexity. (See Report - Section 7.1 / Appendices D, E, F, G)
*   **Architecture Documentation:** Analyzed the chosen architecture (MVT/Layered), discussed distribution patterns, and evaluated adherence to Agile principles. Developed C4 model diagrams (Levels 1-3) for architectural visualization. (See Report - Section 8 / Appendix H)
*   **User Interface:** Created wireframes and a functional prototype (using HTML/CSS/JS with Django) demonstrating key user flows (like viewing the schedule). (See Report - Section 10 / Appendices J, K)
*   **(Conceptual) Supplier Integration Design:** Outlined a design approach for integrating with hypothetical external supplier APIs (A - JSON, B - XML) for restocking (though not implemented).

### Part 3: Extended Testing and Integration (Conceptual)

While the provided description focuses heavily on Parts 1 & 2, the formal requirements mentioned a third part involving extended testing and integration with third-party systems. Our work laid the groundwork for this through the API specification and initial implementation.

## View the Project Report

The complete analysis, design decisions, diagrams, specifications, and discussions are documented in the project report PDF.

➡️ **[View the DM571 Project Report](./assets/DM571_Project_report.pdf)** ⬅️



# Install Dependencies
Use python version 3.11, and then execute the below command:
```
pip install -r requirements.txt
```

# Logins 

To help with testing, we have implemented a `dummy_database.py` that includes some users:
- Sales user:
    - E-Mail: sales@gmail.com
    - Password: sales
- PR user:
    - E-Mail: pr@gmail.com
    - Password: pr
- Super user:
    - E-Mail: admin@gmail.com
    - Password: admin
    - Note that this user is a Super user and is not a part of any group themselves.

# How to make test
Make a file in the website/tests folder and it will be run by the tests.
You are allowed to make subdirectories and make test in them too, as long as you also add an __init__.py file in that directory. 

# Run Test
```
python manage.py test website
```

# Run specific test
```
python manage.py test website.tests.test_models
```

# To Generate coverage report run:
```
coverage run --source='.' manage.py test website
```

# To view the coverage report
```
coverage report
```

# For a more detailed HTML report, run:
```
coverage html
```
