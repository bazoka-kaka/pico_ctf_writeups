# SQL Direct

## Problem

Connect to this PostgreSQL server and find the flag!

Additional details will be available after launching your challenge instance.

## Solution

1. Install postgresql

```sh
sudo apt update -y
sudo apt install postgresql postgresql-contrib -y
sudo systemctl start postgresql.service
```

2. Connect to the server `psql -h saturn.picoctf.net -p 64396 -U postgres pico` the password is `postgres`

3. Inspect the db and find the flag using the following commands

```sql
\l # list all dbs
\c pico # select pico db
\dt # list all db tables
SELECT * FROM flags;
```

FLAG: `picoCTF{L3arN_S0m3_5qL_t0d4Y_31fd14c0}`