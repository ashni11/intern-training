import { useState } from "react";
import toast from "react-hot-toast";
import { useNavigate } from "@tanstack/react-router";
import { signupUser } from "../../Service/Auth/Auth.Service";

type SignUpFormData = {
  email: string;
  password: string;
};

function SignUp() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState<SignUpFormData>({
    email: "",
    password: "",
  });

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;

    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    try {
      const response = await signupUser(formData);

      if (response.status === 201) {
        toast.success(response.data.message || "User registered successfully");

        setFormData({
          email: "",
          password: "",
        });

        navigate({ to: "/signin" });
      } else {
        toast.error(response.data.message || "Failed to register user");
      }
    } catch (error: any) {
      console.error(error);
      toast.error(
        error?.response?.data?.detail ||
          error?.response?.data?.message ||
          "Something went wrong while signing up"
      );
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 py-10">
      <div className="mx-auto w-full max-w-3xl rounded-xl bg-white p-8 shadow-lg">
        <h1 className="mb-6 text-center text-3xl font-bold text-gray-800">
          Sign Up
        </h1>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="mb-1 block text-sm font-medium text-gray-700">
              Email
            </label>
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              placeholder="Enter email"
              className="w-full rounded-lg border border-gray-300 px-4 py-2 outline-none focus:border-green-500"
            />
          </div>

          <div>
            <label className="mb-1 block text-sm font-medium text-gray-700">
              Password
            </label>
            <input
              type="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              placeholder="Enter password"
              className="w-full rounded-lg border border-gray-300 px-4 py-2 outline-none focus:border-green-500"
            />
          </div>

          <button
            type="submit"
            className="w-full rounded-lg bg-green-600 py-2 font-semibold text-white hover:bg-green-700"
          >
            Sign Up
          </button>
        </form>

        <div className="mt-6 flex flex-wrap gap-3">
          <button
            onClick={() => navigate({ to: "/" })}
            className="rounded-lg bg-gray-600 px-4 py-2 font-medium text-white hover:bg-gray-700"
          >
            Back to Home
          </button>

          <button
            onClick={() => navigate({ to: "/signin" })}
            className="rounded-lg bg-blue-600 px-4 py-2 font-medium text-white hover:bg-blue-700"
          >
            Go to Sign In
          </button>
        </div>
      </div>
    </div>
  );
}

export default SignUp;