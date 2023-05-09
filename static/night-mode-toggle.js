const toggleSwitch = document.querySelector('#night-mode-toggle');
const body = document.querySelector('body');

function switchTheme(e) {
    if (e.target.checked) {
        body.classList.add('night-mode');
        localStorage.setItem('nightMode', 'enabled');
    } else {
        body.classList.remove('night-mode');
        localStorage.setItem('nightMode', null);
    }
}

toggleSwitch.addEventListener('change', switchTheme, false);

const currentTheme = localStorage.getItem('nightMode');
if (currentTheme === 'enabled') {
    toggleSwitch.checked = true;
    body.classList.add('night-mode');
} else {
    toggleSwitch.checked = false;
    body.classList.remove('night-mode');
}