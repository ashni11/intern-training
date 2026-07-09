import { useEffect, useState } from "react";
import { createUser } from "../../Service/User/Form.Service";
import toast from "react-hot-toast";

type UserItem = {
  username: string;
  dob: string;
  phoneNumber: string;
};
function UserForm() {
  const [formData, setFormData] = useState<UserItem>({
    username: "",
    dob: "",
    phoneNumber: "",
  });
  const [users, setUsers] = useState<UserItem[]>([]);

  useEffect(() => {
    console.log("UserForm component mounted");
  }, []);

  function handleChange(e: React.ChangeEvent<HTMLInputElement>) {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  }
  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
  e.preventDefault();

  try {
    const response = await createUser(formData);

    if (response.status === 201) {
      toast.success(response.data.message || "User created successfully");

      setUsers((prev) => [...prev, formData]);

      setFormData({
        username: "",
        dob: "",
        phoneNumber: "",
      });
    } else {
      toast.error(response.data.message || "Failed to create user");
    }
  } catch (error) {
    console.error(error);
    toast.error("Something went wrong while creating user");
  }
}
  return (
    <div className="min-h-screen bg-gray-100 py-10">
      {/* Form Card */}
      <div className="mx-auto w-full max-w-3xl rounded-xl bg-white p-8 shadow-lg">
        <h1 className="mb-6 text-center text-3xl font-bold text-gray-800">
          User Form
        </h1>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="mb-1 block text-sm font-medium text-gray-700">
              Username
            </label>
            <input
              type="text"
              name="username"
              value={formData.username}
              onChange={handleChange}
              placeholder="Enter username"
              className="w-full rounded-lg border border-gray-300 px-4 py-2 outline-none focus:border-blue-500"
            />
          </div>

          <div>
            <label className="mb-1 block text-sm font-medium text-gray-700">
              Date of Birth
            </label>
            <input
              type="date"
              name="dob"
              value={formData.dob}
              onChange={handleChange}
              className="w-full rounded-lg border border-gray-300 px-4 py-2 outline-none focus:border-blue-500"
            />
          </div>
          <div>
            <label className="mb-1 block text-sm font-medium text-gray-700">
              Phone Number
            </label>
            <input
              type="text"
              name="phoneNumber"
              value={formData.phoneNumber}
              onChange={handleChange}
              placeholder="Enter phone number"
              className="w-full rounded-lg border border-gray-300 px-4 py-2 outline-none focus:border-blue-500"
            />
          </div>

          <button
            type="submit"
            className="w-full rounded-lg bg-blue-600 py-2 font-semibold text-white hover:bg-blue-700"
          >
            Submit
          </button>
        </form>
      </div>

      {/* Submitted Users Table */}
      <div className="mx-auto mt-8 w-full max-w-5xl rounded-xl bg-white p-6 shadow-lg">
        <h2 className="mb-4 text-2xl font-semibold text-gray-800">
          Submitted Users
        </h2>

        {users.length === 0 ? (
          <p className="text-gray-500">No users submitted yet.</p>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full border-collapse overflow-hidden rounded-lg">
              <thead>
                <tr className="bg-blue-600 text-white">
                  <th className="border px-4 py-3 text-left">S.No</th>
                  <th className="border px-4 py-3 text-left">Username</th>
                  <th className="border px-4 py-3 text-left">Phone Number</th>
                  <th className="border px-4 py-3 text-left">DOB</th>
                </tr>
              </thead>

              <tbody>
                {users.map((user, index) => (
                  <tr key={index} className="hover:bg-gray-50">
                    <td className="border px-4 py-3">{index + 1}</td>
                    <td className="border px-4 py-3">{user.username}</td>
                    <td className="border px-4 py-3">{user.phoneNumber}</td>
                    <td className="border px-4 py-3">{user.dob}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
}
export default UserForm;