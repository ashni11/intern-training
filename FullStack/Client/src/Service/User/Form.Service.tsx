import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

export interface UserPayload {
  name: string;
  phone_number: string;
  email: string;
}

export const getUsers = async () => {
  const response = await axios.get(
    `${BASE_URL}/api/v1/user`
  );
  return response;
};

export const createUser = async (
  payload: UserPayload
) => {
  const response = await axios.post(
    `${BASE_URL}/api/v1/user/create`,
    payload
  );
  return response;
};

export const getUserById = async (
  id: string
) => {
  const response = await axios.get(
    `${BASE_URL}/api/v1/user/${id}`
  );
  return response;
};

export const updateUser = async (
  id: string,
  payload: UserPayload
) => {
  const response = await axios.put(
    `${BASE_URL}/api/v1/user/${id}`,
    payload
  );
  return response;
};

export const deleteUser = async (
  id: string
) => {
  const response = await axios.delete(
    `${BASE_URL}/api/v1/user/${id}`
  );
  return response;
};