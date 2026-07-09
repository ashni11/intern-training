import { useNavigate } from "@tanstack/react-router";

function Home() {
  const navigate = useNavigate();
  function handleGoToForm() {
    navigate({ to: "/user-form" });
  }

  return (
    <div className="flex min-h-screen items-center justify-center bg-gray-100">
      <div className="rounded-xl bg-white p-10 shadow-lg text-center w-[400px]">
        <h1 className="mb-4 text-3xl font-bold text-gray-800">
          User Form Project
        </h1>

        <p className="mb-6 text-gray-600">
          Click below to go to the User Form page
        </p>

        <button
          onClick={handleGoToForm}
          className="rounded-lg bg-blue-600 px-6 py-3 text-white hover:bg-blue-700"
        >
          Go to User Form
        </button>
      </div>
    </div>
  );
}

export default Home;