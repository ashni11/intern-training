import axios from "axios";

const API_URL = "http://localhost:8000/api/v1/users";

type UserData = {
  username: string;
  dob: string;
  phoneNumber: string;
};

export const createUser = async (data: UserData) => {
  return await axios.post(API_URL, data);
};