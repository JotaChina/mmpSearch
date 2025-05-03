---
layout: default
title: Projetos com Instrumentos
permalink: /instruments/
---

<meta charset="utf-8">

<main class="main-content">  
  <div class="publication">
    {% include sidebar.html %}
  </div>

  <div class="container">
    <div class="columns is-mobile is-vcentered" style="margin-bottom: 2rem;">
      <!-- Título -->
      <div class="column is-auto">
        <h2 class="title is-4"><code>Projetos e seus instrumentos:</code></h2>
      </div>
      <!-- Botão Limpar Filtro -->
      <div class="column is-auto">
        <button id="clearFilterButton" class="button is-small is-light">
          Limpar filtro
        </button>
      </div>
    </div>

    <!-- Projetos -->
    <div id="project-list" class="columns is-multiline">
      {% for projeto in site.data.all %}
        <div class="column is-6 project-item" data-project-id="{{ projeto.file }}">
          <div class="box">
            <!-- Botão do projeto -->
            {% assign file_url = projeto.file | downcase 
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
                                  | replace: 'ú', 'u' %}

            <a href="../mmp_pages/{{ file_url }}.html" class="button is-link is-fullwidth">
              {{ projeto.file }}
            </a>

            <!-- Lista de Instrumentos clicáveis -->
            <div class="instruments">
              {% assign instruments_exibidos = "" %}
              {% for track in projeto.tracks %}
                {% if track.instruments %}
                  {% for instrument in track.instruments %}
                    {% unless instruments_exibidos contains instrument.instrument_name %}
                      {% capture instruments_exibidos %}{{ instruments_exibidos }},{{ instrument.instrument_name }}{% endcapture %}

                      <!-- Gerar link para o instrumento -->
                      {% assign instrument_slug = instrument.instrument_name %}
                      <a href="{{ '/instruments/?instrument=' | append: instrument_slug | encodeURIComponent | relative_url }}" class="button is-link instrument-button" style="margin: 0.5rem;">
                        {{ instrument.instrument_name }}
                      </a>

                    {% endunless %}
                  {% endfor %}
                {% endif %}
              {% endfor %}
            </div>
          </div>
        </div>
      {% endfor %}
    </div>
  </div>
</main>

<script>
  document.addEventListener("DOMContentLoaded", function() {
  const instrumentButtons = document.querySelectorAll('.instrument-button');
  const projectItems = document.querySelectorAll('.project-item');
  const urlParams = new URLSearchParams(window.location.search);
  let instrumentFilter = urlParams.get('instrument'); // Pega o parâmetro 'instrument' da URL, se houver

  // Decodificando o valor do instrumento para garantir que espaços e caracteres especiais sejam tratados
  if (instrumentFilter) {
    instrumentFilter = decodeURIComponent(instrumentFilter);
  }

  // Função para aplicar o filtro de instrumento
  function filterProjects() {
    projectItems.forEach(project => {
      const projectId = project.getAttribute('data-project-id');
      let projectContainsInstrument = false;

      // Verificar se algum instrumento do projeto corresponde ao filtro
      project.querySelectorAll('.instrument-button').forEach(button => {
        const instrumentSlug = button.getAttribute('href').split('=')[1]; // Pega o instrumento do link

        // Decodificando o slug do instrumento para comparar corretamente
        const decodedSlug = decodeURIComponent(instrumentSlug);

        // Se o projeto contém o instrumento desejado, exibe o projeto
        if (decodedSlug === instrumentFilter) {
          projectContainsInstrument = true;
        }
      });

      // Ocultar ou exibir o projeto com base no filtro
      if (instrumentFilter && !projectContainsInstrument) {
        project.style.display = 'none'; // Oculta o projeto
      } else {
        project.style.display = 'block'; // Exibe o projeto
      }
    });
  }

  filterProjects(); // Aplica o filtro de instrumentos assim que a página é carregada

  // Botão para limpar filtro
  const clearFilterButton = document.querySelector('#clearFilterButton');
  if (clearFilterButton) {
    clearFilterButton.addEventListener('click', function () {
      // Limpa o filtro e mostra todos os projetos
      projectItems.forEach(project => {
        project.style.display = 'block'; // Exibe todos os projetos
      });

      // Remove o parâmetro 'instrument' da URL
      const newUrl = new URL(window.location.href);
      newUrl.searchParams.delete('instrument');
      window.history.replaceState({}, '', newUrl);
    });
  }
});
</script>
