import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

export interface UserPayload {
  username: string;
  dob: string;
  phoneNumber: string;
}
export const createUser = async (payload: UserPayload) => {
  const response = await axios.post(`${BASE_URL}/api/v1/createform`, payload);
  return response.data;
};