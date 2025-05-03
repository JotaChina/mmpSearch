---
layout: default
title: Arquivos MMP
permalink: /mmp_pages/
---

<div class="publication">
  {% include sidebar.html %}
  <div class="container">
    <h2 class="title is-4 mb-5"><code>📁 Projetos disponíveis</code></h2>

    <div class="columns is-multiline">
      {% assign mmp_pages = site.pages | where_exp: "page", "page.path contains 'mmp_pages/'" | sort: "title" %}
      {% for page in mmp_pages %}
        {% if page.url != '/mmp_pages/' %}
          <div class="column is-6-tablet is-4-desktop is-3-widescreen">
            <a href="{{ page.url | relative_url }}" style="text-decoration: none;">
              <div class="card hover-shadow" style="height: 100%;">
                <div class="card-content">
                  <p class="title is-6" style="word-break: break-word;">
                    {{ page.title | default: page.name | replace: '.html', '' }}
                  </p>
                </div>
              </div>
            </a>
          </div>
        {% endif %}
      {% endfor %}
    </div>
  </div>
</div>
