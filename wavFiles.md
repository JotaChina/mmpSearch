---
layout: default
title: Músicas
permalink: /beatsDisponiveis/
---

<h1>Lista de Beats</h1>

Aqui estão os beats disponíveis.

<ul>
{% assign files = site.static_files %}
{% for file in files %}
  {% if file.path contains '/mmp/wav/' %}
    <li>
      <span> {{ file.name }} </span>
	<br>
	<audio controls>
	<source src="{{ file.path | relative_url }}"
	type="audio/wav">
	Seu navegador não suporta o elemento de áudio.
        </audio>
    </li>	
    <br>
   {% endif %}
{% endfor %}
</ul>
