# ETL PROJECT

## Requirements
### Database Setup
#### Installation

1. **Install PostgreSQL**: Download and install PostgreSQL on your operating system.
2. **Configure PostgreSQL**: Follow the installation instructions to set up PostgreSQL on your system. Ensure that the necessary configuration parameters are appropriately set based on the system requirements.

#### Database Creation

We're going to create the database with a script inside the project. You need to guarantee that the project runs.

#### Database Configuration
1. **Authentication**: Configure authentication methods (e.g., password authentication, certificate-based authentication) in pg_hba.conf to control access to the database. Ensure that the user is set to postgres and the password is set to postgres.
2. **Connection Pooling**: Consider implementing connection pooling using tools like PgBouncer to optimize resource utilization and improve performance.
3. **Logging**: Configure logging parameters in postgresql.conf to monitor database activity, errors, and performance metrics effectively. Ensure that the host is set to localhost and the port is set to 5432.
4. **Backup and Recovery**: Set up regular backups using tools like pg_dump or continuous archiving with Point-in-Time Recovery (PITR) to ensure data integrity and disaster recovery.

### Environment Setup

This project requires Python 3.x and several third-party libraries which interact with databases, handle data manipulation, and manage HTTP requests. Below are the instructions to set up your environment and install the necessary dependencies.

#### Prerequisites
Python 3.x installed on your system. You can download it from Python.org.

#### Dependencies
The script uses several external libraries which can be installed using Python's package manager, pip. Run the following commands in your terminal to install them:

```
# Install pandas for data manipulation
pip install pandas

# Install SQLAlchemy for database interactions
pip install sqlalchemy

# Install psycopg2-binary for PostgreSQL database connectivity
pip install psycopg2-binary

# Install requests for HTTP requests
pip install requests

```

#### Modules from the Python Standard Library

The script also utilizes modules from the Python Standard Library, which are included in your Python installation and do not require separate installation:

1. **os**: Provides a portable way of using operating system dependent functionality.
2. **zipfile**: Allows extraction of ZIP files.
3. **shutil**: Offers a number of high-level operations on files and collections of files.
