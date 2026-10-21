// Conway Family Farms — small shared behaviors
(function () {
  // Footer year
  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();

  // Mobile nav toggle
  var btn = document.querySelector(".nav-toggle");
  var nav = document.getElementById("main-nav");
  if (btn && nav) {
    btn.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  // PREVIEW STATE: forms are not connected yet. The form action points at a
  // placeholder Formspree endpoint (see data-endpoint note in the HTML);
  // on submit we stop the send and show an honest notice instead of
  // pretending the message went anywhere.
  document.querySelectorAll("form[data-preview]").forEach(function (f) {
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var note = f.querySelector(".form-note");
      if (note) {
        note.classList.add("show");
        note.setAttribute("tabindex", "-1");
        note.focus();
      }
    });
  });
})();
