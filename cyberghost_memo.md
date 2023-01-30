# VPN Cyberghost

## connect (default oppenvpn)

```sh
# US
sudo cyberghostvpn --traffic --country-code US –-connect
# Germany
sudo cyberghostvpn --traffic --country-code DE –-connect
# Romania
sudo cyberghostvpn --traffic --country-code RO –-connect
```

## List country codes

```sh
cyberghostvpn --traffic --country-code
```

## List by city

```sh
sudo cyberghostvpn --traffic --country-code US
```

## Torrent

```sh
# list
cyberghostvpn --torrent --country-code

# Connect (Poland)
sudo cyberghostvpn --torrent --country-code PL --connect
```

## Status

```sh
cyberghostvpn --status
```

## Disconnect

```sh
sudo cyberghostvpn --stop
```
