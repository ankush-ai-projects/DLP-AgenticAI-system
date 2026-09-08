# FastAPI Data Loss Prevention (DLP) System

A comprehensive FastAPI-based Data Loss Prevention system designed to detect, analyze, and prevent unauthorized data exfiltration.

## Project Structure

```
fastapi_project/
│
├── app/
│   ├── api/                  # Route layer (controllers)
│   │   ├── v1/
│   │   │   ├── endpoints/
│   │   │   │   ├── auth.py              # Authentication endpoints
│   │   │   │   ├── user.py              # User management endpoints
│   │   │   │   ├── scan.py              # DLP scanning endpoints
│   │   │   │   └── health.py            # Health check endpoint
│   │   │   └── api_router.py            # API router aggregation
│   │
│   ├── core/                 # Core configs & settings
│   │   ├── config.py         # Environment configuration
│   │   ├── security.py       # JWT, hashing utilities
│   │   ├── logging.py        # Logging setup
│   │   └── constants.py      # Application constants
│   │
│   ├── models/               # SQLAlchemy database models
│   │   ├── user.py           # User model
│   │   ├── scan.py           # Scan model
│   │   └── base.py           # Base model
│   │
│   ├── schemas/              # Pydantic validation schemas
│   │   ├── user.py           # User schemas
│   │   ├── scan.py           # Scan schemas
│   │   └── common.py         # Common schemas
│   │
│   ├── services/             # Business logic layer
│   │   ├── user_service.py   # User business logic
│   │   ├── scan_service.py   # Scan business logic
│   │   └── risk_engine.py    # DLP pattern detection
│   │
│   ├── repositories/         # Database abstraction layer
│   │   ├── user_repo.py      # User database operations
│   │   └── scan_repo.py      # Scan database operations
│   │
│   ├── workers/              # Background tasks (Celery)
│   │   ├── celery_app.py     # Celery configuration
│   │   └── tasks.py          # Background job tasks
│   │
│   ├── db/                   # Database connection
│   │   ├── session.py        # Session management
│   │   └── base.py           # Model imports
│   │
│   ├── utils/                # Utility functions
│   │   ├── file_parser.py    # File parsing utilities
│   │   ├── regex_detector.py # Pattern detection
│   │   └── masking.py        # Data masking utilities
│   │
│   ├── middleware/           # HTTP middleware
│   │   ├── auth_middleware.py    # Authentication middleware
│   │   └── logging_middleware.py # Request/response logging
│   │
│   └── main.py               # FastAPI application entry point
│
├── tests/                    # Unit & integration tests
│   ├── conftest.py          # Pytest configuration
│   └── test_*.py            # Test files
│
├── alembic/                  # Database migrations
│   └── versions/            # Migration scripts
│
├── docker/
│   ├── Dockerfile           # Docker image
│   └── docker-compose.yml   # Multi-container setup
│
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## Features

### Authentication & Security
- JWT-based authentication
- Password hashing with bcrypt
- Role-based access control (RBAC)
- Token expiration and refresh

### DLP Scanning
- Multi-format file scanning (PDF, DOCX, CSV, TXT)
- Pattern detection for:
  - Credit card numbers
  - Social Security Numbers (SSN)
  - Email addresses
  - Phone numbers
- Risk assessment engine
- Custom regex pattern support

### Database
- SQLAlchemy ORM
- Multiple database support (SQLite, PostgreSQL)
- Alembic migrations
- User and Scan models

### Background Processing
- Celery task queue
- Redis cache
- Asynchronous file processing

### API Features
- RESTful endpoints
- Comprehensive API documentation (Swagger UI)
- CORS support
- Request/response logging
- Health checks

## Installation

### Prerequisites
- Python 3.11+
- PostgreSQL (optional, SQLite default)
- Redis (for Celery, optional)

### Local Setup

1. Clone the repository:
```bash
cd fastapi_project
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment:
```bash
cp .env.example .env
# Edit .env with your settings
```

5. Initialize database:
```bash
python -m alembic upgrade head
```

6. Run application:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Docker Setup

1. Build and run with Docker Compose:
```bash
docker-compose -f docker/docker-compose.yml up --build
```

2. Access services:
- API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- PostgreSQL: localhost:5432
- Redis: localhost:6379

## API Endpoints

### Authentication
- `POST /api/v1/auth/login` - User login
- `POST /api/v1/auth/register` - User registration

### Users
- `GET /api/v1/users/` - List all users
- `GET /api/v1/users/{user_id}` - Get user by ID

### Scanning
- `POST /api/v1/scans/upload` - Upload and scan file
- `GET /api/v1/scans/{scan_id}` - Get scan results

### Health
- `GET /api/v1/health` - Health check

## Configuration

### Environment Variables

```env
# API
API_TITLE=DLP System API
DEBUG=False

# Database
DATABASE_URL=sqlite:///./dlp.db

# Security
SECRET_KEY=your-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Celery
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
```

## Development

### Run Tests
```bash
pytest
```

### Run with auto-reload
```bash
uvicorn app.main:app --reload
```

### Generate Database Migrations
```bash
alembic revision --autogenerate -m "Migration message"
alembic upgrade head
```

### Run Celery Worker
```bash
celery -A app.workers.celery_app worker --loglevel=info
```

## Architecture

### Layered Architecture
1. **API Layer**: FastAPI endpoints and routing
2. **Service Layer**: Business logic and orchestration
3. **Repository Layer**: Database abstraction
4. **Model Layer**: ORM entities
5. **Schema Layer**: Pydantic validation

### Design Patterns
- Repository Pattern: Data access abstraction
- Service Pattern: Business logic separation
- Middleware Pattern: Cross-cutting concerns
- Factory Pattern: Dependency injection

## Security Considerations

1. **Change SECRET_KEY in production**
2. **Use PostgreSQL in production** (not SQLite)
3. **Enable HTTPS** for all endpoints
4. **Implement rate limiting**
5. **Validate and sanitize all inputs**
6. **Use environment variables** for sensitive data
7. **Regular security audits** of DLP patterns

## Performance Optimization

- Database connection pooling
- Redis caching
- Asynchronous file processing with Celery
- Pagination for list endpoints
- Request logging and monitoring

## Monitoring & Logging

- Structured logging with timestamps
- Request/response logging middleware
- Application health checks
- Error tracking and alerting

## Contributing

1. Create a feature branch
2. Make changes and write tests
3. Submit a pull request

## License

MIT License

## Support

For issues and questions, please create an issue in the repository.
