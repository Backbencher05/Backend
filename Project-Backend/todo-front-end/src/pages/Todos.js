import React, { useState, useEffect } from "react";
import axiosInstance from "../api/axios";

const Todos = () => {
  const [todos, setTodos] = useState([]);
  const [title, setTitle] = useState("");
  const [error, setError] = useState("");

  // 📄 Fetch Todos on mount
  useEffect(() => {
    fetchTodos();
  }, []);

  const fetchTodos = async () => {
  try {
    const res = await axiosInstance.get("todos/");
    console.log("Fetched todos:", res.data);  // 🐛 Debug log
    setTodos(res.data);
  } catch (err) {
    setError("Failed to fetch todos");
    console.error(err.response?.data || err.message);
  }
};

  // ➕ Create new task
  const handleAdd = async () => {
    if (!title.trim()) return;
    try {
      const res = await axiosInstance.post("todos/", { title });
      setTodos([...todos, res.data]);
      setTitle("");
    } catch (err) {
      setError("Failed to add todo");
    }
  };

  // ✅ Toggle complete
  const handleToggle = async (todo) => {
    try {
      const res = await axiosInstance.patch(`todos/${todo.id}/`, {
        completed: !todo.completed,
      });
      setTodos(
        todos.map((t) => (t.id === todo.id ? { ...t, completed: res.data.completed } : t))
      );
    } catch (err) {
      setError("Failed to update todo");
    }
  };

  // ❌ Delete task
  const handleDelete = async (id) => {
    try {
      await axiosInstance.delete(`todos/${id}/`);
      setTodos(todos.filter((todo) => todo.id !== id));
    } catch (err) {
      setError("Failed to delete todo");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Your Todo List</h2>

      <input
        type="text"
        value={title}
        placeholder="New Task..."
        onChange={(e) => setTitle(e.target.value)}
      />
      <button onClick={handleAdd}>Add</button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      <ul>
        {todos.map((todo) => (
          <li key={todo.id}>
            <span
              style={{
                textDecoration: todo.completed ? "line-through" : "none",
                cursor: "pointer",
              }}
              onClick={() => handleToggle(todo)}
            >
              {todo.title}
            </span>{" "}
            <button onClick={() => handleDelete(todo.id)}>❌</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Todos;
