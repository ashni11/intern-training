import { useState } from "react";
import { useNavigate } from "@tanstack/react-router";
import toast from "react-hot-toast";
import { signinUser } from "../../Service/Auth/Auth.Service";

type SignInItem = {
  email: string;
  password: string;
};

function SignIn() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState<SignInItem>({
    email: "",
    password: "",
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
      const response = await signinUser(formData);
      if (response.data.status_code === 200) {
        localStorage.setItem(
          "access_token",
          response.data.detail.access_token
        );
        toast.success(response.data.message);
        navigate({
          to: "/home",
        });
      } else {
        toast.error(response.data.message);
      }
    } catch (error: any) {
      toast.error(
        error?.response?.data?.message ||
          "Login Failed"
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="flex min-h-screen items-center justify-center bg-slate-100">

      <div className="w-full max-w-md rounded-xl bg-white p-8 shadow-lg">

        <h1 className="mb-6 text-center text-3xl font-bold">
          Sign In
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
              placeholder="Enter Email"
              className="w-full rounded-lg border px-4 py-3 outline-none focus:border-blue-500"
              required
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
              placeholder="Enter Password"
              className="w-full rounded-lg border px-4 py-3 outline-none focus:border-blue-500"
              required
            />
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full rounded-lg bg-blue-600 py-3 font-semibold text-white hover:bg-blue-700 disabled:bg-gray-400"
          >
            {loading ? "Signing In..." : "Sign In"}
          </button>

          <p className="text-center text-sm">
            Don't have an account?{" "}
            <span
              className="cursor-pointer font-semibold text-blue-600"
              onClick={() =>
                navigate({
                  to: "/signup",
                })
              }
            >
              Sign Up
            </span>
          </p>

        </form>

      </div>

    </div>
  );
}

export default SignIn;