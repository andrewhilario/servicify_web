# Servicify

Servicify is a service platform.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
cd servicify_web
python -m venv env
source env/Scripts/activate
pip install -r requirements.txt
python manage.py migrate

```

### How to install Postgres for Windows 10

1. Download and install [Postgres 14.2](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads).
2. After installation, right click My Computer > Advanced System Settings > Environment Variable.
3. On System Variables section, select the variable 'Path' and click Edit.
4. Click New and paste the /bin folder directory of your Postgres installation. *Ex. C:\Program Files\PostgreSQL\14\bin*
5. Press Ok
6. To confirm the installation, open cmd or terminal and type:
```bash
psql -U postgres;
```
7. It will prompt you for password if you've done the steps correctly.
8. Enter 'postgres' as the password.
9. After successful login, type:
```bash
CREATE DATABASE servicify;
```

## Usage
*If you've already completed the steps above, you may run the server with: *
```python
python manage.py runserver
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)