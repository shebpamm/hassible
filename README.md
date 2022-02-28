<div align="center">

# 📘 Hassible

Collection of Ansible playbooks to deploy your own smart home environment

[Getting started](#getting-started) •
[Requirements](#requirements) •
[Configuration](#configuration)

</div>

## Getting started

Hassible targets Ubuntu/Debian distros and deploys docker and [homestack](https://github.com/shebpamm/homestack).
It then configures and brings up the wanted containers defined in homestack.

### Smart Home applications that Hassible manages: 

- [Mosquitto](https://mosquitto.org)
- [NodeRed](https://nodered.org)
- [Zigbee2MQTT](https://www.zigbee2mqtt.io)
- [Zwavejs2MQTT](https://github.com/zwave-js/zwavejs2mqtt)
- [Home Assistant](https://www.home-assistant.io)

*Do note that for zigbee and zwave, you need to have a physical coordinator!*

### Additional benefits

- Hassible also installs [NGINX](https://www.nginx.com/) as a reverse proxy for you 
- Handles SSL Certs with Let's Encrypt!
- Capability to handle dynamic dns with duckdns

### Ansible Structure
The playbook `homestack.yml` executes all the roles.  
For convenience, each role also has it's own playbook if you want to execute only a specific role.

## Requirements

Hassible has been written for **Ansible 2.9** so make sure you have that installed, for example in a virtualenv.

If you plan to use the zigbee2mqtt or zwavejs2mqtt roles, make sure you own the corresponding physical USB adapters!

## Configuration

0. Install required roles from Ansible Galaxy: `ansible-galaxy install -r requirements.yml -p roles`

1. Start by editing the inventory file or pass your own inventory with the same group names.
   - Replace localhost with the host that you are targeting
   - Remove the host from groups you don't want

2. Remove/Comment out roles that you don't care for from `homestack.yml`

3. Set up a domain to point towards the host and ensure port 80 is open

4. Edit files in `group_vars`
   - Set install location in `group_vars/homestack`
   - Change all default passwords (if you're real savvy use a vault!)
   - Configure domains for all the services you want to reverse proxy in `group_vars/nginx_frontend`

5. Configure variables in group_vars as you see fit

6. Run the playbook!  
`ansible-playbook -i inventory homestack.yml`

<details>
<summary>Optional: set up Duck DNS</summary>
  <ul>
    <li>Log in to <a href="https://www.duckdns.org/">duckdns</a></li>
    <li>Create subdomain(s) and add them to group_vars/duckdns</li>
    <li>Copy token to group_vars/duckdns</li>
  </ul>
</details>







