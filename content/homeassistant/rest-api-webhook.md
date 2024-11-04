This is about integration to and from HASS regarding REST API and web framework related.

**Webhook**
https://www.home-assistant.io/docs/automation/trigger/#webhook-trigger
Create an automation and set the trigger to webhook.
The webhook will be a long randomized string for security
![](assets/Pasted%20image%2020241022205553.png)
If `Only Accessible from the local network` is selected, only the `ip:port` can be used. 
The webhook can accept both GET and POST requests.
```shell
curl -X POST -d 'key=value&key2=value2' https://192.168.0.1:8123/api/webhook/some_hook_id
```
- the address is located at `/api/webhook`

**Rest Commands (Action)** ^63dce3
https://www.home-assistant.io/integrations/rest_command/
To include restful commands in [configuration.yaml](configuration.yaml.md)
```yaml
rest_command: !include rest.yaml
```

```yaml
name_of_action::
  url: 'http://10.10.120.1:1378/api/StartAction'
  method: POST
  headers:
    content-type: 'application/json'
  payload: '{"key": "value", "array": [{"k": "v", "value": "{{ variable }}"}]}'
```
- `name_of_action` the action that will be displayed as `rest_command.name_of_action` 
- options for request types and header
- payload is the data that will be sent to the API
	- the content of the payload can be customized using `{{ variable }}`
To use custom variables in automation
```yaml
    - service: rest_command.name_of_action
      data: # additional options
        variable: value_that_replace_variable
	  data: {} # if no additional options defined
```
- the custom variable is defined under `data` block as key value pairs
