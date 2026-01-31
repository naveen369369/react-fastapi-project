import { useState } from "react";
import { createUser, updateUser } from "../api/userApi";

function UserForm({ selectedUser, refreshUsers, clearSelection }) {
  const [name, setName] = useState(selectedUser?.name || "");
  const [email, setEmail] = useState(selectedUser?.email || "");

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (selectedUser) {
      await updateUser(selectedUser.id, name, email);
    } else {
      await createUser(name, email);
    }

    setName("");
    setEmail("");
    refreshUsers();
    clearSelection();
  };

  return (
    <form className="form" onSubmit={handleSubmit}>
      <h2>{selectedUser ? "Update User" : "Create User"}</h2>

      <input
        type="text"
        placeholder="Enter name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        required
      />

      <input
        type="email"
        placeholder="Enter email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
      />

      <button type="submit">
        {selectedUser ? "Update" : "Create"}
      </button>
    </form>
  );
}

export default UserForm;