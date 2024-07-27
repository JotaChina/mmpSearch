---
layout: default
title: Instrumentos Similares
permalink: /quaisProjetos/
---

<h2>Arquivos que possuem instrumentos similares:</h2>
<ul>
{% for item in site.data.processed_data %}
    <li>{{ item.instrument_name }}:
        <ul>
        {% for file_name in item.files %}
            <li>{{ file_name }}</li>
        {% endfor %}
        </ul>
    </li>
{% endfor %}
</ul>
