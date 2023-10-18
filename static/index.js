document.querySelectorAll('a[data-artist]').forEach(function(link) {
    link.addEventListener('click', function(event) {
      event.preventDefault();
      const artist = link.getAttribute('data-artist');
      const song = link.textContent.trim();
      // Redirect to lyrics page with artist and song parameters
      window.location.href = '/get_lyrics?artist=' + artist + '&title=' + song;
    });
  });