### Запуск с Docker Compose

Перейдите в директорию, где находится docker-compose.yml, и запустите все сервисы:

```sh
docker-compose up
```

### Доступ к Grafana и Prometheus

    Grafana будет доступна по адресу http://localhost:3000.
    Prometheus будет доступен по адресу http://localhost:9090.

### Настройка Grafana

    Войдите в Grafana (по умолчанию логин/пароль: admin/admin).
    Добавьте Prometheus в качестве источника данных.
    Создайте дашборд для отображения метрики температуры.

После этого вы сможете наблюдать метрики температуры в Grafana, собираемые Prometheus с вашего Python приложения.