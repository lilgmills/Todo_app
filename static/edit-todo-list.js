// Get references to the necessary elements
const todoListForm = document.getElementById("todoListForm");
const todoListName = document.querySelector("#todoListName");
const originalName = todoListName.textContent;
const todoListNameInput = document.createElement("input");
todoListNameInput.type = "text";
todoListNameInput.value = originalName;
todoListNameInput.id = "todoListNameInput";
todoListNameInput.autocomplete = "off";

// Function to handle editing the todo list name
function editTodoList() {
    let isUpdated = false;

    // Event listener for keydown events in the input field
    todoListNameInput.addEventListener("keydown", function (event) {
        // Check if the key pressed was the enter key
        if (event.keyCode === 13) {
            event.preventDefault();
            let newName = todoListNameInput.value;
            if (newName !== originalName) {
                // Send a POST request to update the todo list name
                let xhr = new XMLHttpRequest();
                xhr.open("POST", "/update_todo_list_name");
                xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
                xhr.send(JSON.stringify({ "new_name": newName }));
                xhr.onload = function () {
                    if (xhr.status === 200) {
                        todoListName.textContent = newName;
                        isUpdated = true;
                    } else {
                        todoListName.textContent = originalName;
                    }
                };
            } else {
                todoListName.textContent = originalName;
            }
            // Add the blur event listener when the input is updated
            todoListNameInput.addEventListener("blur", updateTodoListName);
        }
    });

    // Clear the todo list name and append the input field
    todoListName.textContent = "";
    todoListName.appendChild(todoListNameInput);
    todoListNameInput.focus();

    // Add the blur event listener when the input is created
    todoListNameInput.addEventListener("blur", function () {
        if (!isUpdated) {
            if (todoListNameInput.value === "") {
                todoListName.textContent = "Todo List";
            } else {
                todoListName.textContent = originalName;
            }
        }
        updateTodoListName();
    });
}

// Function to update the todo list name
function updateTodoListName() {
    let newName = todoListNameInput.value;
    if (newName !== originalName && newName !== "" && newName !== null) {
        // Send a POST request to update the todo list name
        let xhr = new XMLHttpRequest();
        xhr.open("POST", "/update_todo_list_name");
        xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        xhr.send(JSON.stringify({ "new_name": newName }));
        xhr.onload = function () {
            if (xhr.status === 200) {
                todoListName.textContent = newName;
            } else {
                todoListName.textContent = originalName;
            }
        };
    } else {
        todoListName.textContent = originalName;
    }
    // Remove the blur event listener after the input is updated
    todoListNameInput.removeEventListener("blur", updateTodoListName);
}

// Event listener for clicking on the todo list name header
let todoListNameHeader = document.querySelector("h1");
todoListNameHeader.addEventListener("click", editTodoList);

// Event listener for submitting the todo list form
todoListForm.addEventListener("submit", (event) => {
    event.preventDefault();
    let newName = document.getElementById("todoListNameInput").value;
    if (newName === "" || newName === null) {
        newName = "Todo List";
    }
    // Send a POST request to update the todo list in database
    fetch("/update_todo_list_name", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ "new_name": newName })
    }).then(() => {
        location.reload();
    });

});
