const form = document.getElementById('new-item-form');
const input = document.getElementById('new-item-input');

form.addEventListener('submit', (event) => {
  if (input.value.trim() === '') {
    event.preventDefault();
    alert('Please enter a non-empty item.');
  }
});
