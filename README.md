letsencrypt
=========

Request a SSL certificate from [Let's encrypt](https://letsencrypt.org/)

Requirements
------------

None

Role Variables
--------------

Default variables:

    letsencrypt_is_dev: false
    letsencrypt_domain_name: dummy.example.com

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

License
-------

MIT
