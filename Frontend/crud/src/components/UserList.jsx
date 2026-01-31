import { deleteUser } from "../api/userApi";

function UserList({ users, onEdit, refreshUsers }) {
  const handleDelete = async (id) => {
    await deleteUser(id);
    refreshUsers();
  };

  return (
    <table className="table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Email</th>
          <th>Actions</th>
        </tr>
      </thead>

      <tbody>
        {users.map((user) => (
          <tr key={user.id}>
            <td>{user.id}</td>
            <td>{user.name}</td>
            <td>{user.email}</td>
            <td>
              <button onClick={() => onEdit(user)}>Edit</button>
              <button className="delete" onClick={() => handleDelete(user.id)}>
                Delete
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default UserList;