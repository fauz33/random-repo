firefox:
  pkg.installed:
    {% if grains['osfinger'] == 'Ubuntu-16.04' %}
    - version: 85
    {% elif grains['osfinger'] == 'Ubuntu-18.04' %}
    - version: 89
    {% endif %}