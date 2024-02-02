document.addEventListener('DOMContentLoaded', (event) => {
  const addItem = document.querySelector('#add_item');
  const myList = document.querySelector('.my_list');

  addItem.addEventListener('click', () => {
    const newLi = document.createElement('li');
    newLi.textContent = 'Item';
    myList.appendChild(newLi);
  });
});
