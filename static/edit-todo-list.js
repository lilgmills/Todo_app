const todoListForm = document.getElementById("todoListForm");

function editTodoList() {
    let todoListName = document.querySelector("#todoListName");
    let originalName = todoListName.textContent;
    let input = document.createElement("input");
    input.type = "text";
    input.value = originalName;
    input.id = "todoListNameInput"

    // Remove the blur event listener when the input is created
    input.removeEventListener("blur", updateTodoListName);

    input.addEventListener("keydown", function (event) {
        // Check if the key pressed was the enter key
        if (event.keyCode === 13) {
            event.preventDefault();
            let newName = input.value;
            if (newName !== originalName && newName !== "" && newName !== null) {
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
            // Add the blur event listener when the input is updated
            input.addEventListener("blur", updateTodoListName);
        }
    });

    todoListName.textContent = "";
    todoListName.appendChild(input);
    input.focus();

    // Add the blur event listener when the input is created
    input.addEventListener("blur", updateTodoListName);
}

function updateTodoListName() {
    let todoListName = document.querySelector("#todoListName");
    let originalName = todoListName.textContent;
    let input = document.querySelector("#todoListNameInput");
    let newName = input.value;
    if (newName !== originalName && newName !== "" && newName !== null) {
        let xhr = new XMLHttpRequest();
        xhr.open("POST", "/update_todo_list_name");
        xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        xhr.send(JSON.stringify({ "new_name" : newName }));
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
    input.removeEventListener("blur", updateTodoListName);
}

let todoListNameHeader = document.querySelector("h1");
todoListNameHeader.addEventListener("click", editTodoList);

todoListForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const newName = document.getElementById("todoListNameInput").value;
    fetch("/update_todo_list_name", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({new_name: newName })
    }).then(() => {
        location.reload();
    });
});
