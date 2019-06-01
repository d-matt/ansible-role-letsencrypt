letsencrypt
=========

Request a SSL certificate from [Let's encrypt](https://letsencrypt.org/)

This role detects if a web server is already running (*e.g* nginx) and if so
uses the webroot method (you have to define then the
`letsencrypt_webroot_path` var). If not, it uses the standalone method. 

This role can also forge self signed certificates, that can be usefull in dev
environment without internet access (`letsencrypt_is_dev: true`). 

Requirements
------------

None

Role Variables
--------------

Default variables:

    letsencrypt_is_dev: false
    letsencrypt_domain_name: dummy.example.com
    letsencrypt_webroot_path: /var/www/html
    letsencrypt_version: v0.34.2
    letsencrypt_email: changeme@somewhere.com

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - role: letsencrypt
           letsencrypt_domain_name: "mysite.example.com"
           letsencrypt_email: "me@awsome.org"

License
-------

MIT
