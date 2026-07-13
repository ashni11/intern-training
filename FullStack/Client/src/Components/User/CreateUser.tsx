import { useState } from "react";
import { useNavigate } from "@tanstack/react-router";
import toast from "react-hot-toast";

import { createUser } from "../../Service/User/Form.Service";

type UserItem = {
  name: string;
  phone_number: string;
  email: string;
};

function CreateUser() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState<UserItem>({
    name: "",
    phone_number: "",
    email: "",
  });

  const [loading, setLoading] = useState(false);

  function handleChange(
    e: React.ChangeEvent<HTMLInputElement>
  ) {
    const { name, value } = e.target;

    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  }

  async function handleSubmit(
    e: React.FormEvent<HTMLFormElement>
  ) {
    e.preventDefault();

    setLoading(true);

    try {
      const response = await createUser(formData);

      if (response.data.status_code === 201) {
        toast.success(response.data.message);

        setFormData({
          name: "",
          phone_number: "",
          email: "",
        });

        navigate({
          to: "/home",
        });
      } else {
        toast.error(response.data.message);
      }
    } catch (error: any) {
      toast.error(
        error?.response?.data?.message ||
          "Failed to create customer"
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="flex min-h-screen items-center justify-center bg-gray-100">

      <div className="w-full max-w-md rounded-xl bg-white p-8 shadow-lg">

        <h1 className="mb-6 text-center text-3xl font-bold">
          Create Customer
        </h1>

        <form
          onSubmit={handleSubmit}
          className="space-y-5"
        >

          <div>
            <label className="mb-2 block font-medium">
              Name
            </label>

            <input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              placeholder="Enter Name"
              className="w-full rounded-lg border px-4 py-3 outline-none focus:border-blue-500"
              required
            />
          </div>

          <div>
            <label className="mb-2 block font-medium">
              Phone Number
            </label>

            <input
              type="text"
              name="phone_number"
              value={formData.phone_number}
              onChange={handleChange}
              placeholder="Enter Phone Number"
              className="w-full rounded-lg border px-4 py-3 outline-none focus:border-blue-500"
              required
            />
          </div>

          <div>
            <label className="mb-2 block font-medium">
              Email
            </label>

            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              placeholder="Enter Email"
              className="w-full rounded-lg border px-4 py-3 outline-none focus:border-blue-500"
              required
            />
          </div>

          <div className="flex justify-between">

            <button
              type="button"
              onClick={() =>
                navigate({
                  to: "/home",
                })
              }
              className="rounded-lg bg-gray-500 px-6 py-3 text-white"
            >
              Cancel
            </button>

            <button
              type="submit"
              disabled={loading}
              className="rounded-lg bg-blue-600 px-6 py-3 text-white disabled:bg-gray-400"
            >
              {loading ? "Saving..." : "Save"}
            </button>

          </div>

        </form>

      </div>

    </div>
  );
}

export default CreateUser;