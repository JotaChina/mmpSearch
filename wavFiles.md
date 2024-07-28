---
layout: default
title: Beats Disponíveis
permalink: /beatsDisponiveis/
---

<main class="main-content">
  <div class="container">
    <h1>Lista de Beats</h1>
    <p>Aqui estão os beats disponíveis.</p>

    <ul>
      {% assign files = site.static_files %}
      {% for file in files %}
        {% if file.path contains '/mmp/wav/' %}
          <li>
            <span>{{ file.name }}</span><br>
            <audio controls>
              <source src="{{ file.path | relative_url }}" type="audio/wav">
              Seu navegador não suporta o elemento de áudio.
            </audio>
          </li>
          <br>
        {% endif %}
      {% endfor %}
    </ul>
  </div>
</main>

