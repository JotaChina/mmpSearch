---
layout: default
title: Arquivos MMP Processados
---

<h2>Arquivos MMP disponíveis:</h2>

<ul>
{% for files in site.data %}      
    {% assign file_data = files %}
    {% for item in file_data %}
        {% if item.file %}
            <li>File path: <strong>{{ item.file }}</strong></li>
        {% endif %}
        {% if item.bpm %}
            <li>BPM: {{ item.bpm }}</li>
        {% endif %}
        <ul>
        {% for track in item.tracks %}
            <li>{{ track.track_name }} ({{ track.type }})</li>
            <ul>
            {% for instrument in track.instruments %}
                <li>{{ instrument.instrument_name }}</li>
            {% endfor %}
            </ul>
        {% endfor %}
        </ul>
    {% endfor %}
{% endfor %}
</ul>
