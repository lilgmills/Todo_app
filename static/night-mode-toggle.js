const toggleSwitch = document.querySelector('#night-mode-toggle');
const body = document.querySelector('body');

function switchTheme(e) {
  if (e.target.checked) {
    body.classList.add('night-mode');
  } else {
    body.classList.remove('night-mode');
  }    
}

toggleSwitch.addEventListener('change', switchTheme, false);