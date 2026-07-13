import { useState } from "react";
import { useNavigate } from "@tanstack/react-router";
import toast from "react-hot-toast";
import { signupUser } from "../../Service/Auth/Auth.Service";

type SignUpItem = {
  email: string;
  password: string;
};

function SignUp() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState<SignUpItem>({
    email: "",
    password: "",
  });

  function handleChange(e: React.ChangeEvent<HTMLInputElement>) {
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

    try {
      const response = await signupUser(formData);
      if (response.data.status_code === 201) {
        toast.success(response.data.message);
        setFormData({
          email: "",
          password: "",
        });
        navigate({ to: "/" });
      } else {
        toast.error(response.data.message);
      }
    } catch (error: any) {
      toast.error(
        error?.response?.data?.message ||
          "Something went wrong"
      );
    }
  }

  return (
    <div className="flex min-h-screen items-center justify-center bg-gray-100">
      <div className="w-full max-w-md rounded-xl bg-white p-8 shadow-lg">

        <h1 className="mb-6 text-center text-3xl font-bold">
          Sign Up
        </h1>
        <form
          onSubmit={handleSubmit}
          className="space-y-5"
        >
          <div>
            <label className="mb-2 block font-medium">
              Email
            </label>
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              placeholder="Enter email"
              className="w-full rounded-lg border p-3 outline-none focus:border-blue-500"
            />
          </div>
          <div>
            <label className="mb-2 block font-medium">
              Password
            </label>
            <input
              type="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              placeholder="Enter password"
              className="w-full rounded-lg border p-3 outline-none focus:border-blue-500"
            />
          </div>
          <button
            type="submit"
            className="w-full rounded-lg bg-blue-600 py-3 font-semibold text-white hover:bg-blue-700"
          >
            Sign Up
          </button>
        </form>

      </div>

    </div>
  );
}

export default SignUp;