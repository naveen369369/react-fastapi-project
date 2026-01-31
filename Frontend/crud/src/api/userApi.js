import axios from "axios";

const API_URL = "https://react-fastapi-project-3.onrender.com"; // FastAPI base URL

export const getUsers = () => {
  return axios.get(`${API_URL}/view`);
};

export const createUser = (name, email) => {
  return axios.post(`${API_URL}/create`, null, {
    params: { name, email },
  });
};

export const updateUser = (id, name, email) => {
  return axios.put(`${API_URL}/update/${id}`, null, {
    params: { name, email },
  });
};

export const deleteUser = (id) => {
  return axios.delete(`${API_URL}/delete/${id}`);
};