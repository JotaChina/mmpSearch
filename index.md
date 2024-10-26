---
layout: default
title: Arquivos MMP
---

<div class="publication">
  {% include sidebar.html %}
    <main class="content">
    <div class="container">
      
      <h2>Arquivos MMP disponíveis:</h2>

      <div id="tags">
        <strong>Instrumentos:</strong>
        <ul id="instrument-tags">
          {% assign all_instruments = site.data.all_instruments %}
          {% for instrument in all_instruments %}
            <li class="tag" data-instrument="{{ instrument }}">{{ instrument }}</li>
          {% endfor %}
        </ul>
      </div>

      <div id="search">
        <label for="instrument-search">Buscar instrumento:</label>
        <input type="text" id="instrument-search" placeholder="Digite o nome do instrumento...">
        <button id="search-button">Buscar Projetos</button>
      </div>

      <div id="search-wav">
        <label for="file-wav-search">Buscar beat:</label>
        <input type="text" id="file-wav-search" placeholder="Buscar por nome do arquivo">
        <button id="search-wav-button">Buscar Beats</button>
      </div>

      <div id="search-both">
        <label for="instrument-wav-search">Buscar em Projetos e Beats:</label>
        <input type="text" id="instrument-wav-search" placeholder="Buscar por instrumento">
        <button id="search-both-button">Buscar Projetos e Beats</button>
      </div>

      <ul id="file-list-wav" style="display: none;">
        {% assign files = site.static_files %}
        {% for file in files %}
          {% if file.path contains '/mmp/wav/' %}
            <li class="file-wav-item">
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

      <ul id="file-list-mmp" style="display: none;">
        {% for files in site.data %}
          {% assign file_data = files %}
          {% for item in file_data %}
            {% if item.file %}
              <li class="file-item" data-file="{{ item.file }}">
                <strong>Arquivo:</strong> {{ item.file }}<br>
                {% if item.bpm %}
                  <strong>BPM:</strong> {{ item.bpm }}<br>
                {% endif %}
                <strong>Instrumentos:</strong>
                <ul class="instrument-list">
                  {% for track in item.tracks %}
                    {% for instrument in track.instruments %}
                      <li class="instrument-name" data-instrument="{{ instrument.instrument_name }}">{{ instrument.instrument_name }}</li>
                    {% endfor %}
                  {% endfor %}
                </ul>
              </li>
            {% endif %}
          {% endfor %}
        {% endfor %}
      </ul>
    </div>
</main>
