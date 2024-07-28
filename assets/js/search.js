document.addEventListener("DOMContentLoaded", function() {
  var fileItemsMMP = document.querySelectorAll('#file-list-mmp .file-item');
  var fileItemsWAV = document.querySelectorAll('#file-list-wav .file-wav-item');

  // Função para exibir apenas os arquivos WAV correspondentes aos instrumentos encontrados nos projetos MMP
  function showWAVFilesByInstrument(selectedInstrument) {
    fileItemsWAV.forEach(function(item) {
      var fileName = item.getAttribute('data-file').toLowerCase();
      if (fileName.includes(selectedInstrument)) {
        item.style.display = 'block';
      } else {
        item.style.display = 'none';
      }
    });
  }

  // Buscar por instrumento usando o campo de entrada para MMP
  var searchButton = document.getElementById('search-button');
  searchButton.addEventListener('click', function() {
    var searchInput = document.getElementById('instrument-search').value.trim().toLowerCase();
    if (searchInput === '') {
      resetSearch();
      return;
    }
    fileItemsMMP.forEach(function(item) {
      var instrumentsList = item.querySelectorAll('.instrument-list .instrument-name');
      var hasInstrument = false;
      instrumentsList.forEach(function(instrument) {
        var instrumentName = instrument.getAttribute('data-instrument').toLowerCase();
        if (instrumentName.includes(searchInput)) {
          hasInstrument = true;
        }
      });
      if (hasInstrument) {
        item.style.display = 'block';
      } else {
        item.style.display = 'none';
      }
    });
    // Exibir a lista de arquivos MMP após a busca
    document.getElementById('file-list-mmp').style.display = 'block';
  });

  // Buscar por nome de arquivo WAV usando o campo de entrada
  var searchWavButton = document.getElementById('search-wav-button');
  searchWavButton.addEventListener('click', function() {
    var searchInput = document.getElementById('file-wav-search').value.trim().toLowerCase();
    if (searchInput === '') {
      resetSearch();
      return;
    }
    fileItemsWAV.forEach(function(item) {
      var fileName = item.querySelector('span').textContent.toLowerCase();
      if (fileName.includes(searchInput)) {
        item.style.display = 'block';
      } else {
        item.style.display = 'none';
      }
    });
    // Exibir a lista de arquivos WAV após a busca
    document.getElementById('file-list-wav').style.display = 'block';
  });

  // Buscar por instrumento ou nome de arquivo WAV usando o campo de entrada combinado
  var searchBothButton = document.getElementById('search-both-button');
  searchBothButton.addEventListener('click', function() {
    var searchInput = document.getElementById('instrument-wav-search').value.trim().toLowerCase();
    if (searchInput === '') {
      resetSearch();
      return;
    }
    // Buscar em arquivos MMP por instrumento
    fileItemsMMP.forEach(function(item) {
      var instrumentsList = item.querySelectorAll('.instrument-list .instrument-name');
      var hasInstrument = false;
      instrumentsList.forEach(function(instrument) {
        var instrumentName = instrument.getAttribute('data-instrument').toLowerCase();
        if (instrumentName.includes(searchInput)) {
          hasInstrument = true;
          // Mostrar arquivo WAV correspondente ao instrumento
          showWAVFilesByInstrument(item.getAttribute('data-file'));
        }
      });
      if (hasInstrument) {
        item.style.display = 'block';
      } else {
        item.style.display = 'none';
      }
    });
    // Exibir as listas de arquivos após a busca
    document.getElementById('file-list-mmp').style.display = 'block';
    document.getElementById('file-list-wav').style.display = 'block';
  });

  // Função para resetar a busca
  function resetSearch() {
    fileItemsMMP.forEach(function(item) {
      item.style.display = 'block';
    });
    fileItemsWAV.forEach(function(item) {
      item.style.display = 'block';
    });
    document.getElementById('file-list-mmp').style.display = 'none';
    document.getElementById('file-list-wav').style.display = 'none';
  }

});

