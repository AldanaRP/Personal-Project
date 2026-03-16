# Project Roadmap

> Goal: Build a production-style backend using FastAPI + PostgreSQL  
> Focus: Architecture, clean code, authentication, and deployment readiness

---

# Phase 0 – Foundations (Environment & Tools)

## Environment Setup
- [x] Create virtual environment
- [x] Install Pip
- [x] Install FastAPI
- [x] Install Uvicorn
- [x] Install PostgreSQL

## Project Structure
- [X] Add README.md
- [X] Create clean folder structure
- [X] Separate main, models, schemas, database config
- [X] Configure .gitignore properly

---

# Phase 1 – Database Layer (Core Foundation)

## Database Connection
- [X] Configure SQLAlchemy
- [X] Connect FastAPI to PostgreSQL
- [ ] Create session dependency
- [ ] Test DB connection

## User Model
- [ ] Create tables in database
- [ ] Verify persistence

Milestone: ✔ I can store and retrieve users from DB

---

# Phase 2 – FastAPI Core Learning

## Basic Routing
- [ ] Create GET endpoint
- [ ] Create POST endpoint
- [ ] Use Pydantic schemas
- [ ] Understand request vs response models

## Dependency Injection
- [ ] Understand Depends()
- [ ] Inject DB session properly

Milestone: ✔ I understand how FastAPI handles requests and validation

---

# Phase 3 – User Registration

## Registration Endpoint
- [ ] Create POST /register
- [ ] Validate email format
- [ ] Hash password (bcrypt or passlib)
- [ ] Store user in DB
- [ ] Prevent duplicate emails

Milestone: ✔ Users can register securely

---

# Phase 4 – Authentication System

## Login
- [ ] Create POST /login
- [ ] Verify hashed password
- [ ] Return JWT token

## JWT Handling
- [ ] Configure secret key
- [ ] Add token expiration
- [ ] Create auth dependency

Milestone: ✔ Protected routes work

---

# Phase 5 – Authorization & Protected Routes

- [ ] Create protected endpoint
- [ ] Extract current user from token
- [ ] Handle invalid/expired tokens
- [ ] Add role-based logic (optional)

Milestone: ✔ Only authenticated users can access protected data

---

# Phase 6 – Clean Architecture Improvements

- [ ] Separate routers
- [ ] Separate services layer
- [ ] Improve error handling
- [ ] Standardize API responses
- [ ] Add logging

Milestone: ✔ Codebase looks production-ready

---

# Phase 7 – Testing

- [ ] Install pytest
- [ ] Test user registration
- [ ] Test login
- [ ] Test protected route
- [ ] Use test database

Milestone: ✔ Core functionality is tested

---

# Phase 8 – Production Thinking

- [ ] Environment variables (.env)
- [ ] Production config
- [ ] Dockerize app
- [ ] Prepare for deployment
- [ ] Write clean README documentation

Milestone: ✔ Backend is deployment-ready

---

# Phase 9 – Features (To Be Defined)
...

