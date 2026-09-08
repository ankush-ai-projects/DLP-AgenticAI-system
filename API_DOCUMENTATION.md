# API Documentation

## Base URL
```
http://localhost:8000
```

## Authentication

All protected endpoints require a JWT Bearer token in the Authorization header:

```
Authorization: Bearer <your-jwt-token>
```

## API Endpoints

### Health Check

#### GET /api/v1/health
Health check endpoint

**Response:**
```json
{
  "status": "healthy"
}
```

---

### Authentication

#### POST /api/v1/auth/register
Register a new user

**Request Body:**
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "secure_password",
  "full_name": "John Doe"
}
```

**Response (201):**
```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "full_name": "John Doe",
  "is_active": true,
  "role": "user"
}
```

#### POST /api/v1/auth/login
User login

**Request Parameters:**
- `username` (string): Username
- `password` (string): Password

**Response (200):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
```

---

### Users

#### GET /api/v1/users/
List all users (paginated)

**Query Parameters:**
- `skip` (int): Number of records to skip (default: 0)
- `limit` (int): Number of records to return (default: 100)

**Response (200):**
```json
[
  {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "full_name": "John Doe",
    "is_active": true,
    "role": "user",
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-01T00:00:00"
  }
]
```

#### GET /api/v1/users/{user_id}
Get user by ID

**Path Parameters:**
- `user_id` (int): User ID

**Response (200):**
```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "full_name": "John Doe",
  "is_active": true,
  "role": "user",
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-01T00:00:00"
}
```

---

### Scans

#### POST /api/v1/scans/upload
Upload and scan a file

**Request:**
- `file` (file): File to scan (multipart/form-data)

**Response (200):**
```json
{
  "id": 1,
  "user_id": 1,
  "filename": "document.pdf",
  "status": "completed",
  "findings": {
    "CREDIT_CARD": [
      {
        "match": "4532-1234-5678-9010",
        "position": 150,
        "severity": "CRITICAL"
      }
    ]
  },
  "risk_level": "HIGH",
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-01T00:00:00"
}
```

#### GET /api/v1/scans/{scan_id}
Get scan results

**Path Parameters:**
- `scan_id` (int): Scan ID

**Response (200):**
```json
{
  "id": 1,
  "user_id": 1,
  "filename": "document.pdf",
  "status": "completed",
  "findings": {
    "CREDIT_CARD": [
      {
        "match": "****-****-****-9010",
        "position": 150,
        "severity": "CRITICAL"
      }
    ]
  },
  "risk_level": "HIGH",
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-01T00:00:00"
}
```

---

## Error Responses

### 400 Bad Request
```json
{
  "detail": "Invalid request parameters"
}
```

### 401 Unauthorized
```json
{
  "detail": "Invalid authentication credentials"
}
```

### 404 Not Found
```json
{
  "detail": "Resource not found"
}
```

### 500 Internal Server Error
```json
{
  "detail": "Internal server error"
}
```

---

## Interactive API Documentation

FastAPI provides interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
