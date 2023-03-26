var translate = document.querySelector("#btn-translate");
var input_translate = document.querySelector("#input-translate")
var output_translate = document.querySelector("#output-translate")

// mock server
// var url = "https://lessonfourapi.tanaypratap.repl.co/translate/yoda.json"


// actual server
var url = "translate"

function urlfunc(url) {
    return url + "?" + "text=" + input_translate.value
}

function callback() {
    fetch(urlfunc(url), {
        method: 'GET',
        mode: 'cors',
      })
        .then(response => response.json())
        .then(json => {
            console.log("json: ", json)
            var output_text = json[0].translation;
            output_translate.innerText = output_text.trim(); // For some reason the response comes back with leading \n's
        }).catch(function errorhandler(error) {
    alert("Something wrong with the server. Please try again later.")
})
}

translate.addEventListener("click", callback)

const currentTheme = localStorage.getItem("theme");
if (currentTheme == "dark") {
    document.getElementById('toggleknop').innerHTML = '<i class="fas fa-sun" id="zon" style="color:#d8c658;"></i>';
  document.body.classList.add("dark-theme");
}

function changeTheme() {
    document.body.classList.toggle("dark-theme");
  
  document.getElementById('toggleknop').innerHTML = '<i class="fas fa-moon" id="maan" style="color:#737eac;"></i>';

  let theme = "light";
  if (document.body.classList.contains("dark-theme")) {
    document.getElementById('toggleknop').innerHTML = '<i class="fas fa-sun" id="zon" style="color:#d8c658;"></i>';
    theme = "dark";
  }
  localStorage.setItem("theme", theme);
}
