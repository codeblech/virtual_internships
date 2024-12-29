### Authentication
Computerphile(Tom Scoot) -> https://www.youtube.com/watch?v=8ZtInClXe1Q
###### Client-side validation (JavaScript):
- Provides immediate feedback to users
- Reduces server load
- Improves user experience
- BUT can be bypassed by disabling JavaScript or using tools like Postman
###### Server-side validation (Django):
- Provides actual security
- Cannot be bypassed
- Ensures data integrity
- Is the last line of defense

##### Not in Django Auth
- Password strength checking
- Throttling of login attempts
- Authentication against third-parties (OAuth, for example)
- Object-level permissions

### FastAPI Template
https://github.com/tiangolo/full-stack-fastapi-template
Not using it because it has too much of what we don't need.

### Client Server vs Monolith
##### **Advantages of Client-Server
- Decoupling of  the frontend and backend
- Scalability: We can later replace the frontend (e.g., switch from vanilla JS to React) without touching the backend.
- Cross-Platform: APIs can be consumed by multiple clients (web apps, mobile apps, etc.).
##### **Advantage of Monolith**
- Faster and simpler development
- Easier deployment
- No version management of APIs
- Simpler testing
- Django / Flask are build really for this architecture
### Web Framework
Choosing Django because it has build in auth and admin panel.

### Jinja2 vs DTL
Django has built-in support for DTL and it is suited for our simple use case.

### SQLite vs PostgreSQL
Using SQLite is simpler and straightforward because there of built-in support in Python. We can later (if needed) switch to PostgreSQL easily with a few lines of code change. `pgloader` can help in those migrations. We can even use SQLite for development and PostgreSQL for production.
