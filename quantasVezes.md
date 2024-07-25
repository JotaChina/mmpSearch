---
layout: default
title: Quantidade de repetições de instrumentos
permalink: /quantasVezesAparecemInstrumentos/
---

<h2>Quantidade de vezes que cada instrumento é utilizado:</h2>
<ul id="instrument-list">
{% for item in site.data.processed_data %}
    <li data-count="{{ item.count }}">{{ item.instrument_name }}: {{ item.count }}</li>
{% endfor %}
</ul>

<script>
// Apenas para deixar em ordem decrescente
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
