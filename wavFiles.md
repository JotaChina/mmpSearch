---
layout: default
title: Músicas
permalink: /musicas/
---

# Músicas

Aqui estão as músicas exportadas:

{% for music in site.static_files %}
  {% if music.path contains 'mmp/wav' %}
    <div>
      <h2>{{ music.name }}</h2>
      <audio controls>
        <source src="{{ music.path | relative_url }}" type="audio/wav">
        Your browser does not support the audio element.
      </audio>
    </div>
  {% endif %}
{% endfor %}
