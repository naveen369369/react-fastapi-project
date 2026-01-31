import { useEffect, useState } from "react";
import { getUsers } from "./api/userApi";
import UserForm from "./components/UserForm";
import UserList from "./components/UserList";
import "./styles/app.css";

function App() {
  const [users, setUsers] = useState([]);
  const [selectedUser, setSelectedUser] = useState(null);

  const fetchUsers = async () => {
    const res = await getUsers();
    setUsers(res.data);
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  return (
    <div className="container">
      <UserForm
        selectedUser={selectedUser}
        refreshUsers={fetchUsers}
        clearSelection={() => setSelectedUser(null)}
      />

      <UserList
        users={users}
        onEdit={setSelectedUser}
        refreshUsers={fetchUsers}
      />
    </div>
  );
}

export default App;