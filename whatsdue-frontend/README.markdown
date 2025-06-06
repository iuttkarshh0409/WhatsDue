# WhatsDue — WhatsApp-Based Assignment Reminder Agent 📲

**WhatsDue** is an intelligent, AI-powered reminder system that sends assignment deadline notifications via WhatsApp. Built as a minimalist productivity tool, it leverages a Python backend, MySQL database, and Twilio's WhatsApp API to automate reminders for upcoming tasks.

---

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Repository Structure](#repository-structure)
- [Tech Stack](#tech-stack)
- [Setup & Installation](#setup--installation)
- [Running Tests](#running-tests)
- [Sample Output](#sample-output)
- [Future Scope](#future-scope)
- [Author](#author)
- [License](#license)

---

## Features

- **Task Management**: Add and manage tasks with deadlines in a MySQL database.
- **Automated Reminders**: Detect tasks due within 24 hours and send WhatsApp notifications.
- **Twilio Integration**: Deliver reminders via Twilio's WhatsApp API.
- **Scheduled Execution**: Run autonomously using cron jobs on WSL/Linux.
- **Secure Configuration**: Store sensitive credentials securely in a `.env` file.

---

## How It Works

1. **Task Storage**: Tasks with titles, descriptions, and due datetimes are stored in a MySQL database.
2. **Reminder Check**: A Python script (`run_reminders.py`) queries tasks due within the next 24 hours.
3. **Notification Delivery**: If due tasks are found, reminders are sent via Twilio's WhatsApp API.
4. **Automation**: A cron job schedules the script to run periodically.

---

## Repository Structure

```
whatsdue/
│
├── whatsdue-backend/              # Backend source code and modules
│   ├── whatsapp_bot.py            # WhatsApp messaging logic
│   ├── run_reminders.py           # Core reminder script
│   ├── db_config.py               # Database configuration
│   ├── task_manager.py            # Task management logic
│   ├── .env.example               # Example environment file
│   └── requirements.txt           # Python dependencies
│
├── test-files/                    # Test scripts
│   ├── test_db_connection.py      # Database connection tests
│   ├── test_task_manager.py       # Task manager tests
│   └── ...
│
├── README.md                      # Project documentation
└── .gitignore                     # Git ignore file
```

---

## Tech Stack

| Technology       | Purpose                           |
|------------------|-----------------------------------|
| Python           | Core logic and automation         |
| MySQL            | Persistent task storage           |
| Twilio API       | WhatsApp message delivery         |
| Cron (WSL/Linux) | Scheduled task execution          |
| python-dotenv    | Environment variable management    |

---

## Setup & Installation

### Prerequisites
- Python 3.8+
- MySQL Server
- Twilio account with WhatsApp API access
- WSL/Linux (for cron job scheduling)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/iuttkarshh0409/whatsdue.git
   cd whatsdue
   ```

2. **Install Dependencies**
   ```bash
   pip install -r whatsdue-backend/requirements.txt
   ```

3. **Configure Environment Variables**
   Create a `.env` file in `whatsdue-backend/` based on `.env.example`:
   ```env
   DB_HOST=127.0.0.1
   DB_USER=your_mysql_user
   DB_PASS=your_mysql_password
   DB_NAME=whatsdue
   TWILIO_SID=your_twilio_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
   USER_WHATSAPP_NUMBER=whatsapp:+91XXXXXXXXXX
   ```

4. **Initialize the Database**
   Run the following SQL to create the `tasks` table:
   ```sql
   CREATE TABLE tasks (
       id INT AUTO_INCREMENT PRIMARY KEY,
       title VARCHAR(255) NOT NULL,
       description TEXT,
       due_datetime DATETIME NOT NULL,
       reminder_sent BOOLEAN DEFAULT FALSE
   );
   ```

5. **Add Sample Tasks**
   Insert sample data for testing:
   ```sql
   INSERT INTO tasks (title, description, due_datetime, reminder_sent) VALUES
   ('Math Assignment', 'Complete calculus problems', NOW() + INTERVAL 4 HOUR, FALSE),
   ('Java Project', 'Submit project report', NOW() + INTERVAL 12 HOUR, FALSE);
   ```

6. **Run the Reminder Script**
   From the `whatsdue-backend/` directory:
   ```bash
   python run_reminders.py
   ```

7. **Schedule Cron Job (Linux/WSL Only)**
   Edit the cron table:
   ```bash
   crontab -e
   ```
   Add the following to run the script every 15 minutes (adjust paths as needed):
   ```bash
   */15 * * * * /usr/bin/python3 /path/to/whatsdue-backend/run_reminders.py
   ```

---

## Running Tests

Execute test scripts from the root directory to verify functionality:
```bash
python test-files/test_db_connection.py
python test-files/test_task_manager.py
```

---

## Sample Output

**Console Output**:
```
✅ Connected to the MySQL database successfully!
✅ WhatsApp message sent. SID: SMxxxxxxxxxxxxxx
```

**WhatsApp Message**:
```
Reminder: Math Assignment is due by 2025-06-07 13:00.
Task: Complete calculus problems.
```

---

## Future Scope

- Multi-user support with authentication
- Web interface for task management and visualization
- NLP-based task input via WhatsApp
- Integration with Google Calendar or Outlook
- Customizable reminder intervals

---

## Author

**Utkarsh Dubey**  
Devi Ahilya Vishwavidyalaya, Indore  
GitHub: [@iuttkarshh0409](https://github.com/iuttkarshh0409)

---

## License

This project is licensed for **educational and personal use only**. Usage of the Twilio WhatsApp API must comply with the [WhatsApp Business Policy](https://www.whatsapp.com/legal/business-policy/). Ensure you review and adhere to Twilio's terms of service.