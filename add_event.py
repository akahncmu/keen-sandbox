import keen
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("credentials.txt")
print config
keen.project_id = config.get("credentials","project_id")
keen.write_key = config.get("credentials","write_key")

keen.add_event("first_experiement", {
  "hiding_creds": "yes"
})
