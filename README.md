"# ZiaMart" 

## Deploy Kong with PostgreSQL

### Step 1: Create a Docker network

```bash
docker network create kong-net
```

### Step 2: Start the PostgreSQL DB container

```bash
docker run -d --name kong-database --network=kong-net -p 5432:5432 -e "POSTGRES_USER=kong" -e "POSTGRES_DB=kong" -e "POSTGRES_PASSWORD=kong" postgres:latest
```

### Step 3: Run Kong migrations on the PostgreSQL DB

```bash
docker run --rm --network=kong-net -e "KONG_DATABASE=postgres" -e "KONG_PG_HOST=kong-database" -e "KONG_PG_PASSWORD=kong" kong:latest kong migrations bootstrap
```

### Step 4: Start the Kong container 

```bash
docker run -d --name kong --network=kong-net -e "KONG_DATABASE=postgres" -e "KONG_PG_HOST=kong-database" -e "KONG_PG_PASSWORD=kong" -e "KONG_PROXY_ACCESS_LOG=/dev/stdout" -e "KONG_ADMIN_ACCESS_LOG=/dev/stdout" -e "KONG_PROXY_ERROR_LOG=/dev/stderr" -e "KONG_ADMIN_ERROR_LOG=/dev/stderr" -e "KONG_ADMIN_LISTEN=0.0.0.0:8001, 0.0.0.0:8444 ssl" -p 8000:8000 -p 8001:8001 -p 8002:8002 -p 8443:8443 -p 8444:8444 kong:latest
```

### Verify Kong is running

http://localhost:8000/


This should return the Kong admin API response, indicating that the Kong container is up and running and connected to the PostgreSQL database.

### Open Kong UI in browser and verify Kong admin dashboard is up and running

http://localhost:8002/
