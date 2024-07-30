---
layout: default
title: "Pesquisar Projetos e Arquivos"
permalink: /search/
---

<main class="main-content">
  <div class="container">
    <h1>Pesquisar Projetos e Arquivos</h1>
    <input type="text" id="search-input" placeholder="Digite o nome do instrumento">
    <button id="search-button">Pesquisar</button>
  </div>

  <div class="projects">
    <h2>Projetos</h2>
    <ul id="project-list">
      {% for files in site.data %}
        {% assign file_data = files %}
        {% for item in file_data %}
          {% if item.file %}
            <li class="project-item hidden" data-file="{{ item.file }}" data-instruments="{% for track in item.tracks %}{% for instrument in track.instruments %}{{ instrument.instrument_name }}{% if forloop.last == false %}, {% endif %}{% endfor %}{% if forloop.last == false %}, {% endif %}{% endfor %}">
              <strong class="project-title">{{ item.file }}</strong>
              <div class="project-details hidden">
                <br>
                {% if item.bpm %}
                  <strong>BPM:</strong> {{ item.bpm }}<br>
                {% endif %}
                <strong>Instrumentos:</strong>
                <ul class="instrument-list">
                  {% for track in item.tracks %}
                    {% for instrument in track.instruments %}
                      <li class="instrument-name">{{ instrument.instrument_name }}</li>
                    {% endfor %}
                  {% endfor %}
                </ul>
              </div>
            </li>
          {% endif %}
        {% endfor %}
      {% endfor %}
    </ul>
  </div>

  <div class="wavFiles">
    <h2>Arquivos .wav</h2>
    <ul id="wav-list">
      {% assign wav_files = site.static_files %}
      {% for file in wav_files %}
        {% if file.path contains '/mmp/wav/' %}
          {% assign wav_name = file.name %}
          <li class="wav-item hidden" data-file="{{ wav_name }}">
            <span>{{ file.name }}</span><br>
            <audio controls>
              <source src="{{ file.path | relative_url }}" type="audio/wav">
              Seu navegador não suporta o elemento de áudio.
            </audio>
          </li>
        {% endif %}
      {% endfor %}
    </ul>
  </div>
</main>

<style>
  .hidden { display: none; }
  .project-details {
    margin: 10px;
  }
  .project-title {
    cursor: pointer;
    display: block;
    font-weight: bold;
  }
  .wav-item {
    margin: 10px;
  }
</style>

<script>
  document.getElementById('search-button').addEventListener('click', function() {
  var query = document.getElementById('search-input').value;

  // Filtra projetos
  var projectItems = document.querySelectorAll('#project-list .project-item');
  var visibleProjectFiles = new Set(); // Usando um Set para evitar duplicatas

  projectItems.forEach(function(item) {
    var instruments = item.getAttribute('data-instruments');
    var projectFileName = item.getAttribute('data-file')
    if (instruments.includes(query)) {
      item.classList.remove('hidden');
      visibleProjectFiles.add(projectFileName); // Adiciona o nome do arquivo do projeto ao conjunto
    } else {
      item.classList.add('hidden');
    }
  });

  // Filtra arquivos .wav
  var wavItems = document.querySelectorAll('#wav-list .wav-item');
  wavItems.forEach(function(item) {
    var wavFileName = item.getAttribute('data-file');
    if (visibleProjectFiles.size == 0 || visibleProjectFiles.has(wavFileName)) {
      item.classList.remove('hidden');
    } else {
      item.classList.add('hidden');
    }
  });

  // Mostra as listas se houver itens visíveis
  var hasVisibleProjects = Array.from(projectItems).some(item => !item.classList.contains('hidden'));
  var hasVisibleWavFiles = Array.from(wavItems).some(item => !item.classList.contains('hidden'));

  document.getElementById('project-list').classList.toggle('hidden', !hasVisibleProjects);
  document.getElementById('wav-list').classList.toggle('hidden', !hasVisibleWavFiles);
});

// Expande ou colapsa detalhes do projeto ao clicar no título
document.querySelectorAll('#project-list .project-title').forEach(function(title) {
  title.addEventListener('click', function() {
    var details = this.nextElementSibling; // A próxima div que contém detalhes
    var fileName = this.parentElement.getAttribute('data-file');
    console.log('Projeto clicado:', fileName);

    // Toggle de visibilidade dos detalhes do projeto
    if (details.classList.contains('hidden')) {
      details.classList.remove('hidden');
      
      // Mostrar apenas o arquivo .wav correspondente
      document.querySelectorAll('#wav-list .wav-item').forEach(function(wavItem) {
        var wavItemFileName = wavItem.getAttribute('data-file');
  
        var parts = fileName.split('/');
        var auxName = parts.pop(); // ou parts[parts.length - 1]
        parts = auxName.split('.');
        wavName = parts[0] + '.wav';
        
        if (wavItemFileName == wavName) {
          console.log('Encontrou');
          wavItem.classList.remove('hidden');
        } else {
          wavItem.classList.add('hidden');
        }
      });
    } else {
      details.classList.add('hidden');
      
      // Esconder todos os arquivos .wav quando detalhes são ocultados
      document.querySelectorAll('#wav-list .wav-item').forEach(function(wavItem) {
        wavItem.classList.add('hidden');
      });
    }
  });
});

// Inicialmente, esconde todos os arquivos .wav
document.querySelectorAll('#wav-list .wav-item').forEach(function(item) {
  item.classList.add('hidden');
});


</script>
