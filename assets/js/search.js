document.addEventListener("DOMContentLoaded", function() {
  var fileItemsMMP = document.querySelectorAll('#file-list-mmp .file-item');
  var fileItemsWAV = document.querySelectorAll('#file-list-wav li');

  // Buscar por instrumento usando o campo de entrada para MMP
  var searchButton = document.getElementById('search-button');
  searchButton.addEventListener('click', function() {
    var searchInput = document.getElementById('instrument-search').value.trim().toLowerCase();
    if (searchInput === '') {
      resetSearchMMP();
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

  // Buscar por nome do arquivo WAV
  var searchWavButton = document.getElementById('search-wav-button');
  searchWavButton.addEventListener('click', function() {
    var searchInput = document.getElementById('file-wav-search').value.trim().toLowerCase();
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

  // Função para resetar a busca para arquivos MMP
  function resetSearchMMP() {
    fileItemsMMP.forEach(function(item) {
      item.style.display = 'block';
    });
    document.getElementById('file-list-mmp').style.display = 'none';
  }

});
