import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000/api/v1";

export type SignUpPayload = {
  email: string;
  password: string;
};

export type SignInPayload = {
  email: string;
  password: string;
};

export const signupUser = async (payload: SignUpPayload) => {
  return await axios.post(`${API_BASE_URL}/signup`, payload);
};

export const signinUser = async (payload: SignInPayload) => {
  return await axios.post(`${API_BASE_URL}/signin`, payload);
};