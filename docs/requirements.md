Functional Requirements:
- Users must be able to register and log in.
- Users must be able to create, update, and delete tasks.
- Users must be able to create and manage habits, including selecting specific days of the week for habit completion.
- Users must be able to start, pause, and stop focus sessions.
- The system must be able to notify users when a focus session has ended.
- The system shall record focus session duration and completion status.
- The system shall calculate and store productivity metrics
- The system shall provide a dashboard where users can visualize their productivity progress.
- The system shall display a calendar view showing habit completion history and streaks.
- The system shall provide structured data endpoints to support external business intelligence tools.

Non-functional requirements:
- The system shall implement secure authentication and authorization mechanisms.
- User passwords shall be securely hashed before storage.
- The system shall restrict access to user-specific data.
- The system shall respond to user requests without noticeable delay under normal usage.
- The system shall support at least 50 concurrent users (for initial scope).
- The backend shall be deployable on both Windows and Linux environments.
- The frontend shall be accessible through modern web browsers.
- All user activity data shall be persisted in a relational database (PostgreSQL).
- The system shall ensure data consistency during CRUD operations.
