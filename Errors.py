[
  {
    "seq": 1,
    "timestamp": "2026-06-12T15:19:55Z",
    "level": "INFO",
    "message": "Received order request from user user_123"
  },
  {
    "seq": 2,
    "timestamp": "2026-06-12T15:19:56Z",
    "level": "DEBUG",
    "message": "Attempting to apply discount code 'INVALID99'"
  },
  {
    "seq": 3,
    "timestamp": "2026-06-12T15:20:00Z",
    "level": "ERROR",
    "message": "TypeError: 'NoneType' object is not subscriptable",
    "stack_trace": [
      {
        "file": "services.py",
        "line": 12,
        "method": "process_order",
        "module": "services"
      },
      {
        "file": "main.py",
        "line": 14,
        "method": "create_order",
        "module": "main"
      }
    ]
  }
]

# ------------------------------------------------------------------

[
  {
    "seq": 1,
    "timestamp": "2026-06-12T15:30:00Z",
    "level": "INFO",
    "message": "Received order request from user user123"
  },
  {
    "seq": 2,
    "timestamp": "2026-06-12T15:30:01Z",
    "level": "ERROR",
    "message": "IndexError: list index out of range",
    "stack_trace": [
      {
        "file": "main.py",
        "line": 16,
        "method": "create_order",
        "module": "main"
      }
    ]
  }
]
