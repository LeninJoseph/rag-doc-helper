# JavaScript CRUD Operations Example Using Fetch

Below is an example of how to perform CRUD operations in JavaScript using the `fetch` API. These examples assume you have a RESTful API endpoint at `https://api.example.com/users`.

```javascript
const API_URL = "https://api.example.com/users";

// CREATE
async function createUser(user) {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(user),
  });
  return response.json();
}

// READ (Get all users)
async function getUsers() {
  const response = await fetch(API_URL);
  return response.json();
}

// READ (Get user by ID)
async function getUser(id) {
  const response = await fetch(`${API_URL}/${id}`);
  return response.json();
}

// UPDATE
async function updateUser(id, newData) {
  const response = await fetch(`${API_URL}/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(newData),
  });
  return response.json();
}

// DELETE
async function deleteUser(id) {
  const response = await fetch(`${API_URL}/${id}`, {
    method: "DELETE",
  });
  return response.ok;
}

// Usage examples:
(async () => {
  await createUser({ name: "Charlie" });
  const users = await getUsers();
  console.log(users);

  const user = await getUser(2);
  console.log(user);

  await updateUser(1, { name: "Alicia" });
  await deleteUser(2);
})();
```
