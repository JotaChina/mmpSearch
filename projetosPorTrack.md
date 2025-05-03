---
layout: default
title: Projetos por tipo de track
permalink: /projetosPorTrack/
---
<meta charset="utf-8">
<main class="main-content">  
  <div class="publication">
    {% include sidebar.html %}

  <div class="container">
    <br>
    Arquivos que possuem instrumentos similares:
    <br><br>

    <a href="{{ '/instruments/' | relative_url }}" class="button is-link" style="margin-bottom: 1rem;">
      Ver Projetos por Instrumento
    </a>

    <br>
    Arquivos que possuem tracks similares:
    <br><br>

    {% assign tags_exibidas = "" %}
    {% for item in site.data.all %}
        {% for tag in item.tags.TAG %}
            {% unless tags_exibidas contains tag %}
            {% capture tags_exibidas %}{{ tags_exibidas }},{{ tag }}{% endcapture %}

            <a href="../{{ tag | downcase | replace: ' ', '-' }}" class="button is-link" style="margin-bottom: 1rem;">
                {{ tag }}
            </a>
            
            {% endunless %}
        {% endfor %}
    {% endfor %}
  </div>
  </div>
</main>
