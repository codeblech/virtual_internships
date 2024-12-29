# Mentor Mentee Matchmaking

### Hosted At
https://malikk.pythonanywhere.com

### Architecture
Chose a monolithic approach with Django for:
- Built-in authentication
- Admin interface
- ORM for database management
- Template system (DTL)
- Form handling

### Authentication
###### Client-side validation (JavaScript):
- Immediate user feedback
- Reduced server load
- Improved UX
- Note: Can be bypassed, used only for UX

###### Server-side validation (Django):
- Primary security layer
- Password requirements enforcement
- CSRF protection
- Session management

### Database
Using SQLite because:
- Built into Python
- Simple setup
- Sufficient for MVP
- Can migrate to PostgreSQL later if needed

### Frontend
Vanilla stack:
- HTML/CSS/JavaScript
- No frameworks
- Django Template Language
- AJAX for dynamic updates
- Responsive design with CSS Grid/Flexbox

### Core Features
1. User Management:
   - Custom user model
   - Mentor/Mentee roles
   - Profile creation

2. Profile System:
   - Bio, skills, interests
   - JSON fields for flexible storage
   - Profile editing/viewing

3. Connection System:
   - Request/accept/reject flow
   - Many-to-many relationships
   - Status tracking

4. Search/Filter:
   - Role-based filtering
   - Skill matching
   - Real-time updates

### Development
- Fork and clone this repo
- With Poetry installed:
```shell
poetry shell
poetry install
python manage.py migrate
python manage.py runserver
```