# Duplicate File Removal Automation

# Project Description

This Python automation script periodically scans a directory, detects duplicate files using checksums, deletes duplicate copies, creates a detailed log file, and sends the log file via email.

# Features

- Recursive directory scanning
- Checksum-based duplicate detection
- Automatic duplicate file deletion
- Timestamp-based log generation
- Periodic execution
- Email notification
- Log-file attachment
- Input validation
- Exception handling
- Modular Programming

# Requirements

- Python 3.X
- sys
- os
- hashlib
- smtplib
- re
- time
- datetime
- email.message
- config
- schedule
- Internet connection for sending email
- Email application connection or SMTP credentials

# Project Files

- config.py

# Project Structure

```text
Python-Assignments/
│
├── Marvellous/               # Generated log files (ignored)
├── TestFiles/                # Local testing files (ignored)
├── .gitignore                # Git ignore rules
├── config_sample.py          # Sample email configuration
├── config.py                 # Local email configuration (ignored)
├── DuplicateFileRemoval.py   # Main automation script
└── README.md                 # Project documentation

```

# Commnad Line Options

Required arguments:

- Absolute Directory Path
- Time Interval (in minutes)
- Receiver Email Address

# Execution Command

```bash

python3 DuplicateFileRemoval.py <AbsoluteDirectoryPath> <TimeIntervalInMinutes> <ReceiverEmailAddress>

```

**Example:**

```bash
python3 DuplicateFileRemoval.py "C:\Users\Bhagyashri\TestFiles" 30 abc.test@gmail.com
```

# Help Command

```bash

python3 DuplicateFileRemoval.py --help

```

# Usage Command

```bash

python3 DuplicateFileRemoval.py --usage
```

# Log File Information

After each execution, the script automatically creates a log file inside the **_Marvellous_**/ directory.

The log file contains the following information:

- Name of scanned Directory
- Starting Time of Directory scanning
- Completion of Directory scanning
- Total number of files scanned
- Total number of duplicate files
- Total number of duplicate files deleted
- Checksums of duplicate files
- Errors encountered during execution (if any)
- Email delivery status

# Email Configuration

This project uses Gmail SMTP to send the log file as an email attachment after the duplicate file removal process is completed.

Create a file named **config.py** in the project root directory with the following content:

```python
sender_email = "your_email@gmail.com"
app_password = "your_16_character_app_password"
```

Replace:

- `your_email@gmail.com` with your Gmail address.
- `your_16_character_app_password` with your Gmail App Password.

**Note:** Do not upload `config.py` to GitHub because it contains your email credentials.

## Important Notes

- Deleted files may not be recoverable.
- Testing should first be performed on a sample directory.
- Email Passwords should not be hard-coded.
- The first file from each duplicate group should be preserved.
- File should be considered duplicates only when their checksums are identical

## Author

Bhagyashri Manoj Barde

## License

This project is developed for learning and educational purposes.
