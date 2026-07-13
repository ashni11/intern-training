import { useEffect, useState } from "react";
import { useNavigate } from "@tanstack/react-router";
import toast from "react-hot-toast";

import {
  FiBell,
  FiMoon,
  FiSun,
  FiLogOut,
  FiEdit,
  FiPlus,
} from "react-icons/fi";

import { MdDelete } from "react-icons/md";

import {
  getUsers,
  deleteUser,
} from "../../Service/User/Form.Service";

type UserItem = {
  id: string;
  name: string;
  phone_number: string;
  email: string;
};

function Home() {
  const navigate = useNavigate();
  const [users, setUsers] = useState<UserItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [darkMode, setDarkMode] = useState(
    localStorage.getItem("theme") === "dark"
  );
const [notificationCount, setNotificationCount] = useState(0);
const [deleteId, setDeleteId] = useState("");

  useEffect(() => {
    fetchUsers();
  }, []);

  useEffect(() => {
    localStorage.setItem(
      "theme",
      darkMode ? "dark" : "light"
    );
  }, [darkMode]);

 useEffect(() => {
    const eventSource = new EventSource(
        "http://127.0.0.1:8000/api/v1/user/events"
    );
    eventSource.onmessage = (event) => {
        setNotificationCount(Number(event.data));
        fetchUsers();
    };
    return () => eventSource.close();
}, []);
  async function fetchUsers() {
    try {
      setLoading(true);
      const response = await getUsers();
      if (response.data.status_code === 200) {
        setUsers(response.data.detail);
      }
    } catch {
      toast.error("Failed to fetch customers");
    } finally {
      setLoading(false);
    }
  }

  async function handleDelete(id: string) {
    try {
      const response = await deleteUser(id);

      if (response.data.status_code === 200) {
        toast.success(response.data.message);
        fetchUsers();
      } else {
        toast.error(response.data.message);
      }
    } catch (error: any) {
      toast.error(
        error?.response?.data?.message ??
          "Delete Failed"
      );
    }
  }

  function handleLogout() {
    localStorage.removeItem("access_token");
    toast.success("Logout Successful");
    navigate({
      to: "/",
    });
  }

  return (
    <div
      className={`min-h-screen transition-all duration-300 ${
        darkMode
          ? "bg-gray-900 text-white"
          : "bg-gray-100 text-black"
      }`}
    >
      <div className="mx-auto max-w-7xl p-8">

        {/* Top Header */}

        <div className="mb-8 flex items-center justify-end gap-4">

          <button
            onClick={() => setDarkMode(!darkMode)}
            className="rounded-full bg-blue-600 p-3 text-white"
          >
            {darkMode ? (
              <FiSun size={22} />
            ) : (
              <FiMoon size={22} />
            )}
          </button>

          <div className="relative">

  <div className="relative">

    <button className="relative rounded-full bg-green-600 p-3 text-white">

        <FiBell size={22} />

        {notificationCount > 0 && (

            <span
                className="absolute -top-1 -right-1 flex h-5 w-5 items-center justify-center rounded-full bg-red-600 text-xs font-bold"
            >
                {notificationCount}
            </span>

        )}

    </button>

</div>

</div>

          <button
            onClick={handleLogout}
            className="flex items-center gap-2 rounded bg-red-600 px-4 py-2 text-white"
          >
            <FiLogOut />
            Logout
          </button>

        </div>

        {/* Title */}

        <div className="mb-8 flex items-center justify-between">

          <h1 className="text-4xl font-bold">
            Customer List
          </h1>

          <button
            onClick={() =>
              navigate({
                to: "/create",
              })
            }
            className="flex items-center gap-2 rounded-lg bg-blue-600 px-5 py-3 text-white hover:bg-blue-700"
          >
            <FiPlus />
            Create
          </button>

        </div>

        {/* Table */}

        <div
          className={`overflow-hidden rounded-xl shadow-lg ${
            darkMode
              ? "bg-gray-800"
              : "bg-white"
          }`}
        >
          <table className="w-full">

            <thead
              className={
                darkMode
                  ? "bg-gray-700"
                  : "bg-blue-600 text-white"
              }
            >
              <tr>
                <th className="p-4">S.No</th>
                <th className="p-4">
                  Customer Name
                </th>
                <th className="p-4">
                  Phone Number
                </th>
                <th className="p-4">
                  Email
                </th>
                <th className="p-4">
                  Action
                </th>
              </tr>
            </thead>

            <tbody>

              {loading ? (
                <tr>
                  <td
                    colSpan={5}
                    className="py-8 text-center"
                  >
                    Loading Customers...
                  </td>
                </tr>
              ) : users.length === 0 ? (
                <tr>
                  <td
                    colSpan={5}
                    className="py-8 text-center"
                  >
                    No Customers Found
                  </td>
                </tr>
              ) : (
                users.map((user, index) => (
                  <tr
                    key={user.id}
                    className={`border-b ${
                      darkMode
                        ? "border-gray-700 hover:bg-gray-700"
                        : "hover:bg-gray-100"
                    }`}
                  >
                    <td className="p-4">
                      {index + 1}
                    </td>

                    <td className="p-4">
                      {user.name}
                    </td>

                    <td className="p-4">
                      {user.phone_number}
                    </td>

                    <td className="p-4">
                      {user.email}
                    </td>

                    <td className="p-4">
                      <div className="flex gap-3">

                        <button
                          onClick={() =>
                            navigate({
                              to: "/edit/$id",
                              params: {
                                id: user.id,
                              },
                            })
                          }
                          className="rounded bg-green-600 p-2 text-white hover:bg-green-700"
                        >
                          <FiEdit />
                        </button>

                        <button
                          onClick={() =>
                            setDeleteId(user.id)
                          }
                          className="rounded bg-red-600 p-2 text-white hover:bg-red-700"
                        >
                          <MdDelete />
                        </button>

                      </div>
                    </td>

                  </tr>
                ))
              )}

            </tbody>

          </table>
        </div>

        {/* Delete Modal */}

        {deleteId && (
          <div className="fixed inset-0 flex items-center justify-center bg-black/50">

            <div
              className={`w-96 rounded-xl p-6 ${
                darkMode
                  ? "bg-gray-800 text-white"
                  : "bg-white"
              }`}
            >
              <h2 className="mb-4 text-2xl font-bold">
                Delete Customer
              </h2>

              <p className="mb-6">
                Are you sure you want to delete
                this customer?
              </p>

              <div className="flex justify-end gap-3">

                <button
                  onClick={() =>
                    setDeleteId("")
                  }
                  className="rounded bg-gray-500 px-4 py-2 text-white"
                >
                  No
                </button>

                <button
                  onClick={async () => {
                    await handleDelete(
                      deleteId
                    );
                    setDeleteId("");
                  }}
                  className="rounded bg-red-600 px-4 py-2 text-white"
                >
                  Yes
                </button>

              </div>

            </div>

          </div>
        )}

      </div>
    </div>
  );
}

export default Home;