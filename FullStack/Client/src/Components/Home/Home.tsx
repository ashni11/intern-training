import { useNavigate } from "@tanstack/react-router";
import toast from "react-hot-toast";
import { logoutUser } from "../../Service/Auth/Auth.Service";
function Home() {
  const navigate = useNavigate();
  const handleLogout = async () => {
    try {
      const response = await logoutUser();
      if (response.status === 200) {
        localStorage.removeItem("access_token");
        toast.success(response.data.message || "Logout successful");
        navigate({ to: "/signin" });
      } else {
        toast.error(response.data.message || "Logout failed");
      }
    } catch (error: any) {
      console.error(error);
      toast.error(
        error?.response?.data?.detail ||
        error?.response?.data?.message ||
        "Something went wrong while logging out"
      );
    }
  };
  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center px-4">
      <div className="w-full max-w-3xl rounded-2xl bg-white p-10 shadow-lg">
        <h1 className="text-4xl font-bold text-center text-gray-800">
          Full Stack Practice
        </h1>
        <p className="mt-3 text-center text-gray-500">
          Select a page to continue
        </p>
        <div className="mt-10 grid gap-4 sm:grid-cols-2">
          <button
            onClick={() => navigate({ to: "/user-form" })}
            className="rounded-xl bg-blue-600 px-6 py-3 text-white font-semibold shadow hover:bg-blue-700 transition"
          >
            User Form
          </button>
          <button
            onClick={() => navigate({ to: "/signup" })}
            className="rounded-xl bg-green-600 px-6 py-3 text-white font-semibold shadow hover:bg-green-700 transition"
          >
            Sign Up
          </button>
          <button
            onClick={() => navigate({ to: "/signin" })}
            className="rounded-xl bg-purple-600 px-6 py-3 text-white font-semibold shadow hover:bg-purple-700 transition"
          >
            Sign In
          </button>
          <button
            onClick={handleLogout}
            className="rounded-xl bg-red-600 px-6 py-3 text-white font-semibold shadow hover:bg-red-700 transition"
          >
            Logout
          </button>
        </div>
      </div>
    </div>
  );
}

export default Home;