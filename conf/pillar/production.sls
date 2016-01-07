#!yaml|gpg

environment: production

domain: radiant.rochapps.com

repo:
  url: git@github.com:victor-rocha/radiant.git
  branch: master

# Addtional public environment variables to set for the project
env:
  FOO: BAR

# Uncomment and update username/password to enable HTTP basic auth
# Password must be GPG encrypted.
# http_auth:
#   username: |-
#    -----BEGIN PGP MESSAGE-----
#    -----END PGP MESSAGE-----

# Private environment variables.
# Must be GPG encrypted.
secrets:
  "SECRET_KEY": EorYFrGzRAqxR45QjaBhKsxBPA2olAWRUZzdCrXAMu4SpJUp0COHIOELFwIsvbYw

# Private deploy key. Must be GPG encrypted.
github_deploy_key: |-
  -----BEGIN PGP MESSAGE-----
  Version: GnuPG v1.4.11 (GNU/Linux)

  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
  =n0A8
  -----END PGP MESSAGE-----


# Uncomment and update ssl_key and ssl_cert to enabled signed SSL/
# Must be GPG encrypted.
# {% if 'balancer' in grains['roles'] %}
# ssl_key: |-
#    -----BEGIN PGP MESSAGE-----
#    -----END PGP MESSAGE-----
#
# ssl_cert: |-
#    -----BEGIN PGP MESSAGE-----
#    -----END PGP MESSAGE-----
# {% endif %}
