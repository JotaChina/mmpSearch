---
layout: default
title: Quantidade de Repetições de Instrumentos
permalink: /quantasVezesAparecemInstrumentos/
---

<main class="main-content">
  <div class="container">
    <h2>Quantidade de vezes que cada instrumento é utilizado:</h2>
    <ul id="instrument-list">
      {% for item in site.data.processed_data %}
        <li data-count="{{ item.count }}">{{ item.instrument_name }}: {{ item.count }}</li>
      {% endfor %}
    </ul>
  </div>
</main>

<script>
  // Ordenação dos itens em ordem decrescente por contagem
  document.addEventListener("DOMContentLoaded", function() {
    var instrumentList = document.getElementById('instrument-list');
    var items = Array.from(instrumentList.children);

    items.sort(function(a, b) {
      var countA = parseInt(a.getAttribute('data-count'));
      var countB = parseInt(b.getAttribute('data-count'));
      return countB - countA; // Ordenação decrescente
    });

    instrumentList.innerHTML = '';
    items.forEach(function(item) {
      instrumentList.appendChild(item);
    });
  });
</script>

