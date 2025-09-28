Source from a local .env file
```bash
export $(cat .env | xargs) && envsubst < input.txt > output.txt
```
envsubst cannot work on .env if it has comments