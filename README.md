# Servicify

Servicify is a service platform. Made by Group 6 DICT 3-1 of PUP Institute of Technology.


## How to install Git for Windows 10

click [here](https://www.youtube.com/watch?v=4xqVv2lTo40) to watch.


## How to clone a repository in Visual Studio Code or Using CMD

### For Visual Code
click [here](https://www.youtube.com/watch?v=VNNChXqF390) to watch.

### For CMD
click [here](https://www.youtube.com/watch?v=q5JhB9yjh_g) to watch



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
- [x] Service Marketplace Template (You can check reference sa Work Offers Templates (https://imgur.com/a/730oAey))
- [x] Contact Us Page (https://imgur.com/a/PQOAiGM) undraw svg (https://imgur.com/a/M0lrEZ7) (Marc Abi)
- [x] About Us Page (https://imgur.com/a/bCww0gR) undraw svg (https://imgur.com/a/GvoH2KC) (Joshia)
- [x] Work Offer Details Template (https://imgur.com/a/Yee5niQ) (Drew)
- [x] Work Offer Biddings Template (Use Tables) (https://imgur.com/a/wjoMysa)
- [x] Create Service Template (https://imgur.com/a/frlOmJ7)
- [x] Serviceperson Profile (https://imgur.com/a/4TaTYlB)
- [x] Client Profile (https://imgur.com/a/ysW7OtE)
- [x] 404 Page (https://imgur.com/a/wOgJtl9)
- [x] Search Interface (https://imgur.com/a/DEYYeET)
- [x] Avatar Hover Menu
- [x] Combine `templates\includes\register.html` and `templates\includes\register-detail.html` to single page. (Para madali mag-handle ng form) *(Drew)*

### Figma Prototypes
- [x] Service View Page (equivalent of https://imgur.com/a/Yee5niQ for service)
- [x] List of Services Page
- [x] List of Work Offers Page
- [x] Create Service Type Form
- [x] Service request page (For serviceperson) *(Drew)*
- [x] Service request confirmation *(Drew)*
- [x] Work Offer page (with place bid button & bids of other users) *(Drew)*
- [x] Work Offer bid page (with bid details & accept or decline) *(Drew)*
- [x] Work Offer bid confirmation *(Drew)*
- [x] Client Profile page (Web) *(Drew)*
- [x] Search interface (with filters) *(Drew)*
- [x] 404 Page *(Drew)*

### Template Changes
- [x] Bidding Details Blank element (https://imgur.com/a/invM4Zt)
- [x] Register Phone Number and Address style (https://imgur.com/a/z7IlEMV)
- [x] Create Service Address style (same lang ng sa register yung layout) (https://imgur.com/a/D672zTT)
- [x] Service Detail Filter section styles (https://imgur.com/a/AtmdXPZ)
- [x] FIX: Review avatars streched when message is long (https://imgur.com/a/sUWf4VK)
- [x] 'CLOSED' tag for closed work offers (Similar to Created At but darker bg color) (https://imgur.com/a/OA7uUAf)
- [x] Winning Bid Card and Highest Bid Style (https://imgur.com/a/NYqO17S)
- [x] Center and increase size of Bidding is already closed. (https://imgur.com/a/XTGcft2)
- [x] Work Offer Bids (colors are just sample, use the original theme) (https://imgur.com/a/SRcKgek)
- [x] Work Offer Bid details (https://imgur.com/a/3iaUmJK)
- [x] Make Dashboard images fit to box (Not streched and not full)
- [x] Create Service Dropdown add style (https://imgur.com/a/K0ok0a7)
- [x] Create Service Success add style (https://imgur.com/a/Z0u4njy)
- [x] Add 'Browse More' on the end of slide (at the end of Work Offers and Services) (https://imgur.com/a/aE5YJzI)

### System
- [ ] Change default delete behaviour. (Instead of literal delete, add a deleted_at column.) *(Troy)*
- [ ] Chat/Messaging System
- [ ] Location Data
- [ ] SMS api
- [ ] Permissions (Work Offers, Biddings)
- [ ] Avatar/Image validation
- [ ] Client/Serviceperson switch
- [ ] Ratings System
- [x] Service System
- [x] Work Offer System
- [x] Bidding System
- [x] Service Creation
- [x] Work Offer Creation
- [x] Login and Registration
- [x] User, Service, WorkOffer, Bid, ActiveService, ServiceType model *(Troy)*
- [x] Postgres Setup *(Troy)*


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
