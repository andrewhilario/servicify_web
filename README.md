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
CREATE DATABASE servicify; # To create the database needed.
```
10. You can now run the server. 

## Usage
*If you've already completed the steps above, you may run the server with:*
```python
python manage.py runserver
```

## TODO
Lists of tasks that need to be done. 

### Templates
- [ ] Combine `templates\includes\register.html` and `templates\includes\register-detail.html` to single page. (Para madali mag-handle ng form) *(Drew)*

### Figma Prototypes
- [x] Service request page (For serviceperson) *(Drew)*
- [x] Service request confirmation *(Drew)*
- [x] Work Offer page (with place bid button & bids of other users) *(Drew)*
- [x] Work Offer bid page (with bid details & accept or decline) *(Drew)*
- [x] Work Offer bid confirmation *(Drew)*
- [ ] Client Profile page (Web) *(Drew)*
- [ ] Serviceperson Profile *(Drew)*
- [ ] Search interface (with filters) *(Drew)*
- [ ] 404 Page *(Drew)*

### System
- [ ] Change default delete behaviour. (Instead of literal delete, add a deleted_at column.) *(Troy)*
- [x] User, Service, WorkOffer, Bid, ActiveService, ServiceType model *(Troy)*
- [x] Postgres Setup *(Troy)*

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
