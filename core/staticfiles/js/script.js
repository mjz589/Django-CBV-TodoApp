document.getElementById('todo-form').addEventListener('submit', function(e) {
    e.preventDefault();
    var todoInput = document.getElementById('todo-input');
    var todoList = document.getElementById('todo-list');
  
    if (todoInput.value.trim() !== '') {
      var todoItem = document.createElement('li');
      var checkbox = document.createElement('input');
      checkbox.type = 'checkbox';
      var label = document.createElement('label');
      label.textContent = todoInput.value;
      todoItem.appendChild(checkbox);
      todoItem.appendChild(label);
      todoList.appendChild(todoItem);
      todoInput.value = '';
  
      checkbox.addEventListener('change', function() {
        if (this.checked) {
          label.style.textDecoration = 'line-through';
        } else {
          label.style.textDecoration = 'none';
        }
      });
    }
  });