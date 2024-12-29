## Development Approach

### Client Server vs Monolith
##### **Advantages of Client-Server**
- Decoupling of  the frontend and backend
- Scalability: We can later replace the frontend (e.g., switch from vanilla JS to React) without touching the backend.
- Cross-Platform: APIs can be consumed by multiple clients (web apps, mobile apps, etc.).
##### **Advantage of Monolith**
- Faster and simpler development
- Easier deployment
- No version management of APIs
- Simpler testing
- Django / Flask are build really for this architecture

Choosing Django because it is really made for building this kind of application. And since no frontend framework is required, we do not need a client server architecture.

### Jinja2 vs DTL
Django has built-in support for DTL and it is suited for our simple use case.

### SQLite vs PostgreSQL
Using SQLite is simpler and straightforward because there of built-in support in Python. We can later (if needed) switch to PostgreSQL easily with a few lines of code change. `pgloader` can help in those migrations. We can even use SQLite for development and PostgreSQL for production.

### Authentication

##### Client-side validation (JavaScript):
- Provides immediate feedback to users
- Reduces server load
- Improves user experience
- BUT can be bypassed by disabling JavaScript or using tools like Postman
##### Server-side validation (Django):
- Provides actual security
- Cannot be bypassed
- Ensures data integrity
- Is the last line of defense

##### Not in Django Auth
- Password strength checking
- Throttling of login attempts
- Authentication against third-parties (OAuth, for example)
- Object-level permissions

> https://www.youtube.com/watch?v=8ZtInClXe1Q
> Computerphile(Tom Scoot) -> a Video warning developers about saving passwords

## Key Challenges and Solutions

### 1. User Management
**Challenge**: Managing users, profiles, and connections
**Solution**:
- Used Django's built-in authentication.
- Implemented custom user model with additional fields.

### 2. Profile Data Structure
**Challenge**: Storing variable skills and interests
**Solution**:
- Used JSON fields for flexibility
- Implemented custom form handling
- Added data validation for JSON fields

### 3. Connection System
**Challenge**: Managing mentor-mentee relationships
**Solution**:
- Created a Connection model with status tracking
- Implemented state machine for connection status
- Added validation for preventing duplicate connections

### 4. Real-time Search and Filtering
**Challenge**: Responsive profile filtering without page reload
**Solution**:
- Implemented client-side filtering with JavaScript
- Used data attributes for efficient DOM querying
- Added debouncing for performance optimization