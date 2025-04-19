---
layout: default
title: Arquivos MMP
permalink: /mmp_pages/
---

<div class="publication">
  {% include sidebar.html %}
  <h2><strong>📁 Projetos disponíveis</strong></h2><br><br><br>
  <div class="container">
    
    <ul style="list-style: none; padding-left: 0;">
      {% assign mmp_pages = site.pages | where_exp: "page", "page.path contains 'mmp_pages/'" %}
      {% for page in mmp_pages %}
        {% if page.url != '/mmp_pages/' %} 
          <li style="margin-bottom: 0.8rem;">
            <a href="{{ page.url | relative_url }}" style="text-decoration: none; font-weight: 500;">
              🔗 {{ page.title | default: page.name | replace: '.html', '' }}
            </a>
          </li>
        {% endif %}
      {% endfor %}
    </ul>
  </div>
</div>
