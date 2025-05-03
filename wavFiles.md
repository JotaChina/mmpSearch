---
layout: default
title: Beats Disponíveis
permalink: /beatsDisponiveis/
---

<main class="main-content">
  <div class="publication">
    {% include sidebar.html %}
    <div class="container">
      <br>
      <h2 class="title is-4 mb-5"><code>🎧 Lista de Beats 🎧</code></h2>
      <p>Aqui estão os beats disponíveis. 
      <br>Clique em um beat para ouvi-lo.</p>

      <!-- Lista de Beats -->
      <div class="beat-list">
        {% assign files = site.static_files %}
        {% for file in files %}
          {% if file.path contains '/wav/' %}
            <div class="beat-item box">
              {% assign project_url = "" %}
              
              <!-- Aqui, tentamos encontrar o projeto correspondente com base no nome do arquivo -->
              {% assign file_name_without_extension = file.name | remove: '.wav' %}
              {% for projeto in site.data.all %}
                {% if projeto.file == file_name_without_extension %}
                  {% assign project_url = "/mmp_pages/" 
                                    | append: projeto.file
                                    | downcase          
                                    | replace: ' ', '-' 
                                    | replace: ' ', '-' 
                                    | replace: 'ç', 'c' 
                                    | replace: 'ã', 'a' 
                                    | replace: 'á', 'a'
                                    | replace: 'â', 'a'
                                    | replace: 'é', 'e'
                                    | replace: 'ê', 'e'
                                    | replace: 'í', 'i' 
                                    | replace: 'ó', 'o' 
                                    | replace: 'ô', 'o'
                                    | replace: 'õ', 'o'
                                    | replace: 'ú', 'u' 
                                    | append: ".html" %}
                {% endif %}
              {% endfor %}

              <p class="beat-name">
                {% if project_url %}
                  <!-- Link para o projeto que originou o arquivo .wav -->
                  <a href="{{ project_url | relative_url }}" class="project-link">
                    <code>{{ file.name | replace: '.wav', '' }}</code>
                  </a>
                {% else %}
                  <!-- Se não encontrar um projeto relacionado, exibe o nome do arquivo -->
                  {{ file.name | replace: '.wav', '' }}
                {% endif %}
              </p>
              
              <audio class="audio-player" controls>
                <source src="{{ file.path | relative_url }}" type="audio/wav">
                Seu navegador não suporta o elemento de áudio.
              </audio>
            </div>
          {% endif %}
        {% endfor %}
      </div>
    </div>
  </div>
</main>

<style>
  .beat-list {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    margin-top: 2rem;
  }

  .beat-item {
    background-color: #f9f9f9;
    padding: 0.2rem;  /* Reduzido o padding para diminuir a altura */
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    width: 100%;
    max-width: 250px;
    text-align: center;
    max-height: 25px;  /* Define a altura máxima das divs */
    overflow: hidden;  /* Garante que conteúdo extra não sobrecarregue a div */
  }

  .beat-name {
    font-size: 0.9rem;  
    font-weight: bold;
    margin-bottom: 0.2rem;  
    text-overflow: ellipsis;  /* Adiciona '...' se o texto for muito grande */
    white-space: nowrap;  /* Garante que o texto não quebre e adicione '...' */
    overflow: hidden;  /* Garante que o nome do arquivo longo seja cortado com '...' */
  }

  .audio-player {
    width: 100%;
    margin-top: 0.5rem;
  }

  .project-link {
    text-decoration: none;
    color: #3273dc;
  }

  .project-link:hover {
    text-decoration: underline;
  }
</style>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    const audioPlayers = document.querySelectorAll('.audio-player');
    audioPlayers.forEach(audio => {
      audio.addEventListener('play', function() {
        audioPlayers.forEach(otherAudio => {
          if (otherAudio !== audio && !otherAudio.paused) {
            otherAudio.pause();
          }
        });
      });
    });
  });
</script>
