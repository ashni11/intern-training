import { RouterProvider } from "@tanstack/react-router";
import { router } from "./Routes/Routes";
import { Toaster } from "react-hot-toast";

function App() {
  return (
    <>
      <RouterProvider router={router} />
      <Toaster position="top-right" />
    </>
  );
}

export default App;